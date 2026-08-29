import asyncio

from fastmcp import Client, FastMCP
from noodle_biorouter.server import SERVER_NAME, create_server


def test_proxy_preserves_tool_schema_and_structured_result() -> None:
    async def exercise() -> None:
        backend = FastMCP("Public contract fixture")

        @backend.tool
        def get_corpus_summary() -> dict:
            """Return deterministic public corpus metadata."""
            return {"contract_version": "1.0", "counts": {"unique_works": 98}}

        proxy = create_server(backend)
        assert proxy.name == SERVER_NAME
        async with Client(proxy, name="Biorouter bridge unit test") as client:
            tools = await client.list_tools()
            assert [tool.name for tool in tools] == ["get_corpus_summary"]
            assert tools[0].inputSchema["additionalProperties"] is False
            result = await client.call_tool("get_corpus_summary", {})
            assert result.structured_content["counts"]["unique_works"] == 98

    asyncio.run(exercise())
