# latent reasoning

<!-- auto:begin -->

Reasoning carried in continuous internal states rather than in emitted tokens, treated by the sources both as an efficiency measure and as a loss of the readable trace that monitoring depends on. One finds monitorability survives better than expected, depending more on task structure and access to internals than on whether reasoning is explicit or latent. One makes latent prediction a pretraining objective, adding a higher-level abstract latent to limit error accumulation over long horizons. One keeps discrete decoding except at low-confidence steps, which concentrates the unreadable portion exactly where decisions are being made. The three use the term at different levels — inference mode, pretraining target, and per-step gate.

- **Kind**: concept
- **Also called**: implicit chain of thought, latent-space reasoning
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 5

**Related**: [activation probing](../methods/activation-probing.md), [belief state](belief-state.md), [chain of thought](../methods/chain-of-thought.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [circuit complexity](circuit-complexity.md), [compounding error](compounding-error.md), [curriculum learning](curriculum-learning.md), [effective depth](effective-depth.md), [entropy collapse](entropy-collapse.md), [exploration-exploitation trade-off](exploration-exploitation-trade-off.md), [expressivity](expressivity.md), [gradient descent analysis](../methods/gradient-descent-analysis.md), [implicit reasoning](implicit-reasoning.md), [latent chain of thought](../methods/latent-chain-of-thought.md), [linear probe](../methods/linear-probe.md), [monitorability](monitorability.md), [parity](../datasets/parity.md), [sample complexity](sample-complexity.md), [speculative decoding](../methods/speculative-decoding.md), [teacher forcing](../methods/teacher-forcing.md), [test-time compute](test-time-compute.md), [token-level entropy](token-level-entropy.md)

## Appears in

- [Does Out-of-Sight Equal Out-of-Mind in CoT Monitorability?](../../archive/papers/2026/arxiv-2608-04928/summary.md) — Asks whether latent CoT destroys monitorability, and finds monitorability depends more on the task and on access to internals than on whether reasoning is explicit or latent.
- [Hierarchical Latent Prediction for Language Models](../../archive/papers/2026/arxiv-2608-05806/summary.md) — Adds a higher-level abstract latent as an auxiliary pretraining target to reduce compounding error in latent-space rollouts, aiming at longer-horizon coherence than multi-token or next-latent prediction.
- [SeLaR: Selective Latent Reasoning in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-320/summary.md) — Switches to soft-embedding latent reasoning only at low-confidence steps, keeping discrete decoding elsewhere, and pushes the soft embeddings away from the top token to stop them collapsing.
- [The Expressive Power of Transformers with Chain of Thought](../../archive/papers/2024/local-17f5eb14b12eda9b/summary.md) — Characterizes exactly how much computational power a chain of thought buys as a function of its length, sandwiching the class of languages a decoder recognizes with t(n) decoding steps between two standard complexity classes.
- [Transformers Provably Learn to Internalize Chain-of-Thought](../../archive/papers/2026/local-ee30f023d9f2d8fb/summary.md) — Proves that reasoning can be moved from emitted tokens into hidden states without losing sample efficiency, using a curriculum that deletes thinking tokens in geometric chunks and so needs only logarithmically many training stages.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
