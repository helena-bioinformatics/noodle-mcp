from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_public_tree_excludes_private_runtime_topology() -> None:
    assert not (ROOT / "src/noodle_mcp_service").exists()
    assert not (ROOT / "ops/production-compose.yaml").exists()
    assert not (ROOT / "Dockerfile.adapter").exists()
    forbidden = (
        "/root/",
        "folklore-mcp:9017",
        "literature-mining:9004",
        "X-Internal-Secret",
        "PRIVATE KEY",
    )
    for path in ROOT.rglob("*"):
        if (
            not path.is_file()
            or {".git", ".ruff_cache", ".pytest_cache"} & set(path.parts)
            or path.suffix == ".pyc"
        ):
            continue
        if path.name in {"test_public_source_boundary.py", "test_distribution.py"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for marker in forbidden:
            assert marker not in text, f"private marker {marker!r} in {path}"


def test_public_repo_contains_every_discovery_layer() -> None:
    required = (
        "registry/server.json",
        "registry/discovery-contract.json",
        "registry/agent-selection.json",
        "registry/agent-selection.schema.json",
        "skills/noodle-biomedical-literature-discovery/SKILL.md",
        "skills/noodle-biomedical-literature-discovery/agents/openai.yaml",
        "benchmarks/agent-discovery/cases.csv",
        "integrations/biomni/mcp_config.yaml",
        "integrations/biorouter/manifest.json",
        ".github/workflows/publish-official-mcp-registry.yml",
        ".github/workflows/publish-mcpcentral.yml",
        ".github/workflows/publish-biorouter-brxt.yml",
        ".zenodo.json",
        "CITATION.cff",
        "glama.json",
    )
    for relative in required:
        assert (ROOT / relative).is_file(), relative
