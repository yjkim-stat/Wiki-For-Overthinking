<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# RFS-Guard: Detecting Reasoning Hallucinations via Cross-Phase Routing Focus in Large Reasoning Models

- **Authors**: Zihang Liu, Fang Zhouhua, Hui Liu, Zhiwei Liu, Yong Li, Haishuai Wang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.885/>
- **PDF**: <https://aclanthology.org/2026.acl-long.885.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.885
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

RFS-Guard detects and localizes reasoning hallucinations in LRMs training-free, using a Routing Focus Score (RFS) that measures how strongly cross-step attention between reasoning and answer phases collapses toward semantic-neighbor proximity (rather than task-critical evidence) -- finding this 'routing collapse' is a strong hallucination signal that beats sampling-based, uncertainty-based, and other self-aware baselines while remaining far more inference-efficient.

## Problem

Large reasoning models produce fluent, coherent-seeming reasoning traces and answers that nonetheless contain subtle hallucinated errors (arithmetic slips, constraint violations); existing hallucination detectors rely on external verification/ensemble sampling (computationally expensive, requiring many forward passes) or local token-level uncertainty signals (which can be misleading -- a model may assign high likelihood to a plausible continuation even after deviating from the correct path), and largely overlook whether the cross-phase information flow from reasoning to the final answer is structurally robust.

## Contributions

- an empirical finding that attention 'routing collapse' -- where cross-step attention from answer to reasoning phases follows superficial semantic proximity rather than task-critical evidentiary steps -- is a strong, statistically significant indicator of reasoning hallucination in LRMs
- the Routing Focus Score (RFS), a step-level metric quantifying this collapse by comparing attention-based and semantic-based correlation maps between reasoning and answer steps
- RFS-Guard, a training-free hallucination detection and localization framework built on RFS, incorporating a multi-hop 'reason flow' backtracking mechanism to capture non-local information dependencies
- state-of-the-art hallucination detection and localization results across multiple domains and model families, at substantially lower inference cost than sampling/ensemble-based baselines

## Method

First runs an empirical study finding that when attention routing from answer steps back to reasoning steps collapses toward simple semantic proximity (attending to reasoning steps that are merely similar-sounding, rather than to the specific evidentiary steps -- e.g. numeric quantities or stated constraints -- actually needed), this correlates strongly with hallucination: a Routing Focus Score (RFS) computed per answer step by comparing an attention-correlation map against a semantic-correlation map (cosine similarity between step-level hidden-state embeddings) is significantly higher for hallucinated steps than correct ones (Mann-Whitney U tests, R1-7B: p=1.5e-16; Qwen3-8B: p=9.7e-10). Builds RFS-Guard on this signal with three components: (1) Attention Correlation Module extracts step-level attention between reasoning and answer steps, selecting the most informative (lowest-entropy) attention heads per sample; (2) Reason Flow Module refines this into a multi-hop 'reason flow' via a backtracking mechanism that traces which earlier reasoning steps most influence each answer step (not just one-hop dependencies), calibrating the attention map to reflect this multi-hop support; (3) Routing Focus Scoring Module computes RFS as the accumulated calibrated attention mass on semantically-relevant entries (thresholded via the semantic correlation map), using the maximum RFS across answer steps as the sample-level hallucination score, and the per-step RFS for step-level localization. The whole pipeline is training-free, requiring no external tools, no repeated sampling, and no fine-tuning.

## Results

