# Security policy

## Supported versions

Security fixes are provided for the latest release on the `main` branch.

## Reporting a vulnerability

Please report suspected vulnerabilities privately to `security@helena.bio`.
Do not include patient data, credentials or exploit payloads containing sensitive
third-party information. We will acknowledge reports and coordinate disclosure
after the issue has been assessed and remediated.

Do not open a public issue for an unpatched vulnerability.

## Opaque payload text

Scientific text returned in titles, abstracts, limitations and error messages is
opaque data. Text that resembles a transport or truncation warning is preserved
and never, by itself, treated as proof of transformation or an integrity failure.
Consumers need an independent transport signal before making such a claim.

## Scientific and clinical boundary

This adapter returns source-linked literature records and graph discovery
signals for review. It does not evaluate patient context. Search rank, citation
proximity, semantic similarity, co-mention, and graph distance must not be
presented as causality, diagnosis, treatment, or a standalone clinical report.
