<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# e3: Learning to Explore Enables Extrapolation of Test-Time Compute for LLMs

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10008718>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Trains a 1.7B-parameter reasoning model to chain complementary skills like verification and generation in-context, so accuracy keeps improving as it thinks for longer, extending beyond its training token budget.

## Problem

Most existing reasoning models do not extrapolate well: their accuracy stops improving, or degrades, once inference is allowed to run beyond the token budget used during training.

## Contributions

- Trains models via RL to perform systematic in-context exploration by chaining complementary skills (e.g. verification with generation)
- Uses learning signal from incorrect reasoning paths to encourage deeper exploration
- Introduces curriculum training that aligns task complexity with available compute budget
- A 1.7B parameter model (e3) whose accuracy keeps improving as it is allowed to think for longer, extending gains to roughly 2x its original training token budget

## Method

e3 trains a model to perform in-context exploration by chaining complementary, asymmetric operations -- for example pairing answer verification with generation -- so that additional thinking tokens are spent productively rather than repeating the same reasoning. Training uses reinforcement learning that draws a learning signal from incorrect trajectories to push further exploration, combined with a curriculum that matches task difficulty to the compute budget available during training.

## Results

The resulting 1.7B parameter model achieves competitive performance on mathematics benchmarks and shows improving accuracy on hard problems as it is allowed to keep thinking for longer, with the gains extending to roughly 2x the original training token budget.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Directly addresses the 'think more' side of the tradeoff: it studies why models fail to keep improving as reasoning length grows past their training budget, and trains a model whose accuracy on hard problems keeps rising the longer it thinks, with gains extending to about 2x the original training budget.

## Entities

- **Concepts**: extrapolation of test-time compute, in-context exploration, chaining asymmetric skills
- **Methods**: e3, curriculum training, chaining of asymmetric skills (verification + generation)
- **Datasets**: _none recorded_

Tags: `test-time-compute`, `extrapolation`, `exploration`, `reasoning-length`, `reinforcement-learning`

---

Record id: `title:6b3ab05159d7f803`
