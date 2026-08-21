<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Funnel of Thoughts: Efficient Test-Time Scaling via Early Voting and Rollout Pruning

- **Authors**: Chanhee Park, Sungbin Han, Jeongho Yoon, Seongtae Hong, Heuiseok Lim
- **Venue**: cs.AI
- **Published**: 2026-08-15
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.15065>
- **PDF**: <https://arxiv.org/pdf/2608.15065v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

Funnel of Thoughts detects and discards the subset of parallel reasoning rollouts that are spiraling into unproductive self-correction (flagged by a rising density of hesitation words like 'Wait' and 'perhaps'), matching self-consistency's accuracy while cutting attention FLOPs by up to 56% and wall time by 37.6%.

## Problem

Multi-sample inference (self-consistency, SC@k) is the standard way to get reliable answers from large reasoning models despite their inconsistent per-query outputs, but it is prohibitively expensive because every rollout must run to completion even after entering a wasteful late-stage regime of repetitive, self-correcting, non-committing generation -- and because attention cost is quadratic in sequence length, this unproductive tail dominates the compute cost.

## Contributions

- Data-driven analysis of 115,200 rollouts across 6 LRMs and 4 competition-math benchmarks showing incorrect/no-answer rollouts run far longer (avg 16,128 / never-commit tokens) than correct ones (avg 5,575 tokens) and consume disproportionate attention FLOPs (6.0x and 17.4x respectively)
- Identification of 21 hesitation markers (e.g. 'Wait,', 'perhaps', 'actually') whose density correlates negatively with rollout correctness (pooled point-biserial r=-0.30, monotonic 31.4pp accuracy gap between lowest and highest density deciles)
- Funnel of Thoughts (FoT): a training-free, inference-time algorithm that combines early voting (banking rollouts that have already committed to a final answer) with rollout pruning (discarding active rollouts with the highest hesitation-marker density) to preserve self-consistency accuracy at reduced compute
- Demonstration that FoT preserves SC@32 accuracy (87.7% vs 87.8% average) while cutting attention FLOPs by 28.8% (projection) / 56.1% (online) and wall-clock time by 37.6% in a live deployment, and that the pruning signal transfers unchanged to 4 held-out models and 2 out-of-domain benchmarks (GPQA-Diamond, LCB-Lite)

## Method

Funnel of Thoughts (FoT) starts from the same k parallel reasoning rollouts used by self-consistency (SC@k) and, at m fixed token-count checkpoints during generation, applies two training-free mechanisms using only the already-generated text (no logits, embeddings, or extra model calls). (1) Early voting: any active rollout that has already produced a final boxed answer is moved from the active set into a 'vote bank,' preserving its vote while freeing its compute slot -- this is what makes the method a funnel (shrinking the active pool while keeping the ballot full) rather than a simple truncation. (2) Rollout pruning: among the rollouts still active, FoT computes a 'hesitation marker density' (occurrences per 1,000 characters of a fixed 21-word lexicon such as 'Wait,', 'perhaps', 'actually', selected via benchmark-weighted point-biserial correlation with correctness on a held-out 115,200-rollout profiling pool) over each rollout's generated text so far, ranks rollouts by density, and discards the highest-density fraction (keep ratio rho, a fixed hyperparameter) as rollouts exhibiting unproductive self-correction spirals. After the final checkpoint, the answer is selected by plurality vote over the vote bank plus any surviving active rollouts. The pruning signal is purely relative (within the same model, problem, and checkpoint), which is why it transfers across architectures and domains without retuning.

## Results

