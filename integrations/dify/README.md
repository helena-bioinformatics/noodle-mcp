# Noodle Biomedical Literature Discovery for Dify

Official, no-authentication Dify tools for the public Noodle MCP endpoint.

The plugin searches public biomedical papers, retrieves publication records and
traverses bounded citation or semantic neighborhoods. It does not accept patient
or private data and does not provide diagnosis or treatment advice.

- Website: https://noodle.helena.bio
- MCP guide: https://noodle.helena.bio/mcp
- Source: https://github.com/helena-bioinformatics/noodle-mcp
- Publisher: Helena Bioinformatics

No credentials are required. Install the plugin and add its tools to a Dify
agent or workflow.

## Install

Download `dist/noodle-biomedical-literature-0.1.0.difypkg` and its `.sha256`
sidecar. Verify the archive, then in Dify open **Plugins**, choose **Install
plugin from local file**, and select the `.difypkg` file.

Rebuild reproducibly with Dify CLI `0.6.10`:

```bash
dify plugin package integrations/dify \
  -o noodle-biomedical-literature-0.1.0.difypkg
```
