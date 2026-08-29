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
    assert server["version"] == contract["version"] == "0.2.0"
    assert server["remotes"][0]["url"] == contract["endpoint"]
    assert package["mcpServers"]["noodle"]["url"] == contract["endpoint"]


def test_all_distribution_files_are_ascii_and_have_no_secret_markers() -> None:
    for path in (ROOT / "registry").rglob("*"):
        if not path.is_file():
            continue
        text = path.read_text(encoding="ascii")
        assert "PRIVATE KEY" not in text
        assert "X-Internal-Secret" not in text
        assert "literature-mining:9004" not in text
