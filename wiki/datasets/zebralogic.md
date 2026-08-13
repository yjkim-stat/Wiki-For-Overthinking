# ZebraLogic

<!-- auto:begin -->

A benchmark of constraint-satisfaction logic puzzles, used in both sources as the non-mathematical reasoning task that stresses long deductive chains. Two findings attach to it: activation probes for the commitment boundary transfer to it from mathematics training with the smallest accuracy cost of any out-of-distribution set (97% to 86%) but also the smallest token savings (6%), and it is the one dataset where the leading causal-attribution method is beaten by its closest competitor. It is also where the model's dependence on the original problem statement peaks latest in the trace, consistent with harder problems delaying verification.

- **Kind**: dataset
- **Also called**: ZebraLogic
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME 2025](aime-2025.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [commitment boundary](../concepts/commitment-boundary.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [early exit](../methods/early-exit.md), [Gemma-4-26B-A4B-it](../models/gemma-4-26b-a4b-it.md), [GPQA-Diamond](gpqa-diamond.md), [gpt-oss-20b](../models/gpt-oss-20b.md), [GSM8K](gsm8k.md), [linear probe](../methods/linear-probe.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH500](math500.md), [MMLU-Pro](mmlu-pro.md), [monitorability](../concepts/monitorability.md), [overthinking](../concepts/overthinking.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-8B](../models/qwen3-8b.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [verification](../concepts/verification.md)

## Appears in

- [Local Causal Attribution of Chain-of-Thought Reasoning](../../archive/papers/2026/local-6db01f05462cef8e/summary.md) — Fits a structural causal model over the units of a single chain-of-thought trace using leave-one-out interventions and linear regression, producing a pairwise influence matrix between every pair of steps at a cost linear in the number of units.
- [Beyond the Commitment Boundary: Probing Epiphenomenal Chain-of-Thought in Large Reasoning Models](../../archive/papers/2026/local-d6e266929de37684/summary.md) — Measures each CoT step's causal contribution by truncating the trace and forcing an answer, finds reasoning crosses a sharp single-step 'commitment boundary' after which the answer probability stops moving, and trains activation probes to detect that boundary and exit early.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
