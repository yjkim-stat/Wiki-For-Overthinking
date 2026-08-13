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

## In one line

Shows that a perturbation-based selection rule's apparent 31.8-point gain over majority voting in vision-language test-time scaling is a decoding-format effect, by adding a control that spends the same short-answer budget on the unperturbed image and finds it matches or beats the perturbation rule everywhere.

## Problem

Test-time scaling needs a selection signal, and in vision-language models the usual ones fail for a specific reason: neither answer frequency nor verbalized confidence tests whether an answer depends on the pixels, so a grounded answer and a confident language-prior guess look identical at the selection layer. The natural fix is a signal that cannot be computed without the image. But the obvious way to evaluate such a fix is unfair by construction: a perturbation-based rule spends its extra draws as short, no-CoT samples while the majority-voting baseline aggregates only long CoT samples, so any gain mixes the intended mechanism with a change of decoding format.

## Contributions

- Names the confound: comparing a perturbation- or consistency-based selector against CoT-only majority voting conflates the selection mechanism with a CoT-to-short decoding-format change
- MatchedCtrl, a format-matched control that reuses the N CoT answers and adds the same M*K short no-CoT answers drawn from the original unperturbed image, so it differs from the perturbation rule only in whether those short draws pass through perturbed views
- A negative result under that control across four benchmarks and two open VLMs, with no category showing a significant positive difference and every 95% bootstrap interval overlapping zero
- A separation of diagnostic from routing: the perturbation score demonstrably sees the image, and that fact still does not predict when the rule beats the control
- Released audit tooling — the score, the stability gap and paired bootstrap intervals — so the format-matched comparison can be reapplied to other selection claims

## Method

Perturbation-Grounded Selection scores each candidate answer by its original-view vote count plus lambda times its re-derivation support under M label-preserving image edits (crops toward question-relevant regions, background masking, mild photometric or geometric jitter), with support estimated by drawing K short answers per perturbed view and counting how often each candidate is re-derived; majority voting is the empty-perturbation case at lambda = 0, so the rule is a strict generalization rather than a competitor. Three selectors are compared at a fixed generation budget of N + M*K = 32: MV over N CoT samples only, PGS, and MatchedCtrl. Two diagnostics separate the roles the perturbation channel might play: StabilityGap, the paired preserve-minus-destroy support gap under label-destroying crops, and BlankAblation, which blanks the perturbation inputs entirely; and one routing test asks whether a larger per-instance gap predicts a larger per-instance win over MatchedCtrl. Settings are N = 8, M = 6, K = 4, lambda = 2 fixed for the protocol, on a single RTX 4090, with Qwen2.5-VL-7B-Instruct as the headline model and LLaVA-OneVision-7B in the matched-budget selector tables, over TextVQA, MATH-Vision, MMMU and ViLP — the last pairing a language-prior-aligned answer with a vision-required one per question.

## Results

On Qwen2.5-VL-7B over three seeds, PGS appears to beat MV by 31.8 points on TextVQA (86.2 against 54.4) and is near-flat elsewhere. MatchedCtrl tracks or exceeds it on every benchmark: TextVQA 87.6 against 86.2, MATH-Vision 25.3 against 26.0, MMMU 50.1 against 50.3, ViLP 53.7 against 52.3 — with the control ahead on the benchmark where the headline gain was largest. Per-category bootstrap intervals close the case: no category yields a significant positive difference and the ViLP interval lies entirely below zero. Against a panel of label-free alternatives at matched budgets of 32 and 16 on both models, self-certainty and mean token entropy often fall below MatchedCtrl while SC+Borda and confidence-weighted self-consistency track it within noise, so the control absorbs the strongest confidence aggregators too. The diagnostics behave differently from the selector: blanking the perturbation inputs collapses PGS where the signal is visual — TextVQA 87.7 to 7.9, ViLP-F 46.2 to 0.4, MMMU 50.2 to 23.3 — while symbolic MATH-Vision barely moves (26.3 to 23.4), confirming the score genuinely depends on the image. The preserve/destroy gap is real and image-dependent, reaching +0.478 on TextVQA and +0.445 on ViLP, yet instance-level correlation between gap and gain is near zero and gap quartiles are non-monotone. The two diagnostics also decouple from each other: MMMU collapses under blanking while its mean stability gap is only +0.071.

