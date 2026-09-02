# DeepScaler (training)

<!-- auto:begin -->

'DeepScaler (training)' is referenced in these sources only as an RL training setup/dataset context in which reasoning-efficiency and instruction-following behaviors are studied (e.g. MathIF's finding that reasoning-oriented SFT/RL degrades instruction-following, and MINER's data-efficient RL work), not as something the sources define or characterize directly.

- **Kind**: method
- **Also called**: DeepScaleR (training)
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [DAPO (baseline)](dapo-baseline.md), [DeepScaleR-1.5B-Preview](../models/deepscaler-1-5b-preview.md), [GPT-5](../models/gpt-5.md), [GRPO (baseline)](grpo-baseline.md), [GSM8K](../datasets/gsm8k.md), [HMMT25](../datasets/hmmt25.md), [Llama3.1-8B-Instruct](../models/llama3-1-8b-instruct.md), [MATH500](../datasets/math500.md), [MedQA](../datasets/medqa.md), [Minerva](../datasets/minerva.md), [o3-mini](../models/o3-mini.md), [OlympiadBench](../datasets/olympiadbench.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [Qwen3-8B-Base](../models/qwen3-8b-base.md), [QwQ-32B](../models/qwq-32b.md), [s1-32B](../models/s1-32b.md)

## Appears in

- [Scaling Reasoning, Losing Control: Evaluating Instruction Following in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1878/summary.md) — MathIF is a 420-query, 15-constraint controlled benchmark showing that as large reasoning models' chain-of-thought grows longer via reasoning-oriented SFT/RL, their instruction-following obedience degrades -- even the best open model (Qwen3-14B) satisfies only 50.71% of constraints strictly, and artificially lengthening CoT (budget forcing) or reasoning-oriented training both directly and measurably erode compliance, exposing a persistent intelligence-obedience trade-off.
- [Miner: Mining Intrinsic Mastery for Data-Efficient RL in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-237/summary.md) — MINER recovers training signal from 'positive homogeneous' (PH) prompts -- where all sampled RLVR rollouts are already correct and GRPO-style advantage collapses to zero, wasting the rollout budget -- by converting the policy's own per-token uncertainty (negative log-likelihood) into an intrinsic reward that reinforces under-confident-but-correct reasoning paths, combined with token-level focal credit assignment and adaptive advantage calibration, achieving up to +4.58 Pass@1 and +6.66 Pass@K over GRPO with zero extra rollouts or inference cost.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
