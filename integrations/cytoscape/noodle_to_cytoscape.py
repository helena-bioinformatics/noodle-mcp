#!/usr/bin/env python3
"""Export one bounded Noodle publication neighborhood as GraphML."""

import argparse
import json
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

ENDPOINT = "https://api.helena.bio/noodle/v1/mcp"
PROTOCOL = "2026-07-28"
GRAPHML = "http://graphml.graphdrawing.org/xmlns"


def get_neighborhood(pmid: str) -> dict:
    name = "get_publication_neighborhood"
    body = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": name,
            "arguments": {"pmid": pmid},
            "_meta": {
                "io.modelcontextprotocol/protocolVersion": PROTOCOL,
                "io.modelcontextprotocol/clientCapabilities": {},
            },
        },
    }
    request = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "MCP-Protocol-Version": PROTOCOL,
            "Mcp-Method": "tools/call",
            "Mcp-Name": name,
            "User-Agent": "cytoscape-noodle-mcp/0.1.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            document = json.load(response)
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
        raise RuntimeError("Noodle is temporarily unavailable") from exc
    result = document.get("result", {})
    if "error" in document or result.get("isError"):
        raise RuntimeError("Noodle returned a bounded tool error")
    return result.get("structuredContent", result)


def add_data(parent: ET.Element, key: str, value: object) -> None:
    element = ET.SubElement(parent, f"{{{GRAPHML}}}data", key=key)
    element.text = "" if value is None else str(value)


def to_graphml(neighborhood: dict) -> ET.ElementTree:
    ET.register_namespace("", GRAPHML)
    root = ET.Element(f"{{{GRAPHML}}}graphml")
    keys = {
        "label": ("all", "label"),
        "kind": ("node", "kind"),
        "pmid": ("node", "pmid"),
        "doi": ("node", "doi"),
        "work_id": ("node", "work_id"),
        "edge_reasons": ("edge", "edge_reasons"),
        "edge_score": ("edge", "edge_score"),
        "graph_version": ("graph", "graph_version"),
    }
    for key_id, (target, name) in keys.items():
        ET.SubElement(
            root,
            f"{{{GRAPHML}}}key",
            id=key_id,
            **{"for": target, "attr.name": name, "attr.type": "string"},
        )
    graph = ET.SubElement(
        root, f"{{{GRAPHML}}}graph", id="noodle", edgedefault="directed"
    )
    add_data(graph, "graph_version", neighborhood.get("graph_version"))
    for item in neighborhood.get("nodes", []):
        node = ET.SubElement(graph, f"{{{GRAPHML}}}node", id=item["id"])
        add_data(node, "label", item.get("label"))
        add_data(node, "kind", item.get("kind"))
        add_data(node, "pmid", item.get("publication_pmid"))
        add_data(node, "doi", item.get("publication_doi"))
        add_data(node, "work_id", item.get("publication_work_id"))
    for item in neighborhood.get("edges", []):
        edge = ET.SubElement(
            graph,
            f"{{{GRAPHML}}}edge",
            id=item["id"],
            source=item["source_id"],
            target=item["target_id"],
        )
        reasons = item.get("reasons", [])
        add_data(
            edge, "edge_reasons", "; ".join(str(r.get("kind", "")) for r in reasons)
        )
        scores = [r.get("score") for r in reasons if r.get("score") is not None]
        add_data(edge, "edge_score", max(scores) if scores else "")
    return ET.ElementTree(root)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pmid", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    tree = to_graphml(get_neighborhood(args.pmid))
    ET.indent(tree, space="  ")
    tree.write(args.output, encoding="utf-8", xml_declaration=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
