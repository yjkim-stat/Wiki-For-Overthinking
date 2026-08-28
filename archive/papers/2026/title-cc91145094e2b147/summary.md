<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Adaptive Thinking: Large Language Models Know When to Think in Latent Space

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10011708>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Sonata predicts a query's self-consistency from the last-layer hidden state at prefill and uses that prediction to set the thinking budget before the model starts reasoning.

## Problem

Raising the thinking budget improves accuracy smoothly at inference time, but the relationship between model capability, query complexity and the budget that is actually needed is poorly understood, so budgets are set uniformly across queries rather than per query. A fixed budget overspends on queries the model already answers consistently and underspends on the ones it does not.

## Contributions

- The empirical finding that lower self-consistency indicates queries needing extended thinking to reach a correct answer
- Sonata, an adapter that predicts self-consistency from last-layer hidden states at prefill, before any thinking tokens are generated
- Per-query thinking-budget allocation driven by that prediction, at close to zero inference overhead
- Demonstration that the method composes with existing CoT compression methods rather than competing with them

## Method

The paper first establishes self-consistency — the agreement among multiple sampled reasoning paths — as a proxy for whether a query needs extended thinking, observing that low self-consistency marks queries that require more thinking to reach a correct answer. Measuring self-consistency directly would require sampling several traces, which defeats the purpose, so Sonata (Self-Consistency-Guided Adapter for Thinking Allocation) trains a lightweight adapter offline on a calibration dataset to predict self-consistency from the last-layer hidden representations available during the prefilling stage, before any thinking tokens are generated. The predicted value then drives on-the-fly budget allocation for that query. The adapter is trained once, transfers across tasks, and adds close to zero inference overhead. It is orthogonal to CoT compression methods and can be stacked on them.

## Results

Across Qwen3-8B, GPT-OSS-120B, Qwen3-235B-A22B and Intern-S1-mini on AIME24, AIME25, GSM8K, MATH500 and GPQA, the paper reports either a reduction in thinking tokens at equal accuracy or an accuracy gain at equal token cost. The two published versions of the abstract state different ranges: 20%-80% token reduction and up to 5% accuracy improvement in the authors' full version, and 20%-60% token reduction and up to 2% accuracy improvement in the ICLR 2026 poster listing. Per-benchmark breakdowns are not in the abstract.

## Limitations

Not stated in the material available. A reader should notice several things. The two circulated abstracts disagree on the headline range (80% vs 60% token reduction, 5% vs 2% accuracy gain), so the larger figures should not be quoted without checking which version they come from. The adapter is trained on a calibration dataset and its transfer claim is asserted rather than quantified in the abstract. Self-consistency is a proxy for difficulty that conflates 'hard' with 'the model disagrees with itself', so a query the model is confidently and consistently wrong about will be predicted to need little thinking. The evaluation is mathematics and science QA with verifiable answers.

## Why it matters here

- **overthinking**: Directly on topic, and it attacks the decision at the earliest possible point. Where most efficient-reasoning work either trains a model to be terser or interrupts a trace once it is running, Sonata decides how much thinking a query deserves before the first thinking token, using only the prefill hidden state — so the saving costs nothing to obtain. Its contribution to the group's picture is the claim that the signal for 'this query needs more thought' is already linearly present in the last-layer representation of the question, and that its content is predicted self-consistency: the model knows in advance when its own reasoning paths will disagree. That reframes budget allocation as a calibration problem on the prompt rather than a control problem on the trace. It also reports the two-sided result the topic cares about — the same allocator either cuts tokens at fixed accuracy or raises accuracy at fixed tokens — which is evidence that uniform budgets are misallocated in both directions, not merely wasteful. The caveat worth carrying is that self-consistency cannot distinguish a hard query from one the model is consistently wrong about.

## Entities

- **Concepts**: Thinking budget allocation, Self-consistency as a difficulty proxy, [Compute-optimal inference](../../../../wiki/concepts/compute-optimal-inference.md), Prefill-stage prediction, Latent-space probing, [Adaptive test-time compute](../../../../wiki/concepts/adaptive-test-time-compute.md), CoT compression
- **Methods**: Sonata, Self-Consistency-Guided Adapter for Thinking Allocation, [Self-consistency](../../../../wiki/methods/self-consistency.md), Hidden-state probing adapter, Qwen3-8B, GPT-OSS-120B, Qwen3-235B-A22B, Intern-S1-mini
- **Datasets**: [AIME24](../../../../wiki/datasets/aime-2024.md), [AIME25](../../../../wiki/datasets/aime-2025.md), [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH500](../../../../wiki/datasets/math500.md), [GPQA](../../../../wiki/datasets/gpqa.md)

Tags: `adaptive-thinking`, `thinking-budget`, `self-consistency`, `test-time-compute`, `latent-space`, `efficient-reasoning`, `probing`

---

Record id: `title:cc91145094e2b147`
