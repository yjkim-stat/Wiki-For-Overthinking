# weighted majority voting

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2025](../datasets/aime-2025.md), [AQuA-RAT](../datasets/aqua-rat.md), [CommonsenseQA](../datasets/commonsenseqa.md), [Confidence-Informed Self-Consistency (CISC, baseline)](../methods/confidence-informed-self-consistency-cisc-baseline.md), [DeepSeek-R1-0528-Qwen3-8B](../models/deepseek-r1-0528-qwen3-8b.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [HMMT25](../datasets/hmmt25.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama 3.3 70B](../models/llama-3-3-70b.md), [MMLU-Pro](../datasets/mmlu-pro.md), [Qwen2.5 7B](../models/qwen2-5-7b.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [Self-Consistency (SC, baseline)](../methods/self-consistency-sc-baseline.md)

## Appears in

- [VecCISC: Improving Confidence-Informed Self-Consistency with Reasoning Trace Clustering and Candidate Answer Selection](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1305/summary.md) — VecCISC reduces the cost of Confidence-Informed Self-Consistency (CISC) -- which needs a separate critic-LLM call on every sampled reasoning trace to weight majority voting -- by embedding traces, clustering them per candidate answer, and sending only cluster-representative (nearest-centroid) traces to the critic, cutting critic calls 30-35% and total pipeline token usage 47% while matching or exceeding CISC's accuracy across five models and five datasets.
- [Hidden States as Early Signals: Step-level Trace Evaluation and Pruning for Efficient Test-Time Scaling](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1336/summary.md) — STEP trains a lightweight 2-layer-MLP step scorer on reasoning-model hidden states at step boundaries to evaluate parallel-reasoning trace quality with near-zero overhead, and pairs it with a GPU-memory-triggered (not confidence-threshold or fixed-schedule) pruning mechanism that eliminates the KV-cache waiting-queue bottleneck identified as the dominant source of end-to-end latency in parallel test-time scaling -- cutting latency 45-70% versus self-consistency while improving accuracy 0.4-7.5 points across three models and six benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
