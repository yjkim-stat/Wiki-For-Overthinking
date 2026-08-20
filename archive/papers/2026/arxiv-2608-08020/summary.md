<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Thought-Level Beam Search for Reasoning

- **Authors**: Lijie Yang, Hongyin Luo, Jiawei Zhao, Tri Dao, Ravi Netravali
- **Venue**: cs.AI
- **Published**: 2026-08-08
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.08020>
- **PDF**: <https://arxiv.org/pdf/2608.08020v2>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-evaluation 0.25, reasoning-faithfulness 0.25, reasoning-training 0.40, test-time-scaling 0.25

## In one line

Reformulates test-time reasoning as compute allocation over partial trajectories under a hardware budget, and runs a zero-sum beam search over reasoning steps that prunes weak traces and immediately re-spends the freed capacity by branching from high-scoring prefixes.

## Problem

Parallel sampling treats traces as independent trials, so the vast majority of a large budget goes to paths that will be wrong, and one B300 needs hours to complete 512 traces for a single AIME-2025 problem while still failing the hardest instances. The two existing escapes each fail differently: unmanaged sampling saturates KV-cache memory and induces severe queueing, while subtractive pruning frees memory but never replaces the terminated traces, so concurrency decays and the GPU idles -- and, more fundamentally, pruning alone leaves the output distribution unchanged. The question has shifted from how much compute to spend to where to put it.

## Contributions

- Test-time reasoning stated as a constrained compute-allocation problem over a dynamic population of partial trajectories, with the budget as a hard cap on concurrent traces and KV-cache footprint
- Thought-level beam search: periodic tournaments that prune the bottom-K and branch the top-K, holding the active pool at exactly capacity
- A decoupled scheduler/tree architecture that stops memory-pressure evictions from corrupting the search policy
- An evaluation that holds the scorer fixed against a pruning baseline, so the measured difference is attributable to search topology rather than to a better signal

## Method

Each trajectory is a sequence of thoughts separated by double newlines, and every trace carries a running score from a scorer applied to the last-layer hidden state at each step boundary. Every check interval, a tournament ranks all active traces: at capacity it prunes the K lowest and branches the K highest, spawning children that inherit the parent's KV-cache by prefix sharing, so pruning and branching are paired identically and the active count stays exactly C -- a strict zero-sum memory invariant. Two constraints stop the obvious failure modes. A warmup threshold delays all scoring and checkpointing until a trace has generated enough tokens, because early reasoning is incomplete and the internal signals are noisy, and an eligibility rule requires a trace to have generated enough tokens since its own creation, which prevents cascading branch explosions from immature children. The systems half is the part that is not obvious. Under memory pressure the serving engine preempts running traces, and if the search observes those evictions the effective active count drops below capacity, triggering repeated under-capacity branching from the single top trace -- a feedback loop that concentrates all compute on one prefix and collapses solution quality. Gambit therefore keeps two views: a scheduler view tracking which traces hold physical KV blocks, and a tree view tracking the logical topology, in which an evicted trace becomes a ghost trace that generates nothing and holds no memory but stays logically active. Capacity checks read the tree view, so the tournament always executes a balanced prune-and-branch swap and ghost traces are pruned only when they naturally fall to the bottom. Final answers are aggregated by score-weighted majority vote with a position weighting that favours confidence in later steps. The evaluation uses the same off-the-shelf two-layer MLP hidden-state scorer as the STEP pruning baseline, and holds every tournament hyperparameter constant across all benchmarks and models: capacity 256, swap size 16, check interval 200 tokens, warmup 12,000 tokens.

## Results

The motivating measurement is the largest number in the paper and the least representative: pausing 64 parallel traces midway on one hard AIME-2025 problem, ranking them, and branching 64 continuations exclusively from the top-ranked prefix lifts pass@1 from 6.2 to 87.5 percent at roughly half the token budget, with a second problem going from 1.6 to 39.1. At scale the gains are real and much smaller. Against SC@256 across three models and five benchmarks, Gambit improves accuracy in every cell: on Qwen3-4B-Thinking, HMMT-24 rises 50.8 to 65.0 and GPQA-Diamond 68.2 to 70.2; on DeepSeek-R1-8B, HMMT-24 rises 55.8 to 65.6; on Phi-4-reasoning-plus, HMMT-25 rises 73.3 to 75.8. Against the pruning-only STEP baseline sharing the identical scorer -- the comparison that isolates the search topology -- the lifts are +3.3 on AIME-25 and +6.7 on HMMT-24 for the 4B model, +2.5 on AIME-25 for the 8B, and +1.6 on HMMT-24 for Phi-4. Token consumption falls sharply against parallel sampling, by 68.5 percent on Phi-4/HMMT-25 (1.75M against 5.56M) and 60.6 percent on Qwen3-4B/HMMT-24. Hardware utilisation is where the systems argument lands: average GPU memory 81.6 percent at 3K tokens/s for Gambit, against 88.5 percent at 1.5K for parallel sampling and 88.8 percent at 2.3K for pruning, with parallel sampling inflating latency roughly threefold; completed-trace throughput roughly doubles on AIME-26 across all three models.

