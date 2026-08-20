# expressivity-learnability gap

<!-- auto:begin -->

The gap between what a transformer can represent and what training can actually find from finite data, which the sources treat as the thing expressivity results leave unaddressed. One makes it quantitative on boolean functions, showing the generalization gap scales as the Fourier sparsity times the squared degree, so a high-degree function can be expressible and out of reach. One closes it from the statistical side, giving tight VC-dimension and chain-of-thought sample-complexity bounds so that representational results can be converted into learning guarantees. One closes it from the optimization side, proving gradient descent reaches NC^1-complete problems with CoT where prior optimization analyses had reached only TC^0. Together they mark the three separate things 'can solve' can mean: representable, learnable from data, and findable by gradient descent.

- **Kind**: concept
- **Also called**: expressiveness-learnability gap, representation-learning gap
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [attention analysis](../methods/attention-analysis.md), [chain of thought](chain-of-thought.md), [circuit complexity](circuit-complexity.md), [generalization](generalization.md), [gradient descent analysis](../methods/gradient-descent-analysis.md), [hard attention](../methods/hard-attention.md), [length generalization](length-generalization.md), [mechanistic interpretability](mechanistic-interpretability.md), [parity](../datasets/parity.md), [sample complexity](sample-complexity.md), [self-training](self-training.md), [state tracking](state-tracking.md), [teacher forcing](../methods/teacher-forcing.md), [training dynamics](training-dynamics.md), [VC dimension](vc-dimension.md)

## Appears in

- [A Sharper Picture of Generalization in Transformers](../../archive/papers/2026/local-03f1eff4f1d40725/summary.md) — Derives a non-vacuous PAC-Bayes generalization bound for transformers on boolean functions in terms of Fourier sparsity and degree, and uses it to show chain of thought turns an exponential dependence on reasoning length into a linear one for Parity.
- [Tight Sample Complexity of Transformers](../../archive/papers/2026/local-209065fd89f43691/summary.md) — Pins down the VC dimension of transformers as depth times parameters times a logarithm, and shows chain-of-thought learning by teacher forcing costs only logarithmically more as the number of reasoning steps grows.
- [Transformers Provably Learn Chain-of-Thought Reasoning with Length Generalization](../../archive/papers/2025/local-fe69869b0e362891/summary.md) — Gives the first optimization guarantee that gradient descent trains constant-depth transformers to solve NC1-complete problems with chain of thought, and shows the algebraic structure of the task decides how far the learned reasoning extrapolates.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._

### The chain is now complete, and it is three separate claims

Twelve theory papers filed in one batch (2026-08-09) close a loop this archive
previously held only the first link of. "A transformer with CoT can solve X" turns
out to name three different results, and until now only the first was here:

1. **Representable.** A constant-depth transformer with a linear number of CoT
   steps can express NC^1-complete problems — automaton simulation, and beyond
   that P with polynomial steps. Two groups prove this independently under
   different precision models and agree on the regime boundaries: logarithmic
   steps buy essentially nothing, linear steps buy recurrence.
2. **Learnable from data.** Sample complexity for CoT learning by teacher
   forcing is O(LW log((T+T')W)), with a matching lower bound. Input length and
   number of reasoning steps enter only inside a logarithm, and only via their
   sum. Long chains are not statistically expensive.
3. **Findable by gradient descent.** Constant-depth transformers trained by GD
   provably reach NC^1-complete problems with CoT. Prior optimization analyses
   had covered only TC^0 tasks — the parallelizable ones that need no sequential
   reasoning, i.e. exactly the regime where CoT is not the interesting variable.

That the three arrive separately is the point. An expressivity result is
compatible with the target being unlearnable, and a sample-complexity result is
compatible with SGD never finding it. The archive should not let a paper's
"transformers can solve" be read across these without checking which one it
proved.

### What is still missing

The `O(omega * D_f^2)` generalization bound says which reasoning problems are
hard — those whose targets have high Fourier degree — but it is stated on boolean
domains for an idealized low-sharpness learner, not SGD. And the archive has
**nothing** connecting these bounds to the empirical scaling behaviour of
deployed models. The theory says CoT changes a complexity class; no source here
measures whether a frontier model's gains track that boundary.
