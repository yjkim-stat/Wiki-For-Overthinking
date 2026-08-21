# Manifold Steering

<!-- auto:begin -->

An overthinking-mitigation technique that identifies overthinking as movement along a low-dimensional manifold in a reasoning model's activation space, then steers activations along that manifold at inference time to shorten reasoning. Its source paper reports cutting output tokens up to 71% while maintaining or improving accuracy; the 'Don't Overthink It' survey categorizes it under 'Representation Engineering', alongside similar steering-vector methods (SEAL, Pre-allocated Direction Vectors, Thinking Progress Vector).

- **Kind**: method
- **Also called**: activation steering, representation engineering
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [A*-Thought](a-thought.md), [Accuracy-Length Tradeoff](../concepts/accuracy-length-tradeoff.md), [activation steering](activation-steering.md), [Ada-R1](ada-r1.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [chain-of-thought compression](../concepts/chain-of-thought-compression.md), [DEER](deer.md), [DRP](drp.md), [early exit](early-exit.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [LASER](laser.md), [LC-R1](lc-r1.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH-500](../datasets/math-500.md), [mechanistic interpretability](../concepts/mechanistic-interpretability.md), [NoThinking](nothinking.md), [NOWAIT](nowait.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](../concepts/overthinking.md), [PLAN-AND-BUDGET](plan-and-budget.md), [S-GRPO](s-grpo.md), [SEAL](seal.md), [SelfBudgeter](selfbudgeter.md), [SPIRIT](spirit.md), [StrategyQA](../datasets/strategyqa.md), [test-time compute scaling](../concepts/test-time-compute-scaling.md), [Thinkless](thinkless.md), [TokenSkip](tokenskip.md), [TrimR](trimr.md), [underthinking](../concepts/underthinking.md), [VeriThinker](verithinker.md)

## What we have settled

- **Established** — Manifold Steering's repository (github.com/Aries-iai/Manifold_Steering) exists and names the paper as its official implementation, but as of 2026-08-21 the repo itself notes the code was not yet uploaded ("available next month") -- so the paper's headline 71% token-reduction result cannot yet be independently verified by running the code.
  - Checked the repository directly rather than trusting the paper's own 'code is available at' claim; the repo's current state (README present, implementation pending) is worth recording so a later reader does not assume it is runnable today.

## Appears in

- [Don't Overthink It: A Survey of Efficient R1-style Large Reasoning Models](../../archive/papers/2025/local-6c80b6fd388d671e/summary.md) — A survey that organizes methods for making R1-style large reasoning models reason efficiently (i.e., avoid overthinking) into two axes: single-model optimization and multi-model collaboration.
- [Efficient Reasoning with Balanced Thinking](../../archive/papers/2026/title-7a3e08192f168bcb/summary.md) — ReBalance is a training-free inference-time steering method that reads a reasoning model's token confidence to detect overthinking or underthinking and applies a hidden-state steering vector to shorten or extend the chain of thought accordingly.
- [Mitigating Overthinking in Large Reasoning Models via Manifold Steering](../../archive/papers/2025/title-b4ba27743c499d8d/summary.md) — Identifies that overthinking in large reasoning models corresponds to a low-dimensional manifold in activation space and proposes projecting steering interventions onto that manifold to cut output tokens by up to 71% without hurting accuracy.

## Checked against

- [https://github.com/Aries-iai/Manifold_Steering](https://github.com/Aries-iai/Manifold_Steering) — github.com · code · retrieved 2026-08-21
  - _The official implementation for "Mitigating Overthinking in Large Reasoning Models via Manifold Steering" -- the repository notes the code itself was not yet uploaded at the time of this check ("code will be available next month"), so this confirms the paper has a claimed official repo but not yet a runnable release._

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
