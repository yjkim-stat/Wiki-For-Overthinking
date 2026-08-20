<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Does Accuracy Equal Evidence? Reasoning Faithfulness under KV Cache Compression

- **Authors**: Mengting Ai, Jingrui He, Yue Guo
- **Venue**: cs.CL
- **Published**: 2026-08-03
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.01631>
- **PDF**: <https://arxiv.org/pdf/2608.01631v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-evaluation 0.25, reasoning-faithfulness 0.25, reasoning-training 0.40

## In one line

Replays one fixed reasoning trace through eleven KV cache compression methods and finds that the ones preserving final-answer accuracy are largely the ones destroying the reasoning that supports it — on AIME the accuracy ranking of compressors correlates with their chain-validity ranking at Spearman -0.95.

## Problem

KV cache compression is evaluated by final-answer accuracy, which assumes that whatever preserves the answer preserves the derivation behind it. For large reasoning models that assumption is load-bearing in a way it is not elsewhere, because the intermediate trace is what a user audits. If a compressed cache retains enough to recover the answer while losing the structure that justifies it, an accuracy-only leaderboard produces false positives — a method counted as successful although the reasoning state no longer supports the output.

## Contributions

- Names the failure mode — an answer-evidence gap — and frames it behaviourally rather than mechanistically, making no claim that KV states factorize into separate answer and justification components
- A controlled fixed-trace replay protocol: an uncompressed model generates the trace once, then every compression method is evaluated on that same prompt and text under its own compressed KV states, so differences reflect retention of information that was demonstrably present
- Three measurement axes — final accuracy, answer-chain consistency judged by an LLM auditor, and perturbation faithfulness under an injected wrong answer at three trace positions
- The finding that final accuracy is an asymmetric diagnostic: its collapse reveals damage, but its preservation does not imply preserved evidence
- Evidence that the gap is specific to token eviction rather than to memory reduction, since a quantization control that keeps every token remains close to the uncompressed model on all metrics

## Method

For each question the full-KV model produces a complete trace; the prompt and trace are then prefilled, the question's cache is protected, only the cache corresponding to the trace is compressed, and decoding resumes immediately after the closing think tag. The replayed text is identical across methods, so what varies is whether the compressed representation still makes that trace usable for constructing a valid rationale. Answer-chain consistency is measured as RWAC — a correct final answer whose reasoning is not fully correct, meaning it uses an incorrect result, applies an invalid formula, makes an unsupported transition, contradicts its own answer, or simply asserts the answer — reported both over all samples and over answer-correct samples. Perturbation faithfulness inserts a task-formatted declarative claim of a wrong answer at the start, middle or end of the trace and reports Fidelity (the answer is unchanged) and Bias Rate (the model adopts the injected error); a second variant replaces a middle reasoning block with a wrong-chain block sampled from another seed. Eleven compressors spanning recency and attention sinks, attention scoring, head- and layer-wise allocation, semantic chunking, local utility, redundancy- and reasoning-aware retention, plus a 2-bit quantization control, are run at a 256-token retained budget on Qwen3-8B with DeepSeek-R1-Distill-Llama-8B and Qwen3-30B-A3B as checks, over AIME 2024-26, GPQA-Diamond, MedCalc-Bench and RULER QA, at three seeds. The LLM judge is validated against a human auditor at 94.6% agreement, Cohen's kappa 0.89, on 400 stratified outputs, with a second judge model and a second human on a 50-output subset agreeing at 95.0% and 96.0%.

## Results

On AIME with Qwen3-8B, the uncompressed model reaches 67.4% accuracy with 4.3% of its correct answers resting on invalid chains and 92.8 fidelity. The best compressed method, SnapKV, retains 50.0% accuracy — but 65.5% of its correct answers have invalid chains and fidelity falls to 61.6. The rank correlation makes the tradeoff explicit: across compressors on AIME26, accuracy and reasoning quality correlate at Spearman -0.95, so an accuracy-based leaderboard would order methods almost exactly backwards on chain validity. Under matched conditions — same correct answer, uncompressed chain judged correct — the chain degrades in 64.8% of SnapKV cases, 63.2% for AdaKV and 60.2% for HeadKV, against 4.2% for the quantization control that evicts nothing. The failure signature shifts as well as worsening: answer-first rationalization rises from 58% of uncompressed failure cases to 94% under SnapKV. On GPQA-Diamond one method (LagKV) slightly exceeds the uncompressed model's accuracy at 57.9% while 90.2% of its correct answers carry unsupported reasoning against 42.3% uncompressed. RULER is the control condition: because the answer depends on exact distant evidence with no shortcut, compression collapses accuracy itself (78.9% to 27-64%), which the paper reads as accuracy being informative precisely where answer-recovery shortcuts are unavailable. Position matters in a way that follows each method's retention bias — sink-and-window methods make early injected claims unusually influential, while attention- and head-based methods over-preserve late conclusion-shaped tokens, so a false conclusion is retained because it is salient. Enlarging the budget from 256 to 8,192 tokens recovers accuracy first; on AIME chain validity stays degraded at every budget while fidelity recovers, and on GPQA and MedCalc chain validity returns near baseline while a fidelity gap persists.

