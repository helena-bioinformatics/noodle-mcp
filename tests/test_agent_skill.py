from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills/noodle-biomedical-literature-discovery"


def _frontmatter(text: str) -> dict[str, str]:
    parts = text.split("---", 2)
    assert len(parts) == 3 and not parts[0].strip()
    return yaml.safe_load(parts[1])


def test_agent_skill_has_task_selection_metadata() -> None:
    text = (SKILL_DIR / "SKILL.md").read_text()
    metadata = _frontmatter(text)
    assert metadata.keys() == {"name", "description"}
    assert metadata["name"] == "noodle-biomedical-literature-discovery"
    for trigger in ("PMID", "DOI", "PMCID", "related papers", "citation", "semantic"):
        assert trigger in metadata["description"]
    assert "does not mention Noodle" in metadata["description"]


def test_agent_skill_preserves_routes_outcomes_and_safety() -> None:
    text = (SKILL_DIR / "SKILL.md").read_text()
    for tool in (
        "search_biomedical_literature",
        "get_publication_details",
        "get_work_details",
        "get_publication_neighborhood",
        "get_work_neighborhood",
        "get_corpus_summary",
    ):
        assert f"`{tool}`" in text
    for outcome in (
        "publication_not_found",
        "work_not_found",
        "neighborhood_not_found",
        "invalid_arguments",
        "upstream_timeout",
        "upstream_unavailable",
        "upstream_rate_limited",
        "invalid_upstream_response",
        "internal_failure",
    ):
        assert f"`{outcome}`" in text
    assert "Never send patient" in text
    assert "do not establish causality" in text
    assert "https://api.helena.bio/noodle/v1/mcp" in text


def test_openai_metadata_declares_hosted_dependency() -> None:
    metadata = yaml.safe_load((SKILL_DIR / "agents/openai.yaml").read_text())
    assert metadata["policy"]["allow_implicit_invocation"] is True
    dependency = metadata["dependencies"]["tools"][0]
    assert dependency["type"] == "mcp"
    assert dependency["transport"] == "streamable_http"
    assert dependency["value"] == "io.github.helena-bioinformatics/noodle"
    assert dependency["url"] == "https://api.helena.bio/noodle/v1/mcp"
