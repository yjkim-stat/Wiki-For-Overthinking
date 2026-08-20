<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# CoBa: Cost-Effective Test-Time Scaling via Compute-Balanced Routing

- **Authors**: Yan Zhou, Yue Ouyang, Kaiyang Zheng, Suncheng Xiang
- **Venue**: cs.AI
- **Published**: 2026-08-07
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.07424>
- **PDF**: <https://arxiv.org/pdf/2608.07424v2>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

CoBa treats test-time scaling as a compute-allocation problem and routes cheap answer-agreement evidence versus a small number of strong-verifier calls, reaching majority-voting/self-evaluation-level accuracy on math and symbolic reasoning benchmarks while using roughly half the parameter-weighted tokens.

## Problem

Test-time scaling for LLM reasoning is usually implemented by spending more compute along a single fixed axis (more samples, longer chains of thought, or a stronger evaluator), but under a fixed inference budget these choices compete for the same compute, and prior methods do not explicitly decide, per example, whether the next unit of compute is better spent generating, verifying, or stopping.

## Contributions

- Formulates test-time reasoning as a unified compute-allocation problem: at each decision step a system must choose whether the next unit of compute is spent on sampling another candidate, applying lightweight or strong verification, or stopping.
- Introduces CoBa, a reproducible local routing policy with lightweight and strong verification tiers that first buys a small amount of candidate diversity, scores candidates cheaply, and routes only uncertain or high-value candidates to stronger (more expensive) verification.
- Provides controlled replay experiments over a shared candidate pool (offline replay protocol) showing CoBa-Routed-Strong reaches the accuracy region of much more expensive sampling (best-of-16) and evaluator-scaling (self-evaluation weighted voting) baselines while using substantially fewer parameter-weighted tokens, with ablations and paired significance tests explaining when routing helps.

## Method

CoBa treats test-time reasoning as an allocation problem with action space {SAMPLE, VERIFY_1, ..., VERIFY_L, STOP} at each decision step, where the system state includes the candidate set, verifier scores observed so far, remaining budget, and history features (answer diversity, candidate length, answer flips, token-cap hits). CoBa-Routed inference (Algorithm 1): generate a small warm-up set of k=2 candidates; score all candidates with a rule-based answer-frequency/agreement verifier (V0) and a lightweight local judge (V1, Qwen3-8B); while under the candidate cap and budget remain, check if the top answer is stable and the lightweight score is high -- if so, stop; otherwise generate one more candidate and re-score. After the loop, candidates are ranked by a fusion of answer frequency and verifier scores (R(c) = 0.20*f(c) + 0.30*s1(c) + 0.15*s2(c) + 0.45*s3(c), with missing scores renormalized), and the top K candidates (K=0/2/4 for CoBa-Routed-Light/Routed/Routed-Strong) are routed to a strong verifier (V3, Qwen3-14B deep verifier); the final answer is extracted from the highest-ranked candidate under R(c). All methods (CoBa and baselines) draw from the same offline-generated pool of N=16 candidates per example (generators Qwen3-14B, Phi-4-reasoning, Qwen3-8B; temperature 0.6, top-p 0.95, 16,384-token budget) so that comparisons isolate the effect of the allocation/routing policy from candidate generation itself.

## Results

Macro-averaged over 3,129 example-generator evaluations (15 dataset-generator pairs): CoBa-Routed-Strong reaches 85.13% accuracy at 58.0k average total tokens, 7.91 average model calls, and 629.9k parameter-weighted tokens per item. This is statistically indistinguishable from a self-evaluation weighted-voting proxy baseline (85.20%, 95% CI of the difference [-1.25,+... ] includes zero) while using 49.1% fewer parameter-weighted tokens (629.9k vs 1236.7k). It matches best-of-16 majority voting (85.12%) within 0.70 accuracy points (95% CI [-1.25,-0.16], p=.004) while using 58.9% fewer parameter-weighted tokens (629.9k vs 1533.3k, i.e. best-of-16 costs 2.43x more). CoBa-Routed-Strong significantly beats greedy decoding by +3.74 points (95% CI [+2.97,+4.54], p<.001; greedy=75.72%). Per-dataset (Table 3, averaged over 3 generators): CoBa-Routed-Strong reaches 87.6% on MATH, 82.2% on AIME2024 (vs 65.6% greedy), 71.1% on AIME2025, 92.4% on AMC, and 92.3% on Reasoning Gym hard subset; the pool oracle upper bound is 90.3/87.8/83.3/95.6/99.8% respectively, with the largest remaining oracle gap on AIME2025. Ablation (Table 4): moving from CoBa-Routed-Light (78.88% acc, 3.97 calls, 252.9k p-tok) to CoBa-Routed (82.92%, 5.48 calls, 392.4k p-tok) yields a large accuracy gain from a small number of added strong-verifier calls; moving to CoBa-Routed-Strong (85.13%, 7.91 calls, 629.9k p-tok) gives further but diminishing-return gains at higher marginal cost.

