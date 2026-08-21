<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ThreadWeaver: Adaptive Threading for Efficient Parallel Reasoning in Language Models

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/65330>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Trains Qwen3-8B to split its chain of thought into concurrently decoded threads that spawn and join, so the critical path is shorter than a sequential trace of the same total length, using a trie-based rollout that runs on stock autoregressive inference engines.

## Problem

Test-time compute scaling buys accuracy with sequential decoding, and sequential decoding sets latency by the length of the trace. Prior parallel-reasoning schemes lose accuracy relative to sequential models of the same size and typically need a bespoke inference engine to execute their branching, which blocks deployment. The open question is whether a model can be trained to decide for itself which parts of a solution are independent, without giving up accuracy and without a custom serving stack.

## Contributions

- A spawn/join threading format (<Parallel>, <Outlines>, <Thread>, reducer) in which the model itself decides what to parallelize, trained end to end rather than imposed by a planner.
- A trie-based rollout with ancestor-only attention masking that makes parallel reasoning trainable and servable on any off-the-shelf autoregressive inference engine, without KV-cache modifications.
- P-GRPO, an RL objective adding an acceleration bonus proportional to the fraction of tokens removed from the critical path, paid only on correct trajectories and clipped to stay small relative to correctness.
- A two-stage parallel trajectory generator producing parallel CoT SFT data from sequential traces.
- Six-benchmark evaluation reporting an accuracy/latency Pareto frontier against sequential GRPO, Multiverse and Parallel-R1.

## Method

The model emits <Parallel> blocks containing an <Outlines> section that declares independent sub-tasks and several <Thread> sections that are decoded concurrently; at the join point a designated reducer thread aggregates the child outputs and returns them to the parent. Training data comes from a two-stage parallel trajectory generator that converts sequential CoT into this format for supervised fine-tuning. The trie-based rollout is what removes the need for a special engine: every <context, completion> unit that inference would issue is extracted and inserted into a token-level prefix tree, and an ancestor-only attention mask lets a thread see its own ancestors but not its siblings, so shared prefixes are computed once while cross-thread leakage is prevented — all without touching KV caches, so any off-the-shelf autoregressive engine can serve it. P-GRPO then adds a parallelization-aware term to the RL reward: correctness is a binary indicator, and an acceleration bonus min(rho * eta(s), rho_clip) is paid only on correct trajectories, where eta(s) = 1 - L_longest / L_total is the fraction of tokens taken off the critical path. rho = 0.5 and rho_clip = 0.2 keep the bonus small relative to correctness, which is the guard against the model manufacturing redundant branches to collect it.

## Results

Qwen3-8B base, six math benchmarks, against a sequential GRPO baseline of the same size: AIME24 79.9% vs 78.3%, AIME25 60.5% vs 61.6%, AMC23 92.3% vs 92.6%, MATH500 91.4% vs 91.8%, Minerva Math 43.7% vs 43.9%, OlympiadBench 63.5% vs 65.0%; average 71.9%. Against prior parallel methods on AIME24 the gap is large: Multiverse 53.8%, Parallel-R1 19.4%. Token-latency speedup, where token latency is defined as the token count of the longest thread (the critical path) rather than total tokens generated: Minerva Math 1.53x, MATH500 1.23x, OlympiadBench 1.21x, AMC23 1.16x, AIME24 1.14x average with a 1.47x maximum, AIME25 1.03x. Measured wall-clock speedup was 1.14x on 50 MATH problems with parallelization across four GPUs.

## Limitations

The paper states that token-latency speedups are an upper bound on end-to-end runtime, since scheduling, communication, kernel launches and imperfect hardware utilization are excluded — the one wall-clock measurement reported (1.14x on MATH500) is well below that benchmark's 1.23x token-latency figure. It also acknowledges the reward-hacking risk of spawning redundant branches to earn the acceleration bonus, reporting that this was not observed and crediting SFT priors plus a 40k token cap rather than any mechanism that prevents it. And it notes that SFT data quality dominates: RL adds little when the SFT distribution is poorly matched, so the method's transferability rests on the trajectory generator. Two things the reader should notice on top of these. First, 'matches the accuracy of sequential models' is generous to the paper's own table — ThreadWeaver is *below* the sequential baseline on five of six benchmarks (AIME25 -1.1, OlympiadBench -1.5, AMC23 -0.3, MATH500 -0.4, Minerva -0.2) and above on only AIME24 (+1.6), so the honest reading is a small average accuracy cost bought back as latency. Second, the headline '1.53x' is the best of six benchmarks and the outlier; the median is about 1.19x and AIME25 — the hardest benchmark, where latency matters most — gets 1.03x, essentially nothing, which the paper attributes to the model doing more self-reflection there. Latency is also not compute: threads are decoded concurrently on separate hardware, so total token count is unchanged or higher and the four-GPU wall-clock setup buys a 1.14x latency win with roughly 4x the serving resources.

## Why it matters here

- **overthinking**: This paper is on the topic's efficiency axis but changes which quantity is being economised, and that distinction is worth recording. Every other efficient-reasoning method the group tracks reduces the *number of tokens* the model thinks for; ThreadWeaver reduces the *wall-clock depth* of the thinking while leaving total tokens unchanged or higher, by decoding independent parts of the trace concurrently. So it is not a treatment for overthinking — a model that reasons redundantly still reasons redundantly here, just in parallel — and its acceleration reward explicitly pays for restructuring rather than for brevity. It belongs in the topic as the parallel-compute corner of the accuracy/efficiency tradeoff, and it is a useful control: it shows how much of the latency cost of long reasoning is intrinsic sequential dependency rather than length, and the answer is modest (median about 1.19x critical-path speedup, 1.14x wall-clock on four GPUs). Its own numbers also supply a caution the group should reuse when reading efficiency claims — the headline 'matches sequential accuracy' covers a table where the sequential baseline wins on five of six benchmarks, so the accuracy is matched on average and lost in detail. And the correlation between where the method helps least (AIME25, 1.03x) and where the model self-reflects most is the one place it touches overthinking directly: reflection is inherently sequential, so the traces most in need of shortening are the ones parallelism cannot shorten.

## Entities

- **Concepts**: Parallel Reasoning, Critical Path Latency, [Test-Time Compute Scaling](../../../../wiki/concepts/test-time-compute-scaling.md), [Accuracy-Efficiency Pareto Frontier](../../../../wiki/concepts/accuracy-efficiency-pareto-frontier.md), [Reward Hacking](../../../../wiki/concepts/reward-hacking.md), Adaptive Reasoning Structure
- **Methods**: ThreadWeaver, P-GRPO, [GRPO](../../../../wiki/methods/grpo.md), trie-based rollout, ancestor-only attention mask, two-stage parallel trajectory generator, Multiverse, Parallel-R1
- **Datasets**: [AIME 2024](../../../../wiki/datasets/aime-2024.md), [AIME 2025](../../../../wiki/datasets/aime-2025.md), AMC 2023, MATH500, [Minerva Math](../../../../wiki/datasets/minerva-math.md), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md)

Tags: `parallel-reasoning`, `inference-latency`, `test-time-compute`, `reinforcement-learning`, `grpo`, `chain-of-thought`, `efficient-reasoning`, `llm`

---

Record id: `title:c65838fd39e8d183`
