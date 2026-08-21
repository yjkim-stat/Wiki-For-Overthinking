# Best-of-N

<!-- auto:begin -->

A test-time-compute strategy that samples N candidate solutions independently and selects one, trading inference compute for accuracy. In the sources tagged separately under this exact capitalization: CaTS uses a self-distilled confidence signal to adaptively size the sampling budget per query instead of a fixed N; a theoretical paper derives worse sample-complexity bounds for best-of-n than for self-consistency; and 'Less Diverse, Less Safe' finds that reducing candidate diversity within Best-of-N/MCTS search substantially raises the rate of unsafe outputs. Note: this is the same underlying method as the archive's separate 'best-of-N sampling' entry -- the wiki did not merge the two spellings.

- **Kind**: method
- **Also called**: BoN, best-of-N sampling, best-of-n
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [adaptive test-time compute](../concepts/adaptive-test-time-compute.md), [Best-of-N sampling](best-of-n-sampling.md), [Compute-optimal inference](../concepts/compute-optimal-inference.md), [Confidence-based early stopping](confidence-based-early-stopping.md), [Confidence Calibration](../concepts/confidence-calibration.md), [early stopping](../concepts/early-stopping.md), [GSM8K](../datasets/gsm8k.md), [Majority Voting](majority-voting.md), [MATH500](../datasets/math500.md), [MathQA](../datasets/mathqa.md), [MBPP](../datasets/mbpp.md), [Monte Carlo Tree Search](monte-carlo-tree-search.md), [process reward model](process-reward-model.md), [Self-Consistency](self-consistency.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Test-Time Scaling](../concepts/test-time-scaling.md), [Tree Search Decoding](../concepts/tree-search-decoding.md), [weighted voting](../concepts/weighted-voting.md)

## Appears in

- [CaTS: Calibrated Test-Time Scaling for Efficient LLM Reasoning](../../archive/papers/2026/title-03232c54fde9b57f/summary.md) — Proposes CaTS, a calibrated test-time scaling framework that uses a self-distilled confidence signal to adaptively allocate sampling budget per query, including early stopping once the model is confident.
- [Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving](../../archive/papers/2025/title-0d818df77a2dc810/summary.md) — An empirical study of compute-optimal inference that measures accuracy against FLOPs for greedy decoding, sampling with majority and weighted voting, best-of-n and tree search across model sizes, and introduces REBASE, a reward-guided tree search.
- [Sample Complexity and Representation Ability of Test-time Scaling Paradigms](../../archive/papers/2026/title-27bc5c2aff7ebdab/summary.md) — A theoretical paper deriving sample-complexity bounds for self-consistency versus best-of-n, and an expressiveness result showing self-correction lets a Transformer simulate online learning over multiple tasks at test time.
- [Less Diverse, Less Safe: The Indirect But Pervasive Risk of Test-Time Scaling in Large Language Models](../../archive/papers/2026/title-abd61e399170fa2c/summary.md) — Shows that test-time-scaling methods such as Monte Carlo Tree Search and Best-of-N become substantially more likely to produce unsafe outputs when candidate diversity is curtailed, using a diagnostic protocol called RefDiv.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
