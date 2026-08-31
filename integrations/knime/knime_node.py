"""KNIME Python Script node for Noodle biomedical literature search."""

import json
import urllib.error
import urllib.request

import knime.scripting.io as knio
import pyarrow as pa

ENDPOINT = "https://api.helena.bio/noodle/v1/mcp"
PROTOCOL = "2026-07-28"


def call_noodle(query: str, limit: int = 10) -> dict:
    body = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "search_biomedical_literature",
            "arguments": {"query": query, "limit": limit, "sort": "relevance"},
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
            "Mcp-Name": "search_biomedical_literature",
            "User-Agent": "knime-noodle-mcp/0.1.0",
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


input_table = knio.input_tables[0].to_pyarrow()
queries = input_table.column(0).to_pylist()
rows = []
for query in queries:
    if query is None or not str(query).strip():
        continue
    value = str(query).strip()
    rows.append({"query": value, "noodle_result_json": json.dumps(call_noodle(value))})

knio.output_tables[0] = knio.Table.from_pyarrow(pa.Table.from_pylist(rows))
