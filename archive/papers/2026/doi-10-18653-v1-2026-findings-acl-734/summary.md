<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# When Internalization Fails: Finding Better Targets for Reasoning Compression

- **Authors**: Mourad Heddaya, Manley Roberts, Rohan Wadhawan, Chenhao Tan
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.734/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.734.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.734
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Reasoning language models generate long reasoning traces that increase latency and cost. We study how to shorten these traces while preserving accuracy on competition-level mathematics. In a teacher-student distillation setup, we compare three approaches: (i) inference-time truncation after the first k tokens, (ii) Implicit Chain-of-Thought (ICoT)-style curricula that progressively shorten the teacher trace during training, and (iii) direct distillation to shorter reasoning traces. Using NuminaMath 1.5 with traces from DeepSeek-R1 and QwQ-32B, we distill into Qwen2.5-7B and measure accuracy against total tokens generated. We find: (1) with standard SFT and first-k truncation, models compensate by generating longer text after reasoning, undermining token savings; (2) ICoT-style curricula provide little benefit on competition-level mathematics, where reasoning traces are long and diverse; and (3) training on post-think, text the teacher generates after reasoning, achieves the best accuracy–efficiency trade-off among all shortened targets, outperforming generic summaries at matched token budgets. These results show that curriculum-based internalization methods effective on simple tasks do not transfer to complex reasoning, and that post-think provides a better distillation target.

---

Record id: `doi:10.18653/v1/2026.findings-acl.734`
