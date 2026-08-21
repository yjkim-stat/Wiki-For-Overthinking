<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Mixture-of-Visual-Thoughts: Exploring Context-Adaptive Reasoning Mode Selection for General Visual Reasoning

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10011171>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Unifies text-based and visually-grounded reasoning in one vision-language model and uses RL with a mode-relative advantage to make the model pick which mode to use per input, raising average accuracy over eight benchmarks by about 5 points.

## Problem

Visual reasoning methods each commit to one reasoning mode -- pure language chain of thought, or reasoning grounded in image coordinates -- and each helps in the domain it suits while failing outside it, so no single model reasons generally. The open question is whether one model can hold both modes and choose between them from context rather than being fixed to one.

## Contributions

- MoVT: a paradigm holding multiple visual reasoning modes in one model with context-dependent selection between them
- AdaVaR: a two-stage framework, a cold-start SFT stage unifying modes via a shared sequence format with mode-specific prefix tokens, then an RL stage that induces selection
- AdaGRPO: prefix-guided mode exploration, a mode-relative advantage comparing rollouts across modes on the same input, and curriculum-based data scheduling
- Average gains of about 5 points over the Qwen2.5-VL base at 3B and 7B across eight benchmarks, with AdaVaR-7B above the reported GPT-4o average
- Per-benchmark mode-selection statistics showing the learned policy specialises text mode to math and grounded mode to perception tasks

## Method

MoVT is the paradigm: several reasoning modes inside one model, selected by context. AdaVaR is the two-stage training framework that produces it. Stage one is a supervised cold start that unifies the modes: reasoning paths of all modes are written in one sequence format inside <think> tags and distinguished only by a mode-specific prefix token, which lets data from different modes be mixed in a single SFT run. Stage two induces selection by RL with AdaGRPO, which has three parts: prefix-guided mode exploration, which fixes the prefix to force even sampling of each mode rather than letting the policy collapse early to one; a mode-relative advantage that compares rollouts across modes on the same input so the update rewards the better mode rather than the better rollout; and curriculum-based data scheduling, starting on easy items where the modes differ coarsely and moving to harder ones. The two modes unified are text-based reasoning (chain-of-thought rationales expressed in natural language) and visually-grounded reasoning (structured outputs such as bounding boxes or points that tie reasoning steps to image regions). Neither is a direct-answer or no-reasoning mode; both emit an explicit chain.

## Results

Base models Qwen2.5-VL-3B and 7B, evaluated on eight benchmarks: MathVista, MathVision, MathVerse, WeMath (math-oriented) and MMStar, V*, POPE, SpatialScore (general). AdaVaR-3B averages 50.84% against 45.74% for Qwen2.5-VL-3B, including MathVista 69.8% vs 62.3%; AdaVaR-7B averages 55.82% against 50.90% for Qwen2.5-VL-7B, above the 53.20% average reported for GPT-4o. The mode-selection analysis is the more informative result: after RL the model picks text mode almost exclusively on the math benchmarks (0-2% grounded on MathVista, MathVerse, WeMath), grounded mode almost exclusively on V* and POPE (99-100%), and splits roughly evenly on MMStar (~51% grounded). Single-mode and mixed-data baselines both underperform AdaVaR, which the authors read as adaptivity rather than data diversity being the source of the gain.

## Limitations

No stated limitations section was found in the material available. Two the reader should notice. First, the paper reports no token counts, latency or any other cost measure for either mode, so nothing here says what adaptive mode selection costs or saves -- the case is made entirely on accuracy. Second, the near-degenerate selection rates (0-2% and 99-100%) mean that on six of the eight benchmarks the learned policy is close to a fixed per-dataset choice; the paper does not report an oracle-per-dataset-mode baseline, which is what would separate genuine per-instance adaptivity from having learned the domain-to-mode mapping. Only two modes are unified, and only two model sizes tested, both Qwen2.5-VL.

## Why it matters here

- **overthinking**: Partly relevant, on the machinery rather than the question. The mechanism -- train one model to hold several reasoning behaviours and use RL to make it choose per input -- is the same construction used for think/no-think routing that the topic tracks, and AdaGRPO's mode-relative advantage (compare rollouts of different modes on the same input, reward the mode not the rollout) is a training signal directly reusable for a long-vs-short reasoning decision. But the axis being selected here is representational, text chain-of-thought against coordinate-grounded reasoning, not how much to think: both modes emit a full chain, neither is a direct-answer mode, and the paper reports no token counts, latency or cost of any kind, so it contains no evidence about the accuracy/efficiency tradeoff. It also does not claim one; the gains are accuracy gains. Take it as a method to borrow, not as a result about reasoning length.

## Entities

- **Concepts**: adaptive reasoning mode selection, visually-grounded reasoning, mode-relative advantage, prefix-guided exploration, reasoning mode routing
- **Methods**: MoVT, AdaVaR, AdaGRPO, [GRPO](../../../../wiki/methods/grpo.md), supervised cold start, curriculum data scheduling
- **Datasets**: [MathVista](../../../../wiki/datasets/mathvista.md), [MathVision](../../../../wiki/datasets/mathvision.md), [MathVerse](../../../../wiki/datasets/mathverse.md), [WeMath](../../../../wiki/datasets/wemath.md), [MMStar](../../../../wiki/datasets/mmstar.md), V*, [POPE](../../../../wiki/datasets/pope.md), SpatialScore

Tags: `adaptive-reasoning`, `visual-reasoning`, `mode-selection`, `reinforcement-learning`, `multimodal`, `grpo`

---

Record id: `title:4321f3ae06d02a2e`
