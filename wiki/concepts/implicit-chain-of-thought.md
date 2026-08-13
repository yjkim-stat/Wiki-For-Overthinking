# implicit chain of thought

<!-- auto:begin -->

Reasoning that has been moved out of emitted tokens and into hidden state, so the steps happen without being written. The two sources approach it from opposite ends. One proves it is possible without losing sample efficiency, using a curriculum that deletes thinking tokens in geometric chunks so only logarithmically many stages are needed. The other builds it: a small recurrent block between a frozen model's body and its head, refining latent states instead of generating text. The archive's caution attaches to the second -- its claim that latent-state stabilization shows the model is not guessing conflates convergence with correctness, and other entries here find intermediate answers stabilize whether or not they are right.

- **Kind**: concept
- **Also called**: implicit chain of thought, internalized chain of thought
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [answer stabilization](answer-stabilization.md), [chain of thought](../methods/chain-of-thought.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Coconut](../methods/coconut.md), [curriculum learning](curriculum-learning.md), [DeepSeek-R1](../models/deepseek-r1.md), [effective depth](effective-depth.md), [GPT-4](../models/gpt-4.md), [gradient descent analysis](../methods/gradient-descent-analysis.md), [implicit reasoning](implicit-reasoning.md), [latent reasoning](latent-reasoning.md), [parity](../datasets/parity.md), [ProofWriter](../datasets/proofwriter.md), [QwQ-32B](../models/qwq-32b.md), [RoBERTa](../models/roberta.md), [sample complexity](sample-complexity.md), [test-time compute](test-time-compute.md)

## Appears in

- [Think Deep, Speak Once: Relit, A Recursive Latent Implicit Transformer Framework](../../archive/papers/2026/arxiv-2608-08113/summary.md) — Bolts a small trainable recurrent block between a frozen 1.1B language model's body and its output head, so reasoning happens as repeated refinement of two latent vectors rather than as generated tokens.
- [Transformers Provably Learn to Internalize Chain-of-Thought](../../archive/papers/2026/local-ee30f023d9f2d8fb/summary.md) — Proves that reasoning can be moved from emitted tokens into hidden states without losing sample efficiency, using a curriculum that deletes thinking tokens in geometric chunks and so needs only logarithmically many training stages.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
