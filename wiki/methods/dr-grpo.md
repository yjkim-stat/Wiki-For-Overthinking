# Dr. GRPO

<!-- auto:begin -->

The archive's sources name Dr. GRPO only as a GRPO variant used as a training baseline, never describing what it changes. The Netflix verifier study runs it alongside GRPO and GSPO with a binary outcome-only reward (G=8 rollouts, 400 steps) and reports that all three degrade Qwen2.5-7B on every subjective verification task; WS-GRPO reports that GRPO and Dr.GRPO improve more slowly and on increasingly long chains, so their accuracy-per-step early in training is lower than WS-GRPO's. On the archive's evidence the entry supports no more than that: it is a same-family alternative to GRPO whose distinguishing mechanism is not stated in any collected reading.

- **Kind**: method
- **Also called**: Dr.GRPO
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [AdaptThink](adaptthink.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AutoThink](autothink.md), [CommonsenseQA](../datasets/commonsenseqa.md), [DAPO](dapo.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [Length Penalty](../concepts/length-penalty.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [Overthinking](../concepts/overthinking.md), [Reasoning Collapse](../concepts/reasoning-collapse.md), [RLVR](rlvr.md), [routing collapse](../concepts/routing-collapse.md), [Thinkless](thinkless.md)

## Appears in

- [LLM Reasoning for Subjective Tasks: Failure Modes, Mitigation, and Dynamic Reasoning Routing](../../archive/papers/2026/arxiv-2608-08889/summary.md) — An empirical study of LLM verifiers on four subjective verification tasks from a production recommender platform, showing that explicit reasoning often degrades accuracy and that standard RLVR drives reasoning length to near zero ('reasoning collapse'), plus a conditional length-penalized reward that restores it.
- [Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation](../../archive/papers/2026/arxiv-2608-20256/summary.md) — Trains a 1.5B reasoning model to emit one of three mode tokens (NoThink, Short, Long) as the very first token of its response and to reason under that mode's budget, learned end-to-end inside GRPO with no separate router.
- [WS-GRPO: Weakly-Supervised Group-Relative Policy Optimization for Rollout-Efficient Reasoning](../../archive/papers/2026/title-39bbcb4cded34ec7/summary.md) — WS-GRPO trains a preference model from outcome-only correctness labels to score partial reasoning trajectories, turning terminal reward into prefix-level signal about whether continuing is worthwhile, and reports far shorter reasoning at some accuracy cost.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
