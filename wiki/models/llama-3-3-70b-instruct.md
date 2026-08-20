# Llama-3.3-70B-Instruct

<!-- auto:begin -->

A 70-billion-parameter instruction-tuned Llama model, and the site of the archive's best-controlled probe-and-steer result. In the steering-pressure study its unsteered responses to values-conflict prompts split 42 clarification-seeking derails to 58 substantive answers -- the largest within-model baseline split in that evaluation -- and that distinction is decodable from the residual stream at 0.87 balanced accuracy plateauing across the second half of the network, against 0.72 available from prompt ambiguity alone. Steering along the decoded direction moves the derail rate monotonically from 0 to 86 percent across a norm-referenced strength sweep, with the zero-strength control landing within two points of the originally logged rate, and with 28 of 50 generations truncating at the strongest suppression. It appears again in the mutual-information work identifying sparse information peaks that decode to reflective tokens. Neither source describes the model itself.

- **Kind**: model
- **Also called**: Llama-3.3-70B-Instruct
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation steering](../methods/activation-steering.md), [AIME 2024](../datasets/aime-2024.md), [benchmark design](../concepts/benchmark-design.md), [budget forcing](../methods/budget-forcing.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [Claude Opus 4.7](claude-opus-4-7.md), [Cohen's kappa](../methods/cohen-s-kappa.md), [construct validity](../concepts/construct-validity.md), [DeepSeek](deepseek.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-14B](deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [detection versus control](../concepts/detection-versus-control.md), [difference-in-means direction](../methods/difference-in-means-direction.md), [epistemic verbalization](../concepts/epistemic-verbalization.md), [GPT-5](gpt-5.md), [GSM8K](../datasets/gsm8k.md), [IFEval](../datasets/ifeval.md), [information bottleneck](../concepts/information-bottleneck.md), [jury aggregation](../methods/jury-aggregation.md), [linear probe](../methods/linear-probe.md), [Llama-3.1-8B](llama-3-1-8b.md), [Llama-3.2-1B-Instruct](llama-3-2-1b-instruct.md), [Llama-3.3-70B](llama-3-3-70b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [monitorability](../concepts/monitorability.md), [nested cross-validation](../methods/nested-cross-validation.md), [permutation test](../methods/permutation-test.md), [position bias](../concepts/position-bias.md), [Qwen](qwen.md), [Qwen2.5-14B](qwen2-5-14b.md), [Qwen2.5-32B](qwen2-5-32b.md), [Qwen2.5-Math-7B](qwen2-5-math-7b.md), [QwQ-32B](qwq-32b.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [selectivity control](../methods/selectivity-control.md), [self-correction](../concepts/self-correction.md), [steering vector](../methods/steering-vector.md), [test-time scaling](../concepts/test-time-scaling.md)

## Appears in

- [Divergent Response Modes in Frontier Language Models Under Steering Pressure](../../archive/papers/2026/arxiv-2608-06578/summary.md) — Measures not how far six frontier models move under steering pressure but what kind of response they give when they decline, finds several response modes belonging to a single model, and then traces the largest within-model split to a linearly decodable and causally steerable direction in an open-weight model's residual stream.
- [Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks in LLM Reasoning](../../archive/papers/2025/local-2c3407071e27c9d6/summary.md) — Tracks mutual information between each reasoning step's representation and the correct answer, finds it spikes at sparse 'MI peaks' that decode to reflective tokens like 'Wait' and 'Hmm', and shows suppressing exactly those tokens degrades reasoning while suppressing equally many others does not.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
