<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Hidden States as Early Signals: Step-level Trace Evaluation and Pruning for Efficient Test-Time Scaling

- **Authors**: Zhixiang Liang, Beichen Huang, Zheng Wang, Minjia Zhang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1336/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1336.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1336
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

STEP trains a lightweight 2-layer-MLP step scorer on reasoning-model hidden states at step boundaries to evaluate parallel-reasoning trace quality with near-zero overhead, and pairs it with a GPU-memory-triggered (not confidence-threshold or fixed-schedule) pruning mechanism that eliminates the KV-cache waiting-queue bottleneck identified as the dominant source of end-to-end latency in parallel test-time scaling -- cutting latency 45-70% versus self-consistency while improving accuracy 0.4-7.5 points across three models and six benchmarks.

## Problem

Parallel test-time scaling (self-consistency and its variants) improves LLM reasoning accuracy but at prohibitive latency, because prior trace-pruning methods rely on unreliable quality signals (surface-level textual similarity, which does not indicate reasoning redundancy since different valid paths can converge to the same answer; or model confidence, which suffers overconfidence/miscalibration on factually false outputs) and overlook a more fundamental system-level bottleneck: as multiple long traces' KV caches accumulate, GPU memory saturates and the inference engine preempts traces into a waiting queue, and this waiting time (measured at ~40% of end-to-end latency) -- not token generation alone -- is the dominant inefficiency.

## Contributions

- an identification, via time-breakdown profiling, that KV-cache-driven trace preemption and waiting -- not token generation alone -- is the dominant source of end-to-end latency in parallel test-time scaling (~40% of total time under self-consistency)
- STEP, a lightweight (2-layer MLP) step scorer trained on hidden states at reasoning-step boundaries that reliably discriminates correct from incorrect traces earlier and more accurately than token-level confidence, at negligible computational overhead versus a full Process Reward Model
- a GPU-memory-triggered pruning mechanism that ties pruning decisions directly to memory saturation, eliminating the waiting queue entirely rather than only shortening it, unlike confidence- or similarity-based pruning schedules
- state-of-the-art accuracy-latency trade-offs across three models and six benchmarks (mathematical, scientific, code-equivalence, and logical-reasoning domains), with 45-70% latency reduction and simultaneous accuracy improvement versus self-consistency

## Method

Trains a lightweight step scorer f_theta (a 2-layer MLP) that maps the last-layer hidden state of each reasoning step's boundary token (the token whose text contains '\n\n') to a correctness-probability score, supervised with trace-level correctness labels propagated as pseudo-labels to every step within the trace, using a weighted binary cross-entropy loss compensating for the class imbalance that arises because incorrect traces tend to be longer (more negative step instances even in a trace-balanced dataset). During generation, each trace's running average of step scores gives a trace-level score, which is more stable than the latest step score alone since it captures reasoning-quality evolution rather than being sensitive to individual-step variance. Pruning is triggered not by a fixed confidence threshold or wall-clock schedule but by GPU memory saturation: whenever the KV cache for the next decoding step cannot be scheduled (memory is full), the trace with the lowest current average score is immediately pruned and its KV cache released, eliminating the waiting-queue/preemption-resumption cycle entirely rather than merely shortening it. Once all traces have completed or been pruned, a final answer is produced via weighted majority voting using each surviving trace's final trace-level score as its vote weight.

## Results

