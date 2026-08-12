# sample complexity

<!-- auto:begin -->

How many training examples suffice to learn a target to a given accuracy, and the archive's measure of what reasoning supervision costs statistically. The sources agree the news is good and arrive at it differently. One bounds it parametrically through the VC dimension of transformers, finding chain-of-thought learning by teacher forcing costs O(LW log((T+T')W)) — so input length and the number of reasoning steps enter only inside a logarithm, and only through their sum. One bounds it by the target's Fourier structure via PAC-Bayes, where CoT turns Parity's dependence from exponential to linear in reasoning length. One shows the efficiency survives internalization, with implicit CoT learning k-parity from polynomially many samples. The common conclusion is that long reasoning chains are not statistically expensive; whatever they cost is compute or annotation.

- **Kind**: concept
- **Also called**: example complexity, statistical complexity
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [chain of thought](../methods/chain-of-thought.md), [curriculum learning](curriculum-learning.md), [effective depth](effective-depth.md), [expressivity-learnability gap](expressivity-learnability-gap.md), [generalization](generalization.md), [gradient descent analysis](../methods/gradient-descent-analysis.md), [implicit reasoning](implicit-reasoning.md), [latent reasoning](latent-reasoning.md), [mechanistic interpretability](mechanistic-interpretability.md), [parity](../datasets/parity.md), [teacher forcing](../methods/teacher-forcing.md), [test-time compute](test-time-compute.md)

## Appears in

- [A Sharper Picture of Generalization in Transformers](../../archive/papers/2026/local-03f1eff4f1d40725/summary.md) — Derives a non-vacuous PAC-Bayes generalization bound for transformers on boolean functions in terms of Fourier sparsity and degree, and uses it to show chain of thought turns an exponential dependence on reasoning length into a linear one for Parity.
- [Tight Sample Complexity of Transformers](../../archive/papers/2026/local-209065fd89f43691/summary.md) — Pins down the VC dimension of transformers as depth times parameters times a logarithm, and shows chain-of-thought learning by teacher forcing costs only logarithmically more as the number of reasoning steps grows.
- [Transformers Provably Learn to Internalize Chain-of-Thought](../../archive/papers/2026/local-ee30f023d9f2d8fb/summary.md) — Proves that reasoning can be moved from emitted tokens into hidden states without losing sample efficiency, using a curriculum that deletes thinking tokens in geometric chunks and so needs only logarithmically many training stages.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
