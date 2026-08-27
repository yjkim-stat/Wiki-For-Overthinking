<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# A Simple "Motivation" Can Enhance Reinforcement Finetuning of Large Reasoning Models

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10011610>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

MeRF (Motivation-enhanced Reinforcement Finetuning) puts the verifiable reward specification itself into the training prompt, giving the model advance awareness of its optimization objective, and substantially improves over baseline RLVR performance.

## Problem

Standard Reinforcement Learning with Verifiable Rewards (RLVR) trains via trial-and-error exploration without giving the model any awareness of the overall reward pattern it is being optimized against, making exploration inefficient.

## Contributions

- MeRF, which puts the verifiable reward specification directly into the training prompt as task motivation
- an empirical demonstration of substantial gains over baseline RLVR from this simple addition
- an ablation showing gains scale with alignment between the in-context motivation and the true reward function

## Method

Exploits that verifiable rewards can be expressed in natural language and that LLMs have strong in-context learning ability: MeRF directly incorporates the reward specification into the prompt as an explicit 'motivation,' so the model understands its optimization objective before training begins, rather than discovering it purely through trial and error.

## Results

MeRF demonstrates substantial improvements over baseline RLVR performance; ablations show gains scale with the alignment between the in-context motivation and the actual reward function, and models can also adapt to deliberately contradictory motivations through the RL process (no specific numeric deltas given in the fetched abstract).

## Limitations

Not stated in the fetched abstract; the approach depends on rewards being expressible as natural-language specifications, which the excerpt does not discuss the limits of.

## Why it matters here

- **overthinking**: Indirectly relevant: it targets training-time sample efficiency of RLVR (how quickly a model learns its objective) rather than inference-time reasoning length, but a model trained with explicit awareness of its reward pattern is a plausible lever for shaping *what* the reasoning is optimized for -- including, in principle, an efficiency or length-aware objective, though the fetched abstract does not test that.

## Entities

- **Concepts**: in-context reward specification ('motivation'), Reinforcement Learning with Verifiable Rewards (RLVR), exploration efficiency in RL fine-tuning
- **Methods**: Reinforcement Learning with Verifiable Rewards (RLVR), in-context reward specification
- **Datasets**: _none recorded_

Tags: `reinforcement-learning`, `RLVR`, `training-efficiency`, `large-reasoning-models`

---

Record id: `title:a7838a0be137b21d`