## Limitations

The paper states its bounds directly. The grid is two open 7B VLMs and four automatically scored benchmarks, so a stronger model family or a larger decode budget could in principle show a benefit this does not; universality is not claimed. Main results are three-seed means, which cannot rule out rarer decoding regimes, though the paired PGS-vs-MatchedCtrl comparisons carry instance-level bootstrap intervals. The perturbation families are hand-designed heuristics and a learned set could carry more signal — but the authors note it would still have to clear a MatchedCtrl-style control. No stronger-signal reference point is included: they do not show that a trained verifier or a multi-model ensemble beats MatchedCtrl, so whether the gap is recoverable under training is untested. And the negative finding is about answer selection specifically; the stability gap survives as a partial diagnostic of visual dependence, and abstention and routing uses of it are not evaluated.

## Why it matters here

- **test-time-scaling**: It supplies a control that most test-time-scaling comparisons in this archive do not run. Any selection rule that spends its extra draws in a different decoding format than the baseline it is compared against — short answers against long chains — is measuring two things at once, and here that confound is worth up to 31.8 points, larger than almost any selection gain reported anywhere. The practical hurdle it establishes is also cheap: short-answer aggregation on the original image at matched budget is a strong baseline that both confidence-style and perturbation-weighted selectors failed to clear. It also sharpens what a grounding claim has to show, by exhibiting a signal that provably tracks the pixels (blanking it collapses accuracy from 87.7 to 7.9) and still buys nothing at the selection layer.

## Entities

- **Concepts**: test-time scaling, [selection signal](../../../../wiki/concepts/selection-signal.md), decoding format, majority voting, self-consistency, [visual grounding](../../../../wiki/concepts/visual-grounding.md), label-preserving perturbation, [matched-budget comparison](../../../../wiki/concepts/matched-budget-comparison.md), confound control, generation-verification gap
- **Methods**: Perturbation-Grounded Selection, MatchedCtrl, [best-of-N](../../../../wiki/methods/best-of-n.md), confidence-weighted self-consistency, [Borda count](../../../../wiki/methods/borda-count.md), [paired bootstrap confidence intervals](../../../../wiki/methods/paired-bootstrap-confidence-intervals.md)
- **Datasets**: TextVQA, [MATH-Vision](../../../../wiki/datasets/mathvision.md), MMMU, ViLP

Tags: `vision-language`, `test-time scaling`, `selection`, `negative result`, `experimental control`

## Abstract

Test-time scaling lifts large language model reasoning by sampling many candidate solutions and selecting among them, yet the same recipe transfers poorly to vision-language models (VLMs): recent work shows that simple majority voting beats selection methods built on the model's own self-verification, apparently because at the selection layer an image-grounded answer and a confident guess from the language prior look the same. A natural fix is to make the selection signal one that cannot be computed without the image. We study Perturbation Grounded Selection (Pgs), a label-free, training-free rule that scores each candidate by whether the model re-derives it under label-preserving perturbations of the input (cropping, background masking, mild photometric or geometric jitter); Pgs recovers majority voting when the perturbation set is empty. The decisive question is not whether Pgs beats chain-of-thought only majority voting, but whether the perturbation term adds anything once decoding format and budget are controlled. We therefore introduce a format-matched control (MatchedCtrl): the same short, no-CoT draws spent on the original image. Across TextVQA, MATH-Vision, MMMU, and ViLP, with a Qwen headline (three-seed means) and LLaVA-OneVision coverage in matched-budget selector tables, Pgs appears to beat plain majority voting by up to +31.8 points on TextVQA (Qwen), but MatchedCtrl tracks or exceeds Pgs within noise on every benchmark, including the vision-required ViLP; no Qwen category shows a significant gain over this control. The stability gap is real and image-dependent (up to +0.48), yet does not predict per-instance wins. The result is negative and diagnostic: perturbation consistency is at best a partial diagnostic of visual dependence and, on its own, not a usable selection signal once format is controlled; gains reported against CoT-only majority voting overstate such methods.

---

Record id: `arxiv:2608.01207`
