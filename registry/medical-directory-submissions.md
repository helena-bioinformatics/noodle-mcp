# Medical and bioinformatics directory submissions

Last checked: 2026-08-30

Every submission uses the canonical Noodle identity and the same scientific-use
boundary. A submission is not considered active until a durable public listing
or merged entry can be independently observed.

| Destination | Category | Status | Evidence |
| - | - | - | - |
| MCPMed, Chair for Clinical Bioinformatics at Saarland University | Biomedical Literature | Not submitted | The public source prerequisite is satisfied; no publisher-dashboard submission is claimed without an observed receipt. |
| Awesome Healthcare MCP Servers | Life Sciences & Research | Open submission | [Issue #9](https://github.com/rdmgator12/awesome-healthcare-mcp-servers/issues/9) |
| Awesome Medical AI Skills | Medical MCP Servers / Literature & Research | Open pull request | [Pull request #4](https://github.com/JuneYaooo/awesome-medical-ai-skills/pull/4) |
| BioContextAI | Biomedical Research | Open pull request; schema CI passed | [Pull request #68](https://github.com/biocontext-ai/registry/pull/68) |
| Awesome Genomic Skills | MCP Servers for Life Sciences | Open pull request | [Pull request #10](https://github.com/GoekeLab/awesome-genomic-skills/pull/10) |
| TensorBlock MCP Index | Healthcare & Life Sciences | Open pull request | [Pull request #2054](https://github.com/TensorBlock/awesome-mcp-servers/pull/2054) |
| Awesome Codex MCP Servers | Science and research | Open pull request | [Pull request #7](https://github.com/Kuberwastaken/awesome-codex-mcp-servers/pull/7) |
| add-mcp | Remote Official Registry server | Open pull request; CodeRabbit passed, maintainer Vercel authorization pending | [Pull request #110](https://github.com/neon-solutions/add-mcp/pull/110) |
| Docker MCP Registry | Healthcare remote server | Open pull request | [Pull request #4835](https://github.com/docker/mcp-registry/pull/4835) |
| mcp.so | Biomedical literature and research | Open submission | [Issue #3830](https://github.com/chatmcp/mcpso/issues/3830) |
| awesome-mcp-servers | Biology, Medicine and Bioinformatics | Open pull request; submission CI passed | [Pull request #13177](https://github.com/punkpeye/awesome-mcp-servers/pull/13177) |

MCP Central publication was attempted through the public repository's pinned
OIDC workflow in [run 33274695400](https://github.com/helena-bioinformatics/noodle-mcp/actions/runs/33274695400).
Manifest validation passed, but authentication could not start because
`registry.mcpcentral.io` had no DNS record. No MCP Central listing is claimed.

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
