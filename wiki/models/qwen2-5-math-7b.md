# Qwen2.5-Math-7B

<!-- auto:begin -->

Qwen2.5-Math-7B is used as a base/reference model in studies of entropy collapse during RL post-training: CurioSFT diagnoses that standard SFT causes entropy collapse limiting subsequent RL, a systematic entropy study finds performance can improve without entropy loss, and SCOPE derives an exact token-level decomposition showing entropy collapse in GRPO-based RL is driven by a small (~5%) subset of structurally critical tokens.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [ARC-Challenge](../datasets/arc-challenge.md), [DAPO-Math-17k (training)](../datasets/dapo-math-17k-training.md), [entropy collapse](../concepts/entropy-collapse.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [HumanEval](../datasets/humaneval.md), [IFEval](../datasets/ifeval.md), [LiveCodeBench](../datasets/livecodebench.md), [LLaMA-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [Llama3.1-8B-Instruct](llama3-1-8b-instruct.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MBPP](../datasets/mbpp.md), [Minerva](../datasets/minerva.md), [MMLU-Pro](../datasets/mmlu-pro.md), [OlympiadBench](../datasets/olympiadbench.md), [Qwen2.5-3B-Base](qwen2-5-3b-base.md), [Qwen2.5-7B-Base](qwen2-5-7b-base.md), [Qwen3-4B-Base](qwen3-4b-base.md), [TACO](../datasets/taco.md)

## Appears in

- [Learning While Staying Curious: Entropy-Preserving Supervised Fine-Tuning via Adaptive Self-Distillation for Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-617/summary.md) — CurioSFT diagnoses that standard SFT causes 'entropy collapse' (overconfidence, narrowed exploration) that limits the subsequent RL stage in the SFT-then-RL pipeline, and fixes it with Self-Exploratory Distillation toward a self-generated, temperature-scaled teacher plus Entropy-Guided Temperature Selection that concentrates exploration on high-entropy reasoning-connector tokens while preserving low-entropy factual tokens, improving downstream RL accuracy by 5.0 points on average.
- [Revisiting Entropy in Reinforcement Learning for Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1266/summary.md) — A systematic study of entropy collapse in GRPO-based RLVR training finds performance can improve without entropy loss (so entropy collapse is not merely a side effect of legitimate learning), identifies clipping thresholds, off-policy update count, and training-data diversity as governing factors, proves theoretically and confirms empirically that positive-advantage tokens are the primary driver of entropy collapse, and proposes Positive-Advantage Reweighting -- dynamically down-weighting positive-advantage-token loss -- to regulate entropy while maintaining performance, though training exclusively on non-positive-advantage tokens actually hurts benchmark scores despite reducing collapse.
- [A Few Bad Apples Spoil the Bunch: Preventing Global Entropy Collapse Driven by a Small Set of Tokens in LLM Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-641/summary.md) — Derives an exact, non-asymptotic decomposition of GRPO's token-level policy update showing entropy collapse in reasoning RL is driven by a small subset (~5%) of structurally critical 'branch-defining' tokens rather than uniform decay across the sequence, and proposes SCOPE, which applies KL regularization only to that top-5% (ranked by a computable redistribution score), consistently improving both Pass@1 and Pass@k under both RLVR and RLIF across model scales.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
