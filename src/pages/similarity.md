---
layout: ../layouts/Basic.astro
title: Measuring Similarity
---
Similarity between code vectors in MAVIS is measured using **Cosine Similarity**. **Cosine similarity** is a metric used to measure how similar two vectors are, based on the **angle between them** in a multi-dimensional space, rather than their magnitude.

### Formula:

$$
\text{cosine\_similarity}(A, B) = \frac{A \cdot B}{\|A\| \|B\|}
$$

Where:

* $A \cdot B$ is the **dot product** of vectors $A$ and $B$
* $\|A\|$ and $\|B\|$ are the **Euclidean norms** (lengths) of the vectors

### Key Properties:

* The result ranges from **–1 to 1**

  * **1** means vectors are in the **same direction** (high similarity)
  * **0** means vectors are **orthogonal** (no similarity)
  * **–1** means vectors are in **opposite directions**

### Why Use Cosine Similarity?

It focuses on **orientation**, not magnitude, making it useful for:

* **Text similarity** (e.g., comparing word or sentence embeddings)
* **Recommendation systems**
* **Clustering** in high-dimensional spaces

Because it's unaffected by vector length, cosine similarity is ideal when input vectors vary in scale but direction encodes meaning. This should perform well since MAVIS seeks to identify code *intent* rather than attempting to scan for known vulnerable patterns or signatures, making MAVIS more powerful than many other code analysis solutions; it should also prove more difficult to fool, whether intentionally or unintentionally.
