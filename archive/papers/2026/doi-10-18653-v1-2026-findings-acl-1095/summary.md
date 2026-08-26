<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ThinkBrake: Efficient Reasoning via Log-Probability Margin Guided Decoding

- **Authors**: Sangjun Song, Minjae Oh, Seungkyu Lee, Sungmin Jo, Yohan Jo
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1095/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1095.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1095
- **Topics**: overthinking
- **Relevance score**: overthinking 0.62

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large Reasoning Models (LRMs) allocate substantial inference-time compute to Chain-of-Thought (CoT) reasoning, improving performance on mathematics, scientific QA, and tool usage. However, this introduces overthinking: LRMs often reach a correct intermediate solution, continue reasoning, and overwrite it with an incorrect answer. We first demonstrate that oracle stopping—where we inject lt;/think gt; at every sentence boundary and select the best stopping point in hindsight—improves average accuracy by 8% while reducing thinking tokens by 72%, exposing substantial overthinking. Motivated by this finding, we propose ThinkBrake, which monitors the log-probability margin between the top continuation token and lt;/think gt; at sentence boundaries, stopping reasoning when this margin narrows. ThinkBrake requires no training and achieves favorable accuracy–efficiency trade-offs across math, scientific QA, and tool usage benchmarks, reducing thinking token usage by up to 30%. Furthermore, we provide theoretical analysis showing that ThinkBrake is equivalent to test-time realignment with a reward bonus for the lt;/think gt; token.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1095`
