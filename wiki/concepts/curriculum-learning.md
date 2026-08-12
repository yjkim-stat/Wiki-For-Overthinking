# curriculum learning

<!-- auto:begin -->

Ordering training so that a target is approached in stages, which both sources find is not an optimization convenience but a requirement. One proves curriculum is necessary rather than merely helpful for training latent reasoners: removing it collapses the model to at or below the no-CoT baseline on two of three benchmarks. The other designs the schedule to match the target's structure, deleting thinking tokens in geometric chunks aligned to the parity tree's levels rather than one at a time, which cuts the number of training stages from linear in chain length to logarithmic. The shared lesson is that the schedule should follow the shape of the computation being internalized, not the length of the text.

- **Kind**: concept
- **Also called**: curriculum, progressive training, staged training
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [chain of thought](../methods/chain-of-thought.md), [Coconut](../methods/coconut.md), [compounding error](compounding-error.md), [effective depth](effective-depth.md), [GPT-2](../models/gpt-2.md), [gradient descent analysis](../methods/gradient-descent-analysis.md), [GSM8K](../datasets/gsm8k.md), [implicit reasoning](implicit-reasoning.md), [information bottleneck](information-bottleneck.md), [latent chain of thought](../methods/latent-chain-of-thought.md), [latent reasoning](latent-reasoning.md), [parity](../datasets/parity.md), [ProntoQA](../datasets/prontoqa.md), [ProsQA](../datasets/prosqa.md), [sample complexity](sample-complexity.md), [self-consistency](../methods/self-consistency.md), [test-time compute](test-time-compute.md)

## Appears in

- [Capabilities and Fundamental Limits of Latent Chain-of-Thought](../../archive/papers/2026/local-6b66615b7bf3ef86/summary.md) — Explains why latent chain-of-thought excels at exploration but fails at computation by identifying decisional certainty as the governing variable, formalizing it as the Symbolic Index, and proving that curriculum learning is not merely helpful but necessary for training latent reasoners.
- [Transformers Provably Learn to Internalize Chain-of-Thought](../../archive/papers/2026/local-ee30f023d9f2d8fb/summary.md) — Proves that reasoning can be moved from emitted tokens into hidden states without losing sample efficiency, using a curriculum that deletes thinking tokens in geometric chunks and so needs only logarithmically many training stages.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
