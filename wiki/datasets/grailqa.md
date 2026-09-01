# GrailQA

<!-- auto:begin -->

GrailQA is a multi-hop knowledge-graph question-answering benchmark used to evaluate Thought-Action Graph (TAG) reasoning, which distills past successful LLM-knowledge-graph interaction trajectories into reusable reasoning operators, and fs1, which fine-tunes LLMs on knowledge-graph-path-grounded reasoning traces to improve factual accuracy.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [DeepSeek-R1 (teacher)](../models/deepseek-r1-teacher.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Qwen2.5 7B](../models/qwen2-5-7b.md), [QwQ-32B (teacher)](../models/qwq-32b-teacher.md), [SimpleQA](simpleqa.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md), [WebQSP](webqsp.md)

## Appears in

- [Thought-Action Graph Reasoning: Faithful and Efficient Reasoning of Large Language Models via Reusing Past Experience](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1572/summary.md) — Thought-Action Graph (TAG) distills past successful LLM-knowledge-graph interaction trajectories into a structured, reusable repository of fine-grained reasoning operators (a thought layer of abstract query patterns plus an action layer of concrete entity/relation parameters), letting TAG-Reasoning (TAGR) retrieve and assemble a query-specific reasoning blueprint offline instead of exploring the KG online -- outperforming 15 baselines on three KGQA benchmarks while using far fewer LLM calls (3, vs. up to 11.6) and generated tokens (65-71, vs. hundreds).
- [Follow the Path: Reasoning over Knowledge Graph Paths to Improve Large Language Model Factuality](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-561/summary.md) — fs1 fine-tunes LLMs on reasoning traces grounded in knowledge-graph paths (rather than raw distilled reasoning traces), improving factual accuracy on complex multi-hop QA by 6-14 pass@16 points while also producing shorter reasoning traces than the ungrounded baseline.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
