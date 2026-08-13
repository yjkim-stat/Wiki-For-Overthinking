# RLOO

<!-- auto:begin -->

REINFORCE Leave-One-Out, a critic-free policy-gradient method that estimates each sample's baseline from the other samples in its group. In the archive it appears only as a comparison point: among six RLVR algorithms it shows only minor variation in how far it closes the gap to the base model's pass@k bound, and it sits in the same entropy-dynamics family as the rest. Its leave-one-out baseline is the same group-relative idea GRPO uses, which is part of why the archive's sources find these methods behave alike.

- **Kind**: method
- **Also called**: REINFORCE Leave-One-Out
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [advantage function](../concepts/advantage-function.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [Clip-Cov](clip-cov.md), [clip-higher](clip-higher.md), [covariance of probability and advantage](../concepts/covariance-of-probability-and-advantage.md), [DAPO](dapo.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [entropy bonus](../concepts/entropy-bonus.md), [entropy collapse](../concepts/entropy-collapse.md), [entropy regularization](entropy-regularization.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [HumanEval+](../datasets/humaneval.md), [KL-Cov](kl-cov.md), [KodCode](../datasets/kodcode.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [MATH500](../datasets/math500.md), [MathVista](../datasets/mathvista.md), [Minerva](../datasets/minerva.md), [Mistral-7B](../models/mistral-7b.md), [OlympiadBench](../datasets/olympiadbench.md), [Omni-MATH](../datasets/omni-math.md), [pass@k](pass-k.md), [performance ceiling](../concepts/performance-ceiling.md), [policy entropy](../concepts/policy-entropy.md), [policy gradient](policy-gradient.md), [PPO](ppo.md), [PRIME](prime.md), [Qwen2.5-14B](../models/qwen2-5-14b.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [reasoning boundary](../concepts/reasoning-boundary.md), [reasoning distillation](reasoning-distillation.md), [REINFORCE](reinforce.md), [RLVR](rlvr.md), [scaling laws](../concepts/scaling-laws.md), [softmax policy](../concepts/softmax-policy.md), [tabular softmax parameterization](../concepts/tabular-softmax-parameterization.md), [token-level entropy](../concepts/token-level-entropy.md), [VeRL](verl.md)

## Appears in

- [The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models](../../archive/papers/2025/local-5175928072823010/summary.md) — Establishes that RL trades policy entropy for reward along a predictable exponential curve R = -a·exp(H) + b, derives that entropy change is driven by the covariance between action probability and advantage, and controls it by restricting updates to the highest-covariance tokens.
- [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](../../archive/papers/2025/local-b050d2841cbb4959/summary.md) — Measures RLVR-trained models against their base models with pass@k at large k and finds the base wins, concluding RLVR sharpens sampling toward paths the base already had rather than adding new ones.
- [A Comparative Theoretical Analysis of Entropy Control Methods in Reinforcement Learning for Reasoning Language Models](../../archive/papers/2026/local-ed740509686ff305/summary.md) — Proves that an entropy bonus permanently moves the stationary point of RL training while covariance-targeted control reaches the unregularized optimum once its coefficient is annealed, and that the bonus shrinks the stability margin where the targeted methods leave it intact.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
