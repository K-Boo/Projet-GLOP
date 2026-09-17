#!/usr/bin/env bash
# Token Tracker Live - FinOps ShopLoc (macOS / Linux)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
cd "${REPO_ROOT}"

if [ -f "${REPO_ROOT}/venv/bin/python3" ]; then
    "${REPO_ROOT}/venv/bin/python3" "${SCRIPT_DIR}/token_tracker.py" --watch
elif command -v python3 >/dev/null 2>&1; then
    python3 "${SCRIPT_DIR}/token_tracker.py" --watch
elif command -v python >/dev/null 2>&1; then
    python "${SCRIPT_DIR}/token_tracker.py" --watch
else
    echo "[ERREUR] Python introuvable sur cette machine."
    exit 1
fi
