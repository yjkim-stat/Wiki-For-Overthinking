# Difficulty-aware compute allocation

<!-- auto:begin -->

Spending inference or exploration effort in proportion to how hard a problem is, so that easy queries are answered cheaply and the saved budget is moved onto hard ones. The two archived sources make the allocation explicit in different places: IBPO casts it as constrained policy optimisation — cap the fraction of queries allowed an expensive response, maximise the reward margin between the expensive and regular groups subject to that cap — and solves the per-batch cap as an integer linear program, taking LLaMA 3.1 8B Instruct from 51.26 to 55.4 pass@1 on MATH500 at 2.16x trials, with only 2% of level-1 problems but 41% of level-5 receiving an expensive response at a 25% cap. ARES instead uses sliding-window token entropy as the in-trace signal for when and how much to explore, after a cold start on traces whose length is proportional to item difficulty. Both make the same point about what the idea buys: it is reallocation rather than net reduction — ARES is about 22% shorter than its cold-start model on GSM8K and 19% shorter on MathVista, but about 38% longer on AIME25 (22,618.8 against 16,361.6 tokens).

- **Kind**: concept
- **Also called**: Difficulty-Aware Compute Allocation
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [adaptive reasoning](adaptive-reasoning.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [ARES](../methods/ares.md), [BBEH](../datasets/bbeh.md), [DynaMath](../datasets/dynamath.md), [GPQA](../datasets/gpqa.md), [GSM8K](../datasets/gsm8k.md), [MATH500](../datasets/math500.md), [MathVerse](../datasets/mathverse.md), [MathVision](../datasets/mathvision.md), [MathVista](../datasets/mathvista.md), [MMLU-Pro](../datasets/mmlu-pro.md), [MMMU](../datasets/mmmu.md), [MMMU-Pro](../datasets/mmmu-pro.md), [MMStar](../datasets/mmstar.md), [Overthinking](overthinking.md), [Qwen2.5-VL](../methods/qwen2-5-vl.md), [Reasoning Trace Length](reasoning-trace-length.md), [RLVR](../methods/rlvr.md), [Test-Time Compute Scaling](test-time-compute-scaling.md), [Token Budget](token-budget.md), [Token-Level Entropy](token-level-entropy.md), [ViRL39k](../datasets/virl39k.md), [WeMath](../datasets/wemath.md)

## Appears in

- [Think Smarter not Harder: Adaptive Reasoning with Inference Aware Optimization](../../archive/papers/2025/title-00cdef4a3a910795/summary.md) — Formulates adaptive inference-budget allocation as constrained policy optimisation - cap the fraction of queries allowed an expensive response, maximise reward margin subject to that cap - and solves the per-batch cap with an integer linear program whose solution reweights an SFT update.
- [ARES: Multimodal Adaptive Reasoning via Difficulty-Aware Token-Level Entropy Shaping](../../archive/papers/2026/title-544eea46a2eb68c1/summary.md) — ARES trains multimodal reasoning models to spend exploration effort in proportion to problem difficulty, using sliding-window token entropy as the signal for when and how much to explore.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
