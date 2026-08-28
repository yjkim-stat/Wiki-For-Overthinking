# RLOO

<!-- auto:begin -->

None of the three sources describe RLOO's mechanism directly in the material given; it appears as a named baseline/reference algorithm alongside these papers' GRPO-based approaches. SLPO extends outcome-reward RL to latent reasoners with a learned stopping head; TRACE measures implicit reward hacking via a reward-vs-CoT-length curve; DRPO diagnoses and fixes a length-penalty pathology specific to GRPO's group-relative advantage. How RLOO specifically compares is not stated in the supplied notes.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Accuracy-Efficiency Score (AES)](../concepts/accuracy-efficiency-score-aes.md), [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [AIME](../datasets/aime.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [COCONUT](coconut.md), [CODI](codi.md), [CoLaR](colar.md), [Efficient Reasoning](../concepts/efficient-reasoning.md), [Group-Relative Advantage](../concepts/group-relative-advantage.md), [GRPO](grpo.md), [GSM-Hard](../datasets/gsm-hard.md), [GSM8K](../datasets/gsm8k.md), [GSM8K-Test](../datasets/gsm8k-test.md), [Latent reasoning](../concepts/latent-reasoning.md), [Length reward](../concepts/length-reward.md), [Llama-3-8B](../models/llama-3-8b.md), [MATH500](../datasets/math500.md), [MultiArith](../datasets/multiarith.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [reasoning effort](../concepts/reasoning-effort.md), [Test-Time Scaling](../concepts/test-time-scaling.md), [Thinking Budget](../concepts/thinking-budget.md)

## Appears in

- [SLPO: Scaling Latent Reasoning via a Surrogate Policy](../../archive/papers/2026/arxiv-2607-19691/summary.md) — SLPO adds outcome-reward RL to autoregressive latent (continuous-vector) reasoners by scoring latent transitions with a Gaussian surrogate density built from MC-dropout forwards, and by training a stopping head that turns a fixed latent thinking budget into a learned per-instance horizon.
- [Is it Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort](../../archive/papers/2026/title-49c61dced5ecc63a/summary.md) — TRACE detects implicit reward hacking by truncating a model's chain of thought at increasing fractions, forcing an answer at each cut, and scoring the area under the resulting reward-versus-CoT-length curve — a hacking model reaches high reward with little of its reasoning consumed.
- [DRPO: Efficient Reasoning via Decoupled Reward Policy Optimization](../../archive/papers/2026/title-68327bf6b9e4e869/summary.md) — Diagnoses why adding a length penalty to GRPO degrades accuracy — the group-relative advantage can turn correct-but-long rollouts negative — and fixes it by normalising the reward of correct rollouts only against other correct rollouts.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
