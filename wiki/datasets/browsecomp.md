# BrowseComp

<!-- auto:begin -->

A benchmark for web-browsing agents, and the point at which this archive's test-time-scaling question moves from a single reasoning trace to a multi-turn agent with retrieval. None of the five sources defines it; all five use it to ask how extra compute should be spent when the model is searching rather than thinking alone, and they answer differently. 'Pushing Test-Time Scaling Limits of Deep Search' finds that giving modest compute to a cheap verifier beats extending sequential generation. BrowseConf finds web agents poorly calibrated in absolute terms - verbalised confidence systematically exceeds accuracy - yet strongly rank-correlated with correctness, so confidence remains usable for allocation even where it is wrong as a probability. 'Beyond Confidence' identifies why the usual confidence signal breaks here at all: retrieved documents in context inflate the log-probabilities of tokens copied from them, so log-probability voting measures copying rather than conviction. FS-Researcher and Routed Graph Handoff scale by moving state out of the context window and by choosing the handoff format per delegation.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 5

**Related**: [BFCL v3](bfcl-v3.md), [Budget Forcing](../methods/budget-forcing.md), [Claude Sonnet 4.5](../models/claude-sonnet-4-5.md), [Confidence-Informed Self-Consistency (CISC, baseline)](../methods/confidence-informed-self-consistency-cisc-baseline.md), [GAIA](gaia.md), [Gemini-2.5-Pro](../models/gemini-2-5-pro.md), [GPT-5](../models/gpt-5.md), [GPT-5 mini](../models/gpt-5-mini.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [Kimi-K2.5](../models/kimi-k2-5.md), [Overthinking](../concepts/overthinking.md), [Self-Consistency (baseline)](../methods/self-consistency-baseline.md), [sequential vs. parallel test-time scaling](../concepts/sequential-vs-parallel-test-time-scaling.md), [Test-Time Scaling](../concepts/test-time-scaling.md)

## Appears in

- [Beyond Confidence: Test-Time Scaling for Multi-Turn Search Agents via Retrieval Grounding](../../archive/papers/2026/arxiv-2608-24024/summary.md) — Identifies copy-inflation -- retrieved documents in a search agent's context systematically inflate the token log-probabilities of copied tokens -- as the reason logprob-based confidence voting (DeepConf) fails on multi-turn search agents, and fixes it with Retrieval-Grounded Voting (RGV), which weights each rollout by lexical overlap between its answer and the documents it retrieved instead of by internal confidence.
- [Routed Graph Handoff: Adaptive Format Selection for Multi-Agent LLM Delegation](../../archive/papers/2026/arxiv-2608-25277/summary.md) — Routed Graph Handoff (RGH) uses a lightweight LLM router to pick, per delegation, between a typed dependency-graph message and natural-language prose for multi-agent LLM handoffs, matching or beating NL-only on every one of four benchmarks while cutting token cost 2-3x.
- [FS-Researcher: Test-Time Scaling for Long-Horizon Research Tasks with File-System-Based Agents](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-288/summary.md) — FS-Researcher is a dual-agent (Context Builder / Report Writer) deep-research framework that scales test-time compute beyond a single context window by persisting evidence and task state in an external file-system workspace instead of the model's context, achieving state-of-the-art report quality on two open-ended benchmarks and outperforming official agent harnesses on an answer-verifiable search benchmark.
- [BrowseConf: Confidence-Guided Test-Time Scaling for Web Agents](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-21/summary.md) — BrowseConf shows that despite web-search agents being poorly calibrated in absolute terms (verbalized confidence systematically exceeds actual accuracy), their confidence is strongly rank-correlated with correctness -- near-zero accuracy below 70% confidence, more than double the average accuracy above 95% -- and exploits this by triggering additional search attempts only when confidence falls below a calibrated threshold rather than always sampling a fixed number, matching or beating fixed-budget Self-Consistency/CISC on BrowseComp while cutting average attempts from a fixed 10 down to 2.06-5.72.
- [Pushing Test-Time Scaling Limits of Deep Search with Asymmetric Verification](../../archive/papers/2026/title-711c479b500244c5/summary.md) — Studies sequential and parallel test-time compute scaling for deep-search LLM agents and shows that allocating modest compute to a cheap verifier outperforms pushing sequential generation length further.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
