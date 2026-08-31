import json
import urllib.error
import urllib.request
from typing import Any

ENDPOINT = "https://api.helena.bio/noodle/v1/mcp"
PROTOCOL = "2026-07-28"


def call_tool(name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": name,
            "arguments": arguments,
            "_meta": {
                "io.modelcontextprotocol/protocolVersion": PROTOCOL,
                "io.modelcontextprotocol/clientCapabilities": {},
            },
        },
    }
    request = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "MCP-Protocol-Version": PROTOCOL,
            "Mcp-Method": "tools/call",
            "Mcp-Name": name,
            "User-Agent": "dify-helena-noodle/0.1.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            document = json.load(response)
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
        raise RuntimeError("Noodle is temporarily unavailable.") from exc
    if "error" in document:
        raise RuntimeError(str(document["error"].get("message", "Noodle MCP error")))
    result = document.get("result", {})
    if result.get("isError"):
        content = result.get("content") or []
        message = content[0].get("text") if content and isinstance(content[0], dict) else "Noodle tool error"
        raise RuntimeError(message)
    structured = result.get("structuredContent")
    return structured if isinstance(structured, dict) else result
