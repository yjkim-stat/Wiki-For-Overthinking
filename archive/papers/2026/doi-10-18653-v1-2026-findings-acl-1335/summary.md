<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# CLARO: Controlled Attribute-Driven Reasoning Optimization for Efficient Chain-of-Thought

- **Authors**: Oded Schlesinger, Young Kyung Kim, J. Matias Di Martino, Guillermo Sapiro
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1335/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1335.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1335
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large language models exhibit strong reasoning capabilities but often require significant computational resources due to verbose, unstructured Chain-of-Thought outputs. Recent approaches guide reasoning length through token penalties or truncation, risking the omission of necessary steps. We posit that conciseness should be an emergent property of structured thought, rather than a result of artificially forced brevity. To this end, we first demonstrate that Attribute-Guided Prompting, a lightweight zero-shot strategy, improves reasoning performance while reducing inference cost. Building on this foundation, we introduce Controlled Attribute-Driven Reasoning Optimization (CLARO), a reinforcement learning framework designed to internalize these benefits. CLARO guides models to embed high-quality structural attributes, such as readability, math density, syntactic compression, and low redundancy, within a user-defined token budget. The proposed method outperforms state-of-the-art baselines across diverse benchmarks, yielding accuracy gains of up to 63.6%, demonstrating that guiding generated output language structure enhances reasoning. Overall, our findings establish that optimizing the thought process structure refines reasoning efficacy, with computational efficiency emerging as a derivative benefit of a clearer thought process. Code and models are available at https://github.com/odedsc/CLARO.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1335`
