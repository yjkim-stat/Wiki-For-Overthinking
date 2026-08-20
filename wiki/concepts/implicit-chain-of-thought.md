# implicit chain of thought

<!-- auto:begin -->

Performing the steps of a chain of thought without emitting them, and across 3 sources the target of both a training programme and a theoretical result. The theory: one source proves transformers provably learn to internalise chain of thought, which is the formal companion to the archive's empirical latent-reasoning material. The implementations keep the computation recurrent rather than autoregressive -- a small trainable recurrent block between a frozen model's body and its head, or evolving recurrent memory in a continuous workspace never decoded into language. The archive's related caution is the sharpest available on this idea: on off-the-shelf models, continuous-state decoding is functionally indistinguishable from discrete decoding, and in one fine-tuned latent method deleting every latent token changes accuracy by at most 1.0 point -- so internalisation must be demonstrated rather than assumed from the architecture.

- **Kind**: concept
- **Also called**: implicit chain of thought, internalized chain of thought, internalized reasoning
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [answer stabilization](answer-stabilization.md), [chain of thought](chain-of-thought.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Coconut](../methods/coconut.md), [compositional generalization](compositional-generalization.md), [curriculum learning](../methods/curriculum-learning.md), [DeepSeek-R1](../models/deepseek-r1.md), [effective depth](effective-depth.md), [GPT-4](../models/gpt-4.md), [gradient descent analysis](../methods/gradient-descent-analysis.md), [implicit reasoning](implicit-reasoning.md), [in-context learning](in-context-learning.md), [latent reasoning](latent-reasoning.md), [McNemar test](../methods/mcnemar-test.md), [monitorability](monitorability.md), [o1-mini](../models/o1-mini.md), [parity](../datasets/parity.md), [pass@k](pass-k.md), [ProofWriter](../datasets/proofwriter.md), [QwQ-32B](../models/qwq-32b.md), [recurrent depth](recurrent-depth.md), [RoBERTa](../models/roberta.md), [sample complexity](sample-complexity.md), [test-time compute](test-time-compute.md), [test-time scaling](test-time-scaling.md), [Wilson confidence interval](../methods/wilson-confidence-interval.md)

## Appears in

- [Think Deep, Speak Once: Relit, A Recursive Latent Implicit Transformer Framework](../../archive/papers/2026/arxiv-2608-08113/summary.md) — Bolts a small trainable recurrent block between a frozen 1.1B language model's body and its output head, so reasoning happens as repeated refinement of two latent vectors rather than as generated tokens.
- [BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](../../archive/papers/2026/arxiv-2608-09888/summary.md) — Combines in-context learning through evolving recurrent memory with iterative reasoning in a continuous latent workspace that is never decoded into language, reaching 29.5% pass@2 on public ARC-AGI-1 at $0.0007 per task from 150M parameters, and then probes with controlled tasks what the resulting demonstration-bound operators can and cannot do.
- [Transformers Provably Learn to Internalize Chain-of-Thought](../../archive/papers/2026/local-ee30f023d9f2d8fb/summary.md) — Proves that reasoning can be moved from emitted tokens into hidden states without losing sample efficiency, using a curriculum that deletes thinking tokens in geometric chunks and so needs only logarithmically many training stages.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
