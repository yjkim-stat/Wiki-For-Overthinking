<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# AdaNav: Adaptive Reasoning with Uncertainty for Vision-Language Navigation

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/61535>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

AdaNav introduces an Uncertainty-Adaptive Reasoning Block that dynamically triggers extra reasoning during vision-language navigation based on action-entropy metrics, trained via a Heuristics-to-RL methodology that lets agents learn difficulty-aware reasoning policies from only 6,000 samples, outperforming closed-source models trained on far larger datasets.

## Problem

Vision-language navigation agents need to reason adaptively about when a situation is uncertain enough to warrant deliberation, but embodied-AI training data is limited, making it hard to learn difficulty-aware reasoning policies that trigger extra reasoning only when needed rather than uniformly or never.

## Contributions

- an Uncertainty-Adaptive Reasoning Block that dynamically triggers reasoning during navigation based on action-entropy
- a Heuristics-to-RL training methodology enabling difficulty-aware reasoning policy learning from limited embodied-AI data
- 20%/11.7%/11.4% improvements on R2R val-unseen/RxR-CE/real-world navigation using only 6,000 training samples, beating larger closed-source models

## Method

Introduces an Uncertainty-Adaptive Reasoning Block that dynamically triggers reasoning based on action-entropy metrics (higher predicted-action uncertainty triggers more deliberate reasoning), trained via a Heuristics-to-RL methodology -- starting from heuristic difficulty signals and transitioning to reinforcement learning -- to let the agent learn a difficulty-aware reasoning policy despite scarce embodied-AI training data.

## Results

Using only 6,000 training samples, AdaNav achieves a 20% improvement on R2R val-unseen, 11.7% on RxR-CE, and 11.4% in real-world scenes, outperforming closed-source models trained on substantially larger datasets.

## Limitations

Not stated in the fetched abstract beyond the vision-language navigation domain and the 6,000-sample training scale reported.

## Why it matters here

- **overthinking**: Indirectly relevant: an embodied-AI analog of difficulty-adaptive reasoning -- deciding when to spend extra reasoning effort based on an entropy/uncertainty signal rather than uniformly -- structurally similar to difficulty-adaptive test-time compute methods proposed for LLM reasoning, but applied to navigation action selection rather than text-based chain-of-thought.

## Entities

- **Concepts**: Uncertainty-Adaptive Reasoning Block, action-entropy-triggered reasoning, Heuristics-to-RL training methodology
- **Methods**: Uncertainty-Adaptive Reasoning Block, Heuristics-to-RL training
- **Datasets**: R2R (val-unseen), RxR-CE

Tags: `vision-language-navigation`, `adaptive-reasoning`, `uncertainty-driven-computation`, `embodied-ai`

---

Record id: `title:20e2f5ee0a29cfd6`
