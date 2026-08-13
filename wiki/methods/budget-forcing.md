# budget forcing

<!-- auto:begin -->

Controlling how long a model thinks by cutting the thinking block short, or extending it by suppressing the end-of-thinking token and appending 'Wait'. Its originating source reports it extrapolating a model beyond its unassisted performance, from 50% to 57% on AIME24. A second source supplies the mechanism the first lacks: the representations at reflective tokens like 'Wait' carry a spike of mutual information with the correct answer, so the token is not an arbitrary continuation cue but the one measured to be most informative.

- **Kind**: method
- **Also called**: budget forcing
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [activation steering](activation-steering.md), [AIME24](../datasets/aime24.md), [AlpacaEval](../datasets/alpacaeval.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [epistemic verbalization](../concepts/epistemic-verbalization.md), [GSM8K](../datasets/gsm8k.md), [information bottleneck](../concepts/information-bottleneck.md), [linear probing](linear-probing.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](../concepts/overthinking.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen2.5-14B](../models/qwen2-5-14b.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-32B-Instruct](../models/qwen2-5-32b-instruct.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [QwQ-32B](../models/qwq-32b.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [self-correction](../concepts/self-correction.md), [steering vector](steering-vector.md), [supervised finetuning](supervised-finetuning.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](test-time-scaling.md)

## Appears in

- [s1: Simple test-time scaling](../../archive/papers/2025/arxiv-2501-19393/summary.md) — Reaches test-time scaling with two simple ingredients: supervised finetuning on 1,000 curated reasoning traces, and 'budget forcing', which controls thinking length by cutting generation off or appending 'Wait' to extend it.
- [Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks in LLM Reasoning](../../archive/papers/2025/local-2c3407071e27c9d6/summary.md) — Tracks mutual information between each reasoning step's representation and the correct answer, finds it spikes at sparse 'MI peaks' that decode to reflective tokens like 'Wait' and 'Hmm', and shows suppressing exactly those tokens degrades reasoning while suppressing equally many others does not.
- [On Reasoning Strength Planning in Large Reasoning Models](../../archive/papers/2025/local-77b3413236375923/summary.md) — Shows that a reasoning model decides how long to think before emitting a single reasoning token — the eventual token count is linearly decodable from the question's activations at Spearman 0.84 — and that this plan is carried by one shared direction vector whose magnitude encodes strength and which acts by shifting the logits of the end-of-thinking token.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
