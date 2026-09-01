# Qwen2.5-7B-Base

<!-- auto:begin -->

Qwen2.5-7B-Base is used as a base model in ADaPT (diagnosing that sequence-level efficiency rewards implicitly penalize correct-but-long reasoning) and in SCOPE's entropy-collapse-mitigation experiments (A Few Bad Apples Spoil the Bunch), which derives an exact token-level decomposition showing entropy collapse is driven by a small subset of structurally critical tokens.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [GRPO](../methods/grpo.md), [GRPO (baseline)](../methods/grpo-baseline.md), [GSM8K](../datasets/gsm8k.md), [Llama3.1-8B-Instruct](llama3-1-8b-instruct.md), [MATH500](../datasets/math500.md), [MMLU-Pro](../datasets/mmlu-pro.md), [Olympiad](../datasets/olympiad.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-3B-Base](qwen2-5-3b-base.md), [Qwen2.5-Math-7B](qwen2-5-math-7b.md), [SFT (baseline)](../methods/sft-baseline.md), [TLMRE (baseline)](../methods/tlmre-baseline.md)

## Appears in

- [ADaPT: Token-Level Decoupling for Efficient Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-165/summary.md) — ADaPT diagnoses that existing efficiency-oriented RL methods fail because sequence-level efficiency rewards implicitly penalize correct-but-long reasoning (a structural mismatch, since only the first token -- the fast/slow mode choice -- actually determines efficiency, while all subsequent tokens can only affect correctness), and fixes this by applying an efficiency reward exclusively to a dedicated mode-selection <think>/<answer> token via a CISPO-stabilized token-level GRPO variant -- cutting Qwen2.5-7B's average generation length from 1540 to 1031 tokens (SFT+GRPO baseline) with only a 0.4-point accuracy drop, tracing a genuine Pareto frontier other methods stay strictly inside, and letting a single trained model's efficiency be tuned post-hoc by adjusting the mode-token's decoding threshold with no retraining.
- [A Few Bad Apples Spoil the Bunch: Preventing Global Entropy Collapse Driven by a Small Set of Tokens in LLM Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-641/summary.md) — Derives an exact, non-asymptotic decomposition of GRPO's token-level policy update showing entropy collapse in reasoning RL is driven by a small subset (~5%) of structurally critical 'branch-defining' tokens rather than uniform decay across the sequence, and proposes SCOPE, which applies KL regularization only to that top-5% (ranked by a computable redistribution score), consistently improving both Pass@1 and Pass@k under both RLVR and RLIF across model scales.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
