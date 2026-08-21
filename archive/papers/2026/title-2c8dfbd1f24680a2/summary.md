<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Retrieval-of-Thought: Efficient Reasoning via Reusing Thoughts

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10009010>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Retrieval-of-Thought stores prior reasoning as a graph of composable thought steps and, at inference, retrieves and traverses it to assemble a problem-specific template that shortens the model's generated reasoning without retraining.

## Problem

Long reasoning traces buy accuracy but inflate latency and cost at inference. Much of the length is redundant re-derivation: models re-explore reasoning steps that they, or the corpus, have already worked out for similar problems. The open question the paper takes up is whether that prior reasoning can be reused as structured guidance at inference time, rather than being regenerated from scratch per query.

## Contributions

- A thought graph representation storing prior reasoning as composable step-level nodes with both sequential and semantic edges, allowing recombination across traces rather than whole-trace reuse
- Reward-guided traversal that assembles a per-query template from retrieved nodes at inference time
- A training-free inference-time efficiency method: up to 40% fewer output tokens, up to 82% lower latency, 3.8-59% lower cost across Qwen3 0.6B-14B
- The RoT+TI variant, which injects the template inside the model's <think> block rather than the prompt
- A measured accounting of the overhead: ~20% input-token growth against 49% output-token reduction on Qwen3-0.6B, and ~4.3% GPU memory for the graph

## Method

Prior reasoning is decomposed into discrete 'thought' steps and stored as nodes in a thought graph with two edge types: sequential edges linking consecutive steps within one trace, and semantic edges linking similar steps across traces, which is what allows recombination rather than whole-trace replay. The graph in the experiments is built from 3.34k templates drawn from the ReasonFlux-v2 dataset. At inference, query-relevant nodes are retrieved, then a reward-guided traversal walks the graph to assemble a template of steps specific to that problem. The template is injected as guidance for generation, so the model follows an outline instead of searching for one. Two injection variants: plain RoT puts the template in the prompt, RoT+TI (Thinking Intervention) places it inside the model's <think> block. Training-free — nothing about the model is updated.

## Results

Evaluated on AIME 2023/2024/2025 and AMC 2023 with Qwen3 at 0.6B, 1.7B, 4B, 8B and 14B, against CoT, CoT with self-consistency, static RAG, and Buffer of Thoughts. Headline: output tokens down up to 40%, inference latency down up to 82%, cost down 3.8-59% across model scales. The per-cell table does not support 'accuracy maintained' as a general claim. Qwen3-1.7B on AMC'23: CoT 80% at 6403 tokens, RoT 72.5% at 8478 tokens, RoT+TI 57.5% at 5955 tokens — RoT costs 7.5 points AND more tokens, and RoT+TI costs 22.5 points for a 7% token saving. Qwen3-1.7B AIME'24: 40.74% (CoT) vs 40.74% (RoT) vs 33.33% (RoT+TI). Qwen3-0.6B AIME'24: CoT 3.7%, RoT 11.11%, RoT+TI 0% at 4318 tokens. Where it works: Qwen3-4B AIME'24 improves 55.56% to 66.67% (RoT) with tokens roughly flat, and Qwen3-8B AIME'24 62.96% to 66.67%. Input tokens grow modestly — Qwen3-0.6B roughly 285 to 345 (+20%) against a 49% output-token drop (9719 to 4932). Memory overhead of the graph is about 4.3% of GPU memory on A100. The pattern across sizes is that the largest token savings come from RoT+TI on small models, which is also where accuracy falls hardest.

## Limitations

The authors' own discussion notes smaller models benefit more, attributing it to instruction-following: larger models have had more RL that amplifies exploration and reduces adherence to an externally supplied template. Read against the table, that framing understates the cost — for the small models where the template is followed most tightly, following it can drive accuracy to 0% (Qwen3-0.6B, AIME'24, RoT+TI). The token/latency/cost reductions are reported as 'up to' figures and are not simultaneous with accuracy preservation in the same cell. The thought graph is built from a mathematics template corpus and evaluated only on competition mathematics, where problems resemble each other enough for step reuse to be plausible; nothing establishes it on domains with less repetitive structure. Retrieval and traversal add their own compute and memory, counted here as ~4.3% GPU memory but not folded into the reported cost savings in a way the summary makes checkable.

## Why it matters here

- **overthinking**: On topic, and it isolates one specific source of excess length: redundant re-derivation of steps already worked out elsewhere. That is a different diagnosis from the usual one (the model does not know when to stop) and implies a different remedy — supply the outline rather than penalize the length — and it needs no retraining, which makes it composable with the RL-based methods the group tracks. The result worth carrying forward is not the headline but the shape of the tradeoff in the table: guidance strong enough to cut tokens meaningfully (RoT+TI on small models) is also strong enough to destroy accuracy, dropping Qwen3-1.7B on AMC'23 from 80% to 57.5% and Qwen3-0.6B on AIME'24 to 0%. The authors' explanation — larger models have had RL that reduces adherence to external templates — is a useful hypothesis for why template-injection methods and RL-trained reasoners may not compose well as models scale.

## Entities

- **Concepts**: [Overthinking](../../../../wiki/concepts/overthinking.md), Redundant Exploration, Thought Reuse, [Retrieval-Augmented Reasoning](../../../../wiki/concepts/retrieval-augmented-reasoning.md), [Accuracy-Efficiency Tradeoff](../../../../wiki/concepts/accuracy-efficiency-tradeoff.md), [Test-Time Compute Scaling](../../../../wiki/concepts/test-time-compute-scaling.md)
- **Methods**: Retrieval-of-Thought (RoT), thought graph, reward-guided traversal, Thinking Intervention, retrieval-augmented generation, Buffer of Thoughts, chain-of-thought, [self-consistency](../../../../wiki/methods/self-consistency.md)
- **Datasets**: AIME 2023, [AIME 2024](../../../../wiki/datasets/aime-2024.md), [AIME 2025](../../../../wiki/datasets/aime-2025.md), AMC 2023, ReasonFlux-v2 template corpus

Tags: `overthinking`, `efficient-reasoning`, `retrieval`, `thought-graph`, `training-free`, `inference-efficiency`, `test-time-compute`

---

Record id: `title:2c8dfbd1f24680a2`
