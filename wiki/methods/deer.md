# DEER

<!-- auto:begin -->

DEER is a training-free decoding method that ends a large reasoning model's chain of thought early: it treats the points where the model switches thoughts (marked in practice by transition tokens such as 'Wait', with an entropy-based detector as fallback) as candidate exits, prompts the model there for a trial answer, and stops the thinking block when that answer's confidence, the geometric mean of its token probabilities, exceeds a threshold set to 0.95. Across 10 benchmarks and 11 models it cuts 19.1%-80.1% of chain-of-thought tokens while raising accuracy by 0.3%-5.0%, though the compression is strongly difficulty-dependent: roughly 67% on GSM8K against roughly 25% on AIME 2024 for the same model, so the saving is largest where inference was already cheap. A branch-parallel decoding scheme overlaps the trial-answer check with continued reasoning so it does not serialise against generation, and a variant DEER-PRo averages several prompt-varied inductions minus a mean-absolute-deviation penalty. Other archived work treats it as the standard baseline for this family: ReBalance compares against it, and DiffAdapt reports end-to-end inference 5x faster than DEER.

- **Kind**: method
- **Also called**: DEER-PRo
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [A*-Thought](a-thought.md), [Accuracy-Length Tradeoff](../concepts/accuracy-length-tradeoff.md), [activation steering](activation-steering.md), [Ada-R1](ada-r1.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [BigCodeBench](../datasets/bigcodebench.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [chain-of-thought prompting](../concepts/chain-of-thought-prompting.md), [DAST](dast.md), [DRP](drp.md), [Dynamic Early Exit](dynamic-early-exit.md), [Dynasor](dynasor.md), [Early Exit](early-exit.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [Hidden-State Probing](../concepts/hidden-state-probing.md), [HumanEval](../datasets/humaneval.md), [Laser](laser.md), [LC-R1](lc-r1.md), [LiveCodeBench](../datasets/livecodebench.md), [Manifold Steering](manifold-steering.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [MMLU-Pro](../datasets/mmlu-pro.md), [NoThinking](nothinking.md), [NOWAIT](nowait.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [PLAN-AND-BUDGET](plan-and-budget.md), [S-GRPO](s-grpo.md), [SEAL](seal.md), [SelfBudgeter](selfbudgeter.md), [SPIRIT](spirit.md), [StrategyQA](../datasets/strategyqa.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Test-Time Scaling](../concepts/test-time-scaling.md), [Thinkless](thinkless.md), [ThinkPrune](thinkprune.md), [TokenSkip](tokenskip.md), [TrimR](trimr.md), [underthinking](../concepts/underthinking.md), [VeriThinker](verithinker.md), [vLLM](vllm.md)

## Appears in

- [Don't Overthink It: A Survey of Efficient R1-style Large Reasoning Models](../../archive/papers/2025/local-6c80b6fd388d671e/summary.md) — A survey that organizes methods for making R1-style large reasoning models reason efficiently (i.e., avoid overthinking) into two axes: single-model optimization and multi-model collaboration.
- [DiffAdapt: Difficulty-Adaptive Reasoning for Token-Efficient LLM Inference](../../archive/papers/2026/title-18b94d8204ec3367/summary.md) — DiffAdapt trains a small probe on a reasoning model's hidden state to classify each question as Easy/Normal/Hard and picks a matching prompt, temperature and token limit, cutting token use without retraining the model.
- [Efficient Reasoning with Balanced Thinking](../../archive/papers/2026/title-7a3e08192f168bcb/summary.md) — ReBalance is a training-free inference-time steering method that reads a reasoning model's token confidence to detect overthinking or underthinking and applies a hidden-state steering vector to shorten or extend the chain of thought accordingly.
- [Dynamic Early Exit in Reasoning Models](../../archive/papers/2026/title-f508a5b012a33fd1/summary.md) — DEER is a training-free decoding method that watches for the points where a reasoning model switches thought chains, prompts it for a trial answer there, and terminates the chain of thought when the trial answer's token confidence exceeds a threshold.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
