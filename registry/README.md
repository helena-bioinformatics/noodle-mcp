# Noodle MCP distribution

This directory is the canonical distribution package for
`Noodle Biomedical Literature Discovery MCP` (`io.github.helena-bioinformatics/noodle`).
Version `0.2.0` is the coordinated task-first discovery release. The endpoint,
domain Server Card, signed Registry publication, and canonical discovery pages
are active and observed in sync. The public adapter repository remains blocked
until the canonical organization grants repository-creation permission.
Directory listings remain unclaimed until separately observed.

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
- `medical-directory-submissions.md`: evidence ledger for biomedical and
  healthcare directories; blocked, submitted, and active are kept distinct.
- `discovery-contract.json`: machine-readable desired state.
- `agent-selection.json`: brand-blind task selection and routing contract.
- `agent-selection.schema.json`: strict validation schema for that contract.

Lifecycle is `active` after production and public protocol verification. Run
`ops/reconcile_discovery.py` to compare health, readiness, Official Registry,
Server Card, live MCP catalogs, and configured aggregators. Canonical drift is
release-blocking; unavailable or stale aggregators are reported separately.
Record only observed crawler and editorial URLs. Never invent a listing.
