# DeepScaleR-preview (training)

<!-- auto:begin -->

DeepScaleR-preview (training) is named only in a training context by this archive's sources -- GRIP's reward-guided parameter-interpolation method and Anti-Length Shift's outlier-truncation (DOT) method for efficient reasoning both reference it alongside their own training setups -- without further characterization of what it is beyond that training-time role.

- **Kind**: dataset
- **Also called**: DeepScaleR-Preview (training)
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [GPQA-D](gpqa-d.md), [GPQA-Diamond](gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [HumanEval](humaneval.md), [LiveCodeBench](livecodebench.md), [LiveCodeBench-v6](livecodebench-v6.md), [MATH500](math500.md), [MMLU](mmlu.md), [OlympiadBench](olympiadbench.md), [Qwen3-4B-Instruct-2507](../models/qwen3-4b-instruct-2507.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [TLMRE (baseline)](../methods/tlmre-baseline.md)

## Appears in

- [GRIP: Granular Reward-Guided Parameter Interpolation for Efficient Reasoning](../../archive/papers/2026/arxiv-2608-25583/summary.md) — GRIP fuses a reasoning model and an instruction (non-thinking) model of identical architecture by learning a separate sigmoid-controlled interpolation ratio per module (attention, FFN, embedding/LM-head), trained with an RL reward that favors correct and concise responses while keeping both source models frozen, cutting Qwen3-4B-Thinking's average generation length 27.0% while slightly improving average accuracy.
- [Anti-Length Shift: Dynamic Outlier Truncation for Training Efficient Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1047/summary.md) — Identifies 'length shift' -- reasoning models progressively generate longer responses on already-correctly-solved (zero-gradient) training queries during RLVR, because reasoning-word emission learned for hard problems generalizes indiscriminately to easy ones -- and fixes it with Dynamic Outlier Truncation (DOT), a training-time RL intervention that truncates only the statistical outlier-length tail of all-correct rollout groups (affecting <0.5% of responses) while leaving hard queries unconstrained, cutting AIME-24 token usage 78% while increasing accuracy over the initial policy and beating prior efficient-reasoning methods.
- [AttnPO: Attention-Guided Process Supervision for Efficient Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1845/summary.md) — Discovers Key-Focus Heads (KFHs) -- a small subset of attention heads that, during final-answer generation, naturally attend more to essential reasoning steps than redundant ones -- and builds ATTNPO, an RL framework that rescales GRPO's outcome-level advantage per reasoning step using KFH attention scores, cutting reasoning length 55-61% while improving accuracy +2.9 to +7.3 points on DeepSeek-R1-Distill-Qwen-1.5B/7B.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
