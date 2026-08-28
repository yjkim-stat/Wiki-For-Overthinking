# Qwen3-4B-Instruct-2507

<!-- auto:begin -->

An open-weight instruction-tuned model used across sources as a cross-model transfer test subject for decoding-time code-verification methods (DTV), and as one of the two identical-architecture models (paired with Qwen3-4B-Thinking-2507) that GRIP's module-wise, RL-learned interpolation fuses to reduce reasoning-model overthinking while preserving or improving accuracy.

- **Kind**: model
- **Also called**: Qwen3-4B-Instruct
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [best-of-N](../methods/best-of-n.md), [DeepScaleR-preview (training)](../datasets/deepscaler-preview-training.md), [Gemma-4-E4B](gemma-4-e4b.md), [GPQA-D](../datasets/gpqa-d.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [IFEval](../datasets/ifeval.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B](llama-3-1-8b.md), [MATH500](../datasets/math500.md), [OlympiadBench](../datasets/olympiadbench.md), [Qwen3-30B-A3B](qwen3-30b-a3b.md), [Qwen3-4B](qwen3-4b.md), [Qwen3-4B-Base](qwen3-4b-base.md), [Qwen3-4B-Thinking-2507](qwen3-4b-thinking-2507.md), [self-refine](../methods/self-refine.md)

## Appears in

- [Verifier-Guided Code Translation via Meta-Step Decoding](../../archive/papers/2026/arxiv-2605-17626/summary.md) — Decoding Time Verification (DTV) interleaves code generation with deterministic verifier calls (compiler, type checker) at structural boundaries, using structure-aware rollback and diagnostic feedback instead of post-hoc filtering, to translate code more accurately and more token-efficiently than resampling-based test-time scaling.
- [GRIP: Granular Reward-Guided Parameter Interpolation for Efficient Reasoning](../../archive/papers/2026/arxiv-2608-25583/summary.md) — GRIP fuses a reasoning model and an instruction (non-thinking) model of identical architecture by learning a separate sigmoid-controlled interpolation ratio per module (attention, FFN, embedding/LM-head), trained with an RL reward that favors correct and concise responses while keeping both source models frozen, cutting Qwen3-4B-Thinking's average generation length 27.0% while slightly improving average accuracy.
- [Revisiting Model Interpolation for Efficient Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-389/summary.md) — Reveals that linear interpolation between an Instruct model's and a Thinking model's weights does not trade off performance and reasoning verbosity smoothly, but follows a predictable three-stage transition (Instruct-dominated -> abrupt thinking-pattern emergence -> converging to Thinking with diminishing/overthinking returns), and shows a strategically chosen interpolation point beats sophisticated model-merging baselines (task arithmetic, TIES) on both efficiency and accuracy.
- [Rhombus: Incentivizing Coordination in Parallel Thinking through Reinforcement Learning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1956/summary.md) — Rhombus reformulates parallel test-time scaling as a communication-optimization problem: multiple Proposer instances and a central Synthesizer (all the same shared model, role-switched via system prompt) are co-trained end-to-end via GRPO with a hybrid local-plus-system reward and role-level advantage normalization, teaching Proposers to emit compact, decision-focused (rather than implicit, hard-to-verify) reasoning cues -- beating a token-budget-matched Long-CoT baseline by 6.0% accuracy while cutting wall-clock latency 39.4%, with the coordination gap between Proposer exploration potential and realized Synthesizer accuracy nearly eliminated (0.7% vs. 4.6% for an uncoordinated baseline).

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