## Limitations

The paper has no limitations section but states several bounds in place. Fixed-trace replay is a component-level diagnostic of KV retention, not a deployment benchmark: real compressed generation also changes which trace gets constructed, and end-to-end checks are run only on AIME26 and GPQA-Diamond. The 256-token budget is chosen because larger budgets make methods cluster near the uncompressed model, so the headline separations are measured at an aggressive setting the budget sweep shows is not representative of all deployments. The perturbation is described by the authors as a controlled probe of robustness to unsupported content rather than an adversarial robustness benchmark, and the injected claim is an explicit answer-like statement, which is the easiest kind for an importance-based compressor to retain. Reasoning-quality labels come from an LLM judge; the validation is unusually careful for this archive — two judge models, two human auditors, kappa 0.88 to 0.92 — but rests on one graduate-level auditor for the 400-output set and a second for only 50. The main table is a single model, with the other two relegated to an appendix.

## Why it matters here

- **reasoning-training**: The paper is about inference-time compression rather than training, and its bearing on this topic is through the reward and evaluation signal both share. It demonstrates, with an intervention nobody designed as a faithfulness test, that final-answer correctness and trace validity come apart far enough to invert a ranking: across eleven compressors on AIME26 the accuracy ordering correlates with the chain-validity ordering at Spearman -0.95. That is a direct statement about the signal outcome-supervised training optimizes -- answer correctness scores a trace whose derivation may be invalid, and here the share of correct answers resting on invalid chains rises from 4.3% to 65.5% while accuracy still reads as 74% retained. The failure signature is also the one this topic cares about: answer-first rationalization climbs from 58% to 94% of failure cases, which is what a process-supervision argument predicts an outcome-only criterion will fail to penalize. The transferable protocol is holding a trace fixed and varying only what the model can read of it, which separates whether reasoning is present from whether it is used -- a control worth having when a training method claims its traces do work.

## Entities

- **Concepts**: answer-evidence gap, [chain-of-thought faithfulness](../../../../wiki/concepts/chain-of-thought-faithfulness.md), [post-hoc rationalization](../../../../wiki/concepts/post-hoc-rationalization.md), KV cache compression, [auditability](../../../../wiki/concepts/auditability.md), perturbation faithfulness, answer-chain consistency, LLM-as-a-judge, [causal intervention](../../../../wiki/concepts/causal-intervention.md)
- **Methods**: fixed-trace replay, SnapKV, StreamingLLM, KIVI, AdaKV, HeadKV, LagKV, PyramidKV, TOVA
- **Datasets**: [AIME 2024](../../../../wiki/datasets/aime-2024.md), [AIME 2025](../../../../wiki/datasets/aime-2025.md), [AIME 2026](../../../../wiki/datasets/aime-2026.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), MedCalc-Bench, RULER

Tags: `faithfulness`, `kv cache`, `compression`, `evaluation`, `auditability`

## Abstract

KV cache compression is commonly evaluated by final-answer accuracy, implicitly assuming that preserving the answer also preserves the reasoning that supports it. We test this assumption for large reasoning models and show that it can fail: under compression, correct answers and the validity of their visible supporting rationales can be preserved at different rates. We study this failure with a controlled fixed-trace replay protocol, which holds reasoning content fixed and isolates whether compression preserves usable information from an already available trace. We evaluate ten token-eviction KV compression methods and one quantization method on three models across mathematical reasoning, scientific QA, clinical calculation, and long-context retrieval. We measure final accuracy, answer-chain consistency, and perturbation faithfulness. Across tasks, token-eviction methods can preserve competitive final-answer accuracy while substantially degrading chain support or perturbation faithfulness. We call this the answer-evidence gap. A coverage-preserving quantization control is substantially less affected, suggesting that the failure is tied less to KV memory reduction itself than to losing access to parts of the reasoning trace. Code is available at https://github.com/famous-blue-raincoat/Safe_KV_Compress.

---

Record id: `arxiv:2608.01631`
