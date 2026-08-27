# BrowseComp

<!-- auto:begin -->

A benchmark for evaluating web-browsing/search LLM agents, used by sources to test test-time-scaling and voting methods for multi-turn search agents. One source treats it as a noisy open-web-retrieval setting where voting gains are largest; another uses it to study sequential vs. parallel test-time compute allocation with a cheap verifier.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Budget Forcing](../methods/budget-forcing.md), [GAIA](gaia.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [Kimi-K2.5](../models/kimi-k2-5.md), [sequential vs. parallel test-time scaling](../concepts/sequential-vs-parallel-test-time-scaling.md)

## Appears in

- [Beyond Confidence: Test-Time Scaling for Multi-Turn Search Agents via Retrieval Grounding](../../archive/papers/2026/arxiv-2608-24024/summary.md) — Identifies copy-inflation -- retrieved documents in a search agent's context systematically inflate the token log-probabilities of copied tokens -- as the reason logprob-based confidence voting (DeepConf) fails on multi-turn search agents, and fixes it with Retrieval-Grounded Voting (RGV), which weights each rollout by lexical overlap between its answer and the documents it retrieved instead of by internal confidence.
- [Routed Graph Handoff: Adaptive Format Selection for Multi-Agent LLM Delegation](../../archive/papers/2026/arxiv-2608-25277/summary.md) — Routed Graph Handoff (RGH) uses a lightweight LLM router to pick, per delegation, between a typed dependency-graph message and natural-language prose for multi-agent LLM handoffs, matching or beating NL-only on every one of four benchmarks while cutting token cost 2-3x.
- [Pushing Test-Time Scaling Limits of Deep Search with Asymmetric Verification](../../archive/papers/2026/title-711c479b500244c5/summary.md) — Studies sequential and parallel test-time compute scaling for deep-search LLM agents and shows that allocating modest compute to a cheap verifier outperforms pushing sequential generation length further.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
