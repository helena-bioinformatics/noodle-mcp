#!/usr/bin/env python3
"""Read-only Noodle discovery contract gate and post-activation probe."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "registry" / "discovery-contract.json"


def fetch(url: str, *, timeout: float) -> dict[str, object]:
    request = Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "Helena-Noodle-Discovery-Reconciler/1.0",
        },
    )
    try:
        with urlopen(request, timeout=timeout) as response:  # noqa: S310 - contract-bound HTTPS URLs
            return json.load(response)
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"public probe failed: {type(exc).__name__}") from exc


def validate(contract: dict[str, object]) -> list[str]:
    errors: list[str] = []
    if contract.get("protocolVersion") != "2026-07-28":
        errors.append("protocolVersion must be 2026-07-28")
    if contract.get("registryName") != "io.github.helena-bioinformatics/noodle":
        errors.append("registryName drift")
    if contract.get("endpoint") != "https://api.helena.bio/noodle/v1/mcp":
        errors.append("endpoint drift")
    if contract.get("lifecycle") not in {"source_candidate", "active"}:
        errors.append("invalid lifecycle")
    values = contract.get("tools")
    if (
        not isinstance(values, list)
        or len(values) != 7
        or len(values) != len(set(values))
    ):
        errors.append("tools must contain seven unique names")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--probe-active", action="store_true")
    parser.add_argument("--timeout", type=float, default=5.0)
    args = parser.parse_args()
    contract = json.loads(CONTRACT.read_text(encoding="ascii"))
    errors = validate(contract)
    if args.probe_active:
        if contract["lifecycle"] != "active":
            errors.append("refusing public probes before lifecycle=active")
        else:
            health = fetch(str(contract["health"]), timeout=args.timeout)
            readiness = fetch(str(contract["readiness"]), timeout=args.timeout)
            if health.get("status") != "healthy":
                errors.append("health is not healthy")
            if readiness.get("status") != "ready":
                errors.append("readiness is not ready")
    print(
        json.dumps(
            {
                "status": "failed" if errors else "in_sync",
                "lifecycle": contract.get("lifecycle"),
                "errors": errors,
            },
            sort_keys=True,
        )
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
