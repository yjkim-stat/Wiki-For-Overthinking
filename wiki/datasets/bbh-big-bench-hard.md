# BBH (Big Bench Hard)

<!-- auto:begin -->

A benchmark of hard multi-step reasoning tasks used in the archive's sources as one of several standard evaluation sets for test-time-compute efficiency methods, alongside AIME/AMC/GPQA-Diamond. TRAAC and Atom of Thoughts both evaluate on it; neither source describes its construction, only using it as an evaluation target.

- **Kind**: dataset
- **Also called**: BBH, BBH (BIG-Bench Hard), Big-Bench Hard
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AdaptThink](../methods/adaptthink.md), [AIME](aime.md), [DAPO-Math-17k](dapo-math-17k.md), [GPQA-Diamond](gpqa-diamond.md), [GRPO (Group Relative Policy Optimization)](../methods/grpo-group-relative-policy-optimization.md), [HotpotQA](hotpotqa.md), [LC-R1](../methods/lc-r1.md), [MMLU](mmlu.md), [SuperGPQA](supergpqa.md), [TokenSkip](../methods/tokenskip.md)

## Appears in

- [Think Right: Learning to Mitigate Under-Over Thinking via Adaptive, Attentive Compression](../../archive/papers/2025/local-da3fbe3617acc5f8/summary.md) — TRAAC is an online GRPO-based RL method that prunes a reasoning model's chain-of-thought using attention scores from the </think> token and calibrates how aggressively it prunes based on estimated problem difficulty, so it thinks less on easy problems and more on hard ones.
- [Atom of Thoughts for Markov LLM Test-Time Scaling](../../archive/papers/2025/title-0393ca4ca3f4fb8c/summary.md) — Atom of Thoughts reframes multi-step LLM reasoning as a Markov process of decomposing a question into independent atomic subquestions and contracting them into an answer-equivalent simplified question, removing the need to carry accumulated historical context and serving as a plug-in for existing test-time scaling methods.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
