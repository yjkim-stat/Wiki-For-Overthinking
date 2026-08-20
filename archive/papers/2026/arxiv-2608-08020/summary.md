<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Thought-Level Beam Search for Reasoning

- **Authors**: Lijie Yang, Hongyin Luo, Jiawei Zhao, Tri Dao, Ravi Netravali
- **Venue**: cs.AI
- **Published**: 2026-08-08
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.08020>
- **PDF**: <https://arxiv.org/pdf/2608.08020v2>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## In one line

Introduces Gambit, an inference algorithm that formulates test-time reasoning as thought-level beam search, periodically pruning weak reasoning traces and branching new ones from high-quality prefixes to concentrate a fixed hardware budget on the most promising partial reasoning.

## Problem

Under a fixed hardware/memory budget, existing test-time compute-scaling paradigms fail to actively reallocate compute toward the most promising partial reasoning trajectories: parallel sampling treats traces independently and hits severe memory bottlenecks, while subtractive pruning frees capacity but leaves it idle (hardware starvation) instead of redirecting it, so the critical question shifts from how much compute to spend to where to allocate it.

## Contributions

- Formalizes test-time reasoning as a constrained compute-allocation problem over partial trajectories under a fixed hardware budget.
- Introduces Gambit, an inference algorithm performing periodic thought-level beam search: prune the lowest-scoring traces and immediately branch new children from the highest-scoring prefixes via KV-cache sharing.
- Introduces a decoupled Scheduler View / Tree View architecture with 'ghost traces' to prevent a pathological under-capacity feedback loop that would collapse the search onto a single prefix under memory pressure.
- Empirically shows Gambit strictly dominates parallel sampling and subtractive-pruning baselines (Self-Consistency, Slim-SC, DeepConf, STEP) in accuracy, token consumption, and hardware utilization across three model architectures and multiple math/science reasoning benchmarks.

## Method

Formulates test-time reasoning as maximizing the probability of the ground-truth answer subject to a hard capacity constraint C on concurrently active traces (peak compute/KV-cache footprint). Gambit runs C parallel traces and, every Delta tokens ('check interval'), ranks all active traces by a lightweight scorer f_theta applied to hidden states (average cumulative score, using a warmup threshold w tokens before a trace is eligible to branch); it then performs a zero-sum swap: prunes the K lowest-scoring traces and branches K new children from the K highest-scoring eligible prefixes via KV-cache/prefix sharing, keeping the active pool at exactly C traces throughout generation. A Decoupled Memory Management scheme separates a Scheduler View (which physical KV-cache blocks currently exist, evicting the lowest-ranked trace under memory pressure) from a Tree View (the logical search topology, where an evicted trace becomes an inactive 'ghost trace' that still counts toward capacity until it is naturally pruned), preventing search decisions from being distorted by transient memory pressure. Final answers are aggregated via a score-weighted majority vote. Implemented atop vLLM.

## Results

At N=256 sampled traces on a single NVIDIA B300 GPU: on Qwen3-4B-Thinking, Gambit reaches 90.0% on AIME-25 (matching the calibrated DeepConf baseline) while using fewer tokens (3.07M vs. SC's 6.02M, a 49.0% reduction), and outperforms STEP pruning by +3.3% on AIME-25/HMMT-24, reaching 88.3% AIME-26, 65.0% HMMT-24 (+6.7% over STEP), and 67.5% GPQA (+2.6% over STEP). On DeepSeek-R1-8B, Gambit gives +2.5% AIME-25 over STEP (85.8%) with a 37.7% token reduction. On Phi-4-reasoning-plus-14B, Gambit gives the largest efficiency gain, reducing tokens by up to 68.5% on HMMT-25 (1.76M vs. SC's 4.24M) while reaching 90.0% AIME-26 and 77.1% GPQA. Gambit delivers over 2x higher completed-trace throughput than SC (e.g., 0.216 vs. 0.098 traces/sec on Qwen3-4B, AIME-26) and more than 2x faster wall-clock latency than parallel sampling, remaining competitive with (roughly 1.1x slower than) the faster but hardware-starved STEP baseline, with under 1% claimed system overhead.

## Limitations

No dedicated limitations section is stated; the empirical evaluation is confined to a single hardware setup (one 275GB NVIDIA B300 GPU) via vLLM and three open-weight architectures (Qwen3-4B-Thinking, DeepSeek-R1-8B, Phi-4-reasoning-plus-14B). The main comparison isolates the search-topology contribution by reusing the identical off-the-shelf 2-layer MLP scorer from prior work (STEP), so results depend on that scorer's reliability. The paper notes that its large total-token savings do not translate proportionally into latency reductions, because branching increases the frequency of long-running traces (a rightward shift in the total sequence-length distribution) rather than shortening individual traces.

## Why it matters here

- **overthinking**: Directly targets the test-time compute allocation problem central to this topic: rather than controlling the length of a single chain-of-thought, Gambit reallocates a fixed compute budget across many partial reasoning trajectories in real time, cutting total token consumption by up to 68.5% relative to standard parallel sampling while improving accuracy (+6.7% on HMMT-24, +3.3% on AIME-25 over pruning baselines) — a concrete demonstration that naive test-time scaling wastes compute on unpromising reasoning and that smarter allocation improves the accuracy/efficiency tradeoff.

## Entities

- **Concepts**: constrained compute allocation over partial reasoning trajectories, zero-sum reallocation policy for a fixed-capacity trace pool, decoupled scheduler view vs. tree (ghost-trace) view for memory management, thought-level (vs. token-level) beam search
- **Methods**: Gambit (thought-level beam search), STEP hidden-state scorer, prefix-caching / KV-cache-sharing branching, Self-Consistency (baseline), [Slim-SC (baseline)](../../../../wiki/methods/slim-sc-baseline.md), DeepConf (baseline), STEP subtractive pruning (baseline)
- **Datasets**: [AIME 2025](../../../../wiki/datasets/aime-2025.md), [AIME 2026](../../../../wiki/datasets/aime-2026.md), HMMT 2024, [HMMT 2025](../../../../wiki/datasets/hmmt-2025.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md)

Tags: `test-time-compute`, `beam-search`, `reasoning`, `inference-efficiency`, `pruning`, `kv-cache`, `vllm`

## Abstract

Test-time compute scaling is a primary driver of performance in large reasoning models (LRMs), but extreme inefficiency bounds current approaches, shifting the critical question from \emph{how much} compute to spend, to \emph{where} to allocate it. We formalize test-time reasoning as a constrained compute allocation problem over partial trajectories. Under a fixed hardware budget, existing paradigms fail to actively allocate the compute to the most promising partial progress: traditional parallel sampling treats traces independently and induces severe memory bottlenecks, while subtractive pruning starves hardware and fails to actively and sufficiently shift the output distribution. To overcome this dichotomy, we introduce Gambit, an inference algorithm that executes \emph{thought-level beam search}. By periodically pruning unpromising trajectories and immediately branching from high-quality prefixes, Gambit dynamically concentrates compute onto the most promising reasoning traces via a light-weight scorer probing hidden states while maintaining continuous high hardware utilization. Extensive evaluations across multiple models and benchmarks demonstrate that Gambit strictly dominates existing baselines. Under identical hardware constraints, our method yields up to a +6.7\% absolute accuracy gain on HMMT-24 and +3.3\% on AIME-25 over pruning baselines, delivers $>2\times$ higher throughput on trace completion, and reduces total token consumption by up to 68.5\% relative to standard parallel sampling.

---

Record id: `arxiv:2608.08020`
