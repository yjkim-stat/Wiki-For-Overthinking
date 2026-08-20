# state tracking

<!-- auto:begin -->

Maintaining an accurate representation of what has changed over the course of a problem, which the sources treat as a prerequisite that is separately measurable from reasoning. One uses chess because it demands rule adherence and game-state tracking alongside strategy, and finds some models lose to random play. One builds multi-turn interactive tasks that require tracking across exchanges with an environment. One asks whether models actually read what they previously wrote, testing causal registers in a scratchpad — which makes the question sharper: the state is present in the context and the issue is whether it is used. Failures here are easily misread as reasoning failures.

- **Kind**: concept
- **Also called**: context tracking, scratchpad use, state maintenance
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [activation patching](../methods/activation-patching.md), [attention analysis](../methods/attention-analysis.md), [chain of thought](../methods/chain-of-thought.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [circuit complexity](circuit-complexity.md), [construct validity](construct-validity.md), [expressivity-learnability gap](expressivity-learnability-gap.md), [gradient descent analysis](../methods/gradient-descent-analysis.md), [KV cache](kv-cache.md), [length generalization](length-generalization.md), [linear probe](../methods/linear-probe.md), [long-horizon reasoning](long-horizon-reasoning.md), [Mistral-7B-v0.3](../models/mistral-7b-v0-3.md), [multi-turn reasoning](../methods/multi-turn-reasoning.md), [pattern recognition versus reasoning](pattern-recognition-versus-reasoning.md), [process supervision](process-supervision.md), [Qwen2.5-coder-7B](../models/qwen2-5-coder-7b.md), [Qwen3-8B](../models/qwen3-8b.md), [residual stream](residual-stream.md), [selectivity control](selectivity-control.md), [self-training](self-training.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [training dynamics](training-dynamics.md)

## Appears in

- [ChessArena: A Chess Testbed for Evaluating Strategic Reasoning Capabilities of Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-360/summary.md) — A competitive chess testbed where 13 models play each other, and no model beats a human-amateur-level engine while some lose to random play.
- [MTR-Bench: A Comprehensive Benchmark for Multi-Turn Reasoning Evaluation](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-984/summary.md) — A fully automated multi-turn reasoning benchmark of 40 tasks and 3600 instances requiring interaction with an environment, on which frontier reasoning models fall short.
- [Do Models Read What They Write? Causal Registers in Scratchpad Reasoning](../../archive/papers/2026/local-54a1c25fa51cd59a/summary.md) — Edits the internal representation of a written scratchpad state while holding the printed text fixed, and asks whether the next step follows the transition rule applied to the edited value — turning 'does the model use its scratchpad?' into a causal test with a single correct answer.
- [Transformers Provably Learn Chain-of-Thought Reasoning with Length Generalization](../../archive/papers/2025/local-fe69869b0e362891/summary.md) — Gives the first optimization guarantee that gradient descent trains constant-depth transformers to solve NC1-complete problems with chain of thought, and shows the algebraic structure of the task decides how far the learned reasoning extrapolates.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
