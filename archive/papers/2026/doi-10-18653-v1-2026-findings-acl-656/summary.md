<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# DeepPrune: Parallel Scaling without Inter-trace Redundancy

- **Authors**: Shangqing Tu, Yaxuan Li, Yushi Bai, Lei Hou, Juanzi Li
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.656/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.656.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.656
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## In one line

DeepPrune identifies inter-trace redundancy in parallel test-time scaling (over 80% of parallel reasoning traces yield identical final answers) and trains a specialized judge model to predict answer equivalence from unfinished trace pairs, combined with online greedy clustering to prune redundant paths during generation, cutting token consumption 65.7-88.5% versus consensus sampling with accuracy within 3 percentage points.

## Problem

Parallel scaling (running many CoT traces simultaneously and majority-voting the final answer) improves reasoning accuracy but at severe computational cost -- pushing total token cost to 100M or more -- because a large fraction of the parallel traces are redundant, converging to the same final answer; existing efficient-reasoning methods target sequential-scaling overthinking (shortening one trace) or use single-trace confidence signals for early stopping, but no prior method explicitly models and prunes redundancy *between* parallel traces, and confidence-based methods risk prematurely terminating traces that are actually correct.

## Contributions

- identification and quantification of inter-trace redundancy as the primary efficiency bottleneck in parallel test-time scaling, showing over 80% of parallel reasoning traces on average yield identical final answers -- a previously unaddressed complement to sequential-scaling overthinking
- a specialized, trained judge model predicting answer equivalence from unfinished (truncated) reasoning-trace pairs, substantially outperforming both shallow semantic similarity and zero-shot LLM judgment, with reasoning-word-aligned truncation shown superior to fixed-token windows
- an online greedy clustering algorithm that dynamically prunes redundant parallel traces during generation while preserving answer diversity, requiring only pairwise comparisons against cluster representatives rather than exhaustive comparison
- 65.7-88.5% token reduction versus consensus sampling with accuracy within 3 points across three reasoning models and three benchmarks, substantially outperforming confidence-based pruning baselines, with strong out-of-distribution/cross-model generalization

## Method

