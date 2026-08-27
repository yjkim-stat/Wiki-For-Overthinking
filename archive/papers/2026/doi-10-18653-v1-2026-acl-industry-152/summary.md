<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# CAT: Confidence-Adaptive Thinking for Efficient Reasoning of Large Reasoning Models

- **Authors**: Qizhi Jiang, Shuo Wang, Pei Ke, Yuhang Song, Ke Qin
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-industry.152/>
- **PDF**: <https://aclanthology.org/2026.acl-industry.152.pdf>
- **DOI**: 10.18653/v1/2026.acl-industry.152
- **Topics**: overthinking
- **Relevance score**: overthinking 0.79

## In one line

CAT (Confidence-Adaptive Thinking) uses self-certainty -- the KL divergence of a reasoning trajectory's per-token predictive distribution from uniform, an intrinsic model signal requiring no external labels -- to build preference pairs and a confidence-weighted preference-optimization loss (CWPO) that compresses reasoning on problems the model is confident about while preserving deliberation on uncertain ones, beating three efficient-reasoning baselines (OverThink, DAST, ConCISE) on accuracy-at-compression across three LRMs and three benchmarks.

## Problem

Large reasoning models overthink simple queries, producing redundant self-reflection and excessive token overhead, and existing efficient-reasoning methods either apply uniform length reduction (hurting hard-problem accuracy, since difficult tasks genuinely need long reasoning) or rely on coarse-grained difficulty estimation using only the correctness of a model's final answer -- external labels that assess just the output, not the quality of the whole reasoning chain that produced it.

## Contributions

- identification of self-certainty (an intrinsic, ground-truth-independent, token-distribution-based confidence signal) as a fine-grained indicator of reasoning-trajectory quality, shown empirically to separate correct from incorrect trajectories and to be robust to response length
- Confidence-Aware Preference Labeling (CAPL), constructing Conciseness Pairs and Deliberation Pairs whose preference strength combines a length/correctness margin with a self-certainty margin, with dynamic pruning to prioritize informative supervision
- Confidence-Weighted Preference Optimization (CWPO), the first method (per the authors) to incorporate intrinsic self-certainty directly into the preference-optimization loss landscape, dynamically scaling winning/losing-trajectory weights instead of applying a uniform length penalty
- state-of-the-art accuracy-at-compression results across three LRMs (DeepSeek-R1-Distill-Qwen-7B/1.5B, Qwen3-8B) and three benchmarks (MATH-500, AIME24, GPQA) versus three efficient-reasoning baselines (OverThink, DAST, ConCISE), plus a demonstrated generalization of the CWPO idea to a DPO backbone

## Method

CAT has two stages. Confidence-Aware Preference Labeling (CAPL): for each training question, sample K reasoning trajectories and compute each one's self-certainty (SC), defined as the average KL divergence of the model's per-token next-token distribution from the uniform distribution across the trajectory -- higher SC means a more peaked, confident predictive distribution. Trajectories are split into Conciseness Pairs (CPs: both correct, shorter preferred) and Deliberation Pairs (DPs: both incorrect, longer preferred, since giving up early on a hard problem is worse than at least attempting more exploration), with preference-pair strength scored by combining a length/correctness-based margin (Delta r) with the SC margin (Delta SC) -- for CPs, favoring solutions that are both efficient AND internally confident; for DPs, penalizing short-but-overconfident wrong answers more than long-but-uncertain ones. A dynamic pruning step keeps only the highest-scoring pairs (top-3 score levels) per query, capped at one CP and one DP per query after global truncation (ratio tau=0.15), to prioritize the most informative supervision. Confidence-Weighted Preference Optimization (CWPO): builds on the SimPO preference-optimization objective but replaces its fixed scaling factor beta with dynamic per-pair weights beta_w/beta_l derived from a calibration ratio rho(x,y) = SC(x,y) / |y|^alpha (self-certainty normalized by a length-aware exponent), so CPs reward paths that are both short and confident more strongly, and DPs penalize short-but-overconfident-wrong trajectories more heavily than long-but-uncertain-wrong ones -- letting the model autonomously judge, per query, when to compress and when to keep deliberating, without any externally-imposed length budget. Trained on 2,000 MATH-training-set questions (20 sampled reasoning paths each) for DeepSeek-R1-Distill-Qwen-7B/1.5B and Qwen3-8B via LoRA (rank 32) on top of SimPO, evaluated on MATH-500, AIME24, and GPQA against OverThink, DAST, and ConCISE(SimPO) baselines, measuring accuracy, mean response length, length among correct-only trajectories, and percentage compression ratios.

## Results

