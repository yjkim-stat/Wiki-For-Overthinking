<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Early Stopping in Large Reasoning Models: A Survey and Empirical Audit of Efficiency and Reliability

- **Authors**: Quang Hung Nguyen, Hanh Nguyen, Thanh Tam Nguyen, Quoc Viet Hung Nguyen, Trinh Pham, Thanh Trung Huynh
- **Venue**: cs.AI
- **Published**: 2026-11-03
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2611.00166>
- **PDF**: <https://arxiv.org/pdf/2611.00166>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.70

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large reasoning models can improve accuracy by generating longer reasoning traces, but some of this computation may be unnecessary. Early-stopping methods aim to stop once enough reasoning is available to answer. Evaluating these methods requires accounting for the cost of deciding when to stop and the reliability of the resulting answer. We evaluate different methods across five reasoning models on mathematical and scientific reasoning, code generation, and factuality tasks by using a shared rollout replay protocol. We introduce Target-Integrated Token Efficiency (TITE) to measure efficiency relative to the oracle across accuracy targets. We also examine correctness at later exit positions, transfer across models and tasks, post-stop reasoning continuation, and retained justification quality. In our experiments, correctness can decrease at later positions beyond what the fitted decoding-noise model predicts. Reliability checks also reveal continued reasoning after forced termination and weaker supporting reasoning in some correct early-stopping outputs. The implementation can be found in https://github.com/hung20gg/audit-early-stopping.

---

Record id: `arxiv:2611.00166`
