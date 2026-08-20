# AIME

<!-- auto:begin -->

The American Invitational Mathematics Examination, used throughout the archive's sources (unspecified year in this entry) as a standard hard competition-math benchmark. Under this exact spelling, the 5 sources use it to evaluate: self-braking tuning, the foundational overthinking paper, meta-RL test-time-compute optimization, reasoning-step pruning (LIMOPro), and Kinetics' reworked test-time scaling law. Note: the archive's wiki tracks this exam under at least 8 separate near-duplicate entries by exact spelling that were never merged -- this is the same underlying exam split into fragmented wiki notes.

- **Kind**: dataset
- **Also called**: AIME 2024, AIME 2025, AIME'25, AIME2024, AIME2025, AIME24, AIME25
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 5

**Related**: [AMC](amc.md), [GPQA](gpqa.md), [GPQA-Diamond](gpqa-diamond.md), [GSM8K](gsm8k.md), [LiveCodeBench](livecodebench.md), [MATH-500](math-500.md), [overthinking](../concepts/overthinking.md)

## Appears in

- [Let LRMs Break Free from Overthinking via Self-Braking Tuning](../../archive/papers/2025/title-2b17dd2ef08b6fa4/summary.md) — Introduces Self-Braking Tuning, which trains a large reasoning model to detect and stop its own redundant reasoning steps, cutting token usage by up to 60% with comparable accuracy on math benchmarks.
- [Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](../../archive/papers/2025/title-7805f8ec24eadc13/summary.md) — The first systematic study of overthinking in o1-like reasoning models, introducing outcome/process efficiency metrics and a self-training method that trims redundant reasoning on easy problems without hurting accuracy.
- [Optimizing Test-Time Compute via Meta Reinforcement Finetuning](../../archive/papers/2025/title-86af300fcc089e57/summary.md) — Casts test-time compute optimization as a meta reinforcement learning problem and fine-tunes reasoning models with an information-gain-based dense reward so each block of reasoning measurably progresses toward the answer.
- [LIMOPro: Reasoning Refinement for Efficient and Effective Test-time Scaling](../../archive/papers/2025/title-f14f82d5eba9e811/summary.md) — PIR scores reasoning steps by their effect on answer confidence and prunes only low-importance verification/error-correction steps from distilled chain-of-thought data, producing models that reason more concisely without losing accuracy.
- [Kinetics: Rethinking Test-Time Scaling Law](../../archive/papers/2025/title-fe7ecea333b91370/summary.md) — Reworks test-time scaling laws to account for memory-access cost alongside compute, finding a 14B-parameter threshold below which test-time compute is less effective, and shows sparse attention substantially improves accuracy under a fixed test-time budget.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
