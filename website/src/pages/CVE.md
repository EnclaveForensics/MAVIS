---
layout: ../layouts/Basic.astro
title: Known Vulnerabilities via CVEs
---
The CVE (Common Vulnerabilities and Exposures) database is a publicly accessible repository of standardized identifiers for known cybersecurity vulnerabilities. Managed by the MITRE Corporation and sponsored by the U.S. Department of Homeland Security, it provides a unique CVE ID for each disclosed vulnerability, along with metadata such as a brief description, affected software or hardware, and references to more detailed reports or patches.

Relationship to Vulnerable Source Code
The CVE database often includes or references:

Descriptions of flaws in software, which can be traced back to specific segments of vulnerable source code.

Affected versions, helping developers locate problematic code within particular commits or releases.

Mitigations or patches, which show how the vulnerable code was modified to fix the issue.

Security tools, researchers, and developers use CVE entries to:

Identify known vulnerabilities in codebases.

Prioritize patches based on CVSS scores (Common Vulnerability Scoring System, often linked in CVEs).

Train models to detect insecure coding patterns by using examples tied to CVE-tagged flaws.

In essence, the CVE database serves as a bridge between abstract vulnerability knowledge and the concrete, often publicly available, instances of insecure source code.

An unreleased portion of MAVIS is used to continuously track CVEs, identify open source vulnerabilities, identify the vulnerable portions of a project, and generate vector embeddings for the vulnerable code. A major part of what *is* released via MAVIS is the vector database for these known-flawed code samples.