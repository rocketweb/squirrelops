#!/bin/sh
set -eu

APP_USER="appuser"
APP_GROUP="appgroup"
REPO_PATH="${PINGTING_REPO_PATH:-/workspace/pingting}"

if [ "$(id -u)" -ne 0 ]; then
  exec "$@"
fi

if [ ! -d "${REPO_PATH}" ]; then
  echo "control-plane entrypoint: PingTing repo is not mounted at ${REPO_PATH}" >&2
  exit 78
fi

REPO_UID="$(stat -c '%u' "${REPO_PATH}")"
REPO_GID="$(stat -c '%g' "${REPO_PATH}")"

case "${REPO_UID}:${REPO_GID}" in
  *[!0-9:]*|:*|*:)
    echo "control-plane entrypoint: invalid PingTing ownership ${REPO_UID}:${REPO_GID}" >&2
    exit 78
    ;;
esac

if [ "${REPO_UID}" -eq 0 ]; then
  echo "control-plane entrypoint: refusing to run the API as root for a root-owned PingTing mount" >&2
  exit 78
fi

CURRENT_UID="$(id -u "${APP_USER}")"
CURRENT_GID="$(id -g "${APP_USER}")"
if [ "${CURRENT_GID}" -ne "${REPO_GID}" ]; then
  groupmod --non-unique --gid "${REPO_GID}" "${APP_GROUP}"
fi
if [ "${CURRENT_UID}" -ne "${REPO_UID}" ]; then
  usermod --non-unique --uid "${REPO_UID}" --gid "${APP_GROUP}" "${APP_USER}"
fi

chown -R "${APP_USER}:${APP_GROUP}" /opt/controlplane

STATUS_PATH="${PINGTING_STATUS_PATH:-${REPO_PATH}/data/status.json}"
CONFIG_PATH="${PINGTING_CONFIG_PATH:-${REPO_PATH}/config/pingting.yaml}"
if [ -e "${STATUS_PATH}" ] && ! gosu "${APP_USER}" test -r "${STATUS_PATH}"; then
  echo "control-plane entrypoint: ${STATUS_PATH} is not readable by the runtime user" >&2
  exit 78
fi
if ! gosu "${APP_USER}" test -r "${CONFIG_PATH}"; then
  echo "control-plane entrypoint: PingTing config is not readable at ${CONFIG_PATH}" >&2
  exit 78
fi
if [ -d "${REPO_PATH}/data" ] && ! gosu "${APP_USER}" test -w "${REPO_PATH}/data"; then
  echo "control-plane entrypoint: ${REPO_PATH}/data is not writable for SQLite WAL access" >&2
  exit 78
fi
if [ -d "${REPO_PATH}/logs" ] && ! gosu "${APP_USER}" test -w "${REPO_PATH}/logs"; then
  echo "control-plane entrypoint: ${REPO_PATH}/logs is not writable for PingTing CLI logging" >&2
  exit 78
fi

exec gosu "${APP_USER}" "$@"