## Limitations

Stated/observed limitations from the document: the offline replay protocol operates over a shared, pre-generated candidate pool (N=16 candidates per example, fixed token budget), so routing can change which candidates are inspected/selected but cannot benefit from private, freshly-generated candidates unavailable to baselines -- it approximates rather than reproduces fully interactive test-time methods. Verifier baselines (V1 Qwen3-8B judge, V3 Qwen3-14B deep verifier) are local open-weight proxies, not claims of reproducing separately RL-trained or closed reward-model checkpoints. A learned MLP controller was also tried and degenerated to a near-greedy policy in a leave-one-dataset-out generalization test, described as a negative result showing the current evidence supports transparent routing over a learned controller. On AIME 2025 specifically, the oracle (pool-correctness upper bound) gap remains large because the candidate pool itself often lacks a correct answer, so routing/verification cannot recover accuracy that generation never produced -- CoBa-Routed-Strong still trails best-of-16 by 0.70 accuracy points (95% CI [-1.25,-0.16], p=.004) at 2.43x lower parameter-weighted token cost. The paper notes cost is measured in tokens/parameter-weighted tokens/latency, not a full dollar or energy cost model.

## Why it matters here

- **overthinking**: Directly on topic: the paper explicitly frames test-time reasoning as deciding whether the next unit of compute should go to generation, verification, or stopping -- i.e. when a reasoning system should keep spending compute versus stop -- and evaluates the accuracy/cost tradeoff of that stopping/routing decision on math and symbolic reasoning benchmarks (MATH-500, AIME, AMC, Reasoning Gym), which is a direct instance of the topic's 'methods to make a model stop (or keep going) at the right point.'

## Entities

- **Concepts**: test-time reasoning as a compute-allocation problem, generation vs. verification vs. stopping as competing actions under a fixed budget, compute-balanced routing, parameter-weighted token cost, accuracy-cost Pareto frontier
- **Methods**: CoBa (Compute-Balanced test-time scaling) routing policy, CoBa-Routed-Light / -Routed / -Routed-Strong variants, tiered verification (rule-based V0, lightweight judge V1, process verifier V2, strong deep verifier V3), answer-frequency + verifier-score fusion ranking, paired bootstrap significance testing
- **Datasets**: [MATH-500](../../../../wiki/datasets/math-500.md), [AIME 2024](../../../../wiki/datasets/aime-2024.md), [AIME 2025](../../../../wiki/datasets/aime-2025.md), AMC 2023, Reasoning Gym (procedural symbolic reasoning, hard subset)

Tags: `test-time-scaling`, `compute-allocation`, `routing`, `verification`, `stopping-policy`, `mathematical-reasoning`, `cost-efficiency`

## Abstract

Test-time scaling is often implemented by spending more compute along one axis: sampling more solutions, extending a chain of thought, or applying a stronger evaluator. Under a fixed inference budget, these choices compete. This paper formulates test-time reasoning as a compute-allocation problem in which a system must decide whether the next unit of compute should be spent on generation, verification, or stopping. We introduce CoBa, a compute-balanced routing policy that first obtains a small set of candidates, applies cheap verification broadly, and routes uncertain or high-value candidates to stronger verification. On 3,129 example-generator evaluations spanning MATH-500, AIME 2024/2025, AMC 2023, and procedural symbolic reasoning, CoBa-Routed-Strong reaches 85.13% macro accuracy, statistically matching a self-evaluation weighted-voting proxy at 85.20% while using 49.1% fewer parameter-weighted tokens. It also matches best-of-16 majority voting within 0.01 macro-accuracy points while using 58.9% fewer parameter-weighted tokens; paired tests retain a small best-of-16 edge at substantially higher cost. Paired bootstrap tests show significant gains over single-sample decoding, while the remaining gap to the pool oracle exposes headroom for sharper routing. For local reasoning systems, test-time scaling becomes a question of where the next computation is most valuable.

---

Record id: `arxiv:2608.07424`
