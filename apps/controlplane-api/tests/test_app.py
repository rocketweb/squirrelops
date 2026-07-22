from __future__ import annotations

import asyncio
import base64
from threading import Event
from typing import Any

from fastapi.testclient import TestClient
import pytest
from starlette.websockets import WebSocketDisconnect

from adapters.clownpeanuts import ClownPeanutsAdapter
from controlplane_api import app as app_module
from controlplane_api.app import create_app


def _ws_auth_protocol(token: str) -> str:
    encoded = base64.urlsafe_b64encode(token.encode("utf-8")).decode("ascii").rstrip("=")
    return f"cp-auth.{encoded}"


def test_http_auth_fails_closed_and_rejects_query_tokens(settings_factory: Any) -> None:
    settings = settings_factory()
    client = TestClient(create_app(settings))

    assert client.get("/health").status_code == 200
    assert client.get("/orchestration/summary").status_code == 401
    assert client.get(f"/orchestration/summary?token={settings.api_auth_token}").status_code == 401
    assert client.get(
        "/orchestration/summary",
        headers={"Authorization": f"Bearer {settings.api_auth_token}"},
    ).status_code == 200

    unconfigured = TestClient(create_app(settings_factory(api_auth_token="")))
    response = unconfigured.get("/orchestration/summary")
    assert response.status_code == 503
    assert "not configured" in response.json()["detail"]


def test_websocket_relay_closes_idle_upstream_and_keeps_tokens_out_of_urls(
    settings_factory: Any,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    upstream_exited = Event()
    connection_args: dict[str, Any] = {}

    class FakeUpstream:
        async def recv(self) -> str:
            await asyncio.Event().wait()
            raise AssertionError("unreachable")

        async def send(self, _message: str | bytes) -> None:
            return None

    class FakeConnection:
        async def __aenter__(self) -> FakeUpstream:
            return FakeUpstream()

        async def __aexit__(self, *_args: Any) -> None:
            upstream_exited.set()

    def fake_connect(url: str, **kwargs: Any) -> FakeConnection:
        connection_args["url"] = url
        connection_args.update(kwargs)
        return FakeConnection()

    monkeypatch.setattr(app_module.websockets, "connect", fake_connect)
    upstream_token = "upstream-websocket-token-0123456789"
    settings = settings_factory(clownpeanuts_ws_token=upstream_token)
    client = TestClient(create_app(settings))

    with client.websocket_connect(
        "/deception/ws/events",
        subprotocols=["cp-events-v1", _ws_auth_protocol(settings.api_auth_token)],
    ) as websocket:
        assert websocket.accepted_subprotocol == "cp-events-v1"

    assert upstream_exited.wait(timeout=1)
    assert connection_args["url"] == settings.clownpeanuts_ws_events_url
    assert "token=" not in connection_args["url"]
    assert connection_args["additional_headers"] == {
        "Authorization": f"Bearer {upstream_token}"
    }


def test_websocket_query_token_is_rejected(settings_factory: Any) -> None:
    settings = settings_factory()
    client = TestClient(create_app(settings))

    with pytest.raises(WebSocketDisconnect) as exc:
        with client.websocket_connect(
            f"/deception/ws/events?token={settings.api_auth_token}"
        ):
            pass
    assert exc.value.code == 4401


def test_deception_proxy_only_returns_allowlisted_headers(
    settings_factory: Any,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    async def fake_proxy(self: ClownPeanutsAdapter, **_kwargs: Any) -> tuple[int, dict[str, str], bytes]:
        return 200, {
            "content-type": "application/json",
            "set-cookie": "upstream-secret=bad",
            "www-authenticate": "Bearer upstream",
        }, b'{"ok":true}'

    monkeypatch.setattr(ClownPeanutsAdapter, "proxy", fake_proxy)
    settings = settings_factory()
    client = TestClient(create_app(settings))
    response = client.get(
        "/deception/status",
        headers={"Authorization": f"Bearer {settings.api_auth_token}"},
    )

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert "set-cookie" not in response.headers
    assert "www-authenticate" not in response.headers
    assert client.options("/deception/status").status_code == 405
