import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_active_distribution_identity_is_exact() -> None:
    contract = json.loads(
        (ROOT / "registry/discovery-contract.json").read_text(encoding="ascii")
    )
    server = json.loads((ROOT / "registry/server.json").read_text(encoding="ascii"))
    package = json.loads(
        (ROOT / "registry/packages/noodle/.mcp.json").read_text(encoding="ascii")
    )
    assert contract["lifecycle"] == "active"
    assert (
        server["name"]
        == contract["registryName"]
        == "io.github.helena-bioinformatics/noodle"
    )
    assert server["version"] == contract["version"] == "0.2.1"
    assert server["repository"] == {
        "url": "https://github.com/helena-bioinformatics/noodle-mcp",
        "source": "github",
        "id": "1350901429",
    }
    assert server["remotes"][0]["url"] == contract["endpoint"]
    assert package["mcpServers"]["noodle"]["url"] == contract["endpoint"]


def test_agent_plugin_and_kiro_power_preserve_canonical_identity() -> None:
    contract = json.loads(
        (ROOT / "registry/discovery-contract.json").read_text(encoding="ascii")
    )
    plugin = json.loads((ROOT / "plugin.json").read_text(encoding="ascii"))
    power = json.loads((ROOT / "mcp.json").read_text(encoding="ascii"))

    assert plugin["$schema"] == (
        "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
    )
    assert plugin["name"] == "noodle-biomedical-literature-discovery"
    assert plugin["version"] == contract["version"]
    assert plugin["author"] == {
        "name": "Helena Bioinformatics",
        "email": "contact@helena.bio",
        "url": "https://www.helena.bio",
    }
    assert plugin["homepage"] == "https://noodle.helena.bio/mcp"
    assert plugin["repository"] == (
        "https://github.com/helena-bioinformatics/noodle-mcp"
    )
    assert plugin["license"] == "Apache-2.0"
    assert "biomedical literature" in plugin["keywords"]
    assert "citation graph" in plugin["keywords"]
    assert power["$schema"] == (
        "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json"
    )
    assert (
        power["mcpServers"]["noodle-biomedical-literature"]["url"]
        == (contract["endpoint"])
    )


def test_goose_recipe_is_direct_remote_and_task_first() -> None:
    contract = json.loads(
        (ROOT / "registry/discovery-contract.json").read_text(encoding="ascii")
    )
    clients = json.loads(
        (ROOT / "registry/platforms/client-configs.json").read_text(encoding="ascii")
    )
    goose = clients["clients"]["goose"]

    assert goose["type"] == "streamable_http"
    assert goose["uri"] == contract["endpoint"]
    assert goose["timeout"] == 300
    assert goose["deeplink"].startswith("goose://extension?")
    assert "type=streamable_http" in goose["deeplink"]
    assert "Noodle%20Biomedical%20Literature%20Discovery" in goose["deeplink"]
    assert "npx" not in goose["deeplink"]


def test_training_tutorial_covers_search_graph_and_safety() -> None:
    tutorial = (
        ROOT / "docs/tutorials/biomedical-literature-discovery-and-graph-traversal.md"
    ).read_text(encoding="ascii")

    assert "Estimated time:" in tutorial
    assert "Learning objectives" in tutorial
    assert "search_biomedical_literature" in tutorial
    assert "get_publication_details" in tutorial
    assert "get_publication_neighborhood" in tutorial
    assert "get_work_neighborhood" in tutorial
    assert "get_corpus_summary" in tutorial
    assert "https://noodle.helena.bio" in tutorial
    assert "https://api.helena.bio/noodle/v1/mcp" in tutorial
    assert "Do not submit patient records" in tutorial


def test_all_distribution_files_are_ascii_and_have_no_secret_markers() -> None:
    for path in (ROOT / "registry").rglob("*"):
        if not path.is_file():
            continue
        text = path.read_text(encoding="ascii")
        assert "PRIVATE KEY" not in text
        assert "X-Internal-Secret" not in text
        assert "literature-mining:9004" not in text