Confirms inter-trace redundancy empirically: across four reasoning models (Deepseek-R1-Distill-Llama-8B, Qwen3-4B-Thinking-2507, GLM-4.5-Air, QwQ-32B) on Math500/AIME24/AIME25/GPQA, 16 parallel traces per problem paired exhaustively show over 80% same-final-answer pairs on average (up to 94.5% for GLM-4.5-Air). Shows shallow semantic similarity (SentenceBERT cosine similarity on first 700 tokens) is a poor predictor of eventual answer equivalence (AUROC=0.58, barely above chance) and zero-shot LLM judgment (Qwen3-4B-Instruct) is only moderately better (AUROC=0.66) -- motivating a specialized, trained judge model. DeepPrune has two stages: (1) offline, fine-tunes Qwen3-4B-Instruct as a judge model J_theta on trace pairs collected from Deepseek-R1-Distill-Llama-8B on out-of-distribution data (AIME 2022/2023, MATH 500), labeled by rule-based answer-equivalence checking (DeepScaleR's verifier); to handle the ~80/20 class imbalance, trains with focal loss plus 2x oversampling of the minority (different-answer) class, and finds top-25-reasoning-word truncation (segments aligned to discourse markers like 'wait', 'thus', 'since') outperforms fixed-token-count truncation, since it captures structurally meaningful reasoning boundaries rather than an arbitrary token window; (2) online, applies an online greedy clustering algorithm during generation: each new unfinished trace is compared (via the judge) against representative sampled traces from existing clusters, assigned to the most similar cluster if above a redundancy threshold tau (default 0.5) or used to found a new cluster otherwise, letting only the largest cluster's top-q traces continue reasoning to completion, then majority-voting the final answer -- avoiding exhaustive pairwise comparison for real-time inference.

## Results

Offline, the best judge configuration (top-25 reasoning words + focal loss + oversampling) achieves 0.8701 average AUROC and 0.8186 TNR@0.2 across three out-of-distribution reasoning models -- a substantial improvement over the zero-shot LLM judgment baseline (AUROC=0.66) -- confirming specialized training on reasoning-word-truncated traces is necessary; oversampling alone (without focal loss) degrades performance, showing the combination, not just class balancing, is what matters. Online, across three reasoning models (DeepSeek-8B, Qwen3-32B, GPT-OSS-20B) and three benchmarks (AIME24, AIME25, GPQA), DeepPrune reduces token consumption by 65.73-88.50% versus cons@512 (512-trace consensus sampling) while maintaining accuracy within 3 percentage points, and substantially outperforms confidence-based pruning baselines (DeepConf-high/low): e.g. on Qwen3-32B/AIME25, DeepPrune cuts tokens by 91.4% while *improving* accuracy from 80.0% (cons@512) to 90.0%, whereas DeepConf-low achieves only 80.2% accuracy with less token savings at the same setting. DeepPrune's judge model, trained exclusively on out-of-distribution DeepSeek-R1-Distill-Llama-8B traces, generalizes strongly to three entirely unseen reasoning models in online testing -- a practical, cross-model-transferable solution. A redundancy-threshold ablation (Table 3, Qwen3-32B on AIME datasets) shows a clear diversity-efficiency trade-off: lowering tau from 0.75 to 0.25 sharply reduces token consumption via more aggressive pruning, but on AIME25 the pass rate (proxy for answer diversity preserved after clustering) drops from 96.7% to 70% under the tightest pruning, and majority-voting accuracy follows the same trend -- tau=0.5 is identified as the best balance across benchmarks tested.

## Limitations

The judge model is trained exclusively on reasoning traces from a single source model (Deepseek-R1-Distill-Llama-8B), which the authors note may limit generalization to model families with substantially different reasoning styles, though cross-model evaluation shows promising results. The greedy clustering algorithm makes locally optimal decisions and can occasionally prune beneficial diverse paths, particularly in complex reasoning scenarios where early-trace similarity is not indicative of eventual answer equivalence. The judge model itself adds inference overhead during pruning, so the net efficiency gain depends on the cost ratio between the judge and the reasoning model being pruned. The optimal redundancy threshold tau may be problem-dependent; the paper uses a single fixed value (0.5) across all benchmarks rather than adaptive threshold selection, which it flags as a promising future direction.

## Why it matters here

- **overthinking**: Directly relevant and identifies a distinct, previously under-addressed variety of reasoning waste: rather than a single trace's sequential overthinking (excess tokens within one CoT), DeepPrune quantifies and targets *inter-trace* overthinking in parallel scaling -- most parallel samples in a best-of-N or majority-vote setup are redundant computation from the start. This extends the archive's overthinking-measurement and mitigation literature (largely focused on single-trace length) to the parallel/multi-sample setting, and its empirical finding (>80% same-answer traces on average, up to 94.5%) is a strong, directly quotable statistic for how much of parallel test-time compute is wasted.

## Entities

- **Concepts**: inter-trace redundancy, answer-equivalence judge model, online greedy clustering (early stopping), reasoning-word-aligned truncation
- **Methods**: DeepPrune (judge model + online greedy clustering), cons@512 (majority-voting consensus baseline), DeepConf-high / DeepConf-low (confidence-based pruning baselines)
- **Datasets**: AIME 2022 (training), AIME 2023 (training), MATH 500 (training), [AIME 2024](../../../../wiki/datasets/aime-2024.md), [AIME 2025](../../../../wiki/datasets/aime-2025.md), [GPQA](../../../../wiki/datasets/gpqa.md)

Tags: `overthinking`, `parallel-scaling`, `inter-trace-redundancy`, `test-time-scaling`, `efficient-reasoning`

## Abstract

Parallel scaling has emerged as a powerful paradigm to enhance reasoning capabilities in large language models (LLMs) by generating multiple Chain-of-Thought (CoT) traces simultaneously. However, this approach introduces significant computational inefficiency due to inter-trace redundancy—our analysis reveals that over 80% of parallel reasoning traces yield identical final answers, representing substantial wasted computation. To address this critical efficiency bottleneck, we propose DeepPrune, a novel framework that enables efficient parallel scaling through dynamic pruning. Our method features a specialized judge model trained with oversampling techniques to accurately predict answer equivalence from partial reasoning traces, achieving 0.7072 AUROC on equivalence prediction across unseen reasoning models. This is combined with an online greedy clustering algorithm that dynamically prunes redundant paths while preserving answer diversity. Comprehensive evaluations across three challenging benchmarks (AIME 2024, AIME 2025, and GPQA) and multiple reasoning models demonstrate that DeepPrune achieves remarkable token reduction ranging from 65.73% to 88.50% compared to conventional consensus sampling, while maintaining competitive accuracy within 3.4 percentage points. Our work establishes a new standard for efficient parallel reasoning, making high-performance reasoning more efficient. Our code and data are here: https://github.com/THU-KEG/DeepPrune/

---

Record id: `doi:10.18653/v1/2026.findings-acl.656`
