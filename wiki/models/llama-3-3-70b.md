# Llama 3.3 70B

<!-- auto:begin -->

Llama 3.3 70B is used in these sources as an evaluated LLM: the cross-cultural-measurement-systems study finds it (like other large models) suffers accuracy drops when queried in a non-default (non-Western) measurement system, and that chain-of-thought reasoning stabilizes accuracy back toward the default level but at 180-300% more test-time compute -- a cost that disproportionately burdens users outside the model's default cultural context; VecCISC also evaluates on Llama 3.3 70B among its five models.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AQuA-RAT](../datasets/aqua-rat.md), [chain-of-thought prompting](../concepts/chain-of-thought-prompting.md), [CommonsenseQA](../datasets/commonsenseqa.md), [Confidence-Informed Self-Consistency (CISC, baseline)](../methods/confidence-informed-self-consistency-cisc-baseline.md), [GPQA](../datasets/gpqa.md), [GPT-4o-mini](gpt-4o-mini.md), [Llama-3.1-8B](llama-3-1-8b.md), [MMLU-Pro](../datasets/mmlu-pro.md), [Qwen2.5 7B](qwen2-5-7b.md), [Self-Consistency (SC, baseline)](../methods/self-consistency-sc-baseline.md), [weighted majority voting](../concepts/weighted-majority-voting.md)

## Appears in

- [On Generalization across Measurement Systems: LLMs Entail More Test-Time Compute for Underrepresented Cultures](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-1032/summary.md) — LLMs default to Western measurement systems (USD, kilometers, kilograms) reflecting their training-data culture, suffer significant accuracy drops when queried in a non-default system (currency, length, or weight), and while chain-of-thought/sequential reasoning stabilizes large models' accuracy back toward the default level, it increases test-time compute by 180-300% -- disproportionately burdening users whose cultural context is not the default.
- [VecCISC: Improving Confidence-Informed Self-Consistency with Reasoning Trace Clustering and Candidate Answer Selection](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1305/summary.md) — VecCISC reduces the cost of Confidence-Informed Self-Consistency (CISC) -- which needs a separate critic-LLM call on every sampled reasoning trace to weight majority voting -- by embedding traces, clustering them per candidate answer, and sending only cluster-representative (nearest-centroid) traces to the critic, cutting critic calls 30-35% and total pipeline token usage 47% while matching or exceeding CISC's accuracy across five models and five datasets.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
