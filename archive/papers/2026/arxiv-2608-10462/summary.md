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

## In one line

Calibrates feature-based data-contamination detectors against the systematic feature shifts that post-training introduces, by measuring how controlled prompt variants move scores on known non-members and then correcting only the recurring shift directions, with the gains concentrated at the low-false-positive operating point rather than in AUC.

## Problem

Data contamination detection asks whether a given text was in a model's pre-training corpus, and the strongest current methods are feature-based: derive membership features from the input text and the model's output, then train a classifier to separate members from non-members. That paradigm inherits a vulnerability. Modern models are post-trained by instruction tuning, preference optimization and reasoning-oriented training, all of which change the style, length, structure and content of generated output, which shifts the resulting membership features and reduces the separation between members and non-members. Detectors built before that shift degrade against models that have undergone it.

## Contributions

- A calibration framework applicable to existing feature-based contamination detectors rather than a replacement detector, so the post-training shift is corrected without retraining or redesigning the detector.
- Multi-View Shift Detection: evaluating controlled prompt variants on known non-members, prioritising views by the false-positive pressure they induce, and taking a cross-view consensus to isolate recurring shift directions from view-specific noise.
- Bounded Feature Correction: adjusting only the components aligned with detected shifts, with score-sensitive weights and an adaptively selected correction extent below full, on the argument that over-correction removes detection signal along with shift.
- An ablation set showing that the consensus step carries the most AUC and single-view restriction costs the most at the low-false-positive operating point, with the complete method ahead in 23 or 24 of 24 settings on every comparison.
- An explicit statement that the corrected shifts are identified by association with elevated non-member scores rather than shown to be caused by post-training.

## Method

CalibDCD is a calibration wrapper rather than a new detector, applied on top of existing feature-based methods in the standard black-box setting where the detector may query the model and read its outputs but has no access to parameters or internals. It has two stages. Multi-View Shift Detection evaluates a set of controlled prompt variants -- eight universal views plus two model-specific ones -- on texts known to be non-members, scores each view by the false-positive pressure it produces, prioritises the most informative, and takes a cross-view consensus so that recurring shift directions are retained while view-specific idiosyncrasies are dropped. Bounded Feature Correction then adjusts only the feature components aligned with those detected directions, with score-sensitive rather than binary weights and a correction extent below full so that useful detection information is preserved; the correction strength is selected adaptively per setting rather than fixed. Evaluation covers two feature-based detectors across four contamination benchmarks and three target model families, reporting both AUC and true positive rate at 5 percent false positive rate, with ablations that replace view prioritisation with random selection, restrict to the single best view, remove the consensus step, replace the weighting with binary, and force full correction on the eighteen settings where the adaptive rule chose less.

## Results

The improvement is real but its size depends entirely on which metric is read, and the two diverge sharply. AUC gains are small: averaged by model, 2.4 percent for Qwen, 1.7 for Llama, 2.3 for DeepSeek, with the largest benchmark-level average of 4.0 on BookMIA, and per-cell movements typically of one to three points (the strongest detector goes from 88.8 to 91.7 on one cell, 78.5 to 84.0 on another). At the 5 percent false-positive operating point the same corrections are worth several times more: the stronger detector moves from 53.6 to 68.6 on BookTection with Qwen, 45.3 to 58.0 with DeepSeek, 41.5 to 49.8 on BookMIA, and 74.8 to 81.6 on WikiMIA, while the weaker detector roughly doubles on several cells (15.3 to 26.0, 20.2 to 32.2, 6.6 to 15.5). Since AUC integrates over all thresholds and contamination detection is used at a low false-positive threshold, the second set is the operationally relevant one and the first understates the method. Every ablation degrades both metrics in essentially every setting, and the ordering is informative: removing cross-view consensus costs the most AUC (1.3 points, worse in all 24 settings), while restricting to the single best view costs the most at the operating point (4.2 points of TPR, worse in all 24). Replacing informed view prioritisation with three random views costs only 0.6 AUC and 3.1 TPR, so most of the benefit comes from combining several views at all rather than from choosing them well. Forcing full correction where the adaptive rule chose partial costs 0.9 AUC and 2.6 TPR across those eighteen settings, confirming that over-correcting removes signal along with shift. The weaker of the two detectors starts near chance on several cells (53.5, 54.3, 57.0 AUC), so its improvements are improvements on a detector that was barely discriminating.

## Limitations

