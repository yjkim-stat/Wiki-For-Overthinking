# MBPP

<!-- auto:begin -->

A Python program-synthesis benchmark, graded by execution, that the archive's papers use as the easier half of a code-generation pair with HumanEval. The one paper reporting it directly is C4, where a diffusion language model matches its own baseline exactly (45.9 versus 45.9) using 33.3 of a 384-step budget — an 11.11x saving — while the margin-based baselines Prophet and SchED collapse to 1.9 and 27.6, so MBPP is where the archive's sharpest 'same answer, far less compute' result sits. The reasoning-length papers include it only inside mixtures: SuCo averages it over eight benchmarks, and ShorterBetter puts it in a 6K out-of-domain pool where length falls 62.3% for a 0.48% accuracy drop, while Inference Scaling Laws lists it without a stated number. No archived source gives a standalone MBPP accuracy-versus-token-count figure for a reasoning model.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [Accuracy-Efficiency Tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [AIME](aime.md), [AIME 2025](aime-2025.md), [AMC](amc.md), [AMC23](amc23.md), [ARC-Challenge](arc-challenge.md), [Best-of-N](../methods/best-of-n.md), [C4](../methods/c4.md), [chain-of-thought compression](../concepts/chain-of-thought-compression.md), [CommonsenseQA](commonsenseqa.md), [Compute-optimal inference](../concepts/compute-optimal-inference.md), [confidence calibration](../concepts/confidence-calibration.md), [DeepSeek-R1-Distill-Qwen-1.5B](../methods/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../methods/deepseek-r1-distill-qwen-7b.md), [early exit](../methods/early-exit.md), [GPQA-Diamond](gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM-Hard](gsm-hard.md), [GSM8K](gsm8k.md), [HellaSwag](hellaswag.md), [HumanEval](humaneval.md), [LiveCodeBench](livecodebench.md), [LiveCodeBench-v6](livecodebench-v6.md), [majority voting](../methods/majority-voting.md), [MATH](math.md), [MATH-500](math-500.md), [MathQA](mathqa.md), [MMLU](mmlu.md), [MMLU-STEM](mmlu-stem.md), [O1-Pruner](../methods/o1-pruner.md), [Omni-MATH](omni-math.md), [overthinking](../concepts/overthinking.md), [process reward model](../concepts/process-reward-model.md), [Qwen2.5-Instruct](../methods/qwen2-5-instruct.md), [Redundant Self-Verification](../concepts/redundant-self-verification.md), [Reinforcement Learning with Verifiable Rewards](../methods/reinforcement-learning-with-verifiable-rewards.md), [s1K-1.1](s1k-1-1.md), [Still](still.md), [StrategyQA](strategyqa.md), [SVAMP](svamp.md), [test-time compute scaling](../concepts/test-time-compute-scaling.md), [tree-search decoding](../methods/tree-search-decoding.md), [underthinking](../concepts/underthinking.md), [weighted voting](../methods/weighted-voting.md)

## Appears in

- [Commit Locally, Exit Globally: Coordinating Adaptive Sampling and Early Exit in Diffusion Language Models](../../archive/papers/2026/arxiv-2607-28166/summary.md) — C4 accelerates diffusion language model decoding with two separate gates: one that decides when the whole sequence may stop, by checking that the extracted answer span is both confident and unchanged for several steps, and one that decides which token positions a step may commit, by committing only a boundary-anchored run and confirming deferred positions one step later.
- [Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving](../../archive/papers/2025/title-0d818df77a2dc810/summary.md) — An empirical study of compute-optimal inference that measures accuracy against FLOPs for greedy decoding, sampling with majority and weighted voting, best-of-n and tree search across model sizes, and introduces REBASE, a reward-guided tree search.
- [SuCo: Sufficiency-guided Continuous Adaptive Reasoning](../../archive/papers/2026/title-b37859867120f044/summary.md) — Defines the Minimal Sufficient CoT — the shortest reasoning prefix at which the model's confidence in the ground-truth answer crosses a difficulty-adaptive threshold — and trains on it via supervised fine-tuning plus a GRPO stage whose reward penalises both over- and under-thinking, so reasoning length is calibrated continuously rather than by discrete modes.
- [ShorterBetter: Guiding Reasoning Models to Find Optimal Inference Length for Efficient Reasoning](../../archive/papers/2025/title-d40396527f776f1d/summary.md) — ShorterBetter takes the length of the shortest correct response in a sampled group as a per-problem target and rewards the model for matching it, cutting output length by 50%-80% on DeepSeek-Distill-Qwen-1.5B/7B.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
