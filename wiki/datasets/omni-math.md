# Omni-MATH

<!-- auto:begin -->

A competition-level mathematics benchmark, reported by both sources only as one of the held-out evaluation sets in reinforcement learning experiments on verifiable mathematics. Neither source characterizes its contents, difficulty range or construction, so nothing further can be stated from the archived material.

- **Kind**: dataset
- **Also called**: OMNI-MATH
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [advantage function](../concepts/advantage-function.md), [AIME24](aime24.md), [AIME25](aime25.md), [AMC](amc.md), [AMC23](amc23.md), [answer stabilization](../concepts/answer-stabilization.md), [chain of thought](../methods/chain-of-thought.md), [chain-of-thought compression](../methods/chain-of-thought-compression.md), [Clip-Cov](../methods/clip-cov.md), [clip-higher](../methods/clip-higher.md), [covariance of probability and advantage](../concepts/covariance-of-probability-and-advantage.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [early exit](../methods/early-exit.md), [entropy bonus](../concepts/entropy-bonus.md), [entropy collapse](../concepts/entropy-collapse.md), [entropy regularization](../methods/entropy-regularization.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [GPT-OSS-20B](../models/gpt-oss-20b.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [HumanEval+](humaneval.md), [KL-Cov](../methods/kl-cov.md), [KodCode](kodcode.md), [length penalty](../methods/length-penalty.md), [MATH-500](math-500.md), [MATH500](math500.md), [MBPP+](mbpp.md), [Minerva](minerva.md), [Mistral-7B](../models/mistral-7b.md), [OlympiadBench](olympiadbench.md), [OpenCodeInstruct](opencodeinstruct.md), [optimal stopping](../concepts/optimal-stopping.md), [overthinking](../concepts/overthinking.md), [performance ceiling](../concepts/performance-ceiling.md), [policy entropy](../concepts/policy-entropy.md), [policy gradient](../methods/policy-gradient.md), [PPO](../methods/ppo.md), [PRIME](../methods/prime.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [REINFORCE++](../methods/reinforce.md), [RLOO](../methods/rloo.md), [RLVR](../methods/rlvr.md), [scaling laws](../concepts/scaling-laws.md), [softmax policy](../concepts/softmax-policy.md), [tabular softmax parameterization](../concepts/tabular-softmax-parameterization.md), [token-level entropy](../concepts/token-level-entropy.md), [VeRL](../methods/verl.md)

## Appears in

- [Attend to Your Own Thoughts: Breaking the Barrier for Post-Training Quantization of Reasoning LLMs through the Lens of 1.58-Bit Quantization](../../archive/papers/2026/arxiv-2608-01078/summary.md) — Finds that ternary post-training quantization of a reasoning model collapses because the calibration set is web text, and repairs it by calibrating on chain-of-thought traces the target model generates for itself.
- [The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models](../../archive/papers/2025/local-5175928072823010/summary.md) — Establishes that RL trades policy entropy for reward along a predictable exponential curve R = -a·exp(H) + b, derives that entropy change is driven by the covariance between action probability and advantage, and controls it by restricting updates to the highest-covariance tokens.
- [OS-Pruner: Pruning Chains-of-Thought of Reasoning Models via Optimal Stopping](../../archive/papers/2026/local-dbfa51b5159a1a77/summary.md) — Recasts when-to-stop-reasoning as optimal stopping rather than classification, and proves that a fixed threshold on the probability of being correct can be arbitrarily far from optimal even when that probability is known exactly, because the decision needs the value of continuing and not the value of stopping.
- [A Comparative Theoretical Analysis of Entropy Control Methods in Reinforcement Learning for Reasoning Language Models](../../archive/papers/2026/local-ed740509686ff305/summary.md) — Proves that an entropy bonus permanently moves the stationary point of RL training while covariance-targeted control reaches the unregularized optimum once its coefficient is annealed, and that the bonus shrinks the stability margin where the targeted methods leave it intact.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
