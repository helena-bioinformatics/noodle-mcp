# Noodle MCP distribution

This directory is the canonical distribution package for
`Noodle Biomedical Literature Discovery MCP` (`io.github.helena-bioinformatics/noodle`).
Version `0.2.0` is the coordinated task-first discovery release. It is not
active until the endpoint, domain Server Card, signed Registry publication,
public adapter repository, and canonical discovery pages have been observed in
sync. Directory listings remain unclaimed until separately observed.

The canonical endpoint is `https://api.helena.bio/noodle/v1/mcp`.
The server uses stateless Streamable HTTP, MCP `2026-07-28`, no authentication,
and seven read-only tools. It contains no literature index, model, credential,
patient data, or write capability. `support_helena` is an isolated opt-in link
helper and cannot initiate payment or outreach.

Artifacts:

- `server.json`: immutable Official MCP Registry record.
- `packages/noodle/.mcp.json`: metadata-only client package.
- `platforms/client-configs.json`: exact client recipes.
- `platforms/microsoft-copilot-openapi.yaml`: Copilot import definition.
- `directory-submission.md`: reusable editorial listing copy.
- `discovery-contract.json`: machine-readable desired state.
- `agent-selection.json`: brand-blind task selection and routing contract.
- `agent-selection.schema.json`: strict validation schema for that contract.

Lifecycle is `active` after production and public protocol verification. Publish
the exact immutable Registry version from the matching signed tag, then record
only observed crawler and editorial URLs. Never invent a listing.
