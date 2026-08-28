# LSAT

<!-- auto:begin -->

LSAT (logical reasoning and reading comprehension) is used in these sources as a general, non-mathematical out-of-domain benchmark for efficient-reasoning methods: CLARO reports it among eight benchmarks (alongside GPQA and MMLU) used to validate that its structural-attribute optimization generalizes beyond math, and SAS (Step-level Advantage Selection) similarly evaluates its short-context-training method's out-of-domain generalization on LSAT.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC](amc.md), [DeepScaleR-1.5B-Preview](../models/deepscaler-1-5b-preview.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [GPQA](gpqa.md), [GPQA-Diamond](gpqa-diamond.md), [GRPO](../methods/grpo.md), [MATH](math.md), [MATH500](math500.md), [MMLU](mmlu.md), [OlympiadBench](olympiadbench.md), [Overthinking](../concepts/overthinking.md)

## Appears in

- [Stabilizing Efficient Reasoning with Step-Level Advantage Selection](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1333/summary.md) — Shows that short-context (4K-token) post-training alone -- with pure GRPO and no length-aware reward at all -- already induces reasoning compression comparable to dedicated length-control RL methods, isolating training context length as a confound in prior efficient-reasoning work; but this compression destabilizes training because truncated-yet-correct rollouts get zero reward, so Step-level Advantage Selection (SAS) zeros the advantage of low-confidence steps in correct rollouts and high-confidence steps in verifier-failed rollouts, cutting average reasoning length 30%+ while improving Pass@1 by 3.79 points over the strongest length-aware baseline.
- [CLARO: Controlled Attribute-Driven Reasoning Optimization for Efficient Chain-of-Thought](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1335/summary.md) — CLARO treats conciseness as an emergent property of well-structured reasoning rather than a truncation target: it fine-tunes models via GRPO with two correctness-gated reward terms (structural attribute alignment -- readability, mathematical-notation density, syntactic compression, low redundancy -- plus a length-contribution term) within a user-specified token budget, outperforming length-controlled baselines (s1, L1-Max) by up to 63.6% relative accuracy under matched budgets across eight math and general-reasoning benchmarks, while a lightweight zero-shot prompting variant (Attribute-Guided Prompting) is shown to be far more robust than simply instructing a model to 'prioritize conciseness.'

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