Across four open-source LRMs (DeepSeek-R1-Distill-Qwen-7B/14B, Qwen3-8B/14B) and three domains (MATH, Science, MultiHopQA), RFS-Guard achieves the best hallucination-detection performance in every setting, improving over the strongest baseline by an average 5.28%/2.74%/3.81% (AUROC-based) on MATH/Science/MultiHopQA respectively, and by 16.63%/16.72%/21.09% specifically over RACE (a reasoning-answer-consistency baseline). RFS-Guard also achieves the strongest step-level hallucination *localization* performance (Hit@1/Hit@3 overlap with ground-truth erroneous steps), outperforming adapted baselines including SelfCheckGPT (best among baselines but far less efficient, requiring multiple diverse generations), LengthScore (competitive, supporting that longer traces tend to be more error-prone, but weaker than RFS-Guard), and uncertainty-based methods (P(True), PPL, CCP), which degrade sharply at the step level -- evidence that local token-level uncertainty is dominated by linguistic variability/syntactic ambiguity rather than tracking factual correctness. RFS-Guard is markedly more inference-efficient than ensemble/sampling-based baselines (e.g. RACE), needing no additional generations, achieving favorable accuracy-efficiency tradeoffs suited to latency-sensitive deployment. Ablations show removing the Reason Flow Module (multi-hop backtracking) causes the largest performance drop (-2.5%/-4.6% average for R1-7B/Qwen3-8B), with the effect most pronounced on datasets with longer reasoning traces (up to -5.9%/-5.3% on Qwen3-8B MATH/Science, which average ~100 reasoning steps), confirming that modeling long-range, non-local information flow (not just immediate step-to-step attention) is necessary; replacing the embedding-based semantic module with alternative aggregations (last-token hidden state, external embedding models, LLM-judged semantic correlation) or attention-aggregation strategies (max/sum pooling) all cause smaller but consistent performance declines relative to the full method. A human spot-check (postgraduate annotators auditing model-judged hallucination labels) shows 86% agreement with the Qwen3-235B judge model used to construct ground truth, and 92% of 100 randomly sampled hallucinated steps stem from concrete arithmetic mistakes or explicit constraint violations, validating that the labeled hallucinations are genuine, checkable errors rather than judge-model artifacts.

## Limitations

The paper does not discuss limitations in the excerpted sections beyond what is implicit in its design: RFS relies on the model's own internal attention patterns being informative about hallucination risk, so its effectiveness could be architecture- or training-regime-dependent (validated only on DeepSeek-R1-Distill and Qwen3 model families); the semantic correlation map uses hidden-state cosine similarity as an approximation of true evidentiary relevance rather than ground-truth annotation of which reasoning steps genuinely support each answer step, which the ablation shows matters (the LLM-judged semantic-correlation variant performs somewhat differently than the default embedding-based one).

## Why it matters here

- **overthinking**: Directly relevant as a mechanistic account of reasoning-trace failure: 'routing collapse,' where a model's attention increasingly retrieves semantically-similar-but-not-evidentially-relevant reasoning content and the answer becomes a paraphrase of the ongoing trajectory rather than an independent verification, is a specific, measurable failure mode of long reasoning traces distinct from but related to overthinking's redundant-verification and unproductive-exploration patterns documented elsewhere in this archive -- and its finding that longer reasoning traces amplify the need to model multi-hop (non-local) information flow is direct evidence that trace length interacts with, and can compound, reasoning-quality failure.

## Entities

- **Concepts**: reasoning hallucination, [routing collapse](../../../../wiki/concepts/routing-collapse.md), Routing Focus Score (RFS), cross-phase attention correlation, reason flow (multi-hop backtracking), self-confirmation loop
- **Methods**: RFS-Guard (Routing Focus Score + Reason Flow), SelfCheckGPT (baseline), SINdex (baseline), RACE (baseline), P(True)/LNPE/PPL/CCP (uncertainty baselines), EigenScore/AttentionScore/UQAC/RHD (self-aware baselines), LengthScore (rule-based baseline)
- **Datasets**: [MATH500](../../../../wiki/datasets/math500.md), [AIME25](../../../../wiki/datasets/aime-2025.md), minervamath, MATH (composite domain), Science (domain), MultiHopQA (domain)

Tags: `hallucination-detection`, `mechanistic-interpretability`, `attention-analysis`, `training-free`, `reasoning-trace-analysis`

## Abstract

Large reasoning models (LRMs) achieve strong performance on complex tasks by generating intermediate reasoning before the final answer, yet they remain prone to reasoning hallucinations such as subtle arithmetic or constraint-violation errors. Prior hallucination detectors often rely on external verification or local token-level signals, which are limited for LRMs and largely overlook whether the cross-phase information flow from reasoning to answering is structurally robust. We propose Routing Focus Score (RFS), a step-level indicator that measures how strongly cross-step attention routing aligns with semantic proximity derived from hidden-state cosine similarity. We further design RFS-Guard, a lightweight hallucination detection framework based on RFS. Empirically, we observe that higher reasoning–answer RFS is consistently associated with higher hallucination risk, suggesting a routing-collapse failure mode where models might prefer self-confirmation loops and suppress the ability to audit their own generations. Experimental results across multiple domains and models demonstrate the superiority of RFS-Guard for detecting and localizing hallucinations in LRMs without requiring external tools or repeated sampling.

---

Record id: `doi:10.18653/v1/2026.acl-long.885`
