<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Label-Free Parkinson's Disease Screening from Face and Voice through Mechanistic Interpretability

- **Authors**: Jiaheng Su, Yu Sun
- **Venue**: cs.LG
- **Published**: 2026-08-10
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.08976>
- **PDF**: <https://arxiv.org/pdf/2608.08976v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Parkinson's disease (PD) is the second most common neurodegenerative disorder. Typical machine learning screening methods require PD labels, but the available data is limited by privacy concerns and the need for expert annotation. We propose a label-free face-plus-voice PD screen built entirely on frozen pretrained encoders--a face-expression Vision Transformer and HuBERT--in which no PD label touches any fit; the reference is training controls only. The voice modality uses a synthetic-dysarthria contrastive activation addition (CAA) direction built from time-stretch and breathy degradation of healthy speech; the face modality uses a k-nearest-neighbor anomaly score to the control embedding cluster. We introduce the alignment principle, a post-hoc analysis showing that a synthetic-degradation CAA detector works when the cosine similarity between the synthetic and real disease directions exceeds zero. Measured on the YouTubePD benchmark, this cosine is +0.37 for voice (CAA works, AUROC 0.765) and -0.48 for face (CAA fails; anomaly succeeds, AUROC 0.751). Equal-weight late fusion reaches AUROC 0.802 (95% CI [0.70,0.89]) with NPV 0.95, supporting a rule-out triage interpretation. An overfitting audit shows the voice detector transfers cleanly, while the face-side--and thus fused--AUROC is potentially optimistic pending external validation.

---

Record id: `arxiv:2608.08976`
