# Biomni integration

This recipe connects Biomni to Noodle Biomedical Literature Discovery MCP.
Biomni starts external MCP servers through stdio, so the configuration uses a
digest-pinned `mcp-proxy` container as a transparent transport bridge:

```text
Biomni -> stdio -> pinned mcp-proxy -> https://api.helena.bio/noodle/v1/mcp
```

The bridge contains no corpus, retrieval, ranking, or graph logic. It requires
no account or API key and preserves the hosted tool schemas and structured
results.

```python
from biomni.agent import A1

agent = A1()
agent.add_mcp(config_path="integrations/biomni/mcp_config.yaml")
print(agent.list_mcp_servers())
```

Biomni registers all seven tools under
`mcp_servers.noodle_biomedical_literature_discovery_mcp`.

Run `python integrations/biomni/smoke_test.py` to discover the exact tool set
and retrieve the public corpus summary through the same command array.

Send only public non-sensitive literature questions and identifiers. Search
rank, citations, and semantic proximity are discovery signals, not causality,
diagnosis, or treatment.
