# syntax=docker/dockerfile:1

FROM ghcr.io/sparfenyuk/mcp-proxy:v0.12.0

LABEL org.opencontainers.image.title="Noodle Biomedical Literature Discovery MCP bridge"
LABEL org.opencontainers.image.description="Read-only stdio bridge to the public Noodle biomedical literature discovery endpoint"
LABEL org.opencontainers.image.source="https://github.com/helena-bioinformatics/noodle-mcp"
LABEL org.opencontainers.image.vendor="Helena Bioinformatics"

RUN addgroup -S noodle && adduser -S -G noodle noodle
USER noodle
CMD ["--transport", "streamablehttp", "--log-level", "WARNING", "https://api.helena.bio/noodle/v1/mcp"]
