# Kimi-K2.5

<!-- auto:begin -->

A model used as an annotator LRM (labeling safety judgments and extracting supporting evidence) in the TRACE benchmark's construction, and as one of the evaluated generator models in a retrieval-grounded-voting study of multi-turn search agents.

- **Kind**: model
- **Also called**: KIMI-K2.5, Kimi-K2.5
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [BrowseComp](../datasets/browsecomp.md), [DeepSeek-V3.2](deepseek-v3-2.md), [GAIA](../datasets/gaia.md), [Gemma-4-E4B](gemma-4-e4b.md), [gpt-oss-120b](gpt-oss-120b.md), [Qwen3.5-Plus](qwen3-5-plus.md), [Qwen3-8B](qwen3-8b.md)

## Appears in

- [Beyond Confidence: Test-Time Scaling for Multi-Turn Search Agents via Retrieval Grounding](../../archive/papers/2026/arxiv-2608-24024/summary.md) — Identifies copy-inflation -- retrieved documents in a search agent's context systematically inflate the token log-probabilities of copied tokens -- as the reason logprob-based confidence voting (DeepConf) fails on multi-turn search agents, and fixes it with Retrieval-Grounded Voting (RGV), which weights each rollout by lexical overlap between its answer and the documents it retrieved instead of by internal confidence.
- [TRACE: An Evidence-Grounded Benchmark for Safety Evaluation of Large Reasoning Models](../../archive/papers/2026/arxiv-2608-24232/summary.md) — TRACE is a benchmark that extends LLM-safety evaluation from prompts and final responses to the reasoning traces of large reasoning models, with evidence-grounded annotations for each safety label.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
