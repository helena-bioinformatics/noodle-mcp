import json
from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from tools.mcp_client import call_tool


class GetPublicationNeighborhoodTool(Tool):
    def _invoke(
        self, tool_parameters: dict[str, Any]
    ) -> Generator[ToolInvokeMessage, None, None]:
        arguments = {"pmid": str(tool_parameters.get("pmid", "")).strip()}
        yield self.create_text_message(
            json.dumps(
                call_tool("get_publication_neighborhood", arguments), ensure_ascii=False
            )
        )
