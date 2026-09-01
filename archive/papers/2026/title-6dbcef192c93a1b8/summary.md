<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Restoring Exploration after Post-Training: Latent Exploration Decoding for Large Reasoning Models

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/66546>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Identifies 'exploration collapse' after RL post-training of large reasoning models -- temperature-based sampling no longer increases pass@n accuracy because final-layer output entropy diminishes even though intermediate-layer entropy stays high -- and proposes Latent Exploration Decoding (LED), a training-free depth-conditioned decoding strategy that aggregates intermediate-layer posteriors to restore exploration, improving pass@1 by 0.61 and pass@16 by 1.03 points on average across benchmarks and models.

## Problem

RL post-training gives large reasoning models strong math/code performance, but they suffer an unintended side effect -- exploration collapse -- where temperature-based sampling no longer increases pass@n accuracy, limiting the benefit of parallel/repeated sampling at test time.

## Contributions

- identification of exploration collapse as an unintended side effect of RL post-training, where final-layer entropy diminishes while intermediate-layer entropy remains high
- Latent Exploration Decoding (LED), a training-free decoding strategy that restores sampling diversity by aggregating intermediate-layer posteriors instead of relying on the collapsed final-layer distribution
- consistent pass@1/pass@16 improvements across multiple benchmarks and models with zero additional training

## Method

Observes that post-trained models show significantly diminished entropy specifically in their final-layer output distribution while intermediate layers retain substantially higher entropy, indicating exploratory diversity is not lost from the model overall but suppressed at the output layer; proposes Latent Exploration Decoding (LED), a depth-conditioned decoding strategy that aggregates posteriors from intermediate layers and identifies configurations with maximum entropy to restore effective sampling diversity, requiring no additional training.

## Results

LED delivers consistent improvements across multiple benchmarks and models with no additional training: 0.61 percentage points average pass@1 improvement and 1.03 percentage points average pass@16 improvement, directly addressing the diminished-return-from-more-samples problem caused by exploration collapse.

## Limitations

Not stated in the fetched abstract beyond the reported average pass@1/pass@16 gains and the benchmarks/models tested.

## Why it matters here

- **overthinking**: Directly relevant to the archive's test-time-scaling and RL-training-dynamics thread: this identifies a distinct, previously under-addressed failure mode -- final-layer-specific entropy collapse suppressing the benefit of parallel sampling (pass@n) after RL post-training -- complementary to SCOPE's token-level entropy-collapse analysis read earlier this round, and its training-free, depth-conditioned fix (reading from intermediate layers rather than the collapsed output layer) is a novel lever for restoring exploration that doesn't require retraining or reward redesign.

## Entities

- **Concepts**: exploration collapse (post-RL), final-layer vs. intermediate-layer entropy disparity, Latent Exploration Decoding (depth-conditioned decoding)
- **Methods**: Latent Exploration Decoding (LED), temperature-based sampling (baseline)
- **Datasets**: _none recorded_

Tags: `exploration-collapse`, `test-time-scaling`, `decoding-strategy`, `reinforcement-learning-side-effects`

---

Record id: `title:6dbcef192c93a1b8`
