# Install Noodle in Cline

Noodle is a hosted, read-only Streamable HTTP MCP server. Do not clone the
repository, run a local process, or invent an npm, npx, PyPI, or stdio package.

## Connection

- Name: `Noodle Biomedical Literature Discovery MCP`
- Transport: `Remote (HTTP)` / Streamable HTTP
- URL: `https://api.helena.bio/noodle/v1/mcp`
- Authentication: none

In Cline, open MCP Servers, add a remote HTTP server, enter the URL above, and
save the connection. If editing configuration directly, use the client’s
remote-server URL field; do not configure `command` or `args`.

## Verify

After connecting, confirm that Cline discovers exactly these seven read-only
tools:

1. `search_biomedical_literature`
2. `get_publication_details`
3. `get_work_details`
4. `find_related_publications`
5. `traverse_citation_graph`
6. `search_semantic_neighbors`
7. `get_corpus_coverage`

Run a harmless smoke test such as searching for `BRCA1 homologous recombination`
with a small result limit. A successful response should contain publication
records and provenance metadata without requesting credentials.

## Safety

Use Noodle only for public biomedical literature discovery. Do not send patient,
private, proprietary, or identifying data. Treat citations and graph
relationships as discovery evidence and verify scientific claims in the primary
sources. The server does not provide diagnosis or treatment advice.

Canonical metadata and troubleshooting are available at
<https://noodle.helena.bio/mcp> and in the
[public repository](https://github.com/helena-bioinformatics/noodle-mcp).
