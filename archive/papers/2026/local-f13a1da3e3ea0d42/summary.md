<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# The First Impression Problem: Internal Bias Triggers Overthinking in Reasoning Models

- **Authors**: Renfei Dang, Zhening Li, Shujian Huang, Jiajun Chen
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: local
- **Topics**: overthinking

## In one line

Identifies a reasoning model's implicit, pre-reasoning guess about the answer ('internal bias') as a causal driver of overthinking, showing that when this guess conflicts with the model's derived answer it triggers excessive reflection, and that existing overthinking-mitigation methods fail to remove this influence.

## Problem

Reasoning models are known to overthink -- generating redundant reflective steps even after reaching a correct answer -- but what specifically triggers this behavior, as opposed to just how to shorten the resulting chains, was underexplored; the paper asks what drives a reasoning model's tendency to keep reflecting.

## Contributions

- Identifies internal bias -- a model's implicit pre-reasoning guess about the answer -- as a key driver of overthinking, and validates its influence across model families (DeepSeek-R1, QwQ-32B, R1-Distill-Qwen-14B), model sizes (14B/32B/671B), tasks (character counting, logical reasoning, math), and languages (English/Chinese): the accuracy of the model's direct (no-reasoning) answer is low, and reasoning length is 21.0-42.1% higher (R_delta) for questions with high bias-deviation degree than for low-deviation ones.
- Demonstrates the causal link via two counterfactual interventions: removing the input question from the context right after the model's first reasoning-derived answer reduces subsequent reasoning length by 31.1-53.5% (r) across CharCount, KnowLogic, AIME 2024 and AIME 2025, while maintaining or improving accuracy; and fine-tuning to inject wrong beliefs increases reasoning length (355.5 to 454.9 tokens) while injecting correct beliefs decreases it (600.8 to 412.1 tokens).
- Shows via attention analysis that when the model is about to emit a reflection token, its attention to the question segment increases to more than four times its level during normal answer generation, particularly in middle-to-later layers, suggesting re-reading the question reactivates the internal bias and triggers further reflection.
- Tests existing overthinking-mitigation methods (FCS-SFT, FCS-DPO, SEAL, PROBE) on CharCount and AIME 2024 and finds they shorten reasoning length (R_delta reduced to 26.7-46.3% on CharCount, versus 15.2% for the simple question-removal baseline) but do not eliminate -- and sometimes worsen -- the underlying influence of internal bias, and that on the harder AIME 2024 task the best CharCount method (FCS-SFT) drops accuracy from 63.3% to 50.0%.

## Method

The paper defines a model's 'internal bias' a_bias = f(q; theta) as the preliminary guess it forms about an answer without deliberate reasoning, elicited via a 'Direct Answer' probe: a no-reasoning prompt template ending in the special </think> token forces the model to output whatever guess it had formed before doing any reasoning. Because this guess can vary with sampling, the paper approximates it as a distribution by collecting 64 direct answers per question under varied templates, and quantifies how far this distribution deviates from the model's actual final reasoned answer as a 'bias deviation degree' D_bias (mean absolute error for numerical-answer tasks, inconsistency rate for categorical/multiple-choice tasks). To establish causality rather than mere correlation, two counterfactual interventions are run on DeepSeek-R1-Distill-Qwen-14B: (1) Question removal (an inference-time, training-free manipulation): once the model generates its first complete answer within an ongoing reasoning trace (detected via the position P_first), the input question is deleted from the context/prompt and the model is forced to continue generating using only its own prior reasoning trajectory, preventing internal bias from being reactivated by re-reading the question; length reduction is measured via r = (L_ori - L_rem)/(L_ori - P_first). (2) Bias injection (a training-time intervention): the model is fine-tuned per-sample on 50 rephrased declarative statements asserting either a wrong answer (for samples with low original bias deviation, 'Low2Wrong') or a correct answer (for samples with high original bias deviation, 'High2Correct'), with random-statement controls, to see whether deliberately shifting internal bias changes subsequent overthinking. Separately, an attention-based interpretability analysis computes a position-normalized attention score to the question tokens versus mid-result tokens versus other tokens at each generation step, to test whether the model re-attends to the question when deciding whether to reflect. Finally, the paper evaluates -- but does not itself propose -- existing overthinking-mitigation techniques as a check on whether they eliminate internal bias's influence: two training-time methods (FCS with SFT or DPO, which fine-tunes on short correct reasoning traces) and two existing inference-time methods (SEAL, which steers hidden states during decoding, and PROBE, which probes internal representations to decide when to stop early).

## Results