Table 2 (main results, k=32, 6 models x 4 benchmarks): FoT@32 preserves SC@32 accuracy on average (87.7% vs 87.8%) while saving 54.5% attention FLOPs on average (per-benchmark mean); FoT and SC@32 agree on 3,580 of 3,600 model-problem instances, differing on only 20 (12 FoT wins, 8 losses; not significant under McNemar's exact test, p=0.50; paired-bootstrap 95% CI on accuracy difference [-0.14, +0.36]pp). On the hard split (AIME24+25), FoT preserves SC@32's 75.0% accuracy while saving 57.3% FLOPs, versus Adaptive Consistency's 75.2% accuracy at 44.9% FLOP saving and Slim-SC's 70.3% accuracy (-4.7pp) at 64.0% saving. Cross-model transfer to 4 held-out models (Qwen3-14B, Qwen3-32B, Skywork-OR1-7B, Phi-4-reasoning) with unchanged configuration preserves SC@32 accuracy (1600->1615 out of 2400, +0.6pp) while saving 51.9% attention FLOPs on average. Cross-domain transfer: on GPQA-Diamond, FoT improves accuracy by +1.3pp on average while saving 41.0% FLOPs; on LCB-Lite (code, execution-based grading), FoT improves mean per-rollout pass rate by +1.42pp while saving 56.8% FLOPs, though pass@k (oracle pool accuracy) declines modestly by -2.8pp on average, described as 'the expected cost of any method that shrinks the oracle pool.' Online deployment on 30 AIME24 problems with DeepSeek-R1-Distill-Qwen-7B (single A100): FoT@32 solves 24/30 problems vs SC@32's 23/30, cuts wall time by 37.6% (21,561s to 13,445s), attention FLOPs by 56.1%, and cumulative KV-cache token footprint from 12.88M to 8.51M tokens. Mechanism ablation (Table 7) isolates that the hesitation-density pruning signal, not early voting, drives the accuracy preservation: random pruning loses accuracy at similar compute savings, while density-based pruning preserves SC@32 accuracy (94.47% vs 94.36% baseline) even without early voting; early voting's role is keeping the keep-ratio hyperparameter safe to expose as a deployment knob rather than providing accuracy gain itself.

## Limitations

Stated in Section 6: evaluation is centered on tasks with extractable final answers (boxed numbers, multiple-choice, or executable code); open-ended generation, multi-turn interaction, and tasks where correctness cannot be reduced to answer extraction are outside the study's scope. The calibration pool is unbalanced (MATH500 supplies 3,000 of 3,600 model-problem pairs), so pooled statistics are weighted toward easy problems where pruning has little to remove or risk; the paper reports the hard split separately for this reason. Early voting relies on a commitment detector (the \boxed{} convention in math), and the vote bank's reliability is bounded by that detector's accuracy in other domains. The method uses a fixed checkpoint schedule and an English hesitation-marker kernel; models reasoning in other languages or with substantially different deliberation styles may need a revalidated marker set. FLOP accounting assumes standard full attention; under efficient-attention mechanisms the saving shrinks toward a token-reduction floor (48.7% down to 23.0% in the linear limit, per Appendix D.2). Pool-size sweeps show pruning is mildly harmful when the sampling pool k is small (k=8), becomes neutral around k=16, and only turns clearly positive beyond that -- so FoT is intended as a large-pool replacement for self-consistency, not a general small-k method. Slim-SC (a competing baseline) over-prunes on hard samples (drops AIME25 accuracy from 69.4 to 61.7 while saving 67.1% FLOPs), illustrating that similarity-based pruning approaches can discard useful diversity, a failure mode FoT is designed to avoid via a different (hesitation-density, within-pool relative) signal.

## Why it matters here

- **overthinking**: Directly on-topic: the paper is centrally about the overthinking phenomenon at the level of individual reasoning trajectories -- it shows incorrect/non-committing rollouts run 2.9x-5.6x longer than correct ones and identifies 'spiraling' self-correction (repeated 'Wait', 'Actually', 'perhaps') as a lexical signature of unproductive extra thinking that consumes disproportionate compute without improving (and often degrading) accuracy. Its method directly implements 'stop or discard reasoning that has gone past the point where it helps,' i.e. exactly the stopping-point / accuracy-efficiency tradeoff the topic tracks, though applied at the granularity of pruning whole rollouts within a self-consistency pool rather than truncating a single trace.

## Entities

- **Concepts**: hesitation markers as a lexical signal of unproductive reasoning, late-stage generation waste in self-consistency, rollout pruning vs sample-axis stopping rules, early voting / vote banking, hesitation-marker density as a leading indicator of runaway trajectory length
- **Methods**: Funnel of Thoughts (FoT), Self-Consistency (SC@k), early voting / vote banking, hesitation-marker density pruning, Adaptive Consistency (baseline), [Slim-SC (baseline)](../../../../wiki/methods/slim-sc-baseline.md)
- **Datasets**: [AIME24](../../../../wiki/datasets/aime-2024.md), [AIME25](../../../../wiki/datasets/aime-2025.md), [AMC23](../../../../wiki/datasets/amc23.md), [MATH500](../../../../wiki/datasets/math500.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), LCB-Lite

Tags: `test-time-scaling`, `self-consistency`, `overthinking`, `rollout-pruning`, `inference-efficiency`, `reasoning-length`

## Abstract

Large Reasoning Models produce diverse, sometimes inconsistent answers across repeated queries on the same problem, so multi-sample inference is a prerequisite for reliable deployment. Majority voting at k rollouts is the standard solution and the de facto accuracy target for this regime, but it is prohibitively expensive at the scale LRMs require. We introduce Funnel of Thoughts (FoT), an inference-time method that preserves the full 32-trajectory voted accuracy while halving its attention FLOPs, a 28.8% reduction in full-model inference cost. Across 115K reasoning trajectories from six LRMs, we find that unproductive trajectories often reveal themselves through repeated hesitation markers such as "Wait", "Actually", and "perhaps." These trajectories are less likely to reach the correct answer and consume disproportionate attention FLOPs, degenerating into no-answer loops in the worst case. Built on this training-free lexical signal, FoT identifies the vocabulary that captures these pathological patterns and prunes affected trajectories before completion, reducing online generation attention FLOPs by 56.1% and wall time by 37.6% without any additional model inference; the same signal transfers without retuning across held-out architectures and out-of-domain tasks.

---

Record id: `arxiv:2608.15065`
