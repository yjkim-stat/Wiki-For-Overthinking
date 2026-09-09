# Deepseek-R1-1.5B

<!-- auto:begin -->

DeepSeek-R1-1.5B is one of the reasoning-model checkpoints covered by two archived studies on overthinking and reasoning quality; neither source reports results broken out for this checkpoint specifically. It is among the models covered by a comparison of test-time-scaling methods (Outcome Reward Modeling, Process Reward Modeling, Budget Forcing) run under a FLOPs-matched budget on the 55-language MCLM competition-math benchmark. It is also among the models covered by a mechanistic study that computes a LogitLens-based Reasoning Score to distinguish deep reasoning from shallow pattern-matching, uses it to detect hallucination patterns -- including a perplexity-correlated 'spurious verification' overthinking pattern -- and shapes an RL training reward (GRPO-R) from the same score.

- **Kind**: model
- **Also called**: DeepSeek-R1-1.5B
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [2WikiMultihopQA](../datasets/2wikimultihopqa.md), [AIME 2024](../datasets/aime-2024.md), [AMC23](../datasets/amc23.md), [Bamboogle](../datasets/bamboogle.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-4o](gpt-4o.md), [GPT-4o-mini](gpt-4o-mini.md), [GRPO](../methods/grpo.md), [HotpotQA](../datasets/hotpotqa.md), [MATH500](../datasets/math500.md), [MuSiQue](../datasets/musique.md), [o3-mini](o3-mini.md), [OpenR1-Math-220k](../datasets/openr1-math-220k.md), [Qwen2.5-1.5B-Instruct](qwen2-5-1-5b-instruct.md), [Qwen2.5-Math-1.5B-Instruct](qwen2-5-math-1-5b-instruct.md), [Qwen2.5-Math-7B-Instruct](qwen2-5-math-7b-instruct.md), [reasoning hallucination](../concepts/reasoning-hallucination.md)

## Appears in

- [Linguistic Generalizability of Test-Time Scaling in Mathematical Reasoning](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-699/summary.md) — Under a FLOPs-matched budget across three test-time scaling methods (Outcome Reward Modeling, Process Reward Modeling, Budget Forcing) on a new 55-language competition-math benchmark (MCLM), all three methods yield large gains in English (e.g. Budget Forcing +20 points on AIME) but only ~1.9-2 points average gain across other languages, and reward-model-guided scaling (ORM) matches or beats reasoning-trace-length scaling (Budget Forcing) once FLOPs are equalized -- with more test-time compute also increasing cross-lingual performance variance rather than reducing it.
- [Detection and Mitigation of Hallucination in Large Reasoning Models: A Mechanistic Perspective](../../archive/papers/2025/local-54dd9729250c51ac/summary.md) — Defines a Reasoning Score from the Jensen-Shannon divergence between LogitLens-projected late-layer and final-layer vocabulary distributions to distinguish deep reasoning from shallow pattern-matching, uses it to identify hallucination patterns (early-step fluctuation, incorrect backtracking, and a perplexity-correlated 'spurious verification' overthinking pattern) and build a post-hoc detector (RHD), and separately shapes an RL training reward from the same score (GRPO-R) to reduce reasoning hallucinations.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