On CharCount (zh)/KnowLogic/AIME 2024, direct-answer accuracy is far below reasoned accuracy (e.g. DeepSeek-R1: 99.2% reasoned vs 55.8% direct on CharCount zh; 76.7% vs 3.3% on AIME 2024), and reasoning length for the high-bias-deviation half of questions exceeds the low-deviation half by 21.0-43.1% (R_delta) across models and datasets. Question-removal intervention on R1-Distill-Qwen-14B reduces reasoning length by a ratio r of 31.1% (CharCount en) to 53.5% (AIME 2024), with accuracy roughly maintained or improved on complex tasks (e.g. AIME 2024: 63.3% to 66.7%; AIME 2025: 36.7% to 46.7%) and slightly reduced on simpler ones (CharCount en: 93.8% to 93.2%). Bias injection on 500 lowest- and 500 highest-deviation CharCount(zh) samples: injecting wrong beliefs (Low2Wrong) raises length from a random-control 355.5 to 454.9 tokens while injecting correct beliefs (High2Correct) lowers length from a random-control 600.8 to 412.1 tokens, with corresponding accuracy shifts (89.5%->83.4% and 67.0%->76.6%). Attention analysis (layers 21-30) shows question-token attention rises from a low background level to more than 4x higher at reflection points relative to non-reflection points. Mitigation trials on CharCount reduce R_delta to 26.7-46.3% (versus 31.5% for the plain question-removal reference) and raise accuracy to 76.7-78.9%, but the best-performing method transferred to AIME 2024 (FCS-SFT) drops accuracy from the Qwen-14B baseline of 63.3% to 50.0%, indicating shortened traces can come at the cost of reasoning capability on harder problems.

## Limitations

All analyses are restricted to tasks with outputs that are explicit numerical values, ranges, or multiple-choice options; the authors state internal bias is not yet well-defined for open-ended tasks, where it may manifest in more complex forms. The reflection-keyword counting used to estimate the number of reflections is a rough proxy rather than a verified measure of genuine re-evaluation. The question-removal intervention is coarse-grained (it deletes the entire question at one detected position) and the paper notes this coarseness likely explains the slight accuracy drop it causes on simpler tasks. The paper does not report the inference-time compute or latency cost of its own causal interventions (question removal, or the attention-based early-exit idea explored only preliminarily in an appendix); it also does not propose a deployable inference-time mitigation of its own, evaluating existing methods (SEAL, PROBE, FCS) instead. The bias-injection intervention is a training-time fine-tuning procedure, not an inference-time technique, despite being used to probe the same causal question.

## Why it matters here

- **overthinking**: Proposes and causally validates a specific trigger for overthinking (a preliminary, pre-reasoning 'internal bias' that conflicts with the model's derived answer), and shows that an inference-time context intervention (removing the question after a first answer is reached) reduces redundant reasoning by 31-54%, while also showing existing inference-time and training-time mitigation methods fail to remove the bias's influence.

## Entities

- **Concepts**: internal bias, first impression problem, [overthinking](../../../../wiki/concepts/overthinking.md), bias deviation degree, parroting behavior, attention reactivation of bias
- **Methods**: internal bias measurement (Direct Answer probing), bias deviation degree, question-removal counterfactual intervention, bias injection via fine-tuning, attention-based interpretability analysis, FCS (SFT/DPO), [SEAL](../../../../wiki/methods/seal.md), PROBE
- **Datasets**: CharCount (en), CharCount (zh), KnowLogic, [AIME 2024](../../../../wiki/datasets/aime-2024.md), [AIME 2025](../../../../wiki/datasets/aime-2025.md)

Tags: `overthinking`, `internal-bias`, `reflection`, `attention-analysis`, `counterfactual-intervention`, `reasoning-length`, `interpretability`

## Abstract

Reasoning models often exhibit overthinking, characterized by redundant reasoning steps. We identify internal bias elicited by the input question as a key trigger of such behavior. Upon encountering a problem, the model immediately forms a preliminary guess about the answer, which we term an internal bias since it may not be explicitly generated, and it arises without systematic reasoning. When this guess conflicts with its subsequent reasoning, the model tends to engage in excessive reflection, resulting in wasted computation. We validate the association between internal bias and overthinking across multiple models and diverse reasoning tasks. To demonstrate the causal relationship more rigorously, we conduct two counterfactual interventions, showing that removing the input question after the model derives an answer reduces the redundant reasoning across various complex reasoning tasks, and manually injecting bias affects overthinking accordingly. Further interpretability experiments suggest that excessive attention to the input question serves as a key mechanism through which internal bias influences subsequent reasoning trajectories. Finally, we evaluated several methods aimed at mitigating overthinking, yet the influence of internal bias persisted under all conditions.

---

Record id: `local:f13a1da3e3ea0d42`
