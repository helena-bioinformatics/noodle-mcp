import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_active_contract_reconciles_offline() -> None:
    script = ROOT / "ops/reconcile_discovery.py"
    offline = subprocess.run(
        [sys.executable, str(script)], check=False, capture_output=True, text=True
    )
    assert offline.returncode == 0
    result = json.loads(offline.stdout)
    assert result["status"] == "in_sync"
    assert result["lifecycle"] == "active"