## Limitations

The paper has no limitations section and its central claim is stated more strongly than the table supports. 'Strictly dominates existing baselines' does not hold cell by cell: DeepConf beats Gambit on GPQA for DeepSeek-R1-8B (68.7 against 68.2), and the two tie at 90.0 on AIME-25 for the 4B model, which the text acknowledges as matching rather than beating. Several improvements are one or two problems -- AIME and HMMT sets are 30 problems each, so a 3.3-point gain is a single item, and the archive's standing caution about that resolution applies to most of the per-benchmark deltas here. The motivating 14x figure is a single hand-picked hard problem and should not be read as a method result. On scope: one GPU type and one serving engine, three models from 4B to 14B, mathematics plus one science benchmark, and the scorer is inherited rather than studied -- which is the right control for the search claim but means the whole approach rests on a hidden-state signal whose reliability this paper does not measure. The warmup threshold of 12,000 tokens is a large commitment before any allocation decision is made and its sensitivity is deferred to an appendix. Finally, branching from a shared prefix makes the resulting traces statistically dependent, so the score-weighted majority vote is aggregating over a correlated population; nothing here quantifies what that does to the vote.

## Why it matters here

- **reasoning-training**: Bears on the archive's open question of whether RLVR moves a policy outside the base model's reachable set or redistributes mass within it. This paper redistributes mass within it deliberately and at inference time only -- no weights change -- and reports that concentrating compute on a well-chosen prefix takes one AIME problem from 6.2 to 87.5 percent pass@1. That is evidence about how much of an RL-trained model's apparent ceiling is an allocation artefact rather than a capability bound, and it is measured under a fixed hardware budget, which the pass@k literature here never controls for. It also supplies a cleanly isolated comparison of the kind the archive keeps asking for: the same hidden-state scorer under pruning and under prune-and-branch, so the difference is the allocation policy and not the signal.

## Entities

- **Concepts**: [compute allocation](../../../../wiki/concepts/compute-allocation.md), [test-time compute](../../../../wiki/concepts/test-time-compute.md), partial trajectory, prefix quality, hardware utilization, [KV cache](../../../../wiki/concepts/kv-cache.md), zero-sum allocation, [trajectory diversity](../../../../wiki/concepts/trajectory-diversity.md), answer aggregation
- **Methods**: [beam search](../../../../wiki/methods/beam-search.md), [self-consistency](../../../../wiki/methods/self-consistency.md), [prefix caching](../../../../wiki/methods/prefix-caching.md), [Monte Carlo tree search](../../../../wiki/methods/monte-carlo-tree-search.md), [process reward model](../../../../wiki/methods/process-reward-model.md), [linear probe](../../../../wiki/methods/linear-probe.md), [vLLM](../../../../wiki/methods/vllm.md), score-weighted majority vote
- **Datasets**: [AIME 2025](../../../../wiki/datasets/aime-2025.md), [AIME 2026](../../../../wiki/datasets/aime-2026.md), [HMMT](../../../../wiki/datasets/hmmt.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md)

Tags: `test-time-scaling`, `beam-search`, `serving`, `kv-cache`, `compute-allocation`

## Abstract

Test-time compute scaling is a primary driver of performance in large reasoning models (LRMs), but extreme inefficiency bounds current approaches, shifting the critical question from \emph{how much} compute to spend, to \emph{where} to allocate it. We formalize test-time reasoning as a constrained compute allocation problem over partial trajectories. Under a fixed hardware budget, existing paradigms fail to actively allocate the compute to the most promising partial progress: traditional parallel sampling treats traces independently and induces severe memory bottlenecks, while subtractive pruning starves hardware and fails to actively and sufficiently shift the output distribution. To overcome this dichotomy, we introduce Gambit, an inference algorithm that executes \emph{thought-level beam search}. By periodically pruning unpromising trajectories and immediately branching from high-quality prefixes, Gambit dynamically concentrates compute onto the most promising reasoning traces via a light-weight scorer probing hidden states while maintaining continuous high hardware utilization. Extensive evaluations across multiple models and benchmarks demonstrate that Gambit strictly dominates existing baselines. Under identical hardware constraints, our method yields up to a +6.7\% absolute accuracy gain on HMMT-24 and +3.3\% on AIME-25 over pruning baselines, delivers $>2\times$ higher throughput on trace completion, and reduces total token consumption by up to 68.5\% relative to standard parallel sampling.

---

Record id: `arxiv:2608.08020`
