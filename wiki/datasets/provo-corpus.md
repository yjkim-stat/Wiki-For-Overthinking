# Provo Corpus

<!-- auto:begin -->

The Provo Corpus is an eye-tracking reading-time dataset used to study whether language-model word-surprisal predicts human reading times: one source shows the well-known inverse-scaling effect (larger pretrained LMs predicting reading times worse than smaller ones) is not an artifact of the corpus itself, and another uses it to validate a working-memory-constrained GPT-2-small model injecting Gaussian noise into self-attention value vectors.

- **Kind**: dataset
- **Also called**: Provo Corpus
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

## Appears in

- [The Inverse Scaling Effect of Pre-Trained Language Model Surprisal Is Not Due to Data Leakage](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-91/summary.md) — Shows that the well-known inverse-scaling effect -- larger pre-trained language models' word-surprisal predicting human reading times worse than smaller models' -- is not an artifact of training-data leakage: overlap between five naturalistic reading-time corpora and two pre-training corpora is minimal, and models trained from scratch on leakage-free data still replicate the negative size-vs-fit relationship.
- [Memory efficiency and resource-rational encoding in sentence processing](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1550/summary.md) — Models human working-memory (WM) constraints in a GPT-2-small language model by injecting Gaussian noise into self-attention value vectors (with precision decaying exponentially by query-key distance) and training with a hybrid objective that trades off next-word prediction against total encoding precision, finding this explicit WM constraint improves alignment with human reading times and reshapes next-word predictions into a more compressed, categorical representational space.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
