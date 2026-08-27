# GAIA

<!-- auto:begin -->

A general-assistant benchmark dominated by web-search tasks, used across sources to evaluate agent harnesses and search-agent test-time-scaling/voting methods, including causal-intervention-based harness orchestration, retrieval-grounded voting, sequential-vs-parallel deep-search compute allocation, and deep-research agents that interleave search with reasoning and report drafting.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [BrowseComp](browsecomp.md), [Budget Forcing](../methods/budget-forcing.md), [deepseek-v4-flash](../models/deepseek-v4-flash.md), [deepseek-v4-pro](../models/deepseek-v4-pro.md), [GPQA](gpqa.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [HLE](hle.md), [Kimi-K2.5](../models/kimi-k2-5.md), [sequential vs. parallel test-time scaling](../concepts/sequential-vs-parallel-test-time-scaling.md), [SWE-bench Verified](swe-bench-verified.md)

## Appears in

- [CHILL-Harness: Counterfactual Harness Learning for Efficient Reasoning in Long-Horizon Agents](../../archive/papers/2026/arxiv-2607-25825/summary.md) — Treats an agent harness's orchestration decisions as causal interventions on the current workflow, learns which ones would improve it, and executes only those whose estimated advantage clears a margin -- so deliberation is spent where it changes the plan rather than at every step.
- [Beyond Confidence: Test-Time Scaling for Multi-Turn Search Agents via Retrieval Grounding](../../archive/papers/2026/arxiv-2608-24024/summary.md) — Identifies copy-inflation -- retrieved documents in a search agent's context systematically inflate the token log-probabilities of copied tokens -- as the reason logprob-based confidence voting (DeepConf) fails on multi-turn search agents, and fixes it with Retrieval-Grounded Voting (RGV), which weights each rollout by lexical overlap between its answer and the documents it retrieved instead of by internal confidence.
- [Pushing Test-Time Scaling Limits of Deep Search with Asymmetric Verification](../../archive/papers/2026/title-711c479b500244c5/summary.md) — Studies sequential and parallel test-time compute scaling for deep-search LLM agents and shows that allocating modest compute to a cheap verifier outperforms pushing sequential generation length further.
- [WebThinker: Empowering Large Reasoning Models with Deep Research Capability](../../archive/papers/2025/title-93df459afa09bdd6/summary.md) — WebThinker gives large reasoning models a Deep Web Explorer module and an Autonomous Think-Search-and-Draft strategy so they can search, navigate, and draft research reports interleaved with reasoning, trained via iterative online DPO, and it outperforms existing methods and strong proprietary systems on complex reasoning and report-generation benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
