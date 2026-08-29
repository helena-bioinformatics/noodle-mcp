#!/usr/bin/env python3
"""Build a deterministic Noodle agent-skill archive and checksum."""

from __future__ import annotations

import argparse
import hashlib
import zipfile
from pathlib import Path

SKILL_NAME = "noodle-biomedical-literature-discovery"
FIXED_TIMESTAMP = (2026, 1, 1, 0, 0, 0)
FILE_MODE = 0o100644 << 16


def build(output: Path) -> str:
    root = Path(__file__).resolve().parents[1]
    skill = root / "skills" / SKILL_NAME
    files = [skill / "SKILL.md", skill / "agents/openai.yaml"]
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(
        output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for path in files:
            name = f"{SKILL_NAME}/{path.relative_to(skill).as_posix()}"
            info = zipfile.ZipInfo(name, FIXED_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = FILE_MODE
            info.create_system = 3
            archive.writestr(info, path.read_bytes(), compresslevel=9)
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    output.with_suffix(output.suffix + ".sha256").write_text(
        f"{digest}  {output.name}\n", encoding="ascii"
    )
    return digest


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output", type=Path, default=root / "dist" / f"{SKILL_NAME}.zip"
    )
    args = parser.parse_args()
    print(build(args.output.resolve()))


if __name__ == "__main__":
    main()
