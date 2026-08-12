# retrieval-augmented generation

<!-- auto:begin -->

Conditioning generation on retrieved documents so that answers are grounded in supplied evidence rather than in parameters. The two sources use the term for different things, which is worth noting because the archive holds only these two. One treats RAG as the deployment setting needing a guardrail, training a 4B model to classify document-claim pairs as grounded or hallucinated in closed-book document-grounded settings. The other uses retrieval as a contrast case in a mechanistic study of how transformers come to reason implicitly over stored facts. Grounding on retrieved text does not guarantee the answer follows from it, which is the gap the first source addresses.

- **Kind**: method
- **Also called**: RAG, retrieval augmentation
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [causal analysis](causal-analysis.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [circuit analysis](circuit-analysis.md), [GPT-4o](../models/gpt-4o.md), [hallucination](../concepts/hallucination.md), [implicit reasoning](../concepts/implicit-reasoning.md), [memorization](../concepts/memorization.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [reasoning distillation](reasoning-distillation.md), [synthetic data generation](synthetic-data-generation.md), [verification](../concepts/verification.md)

## Appears in

- [HalluGuard: Evidence-Grounded Small Reasoning Models to Mitigate Hallucinations in Retrieval-Augmented Generation](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-835/summary.md) — A 4B small reasoning model that classifies document-claim pairs as grounded or hallucinated for RAG pipelines and produces evidence-grounded justifications.
- [Grokked Transformers are Implicit Reasoners: A Mechanistic Journey to the Edge of Generalization](../../archive/papers/2024/local-6252abed1b134f57/summary.md) — Shows that transformers can learn implicit multi-step reasoning over stored knowledge, but only through grokking — extended training far past overfitting — and that whether the resulting circuit generalizes out of distribution depends on the reasoning type, succeeding for comparison and failing for composition.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
