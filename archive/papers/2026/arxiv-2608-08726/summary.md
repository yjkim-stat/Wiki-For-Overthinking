<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# PAST: Privileged Adaptation from Complete Student Trajectories for On-Policy Self-Distillation

- **Authors**: Yangyang Feng, Zhuoyan Feng, Junlan Chen
- **Venue**: cs.LG
- **Published**: 2026-08-09
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.08726>
- **PDF**: <https://arxiv.org/pdf/2608.08726v1>
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.40, reasoning-training 0.25

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

On-policy self-distillation (OPSD) uses a privileged teacher to supervise a reasoning model on prefixes sampled from its own rollouts. Yet each rollout also reveals how the student's response unfolds and whether it succeeds, student-specific hindsight that standard OPSD does not use to form the teacher. We introduce Privileged Adaptation from Student Trajectories (PAST), which treats each completed student trajectory as additional privileged information for the OPSD teacher while leaving the student's distillation prefixes unchanged. PAST preserves the student's next-token distribution on correct trajectories and uses failed trajectories to adapt the teacher toward verified success under student-proximity regularization. We characterize what such a trajectory-conditioned teacher can transfer to a prefix-only student. Forward-KL distillation projects the teacher distributions to their conditional arithmetic mean given the prefix. This projection separates trajectory-specific variation that remains privileged from the mean policy shift available to the student. For correct trajectories, the unclipped population objective also has the frozen student as an ideal distributional fixed point. Across three mathematical reasoning benchmarks, PAST improves the Avg@12 macro average over Vanilla OPSD by 5.6 percentage points. A $2\times2$ factorial study shows gains from both complete-trajectory access and teacher adaptation, while trajectory removal and shuffling confirm that the adapted teacher uses the matching hindsight context.

---

Record id: `arxiv:2608.08726`
