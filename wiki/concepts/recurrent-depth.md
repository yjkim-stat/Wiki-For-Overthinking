# recurrent depth

<!-- auto:begin -->

Applying a shared block repeatedly to a latent state so that effective computational depth is decoupled from parameter count, with reasoning happening as refinement of a state rather than as generated tokens. The two sources instantiate it differently and reach different conclusions about what it buys. One bolts a small trainable recurrent block between a frozen 1.1B model's body and its output head, with a tripartite state -- a frozen semantic anchor that cannot drift however deep the recursion goes, an answer state, and a latent scratchpad -- residual refinement so each step adds a delta rather than regenerating, and adaptive halting whose reported depth rises with task difficulty (3.6 steps on the easiest of its four sets, 7.8 on the hardest). The other combines recurrent memory updated by in-context demonstrations with iterative latent computation, and reports 29.5 percent pass@2 on ARC-AGI-1 at $0.0007 per task from 150M parameters, with accuracy rising monotonically as the latent reasoning effort is increased. The archive's reading of the first records a caveat that bears on both: its comparison trains on each dataset's training split while the language-model numbers it is compared against are few-shot, so the headline is not like for like.

- **Kind**: concept
- **Also called**: looped transformer, recursive depth
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [answer stabilization](answer-stabilization.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Coconut](../methods/coconut.md), [compositional generalization](compositional-generalization.md), [DeepSeek-R1](../models/deepseek-r1.md), [GPT-4](../models/gpt-4.md), [implicit chain of thought](implicit-chain-of-thought.md), [in-context learning](in-context-learning.md), [latent reasoning](latent-reasoning.md), [monitorability](monitorability.md), [pass@k](pass-k.md), [ProofWriter](../datasets/proofwriter.md), [QwQ-32B](../models/qwq-32b.md), [RoBERTa](../models/roberta.md), [test-time scaling](test-time-scaling.md), [Wilson confidence interval](../methods/wilson-confidence-interval.md)

## Appears in

- [Think Deep, Speak Once: Relit, A Recursive Latent Implicit Transformer Framework](../../archive/papers/2026/arxiv-2608-08113/summary.md) — Bolts a small trainable recurrent block between a frozen 1.1B language model's body and its output head, so reasoning happens as repeated refinement of two latent vectors rather than as generated tokens.
- [BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](../../archive/papers/2026/arxiv-2608-09888/summary.md) — Combines in-context learning through evolving recurrent memory with iterative reasoning in a continuous latent workspace that is never decoded into language, reaching 29.5% pass@2 on public ARC-AGI-1 at $0.0007 per task from 150M parameters, and then probes with controlled tasks what the resulting demonstration-bound operators can and cannot do.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
