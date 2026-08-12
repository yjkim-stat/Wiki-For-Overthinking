# DeepSeek-R1-Distill-Qwen-32B

<!-- auto:begin -->

The 32B member of the R1 distillation series. Two findings attach to it specifically: it shows the largest absolute loss in the archive from suppressing expressions of uncertainty, falling from 80.0 to 43.3 AIME24 pass@1 after 800-sample fine-tuning on its own correct traces with those expressions removed; and its proactive self-corrections have low precision (23.9%), consistent with the pattern that expressed doubt fires more often than it is warranted.

- **Kind**: model
- **Also called**: DeepSeek-R1-Distill-32B
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [activation steering](../methods/activation-steering.md), [aha moment](../concepts/aha-moment.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AlpacaEval](../datasets/alpacaeval.md), [AMC23](../datasets/amc23.md), [budget forcing](../methods/budget-forcing.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-14B](deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [epistemic verbalization](../concepts/epistemic-verbalization.md), [GSM8K](../datasets/gsm8k.md), [information bottleneck](../concepts/information-bottleneck.md), [linear probing](../methods/linear-probing.md), [Llama-3.1-8B](llama-3-1-8b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](../concepts/overthinking.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen2.5-14B](qwen2-5-14b.md), [Qwen2.5-32B](qwen2-5-32b.md), [Qwen2.5-32B-Instruct](qwen2-5-32b-instruct.md), [Qwen2.5-7B](qwen2-5-7b.md), [Qwen2.5-Math-7B](qwen2-5-math-7b.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-8B](qwen3-8b.md), [QwQ-32B](qwq-32b.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [self-correction](../concepts/self-correction.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](../methods/test-time-scaling.md)

## Appears in

- [Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks in LLM Reasoning](../../archive/papers/2025/local-2c3407071e27c9d6/summary.md) — Tracks mutual information between each reasoning step's representation and the correct answer, finds it spikes at sparse 'MI peaks' that decode to reflective tokens like 'Wait' and 'Hmm', and shows suppressing exactly those tokens degrades reasoning while suppressing equally many others does not.
- [On Reasoning Strength Planning in Large Reasoning Models](../../archive/papers/2025/local-77b3413236375923/summary.md) — Shows that a reasoning model decides how long to think before emitting a single reasoning token — the eventual token count is linearly decodable from the question's activations at Spearman 0.84 — and that this plan is carried by one shared direction vector whose magnitude encodes strength and which acts by shifting the logits of the end-of-thinking token.
- [Understanding Reasoning in LLMs through Strategic Information Allocation under Uncertainty](../../archive/papers/2026/local-99019f66bdc27581/summary.md) — Separates reasoning into procedural advancement and 'epistemic verbalization' — the token-level externalization of uncertainty — and shows that emitting doubt is what lets a model recover from silent divergence, that injecting a bare doubt cue recovers failed trajectories, and that 800 SFT examples suffice to install or destroy the habit.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
