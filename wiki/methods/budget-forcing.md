# Budget Forcing

<!-- auto:begin -->

Controlling a reasoning model's chain-of-thought length by inserting a keyword at inference time -- most commonly 'Wait' to force it to keep thinking past what it would have generated on its own, or a stop signal to cut it short. 'Wait, Do We Need to Wait?' stress-tests this technique across model families, non-reasoning models and alternative keywords; 'When More Thinking Hurts' and the deep-search asymmetric-verification paper both study its diminishing, and eventually negative, returns as forced length grows.

- **Kind**: method
- **Also called**: Budget Forcing, budget forcing, sequential test-time scaling
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 6

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Answer Convergence](answer-convergence.md), [BrowseComp](../datasets/browsecomp.md), [Chain-of-Draft](chain-of-draft.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DEER](deer.md), [Early-Exit Inference](../concepts/early-exit-inference.md), [GAIA](../datasets/gaia.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [HMMT 2025](../datasets/hmmt-2025.md), [MATH500](../datasets/math500.md), [NoThinking](nothinking.md), [Overthinking](../concepts/overthinking.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-8B](../models/qwen3-8b.md), [sequential test-time scaling](../concepts/sequential-test-time-scaling.md), [sequential vs. parallel test-time scaling](../concepts/sequential-vs-parallel-test-time-scaling.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [vLLM](vllm.md)

## Appears in

- [Token Budget Saturation and Mechanistic Early Detection of Reasoning Non-Convergence in Chain-of-Thought Models](../../archive/papers/2026/arxiv-2607-21433/summary.md) — Two studies on DeepSeek-R1-Distill-Qwen-7B: a budget-forcing sweep showing GSM8K and MATH-500 accuracy saturates at 256 thinking tokens while AIME splits bimodally into generations that terminate and generations that loop until the 10,000-token ceiling, and a linear-probe study showing that hidden-state activations at token 150 predict which of the two an AIME generation will become at AUC 0.608.
- [Keep, Customize, or Exit: Default Design and Token Pricing in LLM Reasoning Services](../../archive/papers/2026/arxiv-2608-13315/summary.md) — Models an LLM reasoning service as a Stackelberg game in which the provider sets a per-token price and a default reasoning-token budget while the user may keep the default, customize it, or exit, and shows the provider's optimal default sits above the budget the user would choose.
- [Early Stopping for Large Reasoning Models via Confidence Dynamics](../../archive/papers/2026/local-204ad034bca12641/summary.md) — CoDE-Stop stops reasoning when either a ramping confidence threshold is crossed or an early-step-weighted 'degeneration score' of accumulated confidence instability exceeds a threshold, targeting both trajectories that are already done and trajectories that are going nowhere, and its evaluation is the archive's first independent head-to-head of RCPD and Answer Convergence under one protocol.
- [When More Thinking Hurts: Overthinking in LLM Test-Time Compute Scaling](../../archive/papers/2026/local-32a56cfa1105c39e/summary.md) — The paper shows that extended chain-of-thought reasoning in LLMs has diminishing and eventually negative marginal utility, quantifies this 'overthinking' via answer-flip tracking, and proposes cost-aware, indicator-based early-stopping strategies that cut compute substantially with little accuracy loss.
- [Wait, Do We Need to Wait? Revisiting Budget Forcing for Sequential Test-Time Scaling](../../archive/papers/2026/title-7071aa99216bb67f/summary.md) — Revisits budget forcing -- forcing a reasoning model to keep thinking or to stop via a keyword like 'Wait' -- and empirically tests how well it generalizes across model families, non-reasoning models, and alternative keywords.
- [Pushing Test-Time Scaling Limits of Deep Search with Asymmetric Verification](../../archive/papers/2026/title-711c479b500244c5/summary.md) — Studies sequential and parallel test-time compute scaling for deep-search LLM agents and shows that allocating modest compute to a cheap verifier outperforms pushing sequential generation length further.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
