---
layout: ../layouts/Layout.astro
---
MAVIS is the **M**achine **A**ssisted **V**ulnerability **I**dentification **S**ystem, an innovative and unique approach to identifying potentially vulnerable code at the source code level by leveraging artitificial intelligence and machine learning techniques.

-----
Mavis uses a [pre-trained](pretraining) [embedding model](embeddings) to vectorize the [abstract syntax tree](ast) for code as it is checked into a git repository to identify potential code vulnerabilities by identifying [known vulnerable code](CVE) [similarity](similarity). The initial free release provides everything necessary to automatically detect potential flaws in C code. Additional language support will be provided over time.

The approach used by MAVIS is significantly different than most (if not all) other AI based source code vulnerability scanning tools, which typically attempt to leverage an [LLM (Large Language Model)](LLM) or a [fine-tuned LLM](finetuning) to attempt to identify flaws. This approach is very interesting, but much more expensive (computationally and financially), less accurate, and vulnerable to hallucination.