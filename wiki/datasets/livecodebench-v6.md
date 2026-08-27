# LiveCodeBench-v6

<!-- auto:begin -->

The sixth release window of LiveCodeBench, used in the archive as a free-form competitive-programming set on which test-time-scaling and length-calibration methods are checked outside mathematics. Consilience is the only source reporting numbers on it: with n = 64 sampled completions its reasoning-isolated variant raises GPT-OSS-120B to 69.7% against Pass@1's 65.7% and self-certainty's degraded 64.5%, and Qwen to 60.4-60.9% against 55.3%, with the gain concentrated on hard problems (AUROC 0.61-0.62 for separating correct completions, versus 0.47-0.50 for mean confidence) and neutral on easy ones. SuCo folds it into an eight-benchmark average without a per-set figure, and Lightning OPD 2.0 names both v5 and v6 as evaluation sets but reports only a v5 number (63.0%), so the archive's version labelling is inconsistent and no v6 token-count or length figure is recorded anywhere.

- **Kind**: dataset
- **Also called**: LiveCodeBench v6, LiveCodeBench(v6), LiveCodeBench-v6
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [best-of-n selection](../methods/best-of-n-selection.md), [CommonsenseQA](commonsenseqa.md), [DeepScaleR-preview (training)](deepscaler-preview-training.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../methods/deepseek-r1-distill-qwen-7b.md), [GPQA-Diamond](gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [HMMT 2025](hmmt-2025.md), [HumanEval](humaneval.md), [LiveCodeBench](livecodebench.md), [LiveCodeBench (v5)](livecodebench-v5.md), [MATH500](math500.md), [MBPP](mbpp.md), [MMLU-STEM](mmlu-stem.md), [Overthinking](../concepts/overthinking.md), [Pass@1](../concepts/pass-1.md), [s1K-1.1](s1k-1-1.md), [StrategyQA](strategyqa.md), [SWE-bench Verified](swe-bench-verified.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [underthinking](../concepts/underthinking.md)

## Appears in

- [Consilience for Verifier-Free Test-Time Scaling](../../archive/papers/2026/arxiv-2608-09898/summary.md) — Introduces consilience, a verifier-free test-time-scaling selection metric that picks the sampled reasoning rollout whose confidence starts low (exploratory) and ends high (convergent), fixing a failure mode where naive confidence maximization favors confidently wrong answers on hard problems.
- [Anti-Length Shift: Dynamic Outlier Truncation for Training Efficient Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1047/summary.md) — Identifies 'length shift' -- reasoning models progressively generate longer responses on already-correctly-solved (zero-gradient) training queries during RLVR, because reasoning-word emission learned for hard problems generalizes indiscriminately to easy ones -- and fixes it with Dynamic Outlier Truncation (DOT), a training-time RL intervention that truncates only the statistical outlier-length tail of all-correct rollout groups (affecting <0.5% of responses) while leaving hard queries unconstrained, cutting AIME-24 token usage 78% while increasing accuracy over the initial policy and beating prior efficient-reasoning methods.
- [SuCo: Sufficiency-guided Continuous Adaptive Reasoning](../../archive/papers/2026/title-b37859867120f044/summary.md) — Defines the Minimal Sufficient CoT — the shortest reasoning prefix at which the model's confidence in the ground-truth answer crosses a difficulty-adaptive threshold — and trains on it via supervised fine-tuning plus a GRPO stage whose reward penalises both over- and under-thinking, so reasoning length is calibrated continuously rather than by discrete modes.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
