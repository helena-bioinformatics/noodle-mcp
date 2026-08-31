# Noodle Galaxy wrapper

Credential-free Galaxy wrapper for the public Noodle Biomedical Literature
Discovery MCP. It returns the canonical structured JSON without re-ranking or
reinterpreting scientific results.

Run `planemo lint noodle_mcp.xml` and `planemo test --galaxy_root ...` before a
ToolShed release. Live use requires outbound HTTPS access to `api.helena.bio`.
