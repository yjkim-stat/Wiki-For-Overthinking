# Chain-of-Thought (CoT, baseline)

<!-- auto:begin -->

Plain chain-of-thought (CoT) prompting is used across these sources as the reference baseline against which structured or multi-agent test-time-scaling methods are measured: SCOPE reports a 61.6-point accuracy gain and large cost/time reductions over a CoT baseline on a multi-constraint planning benchmark by compiling constraints into deterministic solver code instead; the Pareto-optimal multi-agent-reasoning study finds mixture-of-agents gains +7.1 percentage points over CoT at high compute, while self-refinement -- despite using more compute than CoT -- consistently underperforms it.

- **Kind**: method
- **Also called**: chain-of-thought (CoT, baseline)
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [BBH (Big-Bench Hard)](../datasets/bbh-big-bench-hard.md), [Best-of-N (baseline)](best-of-n-baseline.md), [Gemini-2.5-Pro](../models/gemini-2-5-pro.md), [GPT-4o](../models/gpt-4o.md), [GPT-5](../models/gpt-5.md), [gpt-o3](../models/gpt-o3.md), [GSM8K](../datasets/gsm8k.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [LLaMA-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [MMLU-Pro](../datasets/mmlu-pro.md), [Multi-Agent Debate](multi-agent-debate.md), [Self-Consistency](self-consistency.md)

## Appears in

- [Programming over Thinking: Efficient and Robust Multi-Constraint Planning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2028/summary.md) — SCOPE replaces long natural-language reasoning chains for multi-constraint planning with a two-stage, multi-agent pipeline that infers a query's combination/constraint structure once and compiles it into reusable, deterministic solver functions (Combination/Filter/Deliver), reaching 93.1% success on TravelPlanner with GPT-4o (a 61.6-point gain over CoT) while cutting inference cost 1.4x and time 4.67x versus the best baseline.
- [Multi-Agent Reasoning Improves Compute Efficiency: Pareto-Optimal Test-Time Scaling](../../archive/papers/2026/doi-10-18653-v1-2026-acl-srw-1/summary.md) — A systematic Pareto-front analysis of four test-time-scaling pipelines (self-consistency, self-refinement, debate, mixture-of-agents) across 34 configurations finds mixture-of-agents dominates the compute-accuracy frontier (+7.1pp over CoT at 15-20x compute, beating self-consistency and debate by 2.7pp/1.4pp at matched budgets), that debate should scale agents rather than rounds, that MoA is Pareto-optimal when proposer models outnumber layers by one, and that harder tasks benefit far more from added test-time compute than easy ones (+9.0pp vs. +2.2pp), while self-refinement underperforms even the plain chain-of-thought baseline throughout.
- [MetaScale: Test-Time Scaling with Evolving Meta-Thoughts](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-574/summary.md) — MetaScale is a test-time-scaling framework that has an LLM select and iteratively evolve 'meta-thoughts' (a cognitive mindset plus a problem-solving strategy, initialized from self-composed heuristics and retrieved WildChat conversation patterns) via a multi-armed-bandit UCB selection process guided by a reward model, periodically refined by a genetic algorithm that evolves high-reward meta-thoughts into improved child strategies -- outperforming Best-of-N and CoT+Best-of-N baselines on Arena-Hard/MMLU-Pro/GSM8K, beating o1-mini under style control, and scaling more effectively with increased sampling budget than Best-of-N (which plateaus).

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
