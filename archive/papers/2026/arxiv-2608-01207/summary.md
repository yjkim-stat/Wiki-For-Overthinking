<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# It's the Decoding Format, Not the Perturbation: Auditing Consistency-Based Selection for Vision-Language Test-Time Scaling

- **Authors**: Puzhuo Zheng, Hasan Kurban
- **Venue**: cs.CV
- **Published**: 2026-08-02
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.01207>
- **PDF**: <https://arxiv.org/pdf/2608.01207v2>
- **Topics**: test-time-scaling
- **Relevance score**: reasoning-training 0.25, test-time-scaling 0.62

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Test-time scaling lifts large language model reasoning by sampling many candidate solutions and selecting among them, yet the same recipe transfers poorly to vision-language models (VLMs): recent work shows that simple majority voting beats selection methods built on the model's own self-verification, apparently because at the selection layer an image-grounded answer and a confident guess from the language prior look the same. A natural fix is to make the selection signal one that cannot be computed without the image. We study Perturbation Grounded Selection (Pgs), a label-free, training-free rule that scores each candidate by whether the model re-derives it under label-preserving perturbations of the input (cropping, background masking, mild photometric or geometric jitter); Pgs recovers majority voting when the perturbation set is empty. The decisive question is not whether Pgs beats chain-of-thought only majority voting, but whether the perturbation term adds anything once decoding format and budget are controlled. We therefore introduce a format-matched control (MatchedCtrl): the same short, no-CoT draws spent on the original image. Across TextVQA, MATH-Vision, MMMU, and ViLP, with a Qwen headline (three-seed means) and LLaVA-OneVision coverage in matched-budget selector tables, Pgs appears to beat plain majority voting by up to +31.8 points on TextVQA (Qwen), but MatchedCtrl tracks or exceeds Pgs within noise on every benchmark, including the vision-required ViLP; no Qwen category shows a significant gain over this control. The stability gap is real and image-dependent (up to +0.48), yet does not predict per-instance wins. The result is negative and diagnostic: perturbation consistency is at best a partial diagnostic of visual dependence and, on its own, not a usable selection signal once format is controlled; gains reported against CoT-only majority voting overstate such methods.

---

Record id: `arxiv:2608.01207`