Across three reasoning models (Qwen3-4B-Thinking-2507, DeepSeek-R1-0528-Qwen3-8B, Phi-4-reasoning-plus-14B) and six benchmarks (AIME-25, HMMT-24/25, GPQA-Diamond, EquiBench, DivLogicEval) at sampling budget N=64, STEP reduces end-to-end inference latency by 45-70% on average versus self-consistency while improving accuracy by +0.4 to +7.5 percentage points, and consistently outperforms Slim-SC (similarity-based pruning) and DeepConf (confidence-based pruning) in accuracy at comparable or lower latency across nearly all benchmark-model combinations -- e.g. on HMMT-25, STEP improves accuracy over self-consistency by 5.0/3.3/0.8 points for the three models respectively. Latency-scaling comparisons across sampling budgets (N=1,16,32,64) show STEP achieves a consistently superior accuracy-latency frontier: e.g. on Qwen3-4B-Thinking-2507/HMMT-25, STEP reaches 70% accuracy using ~40% of the latency self-consistency needs to reach only 65%; on Phi-4-reasoning-plus/HMMT-24, STEP achieves 58.3% accuracy in 630s versus self-consistency's 2405s for comparable performance, a 3.8x speedup. A detailed waiting-vs-decoding time profiling (DeepSeek-R1-0528-Qwen3-8B, HMMT-25, 64 traces) confirms the mechanism: self-consistency spends 1526s waiting plus 1256s decoding; DeepConf and Slim-SC reduce waiting time (69+194s and 1155s respectively) since pruning alleviates memory pressure, but neither ties its pruning decisions explicitly to GPU memory state, so waiting time is not fully eliminated; STEP's memory-triggered pruning reduces waiting time to zero, with 1024s of decoding as the entire end-to-end cost -- directly confirming that explicit memory-aware triggering, not token-count reduction alone, is what fully removes the waiting-queue bottleneck. The step scorer's discriminative ranking ability (pairwise RankAcc between correct/incorrect trace pairs, evaluated at varying fractions of trace completion) consistently exceeds token-level confidence (as used by DeepConf) at every truncation percentage, and improves steadily as more reasoning steps become visible -- demonstrating that hidden states encode reasoning-quality information reliably well before a trace completes, not just at the end. Compared directly against a much larger, purpose-built verifier (Qwen2.5-Math-PRM-7B, a full 7B-parameter Process Reward Model requiring a separate full forward pass per trace) on the same fixed set of 64 traces, STEP-weighted voting outperforms PRM-weighted voting on all three tested benchmarks by up to 4.2 percentage points (e.g. HMMT-25/DeepSeek-R1-0528-Qwen3-8B: 75.8% vs. 71.7%), despite the step scorer being a lightweight MLP trained on only 10,000 automatically-verified traces and introducing negligible (<10^-6 relative) additional FLOPs per step, versus the PRM's substantial per-trace forward-pass cost.

## Limitations

The paper does not discuss limitations explicitly in the excerpted sections; the step scorer is trained on pseudo-labels propagated from trace-level correctness (rather than genuine fine-grained step-level annotation, described as costly to obtain), which means the supervision signal at any individual step is only an approximation and the paper's own preliminary study notes discriminability strengthens as reasoning progresses (implying weaker signal quality very early in a trace). All evaluation is conducted on a single 96GB NVIDIA GH200 GPU with a modified vLLM implementation, so the specific latency-reduction magnitudes are tied to this hardware/framework configuration and its particular GPU-memory-preemption behavior.

## Why it matters here

- **overthinking**: Directly relevant as a systems-level companion to reasoning-length-focused overthinking work in this archive: it reframes the cost of extended/parallel reasoning not just in terms of tokens generated but in terms of an inference-system bottleneck (GPU-memory-driven trace preemption) that token-count-focused length-penalty or early-stopping methods do not address, and its finding that a cheap hidden-state-based scorer outperforms both token confidence and a much larger trained verifier reinforces a pattern seen elsewhere in this archive (e.g. Guided by Gut, RFS-Guard, STOP) that a model's own internal states carry more reliable quality signal than its output-level confidence.

## Entities

- **Concepts**: overthinking (via wasted parallel-reasoning compute), step-level trace scoring from hidden states, GPU-memory-triggered pruning, KV-cache waiting-queue bottleneck, weighted majority voting
- **Methods**: STEP (Step-level Trace Evaluation and Pruning), [self-consistency (SC, baseline)](../../../../wiki/methods/self-consistency-sc-baseline.md), Slim-SC (baseline, similarity-based pruning), DeepConf (baseline, confidence-based pruning), PRM-weighted voting (Qwen2.5-Math-PRM-7B, comparison)
- **Datasets**: HMMT 2012-2023 (step-scorer training data), [AIME-25](../../../../wiki/datasets/aime-2025.md), HMMT-24, [HMMT-25](../../../../wiki/datasets/hmmt25.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), EquiBench, DivLogicEval

Tags: `test-time-scaling`, `parallel-reasoning`, `mechanistic-interpretability`, `inference-systems`, `KV-cache`, `pruning`

## Abstract

Large Language Models (LLMs) can enhance reasoning capabilities through test-time scaling by generating multiple traces. However, the combination of lengthy reasoning traces with multiple sampling introduces substantial computation and high end-to-end latency. Prior work on accelerating this process has relied on similarity-based or confidence-based pruning, but these signals do not reliably indicate trace quality. To address these limitations, we propose STEP: Step-level Trace Evaluation and Pruning, a novel pruning framework that evaluates reasoning steps using hidden states and dynamically prunes unpromising traces during generation. We train a lightweight step scorer to estimate trace quality, and design a GPU memory-aware pruning strategy that triggers pruning as the GPU memory is saturated by KV cache to reduce end-to-end latency. Experiments across challenging reasoning benchmarks demonstrate that STEP reduces end-to-end inference latency by 45%–70% on average compared to self-consistency while also improving reasoning accuracy.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1336`
