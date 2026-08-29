"""Verify the Biorouter bridge against the live public Noodle endpoint."""

import asyncio
import json

from fastmcp import Client
from noodle_biorouter.server import create_server

EXPECTED_TOOLS = {
    "search_biomedical_literature",
    "get_publication_details",
    "get_work_details",
    "get_publication_neighborhood",
    "get_work_neighborhood",
    "get_corpus_summary",
    "support_helena",
}


async def run_smoke_test() -> dict[str, object]:
    async with asyncio.timeout(90):
        async with Client(
            create_server(), name="Biorouter integration smoke test"
        ) as client:
            listed = await client.list_tools()
            tools = {tool.name: tool for tool in listed}
            assert set(tools) == EXPECTED_TOOLS
            schema = tools["search_biomedical_literature"].inputSchema
            assert schema["additionalProperties"] is False
            assert "query" in schema["required"]
            response = await client.call_tool("get_corpus_summary", {})
            summary = response.structured_content
            assert summary is not None
            assert summary["counts"]["unique_works"] > 0
            return {
                "tools": sorted(tools),
                "unique_works": summary["counts"]["unique_works"],
            }


if __name__ == "__main__":
    print(json.dumps(asyncio.run(run_smoke_test()), indent=2, sort_keys=True))
