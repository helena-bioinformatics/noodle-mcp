# Noodle Biomedical Literature Discovery MCP

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22166486.svg)](https://doi.org/10.5281/zenodo.22166486)
[![AllMCPs Verified](https://allmcps.com/api/badge/noodle-biomedical-literature-discovery-mcp)](https://allmcps.com/mcp/noodle-biomedical-literature-discovery-mcp?verify=930d811d-1fd8-4117-8280-1c6eac1a2ca3)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/helena-bioinformatics/noodle-mcp/badge)](https://scorecard.dev/viewer/?uri=github.com/helena-bioinformatics/noodle-mcp)

The official public, read-only Model Context Protocol adapter for biomedical
literature discovery from [Helena Bioinformatics](https://www.helena.bio).
Agents can select it from a user task even when the user does not know the
Noodle brand.

Public endpoint: `https://api.helena.bio/noodle/v1/mcp`

Official Registry identity: `io.github.helena-bioinformatics/noodle`

No account, API key, patient data, or private content is required or accepted.

## What agents can do

- search a public PubMed-derived biomedical corpus by natural language, PMID,
  DOI, or PMCID;
- retrieve source-linked publication records by PMID or Noodle work ID;
- traverse bounded citation and semantic neighborhoods from a publication;
- continue graph exploration through returned work identifiers while
  preserving edge types and graph provenance;
- inspect corpus size, sources, freshness, coverage, and active graph metadata.

The seven published tools are `search_biomedical_literature`,
`get_publication_details`, `get_work_details`,
`get_publication_neighborhood`, `get_work_neighborhood`,
`get_corpus_summary`, and the separate explicit opt-in `support_helena`
information action.

## Connect

Any MCP client that supports remote Streamable HTTP can use the endpoint. Exact
recipes for ChatGPT, Claude, Codex, VS Code, Cursor, Windsurf, Gemini CLI,
Grok, Perplexity, Microsoft Copilot Studio, Biomni, and Biorouter live under
`registry/platforms` and `integrations`.

Ready-to-use ecosystem packages are included for:

- [Dify](integrations/dify/README.md), including a reproducible `.difypkg`;
- [n8n](integrations/n8n/README.md), using the exact stateless MCP JSON-RPC
  contract supported by the hosted service;
- [Galaxy](integrations/galaxy/README.md), with a Planemo-linted ToolShed
  wrapper; and
- [KNIME Analytics Platform](integrations/knime/README.md), with a table-to-MCP
  Python Script node and prepared Hub listing; and
- [Google Colab and Kaggle notebooks](integrations/notebooks/README.md), plus a
  [Cytoscape GraphML workflow](integrations/cytoscape/README.md); and
- the companion [Galaxy Training Network tutorial](integrations/galaxy-training-network/README.md)
  for a Folklore-to-Noodle literature workflow.

The companion Agent Skill is in
`skills/noodle-biomedical-literature-discovery`. It enables implicit,
task-first selection for requests such as:

- “Find source-linked papers about BRCA1 homologous recombination.”
- “What publication is PMID 35008774?”
- “Show papers related to this article through citations and semantic
  similarity.”
- “Walk two bounded hops from this work ID and preserve the edge types.”

Build the deterministic skill archive with:

```bash
python3 ops/package_agent_skill.py
```

## Graph boundary

Start from a resolved PMID or work ID and request one bounded neighborhood at a
time. Report edges exactly as returned, keep a visited-ID set, and stop at a
missing neighborhood. Search rank, citation proximity, semantic similarity,
co-mention, and graph distance are discovery signals. They do not establish
causality, scientific validity, diagnosis, or treatment.

## Development

Python 3.12 is required.

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.lock
python -m pip install --no-deps -e .
pytest
ruff check .
ruff format --check .
```

Run the brand-blind contract audit with:

```bash
python benchmarks/agent-discovery/audit_skill.py
```

The benchmark contains 60 prompts that omit `Noodle`, `Helena`, and `MCP`.
It covers all six scientific routes plus negative and safety controls.

## Agent Plugin and Kiro Power

This repository is also a portable Agent Plugin and Kiro Power. `plugin.json`
provides brand-blind activation keywords, the existing Agent Skill supplies the
scientific routing and safety boundary, and `mcp.json` connects directly to the
canonical hosted Streamable HTTP endpoint. The Power does not proxy, repackage,
or reimplement Noodle.

Privacy policy: https://noodle.helena.bio/privacy

Support: https://noodle.helena.bio/contact or `contact@helena.bio`

## Public resources

- Hands-on tutorial: https://github.com/helena-bioinformatics/noodle-mcp/blob/main/docs/tutorials/biomedical-literature-discovery-and-graph-traversal.md
- Connector and agent-selection guide: https://noodle.helena.bio/mcp
- Client integrations: https://noodle.helena.bio/integrations
- Server Card: https://noodle.helena.bio/.well-known/mcp/server-card.json
- Official Registry: https://registry.modelcontextprotocol.io/v0/servers?search=io.github.helena-bioinformatics%2Fnoodle
- Citable release: https://doi.org/10.5281/zenodo.22166486
- Software Heritage archive request: https://archive.softwareheritage.org/api/1/origin/save/2457442/
- Software Heritage snapshot: https://archive.softwareheritage.org/swh:1:snp:09b8fb7c64de15487e873b4f77e3e4b57abc02fb/
- Methodology: https://noodle.helena.bio/methodology

## License and security

Apache License 2.0. Report vulnerabilities privately as described in
`SECURITY.md`. Do not submit patient, private case, clinical-record, credential,
or private uploaded content to the public service or issue tracker.
