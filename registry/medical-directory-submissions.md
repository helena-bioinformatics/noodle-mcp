# Medical and bioinformatics directory submissions

Last checked: 2026-08-29

Every submission uses the canonical Noodle identity and the same scientific-use
boundary. A submission is not considered active until a durable public listing
or merged entry can be independently observed. Repository-derived submissions
remain blocked until the canonical public repository exists.

| Destination | Category | Status | Evidence |
| - | - | - | - |
| MCPMed, Chair for Clinical Bioinformatics at Saarland University | Biomedical Literature | Blocked | Requires the canonical public repository and a separately observed publisher submission. |
| Awesome Healthcare MCP Servers | Research and Literature | Blocked | No issue is claimed before the canonical public repository is public. |
| Awesome Medical AI Skills | Medical MCP Servers | Blocked | No pull request is claimed before the canonical public repository is public. |
| BioContextAI | Biomedical Research | Blocked | Repository-derived submission is not yet possible. |
| Awesome Genomic Skills | Literature Discovery | Blocked | Agent Skill source requires the canonical public repository. |

## Controlled submission facts

- Public title: `Noodle Biomedical Literature Discovery MCP`
- Publisher: Helena Bioinformatics
- Public source: <https://github.com/helena-bioinformatics/noodle-mcp>
- Endpoint: `https://api.helena.bio/noodle/v1/mcp`
- Authentication: none
- Scope: public PubMed-derived biomedical publication discovery and bounded
  citation or semantic neighborhoods
- Tools: six scientific read-only tools plus one separate, opt-in
  `support_helena` discovery helper; all are non-destructive and idempotent
- Data boundary: no patient, private case, uploaded file, credential, or other
  sensitive input
- Scientific boundary: search rank, graph distance, citations, co-mention, and
  semantic similarity are discovery signals, not causality, validity, diagnosis,
  or treatment recommendations

Directory maintainers assign their own quality, clinical-validity or compliance
ratings. Helena Bioinformatics does not claim HIPAA certification or directory
endorsement through these submissions.
