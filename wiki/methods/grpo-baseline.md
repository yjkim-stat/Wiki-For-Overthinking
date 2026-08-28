# GRPO (baseline)

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [adaptive reasoning format selection](../concepts/adaptive-reasoning-format-selection.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [AQuA-RAT](../datasets/aqua-rat.md), [CommonsenseQA](../datasets/commonsenseqa.md), [DAPO (baseline)](dapo-baseline.md), [DeepScaler (training)](deepscaler-training.md), [format collapse](../concepts/format-collapse.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [HMMT25](../datasets/hmmt25.md), [Llama3.1-8B-Instruct](../models/llama3-1-8b-instruct.md), [MATH500](../datasets/math500.md), [MMMU](../datasets/mmmu.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [Qwen3-8B-Base](../models/qwen3-8b-base.md)

## Appears in

- [Miner: Mining Intrinsic Mastery for Data-Efficient RL in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-237/summary.md) — MINER recovers training signal from 'positive homogeneous' (PH) prompts -- where all sampled RLVR rollouts are already correct and GRPO-style advantage collapses to zero, wasting the rollout budget -- by converting the policy's own per-token uncertainty (negative log-likelihood) into an intrinsic reward that reinforces under-confident-but-correct reasoning paths, combined with token-level focal credit assignment and adaptive advantage calibration, achieving up to +4.58 Pass@1 and +6.66 Pass@K over GRPO with zero extra rollouts or inference cost.
- [ARM2: Adaptive Reasoning Model with Vision Understanding and Executable Code](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1365/summary.md) — ARM2 extends adaptive reasoning-format selection (Direct Answer, Short CoT, Code-Text, Code-Exec, Long CoT) to multimodal (vision) inputs and lets executable code substitute for lengthy chain-of-thought on tasks with verifiable computation, trained via GRPO-alp (a format-collapse-resistant, length-aware GRPO variant), reducing token usage over 70% versus standard GRPO while matching its accuracy across six in-domain and six out-of-domain text and multimodal benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
