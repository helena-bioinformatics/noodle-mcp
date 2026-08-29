import json
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"


def load(name: str) -> dict:
    return json.loads((REGISTRY / name).read_text())


def test_agent_selection_contract_validates_and_matches_identity() -> None:
    schema = load("agent-selection.schema.json")
    selection = load("agent-selection.json")
    discovery = load("discovery-contract.json")
    jsonschema.validate(selection, schema)
    identity = selection["identity"]
    for field in ("title", "publisher", "registryName", "endpoint"):
        assert identity[field] == discovery[field]


def test_agent_selection_contract_is_task_first_and_safety_complete() -> None:
    selection = load("agent-selection.json")
    task = selection["identity"]["task"]
    for term in ("Search", "biomedical", "identifier", "citation", "semantic"):
        assert term in task
    intents = " ".join(selection["selection"]["positiveIntents"])
    for term in ("literature", "PMID", "citation", "semantic", "corpus", "gene"):
        assert term in intents
    boundary = selection["scientificBoundary"]
    assert boundary["notDiagnosis"] is True
    assert boundary["notTreatment"] is True
    assert boundary["semanticSimilarityIsEvidence"] is False


def test_agent_selection_routes_only_published_scientific_tools() -> None:
    selection = load("agent-selection.json")
    discovery = load("discovery-contract.json")
    routed = {route["tool"] for route in selection["routing"]}
    assert routed == set(discovery["tools"]) - {"support_helena"}
