# Llama 3.3 70B

<!-- auto:begin -->

Llama 3.3 70B is used in these sources as an evaluated LLM: the cross-cultural-measurement-systems study finds it (like other large models) suffers accuracy drops when queried in a non-default (non-Western) measurement system, and that chain-of-thought reasoning stabilizes accuracy back toward the default level but at 180-300% more test-time compute -- a cost that disproportionately burdens users outside the model's default cultural context; VecCISC also evaluates on Llama 3.3 70B among its five models.

- **Kind**: model
- **Also called**: LLaMA-3.3-70B, Llama-3.3-70B
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [AIME 2024](../datasets/aime-2024.md), [AQuA-RAT](../datasets/aqua-rat.md), [chain-of-thought prompting](../concepts/chain-of-thought-prompting.md), [CommonsenseQA](../datasets/commonsenseqa.md), [Confidence-Informed Self-Consistency (CISC, baseline)](../methods/confidence-informed-self-consistency-cisc-baseline.md), [Gemini 2.5 Flash](gemini-2-5-flash.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-4.1](gpt-4-1.md), [GPT-4o](gpt-4o.md), [GPT-4o-mini](gpt-4o-mini.md), [gpt-oss-120b](gpt-oss-120b.md), [GPT-OSS-20B](gpt-oss-20b.md), [Grok-3](grok-3.md), [Llama-3.1-8B](llama-3-1-8b.md), [MMLU-Pro](../datasets/mmlu-pro.md), [Nemotron-32B](nemotron-32b.md), [Qwen2.5 7B](qwen2-5-7b.md), [Self-Consistency (SC, baseline)](../methods/self-consistency-sc-baseline.md), [weighted majority voting](../methods/weighted-majority-voting.md)

## Appears in

- [On Generalization across Measurement Systems: LLMs Entail More Test-Time Compute for Underrepresented Cultures](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-1032/summary.md) — LLMs default to Western measurement systems (USD, kilometers, kilograms) reflecting their training-data culture, suffer significant accuracy drops when queried in a non-default system (currency, length, or weight), and while chain-of-thought/sequential reasoning stabilizes large models' accuracy back toward the default level, it increases test-time compute by 180-300% -- disproportionately burdening users whose cultural context is not the default.
- [VecCISC: Improving Confidence-Informed Self-Consistency with Reasoning Trace Clustering and Candidate Answer Selection](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1305/summary.md) — VecCISC reduces the cost of Confidence-Informed Self-Consistency (CISC) -- which needs a separate critic-LLM call on every sampled reasoning trace to weight majority voting -- by embedding traces, clustering them per candidate answer, and sending only cluster-representative (nearest-centroid) traces to the critic, cutting critic calls 30-35% and total pipeline token usage 47% while matching or exceeding CISC's accuracy across five models and five datasets.
- [Beyond Memorization: Extending Reasoning Depth with Recurrence, Memory and Test-Time Compute Scaling](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2103/summary.md) — Using a controlled 1D-cellular-automata benchmark with disjoint train/test rule sets (precluding memorization), this paper shows models can genuinely infer unseen local rules but fixed-depth architectures collapse sharply beyond one-step-ahead prediction, that most frontier LLMs (except Gemini-2.5-Pro) fail even the simplest natural-language proxy of this task, and that depth -- not width -- is what drives multi-step accuracy, with chain-of-thought-style token-level supervision reaching near-perfect accuracy up to 4 look-ahead steps while RL (GRPO) without intermediate supervision reaches only 3 steps and architectural depth-extension tricks (ACT, recurrent memory) each add only about one effective step.
- [Budget-Aware Anytime Reasoning with LLM-Synthesized Preference Data](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-417/summary.md) — Introduces the Anytime Index, an AUC-style metric quantifying how solution quality improves as reasoning-token budget increases, and Preference Data Prompting (PDP), an inference-time self-improvement method using self-generated contrastive reasoning pairs at fixed token budgets, giving consistent gains across seven LLM families on trip planning, math, and scientific QA.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
