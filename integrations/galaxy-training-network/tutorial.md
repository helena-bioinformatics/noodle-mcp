---
layout: tutorial_hands_on
title: From a germline variant to its literature neighborhood with Folklore and Noodle
zenodo_link: ''
questions:
  - How can a public variant record lead to a reproducible literature search?
objectives:
  - Retrieve one structured variant-evidence result.
  - Search and inspect related biomedical publications.
  - Preserve the scientific safety boundaries in downstream analysis.
time_estimation: 45M
key_points:
  - Variant-level output is not a diagnosis or standalone clinical report.
  - Literature ranking and graph proximity do not establish causality.
contributors:
  - helena-bioinformatics
---

# Introduction

This tutorial combines two public, read-only Helena Bioinformatics services.
Folklore retrieves evidence for one supported GRCh38 germline SNV or simple
indel. Noodle searches a public PubMed-derived corpus and exposes bounded
citation or semantic neighborhoods. Both return provenance-rich structured
results, but neither evaluates patient context or provides treatment advice.

> <agenda-title>Agenda</agenda-title>
>
> 1. Interpret a demonstration variant with Folklore.
> 2. Select publication identifiers from the result.
> 3. Search Noodle for the variant, gene, or PMID.
> 4. Review provenance, retraction state, and graph limitations.

# Variant evidence

> <hands-on-title>Retrieve the demonstration variant</hands-on-title>
>
> 1. Add **Folklore Clinical Variant Interpretation** to the history.
> 2. Set **GRCh38 germline variant** to `chr17:43124028 CTC>C`.
> 3. Run the tool.
> 4. Confirm that the output contains `contract_version`, `result`, and
>    `usage_boundary`.
> 5. Record the resolved canonical identity and any cited PMIDs.

> <question-title>Check your understanding</question-title>
>
> 1. Does a resolved identity mean that the result is a clinical diagnosis?
> 2. Why must ambiguous and not-found outcomes be retained rather than replaced
>    with a model-generated interpretation?
>
> > <solution-title>Solution</solution-title>
> > 1. No. The output is automated variant-level evidence for professional
> >    review and does not evaluate a patient.
> > 2. Replacing a bounded outcome would hide uncertainty and break provenance.

# Literature discovery

> <hands-on-title>Search the biomedical corpus</hands-on-title>
>
> 1. Add **Noodle Biomedical Literature Discovery**.
> 2. Search for `BRCA1 homologous recombination` or use one PMID observed in the
>    Folklore result as an exact anchor.
> 3. Set **Maximum results** to `10` and **Result order** to `Relevance`.
> 4. Run the tool and inspect `results`, `match_types`, `semantic_index_used`,
>    and any graph fields.
> 5. Follow a PMID to its canonical PubMed record before drawing a scientific
>    conclusion.

# Interpretation boundary

Search rank, co-mention, citation proximity, semantic similarity, and graph
distance are discovery signals. They are not evidence strength, support,
contradiction, or causality. Review retractions, source rights, publication
dates, study design, and the primary text before using a result in research.

# Conclusion

The workflow provides a reproducible route from one public variant identifier
to structured evidence and relevant literature while keeping normalization,
uncertainty, provenance, and professional review explicit.
