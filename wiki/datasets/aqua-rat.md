# AQuA-RAT

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: dataset
- **Also called**: AQuA-Rat
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [Ada-GRPO](../methods/ada-grpo.md), [adaptive reasoning format selection](../concepts/adaptive-reasoning-format-selection.md), [AIME 2025](aime-2025.md), [BBH](bbh.md), [CommonsenseQA](commonsenseqa.md), [format collapse](../concepts/format-collapse.md), [GPQA](gpqa.md), [GPQA-Diamond](gpqa-diamond.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [GRPO](../methods/grpo.md), [GRPO (baseline)](../methods/grpo-baseline.md), [GSM8K](gsm8k.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama 3.3 70B](../models/llama-3-3-70b.md), [MATH](math.md), [MATH500](math500.md), [MMLU-Pro](mmlu-pro.md), [MMMU](mmmu.md), [OpenBookQA](openbookqa.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5 7B](../models/qwen2-5-7b.md), [Self-Consistency (SC, baseline)](../methods/self-consistency-sc-baseline.md), [StrategyQA](strategyqa.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md), [SVAMP](svamp.md), [Token Budget](../concepts/token-budget.md), [weighted majority voting](../concepts/weighted-majority-voting.md)

## Appears in

- [VecCISC: Improving Confidence-Informed Self-Consistency with Reasoning Trace Clustering and Candidate Answer Selection](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1305/summary.md) — VecCISC reduces the cost of Confidence-Informed Self-Consistency (CISC) -- which needs a separate critic-LLM call on every sampled reasoning trace to weight majority voting -- by embedding traces, clustering them per candidate answer, and sending only cluster-representative (nearest-centroid) traces to the critic, cutting critic calls 30-35% and total pipeline token usage 47% while matching or exceeding CISC's accuracy across five models and five datasets.
- [ARM2: Adaptive Reasoning Model with Vision Understanding and Executable Code](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1365/summary.md) — ARM2 extends adaptive reasoning-format selection (Direct Answer, Short CoT, Code-Text, Code-Exec, Long CoT) to multimodal (vision) inputs and lets executable code substitute for lengthy chain-of-thought on tasks with verifiable computation, trained via GRPO-alp (a format-collapse-resistant, length-aware GRPO variant), reducing token usage over 70% versus standard GRPO while matching its accuracy across six in-domain and six out-of-domain text and multimodal benchmarks.
- [ARM: Adaptive Reasoning Model](../../archive/papers/2025/title-21d562149c3adad6/summary.md) — ARM trains a model to pick among four reasoning formats (Direct Answer, Short CoT, Code, Long CoT) per task using Ada-GRPO, cutting average tokens by about 30% at roughly unchanged accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
