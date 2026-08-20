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

Proposes SPARC, a two-stage vision-language model pipeline that separates visual search from reasoning to make test-time scaling of visual grounding more modular and token-efficient.

## Problem

In vision-language models, unstructured visual reasoning chains entangle perception and reasoning into long, disorganized contexts, so small perceptual mistakes cascade into wrong answers.

## Contributions

- Proposes SPARC, a two-stage pipeline that first performs explicit visual search to localize question-relevant image regions, then conditions reasoning on those regions
- Enables independent test-time scaling of the perception and reasoning stages with separately adjustable compute
- Reduces visual token counts through compressed, localized contexts

## Method

Separates visual perception from reasoning into two explicit stages: an initial visual search stage localizes the image regions relevant to the question, and a second stage performs reasoning conditioned only on those localized regions rather than the full unstructured visual context. This modularity lets each stage's test-time compute be scaled or optimized independently.

## Results

Improves Qwen3VL 4B on the V* VQA benchmark by 6.7 points; surpasses competing visual-grounding approaches by 4.6 points in out-of-distribution settings; achieves these results with a 200x lower token budget than baseline methods.

## Limitations

Only summarized from the poster/abstract page; details on failure modes, model sizes beyond Qwen3VL 4B, and generalization limits were not available from the summarized source.

## Why it matters here

- **overthinking**: Only tangentially related: this is about VLM architecture and token-efficient visual grounding, separating perception from reasoning to cut visual token budget. It matched on the generic phrase 'test-time scaling' but does not address chain-of-thought reasoning length, when a model should stop textual reasoning, or the accuracy/efficiency tradeoff of longer thinking that the topic tracks.

## Entities

- **Concepts**: perception-reasoning separation, visual grounding, modular test-time compute allocation
- **Methods**: SPARC, two-stage perception-reasoning pipeline, visual search / grounding
- **Datasets**: V* VQA benchmark

Tags: `vlm`, `visual-grounding`, `test-time-scaling`, `perception`, `token-efficiency`

---

Record id: `title:07505639ca4d10d4`
