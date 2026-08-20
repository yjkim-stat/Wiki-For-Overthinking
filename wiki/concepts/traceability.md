# traceability

<!-- auto:begin -->

Whether a model's output can be followed back to the specific evidence it rests on. Both sources treat it as something to be built into the task rather than inspected afterwards. One makes it structural: every reasoning step is a node in a graph anchored to a document block, so the answer carries node-level provenance by construction, and the resulting graph is validated causally by masking what it cites (82.8% of correct answers flip) against what it does not (9.6%). The other builds a benchmark that scores the reasoning process alongside the answer, with expert solutions supplied for 46% of items. The pair marks the two available routes — force the model to emit an inspectable structure, or supply ground-truth reasoning to score against — and only the first is checkable without expert annotation.

- **Kind**: concept
- **Also called**: auditability of outputs, provenance
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [abstention](abstention.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Claude-3.7-Sonnet](../models/claude-3-7-sonnet.md), [counterfactual intervention](../methods/counterfactual-intervention.md), [Gemini-1.5-Pro](../models/gemini-1-5-pro.md), [Gemini-3.1-Pro](../models/gemini-3-1-pro.md), [GPT-4.1](../models/gpt-4-1.md), [GPT-4o](../models/gpt-4o.md), [GPT-5.5](../models/gpt-5-5.md), [grounding](grounding.md), [GRPO](../methods/grpo.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [multi-hop reasoning](multi-hop-reasoning.md), [multimodal reasoning](multimodal-reasoning.md), [process evaluation](process-evaluation.md), [process reward](process-reward.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [synthetic data generation](../methods/synthetic-data-generation.md)

## Appears in

- [DocTrace: Towards Traceable Long Document VQA via Hierarchical Evidence Graph Reasoning](../../archive/papers/2026/arxiv-2608-03292/summary.md) — Recasts long-document visual question answering as building an explicit evidence graph whose nodes are grounded document blocks and whose edges are reasoning dependencies, and verifies the graph causally — masking the evidence it cites flips 82.8% of correct answers while masking uncited evidence changes 9.6%.
- [SciVQR: A Multidisciplinary Multimodal Benchmark for Advanced Scientific Reasoning Evaluation](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-28/summary.md) — A multimodal scientific reasoning benchmark over 54 subfields with domain-specific visuals and expert solutions for 46% of items, scoring the reasoning process as well as the answer.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
