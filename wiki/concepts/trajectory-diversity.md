# trajectory diversity

<!-- auto:begin -->

How many genuinely different solution paths a policy will produce, as against how many samples it draws. Both sources argue reinforcement learning erodes it and locate the erosion in credit rather than in entropy. One measures a policy's preference between two specific verifier-equivalent continuations at a shared branch point and finds RLVR policies more decided than distilled ones on 95.5-100% of branches, with the collapse significantly stronger for semantically distinct continuations than for syntactic variants of the same statement. The other identifies the mechanism in the objective: with binary rewards every verified-correct completion receives the same positive advantage, so a recurring solution form accumulates positive coefficient mass proportional to how often it is sampled, and the fitted slope of cluster credit against cluster size is 1.00. Both then show the cost is real at high sampling budgets, where retaining alternative correct modes is what solves hard problems.

- **Kind**: concept
- **Also called**: diversity collapse, solution diversity
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [advantage estimation](advantage-estimation.md), [AIME](../datasets/aime.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [answer aggregation](../methods/answer-aggregation.md), [backtracking](backtracking.md), [beam search](../methods/beam-search.md), [compute allocation](compute-allocation.md), [credit assignment](credit-assignment.md), [DAPO](../methods/dapo.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DAPO-Qwen-32B](../models/dapo-qwen-32b.md), [DeepSeek-R1-0528-Qwen3-8B](../models/deepseek-r1-0528-qwen3-8b.md), [entropy collapse](entropy-collapse.md), [exploration](exploration.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-5.6-luna](../models/gpt-5-6-luna.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [HMMT](../datasets/hmmt.md), [Humanity's Last Exam](../datasets/humanity-s-last-exam.md), [KV cache](kv-cache.md), [linear probe](../methods/linear-probe.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [long chain-of-thought distillation](../methods/long-chain-of-thought-distillation.md), [LoRA](../methods/lora.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [Monte Carlo tree search](../methods/monte-carlo-tree-search.md), [pass@k](pass-k.md), [policy entropy](policy-entropy.md), [prefix caching](../methods/prefix-caching.md), [process reward model](../methods/process-reward-model.md), [Qwen2.5-32B-Instruct](../models/qwen2-5-32b-instruct.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [Qwen3-8B-Base](../models/qwen3-8b-base.md), [randomized control](randomized-control.md), [reasoning boundary](reasoning-boundary.md), [RLVR](../methods/rlvr.md), [self-consistency](../methods/self-consistency.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time compute](test-time-compute.md), [vLLM](../methods/vllm.md)

## Appears in

- [BODHI: Do LLMs Branch Out and Discover Heterogeneous Inferences?](../../archive/papers/2026/arxiv-2608-02867/summary.md) — Builds prefix trees of semantically equivalent reasoning statements and measures how RLVR changes a model's preference between branches, finding the entropy collapse is not stylistic — the collapse is stronger for semantically distinct continuations than for syntactic variants of the same statement.
- [When Correct Solutions Repeat: Rarity-Aware Credit Redistribution for GRPO](../../archive/papers/2026/arxiv-2608-03467/summary.md) — Shows that GRPO's per-completion uniformity is frequency-skewed once credit is aggregated by solution structure — a recurring correct form accumulates positive coefficient mass proportional to how often it is sampled — and rebalances it by a rarity exponent over a partition built from deterministic cue signatures rather than a judge model.
- [Thought-Level Beam Search for Reasoning](../../archive/papers/2026/arxiv-2608-08020/summary.md) — Reformulates test-time reasoning as compute allocation over partial trajectories under a hardware budget, and runs a zero-sum beam search over reasoning steps that prunes weak traces and immediately re-spends the freed capacity by branching from high-scoring prefixes.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
