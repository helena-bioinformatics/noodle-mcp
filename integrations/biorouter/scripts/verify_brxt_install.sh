#!/usr/bin/env bash
set -euo pipefail

integration_dir="$(cd "$(dirname "$0")/.." && pwd)"
bundle="${1:-$integration_dir/dist/noodle-biomedical-literature-discovery-mcp.brxt}"
install_dir="$(mktemp -d "${TMPDIR:-/tmp}/noodle-biorouter-install.XXXXXX")"
trap 'rm -rf "$install_dir"' EXIT

python3 - "$bundle" "$install_dir" <<'PY'
import sys
import zipfile

with zipfile.ZipFile(sys.argv[1]) as archive:
    archive.extractall(sys.argv[2])
PY

uv sync --frozen --directory "$install_dir"
uv run --frozen --directory "$install_dir" python - <<'PY'
import json
from noodle_biorouter import __version__
from noodle_biorouter.server import ENDPOINT, SERVER_NAME

assert __version__ == "0.2.0"
assert SERVER_NAME == "Noodle Biomedical Literature Discovery MCP"
assert ENDPOINT == "https://api.helena.bio/noodle/v1/mcp"
print(json.dumps({"installed": True, "version": __version__, "server": SERVER_NAME}))
PY
