<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Calibrating Post-Training Feature Shifts for LLM Data Contamination Detection

- **Authors**: Zhen Yang, Mengqi Wang, Gengda Zhao, Mo Zhou, Jianwei Wang, Wenjie Zhang
- **Venue**: cs.CL
- **Published**: 2026-08-11
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.10462>
- **PDF**: <https://arxiv.org/pdf/2608.10462v1>
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large language models (LLMs) are trained on massive and largely undisclosed corpora that may contain copyrighted or privacy-sensitive content. Data contamination detection (DCD) therefore aims to determine whether a given text is a member of the pre-training corpus of a target LLM. Recent state-of-the-art DCD methods follow a feature-based paradigm that derives membership features from the input text and the corresponding model output. However, most modern LLMs undergo post-training, such as instruction tuning, preference optimization, and reasoning-oriented training, which can alter model outputs and shift the corresponding membership features, thereby reducing the separability between members and non-members. To address this problem, we propose CalibDCD, a broadly applicable calibration framework for feature-based DCD methods, comprising (1) Multi-View Shift Detection, which identifies recurring feature shifts associated with post-training, and (2) Bounded Feature Correction, which selectively mitigates their influence on membership prediction. Specifically, Multi-View Shift Detection evaluates controlled prompt variants on known non-member texts and consolidates the most informative views to identify recurring feature shifts. Bounded Feature Correction selectively adjusts feature components aligned with the detected shifts and controls the correction extent to preserve useful detection information. Experiments show that CalibDCD consistently improves existing feature-based detectors, with gains of up to 7.0% in AUC and 15.0% in TPR@5%FPR.

---

Record id: `arxiv:2608.10462`
