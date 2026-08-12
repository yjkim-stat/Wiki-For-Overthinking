# REINFORCE++

<!-- auto:begin -->

REINFORCE++, a critic-free policy-gradient variant used as one of the RLVR algorithms compared in the archive. Both sources treat it as a member of a family rather than a subject: one includes it among six algorithms whose sampling-efficiency gaps differ only marginally, which is evidence that the choice of critic-free algorithm matters less than the paradigm; the other groups it with the RLVR methods whose entropy dynamics follow the same exponential reward-entropy exchange.

- **Kind**: method
- **Also called**: REINFORCE, REINFORCE++, Reinforce++
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC23](../datasets/amc23.md), [Clip-Cov](clip-cov.md), [clip-higher](clip-higher.md), [covariance of probability and advantage](../concepts/covariance-of-probability-and-advantage.md), [DAPO](dapo.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [entropy bonus](../concepts/entropy-bonus.md), [entropy collapse](../concepts/entropy-collapse.md), [entropy regularization](entropy-regularization.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [HumanEval](../datasets/humaneval.md), [importance sampling](importance-sampling.md), [KL-Cov](kl-cov.md), [KodCode](../datasets/kodcode.md), [linear function approximation](linear-function-approximation.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [log-linear policy](../concepts/log-linear-policy.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [Mistral-7B](../models/mistral-7b.md), [natural policy gradient](natural-policy-gradient.md), [OlympiadBench](../datasets/olympiadbench.md), [OMNI-MATH](../datasets/omni-math.md), [pass-k](pass-k.md), [performance ceiling](../concepts/performance-ceiling.md), [policy entropy](../concepts/policy-entropy.md), [policy gradient](policy-gradient.md), [PPO](ppo.md), [PRIME](prime.md), [Qwen2.5-14B](../models/qwen2-5-14b.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [reasoning boundary](../concepts/reasoning-boundary.md), [reasoning distillation](reasoning-distillation.md), [RLOO](rloo.md), [RLVR](rlvr.md), [scaling laws](../concepts/scaling-laws.md), [softmax policy](../concepts/softmax-policy.md), [tabular softmax parameterization](../concepts/tabular-softmax-parameterization.md), [token-level entropy](../concepts/token-level-entropy.md), [VeRL](verl.md)

## Appears in

- [The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models](../../archive/papers/2025/local-5175928072823010/summary.md) — Establishes that RL trades policy entropy for reward along a predictable exponential curve R = -a·exp(H) + b, derives that entropy change is driven by the covariance between action probability and advantage, and controls it by restricting updates to the highest-covariance tokens.
- [Rethinking the Global Convergence of Softmax Policy Gradient with Linear Function Approximation](../../archive/papers/2025/local-8458ce24c9e6b3b5/summary.md) — Shows by two four-armed bandits with nearly identical approximation error, one of which converges and one of which does not, that approximation error cannot characterize whether softmax policy gradient reaches the optimum, and replaces it with a condition on whether the features preserve the ordering of the rewards.
- [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](../../archive/papers/2025/local-b050d2841cbb4959/summary.md) — Measures RLVR-trained models against their base models with pass@k at large k and finds the base wins, concluding RLVR sharpens sampling toward paths the base already had rather than adding new ones.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
