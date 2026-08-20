# MathVista

<!-- auto:begin -->

A benchmark of visual mathematical reasoning problems, used by both sources as the out-of-domain check rather than the training target. In one, a chart-specific method finetuned only on synthetic charts transfers to it with a 10.20-point gain at 3B, which is what turns a domain-specific result into a claim about multimodal reasoning generally. In the other it is among the benchmarks over which RLVR's pass@k behaviour is compared against a base model. Its function in the archive is the same in both: it is where a method has to show it learned something more portable than its training distribution.

- **Kind**: dataset
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME 2024](aime-2024.md), [AMC23](amc23.md), [chain of thought](../methods/chain-of-thought.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [compositional generalization](../concepts/compositional-generalization.md), [curriculum learning](../concepts/curriculum-learning.md), [DAPO](../methods/dapo.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [entropy collapse](../concepts/entropy-collapse.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [Gemma-3-4B](../models/gemma-3-4b.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [GPT-4o](../models/gpt-4o.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [HumanEval+](humaneval.md), [LiveCodeBench](livecodebench.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH500](math500.md), [MathVision](mathvision.md), [Minerva](minerva.md), [multimodal reasoning](../concepts/multimodal-reasoning.md), [OlympiadBench](olympiadbench.md), [pass@k](../concepts/pass-k.md), [PPO](../methods/ppo.md), [process supervision](../concepts/process-supervision.md), [Qwen2.5-14B](../models/qwen2-5-14b.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen2.5-VL-3B](../models/qwen2-5-vl-3b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [reasoning boundary](../concepts/reasoning-boundary.md), [reasoning distillation](../methods/reasoning-distillation.md), [REINFORCE](../methods/reinforce.md), [reinforcement learning](../methods/reinforcement-learning.md), [RLOO](../methods/rloo.md), [RLVR](../methods/rlvr.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [synthetic data generation](../methods/synthetic-data-generation.md), [visual grounding](../concepts/visual-grounding.md)

## Appears in

- [CURV: Enhancing Chart Understanding Through Curriculum Visual Grounded Reasoning](../../archive/papers/2026/arxiv-2608-02833/summary.md) — Reformulates chart question answering as a chain in which every reasoning step carries a predicted image region, trains that pairing through a curriculum graded by nesting depth, and finds explicit intermediate grounding worth 8.78 points over letting the model attend implicitly.
- [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](../../archive/papers/2025/local-b050d2841cbb4959/summary.md) — Measures RLVR-trained models against their base models with pass@k at large k and finds the base wins, concluding RLVR sharpens sampling toward paths the base already had rather than adding new ones.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
