# GPQA-Diamond

<!-- auto:begin -->

A hard multiple-choice science-question benchmark used across the archive's 9 sources as a standard hard-reasoning evaluation set for test-time-compute and overthinking-mitigation methods, alongside AIME/AMC. It appears in beam search (Gambit), verifier-free selection (Consilience, Funnel of Thoughts), attention-based CoT pruning (TRAAC), sparse decoding (AsyncSpade), MoE expert-sampling, and state-machine reasoning-steering work -- always as an evaluation target rather than something the sources describe the construction of.

- **Kind**: dataset
- **Also called**: GPQA Diamond, GPQA-D, GPQA-Diamond
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 9

**Related**: [activation steering](../methods/activation-steering.md), [AdaptThink](../methods/adaptthink.md), [AIME](aime.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AIME 2026](aime-2026.md), [AMC](amc.md), [AMC23](amc23.md), [BBH (Big Bench Hard)](bbh-big-bench-hard.md), [budget forcing](../methods/budget-forcing.md), [GSM8K](gsm8k.md), [HMMT 2025](hmmt-2025.md), [LC-R1](../methods/lc-r1.md), [MATH-500](math-500.md), [overthinking](../concepts/overthinking.md), [Pass@1](../concepts/pass-1.md), [Slim-SC (baseline)](../methods/slim-sc-baseline.md), [SuperGPQA](supergpqa.md), [SWE-bench Verified](swe-bench-verified.md), [test-time compute scaling](../concepts/test-time-compute-scaling.md), [TokenSkip](../methods/tokenskip.md)

## Appears in

- [Thought-Level Beam Search for Reasoning](../../archive/papers/2026/arxiv-2608-08020/summary.md) — Introduces Gambit, an inference algorithm that formulates test-time reasoning as thought-level beam search, periodically pruning weak reasoning traces and branching new ones from high-quality prefixes to concentrate a fixed hardware budget on the most promising partial reasoning.
- [Consilience for Verifier-Free Test-Time Scaling](../../archive/papers/2026/arxiv-2608-09898/summary.md) — Introduces consilience, a verifier-free test-time-scaling selection metric that picks the sampled reasoning rollout whose confidence starts low (exploratory) and ends high (convergent), fixing a failure mode where naive confidence maximization favors confidently wrong answers on hard problems.
- [Funnel of Thoughts: Efficient Test-Time Scaling via Early Voting and Rollout Pruning](../../archive/papers/2026/arxiv-2608-15065/summary.md) — Funnel of Thoughts detects and discards the subset of parallel reasoning rollouts that are spiraling into unproductive self-correction (flagged by a rising density of hesitation words like 'Wait' and 'perhaps'), matching self-consistency's accuracy while cutting attention FLOPs by up to 56% and wall time by 37.6%.
- [When More Thinking Hurts: Overthinking in LLM Test-Time Compute Scaling](../../archive/papers/2026/local-32a56cfa1105c39e/summary.md) — The paper shows that extended chain-of-thought reasoning in LLMs has diminishing and eventually negative marginal utility, quantifies this 'overthinking' via answer-flip tracking, and proposes cost-aware, indicator-based early-stopping strategies that cut compute substantially with little accuracy loss.
- [Think Right: Learning to Mitigate Under-Over Thinking via Adaptive, Attentive Compression](../../archive/papers/2025/local-da3fbe3617acc5f8/summary.md) — TRAAC is an online GRPO-based RL method that prunes a reasoning model's chain-of-thought using attention scores from the </think> token and calibrates how aggressively it prunes based on estimated problem difficulty, so it thinks less on easy problems and more on hard ones.
- [AsyncSpade: Efficient Test-Time Scaling with Asynchronous Sparse Decoding](../../archive/papers/2026/title-2c3f455590b79024/summary.md) — AsyncSpade speeds up decoding of long chain-of-thought generations by predicting query states from recent patterns and running sparse KV-cache selection asynchronously alongside decoding, cutting per-token latency without hurting accuracy.
- [Certain Head, Uncertain Tail: Expert-Sample for Test-Time Scaling in Fine-Grained MoE](../../archive/papers/2026/title-51b4206a5e2ba637/summary.md) — Expert-Sample scales test-time compute for fine-grained MoE LLMs by randomizing only low-confidence expert routing choices, keeping high-confidence expert selections fixed, to get diverse samples without the usual diversity-stability tradeoff of temperature sampling.
- [Modeling Hierarchical Thinking in Large Reasoning Models](../../archive/papers/2026/title-7651639ee2f29946/summary.md) — Models a large reasoning model's chain-of-thought as transitions among six latent cognitive states and uses that abstraction to steer generation toward better reasoning policies at inference time, without training.
- [LIMOPro: Reasoning Refinement for Efficient and Effective Test-time Scaling](../../archive/papers/2025/title-f14f82d5eba9e811/summary.md) — PIR scores reasoning steps by their effect on answer confidence and prunes only low-importance verification/error-correction steps from distilled chain-of-thought data, producing models that reason more concisely without losing accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
