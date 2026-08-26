<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Think Less, Act Early: Reinforced Latent Reasoning with Early Exit in Vision-Language-Action Models

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/61571>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

AVA-VLA replaces explicit chain-of-thought in a vision-language-action policy with a sequence of latent reasoning variables trained by RL denoising, and adds a confidence-gated early exit that cuts mean reasoning depth from 5.0 to 2.3 steps and latency from 312 ms to 145 ms at essentially unchanged LIBERO success rate.

## Problem

Vision-language-action models bridge perception and action with explicit chain-of-thought text, which is expensive to generate and lets errors propagate across the steps of a long-horizon task. Reasoning in a latent space avoids the text generation, but latent trajectories are vulnerable to noise and can drift from the downstream control objective; and a fixed latent depth spends the same reasoning on every state regardless of how hard it is.

## Contributions

- AVA-VLA: a VLA framework that carries reasoning in latent variables instead of generated chain-of-thought text
- An RL-based denoising mechanism that optimises latent reasoning trajectories against task-level rewards, treating latent state generation as a sequential decision process
- A confidence-gated early-exit strategy that varies reasoning depth per state, reducing mean depth from 5.0 to 2.3 steps
- Measurements separating depth from accuracy: 98.3% LIBERO success at 145 ms adaptive versus 98.0% at 156 ms (depth 5) and 98.1% at 267 ms (depth 10)

## Method

AVA-VLA (Adaptive Variable Alignment VLA) models reasoning as a sequence of unobservable latent variables rather than generated text, so no tokens are emitted between perception and action. To keep the latent trajectory aligned with the task, a reinforcement-learning denoising mechanism treats latent state generation as a sequential decision process and optimises the trajectory against task-level rewards rather than a token-level objective. On top of this an early-exit strategy terminates the latent rollout once state confidence passes a gate, so the number of reasoning steps varies per state instead of being fixed, trading reasoning depth against latency at inference time.

## Results

On LIBERO with one policy across all suites, 98.3% average success rate, and 98.1% on LIBERO-Long. On CALVIN ABC->D, 84.0% success on five-step tasks against FLOWER at 77.8%. Efficiency: mean latency 145 ms with early exit against 312 ms without it, and about 6x faster than explicit CoT methods (145 ms vs 892 ms). The depth study (Table 13) is the relevant one for the tradeoff: a fixed depth of 5 gives 98.0% at 156 ms, a fixed depth of 10 gives 98.1% at 267 ms, and adaptive early exit gives 98.3% at 145 ms. Ablations: removing latent reasoning drops LIBERO success to 95.8%, removing RL denoising to 96.6%, and removing early exit leaves success at 98.0% while raising cost.

## Limitations

The authors state that premature exit can occur when the confidence gate is overconfident, and suggest online safety monitors would be needed for physical deployment; they also note the framework gives up the natural-language interpretability that explicit reasoning provides. Their own numbers bound the claim: doubling fixed reasoning depth from 5 to 10 moves success by 0.1 points (98.0% to 98.1%) while latency rises from 156 ms to 267 ms, and removing early exit entirely still yields 98.0%, so on these benchmarks accuracy is flat across the depth range tested and the contribution of the early exit is latency rather than accuracy. LIBERO success rates at 98% are close enough to saturation that the benchmark cannot resolve whether adaptive depth helps accuracy; a harder task suite would be needed. All results are in simulation.

## Why it matters here

- **overthinking**: On-topic, with a caveat about what it actually measures. The paper does run the tradeoff experiment the topic cares about rather than reporting latency alone: Table 13 varies reasoning depth and reports accuracy against latency, and the early-exit ablation isolates the gate's effect. But the accuracy side of that tradeoff is flat, not favourable: fixed depth 5 gives 98.0%, fixed depth 10 gives 98.1%, adaptive gives 98.3%, all within a third of a point, while latency ranges over 145-267 ms. So the honest reading is that on LIBERO the extra reasoning depth buys nothing measurable and the early exit is a latency optimisation that costs no accuracy, rather than a demonstration that stopping at the right point improves answers. Two things transfer to the topic regardless: a confidence gate as a stopping criterion operating on latent states rather than tokens, and the failure mode the authors name, an overconfident gate exiting prematurely, which is the same risk any confidence-based stopping rule carries. The near-saturated benchmark is why this is evidence about cost, not about when a model should keep going.

## Entities

- **Concepts**: [latent reasoning](../../../../wiki/concepts/latent-reasoning.md), early exit, [confidence-based stopping](../../../../wiki/concepts/confidence-based-stopping.md), reasoning depth vs efficiency tradeoff, vision-language-action models, error propagation in multi-step reasoning
- **Methods**: AVA-VLA, latent reasoning, reinforcement-learning denoising, confidence-gated early exit, explicit chain-of-thought VLA (baseline), FLOWER (baseline)
- **Datasets**: LIBERO, [LIBERO-Long](../../../../wiki/datasets/libero-long.md), CALVIN ABC->D

Tags: `early-exit`, `latent-reasoning`, `vision-language-action`, `robotics`, `adaptive-computation`, `confidence-gating`, `efficient-reasoning`

---

Record id: `title:e3df9e3ad63924a6`
