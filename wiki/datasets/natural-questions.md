# Natural Questions

<!-- auto:begin -->

An open-domain question-answering dataset of real search queries, used in this archive as a retrieval-QA workload rather than as a reasoning benchmark. One source pairs it with HotpotQA as the two query sets for measuring per-query latency and energy in edge RAG; another places it with CRAG on the out-of-distribution side of a split whose in-distribution half is HotpotQA and HaluEval. Its single-hop character against HotpotQA's multi-hop one is what both uses rely on.

- **Kind**: dataset
- **Also called**: NQ, NaturalQuestions
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [AIME 2024](aime-2024.md), [Answer Convergence](../concepts/answer-convergence.md), [Concise CoT (CCoT)](../methods/concise-cot-ccot.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [GPQA-Diamond](gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [HotpotQA](hotpotqa.md), [Length Penalty](../concepts/length-penalty.md), [MATH500](math500.md), [Overthinking](../concepts/overthinking.md), [QwQ-32B](../models/qwq-32b.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md)

## Appears in

- [Answer Convergence as a Signal for Early Stopping in Reasoning](../../archive/papers/2025/local-5596d5f3510679fc/summary.md) — Defines the Answer Convergence Ratio — the fraction of a chain of thought needed before the forced answer stops changing — measures it by incremental truncation across five tasks and five models, and proposes three inference-time stopping methods (answer consistency, a logit boost on the end-of-thinking token, and an LSTM probe over activations), of which only the learned probe holds accuracy on hard tasks.
- [Short Chains, Deep Thoughts: Balancing Reasoning Efficiency and Intra-Segment Capability via Split-Merge Optimization](../../archive/papers/2026/title-0bf980e6919c2982/summary.md) — CoSMo restructures reasoning chains by merging redundant segments and splitting logical gaps, then trains with RL against a segment-count budget rather than a token budget.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
