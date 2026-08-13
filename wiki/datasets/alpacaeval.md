# AlpacaEval

<!-- auto:begin -->

An instruction-following benchmark scored by LLM judges, used in the archived sources in two unrelated ways. As a judge benchmark it is part of the preference-evaluation family whose scores are reported not to track safety, world knowledge or instruction following, with style bias offered as the explanation. Separately, its questions serve as the vanilla control in an overthink-detection experiment, paired against versions modified by an overthink attack, where a pre-generation length probe predicts substantially longer reasoning on the attacked versions.

- **Kind**: dataset
- **Also called**: AlpacaEval
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation steering](../methods/activation-steering.md), [AIME 2024](aime-2024.md), [alignment](../concepts/alignment.md), [budget forcing](../methods/budget-forcing.md), [construct validity](../concepts/construct-validity.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [instruction following](../concepts/instruction-following.md), [linear probe](../methods/linear-probe.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH500](math500.md), [meta-evaluation](../concepts/meta-evaluation.md), [MMLU](mmlu.md), [MT-Bench](mt-bench.md), [OlympiadBench](olympiadbench.md), [overthinking](../concepts/overthinking.md), [preference optimization](../methods/preference-optimization.md), [prompt difficulty](../concepts/prompt-difficulty.md), [QwQ-32B](../models/qwq-32b.md), [steering vector](../methods/steering-vector.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time compute](../concepts/test-time-compute.md)

## Appears in

- [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](../../archive/papers/2025/local-503d1e9598036375/summary.md) — Builds a large standardized meta-benchmark and finds that LLM-judge preference scores do not correlate with concrete measures of safety, world knowledge or instruction following, because judges systematically prioritize style over factuality and safety.
- [On Reasoning Strength Planning in Large Reasoning Models](../../archive/papers/2025/local-77b3413236375923/summary.md) — Shows that a reasoning model decides how long to think before emitting a single reasoning token — the eventual token count is linearly decodable from the question's activations at Spearman 0.84 — and that this plan is carried by one shared direction vector whose magnitude encodes strength and which acts by shifting the logits of the end-of-thinking token.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
