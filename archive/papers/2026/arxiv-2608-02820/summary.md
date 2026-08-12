<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Evading Chain-of-Thought Monitoring Through Model Poisoning

- **Authors**: Giorgio Severi, Shujaat Mirza, Blake Bullwinkel, Amanda Minnich
- **Venue**: cs.CR
- **Published**: 2026-08-03
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.02820>
- **PDF**: <https://arxiv.org/pdf/2608.02820v1>
- **Topics**: reasoning-faithfulness, reasoning-training, test-time-scaling
- **Relevance score**: reasoning-faithfulness 0.57, reasoning-interpretability 0.25, reasoning-training 0.57, test-time-scaling 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Chain-of-thought (CoT) monitoring is an increasingly important component of AI safety stacks but relies on the assumption that a model's reasoning trace is informative about its actions. This work studies the limits of CoT monitoring through the lens of model poisoning. We demonstrate that backdoors can be implanted into reasoning models to elicit an attacker-chosen behavior while their CoT traces appear entirely benign. We find that these CoT-Hidden backdoors can be induced through simple fine-tuning recipes across reasoning-model architectures and sizes. When direct poisoning is ineffective, we introduce a curriculum training approach that progressively teaches the model to produce an attacker-chosen output while concealing the behavior from its reasoning traces. These findings suggest that CoT monitoring may be better framed as a question about the consistency between a model's reasoning trace and its final response than as anomaly detection within a trace. We further examine the mechanisms that allow models to suppress evidence of the target behavior from their reasoning traces. Causal interventions locate a trigger-conditioned activation pathway that does not depend on the visible reasoning, and residual stream verbalizations provide an anomaly warning near answer generation, but do not identify the trigger, target, or backdoor mechanism.

---

Record id: `arxiv:2608.02820`
