# Noodle Biomedical Literature Discovery MCP for Biorouter

This reproducible `.brxt` extension is a local stdio bridge to the hosted,
read-only Streamable HTTP endpoint. It contains no corpus, embedding, ranking,
or graph logic and requires no account, key, or environment variable.

It preserves all seven hosted tools, their schemas, structured results, typed
failures, edge types, and provenance. The bundled non-user-invocable skill lets
Biorouter select it for biomedical paper search, publication identifiers,
related-paper discovery, citation or semantic graph traversal, and corpus
questions without requiring the Noodle name.

Build and verify:

```bash
integrations/biorouter/scripts/build_brxt.sh
integrations/biorouter/scripts/verify_brxt_install.sh
```

The reproducible bundle and checksum are written to
`integrations/biorouter/dist/noodle-biomedical-literature-discovery-mcp.brxt`
and its `.sha256` sidecar.

Install with:

```bash
biorouter extension install integrations/biorouter/dist/noodle-biomedical-literature-discovery-mcp.brxt
```

Run the live smoke test with `python integrations/biorouter/smoke_test.py`.
It discovers all seven tools and retrieves the public corpus summary.

Use public non-sensitive research questions and publication identifiers only.
Graph proximity and ranking do not establish causality, diagnosis, or treatment.
