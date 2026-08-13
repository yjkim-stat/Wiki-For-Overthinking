<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Diagnosis Before Recovery: Turning Agent Failures into Selective Self-Correction

- **Authors**: Pan Wang, Yihao Hu, Hang Wang, Zirui Lv, Xin Zhang, Jianshe Li, Jiang-Ming Yang, Wei Wu, Yongqi Tong
- **Venue**: cs.CL
- **Published**: 2026-08-12
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.11772>
- **PDF**: <https://arxiv.org/pdf/2608.11772v1>
- **Topics**: test-time-scaling
- **Relevance score**: test-time-scaling 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Self-correction is particularly useful when a failure constrains the next repair. Coding agents benefit from this property because compilers, tests, and execution traces turn many failures into typed recovery signals, but broad language-agent tasks often expose only a coarse task failure. This creates a tension for generic recovery playbooks: they broaden the agent's context precisely when the system needs a narrower repair interface, mixing incompatible signals for invalid actions, missing procedures, and strict-format errors. Our insight is that development-set failures can recover part of the missing diagnostic substrate by deciding which recovery interventions are admissible before test-time correction. We propose DARC, a diagnosis-guided recovery harness that profiles task-family failure modes, prunes mismatched interventions from a shared recovery library, and freezes a verifier-selected success-cost policy for deployment. This causal order makes correction selective: the harness first determines what kind of failure can be repaired, then decides how much recovery evidence to spend. In ALFWorld, AppWorld, and XBRL Finance, the same protocol yields an action-validity harness, a procedural-recovery fallback, and a format-precision retrieval policy; in each evaluated setting it improves average task performance over base agents and broad playbooks while reducing environment steps or retrieval budget. Our experiments show that failures need not trigger uniformly more context: DARC turns self-correction from prompt expansion into recovery-interface design. DARC provides a practical route toward more reliable agents in domains where compiler-like feedback is absent: making failures actionable before making contexts larger.

---

Record id: `arxiv:2608.11772`
