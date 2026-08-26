<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# From "Aha Moments" to Controllable Thinking: Toward Meta-Cognitive Reasoning in LRMs via Decoupled Reasoning and Control

- **Authors**: Rui Ha, Rui Pu, Chaozhuo Li, Li Sun, Sen Su
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.304/>
- **PDF**: <https://aclanthology.org/2026.acl-long.304.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.304
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large Reasoning Models (LRMs) can exhibit step-by-step reasoning, reflection, and backtracking, but these behaviors are often unregulated, leading to overthinking. As a result, LRMs continue generating redundant reasoning even after reaching high-confidence conclusions. This increases inference cost and latency, limiting practical deployment. The root cause is the absence of an intrinsic mechanism to monitor the reasoning state and decide when to continue, backtrack, or stop. We propose MERA, a meta-cognitive reasoning framework that decouples reasoning from control to enable independent optimization of control strategies. MERA constructs high-quality reasoning–control supervision data via a takeover-based pipeline, and transforms long-horizon traces into structured reasoning–control alternating sequences for training. The model is trained with supervised fine-tuning to internalize the structured separation, and further optimized with Control-Segment Policy Optimization (CSPO), which combines segment-wise GRPO with control masking to focus learning on control segments. Experiments across reasoning benchmarks show that MERA improves both efficiency and accuracy.

---

Record id: `doi:10.18653/v1/2026.acl-long.304`
