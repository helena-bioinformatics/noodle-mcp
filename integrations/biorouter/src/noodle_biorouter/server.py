"""Transparent stdio bridge to Noodle Biomedical Literature Discovery MCP."""

from typing import Any

from fastmcp import Client
from fastmcp.server import create_proxy

ENDPOINT = "https://api.helena.bio/noodle/v1/mcp"
SERVER_NAME = "Noodle Biomedical Literature Discovery MCP"
CLIENT_NAME = "Biorouter Noodle Biomedical Literature Discovery MCP extension"
INSTRUCTIONS = (
    "Use this server for public biomedical literature search, publication records, "
    "related-paper discovery, citation or semantic graph traversal, and corpus "
    "metadata. Never send patient or private data. Preserve identifiers, sources, "
    "edge types, graph provenance, typed failures, and scientific boundaries."
)


def create_server(target: Any = ENDPOINT) -> Any:
    backend = Client(target, name=CLIENT_NAME, timeout=60)
    return create_proxy(backend, name=SERVER_NAME, instructions=INSTRUCTIONS)
