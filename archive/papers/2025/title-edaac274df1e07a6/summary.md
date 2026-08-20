<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Don’t Think Longer, Think Wisely: Optimizing Thinking Dynamics for Large Reasoning Models

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/116095>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

Segments reasoning traces into thinking patterns, prunes detrimental ones, and uses the resulting optimal-vs-suboptimal pairs for preference optimization to cut reasoning length while improving accuracy.

## Problem

Large reasoning models trained with RL for final-answer accuracy often overthink, producing unnecessarily long and complex reasoning paths that waste computation and can even degrade accuracy; the paper attributes this to the model's limited ability to select the right modular reasoning strategy at the right point.

## Contributions

- A dynamic optimization framework that segments model-generated reasoning paths into distinct thinking patterns and identifies beneficial vs detrimental patterns
- A preference optimization method trained on a pairwise dataset contrasting suboptimal and optimal reasoning paths

## Method

Segments an LRM's generated reasoning path into distinct 'thinking patterns' (modular reasoning strategies), then systematically identifies which patterns are beneficial to the final answer and which are detrimental, promoting the former and removing the latter to produce shorter but sufficiently informative reasoning trajectories. These optimized trajectories are then used to build a pairwise preference dataset (suboptimal vs optimal path) for preference optimization training of the model.

## Results

Reduces attention FLOPs by up to 47% while maintaining accuracy on originally correct responses; converts a portion of originally incorrect responses to correct, yielding a 15.6% accuracy improvement with reduced length; after preference optimization, achieves up to 12% accuracy improvement and reduces token usage from approximately 5,000 to 3,000 tokens across multiple mathematical reasoning benchmarks.

## Limitations

Abstract does not name the specific benchmarks, model sizes, or baselines used; no discussion of failure modes or generalization beyond math reasoning is given.

## Why it matters here

- **overthinking**: Directly targets overthinking in LRMs: proposes a method to detect and remove detrimental reasoning patterns and shorten trajectories, reporting a 47% reduction in attention FLOPs and token usage dropping from ~5,000 to ~3,000 while accuracy improves by up to 12-15.6% on math reasoning benchmarks.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), thinking patterns, modular reasoning strategy selection, preference optimization
- **Methods**: thinking pattern segmentation, preference optimization (pairwise)
- **Datasets**: multiple mathematical reasoning benchmarks (unspecified in abstract)

Tags: `overthinking`, `reasoning-efficiency`, `preference-optimization`, `test-time-compute`, `math-reasoning`

## Abstract

Abstract While recent success of large reasoning models (LRMs) significantly advanced LLMs' reasoning capability by optimizing the final answer accuracy using reinforcement learning, they may also drastically increase the output length due to overthinking —characterized by unnecessarily complex reasoning paths that waste computation and potentially degrade the performance. We hypothesize that such inefficiencies stem from LRMs' limited capability to dynamically select the proper modular reasoning strategies, termed thinking patterns at the right position. To investigate this hypothesis, we propose a dynamic optimization framework that segments model-generated reasoning paths into distinct thinking patterns, systematically identifying and promoting beneficial patterns that improve the answer while removing detrimental ones. Empirical analysis confirms that our optimized thinking paths yield more concise yet sufficiently informative trajectories, enhancing reasoning efficiency by reducing attention FLOPs by up to 47% while maintaining accuracy for originally correct responses. Moreover, a non-trivial portion of originally incorrect responses are transformed into correct ones, achieving a 15.6% accuracy improvement with reduced length. Motivated by the improvement brought by the optimized thinking paths, we apply a preference optimization technique supported by a pairwise dataset contrasting suboptimal and optimal reasoning paths. Experimental evaluations across multiple mathematical reasoning benchmarks reveal that our method notably reduces computational overhead while simultaneously improving reasoning accuracy, achieving up to a 12% accuracy improvement and reducing token usage from approximately 5,000 to 3,000 tokens.

---

Record id: `title:edaac274df1e07a6`
