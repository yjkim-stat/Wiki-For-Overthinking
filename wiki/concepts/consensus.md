# consensus

<!-- auto:begin -->

Agreement among several sampled answers or several agents, used both as a selection rule and as a signal about confidence. These sources are useful because both treat unweighted consensus as the thing to improve on rather than the answer. The claim-level work reallocates half of a sampling budget away from generating more solutions and toward asking the same model to refute a handful of decision-critical claims from each trace, then weights the vote by how many claims survive -- with a nonlinear reliability score that lets a smaller but better-supported group overturn a numerically larger consensus, and a decomposition showing the gain comes from falsification-based reweighting rather than from the claim prompt. Its own limitation is the boundary of the idea: a near-saturated model already above 90 gains at most 2.60, so the benefit is conditional on the base consensus being unreliable. The deliberative-diagnosis work uses consensus as a filter over a broadened candidate space rather than as a vote, and traces where each correct answer entered -- the share arriving only through late refinement rises from 7 percent on easy cases to 36 percent where single-model inference recovered nothing. Together they mark the same shape: consensus is a mechanism for selecting among candidates and contributes nothing the candidate set does not contain, so widening the space and filtering it are separate jobs.

- **Kind**: concept
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [answer aggregation](../methods/answer-aggregation.md), [best-of-n](../methods/best-of-n.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Claude Haiku 4.5](../models/claude-haiku-4-5.md), [Claude Sonnet 4.6](../models/claude-sonnet-4-6.md), [CMIMC](../datasets/cmimc.md), [difficulty conditioning](difficulty-conditioning.md), [Gemini-3-Flash](../models/gemini-3-flash.md), [Gemma-3-12B](../models/gemma-3-12b.md), [generation-verification gap](generation-verification-gap.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [gpt-oss-20b](../models/gpt-oss-20b.md), [HMMT](../datasets/hmmt.md), [jury aggregation](../methods/jury-aggregation.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [majority voting](../methods/majority-voting.md), [matched-budget comparison](matched-budget-comparison.md), [multi-agent pipeline](multi-agent-pipeline.md), [pass@k](pass-k.md), [persona conditioning](../methods/persona-conditioning.md), [pool oracle](pool-oracle.md), [process supervision](process-supervision.md), [Qwen3.5-27B](../models/qwen3-5-27b.md), [selection signal](selection-signal.md), [self-consistency](../methods/self-consistency.md), [test-time scaling](test-time-scaling.md), [verifier-free verification](../methods/verifier-free-verification.md)

## Appears in

- [Test-Time Scaling for CAD Generation via Verifier-Free Consensus Selection](../../archive/papers/2026/arxiv-2608-09706/summary.md) — Asks whether a candidate pool contains enough signal to select from itself, by compiling sampled CAD programs into 3D models and returning the one that agrees most with the rest -- and finds this verifier-free rule beats a vision-language verifier on every geometric metric when both select from the identical pool.
- [Social Chain of Thought: A Multi-Agent Architecture Grounded in Medical Differential Diagnosis Methodology](../../archive/papers/2026/arxiv-2608-11420/summary.md) — Structures multi-agent medical differential diagnosis as rounds of persona-conditioned specialist deliberation, and shows the recall advantage is not reproduced by best-of-n sampling from the same model, concentrates entirely in the cases where monolithic inference fails, and reverses on the easiest quartile.
- [Claim-Level Reliability Assessment for Efficient Test-Time Reasoning](../../archive/papers/2026/arxiv-2608-11994/summary.md) — Reallocates half of a test-time sampling budget from generating more solutions to asking the same model to refute a handful of decision-critical claims extracted from each trace, then weights the consensus vote by how many claims survive.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
