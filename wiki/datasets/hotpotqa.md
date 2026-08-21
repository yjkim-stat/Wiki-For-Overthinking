# HotpotQA

<!-- auto:begin -->

HotpotQA is the archive's multi-hop question-answering leg, and it is where reasoning length gets counted in steps rather than in tokens. CoSMo trains and evaluates on it as in-distribution data (with HaluEval, against Natural Questions and CRAG out-of-distribution), reporting a 3.3-point accuracy gain at 28.7% fewer segments and roughly 2.9 segments on average - but its unit is segments, not tokens, and only the SFT-only ablation gives a token figure (19%). It is evaluated on multi-hop QA precisely because its method needs ground-truth hop counts to set a target, which math and code benchmarks do not annotate. Atom of Thoughts also names it as its multi-hop leg alongside BBH, MMLU and LongBench, but the archive could recover only the qualitative claim that performance improves as budget grows, with no numbers.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [BBH (Big Bench Hard)](bbh-big-bench-hard.md), [GRPO](../methods/grpo.md), [Length Penalty](../concepts/length-penalty.md), [MMLU](mmlu.md), [Natural Questions](natural-questions.md), [Overthinking](../concepts/overthinking.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md)

## Appears in

- [Atom of Thoughts for Markov LLM Test-Time Scaling](../../archive/papers/2025/title-0393ca4ca3f4fb8c/summary.md) — Atom of Thoughts reframes multi-step LLM reasoning as a Markov process of decomposing a question into independent atomic subquestions and contracting them into an answer-equivalent simplified question, removing the need to carry accumulated historical context and serving as a plug-in for existing test-time scaling methods.
- [Short Chains, Deep Thoughts: Balancing Reasoning Efficiency and Intra-Segment Capability via Split-Merge Optimization](../../archive/papers/2026/title-0bf980e6919c2982/summary.md) — CoSMo restructures reasoning chains by merging redundant segments and splitting logical gaps, then trains with RL against a segment-count budget rather than a token budget.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
