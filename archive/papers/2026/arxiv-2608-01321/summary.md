<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# BiCAA: Bidirectional Credit Assignment for Search-Augmented Agent

- **Authors**: Yibin Huang, Bin Xu, Hailong Cao, Conghui Zhu
- **Venue**: cs.CL
- **Published**: 2026-08-02
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.01321>
- **PDF**: <https://arxiv.org/pdf/2608.01321v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Multi-step search is a fundamental capability for search agents, enabling them to iteratively acquire, refine, and integrate external evidence for complex reasoning QA. However, vanilla GRPO allocates rewards exclusively based on the model's final outputs, yielding outcome-only supervision with no supervisory signals for intermediate reasoning steps. Such sparse supervision easily causes training instability and redundant search behaviors on multi-step search tasks. To mitigate this limitation, we adopt process reward to deliver stepwise supervision signals. For this process reward, we propose two complementary criteria to judge each search step: whether the step yields new evidence to facilitate problem solving, and whether it forms an efficient, pivotal intermediate decision within the overall reasoning trajectory. Building on this insight, we propose BiCAA: a bidirectional credit assignment framework that delivers dense, distinguishing process rewards for search-augmented agents. BiCAA builds bidirectional process rewards by fusing two complementary signals: forward solvability gain and hindsight success criticality. The former quantifies step-wise improvements in answer plausibility, while the latter evaluates each step's necessity for final success via hindsight outcome-based criticality scoring. We modulate and aggregate the two signals and then fuse them with the outcome reward. Experiments on search-augmented QA benchmarks show that BiCAA stabilizes policy optimization, reduces redundant search behavior, and achieves competitive performance.

---

Record id: `arxiv:2608.01321`
