"""Verify Noodle through Biomni's pinned stdio bridge pattern."""

import asyncio
import json
from pathlib import Path

import yaml
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

HERE = Path(__file__).resolve().parent
EXPECTED_TOOLS = {
    "search_biomedical_literature",
    "get_publication_details",
    "get_work_details",
    "get_publication_neighborhood",
    "get_work_neighborhood",
    "get_corpus_summary",
    "support_helena",
}


def load_server_parameters() -> StdioServerParameters:
    config = yaml.safe_load((HERE / "mcp_config.yaml").read_text())
    command = config["mcp_servers"]["noodle_biomedical_literature_discovery_mcp"][
        "command"
    ]
    executable, *arguments = command
    return StdioServerParameters(command=executable, args=arguments)


async def run_smoke_test() -> dict[str, object]:
    async with asyncio.timeout(90):
        async with stdio_client(load_server_parameters()) as (reader, writer):
            async with ClientSession(reader, writer) as session:
                initialization = await session.initialize()
                listed = await session.list_tools()
                tools = {tool.name: tool for tool in listed.tools}
                assert set(tools) == EXPECTED_TOOLS
                schema = tools["search_biomedical_literature"].input_schema
                assert schema["additionalProperties"] is False
                assert "query" in schema["required"]
                response = await session.call_tool("get_corpus_summary", {})
                assert response.is_error is False
                summary = response.structured_content
                assert summary is not None
                assert summary["counts"]["unique_works"] > 0
                return {
                    "protocol_version": initialization.protocol_version,
                    "tools": sorted(tools),
                    "unique_works": summary["counts"]["unique_works"],
                }


if __name__ == "__main__":
    print(json.dumps(asyncio.run(run_smoke_test()), indent=2, sort_keys=True))
