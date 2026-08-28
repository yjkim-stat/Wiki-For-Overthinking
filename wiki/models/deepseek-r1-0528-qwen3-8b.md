# DeepSeek-R1-0528-Qwen3-8B

<!-- auto:begin -->

DeepSeek-R1-0528-Qwen3-8B is used in these sources as a reasoning-model backbone subject to interventions on its chain-of-thought: CiPO unlearns sensitive knowledge from both this model's intermediate reasoning trace and final answer via counterfactual preference optimization, while STOP evaluates its path-pruning method (learnable [STOP]-token scoring of parallel reasoning trajectories) across model scales including this one.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-oss-120b](gpt-oss-120b.md), [GPT-OSS-20B](gpt-oss-20b.md), [HMMT25](../datasets/hmmt25.md), [majority voting (baseline)](../methods/majority-voting-baseline.md), [Qwen3-4B-Thinking-2507](qwen3-4b-thinking-2507.md), [Self-Consistency (SC, baseline)](../methods/self-consistency-sc-baseline.md), [SimPO](../methods/simpo.md), [weighted majority voting](../concepts/weighted-majority-voting.md), [ZebraLogic](../datasets/zebralogic.md)

## Appears in

- [CiPO: Counterfactual Unlearning for Large Reasoning Models through Iterative Preference Optimization](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-143/summary.md) — CiPO reframes unlearning for large reasoning models as counterfactual intervention on the chain-of-thought: it has the target model generate a logically valid counterfactual reasoning trace and answer, then iteratively preference-optimizes the model toward that counterfactual (SimPO loss against online-sampled dispreferred responses), removing sensitive knowledge from both intermediate CoT and final answers while preserving reasoning ability better than prior unlearning baselines.
- [Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-876/summary.md) — STOP (Super TOken for Pruning) is a lightweight, LoRA-based module that reads a frozen LRM's cached KV states via a single learnable [STOP] token to score and prune futile parallel-reasoning paths early -- at negligible inference overhead (0.59% latency) -- and is shown, via a proposed four-way taxonomy of path-pruning signal generators, to dominate external-signal and non-learnable internal-signal baselines in both accuracy and compute across model scales 1.5B-20B.
- [Hidden States as Early Signals: Step-level Trace Evaluation and Pruning for Efficient Test-Time Scaling](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1336/summary.md) — STEP trains a lightweight 2-layer-MLP step scorer on reasoning-model hidden states at step boundaries to evaluate parallel-reasoning trace quality with near-zero overhead, and pairs it with a GPU-memory-triggered (not confidence-threshold or fixed-schedule) pruning mechanism that eliminates the KV-cache waiting-queue bottleneck identified as the dominant source of end-to-end latency in parallel test-time scaling -- cutting latency 45-70% versus self-consistency while improving accuracy 0.4-7.5 points across three models and six benchmarks.
- [Chronos: Learning Temporal Dynamics of Reasoning Chains for Test-Time Scaling](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1376/summary.md) — Chronos treats a reasoning trace's per-token negative-log-probability sequence as a time series (rather than collapsing it to a single pooled scalar like prior confidence-based scorers) and scores its quality with a multi-scale InceptionTime-style CNN focused on the final tail tokens, then weights majority voting by these learned scores -- beating majority voting by up to 13.76 absolute points and confidence-weighted voting (DeepConf) across all nine model-benchmark combinations, at only a 0.0005% increase in inference FLOPs, and generalizing across models and out-of-domain tasks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