Stated, and the most important one is a disclaimer about the paper's own framing: the method corrects score-increasing feature shifts observed on known non-members, and while post-training motivates the study, those shifts may equally reflect dataset artifacts, decoding behaviour or the feature extractor -- so what is identified is a shift associated with higher non-member scores during calibration, not a shift proved to be caused by post-training. The method also requires a pool of known non-members held outside the supervised classifier's training, which temporal benchmarks and post-cutoff data supply but which is hard to obtain when a model's cutoff is unknown or no trusted non-member pool exists; and the calibration examples remain in the reporting pool under their protocol. Not stated but worth noticing: the AUC improvements are one to four points, which on four benchmarks and three model families with no confidence intervals or repeated runs reported is a thin margin, and the large TPR movements are measured at a single operating point on benchmarks whose positive sets are small. The three target models are described only by family, so what specific post-training each underwent -- the variable the whole framing rests on -- is not controlled or varied, and no experiment compares a base model against its own post-trained descendant, which is the comparison that would establish the causal claim the method is named for.

## Why it matters here

- **reasoning-evaluation**: Two things here bear on this topic beyond the specific method. The first is a metric lesson the paper demonstrates cleanly without drawing attention to it: the same corrections are worth one to four points of AUC and five to fifteen points of true positive rate at a 5 percent false-positive threshold. AUC integrates over thresholds nobody uses, and a contamination detector is deployed at a low false-positive setting, so a paper reporting only AUC would have looked like it had a marginal result and one reporting only TPR would have looked like it had transformed the field. Both tables belong together, and the archive should ask for the operating point wherever a detector's use has an asymmetric cost. The second is what the paper establishes about the fragility of contamination detection generally, which matters because the archive already holds that a brief round of GRPO erases the signals contamination detectors rely on and that similarity-based decontamination has no principled threshold. This adds a third mechanism: ordinary post-training moves the features these detectors read, in directions consistent enough across prompt variants to be measured and corrected. Taken together, the detection side of contamination looks less like a solved measurement and more like something that must be recalibrated per model. The paper's own honesty is the caution to carry when citing it. It declines to claim the shifts it corrects are caused by post-training -- they may be dataset artifacts, decoding behaviour or the feature extractor -- and it runs no experiment comparing a base model against its own post-trained descendant, which is the comparison the framing implies. Note too that the weaker of its two detectors sits near chance on several cells before calibration, so improvements there are improvements to something that was not discriminating.

## Entities

- **Concepts**: [data contamination](../../../../wiki/concepts/benchmark-contamination.md), membership inference, [distribution shift](../../../../wiki/concepts/distribution-shift.md), [calibration](../../../../wiki/concepts/calibration.md), post-training, false positive rate, [operating point](../../../../wiki/concepts/operating-point.md), benchmark integrity, decontamination
- **Methods**: [membership inference](../../../../wiki/methods/membership-inference.md), data contamination detection, feature calibration, prompt variation, consensus filtering, supervised classification, [ROC analysis](../../../../wiki/methods/roc-analysis.md), [ablation](../../../../wiki/methods/ablation.md)
- **Datasets**: BookTection, BookMIA, ArxivTection, WikiMIA

Tags: `contamination-detection`, `membership-inference`, `calibration`, `post-training`, `evaluation-integrity`

## Abstract

Large language models (LLMs) are trained on massive and largely undisclosed corpora that may contain copyrighted or privacy-sensitive content. Data contamination detection (DCD) therefore aims to determine whether a given text is a member of the pre-training corpus of a target LLM. Recent state-of-the-art DCD methods follow a feature-based paradigm that derives membership features from the input text and the corresponding model output. However, most modern LLMs undergo post-training, such as instruction tuning, preference optimization, and reasoning-oriented training, which can alter model outputs and shift the corresponding membership features, thereby reducing the separability between members and non-members. To address this problem, we propose CalibDCD, a broadly applicable calibration framework for feature-based DCD methods, comprising (1) Multi-View Shift Detection, which identifies recurring feature shifts associated with post-training, and (2) Bounded Feature Correction, which selectively mitigates their influence on membership prediction. Specifically, Multi-View Shift Detection evaluates controlled prompt variants on known non-member texts and consolidates the most informative views to identify recurring feature shifts. Bounded Feature Correction selectively adjusts feature components aligned with the detected shifts and controls the correction extent to preserve useful detection information. Experiments show that CalibDCD consistently improves existing feature-based detectors, with gains of up to 7.0% in AUC and 15.0% in TPR@5%FPR.

---

Record id: `arxiv:2608.10462`
