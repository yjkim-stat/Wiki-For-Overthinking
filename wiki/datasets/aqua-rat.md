# AQuA-RAT

<!-- auto:begin -->

AQuA-RAT is a multiple-choice algebraic word-problem dataset used in these sources to evaluate test-time-scaling aggregation and adaptive-reasoning methods: VecCISC evaluates its clustering-based confidence-informed self-consistency reduction on it (among five QA datasets), and it is one of the source domains ARM/ARM2's adaptive-format training draws on.

- **Kind**: dataset
- **Also called**: AQuA-Rat
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [activation steering](../methods/activation-steering.md), [Ada-GRPO](../methods/ada-grpo.md), [adaptive reasoning format selection](../methods/adaptive-reasoning-format-selection.md), [AIME 2025](aime-2025.md), [BBH](bbh.md), [ChartQA](chartqa.md), [CommonsenseQA](commonsenseqa.md), [Confidence-Informed Self-Consistency (CISC, baseline)](../methods/confidence-informed-self-consistency-cisc-baseline.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER (baseline)](../methods/deer-baseline.md), [format collapse](../concepts/format-collapse.md), [GPQA](gpqa.md), [GPQA-Diamond](gpqa-diamond.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [GRPO](../methods/grpo.md), [GRPO (baseline)](../methods/grpo-baseline.md), [GSM8K](gsm8k.md), [GSM8K-Hard](gsm8k-hard.md), [LiveCodeBench](livecodebench.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama 3.3 70B](../models/llama-3-3-70b.md), [MATH](math.md), [MATH500](math500.md), [MMLU-Pro](mmlu-pro.md), [MMMU](mmmu.md), [OpenBookQA](openbookqa.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5 7B](../models/qwen2-5-7b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [QwQ-32B](../models/qwq-32b.md), [SEAL (baseline)](../methods/seal-baseline.md), [Self-Consistency (SC, baseline)](../methods/self-consistency-sc-baseline.md), [StrategyQA](strategyqa.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md), [SVAMP](svamp.md), [Token Budget](../concepts/token-budget.md), [weighted majority voting](../methods/weighted-majority-voting.md)

## Appears in

- [VecCISC: Improving Confidence-Informed Self-Consistency with Reasoning Trace Clustering and Candidate Answer Selection](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1305/summary.md) — VecCISC reduces the cost of Confidence-Informed Self-Consistency (CISC) -- which needs a separate critic-LLM call on every sampled reasoning trace to weight majority voting -- by embedding traces, clustering them per candidate answer, and sending only cluster-representative (nearest-centroid) traces to the critic, cutting critic calls 30-35% and total pipeline token usage 47% while matching or exceeding CISC's accuracy across five models and five datasets.
- [ARM2: Adaptive Reasoning Model with Vision Understanding and Executable Code](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1365/summary.md) — ARM2 extends adaptive reasoning-format selection (Direct Answer, Short CoT, Code-Text, Code-Exec, Long CoT) to multimodal (vision) inputs and lets executable code substitute for lengthy chain-of-thought on tasks with verifiable computation, trained via GRPO-alp (a format-collapse-resistant, length-aware GRPO variant), reducing token usage over 70% versus standard GRPO while matching its accuracy across six in-domain and six out-of-domain text and multimodal benchmarks.
- [Activation Steering for Chain-of-Thought Compression](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1828/summary.md) — Shows via t-SNE that verbose and concise chains-of-thought occupy visibly separable regions of a reasoning model's intermediate activation space, then learns a single, KL-trust-region-constrained steering vector (Contrastive Energy-Based Steering, CES) from only 100 verbose-concise CoT pairs by ranking concise traces below verbose ones in length-normalized energy under the steered model -- Activation-Steered Compression (ASC) cuts CoT length up to 69.35% with no accuracy loss across four model scales and multiple benchmarks, achieves 2.7x end-to-end wall-clock speedup, generalizes cross-task with 0.92 cosine similarity between dataset-specific steering vectors, and mitigates a documented 'underthinking' failure mode (excessive backtracking/path-switching without commitment) in QwQ-32B specifically.
- [ARM: Adaptive Reasoning Model](../../archive/papers/2025/title-21d562149c3adad6/summary.md) — ARM trains a model to pick among four reasoning formats (Direct Answer, Short CoT, Code, Long CoT) per task using Ada-GRPO, cutting average tokens by about 30% at roughly unchanged accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
