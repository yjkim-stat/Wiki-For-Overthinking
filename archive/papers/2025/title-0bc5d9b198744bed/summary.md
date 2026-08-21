<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/118864>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.67

## In one line

AutoThink uses a three-stage RL curriculum with stage-wise reward shaping to teach R1-style distilled models to decide per problem whether to emit an explicit reasoning chain at all.

## Problem

R1-style large reasoning models emit a step-by-step chain before every answer, including on problems that do not need one, which costs tokens and latency. Making the decision to think or not think conditional on problem difficulty is open because the models have no explicit control channel for the mode and RL on a length penalty alone tends to collapse to a single mode.

## Contributions

- Reports that inserting an ellipsis into the '<think>' prompt of an R1-style distilled model stochastically triggers either a thinking or a no-thinking continuation, exposing a latent mode control that needs no architectural change
- Proposes AutoThink, a three-stage RL framework - mode stabilisation by batch-level reward balancing, then unconstrained refinement, then length-aware pruning - that trains the model to select the mode per problem
- Reports a 52% token reduction with 51.7% vs 48.6% average accuracy on DeepSeek-R1-Distill-Qwen-1.5B across five mathematical benchmarks, and applies the same recipe to four further R1-style checkpoints

## Method

The authors observe that replacing the usual reasoning prompt with '<think>\n...\n' - an ellipsis left open - makes an untrained R1-style distilled model stochastically enter either a thinking or a no-thinking mode, which they use as an existing control handle rather than adding a new token or head. On top of this they run three RL stages. Stage 1 stabilises both modes with batch-level reward balancing: penalty factors for the thinking and no-thinking branches are driven by a target ratio and a slope so that whichever mode dominates a batch is softly penalised, preventing collapse. Stage 2 drops the balancing term and applies the plain correctness reward with a larger context budget, letting each mode improve on its own terms. Stage 3 adds length-aware reward modulation with exponential decay: a correct response is penalised in proportion to its length, an incorrect one receives a length-dependent bonus, so brevity is rewarded only when the answer is right and further elaboration is not punished when it is wrong. The result is a policy that defaults to a short direct answer and opens a reasoning chain when the problem calls for it.

## Results

On DeepSeek-R1-Distill-Qwen-1.5B, AutoThink Stage 3 reaches 51.7% average accuracy at 5,108 average tokens against 48.6% at 10,633 tokens for the standard prompt - a 3.1-point absolute gain, which is the 6.4% figure the abstract quotes in relative terms, alongside a 52% token reduction. Per-benchmark accuracy for that model spans 84.0% on MATH to 44.8% on OlympiadBench. On other backbones the accuracy moves the other way: DeepScaleR-Preview-1.5B Stage 3 falls to 55.7% from 56.7%, Skywork-OR1-Math-7B Stage 3 to 68.8% from 70.5% while saving about 60% of tokens, and on Qwen3-8B the ellipsis prompt alone costs 5 points (74.8% vs 79.7%). So the token savings are consistent across backbones; the accuracy gain is not, and the headline is the best of the five settings rather than the typical one.

## Limitations

The authors state three: reward hacking, where the model relocates reasoning after the '</think>' tag so the two modes are not cleanly separated; no control over a global token budget, since the method adapts reasoning length but cannot enforce a cap; and unfiltered training data, used without difficulty-based curriculum filtering. A reader should add that evaluation is dominated by mathematics, that the accuracy improvement holds only on the 1.5B distilled backbone while three of the other four settings lose accuracy, and that the ellipsis trigger is a property of R1-style distilled checkpoints and is not shown to exist in models trained differently.

## Why it matters here

- **overthinking**: A direct instance of the topic: the paper's stated target is the over-thinking problem, and its unit of decision is whether to think at all rather than how long to think. Two things are worth carrying forward. First, the ellipsis finding says the no-thinking mode already exists inside R1-style distilled checkpoints and can be reached by prompt alone - the RL is shaping a choice the model can already make, which is a cheaper story than training a stopping mechanism from scratch. Second, the per-backbone table is a useful corrective to how these results are usually quoted: the accuracy gain appears on one backbone and three others lose 0.9 to 5 points while saving tokens, so this belongs in the archive as evidence that adaptive-mode RL buys length reliably and accuracy only sometimes. The stated reward-hacking failure - reasoning re-emitted after '</think>' - is also a concrete warning for any length-reward scheme the group evaluates.

## Entities

- **Concepts**: [Overthinking](../../../../wiki/concepts/overthinking.md), Adaptive Thinking, Thinking Mode Switching, [Reward Shaping](../../../../wiki/concepts/reward-shaping.md), Mode Collapse, [Accuracy-Efficiency Tradeoff](../../../../wiki/concepts/accuracy-efficiency-tradeoff.md), [Test-Time Compute](../../../../wiki/concepts/test-time-compute.md)
- **Methods**: [AutoThink](../../../../wiki/methods/autothink.md), multi-stage reinforcement learning, GRPO-style policy optimisation, batch-level reward balancing, length-aware reward modulation, ellipsis prompt ('<think>\n...\n')
- **Datasets**: [MATH](../../../../wiki/datasets/math.md), [Minerva Math](../../../../wiki/datasets/minerva.md), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md), [AIME24](../../../../wiki/datasets/aime-2024.md), [AMC23](../../../../wiki/datasets/amc23.md), [GPQA](../../../../wiki/datasets/gpqa.md), [MMLU](../../../../wiki/datasets/mmlu.md), [LiveCodeBench](../../../../wiki/datasets/livecodebench.md)

Tags: `overthinking`, `adaptive-reasoning`, `reinforcement-learning`, `reward-shaping`, `token-efficiency`, `r1-distill`, `math-reasoning`, `test-time-compute`

## Abstract

Abstract Large reasoning models (LRMs) are proficient at generating explicit, step-by-step reasoning sequences before producing final answers. However, such detailed reasoning can introduce substantial computational overhead and latency, particularly for simple problems. To address this over-thinking problem, we explore how to equip LRMs with adaptive thinking capabilities—enabling them to dynamically decide whether or not to engage in explicit reasoning based on problem complexity. Building on R1-style distilled models, we observe that inserting a simple ellipsis ("...") into the prompt can stochastically trigger either a thinking or no-thinking mode, revealing a latent controllability in the reasoning behavior. Leveraging this property, we propose AutoThink, a multi-stage reinforcement learning (RL) framework that progressively optimizes reasoning policies via stage-wise reward shaping. AutoThink learns to invoke explicit reasoning only when necessary, while defaulting to succinct responses for simpler tasks. Experiments on five mainstream mathematical benchmarks demonstrate that AutoThink achieves favorable accuracy–efficiency trade-offs compared to recent prompting and RL-based pruning methods. It can be seamlessly integrated into any R1-style model, including both distilled and further fine-tuned variants. Notably, AutoThink improves relative accuracy by 6.4\% while reducing token usage by 52\% on DeepSeek-R1-Distill-Qwen-1.5B, establishing a scalable and adaptive reasoning paradigm for LRMs. Project Page: https://github.com/ScienceOne-AI/AutoThink.

---

Record id: `title:0bc5d9b198744bed`
