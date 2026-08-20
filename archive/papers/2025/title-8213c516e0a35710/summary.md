<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Test-Time Scaling of Diffusion Models via Noise Trajectory Search

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/116804>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Optimizes the sequence of injected noise vectors during diffusion model denoising, using an epsilon-greedy search cast as sequential contextual bandits, to improve image generation quality at fixed or extra test-time compute.

## Problem

Diffusion models can trade extra denoising compute for higher-fidelity samples, but simply adding denoising steps gives diminishing returns; searching over the noise trajectory itself is a high-dimensional, costly problem this paper tries to make tractable.

## Contributions

- Casts diffusion model denoising as a Markov Decision Process with a terminal reward and shows tree-search methods like MCTS are meaningful but impractical for it
- Relaxes the MDP into a sequence of independent contextual bandits to make search tractable
- Introduces an epsilon-greedy search algorithm that explores globally at extreme timesteps and exploits locally during intermediate de-mixing steps
- Reports state-of-the-art scores on class-conditioned and text-to-image generation with EDM and Stable Diffusion, exceeding baselines by up to 164% and matching or exceeding MCTS performance
- Presents the first practical method for test-time noise trajectory optimization of arbitrary, non-differentiable rewards in diffusion models

## Method

Formulates the denoising trajectory of a diffusion model as an MDP with a terminal reward, then relaxes it to a sequence of independent contextual bandits (one per denoising step) to make search over noise vectors tractable. An epsilon-greedy algorithm explores broadly at extreme timesteps and exploits locally in intermediate steps where de-mixing occurs, searching over injected noise vectors rather than the number of denoising steps.

## Results

Exceeds baselines by up to 164% on class-conditioned/text-to-image generation with EDM and Stable Diffusion, and matches or exceeds MCTS performance while being more practical. No specific baseline names or absolute metric values are given in the abstract.

## Limitations

The abstract does not report compute cost of the epsilon-greedy search relative to baselines, nor limitations of the contextual-bandit relaxation versus the full MDP. Not stated whether the approach generalizes beyond image diffusion models.

## Why it matters here

- **overthinking**: This is test-time scaling for image diffusion models (optimizing injected noise vectors during denoising), not for large language or reasoning models. It shares only the generic term 'test-time scaling' with the tracked topic; it has no connection to reasoning token length, chain-of-thought stopping, or the accuracy/efficiency tradeoff of LLM reasoning that the topic is about.

## Entities

- **Concepts**: noise trajectory optimization, diffusion denoising as a Markov Decision Process, denoising as sequential contextual bandits, epsilon-greedy global exploration / local exploitation search
- **Methods**: epsilon-greedy noise trajectory search, Monte Carlo tree search (baseline comparison), Markov Decision Process formulation, contextual bandits
- **Datasets**: EDM (class-conditioned image generation), Stable Diffusion (text-to-image generation)

Tags: `diffusion-models`, `test-time-scaling`, `image-generation`, `noise-search`, `tangential`

## Abstract

Abstract The iterative and stochastic nature of diffusion models enables *test-time scaling*, whereby spending additional compute during denoising generates higher-fidelity samples. Increasing the number of denoising steps is the primary scaling axis, but this yields quickly diminishing returns. Instead optimizing the *noise trajectory*—the sequence of injected noise vectors—is promising, as the specific noise realizations critically affect sample quality; but this is challenging due to a high-dimensional search space, complex noise-outcome interactions, and costly trajectory evaluations. We address this by first casting diffusion as a Markov Decision Process (MDP) with a terminal reward, showing tree-search methods such as Monte Carlo tree search (MCTS) to be meaningful but impractical. To balance performance and efficiency, we then resort to a relaxation of MDP, where we view denoising as a sequence of independent *contextual bandits*. This allows us to introduce an $\epsilon$-greedy search algorithm that *globally explores* at extreme timesteps and *locally exploits* during the intermediate steps where de-mixing occurs. Experiments on EDM and Stable Diffusion reveal state-of-the-art scores for class-conditioned/text-to-image generation, exceeding baselines by up to $164$% and matching/exceeding MCTS performance. To our knowledge, this is the first practical method for test-time noise *trajectory* optimization of *arbitrary (non-differentiable)* rewards.

---

Record id: `title:8213c516e0a35710`
