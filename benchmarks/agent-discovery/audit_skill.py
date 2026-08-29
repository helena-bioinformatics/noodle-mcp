#!/usr/bin/env python3
import argparse
import csv
import json
from collections import Counter
from pathlib import Path

EXPECTED_TOOLS = {
    "search_biomedical_literature",
    "get_publication_details",
    "get_work_details",
    "get_publication_neighborhood",
    "get_work_neighborhood",
    "get_corpus_summary",
}
INTENT_TERMS = {
    "search": ("biomedical literature", "research question"),
    "identifier": ("PMID", "DOI", "PMCID", "work identifier"),
    "graph": ("citation", "semantic", "neighborhood", "traverse"),
    "corpus": ("corpus", "coverage", "freshness", "graph metadata"),
}
SAFETY_TERMS = (
    "patient",
    "private case",
    "clinical-record",
    "Search rank",
    "do not establish causality",
    "diagnosis",
    "treatment",
)


def audit(cases_path: Path, skill_path: Path) -> dict:
    cases = list(csv.DictReader(cases_path.open(encoding="utf-8")))
    skill = skill_path.read_text(encoding="utf-8")
    families = Counter(case["family"] for case in cases)
    selected = [case for case in cases if case["expected_selection"] == "yes"]
    tools = {case["expected_tool"] for case in selected}
    outcomes = (
        "publication_not_found",
        "work_not_found",
        "neighborhood_not_found",
        "invalid_arguments",
        "upstream_timeout",
        "upstream_unavailable",
        "upstream_rate_limited",
        "invalid_upstream_response",
        "internal_failure",
    )
    return {
        "case_count": len(cases),
        "brand_blind": all(
            forbidden not in case["prompt"]
            for case in cases
            for forbidden in ("Noodle", "Helena", "MCP")
        ),
        "family_counts": dict(sorted(families.items())),
        "expected_selection_yes": len(selected),
        "expected_selection_no": len(cases) - len(selected),
        "tool_routes_complete": tools == EXPECTED_TOOLS,
        "intent_contract": {
            family: all(term in skill for term in terms)
            for family, terms in INTENT_TERMS.items()
        },
        "safety_contract": {term: term in skill for term in SAFETY_TERMS},
        "typed_outcomes_present": all(outcome in skill for outcome in outcomes),
        "implicit_trigger_present": "even when the user does not mention" in skill,
    }


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--cases", type=Path, default=Path(__file__).with_name("cases.csv")
    )
    parser.add_argument(
        "--skill",
        type=Path,
        default=root / "skills/noodle-biomedical-literature-discovery/SKILL.md",
    )
    args = parser.parse_args()
    result = audit(args.cases, args.skill)
    print(json.dumps(result, indent=2, sort_keys=True))
    checks = [
        result["case_count"] >= 60,
        result["brand_blind"],
        result["tool_routes_complete"],
        all(result["intent_contract"].values()),
        all(result["safety_contract"].values()),
        result["typed_outcomes_present"],
        result["implicit_trigger_present"],
    ]
    if not all(checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
