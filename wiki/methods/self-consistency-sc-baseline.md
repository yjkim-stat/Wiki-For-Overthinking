# Self-Consistency (SC, baseline)

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Also called**: self-consistency (SC, baseline)
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [AQuA-RAT](../datasets/aqua-rat.md), [CommonsenseQA](../datasets/commonsenseqa.md), [Confidence-Informed Self-Consistency (CISC, baseline)](confidence-informed-self-consistency-cisc-baseline.md), [DeepSeek-R1-0528-Qwen3-8B](../models/deepseek-r1-0528-qwen3-8b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [HMMT25](../datasets/hmmt25.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama 3.3 70B](../models/llama-3-3-70b.md), [MATH500](../datasets/math500.md), [MMLU-Pro](../datasets/mmlu-pro.md), [Qwen2.5 7B](../models/qwen2-5-7b.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [weighted majority voting](../concepts/weighted-majority-voting.md)

## Appears in

- [VecCISC: Improving Confidence-Informed Self-Consistency with Reasoning Trace Clustering and Candidate Answer Selection](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1305/summary.md) — VecCISC reduces the cost of Confidence-Informed Self-Consistency (CISC) -- which needs a separate critic-LLM call on every sampled reasoning trace to weight majority voting -- by embedding traces, clustering them per candidate answer, and sending only cluster-representative (nearest-centroid) traces to the critic, cutting critic calls 30-35% and total pipeline token usage 47% while matching or exceeding CISC's accuracy across five models and five datasets.
- [Hidden States as Early Signals: Step-level Trace Evaluation and Pruning for Efficient Test-Time Scaling](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1336/summary.md) — STEP trains a lightweight 2-layer-MLP step scorer on reasoning-model hidden states at step boundaries to evaluate parallel-reasoning trace quality with near-zero overhead, and pairs it with a GPU-memory-triggered (not confidence-threshold or fixed-schedule) pruning mechanism that eliminates the KV-cache waiting-queue bottleneck identified as the dominant source of end-to-end latency in parallel test-time scaling -- cutting latency 45-70% versus self-consistency while improving accuracy 0.4-7.5 points across three models and six benchmarks.
- [Seer Self-Consistency: Advance Budget Estimation for Adaptive Test-Time Scaling](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2120/summary.md) — SeerSC resolves a specific gap in adaptive self-consistency methods -- reduced token usage from sequential early-stopping does not translate into reduced latency, since sequential budget decisions conflict with the parallel-sampling engines modern inference uses -- by having a cheap System-1 pass (direct, non-reasoning answers) pre-estimate each query's scaling potential via confidence-weighted answer entropy, then allocating a fixed System-2 (full-reasoning) sample budget in a single parallel batch based on that pre-estimate, cutting inference latency up to 43% and token usage up to 47% versus sequential adaptive baselines (AC, ESC) at comparable accuracy, with System 1's own overhead negligible (well under 1% of total latency) and the method composable with orthogonal weighted-voting and path-pruning techniques.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
