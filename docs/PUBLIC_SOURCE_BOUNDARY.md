# Public source boundary

This repository contains the public Noodle MCP adapter, contracts, selection
skill, benchmarks, client recipes, and transparent bridges. It does not contain
the Helena Literature Corpus, embedding models, ranker, graph store, private
deployment topology, credentials, or unrelated platform code.

Included:

- MCP discovery and stateless JSON-RPC handling;
- closed input and response validation;
- six scientific read-only tools, one opt-in support information tool, four
  prompts, and one methodology resource;
- health, readiness, metrics, tests, container packaging, and CI;
- task-first Agent Skill and 60-case brand-blind benchmark;
- Biomni and Biorouter connector bridges.

The hosted service delegates to Helena's public literature authority. The
adapter does not own or reproduce corpus content, retrieval indexes, embeddings,
ranking logic, or graph releases. Consumers must use the returned identifiers,
source links, graph receipts, and typed failure states.

The public endpoint accepts public non-sensitive research questions, PMID, DOI,
PMCID, and Noodle work identifiers. Never submit patient data, private case
data, clinical records, credentials, or private uploaded content.

Before release, maintainers run the complete test and lint suite, scan the
tracked tree for credentials and internal markers, validate the Registry
record, build the Agent Skill and Biorouter bundle reproducibly, and reconcile
runtime, Server Card, Registry, repository, and public discovery pages.
