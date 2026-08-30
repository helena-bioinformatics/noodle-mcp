# Noodle for goose

Noodle Biomedical Literature Discovery is a public, read-only research service
and MCP extension for finding, inspecting, comparing, and traversing biomedical
literature. It connects directly to the canonical hosted Streamable HTTP
endpoint; no local package, API key, account, or patient data is required.

## One-click install

[Install Noodle in goose](goose://extension?type=streamable_http&url=https%3A%2F%2Fapi.helena.bio%2Fnoodle%2Fv1%2Fmcp&timeout=300&id=noodle-biomedical-literature&name=Noodle%20Biomedical%20Literature%20Discovery&description=Search%20and%20traverse%20public%20biomedical%20literature%20by%20topic%2C%20PMID%2C%20DOI%2C%20PMCID%2C%20citations%2C%20and%20semantic%20neighborhoods)

## Manual configuration

```yaml
extensions:
  noodle-biomedical-literature:
    type: streamable_http
    name: noodle-biomedical-literature
    display_name: Noodle Biomedical Literature Discovery
    enabled: true
    uri: https://api.helena.bio/noodle/v1/mcp
    headers: {}
    env_keys: []
    envs: {}
    timeout: 300
```

## Example tasks

- Find source-linked papers about BRCA1 homologous recombination.
- Resolve PMID 35008774 and show its publication details.
- Find related papers and walk a bounded citation or semantic neighborhood.
- Inspect corpus size, sources, freshness, and graph coverage.

Search rank, citations, similarity, co-mention, and graph distance are discovery
signals. They do not establish causality, diagnosis, treatment, or clinical
variant classification.

- Website: https://noodle.helena.bio
- MCP guide: https://noodle.helena.bio/mcp
- Privacy: https://noodle.helena.bio/privacy
- Support: https://noodle.helena.bio/contact
