import json
from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from tools.mcp_client import call_tool


class SearchBiomedicalLiteratureTool(Tool):
    def _invoke(
        self, tool_parameters: dict[str, Any]
    ) -> Generator[ToolInvokeMessage, None, None]:
        arguments = {
            "query": str(tool_parameters.get("query", "")).strip(),
            "limit": int(tool_parameters.get("limit", 10)),
            "sort": str(tool_parameters.get("sort", "relevance")),
        }
        if not arguments["query"]:
            yield self.create_text_message(
                "A biomedical question or identifier is required."
            )
            return
        yield self.create_text_message(
            json.dumps(
                call_tool("search_biomedical_literature", arguments), ensure_ascii=False
            )
        )
