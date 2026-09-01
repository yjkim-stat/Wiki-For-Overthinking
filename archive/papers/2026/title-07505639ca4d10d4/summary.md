<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# SPARC: Separating Perception And Reasoning Circuits for Test-time Scaling of VLMs

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/62906>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

SPARC is a modular test-time-scaling framework for vision-language models that separates visual perception from reasoning into two stages -- explicit visual search to localize question-relevant regions, then reasoning conditioned only on those regions -- enabling asymmetric compute allocation and improving Qwen3VL-4B on the V* VQA benchmark by 6.7 points at reduced compute versus existing methods.

## Problem

Test-time scaling for vision-language models is brittle because unstructured visual reasoning chains entangle perception and reasoning into long, disorganized contexts, letting perception errors compound through the reasoning process with no way to independently scale or optimize the two stages.

## Contributions

- SPARC, a modular two-stage framework separating explicit visual search (perception) from reasoning conditioned on localized regions, addressing entangled long, disorganized visual reasoning contexts
- asymmetric per-stage compute allocation and selective optimization when either perception or reasoning becomes a bottleneck
- a 6.7-point improvement on Qwen3VL-4B/V* VQA at reduced compute versus existing test-time-scaling methods

## Method

SPARC implements a two-stage pipeline: first, explicit visual search identifies question-relevant regions of the image; second, reasoning is conditioned only on those localized regions rather than the full unstructured visual context. This separation enables asymmetric compute allocation (scaling perception and reasoning independently), selective optimization when a bottleneck emerges in either stage, and context compression via global low-resolution search combined with high-resolution processing restricted to the selected regions.

## Results

SPARC improves Qwen3VL-4B on the V* VQA benchmark by 6.7 points while using significantly reduced computational resources compared to existing test-time-scaling methods for VLMs.

## Limitations

Not stated in the fetched abstract beyond the V* VQA benchmark and Qwen3VL-4B result reported.

## Why it matters here

- **overthinking**: Indirectly relevant: it is a multimodal test-time-scaling method rather than a text-reasoning-length method, but its central diagnosis -- that unstructured reasoning chains entangling perception and reasoning produce long, disorganized contexts where errors compound -- parallels the overthinking literature's concern that undifferentiated reasoning trace growth is a source of waste and error propagation, here addressed by structurally separating what gets scaled (perception vs. reasoning) rather than penalizing length directly.

## Entities

- **Concepts**: perception-reasoning separation, asymmetric compute allocation, context compression via localized high-resolution processing
- **Methods**: SPARC (perception-reasoning circuit separation), explicit visual search
- **Datasets**: V* (VQA benchmark)

Tags: `test-time-scaling`, `vision-language-models`, `perception-reasoning-separation`, `context-compression`

---

Record id: `title:07505639ca4d10d4`
