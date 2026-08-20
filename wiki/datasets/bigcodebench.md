# BigCodeBench

<!-- auto:begin -->

A code-generation benchmark used in both sources as an evaluation set rather than a subject. Its most informative appearance is in the probing-robustness sweep, where it is one of two benchmarks whose disagreement is the finding: on this one, averaging hidden states over the response beats reading the last token by more than twenty points, while on the other the preference reverses -- and the two cancel in a pooled analysis, leaving a decisive factor ranked at under 1 percent of variance. It is also where the fitting data dominates, carrying 75 percent of variance against 16 for construction and 9 for the model, and where a synthetic fitting source drops the signal to 22 percent against a 25 percent chance floor. It appears again in the dynamic early-exit work. Neither source describes its construction; in this archive it is chiefly one half of a pair whose disagreement establishes that probing recipes do not transfer.

- **Kind**: dataset
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [cross-validation](../methods/cross-validation.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER](../methods/deer.md), [detection versus control](../concepts/detection-versus-control.md), [difference-in-means direction](../methods/difference-in-means-direction.md), [distribution shift](../concepts/distribution-shift.md), [Dynasor](../methods/dynasor.md), [early exit](../methods/early-exit.md), [GPQA-Diamond](gpqa-diamond.md), [GSM8K](gsm8k.md), [HumanEval+](humaneval.md), [identifiability](../concepts/identifiability.md), [interpretability illusion](../concepts/interpretability-illusion.md), [layer selection](../methods/layer-selection.md), [linear probe](../methods/linear-probe.md), [LiveCodeBench](livecodebench.md), [MATH500](math500.md), [MBPP+](mbpp.md), [measurement invariance](../concepts/measurement-invariance.md), [OlympiadBench](olympiadbench.md), [operating point](../concepts/operating-point.md), [out-of-domain generalization](../concepts/out-of-domain-generalization.md), [overthinking](../concepts/overthinking.md), [Qwen](../models/qwen.md), [Qwen3-14B](../models/qwen3-14b.md), [QwQ-32B](../models/qwq-32b.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [selection bias](../concepts/selection-bias.md), [test-time compute](../concepts/test-time-compute.md), [token-level entropy](../concepts/token-level-entropy.md), [vLLM](../methods/vllm.md)

## Appears in

- [On the Robustness of LLMs' Internal Representation of Code Correctness](../../archive/papers/2026/arxiv-2608-08266/summary.md) — Asks whether a published internal signal for code correctness is a property of the model or of the one extraction recipe used to find it, sweeps every design choice systematically, and finds no configuration is best anywhere -- with the benchmark deciding which choice wins, and a mismatched fitting source able to drive the signal below chance.
- [Dynamic Early Exit in Reasoning Models](../../archive/papers/2025/local-a1d9fa1eb8899dfc/summary.md) — Detects the points where a reasoning model switches thought chains, interrupts to induce a trial answer, and stops generation when that answer's confidence is high enough — cutting chain-of-thought length substantially while raising accuracy, with no training.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
