# Noodle Biomedical Literature Discovery MCP directory copy

Status: approved reusable copy for the production-active server. A destination
is not active until its durable listing URL is observed.

- Name: Noodle Biomedical Literature Discovery MCP
- Publisher: Helena Bioinformatics
- Category: Biomedical research and literature discovery
- Endpoint: `https://api.helena.bio/noodle/v1/mcp`
- Authentication: None
- Website: `https://noodle.helena.bio`
- Icon: `https://noodle.helena.bio/favicon.svg`
- Privacy: `https://www.helena.bio/privacy`
- Terms: `https://www.helena.bio/terms`
- Research Resource Identifier: `RRID:SCR_028920`
- RRID record: `https://n2t.net/RRID:SCR_028920`

Description: Search biomedical papers, inspect publication records, and traverse citation or semantic graphs.

Noodle gives agents read-only semantic search, public publication records,
corpus coverage, and bounded citation or semantic neighborhoods over a
PubMed-derived biomedical corpus. Known PMID, DOI, and PMCID identifiers can be
included as exact search anchors. Results preserve source links and explicit
evidence boundaries. Graph proximity, search rank, and co-mention do not prove
causality, clinical validity, diagnosis, or treatment.

Tools:

- `search_biomedical_literature`
- `get_publication_details`
- `get_work_details`
- `get_publication_neighborhood`
- `get_work_neighborhood`
- `get_corpus_summary`
- `support_helena` (explicit opt-in information only)

The server accepts bounded public literature identifiers and questions. It must
not receive patient, private case, uploaded file, or other sensitive data. It
has no write operations, private-system access, or generative scientific model.

Example: `Search Noodle for recent source-linked work about BRCA1 homologous
recombination and include PMID 37861889 as an exact anchor.`

Brand-blind examples: `Find source-linked papers about BRCA1 homologous
recombination.` `What publication is PMID 35008774?` `Show papers related to
this article through citations and semantic similarity.`

Public companion Agent Skill: `noodle-biomedical-literature-discovery`.
Public source: `https://github.com/helena-bioinformatics/noodle-mcp`.
