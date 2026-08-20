# PRIME

<!-- auto:begin -->

A reinforcement-learning method using an implicit process reward derived without step labels, appearing across 3 sources as a comparator rather than a subject. Two results place it: one entropy analysis finds its fitted entropy-performance curves unchanged from three other algorithms, so its entropy behaviour is not distinctive; and under symbolic variabilisation a model trained with it loses 50.4 percent of its accuracy on one competition set when consistency across instantiations is required, in the middle of a range running from 13.6 to 94.5 percent across reinforcement-trained 7B models.

- **Kind**: method
- **Also called**: PRIME
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [advantage function](../concepts/advantage-function.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [benchmark contamination](../concepts/benchmark-contamination.md), [bootstrap resampling](bootstrap-resampling.md), [Clip-Cov](clip-cov.md), [clip-higher](clip-higher.md), [covariance of probability and advantage](../concepts/covariance-of-probability-and-advantage.md), [DAPO](dapo.md), [DAPO-Qwen-32B](../models/dapo-qwen-32b.md), [entropy bonus](../concepts/entropy-bonus.md), [entropy collapse](../concepts/entropy-collapse.md), [entropy regularization](entropy-regularization.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [KL-Cov](kl-cov.md), [KodCode](../datasets/kodcode.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [MATH500](../datasets/math500.md), [memorization](../concepts/memorization.md), [Minerva](../datasets/minerva.md), [Mistral-7B](../models/mistral-7b.md), [OlympiadBench](../datasets/olympiadbench.md), [Omni-MATH](../datasets/omni-math.md), [performance ceiling](../concepts/performance-ceiling.md), [policy entropy](../concepts/policy-entropy.md), [policy gradient](../concepts/policy-gradient.md), [PPO](ppo.md), [process reward model](process-reward-model.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-235B-A22B](../models/qwen3-235b-a22b.md), [REINFORCE](reinforce.md), [RLOO](rloo.md), [RLVR](rlvr.md), [scaling laws](../concepts/scaling-laws.md), [Skywork-OR1-Math-7B](../models/skywork-or1-math-7b.md), [softmax policy](../concepts/softmax-policy.md), [tabular softmax parameterization](../concepts/tabular-softmax-parameterization.md), [token-level entropy](../concepts/token-level-entropy.md), [VeRL](verl.md), [vLLM](vllm.md)

## Appears in

- [The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models](../../archive/papers/2025/local-5175928072823010/summary.md) — Establishes that RL trades policy entropy for reward along a predictable exponential curve R = -a·exp(H) + b, derives that entropy change is driven by the covariance between action probability and advantage, and controls it by restricting updates to the highest-covariance tokens.
- [VAR-MATH: Probing True Mathematical Reasoning in LLMs via Symbolic Multi-Instance Benchmarks](../../archive/papers/2026/local-d62cc27b0209da49/summary.md) — Converts AMC23 and AIME24/25 into symbolic templates whose constants are replaced by sampled variables, requires a model to solve several instantiations of each problem, and finds RL-finetuned models lose most of their reported accuracy under that consistency requirement.
- [A Comparative Theoretical Analysis of Entropy Control Methods in Reinforcement Learning for Reasoning Language Models](../../archive/papers/2026/local-ed740509686ff305/summary.md) — Proves that an entropy bonus permanently moves the stationary point of RL training while covariance-targeted control reaches the unregularized optimum once its coefficient is annealed, and that the bonus shrinks the stability margin where the targeted methods leave it intact.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
