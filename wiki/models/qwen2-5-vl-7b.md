# Qwen2.5-VL-7B

<!-- auto:begin -->

A 7B Qwen2.5 vision-language checkpoint, and the archive's usual subject when a finding needs testing outside text. Two sources use it that way: one probes whether RLVR extends the reasoning boundary on visual reasoning benchmarks as well as math and code, the other measures what prolonged RLVR costs, reporting degradation in core capabilities including perception and faithfulness that experience replay is introduced to prevent.

- **Kind**: model
- **Also called**: Qwen2.5-VL-7B-Instruct
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [AIME24](../datasets/aime24.md), [AMC23](../datasets/amc23.md), [catastrophic forgetting](../concepts/catastrophic-forgetting.md), [chain of thought](../methods/chain-of-thought.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [compositional generalization](../concepts/compositional-generalization.md), [curriculum learning](../concepts/curriculum-learning.md), [DAPO](../methods/dapo.md), [DeepSeek-R1-Distill-Qwen-14B](deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [entropy collapse](../concepts/entropy-collapse.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [Gemma-3-4B](gemma-3-4b.md), [GPT-4.1-mini](gpt-4-1-mini.md), [GPT-4o](gpt-4o.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [HumanEval+](../datasets/humaneval.md), [KL regularization](../methods/kl-regularization.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B](llama-3-1-8b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH500](../datasets/math500.md), [MathVista](../datasets/mathvista.md), [Minerva](../datasets/minerva.md), [multimodal reasoning](../concepts/multimodal-reasoning.md), [OlympiadBench](../datasets/olympiadbench.md), [pass@k](../methods/pass-k.md), [PPO](../methods/ppo.md), [process supervision](../concepts/process-supervision.md), [Qwen2.5-14B](qwen2-5-14b.md), [Qwen2.5-32B](qwen2-5-32b.md), [Qwen2.5-7B](qwen2-5-7b.md), [Qwen2.5-Math-7B](qwen2-5-math-7b.md), [Qwen2.5-VL-3B](qwen2-5-vl-3b.md), [reasoning boundary](../concepts/reasoning-boundary.md), [reasoning distillation](../methods/reasoning-distillation.md), [REINFORCE](../methods/reinforce.md), [reinforcement learning](../methods/reinforcement-learning.md), [RLOO](../methods/rloo.md), [RLVR](../methods/rlvr.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [synthetic data generation](../methods/synthetic-data-generation.md), [training dynamics](../concepts/training-dynamics.md), [visual grounding](../concepts/visual-grounding.md)

## Appears in

- [CURV: Enhancing Chart Understanding Through Curriculum Visual Grounded Reasoning](../../archive/papers/2026/arxiv-2608-02833/summary.md) — Reformulates chart question answering as a chain in which every reasoning step carries a predicted image region, trains that pairing through a curriculum graded by nesting depth, and finds explicit intermediate grounding worth 8.78 points over letting the model attend implicitly.
- [Beyond Reasoning Gains: Mitigating General-Capability Forgetting in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1717/summary.md) — Confirms that prolonged RLVR makes models forget foundational skills, and counters it with experience replay whose objective weights adapt online to convergence and instability signals.
- [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](../../archive/papers/2025/local-b050d2841cbb4959/summary.md) — Measures RLVR-trained models against their base models with pass@k at large k and finds the base wins, concluding RLVR sharpens sampling toward paths the base already had rather than adding new ones.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
