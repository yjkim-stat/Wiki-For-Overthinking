<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Cloud-ScPO: Hidden-State Geometry for Semi-Supervised Preference Optimization in LLM Reasoning

- **Authors**: Yuzhou Liu, Xiyang Hu
- **Venue**: cs.CL
- **Published**: 2026-08-02
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.01014>
- **PDF**: <https://arxiv.org/pdf/2608.01014v1>
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.40, reasoning-interpretability 0.25, test-time-scaling 0.25

## In one line

Scores unlabeled reasoning trajectories by how their mean-pooled hidden states connect to correct and incorrect reference point clouds built from a small labeled set, and uses that score to pick the concrete chosen and rejected responses inside answer clusters that self-consistency has already separated.

## Problem

Preference optimization needs chosen-rejected pairs, and the reliable ways of building them all cost something the semi-supervised setting does not have: verified answers, human annotation, or a trained reward model. Self-consistency-based methods (ScPO) supply a direction by majority answer, but leave open which concrete trajectory to take when several share an answer, and are unreliable when the prompt-level vote is close. Semi-supervised reward modelling replaces one dependency with another, since the pseudo-labels are only as good as the small labeled preference set the reward model was trained on.

## Contributions

- A trajectory-quality signal derived from cross-problem representation geometry rather than from within-prompt consensus, on the observation that correct trajectories from different problems merge into connected components at smaller filtration scales than incorrect ones
- A multi-bank scoring rule: R balanced correct/incorrect reference banks are resampled from the labeled pools, each candidate is scored against every bank by a component-level soft k-nearest-neighbour compatibility, and the bank scores are averaged
- Integration with self-consistency in which the vote sets the answer-level preference direction and the Cloud score selects the trajectories within the chosen and rejected answer clusters and filters pairs by score margin
- A pair-level diagnostic protocol — ideal-pair rate, both-incorrect rate, reversed-pair rate, and automatic detection of incompleteness and repetition — used to compare preference data rather than only end accuracy

## Method

A trajectory is represented by the L2-normalized mean of the final-layer hidden states over its valid response tokens; the paper argues this beats the last token, which can be dominated by answer formatting or punctuation. From 600 labeled problems, trajectories are split into a correct pool and an incorrect pool by answer match, and R balanced reference banks are drawn from them with replacement. Inside each bank, zero-dimensional persistent homology under a Vietoris-Rips filtration is run and edges are processed in ascending Euclidean distance, stopping after ceil((N-1)/2) merges, to obtain connectivity-induced components; a candidate is scored against a class by a component-size-weighted sum of exp(-d^2/tau) over its q nearest components, and the final score subtracts the incorrect-cloud term with weight lambda_neg. For the hybrid, ScPO's majority answer is the preferred cluster and a least-frequent eligible non-majority answer the rejected one; Cloud scores then choose the highest- and lowest-scoring trajectory within those clusters, pairs are ranked by the resulting margin and the top alpha fraction is kept. Training is DPO plus a length-normalized negative log-likelihood term on the chosen response, weighted by ScPO's normalized vote margin. Settings: K = 8 rollouts, alpha = 0.30, R = 20 banks of 200 labeled problems, q = 5, tau = 2.0, lambda_neg = 1.0, beta = 0.10, learning rate 5e-6, on 4x A40.

## Results

On GSM8K, Cloud-ScPO is best on both backbones: Llama-3-8B 52.24% against ScPO's 49.74% and IRPO-RM's 46.40%, and Mistral-7B 32.92% against 28.43% and 15.23% — gains of 2.50 and 4.49 points over ScPO. It does this with roughly a third of IRPO-RM's pairs (1,329 vs 3,794; 1,163 vs 2,511). On MATH-Numeric the picture splits: with Qwen3-8B it reaches 62.33% against ScPO's 58.14% and IRPO-RM's 56.99% using 963 pairs against 4,178, but with Llama-3-8B it loses to IRPO-RM, 23.01% against 23.51%. That failure has a stated cause in the pair statistics: on Llama-3-8B MATH-Numeric the ideal-pair rate is 7.58% for ScPO and 7.56% for Cloud-ScPO, with over 92% of pairs holding two incorrect responses, so there is little for a selection rule to select. Pair quality improves where the pool allows it — ideal-pair rate 89.02% to 90.37% on GSM8K/Llama and 56.51% to 59.67% on GSM8K/Mistral, with risky reversed pairs falling from 1.98% to 1.88% and 3.05% to 2.24%. Rejected responses become more visibly defective under Cloud scoring: incomplete-or-truncated rises from 27.84% to 41.46% and obvious repetition from 27.99% to 38.22% on GSM8K/Llama. The Cloud-gap analysis is the sharpest evidence for the score itself: among the top 5% of candidate pairs by score gap, 94.77% disagree on the final answer, against 13.89% across all 6,862 candidates.

