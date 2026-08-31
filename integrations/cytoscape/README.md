# Noodle literature graphs in Cytoscape

Export a bounded, provenance-preserving Noodle publication neighborhood to
GraphML and open it directly in Cytoscape Desktop.

```bash
python3 noodle_to_cytoscape.py --pmid 35008774 --output neighborhood.graphml
```

In Cytoscape, choose **File → Import → Network from File** and select the
generated file. Node columns include PMID, DOI and stable Noodle work ID. Edge
columns preserve the returned reason kinds and scores. The graph-level
`graph_version` is retained for reproducibility.

No account or API key is required. Each invocation retrieves one bounded
neighborhood. Semantic similarity, citation proximity and co-mention are
discovery signals; they do not establish causality, validity or clinical
significance.
