# AIME

<!-- auto:begin -->

The American Invitational Mathematics Examination, used in the archive as a competition-mathematics benchmark whose answers are short integers and therefore automatically checkable. The sources use it as a hard reference point rather than an object of study: one measures a training-free constraint-extraction protocol on it, another reports a 43% token reduction on it with no accuracy drop. Because problems are released by year, AIME appears in the archive both as an undated pool and as year-specific splits, and the year matters for contamination.

- **Kind**: dataset
- **Also called**: American Invitational Mathematics Examination
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 4

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [backtracking](../concepts/backtracking.md), [Brumo](brumo.md), [chain of thought](../methods/chain-of-thought.md), [chain of thought distillation](../methods/chain-of-thought-distillation.md), [CMIMC](cmimc.md), [credit assignment](../concepts/credit-assignment.md), [DAPO](../methods/dapo.md), [DAPO-Math-17K](dapo-math-17k.md), [entropy collapse](../concepts/entropy-collapse.md), [exploration](../concepts/exploration.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [long chain-of-thought distillation](../methods/long-chain-of-thought-distillation.md), [LoRA](../methods/lora.md), [MATH](math.md), [MATH500](math500.md), [OlympiadBench](olympiadbench.md), [overthinking](../concepts/overthinking.md), [pass@k](../methods/pass-k.md), [policy entropy](../concepts/policy-entropy.md), [Qwen2.5-32B-Instruct](../models/qwen2-5-32b-instruct.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-8B-Base](../models/qwen3-8b-base.md), [randomized control](../concepts/randomized-control.md), [reasoning boundary](../concepts/reasoning-boundary.md), [reasoning distillation](../methods/reasoning-distillation.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [RLVR](../methods/rlvr.md), [routing](../concepts/routing.md), [self-verification](../concepts/self-verification.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [token selection](../concepts/token-selection.md), [trajectory diversity](../concepts/trajectory-diversity.md), [verification](../concepts/verification.md)

## Appears in

- [BODHI: Do LLMs Branch Out and Discover Heterogeneous Inferences?](../../archive/papers/2026/arxiv-2608-02867/summary.md) — Builds prefix trees of semantically equivalent reasoning statements and measures how RLVR changes a model's preference between branches, finding the entropy collapse is not stylistic — the collapse is stronger for semantically distinct continuations than for syntactic variants of the same statement.
- [When Correct Solutions Repeat: Rarity-Aware Credit Redistribution for GRPO](../../archive/papers/2026/arxiv-2608-03467/summary.md) — Shows that GRPO's per-completion uniformity is frequency-skewed once credit is aggregated by solution structure — a recurring correct form accumulates positive coefficient mass proportional to how often it is sampled — and rebalances it by a rarity exponent over a partition built from deterministic cue signatures rather than a judge model.
- [Constraint-First Reasoning: A Training-Free Protocol for Exploiting Answer-Space Constraints in Mathematical Problem Solving](../../archive/papers/2026/arxiv-2608-05254/summary.md) — A training-free two-stage prompting protocol that extracts a problem's answer-space constraints first and then checks its own intermediate and final results against them, routed on by a regex detector.
- [DRP: Distilled Reasoning Pruning with Mathematical Skill-aware Step Decomposition for Efficient Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-196/summary.md) — Has a teacher decompose and prune a student's reasoning by mathematical skill, then distills the pruned paths back, on the argument that CoT structure must match student capacity.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
