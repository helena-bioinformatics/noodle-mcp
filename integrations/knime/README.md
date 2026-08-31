# Noodle for KNIME Analytics Platform

This integration turns a table of biomedical questions into source-linked
Noodle literature-search results. It calls the canonical public, read-only MCP
endpoint and contains no corpus or retrieval implementation.

## Build the workflow

1. Create a one-column input table named `query` with one biomedical search per
   row.
2. Add a **Python Script** node and connect the table to input port 0.
3. Configure a KNIME Python environment with `pyarrow`; the remaining imports
   are from Python's standard library.
4. Paste `knime_node.py` into the node and execute it.
5. Expand or parse the `noodle_result_json` output column downstream.

No account or API key is required. Do not submit patient records or private
case content. Search ranking and graph proximity are discovery signals, not
clinical conclusions.

The script uses MCP protocol `2026-07-28` and
`https://api.helena.bio/noodle/v1/mcp`.
