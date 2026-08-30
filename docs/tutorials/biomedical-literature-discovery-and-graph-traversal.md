# Discovering and traversing biomedical literature with Noodle

**Format:** hands-on tutorial  
**Level:** beginner to intermediate  
**Estimated time:** 25 minutes  
**Audience:** biomedical researchers, bioinformaticians, research-software users, and agent developers  
**Material version:** 1.0  
**Noodle release:** 0.2.1  
**Licence:** Apache-2.0

Noodle Biomedical Literature Discovery is a public, read-only research tool
and Model Context Protocol (MCP) service. It searches a PubMed-derived corpus,
resolves publication identifiers, returns source-linked bibliographic records,
and exposes bounded citation and semantic literature neighborhoods.

Website: <https://noodle.helena.bio>  
MCP guide: <https://noodle.helena.bio/mcp>  
Canonical MCP endpoint: <https://api.helena.bio/noodle/v1/mcp>

No account or API key is required. Do not submit patient records, private case
data, credentials, or unpublished confidential material.

## Learning objectives

After completing this tutorial, you will be able to:

1. formulate a biomedical literature query with an optional exact identifier;
2. distinguish discovery ranking from scientific evidence;
3. inspect a source-linked publication record;
4. traverse one or more bounded graph neighborhoods while preserving edge
   types and provenance; and
5. recognize when Noodle is, and is not, appropriate for a task.

## Prerequisites

Use either the Noodle website or an MCP-compatible agent connected to the
canonical endpoint. An MCP client should support remote Streamable HTTP.
Connection recipes are available at <https://noodle.helena.bio/integrations>.

The examples below are written as natural-language agent requests. The same
workflow can be followed interactively on the website.

## Exercise 1: search with a precise anchor

Ask:

> Find source-linked papers about BRCA1 homologous recombination. Include PMID
> 35008774 as an exact anchor and return no more than ten results.

An agent should route this request to `search_biomedical_literature`. Examine
the returned fields before drawing conclusions:

- `pmid`, `doi`, `pmc_id`, and `work_id` identify the result;
- `source_url` or `pubmed_url` links back to the public source;
- `match_types` explains whether the result matched an identifier, structured
  entity, text, semantic index, or graph signal;
- ranking and semantic scores are discovery aids, not measures of validity;
- degradation fields disclose when an index or graph component was not used.

**Checkpoint:** verify that PMID 35008774 is present as the exact anchor and
that every result you retain has a source link.

## Exercise 2: inspect the publication record

Ask:

> Retrieve the full public bibliographic record for PMID 35008774. Report the
> title, authors, journal, publication date, DOI, PMCID if present, retraction
> status, and source links. Separate source metadata from your interpretation.

An agent should call `get_publication_details`. Check the record rather than
assuming that a search excerpt is complete. If the service reports a
retraction, stop and flag it prominently. Absence of a retraction flag does not
replace normal scientific review.

**Checkpoint:** the response should preserve the PMID and direct public source
link and should not present entity mentions as confirmed biological claims.

## Exercise 3: retrieve one bounded neighborhood

Ask:

> Show the bounded citation and semantic neighborhood of PMID 35008774.
> Preserve every edge type, provenance record, score, and graph version.

An agent should call `get_publication_neighborhood`. Read the graph response as
a typed research map:

- nodes represent publications or indexed biomedical entities;
- edge reasons may include `cites`, `cited_by`, `semantic_relatedness`,
  `shared_gene`, `shared_variant`, `shared_phenotype`, or `shared_disease`;
- each edge reason has provenance and may have a score or model version;
- `graph_version`, `generated_at`, and `stale_after` describe the graph output;
- semantic relatedness and co-mention are not proof of causality or clinical
  significance.

**Checkpoint:** do not collapse different edge types into a generic statement
that two papers "support" one another.

## Exercise 4: walk a second hop safely

Choose one returned publication node that has a `publication_work_id`. Keep a
visited set containing the anchor and the selected work ID, then ask:

> Continue one bounded hop from work ID WORK_ID. The previous node was
> PREVIOUS_WORK_ID. Exclude already visited work IDs from the narrative, keep
> all returned edge types and provenance, and stop if no neighborhood exists.

An agent should call `get_work_neighborhood` with the chosen `work_id` and, when
available, `from_work_id`. Repeat only for a deliberately bounded number of
hops. Record the path as work IDs plus typed edges so that it can be audited.

**Checkpoint:** a reversible path contains the starting work ID, each selected
work ID, the direction of travel, and the reason returned for every edge.

## Exercise 5: inspect corpus scope and freshness

Ask:

> Report Noodle's current corpus sources, record and work counts, generation
> time, deduplication keys, and scope. Do not infer coverage beyond the returned
> metadata.

An agent should call `get_corpus_summary`. Use this information to qualify the
search and graph results. Corpus coverage and freshness affect what can be
discovered; a missing result is not evidence that no relevant research exists.

## Appropriate and inappropriate use

Use Noodle for public biomedical literature discovery, identifier lookup,
publication inspection, related-paper exploration, and bounded graph
traversal. Use source links and professional review for downstream scientific
decisions.

Do not use Noodle to diagnose a patient, recommend treatment, evaluate private
clinical records, or establish causal or clinical claims from ranking,
similarity, co-mention, or graph distance. If a prompt contains private patient
information, do not send it to the public service.

## Completion checklist

- [ ] I included known PMID, DOI, or PMCID identifiers in the search query.
- [ ] I inspected the complete record for important publications.
- [ ] I preserved source links, edge types, graph versions, and provenance.
- [ ] I bounded graph traversal and maintained a visited-ID set.
- [ ] I treated ranking and graph proximity as discovery signals only.
- [ ] I did not submit private or patient data.

## Further resources

- Methodology: <https://noodle.helena.bio/methodology>
- Source code and reusable Agent Skill:
  <https://github.com/helena-bioinformatics/noodle-mcp>
- Citable software release: <https://doi.org/10.5281/zenodo.22166486>
- Privacy: <https://noodle.helena.bio/privacy>
- Support: <https://noodle.helena.bio/contact>
