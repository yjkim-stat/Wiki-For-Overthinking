# coverage

<!-- auto:begin -->

How much of the space of correct solutions a model can reach at all, as distinct from how often it reaches one. The two sources use the idea at opposite ends of training. Measured by pass@k at large k, base models cover more than their RLVR-trained descendants, which is the basis for reading RLVR as sharpening the sampling distribution toward paths the base already had rather than adding new ones. In distillation, coverage is a property of the supervision rather than of the policy: teacher-preferred tokens the student rarely samples are never reached by an on-policy update, and 95.5 percent of such deficit positions have under a one percent chance of appearing in sampled supervision -- which is why that paper injects teacher probability mass analytically rather than waiting for those positions to be drawn. Neither source defines coverage formally; between them they establish that a training signal restricted to what the current policy samples cannot expand what it samples, which is the same constraint in both settings.

- **Kind**: concept
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Brumo](../datasets/brumo.md), [CMIMC](../datasets/cmimc.md), [credit assignment](credit-assignment.md), [DAPO](../methods/dapo.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [degenerate generation](degenerate-generation.md), [entropy collapse](entropy-collapse.md), [exploration-exploitation trade-off](exploration-exploitation-trade-off.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [HMMT](../datasets/hmmt.md), [HumanEval+](../datasets/humaneval.md), [knowledge distillation](../methods/knowledge-distillation.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MathVision](../datasets/mathvision.md), [MathVista](../datasets/mathvista.md), [Minerva](../datasets/minerva.md), [OlympiadBench](../datasets/olympiadbench.md), [on-policy distillation](../methods/on-policy-distillation.md), [pass@k](pass-k.md), [PPO](../methods/ppo.md), [Qwen2.5-14B](../models/qwen2-5-14b.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [Qwen3-1.7B-Base](../models/qwen3-1-7b-base.md), [Qwen3-8B](../models/qwen3-8b.md), [reasoning boundary](reasoning-boundary.md), [reasoning distillation](../methods/reasoning-distillation.md), [REINFORCE](../methods/reinforce.md), [reward hacking](reward-hacking.md), [reward shaping](reward-shaping.md), [RLOO](../methods/rloo.md), [RLVR](../methods/rlvr.md), [teacher-student gap](teacher-student-gap.md), [token selection](token-selection.md)

## Appears in

- [Mismatch Matters: On-Policy Distillation Beyond Token Agreement](../../archive/papers/2026/arxiv-2608-09836/summary.md) — Identifies degenerate agreement -- students reaching near-perfect token agreement with a teacher by looping while the response as a whole is broken -- and replaces the agreement objective with two directional mismatch corrections, one bounding runaway excess tokens and one injecting teacher-preferred mass at positions the student almost never samples.
- [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](../../archive/papers/2025/local-b050d2841cbb4959/summary.md) — Measures RLVR-trained models against their base models with pass@k at large k and finds the base wins, concluding RLVR sharpens sampling toward paths the base already had rather than adding new ones.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
