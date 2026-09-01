# Confidence-Informed Self-Consistency (CISC, baseline)

<!-- auto:begin -->

Confidence-Informed Self-Consistency (CISC) weights majority voting over sampled reasoning traces by a critic-LLM's confidence score for each trace. VecCISC reduces its cost (critic calls needed per query) via embedding-based trace clustering while matching or exceeding its accuracy, and BrowseConf uses it as a fixed-budget-10 baseline that its confidence-threshold-triggered test-time-scaling method for web agents outperforms at far fewer average attempts.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AQuA-RAT](../datasets/aqua-rat.md), [BrowseComp](../datasets/browsecomp.md), [CommonsenseQA](../datasets/commonsenseqa.md), [GPQA](../datasets/gpqa.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama 3.3 70B](../models/llama-3-3-70b.md), [MMLU-Pro](../datasets/mmlu-pro.md), [Qwen2.5 7B](../models/qwen2-5-7b.md), [Self-Consistency (baseline)](self-consistency-baseline.md), [Self-Consistency (SC, baseline)](self-consistency-sc-baseline.md), [weighted majority voting](../concepts/weighted-majority-voting.md)

## Appears in

- [VecCISC: Improving Confidence-Informed Self-Consistency with Reasoning Trace Clustering and Candidate Answer Selection](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1305/summary.md) — VecCISC reduces the cost of Confidence-Informed Self-Consistency (CISC) -- which needs a separate critic-LLM call on every sampled reasoning trace to weight majority voting -- by embedding traces, clustering them per candidate answer, and sending only cluster-representative (nearest-centroid) traces to the critic, cutting critic calls 30-35% and total pipeline token usage 47% while matching or exceeding CISC's accuracy across five models and five datasets.
- [BrowseConf: Confidence-Guided Test-Time Scaling for Web Agents](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-21/summary.md) — BrowseConf shows that despite web-search agents being poorly calibrated in absolute terms (verbalized confidence systematically exceeds actual accuracy), their confidence is strongly rank-correlated with correctness -- near-zero accuracy below 70% confidence, more than double the average accuracy above 95% -- and exploits this by triggering additional search attempts only when confidence falls below a calibrated threshold rather than always sampling a fixed number, matching or beating fixed-budget Self-Consistency/CISC on BrowseComp while cutting average attempts from a fixed 10 down to 2.06-5.72.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
