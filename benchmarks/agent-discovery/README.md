# Brand-blind agent discovery benchmark

The 60 prompts test whether an agent selects Noodle Biomedical Literature
Discovery MCP from the task alone. Prompts deliberately omit `Noodle`, `Helena`,
and `MCP`. Positive cases cover all six scientific routes; negative and safety
controls ensure that literature discovery is not selected for unrelated work,
patient decisions, or unsupported causal claims.

Run:

```bash
python benchmarks/agent-discovery/audit_skill.py
```

The CSV is a deterministic selection-contract corpus, not a model performance
claim. Evaluate real agent releases separately and record the model, client,
configuration, skill version, and exact results.
