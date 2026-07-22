from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import sqlite3
from threading import Event, Lock
from typing import Any

import pytest

from adapters.pingting import client as pingting_module
from adapters.pingting.client import PingTingAdapter, PingTingStatusSnapshot


def _adapter(tmp_path: Path) -> PingTingAdapter:
    return PingTingAdapter(
        repo_path=tmp_path,
        status_path=tmp_path / "data" / "status.json",
        config_path=tmp_path / "config" / "pingting.yaml",
        command_timeout_seconds=2,
    )


def test_sqlite_queries_use_read_only_uri_and_apply_filters(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    db_path = tmp_path / "data" / "pingting.db"
    db_path.parent.mkdir()
    connection = sqlite3.connect(db_path)
    connection.executescript(
        """
        CREATE TABLE findings (
          id INTEGER, created_at TEXT, severity TEXT, agent TEXT, title TEXT,
          description TEXT, device_ip TEXT, device_mac TEXT, acknowledged INTEGER,
          false_positive INTEGER, during_learning INTEGER
        );
        INSERT INTO findings VALUES
          (1, '2026-01-01', 'high', 'network', 'real', '', '', '', 0, 0, 0),
          (2, '2026-01-02', 'high', 'network', 'false positive', '', '', '', 0, 1, 0);
        CREATE TABLE agent_runs (
          id INTEGER, agent TEXT, started_at TEXT, completed_at TEXT, status TEXT,
          findings_count INTEGER, raw_data_summary TEXT, error_message TEXT
        );
        INSERT INTO agent_runs VALUES
          (1, 'network', '2026-01-01', '2026-01-01', 'complete', 1, '{}', '');
        """
    )
    connection.commit()
    connection.close()

    real_connect = sqlite3.connect
    connect_calls: list[tuple[Any, dict[str, Any]]] = []

    def tracking_connect(database: Any, *args: Any, **kwargs: Any) -> sqlite3.Connection:
        connect_calls.append((database, kwargs))
        return real_connect(database, *args, **kwargs)

    monkeypatch.setattr(pingting_module.sqlite3, "connect", tracking_connect)
    adapter = _adapter(tmp_path)
    payload = adapter.load_recent_findings(severity="high")
    runs = adapter.load_recent_agent_runs(agent="network", status="complete")

    assert payload["ok"] is True
    assert [finding["title"] for finding in payload["findings"]] == ["real"]
    assert runs["ok"] is True
    assert [run["agent"] for run in runs["runs"]] == ["network"]
    assert len(connect_calls) == 2
    for database, kwargs in connect_calls:
        assert str(database).startswith("file:")
        assert str(database).endswith("?mode=ro")
        assert kwargs["uri"] is True


def test_cli_status_refresh_is_single_flight(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    adapter = _adapter(tmp_path)
    started = Event()
    release = Event()
    count_lock = Lock()
    calls = 0

    def fake_execute() -> PingTingStatusSnapshot:
        nonlocal calls
        with count_lock:
            calls += 1
        started.set()
        assert release.wait(timeout=2)
        return PingTingStatusSnapshot(payload={"ok": True}, source="cli", age_seconds=0.0)

    monkeypatch.setattr(adapter, "_execute_status_cli", fake_execute)
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(adapter._run_status_cli) for _ in range(8)]
        assert started.wait(timeout=1)
        release.set()
        snapshots = [future.result(timeout=2) for future in futures]

    assert calls == 1
    assert all(snapshot.payload == {"ok": True} for snapshot in snapshots)
