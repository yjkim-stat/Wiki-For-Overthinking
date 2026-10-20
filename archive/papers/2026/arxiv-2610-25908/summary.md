<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# CALM: Consistency-Aware Logit Masking in Decoding Space for Mitigating Overthinking of Large Reasoning Models

- **Authors**: Shengjing Liu, Feiyang Li, Yuxuan Yang, Yile Wang, Hui Huang
- **Venue**: cs.CL
- **Published**: 2026-10-19
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2610.25908>
- **PDF**: <https://arxiv.org/pdf/2610.25908v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.73

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large reasoning models (LRMs) have achieved strong performance on challenging mathematical and scientific tasks through long chain-of-thought reasoning, but they often suffer from overthinking with unnecessary reasoning steps. Existing truncation-based methods typically detect consecutive trial-answer agreement and force early exit, yet such local stopping signals do not necessarily indicate final-answer stability and can disrupt useful subsequent reflection or verification, potentially leading to performance degradation. We propose consistency-aware logit masking (CALM), a training-free decoding intervention for mitigating overthinking in LRMs. CALM first monitors trial answers at step boundaries and then applies logit masking to action transition point (ATP) tokens such as "Wait", "Alternatively", and "Hmm", suppressing redundant transitional reasoning while allowing the model to continue its thought process more naturally. Experiments across four advanced LRMs and five benchmarks show that CALM reduces token consumption by 18.6%-25.0% compared with full CoT reasoning while maintaining performance, and can even improve accuracy by 0.07%-1.48% by reducing redundant reasoning. LLM-as-a-Judge results also demonstrate that CALM provides more coherent and concise results.

---

Record id: `arxiv:2610.25908`
