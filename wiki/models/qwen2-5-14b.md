# Qwen2.5-14B

<!-- auto:begin -->

A 14B Qwen2.5 checkpoint, used in the archive at the mid scale where trends are checked rather than discovered. It appears in the pass@k comparison where base models overtake their RLVR-trained counterparts as k grows, and in the mutual-information analysis of reasoning dynamics, where its share of reasoning steps that are information peaks is 3.59% — one of the higher rates measured, against 0.51% for a distilled 7B.

- **Kind**: model
- **Also called**: Qwen2.5-14B-Base
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME24](../datasets/aime24.md), [AMC23](../datasets/amc23.md), [budget forcing](../methods/budget-forcing.md), [DAPO](../methods/dapo.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-14B](deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [entropy collapse](../concepts/entropy-collapse.md), [epistemic verbalization](../concepts/epistemic-verbalization.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [HumanEval+](../datasets/humaneval.md), [information bottleneck](../concepts/information-bottleneck.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B](llama-3-1-8b.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [OlympiadBench](../datasets/olympiadbench.md), [pass-k](../methods/pass-k.md), [PPO](../methods/ppo.md), [Qwen2.5-32B](qwen2-5-32b.md), [Qwen2.5-7B](qwen2-5-7b.md), [Qwen2.5-Math-7B](qwen2-5-math-7b.md), [Qwen2.5-VL-7B](qwen2-5-vl-7b.md), [QwQ-32B](qwq-32b.md), [reasoning boundary](../concepts/reasoning-boundary.md), [reasoning distillation](../methods/reasoning-distillation.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [REINFORCE++](../methods/reinforce.md), [RLOO](../methods/rloo.md), [RLVR](../methods/rlvr.md), [self-correction](../concepts/self-correction.md), [test-time scaling](../methods/test-time-scaling.md)

## Appears in

- [Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks in LLM Reasoning](../../archive/papers/2025/local-2c3407071e27c9d6/summary.md) — Tracks mutual information between each reasoning step's representation and the correct answer, finds it spikes at sparse 'MI peaks' that decode to reflective tokens like 'Wait' and 'Hmm', and shows suppressing exactly those tokens degrades reasoning while suppressing equally many others does not.
- [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](../../archive/papers/2025/local-b050d2841cbb4959/summary.md) — Measures RLVR-trained models against their base models with pass@k at large k and finds the base wins, concluding RLVR sharpens sampling toward paths the base already had rather than adding new ones.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
