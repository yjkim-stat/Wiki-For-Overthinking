<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Wiener Representation Filtering for VLM Hallucination Suppression

- **Authors**: Ameen Ali, Tamim Zoabi, Lidor Brami, Lior Wolf
- **Venue**: cs.CV
- **Published**: 2026-08-08
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.08167>
- **PDF**: <https://arxiv.org/pdf/2608.08167v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Vision-language models (VLMs) excel at open-ended captioning and visual QA but often describe objects, attributes, or relations absent from the image, a phenomenon known as object hallucination. We propose a {training-free, post-hoc representation editing technique} that operates in the representation space of the language backbone. The method performs a lightweight, one-time offline calibration on a modest paired dataset to estimate the required covariance structures, using only forward passes and empirical second-order statistics with no gradient updates or fine-tuning, after which the correction is absorbed directly into the model's existing weights. By modeling hidden states as a superposition of truthful and hallucination-associated components, we derive a Wiener-type estimator whose optimal gains are given in closed form from the covariances of paired truthful and hallucinated representations. An eigendecomposition yields mode-wise attenuation that respects a stability criterion, i.e., the filter responds continuously to estimation noise. The correction is applied once to the feed-forward output projections of selected deeper layers, at inference time, the model runs unchanged and at the same speed. Experiments on LLaVA-1.5, MiniGPT-4, Gemma3, and mPLUG-Owl2 demonstrate consistent reductions in object hallucination on CHAIR, POPE, and MME while maintaining caption fluency and overall response quality. We further demonstrate the generality of our approach on the TempCompass video understanding benchmark and on discrete diffusion language models for grounded dialogue, showing that representation filtering reduces hallucinations even in temporal video reasoning and multi-step, sequence-wide denoising settings.

---

Record id: `arxiv:2608.08167`