## Limitations

The paper has no limitations section. What a reader should weigh: the topological claim is validated qualitatively on Level 3 and Level 4 subsets of MATH with 200 points per cloud, and the appendix states directly that it should not be read as establishing the same pattern for every difficulty level or model configuration. The H1 (loop) signal is reported as exploratory and is not used in scoring at all, and the paper says it weakens after pooling and normalization. The mean-token versus last-token comparison in Table 5 uses different retention ratios, beta and learning rates, so it compares two whole pipelines rather than isolating the representation, which the paper acknowledges. The reference-bank ablation does not identify a single best configuration — M=100 with R=10 gives the best AUC at 67.02 while R=20 gives better extreme rankings — so the setting used for the main results is not the one that maximizes discrimination. Only one labeled-set size is tried (600 problems), only two datasets, and no cost accounting is given for the filtration and multi-bank scoring against a reward-model forward pass.

## Why it matters here

- **reasoning-evaluation**: Its transferable contribution to evaluation is not the training method but the diagnostics: it scores preference data by ideal-pair rate, both-incorrect rate, reversed-pair rate and automatic incompleteness and repetition detection, and shows those move independently of end accuracy — on MATH-Numeric with Llama-3-8B the pair statistics explain a loss the accuracy number alone would leave mysterious. It also supplies a calibration result for a training-free confidence signal: the representation-geometry score gap ranks candidate pairs so that the top 5% are answer-disagreeing 94.77% of the time against a 13.89% base rate, which is a claim about what a hidden-state signal can predict without any verifier.

## Entities

- **Concepts**: persistent homology, hidden-state geometry, [reasoning trajectory](../../../../wiki/concepts/reasoning-trajectory.md), preference optimization, self-consistency, preference pair quality, semi-supervised learning
- **Methods**: Cloud-ScPO, ScPO, [DPO](../../../../wiki/methods/dpo.md), [supervised fine-tuning](../../../../wiki/methods/supervised-fine-tuning.md), Vietoris-Rips filtration, mean pooling of hidden states
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), MATH-Numeric

Tags: `preference optimization`, `representation geometry`, `semi-supervised`, `topological data analysis`, `mathematical reasoning`

## Abstract

Preference optimization improves mathematical reasoning in large language models (LLMs), but reliable chosen-rejected pairs usually require verified answers, human annotations, or external reward models. We investigate whether preference supervision can instead be derived from the model's internal representation geometry in a semi-supervised setting. Our analysis shows that reasoning trajectories generated across different mathematical problems form structured global point clouds in which correct and incorrect trajectories exhibit different geometric organization. Based on this observation, we propose Cloud--ScPO, a topology-guided preference-mining framework that uses a small labeled set to construct multiple correct and incorrect reference Clouds. Each trajectory is represented by a mean-pooled hidden state and scored against connectivity-induced components using a component-level soft $k$-nearest-neighbor measure averaged across reference banks. We combine this cross-problem Cloud signal with prompt-level self-consistency: self-consistency determines the answer-level preference direction, while Cloud scoring selects concrete trajectories and filters pairs by their score margin. Experiments on GSM8K and MATH-Numeric across four model settings show that Cloud--ScPO consistently improves over ScPO, with gains of up to 4.49\% on GSM8K and 4.19\% on MATH-Numeric. Pair-level analyses further show that Cloud--ScPO maintains comparable correctness reliability while more effectively separating informative chosen trajectories from incomplete, repetitive, or otherwise low-quality rejected responses.

---

Record id: `arxiv:2608.01014`
