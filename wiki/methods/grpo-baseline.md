# GRPO (baseline)

<!-- auto:begin -->

GRPO (Group Relative Policy Optimization) is used across these sources both as the RL algorithm several efficient-reasoning methods build on (e.g. ARM2's GRPO-alp variant) and as a plain baseline that alternatives are compared against: MINER reports gains of up to +4.58 Pass@1 and +6.66 Pass@K over vanilla GRPO with zero extra rollouts or inference cost, by converting per-token uncertainty on 'positive homogeneous' prompts (where GRPO's advantage collapses to zero) into an intrinsic reward.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [adaptive reasoning format selection](adaptive-reasoning-format-selection.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [AQuA-RAT](../datasets/aqua-rat.md), [ChartQA](../datasets/chartqa.md), [CommonsenseQA](../datasets/commonsenseqa.md), [DAPO (baseline)](dapo-baseline.md), [DeepScaler (training)](deepscaler-training.md), [format collapse](../concepts/format-collapse.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [HMMT25](../datasets/hmmt25.md), [LLaMA-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [MATH500](../datasets/math500.md), [MedQA](../datasets/medqa.md), [MMLU-Pro](../datasets/mmlu-pro.md), [MMMU](../datasets/mmmu.md), [Olympiad](../datasets/olympiad.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-3B-Base](../models/qwen2-5-3b-base.md), [Qwen2.5-7B-Base](../models/qwen2-5-7b-base.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [Qwen3-8B-Base](../models/qwen3-8b-base.md), [SFT (baseline)](sft-baseline.md), [TLMRE (baseline)](tlmre-baseline.md)

## Appears in

- [Miner: Mining Intrinsic Mastery for Data-Efficient RL in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-237/summary.md) — MINER recovers training signal from 'positive homogeneous' (PH) prompts -- where all sampled RLVR rollouts are already correct and GRPO-style advantage collapses to zero, wasting the rollout budget -- by converting the policy's own per-token uncertainty (negative log-likelihood) into an intrinsic reward that reinforces under-confident-but-correct reasoning paths, combined with token-level focal credit assignment and adaptive advantage calibration, achieving up to +4.58 Pass@1 and +6.66 Pass@K over GRPO with zero extra rollouts or inference cost.
- [ARM2: Adaptive Reasoning Model with Vision Understanding and Executable Code](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1365/summary.md) — ARM2 extends adaptive reasoning-format selection (Direct Answer, Short CoT, Code-Text, Code-Exec, Long CoT) to multimodal (vision) inputs and lets executable code substitute for lengthy chain-of-thought on tasks with verifiable computation, trained via GRPO-alp (a format-collapse-resistant, length-aware GRPO variant), reducing token usage over 70% versus standard GRPO while matching its accuracy across six in-domain and six out-of-domain text and multimodal benchmarks.
- [ADaPT: Token-Level Decoupling for Efficient Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-165/summary.md) — ADaPT diagnoses that existing efficiency-oriented RL methods fail because sequence-level efficiency rewards implicitly penalize correct-but-long reasoning (a structural mismatch, since only the first token -- the fast/slow mode choice -- actually determines efficiency, while all subsequent tokens can only affect correctness), and fixes this by applying an efficiency reward exclusively to a dedicated mode-selection <think>/<answer> token via a CISPO-stabilized token-level GRPO variant -- cutting Qwen2.5-7B's average generation length from 1540 to 1031 tokens (SFT+GRPO baseline) with only a 0.4-point accuracy drop, tracing a genuine Pareto frontier other methods stay strictly inside, and letting a single trained model's efficiency be tuned post-hoc by adjusting the mode-token's decoding threshold with no retraining.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
