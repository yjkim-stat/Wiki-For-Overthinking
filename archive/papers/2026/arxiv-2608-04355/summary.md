<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# The Calibration Floor: Format Repair Can Masquerade as Self-Correction at Small-to-Mid Scale

- **Authors**: Mingguang Chen, Bo Qu, Licheng Wang
- **Venue**: cs.CL
- **Published**: 2026-08-05
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.04355>
- **PDF**: <https://arxiv.org/pdf/2608.04355v1>
- **Topics**: test-time-scaling
- **Relevance score**: test-time-scaling 0.50

## In one line

Decomposes measured self-correction gains into a content margin and format-recovery margins, and shows causally that most of what the field has reported as self-correction is answer-parseability repair.

## Problem

Accuracy changes after self-revision are read as changes in reasoning. That reading fails at the answer-extraction boundary: a revision can turn an unparseable output into a parseable one without changing any reasoning, and the standard total-effect measurement cannot tell the two apart.

## Contributions

- A decomposition of the self-revision accuracy shift into content and format-recovery/loss margins
- A causal test of the decomposition using grammar-constrained decoding over already-generated reasoning
- Evidence that format effects dominate content effects, and intensify with scale in the frontier arm
- A failed verbatim replication of a published confidence-gating self-correction gain
- A released instrument, code and derived results

## Method

The always-revise accuracy shift is decomposed into a content margin (both the pre- and post-revision answers parse) and format-recovery/format-loss margins (parseability itself changes). The causal test forces already-generated reasoning through grammar-constrained decoding so that every answer parses by construction; the remaining gap between the naive total effect and the content-margin estimate is then attributable to format. A clustered model compares floor-scale against capable-scale models. A previously published confidence-gating protocol is replicated verbatim as a check.

## Results

Across 29 primary cells plus a frontier arm on Qwen3.5 (0.8B-9B), Gemma-4-12B, Tencent Hy3 and Nvidia Nemotron-3-Ultra-550B. On the 12 cells with meaningful unparseable-answer rates, format effects exceed content effects (Wilcoxon p=1.7e-3). Grammar-constrained decoding closes a median 71% of the naive-versus-content gap across 14 cells, with two cells converging exactly; the residual on the two largest-effect cells is reported rather than dismissed. Floor-scale models (0.8B/2B) have far higher odds of content-level change and of harm than capable-scale models (p<1e-7). In the frontier arm the content margin is exactly zero in all 5 cells despite total effects up to +0.275, though that arm is lower-powered. Replicating the cited confidence-gating protocol on Qwen3.5 does not reproduce its reported gain and shows the same near-zero content margin. Only one cell is marginally viable under the calibration-floor criterion, with negligible sealed-holdout gain.

## Limitations

The frontier arm is stated to be lower-powered. Two large-effect cells retain an unexplained residual after grammar-constrained decoding. The calibration-floor argument identifies a squeeze rather than a remedy: floor-scale models have headroom but not enough signal, capable-scale models have signal but little headroom, so the design space where self-correction could be measured cleanly is nearly empty. Scope is answer-extractable tasks; the decomposition does not apply where there is no parseable answer field.

## Why it matters here

- **test-time-scaling**: Directly attacks the measurement that most test-time self-correction results rest on. If the content margin is zero in all five frontier cells while total effects reach +0.275, then reported self-correction gains at scale are answer-formatting artefacts, and any test-time method whose evidence is a revise-then-remeasure accuracy delta needs re-auditing with parseability held fixed. It also names a concrete instrument for doing so — grammar-constrained decoding of already-generated reasoning — which is cheap enough to be a standard control.

## Entities

- **Concepts**: [self-correction](../../../../wiki/concepts/self-correction.md), [answer extraction](../../../../wiki/concepts/answer-extraction.md), [calibration](../../../../wiki/concepts/calibration.md), [construct validity](../../../../wiki/concepts/construct-validity.md), format repair, measurement validity, [inverse scaling](../../../../wiki/concepts/inverse-scaling.md)
- **Methods**: grammar-constrained decoding, content-margin decomposition, Wilcoxon signed-rank test, clustered regression, sealed holdout evaluation
- **Datasets**: _none recorded_

Tags: `self-correction`, `evaluation artefact`, `grammar-constrained decoding`, `causal test`, `replication failure`

## Abstract

Accuracy changes after language-model self-revision are usually interpreted as changes in reasoning. We show this can fail at the answer-extraction boundary, and test the failure causally rather than only observationally. Across Qwen3.5 (0.8B-9B), Gemma-4-12B, and two frontier models via API (Tencent Hy3, Nvidia Nemotron-3-Ultra-550B) in 29 primary cells plus a frontier arm, we decompose the always-revise accuracy shift into a content margin (both answers parseable) and format-recovery/loss margins (parseability changes). On 12 cells with meaningful unparseable-answer rates, format effects exceed content effects (Wilcoxon p=1.7e-3). To test this causally, we force already-generated reasoning through grammar-constrained decoding so every answer is parseable by construction: across 14 cells this closes a median 71% of the gap between the naive total effect and the content-margin estimate, with two cells converging exactly and a residual on the two largest-effect cells reported rather than dismissed. A clustered model confirms floor-scale (0.8B/2B) models have far higher odds of content-level change and harm than capable-scale models (p<1e-7). Replicating a cited confidence-gating protocol verbatim on Qwen3.5 does not reproduce its reported gain and shows the same near-zero content margin. A frontier check on much larger models shows format-dominance intensifying with scale: content margin is exactly zero in all 5 cells despite total effects up to +0.275, though this arm is lower-powered. The calibration-floor criterion on the content margin reveals a squeeze: floor-scale cells have headroom but insufficient signal, capable-scale cells have signal but little headroom; only one cell is marginally viable, with negligible sealed-holdout gain. Content is a minority share of what the field has measured as self-correction. We release the instrument, code, and derived results.

---

Record id: `arxiv:2608.04355`
