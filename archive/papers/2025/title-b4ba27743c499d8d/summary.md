<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Mitigating Overthinking in Large Reasoning Models via Manifold Steering

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/119969>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.67

## In one line

Identifies that overthinking in large reasoning models corresponds to a low-dimensional manifold in activation space and proposes projecting steering interventions onto that manifold to cut output tokens by up to 71% without hurting accuracy.

## Problem

Large reasoning models exhibit overthinking during inference -- excessive validation loops and redundant deliberation -- causing substantial computational overhead; prior single-direction activation steering to fix this plateaus and even degrades performance as intervention strength increases.

## Contributions

- Shows overthinking tendency is captured by a single direction in activation space, and that steering along it reduces overthinking up to a plateau
- Shows the overthinking-relevant activation space is actually a low-dimensional manifold, explaining why naive high-dimensional steering saturates and degrades
- Proposes Manifold Steering, which projects the steering direction onto this low-dimensional manifold using a theoretical approximation of interference noise
- Demonstrates cross-domain transfer of the method from math to code generation and knowledge-based QA

## Method

The authors first identify a single activation-space direction correlated with overthinking and show intervening on it reduces overthinking but plateaus and then hurts performance as intervention strength grows. They trace this to the direction actually lying on a low-dimensional manifold within the high-dimensional activation space, so naive steering introduces noise. Manifold Steering projects the steering direction onto this low-dimensional manifold, using a theoretical approximation of the interference noise, before applying it to activations at inference time.

## Results

On DeepSeek-R1 distilled models, Manifold Steering reduces output tokens by up to 71% while maintaining or improving accuracy on several mathematical benchmarks, with consistent token-reduction transfer to code generation and knowledge-based QA tasks.

## Limitations

The abstract does not name the specific benchmarks, model sizes beyond 'DeepSeek-R1 distilled models', or report where accuracy gains versus losses occur; no discussion of failure cases or when the projection approximation breaks down is given.

## Why it matters here

- **overthinking**: Directly targets the topic's core question: it locates the mechanistic source of excessive reasoning length in activation space and proposes an inference-time intervention (Manifold Steering) that reduces output tokens by up to 71% while maintaining or improving accuracy on math benchmarks, with transfer to code and QA tasks.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), [mechanistic interpretability](../../../../wiki/concepts/mechanistic-interpretability.md), activation steering, low-dimensional manifold
- **Methods**: [Manifold Steering](../../../../wiki/methods/manifold-steering.md), [activation steering](../../../../wiki/methods/activation-steering.md), mechanistic interpretability analysis
- **Datasets**: mathematical benchmarks (unspecified), code generation tasks (unspecified), knowledge-based QA tasks (unspecified)

Tags: `overthinking`, `activation-steering`, `mechanistic-interpretability`, `reasoning-length`, `deepseek-r1`, `inference-efficiency`

## Abstract

Abstract Recent advances in Large Reasoning Models (LRMs) have demonstrated remarkable capabilities in solving complex tasks such as mathematics and coding. However, these models frequently exhibit a phenomenon known as overthinking during inference, characterized by excessive validation loops and redundant deliberation, leading to substantial computational overheads. In this paper, we aim to mitigate overthinking by investigating the underlying mechanisms from the perspective of mechanistic interpretability. We first showcase that the tendency of overthinking can be effectively captured by a single direction in the model's activation space and the issue can be eased by intervening the activations along this direction. However, this efficacy soon reaches a plateau and even deteriorates as the intervention strength increases. We therefore systematically explore the activation space and find that the overthinking phenomenon is actually tied to a low-dimensional manifold, which indicates that the limited effect stems from the noises introduced by the high-dimensional steering direction. Based on this insight, we propose Manifold Steering , a novel approach that elegantly projects the steering direction onto the low-dimensional activation manifold given the theoretical approximation of the interference noise. Extensive experiments on DeepSeek-R1 distilled models validate that our method reduces output tokens by up to 71\% while maintaining and even improving the accuracy on several mathematical benchmarks. Our method also exhibits robust cross-domain transferability, delivering consistent token reduction performance in code generation and knowledge-based QA tasks. Code is available at: https://github.com/Aries-iai/Manifold_Steering.

---

Record id: `title:b4ba27743c499d8d`
