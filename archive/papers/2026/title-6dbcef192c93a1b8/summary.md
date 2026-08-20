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

Introduces a training-free decoding method that restores exploration in RL-post-trained reasoning models by sampling from the intermediate layer with maximal entropy rather than only the final layer.

## Problem

Reasoning models trained with reinforcement learning suffer 'exploration collapse', where standard temperature-based sampling at the final layer fails to improve performance, traced to an entropy imbalance between final-layer and intermediate-layer predictions.

## Contributions

- Identifies 'exploration collapse' in RL-post-trained reasoning models, where temperature-based sampling fails to boost performance
- Identifies an entropy imbalance: final-layer predictions have markedly lower entropy than intermediate-layer predictions
- Proposes Latent Exploration Decoding (LED), a training-free, parameter-free depth-conditioned decoding strategy that aggregates intermediate posteriors via cumulative sum and selects the depth with maximal entropy as an exploration candidate

## Method

LED aggregates the model's intermediate-layer output posteriors via a cumulative sum across depth, and at each decoding step selects the depth configuration with maximal entropy as the exploration candidate, instead of relying only on the final layer's (lower-entropy) distribution. It requires no additional training or parameters.

## Results

LED improves pass@1 accuracy by 0.61 percentage points and pass@16 accuracy by 1.03 percentage points on average across multiple reasoning benchmarks and models.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Tangential to the length/stopping-point focus of the topic. LED addresses sampling diversity across multiple generated solutions (pass@1 and pass@16) after RL post-training, i.e. exploration collapse in breadth-wise test-time sampling, rather than controlling the length of a single reasoning chain or when a model should stop or keep going within one chain.

## Entities

- **Concepts**: exploration collapse, entropy imbalance across layers, depth-conditioned decoding
- **Methods**: Latent Exploration Decoding (LED)
- **Datasets**: _none recorded_

Tags: `exploration`, `decoding`, `entropy`, `reasoning-diversity`

---

Record id: `title:6dbcef192c93a1b8`
