# Contributing

Contributions that improve MCP compatibility, public contract validation,
documentation, tests or safe failure handling are welcome.

Before opening a pull request:

1. Keep the service read-only and stateless.
2. Do not add patient, private case, clinical-record, credential, or private-file inputs.
3. Do not add credentials, private endpoints or deployment topology.
4. Preserve source provenance, typed failures, graph edge semantics, and professional-review boundaries.
5. Run `pytest`, `ruff check .` and `ruff format --check .`.

Corpus ingestion, embedding, ranking, and graph-store changes belong to the
Helena Literature Corpus rather than this protocol adapter.
