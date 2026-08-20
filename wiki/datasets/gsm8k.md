# GSM8K

<!-- auto:begin -->

A grade-school math word-problem benchmark used in the archive's 9 sources as an 'easier' reasoning testbed, in contrast to harder benchmarks like AIME or GPQA Diamond. It shows up in studies of overthinking on easy questions (Between Underthinking and Overthinking, the foundational 'Do NOT Think That Much for 2+3=?' paper, ThinkRetrieve), as a contrast point showing GSM8K/GSM-Plus performance doesn't predict basic-arithmetic accuracy (Do LLMs Overthink Basic Math Reasoning?), and as a standard evaluation set for self-braking tuning, verifier-quality analysis (ROC-n-reroll), reasoning-graph topology, state-machine reasoning steering, and diffusion-LLM test-time scaling.

- **Kind**: dataset
- **Also called**: GSM-8K
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 9

**Related**: [activation steering](../methods/activation-steering.md), [AIME](aime.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC](amc.md), [best-of-N sampling](../methods/best-of-n-sampling.md), [GPQA](gpqa.md), [GPQA-Diamond](gpqa-diamond.md), [MATH](math.md), [MATH-500](math-500.md), [overthinking](../concepts/overthinking.md), [rejection sampling](../methods/rejection-sampling.md), [sequential test-time scaling](../concepts/sequential-test-time-scaling.md), [test-time compute scaling](../concepts/test-time-compute-scaling.md), [underthinking](../concepts/underthinking.md)

## Appears in

- [ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling](../../archive/papers/2026/arxiv-2608-10928/summary.md) — ThinkRetrieve augments each step of a reasoning model's chain of thought with a dynamically retrieved, fully worked solved example (rather than just facts), consistently beating standard sequential test-time scaling on math and QA benchmarks.
- [Between Underthinking and Overthinking: An Empirical Study of Reasoning Length and correctness in LLMs](../../archive/papers/2025/local-6afb006d68240134/summary.md) — An empirical study showing reasoning LLMs overthink easy questions and underthink hard ones, and that preferring shorter outputs via SimPO can cut generation length 30-60% with little accuracy loss.
- [Do LLMs Overthink Basic Math Reasoning? Benchmarking the Accuracy-Efficiency Tradeoff in Language Models](../../archive/papers/2025/local-c1f4e56014fb43fb/summary.md) — Introduces LLMThinkBench, a dynamically-generated 14-task basic-math benchmark and a harmonic-mean Overthinking Score, then evaluates 53 LLMs to show that strong performance on complex math benchmarks does not transfer to basic arithmetic and that reasoning-tuned models often spend far more tokens for equal or worse accuracy.
- [Topology of Reasoning: Understanding Large Reasoning Models through Reasoning Graph Properties](../../archive/papers/2025/title-11c5eb0da4499b68/summary.md) — Analyzes large reasoning models by clustering their hidden states into a 'reasoning graph' and studying how its cyclicity, diameter and small-world structure relate to task difficulty, model scale and accuracy.
- [Let LRMs Break Free from Overthinking via Self-Braking Tuning](../../archive/papers/2025/title-2b17dd2ef08b6fa4/summary.md) — Introduces Self-Braking Tuning, which trains a large reasoning model to detect and stop its own redundant reasoning steps, cutting token usage by up to 60% with comparable accuracy on math benchmarks.
- [ROC-n-reroll: How verifier imperfection affects test-time scaling](../../archive/papers/2026/title-6b3727a0a0ac9a23/summary.md) — Proves that verifier ROC-curve geometry determines the accuracy of Best-of-N and Rejection Sampling under a fixed compute budget, and shows RS beats BoN at fixed compute while both converge in the infinite-compute limit.
- [Modeling Hierarchical Thinking in Large Reasoning Models](../../archive/papers/2026/title-7651639ee2f29946/summary.md) — Models a large reasoning model's chain-of-thought as transitions among six latent cognitive states and uses that abstraction to steer generation toward better reasoning policies at inference time, without training.
- [Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](../../archive/papers/2025/title-7805f8ec24eadc13/summary.md) — The first systematic study of overthinking in o1-like reasoning models, introducing outcome/process efficiency metrics and a self-training method that trims redundant reasoning on easy problems without hurting accuracy.
- [TEST-TIME SCALING IN DIFFUSION LLMS VIA HIDDEN SEMI-AUTOREGRESSIVE EXPERTS](../../archive/papers/2026/title-7b2310c5e9f25bde/summary.md) — Shows diffusion LLMs implicitly contain a mixture of semi-autoregressive generation experts and introduces a training-free method that majority-votes across multiple block generation schedules to substantially boost accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