CAT achieves the highest accuracy among all compared efficient-reasoning methods on all three benchmarks across all three base models, while maintaining an acceptable compression ratio (though not always the largest) -- e.g. on Qwen3-8B/MATH-500: 96.6% accuracy (vs. 96.2% backbone, 94.9%/94.6%/94.1% for OverThink/DAST/ConCISE) with 37.9% correct-length reduction; on Qwen3-8B/AIME24: 76.7% accuracy (exceeding the 74.4% backbone) with 34.0% correct-length reduction; on Qwen3-8B/GPQA: 60.9% accuracy (exceeding the 59.9% backbone) with 45.5% correct-length reduction. OverThink and ConCISE achieve larger compression ratios in some settings but at an unavoidable accuracy cost relative to the backbone model, while CAT and DAST show similar accuracy-compression balancing trends, with CAT delivering higher accuracy than DAST in every setting and higher compression than DAST in most settings. Ablation (Table 2, R1-7B) shows removing CAPL (scoring preference pairs by length margin alone, without the SC-based margin) yields a higher compression ratio but larger accuracy degradation on most tasks -- e.g. GPQA accuracy drops to 50.5% (w/o CAPL) vs. 54.0% (full CAT) vs. 49.2% (Origin baseline, meaning w/o CAPL barely beats the untrained model) -- confirming that confidence-aware, not just length-aware, preference signals are necessary for high-quality adaptive compression; removing CWPO (using vanilla SimPO instead) also degrades accuracy/compression versus full CAT on all three benchmarks. Self-certainty analysis (Qwen3-8B on MATH Level 4) shows SC distributions for correct vs. incorrect responses concentrate around distinct, separated means (correct higher), and SC is largely stable/robust across response lengths (only a slight downward trend, attributable to shorter responses containing a higher proportion of correct trajectories) -- validating SC as a length-independent quality signal rather than a proxy that merely tracks verbosity. CAT generalizes to a different preference-optimization backbone: applying the same CAPL-derived preference pairs with a DPO-adapted CWPO objective (CWPO_DPO) beats standard DPO on most metrics across all three benchmarks on R1-7B. A qualitative case study shows CAT reaches the correct answer with the shortest reasoning chain and highest self-certainty of the three compared methods, retaining a brief validity check rather than eliminating reflection entirely or exploring invalid alternatives (as the uncompressed backbone and DAST do).

## Limitations

The framework aggregates token-level self-certainty signals into a single path-level scalar per trajectory, which may overlook variation in confidence at specific reasoning steps; the authors suggest future work could integrate token-position-specific self-certainty scores for more precise step-level compression rather than only whole-trajectory-level compression. Experiments focus on STEM disciplines (mathematics, physics) with datasets that allow rigorous ground-truth correctness verification; although self-certainty itself is an intrinsic, ground-truth-independent signal, CAT's preference-labeling strategy currently still relies on correctness verification results, so extending the approach to open-ended generation tasks (where ground-truth correctness cannot be automatically verified) is left to future work. CAT uses confidence-weighted preference optimization on a static, offline dataset built from pre-sampled trajectories, which limits the policy's ability to dynamically update its confidence estimates during training; the authors flag transitioning to online reinforcement-learning variants (allowing iterative refinement through continuous interaction) as future work.

## Why it matters here

- **overthinking**: Directly central to the topic and explicitly framed as an overthinking-mitigation method: it targets exactly the 'redundant reasoning and self-reflection for simple inputs' pattern the topic tracks, using the model's own intrinsic confidence (rather than an externally-imposed uniform token budget or coarse output-correctness-based difficulty estimate) to decide, per query, whether to compress or keep deliberating. Its finding that self-certainty is stable across response lengths (not merely a proxy for verbosity) and its ablation isolating the distinct contributions of confidence-aware labeling versus confidence-weighted optimization make it methodologically strong evidence for calibration-based, rather than purely length-based, overthinking mitigation -- directly comparable to TALE's prompt-based budget approach and Reflection Steering's activation-based approach already in this archive.

## Entities

- **Concepts**: self-certainty (KL divergence from uniform, path-level confidence measure), Conciseness Pairs / Deliberation Pairs, Confidence-Weighted Preference Optimization (CWPO), dynamic pruning of preference pairs, calibration ratio (confidence normalized by length)
- **Methods**: Confidence-Adaptive Thinking (CAT), self-certainty (path-level KL-divergence confidence), Confidence-Aware Preference Labeling (CAPL), Confidence-Weighted Preference Optimization (CWPO, SimPO- and DPO-based), OverThink / DAST / ConCISE (baselines), [LoRA fine-tuning](../../../../wiki/methods/lora-fine-tuning.md)
- **Datasets**: MATH (2,000 training questions), [MATH-500](../../../../wiki/datasets/math500.md), [AIME 2024](../../../../wiki/datasets/aime-2024.md), [GPQA](../../../../wiki/datasets/gpqa.md)

Tags: `overthinking`, `confidence-calibration`, `preference-optimization`, `adaptive-reasoning`, `token-budget`

## Abstract

Large Reasoning Models (LRMs) have achieved remarkable success on complex tasks by leveraging long chain-of-thought (CoT) trajectories, yet they frequently exhibit overthinking on simple queries, resulting in significant token overhead and reduced inference efficiency. However, existing compression methods predominantly apply uniform length reduction or rely on coarse-grained difficulty estimation, often leading to performance degradation on difficult problems. To address this limitation, we propose Confidence-Adaptive Thinking (CAT), a framework that incorporates the model’s intrinsic self-certainty signals as confidence into the preference optimization process, which autonomously modulates reasoning lengths based on problem difficulty. Experimental results show that CAT consistently outperforms state-of-the-art baselines on reasoning accuracy across multiple benchmarks on different base models. Our work enables LRMs to effectively compress confident responses while deliberating on uncertain ones, offering a potentially robust solution for balancing accuracy and latency in practical industrial scenarios.

---

Record id: `doi:10.18653/v1/2026.acl-industry.152`
