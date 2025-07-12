---
layout: ../layouts/Basic.astro
title: LLM Hallucinations
---
In the context of a **Large Language Model (LLM)**, a **hallucination** is when the model generates information that is **factually incorrect**, **fabricated**, or **not grounded in the input or training data**—even though it may sound plausible.

### Example:

> **Prompt:** "In what year did Einstein discover oxygen?"
> **Hallucinated Answer:** "Albert Einstein discovered oxygen in 1920." 

### Causes:

* The model tries to "fill in the blanks" based on patterns, not actual facts.
* Lack of access to real-time or verified knowledge.
* Ambiguous or incomplete prompts.

### Types:

* **Factual errors** (wrong dates, names, etc.)
* **Fabricated sources or citations**
* **Inaccurate code, logic, or math**

Hallucinations are a key limitation in using LLMs for tasks requiring high accuracy or trust.
