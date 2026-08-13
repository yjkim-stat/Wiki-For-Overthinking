# Qwen3-235B-A22B

<!-- auto:begin -->

A large mixture-of-experts model with roughly 22B active parameters, used by both sources as the frontier-adjacent point where a degradation is shown to persist or not. One ternarizes it and reports the result that carries its scaling claim — 78.80 / 85.97 / 26.88 / 67.07 / 48.51 against FP16's 98.60 / 96.28 / 45.51 / 89.02 / 69.31 — establishing that post-training quantization of a reasoning model holds at 235B and not only at small scale. The other finds it among the frontier models robust on the easier symbolic re-instantiation (-6.4% on AMC23) while still degrading on harder sets. In both, it answers whether a finding survives the largest model the authors could run.

- **Kind**: model
- **Also called**: Qwen3-235B
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC23](../datasets/amc23.md), [benchmark contamination](../concepts/benchmark-contamination.md), [chain of thought](../methods/chain-of-thought.md), [DAPO](../methods/dapo.md), [DAPO-Qwen-32B](dapo-qwen-32b.md), [GSM8K](../datasets/gsm8k.md), [HumanEval+](../datasets/humaneval.md), [MATH-500](../datasets/math-500.md), [MATH500](../datasets/math500.md), [MBPP+](../datasets/mbpp.md), [memorization](../concepts/memorization.md), [OlympiadBench](../datasets/olympiadbench.md), [Omni-MATH](../datasets/omni-math.md), [OpenCodeInstruct](../datasets/opencodeinstruct.md), [PRIME](../methods/prime.md), [Qwen2.5-32B](qwen2-5-32b.md), [Qwen2.5-Math-7B](qwen2-5-math-7b.md), [Qwen3-1.7B](qwen3-1-7b.md), [Qwen3-30B-A3B](qwen3-30b-a3b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-4B](qwen3-4b.md), [RLVR](../methods/rlvr.md), [vLLM](../methods/vllm.md)

## Appears in

- [Attend to Your Own Thoughts: Breaking the Barrier for Post-Training Quantization of Reasoning LLMs through the Lens of 1.58-Bit Quantization](../../archive/papers/2026/arxiv-2608-01078/summary.md) — Finds that ternary post-training quantization of a reasoning model collapses because the calibration set is web text, and repairs it by calibrating on chain-of-thought traces the target model generates for itself.
- [VAR-MATH: Probing True Mathematical Reasoning in LLMs via Symbolic Multi-Instance Benchmarks](../../archive/papers/2026/local-d62cc27b0209da49/summary.md) — Converts AMC23 and AIME24/25 into symbolic templates whose constants are replaced by sampled variables, requires a model to solve several instantiations of each problem, and finds RL-finetuned models lose most of their reported accuracy under that consistency requirement.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
