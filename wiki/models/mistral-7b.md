# Mistral-7B

<!-- auto:begin -->

A 7B open-weight model from Mistral, used across these sources as a second model family for checking that a result is not Qwen- or Llama-specific. It carries two replication roles: its propositional reasoning circuit contains the same four attention-head families found in the Gemma models, and the counterfactual state-editing result replicates in it at 0.93-0.94 edited-state agreement. It also serves as the weakest of three generators in best-of-N reward-model evaluation.

- **Kind**: model
- **Also called**: Mistral-7B, Mistral-7B-Instruct-v0.2, Mistral-7B-v0.1
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [activation patching](../methods/activation-patching.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC23](../datasets/amc23.md), [best-of-n](../methods/best-of-n.md), [causal mediation analysis](../methods/causal-mediation-analysis.md), [circuit analysis](../methods/circuit-analysis.md), [circuit discovery](../methods/circuit-discovery.md), [Clip-Cov](../methods/clip-cov.md), [clip-higher](../methods/clip-higher.md), [covariance of probability and advantage](../concepts/covariance-of-probability-and-advantage.md), [entropy bonus](../concepts/entropy-bonus.md), [entropy collapse](../concepts/entropy-collapse.md), [entropy regularization](../methods/entropy-regularization.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [Game of 24](../datasets/game-of-24.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [implicit reasoning](../concepts/implicit-reasoning.md), [KL-Cov](../methods/kl-cov.md), [KodCode](../datasets/kodcode.md), [Llama-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [localization](../concepts/localization.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [modularity](../concepts/modularity.md), [OlympiadBench](../datasets/olympiadbench.md), [OMNI-MATH](../datasets/omni-math.md), [pass-k](../methods/pass-k.md), [performance ceiling](../concepts/performance-ceiling.md), [policy entropy](../concepts/policy-entropy.md), [PPO](../methods/ppo.md), [PRIME](../methods/prime.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen2.5-32B](qwen2-5-32b.md), [Qwen2.5-7B](qwen2-5-7b.md), [REINFORCE++](../methods/reinforce.md), [RLOO](../methods/rloo.md), [RLVR](../methods/rlvr.md), [scaling laws](../concepts/scaling-laws.md), [softmax policy](../concepts/softmax-policy.md), [token-level entropy](../concepts/token-level-entropy.md), [VeRL](../methods/verl.md)

## Appears in

- [Representation-Based Exploration for Language Models: From Test-Time to Post-Training](../../archive/papers/2026/local-1fadd9f07b138261/summary.md) — Uses elliptical bonuses over a language model's own hidden-state representations as a diversity signal, validates it in a clean inference-time selection setting, then transfers the same signal into RL post-training — where it eliminates the diversity collapse that degrades pass@k at large k.
- [The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models](../../archive/papers/2025/local-5175928072823010/summary.md) — Establishes that RL trades policy entropy for reward along a predictable exponential curve R = -a·exp(H) + b, derives that entropy change is driven by the covariance between action probability and advantage, and controls it by restricting updates to the highest-covariance tokens.
- [A Implies B: Circuit Analysis in LLMs for Propositional Logical Reasoning](../../archive/papers/2025/local-99a25b62fd9ad86c/summary.md) — Uses causal mediation analysis on a minimal propositional logic task to recover a sparse reasoning circuit in Mistral-7B and Gemma-2 up to 27B, and decomposes it into four families of attention heads that execute rule locating, rule moving, fact processing and decision making as sequential steps.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
