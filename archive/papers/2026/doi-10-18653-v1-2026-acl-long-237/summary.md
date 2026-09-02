<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Miner: Mining Intrinsic Mastery for Data-Efficient RL in Large Reasoning Models

- **Authors**: Shuyang Jiang, Yuhao Wang, Ya Zhang, Yanfeng Wang, Yu Wang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.237/>
- **PDF**: <https://aclanthology.org/2026.acl-long.237.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.237
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

MINER recovers training signal from 'positive homogeneous' (PH) prompts -- where all sampled RLVR rollouts are already correct and GRPO-style advantage collapses to zero, wasting the rollout budget -- by converting the policy's own per-token uncertainty (negative log-likelihood) into an intrinsic reward that reinforces under-confident-but-correct reasoning paths, combined with token-level focal credit assignment and adaptive advantage calibration, achieving up to +4.58 Pass@1 and +6.66 Pass@K over GRPO with zero extra rollouts or inference cost.

## Problem

As base reasoning models grow stronger, an increasing share of RLVR training prompts become 'positive homogeneous' (PH) -- every sampled rollout for that prompt is already correct -- causing GRPO-style relative advantage estimation to collapse to zero and rendering the full rollout cost of these prompts computationally wasted, since the update contributes no learning signal despite consuming the same sampling budget as informative prompts.

## Contributions

- identification and formalization of the positive-homogeneous (PH) prompt data-inefficiency problem in RLVR, where an increasing share of training prompts as base models strengthen yield zero-advantage, computationally wasted rollouts under standard GRPO
- an uncertainty-driven intrinsic reward using only the policy's own per-token negative log-likelihood (no external hints, auxiliary reward models, or extra rollouts) to recover a dense, self-supervised learning signal from PH prompts, combined with positive filtering to avoid penalizing already-confident correct trajectories
- token-level focal credit assignment that concentrates gradient updates on uncertain 'bottleneck' tokens rather than uniformly across a trajectory, and adaptive advantage calibration that bounds the intrinsic signal's scale relative to the batch's extrinsic verifier signal to preserve training stability
- state-of-the-art empirical gains (up to +4.58 Pass@1, +6.66 Pass@K over GRPO) across six math benchmarks and two model scales, with demonstrated domain transfer to medical QA, robustness to mode collapse under large-K sampling, and stable scaling to a 14B backbone with zero hyperparameter re-tuning

## Method

Classifies each training prompt by its rollout-group correctness pattern into positive homogeneous (PH, all correct), negative homogeneous (all incorrect), or heterogeneous (mixed), and targets PH prompts specifically (existing work mostly addresses negative-homogeneous prompts via hints or replay buffers). MINER has three coupled components: (1) Uncertainty-Driven Intrinsic Rewards -- defines an intrinsic reward as the per-token negative log-likelihood of each PH rollout (a correct response with high NLL is treated as less mastered by the policy), computes a group-mean-centered intrinsic advantage without standard-deviation normalization (to preserve absolute uncertainty-gap magnitude), and applies positive filtering (ReLU) so only under-confident-yet-correct trajectories are reinforced, leaving already-confident correct rollouts untouched; (2) Token-Level Focal Credit Assignment -- reweights each token's intrinsic advantage by a focal factor (1-p)^gamma based on the old policy's token probability, concentrating gradient updates on low-probability 'bottleneck' tokens along the reasoning chain rather than spending gradient budget uniformly on already-confident tokens; (3) Adaptive Advantage Calibration -- scales the aggregated intrinsic advantage per batch by a reference signal (the total absolute standard GRPO advantage magnitude from heterogeneous prompts in the same batch) capped by a hyperparameter lambda_max, ensuring the intrinsic-reward signal never overrides or destabilizes the extrinsic verifier-based objective from prompts with genuine outcome variance.

## Results

