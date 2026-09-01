<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# From Reasoning Traces to Reusable Modules: Understanding Compositional Generalization in Language Model Reasoning

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/61216>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Proposes that RL post-training's out-of-distribution generalization advantage over supervised fine-tuning stems from compositional generalization -- reasoning decomposes into reusable atomic modules (skills and routing mechanisms) that RL's exploratory nature has sufficient coverage to discover and recombine -- and validates this with controlled experiments showing models extract atomic components from complex examples and recombine them for novel problems, with training on compound examples outperforming isolated module practice.

## Problem

RL post-training significantly improves LLM out-of-distribution reasoning performance over supervised training alone, but why this happens -- what RL's exploration actually buys beyond imitating correct answers -- was not well understood.

## Contributions

- a framework modeling LLM reasoning as discrete latent selections over reusable atomic modules (skills and routing mechanisms)
- a theoretical argument that RL's exploratory nature (versus imitating fixed correct trajectories) provides the coverage needed to discover this latent modular structure and enable compositional generalization
- controlled experiments confirming module extraction and recombination, showing compound-example training beats isolated-module practice, and identifying an SFT-for-coverage-then-RL-for-composition training protocol as most effective

## Method

Models reasoning as discrete latent selections corresponding to reusable atomic modules, comprising both skills (local reasoning operations) and routing mechanisms (which module to apply when); provides a theoretical analysis arguing RL's exploratory nature gives sufficient coverage to identify this latent modular structure and enable compositional generalization (recombining known modules for novel problems), unlike supervised training on fixed correct trajectories; validates with controlled experiments testing whether models extract atomic components from complex training examples and recombine them for novel test problems, and compares training exclusively on compound (multi-module) examples against training separately on isolated single-module practice.

## Results

Controlled experiments confirm models can extract atomic reasoning components from complex training examples and successfully recombine them to solve novel problems not seen during training. Training on compound (multi-module) examples outperforms training on isolated single-module practice for building compositional generalization. An effective training protocol is identified: combining supervised training (to ensure adequate coverage of individual modules) with reinforcement learning (to enable novel compositions of those modules) outperforms either approach alone.

## Limitations

Not stated in the fetched abstract beyond the modular reasoning framework and controlled experimental setup described.

## Why it matters here

- **overthinking**: Indirectly relevant: this is a theoretical account of why RL-trained reasoning generalizes (compositional module reuse), not a length-control or efficiency method, but it offers a structural framework -- reasoning as combinations of reusable atomic modules -- potentially relevant to understanding what makes a long reasoning trace productive (genuine module composition) versus wasteful (e.g. non-compositional repetition), a distinction implicit in much of the overthinking literature.

## Entities

- **Concepts**: compositional generalization in reasoning, reusable atomic modules (skills and routing), RL exploration as latent-structure discovery
- **Methods**: reinforcement learning post-training, supervised fine-tuning (comparison), compound vs. isolated module training
- **Datasets**: _none recorded_

Tags: `reasoning-modularity`, `compositional-generalization`, `reinforcement-learning`, `reasoning-traces`

---

Record id: `title:3deb1b5a47e5bf3b`
