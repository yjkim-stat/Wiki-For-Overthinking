# generalization

<!-- auto:begin -->

Whether what a model learned in one setting holds outside it. With five sources the archive now carries both the behavioural claims and the theory that prices them. Behaviourally it records a recurring gap: a reasoning-structure intervention trained on 1K examples transfers across tasks, while arithmetic reverse-engineered to the neuron turns out to be neither an algorithm nor memorization but a bag of sparse heuristics — so benchmark transfer is evidence about coverage rather than about an algorithm having been learned. Three theoretical entries bound the question rather than illustrate it. A PAC-Bayes analysis on boolean functions makes the generalization gap scale with Fourier sparsity times squared degree, and shows chain of thought turning an exponential dependence on reasoning length into a linear one. A VC-dimension result prices chain-of-thought supervision at depth times parameters times a logarithm, with input length and reasoning length entering only inside that logarithm and only through their sum. And a negative result proves that for transformers of depth two or beyond no computable bound exists on how long the training inputs must be. Together they say the behavioural failures are not merely unlucky: in the general case no procedure can tell you in advance.

- **Kind**: concept
- **Also called**: generalisation, transfer
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 5

**Related**: [activation patching](../methods/activation-patching.md), [alignment tax](alignment-tax.md), [causal analysis](../methods/causal-analysis.md), [chain of thought](../methods/chain-of-thought.md), [circuit analysis](../methods/circuit-analysis.md), [circuit discovery](../methods/circuit-discovery.md), [data efficiency](data-efficiency.md), [expressivity](expressivity.md), [expressivity-learnability gap](expressivity-learnability-gap.md), [finite precision](finite-precision.md), [GPT-J 6B](../models/gpt-j-6b.md), [hard attention](hard-attention.md), [length generalization](length-generalization.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [localization](localization.md), [mechanistic interpretability](mechanistic-interpretability.md), [memorization](memorization.md), [modularity](modularity.md), [out-of-distribution generalization](out-of-distribution-generalization.md), [parity](../datasets/parity.md), [post-training](../methods/post-training.md), [Pythia-410M](../models/pythia-410m.md), [safety alignment](safety-alignment.md), [sample complexity](sample-complexity.md), [scaling laws](scaling-laws.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [teacher forcing](../methods/teacher-forcing.md), [VC dimension](vc-dimension.md)

## Appears in

- [Reasoning Structure Matters for Safety Alignment of Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-240/summary.md) — Argues reasoning models' safety failures come from the reasoning structure itself, and achieves safety alignment by altering that structure with 1K supervised examples and no RL.
- [A Sharper Picture of Generalization in Transformers](../../archive/papers/2026/local-03f1eff4f1d40725/summary.md) — Derives a non-vacuous PAC-Bayes generalization bound for transformers on boolean functions in terms of Fourier sparsity and degree, and uses it to show chain of thought turns an exponential dependence on reasoning length into a linear one for Parity.
- [Tight Sample Complexity of Transformers](../../archive/papers/2026/local-209065fd89f43691/summary.md) — Pins down the VC dimension of transformers as depth times parameters times a logarithm, and shows chain-of-thought learning by teacher forcing costs only logarithmically more as the number of reasoning steps grows.
- [Arithmetic Without Algorithms: Language Models Solve Math With a Bag of Heuristics](../../archive/papers/2025/local-26fdb25b9d157d04/summary.md) — Reverse-engineers the arithmetic circuit down to individual neurons and finds it is neither a learned algorithm nor memorization, but an unordered collection of sparse heuristic neurons that each fire on a numerical input pattern and vote for corresponding answers.
- [Length Generalization Bounds for Transformers](../../archive/papers/2026/local-bd58c1406f4a1ef5/summary.md) — Proves that no computable length-generalization bound exists for transformers of depth two or beyond, and gives a matching exponential bound for the positive fragment that corresponds to fixed-precision transformers.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