On Qwen3-4B-Base and Qwen3-8B-Base across six math reasoning benchmarks (AIME2024, AIME2025, AMC23, HMMT25, MATH, OlympiadBench), MINER achieves the best average Pass@1 and Pass@K among GRPO, DAPO, REINFORCE++ and GSPO baselines plus a strong exploration-enhancement baseline UCAS: on Qwen3-4B, average Pass@1 45.55 / Pass@K 74.92 versus GRPO's 40.97/70.69 (+4.58/+4.23) and DAPO's 46.46/70.74; on Qwen3-8B, average Pass@1 47.07/Pass@K 77.03 versus GRPO's 44.70/70.39 (+2.37/+6.66 Pass@K) and DAPO's 44.59/74.89. Domain-generalization experiments on five medical-QA benchmarks (MedQA, MedMCQA, PubMedQA, MedXpertQA, MMLU-Pro medical) with Llama3.1-8B-Instruct show MINER outperforms GRPO and two data-intensive medical-specialized baselines (HuatuoGPT-o1, MedReason, both requiring complex data processing and GPT-4o distillation) while remaining stable even with >65% PH prompts per batch, confirming domain- and backbone-agnostic gains. Ablation removing intrinsic reward (fixed advantage for all PH rollouts) causes unstable training with reduced Pass@1/Pass@K; removing token-level focal weighting (uniform token weight) substantially reduces Pass@K exploration gains despite retaining sharpened-knowledge Pass@1; removing advantage calibration causes mid-training underfitting, together confirming all three components are necessary. Comparison against other exploration-enhancement methods that instead reshape advantages on heterogeneous prompts (BAPO, KL-Cov, Clip-Cov, Entropy-Adv) shows those baselines fail to generalize as consistently across benchmarks/metrics as reported in their original papers, while MINER surpasses them by a large margin with only one new hyperparameter. Under an extended 32K-token inference budget, MINER shows a stable, statistically significant +1.9 Pass@1 improvement while other methods' gains fluctuate within the margin of error; under large-K parallel test-time scaling (self-consistency up to K=512 trajectories), MINER shows sustained, non-plateauing improvement over the base model on AIME24/25/HMMT25 while most compared methods show performance staleness, indicating MINER mitigates mode collapse rather than merely sharpening the existing policy distribution. Scaling to Qwen3-14B-Base with the same lambda_max (no re-tuning) preserves consistent gains over GRPO (+4.11 Pass@1, +5.18 Pass@K), and extending RL training to a second epoch shows stable KL/entropy dynamics with continuously improving AIME24 scores on both 4B and 8B backbones, indicating no signs of training collapse from prolonged use.

## Limitations

The work focuses specifically on unlocking signal from positive-homogeneous prompts and does not directly address negative-homogeneous prompts (all-incorrect rollouts), which the paper treats as a complementary, largely orthogonal problem addressed by other existing techniques (hints, in-context demonstrations, replay buffers). Training was validated only up to Qwen3-14B-Base due to computational constraints; scaling to substantially larger backbones (e.g. 32B) was not tested, though the paper notes the same hyperparameter setting transferring smoothly from 4B to 14B suggests further scaling would require more compute rather than methodological changes.

## Why it matters here

- **overthinking**: Indirectly relevant: this is a training-time RL data-efficiency method (recovering signal from already-solved prompts) rather than a direct intervention on reasoning-trace length or the inference-time accuracy/efficiency tradeoff, but it is upstream infrastructure for the same GRPO-style training pipeline that many overthinking-mitigation papers in this archive build reward-shaping (length penalties, difficulty-aware rewards) on top of -- a more data-efficient base RLVR recipe is complementary to, not competing with, those length-control objectives, and its demonstrated resistance to mode collapse under large-K sampling is relevant to papers in this archive studying self-consistency's diminishing returns.

## Entities

- **Concepts**: positive homogeneous (PH) prompt, uncertainty-driven intrinsic reward (per-token NLL), token-level focal credit assignment, adaptive advantage calibration
- **Methods**: MINER (uncertainty-driven intrinsic reward + token-level focal credit assignment + adaptive advantage calibration), [GRPO (baseline)](../../../../wiki/methods/grpo-baseline.md), [DAPO (baseline)](../../../../wiki/methods/dapo-baseline.md), REINFORCE++ (baseline), GSPO (baseline), UCAS (baseline), BAPO, KL-Cov, Clip-Cov, Entropy-Adv (exploration-enhancement baselines)
- **Datasets**: [MATH500](../../../../wiki/datasets/math500.md), [AMC23](../../../../wiki/datasets/amc23.md), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md), [AIME2024](../../../../wiki/datasets/aime-2024.md), [AIME2025](../../../../wiki/datasets/aime-2025.md), [HMMT25](../../../../wiki/datasets/hmmt25.md), DeepScaleR (training), [MedQA](../../../../wiki/datasets/medqa.md), MedMCQA, PubMedQA, MedXpertQA, MMLU-Pro (medical subset)

Tags: `reinforcement-learning`, `RLVR`, `data-efficiency`, `training-efficiency`, `large-reasoning-models`

## Abstract

Current critic-free RL methods for large reasoning models suffer from severe inefficiency when training on positive homogeneous prompts (where all rollouts are correct), resulting in waste of rollouts due to zero advantage estimates. We introduce a radically simple yet powerful solution to Mine intrinsic mastery (Miner), that repurposes the policy’s intrinsic uncertainty as a self-supervised reward signal, with no external supervision, auxiliary models, or additional inference cost. Our method pioneers two key innovations: (1) a token-level focal credit assignment mechanism that dynamically amplifies gradients on critical uncertain tokens while suppressing overconfident ones, and (2) adaptive advantage calibration to seamlessly integrate intrinsic and verifiable rewards. Evaluated across six reasoning benchmarks on Qwen3-4B and Qwen3-8B base models, Miner achieves state-of-the-art performance among the other four algorithms, yielding up to 4.58 absolute gains in Pass@1 and 6.66 gains in Pass@K compared to GRPO. Comparison with other methods targeted at exploration enhancement further discloses the superiority of the two newly proposed innovations. This demonstrates that latent uncertainty exploitation is both necessary and sufficient for efficient and scalable RL training of reasoning models. Code is available at https://github.com/pixas/Miner.

---

Record id: `doi:10.18653/v1/2026.acl-long.237`
