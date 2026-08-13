# Qwen3-4B

<!-- auto:begin -->

A small reasoning model, and the most heavily used single checkpoint in this archive's recent readings — three sources apply quite different instruments to it. One ternarizes it and makes it the model on which the whole calibration finding rests: the same quantization procedure yields 0.00 or 58.40 on Math-500 depending only on whether the calibration text contains the model's own reasoning traces. One includes it in an observability sweep asking what a monitor can read from its traces. One steers it by hidden-state L2 norm, lifting AIME24 from 60.00 to 70.00, and reports the sensitivity that matters more — replacing the adaptive threshold with a fixed one collapses that to 23.33. Its recurrence is itself informative: it is small enough to sweep exhaustively and capable enough that interventions move it, which is what makes a checkpoint become a de facto testbed.

- **Kind**: model
- **Also called**: Qwen3-4B-Base
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [activation steering](../methods/activation-steering.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [BBH](../datasets/bbh.md), [chain of thought](../methods/chain-of-thought.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [Gemma-3-4B](gemma-3-4b.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-oss-120b](gpt-oss-120b.md), [gpt-oss-20b](gpt-oss-20b.md), [GSM8K](../datasets/gsm8k.md), [HumanEval+](../datasets/humaneval.md), [IFEval](../datasets/ifeval.md), [linear probe](../methods/linear-probe.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [logistic regression](../methods/logistic-regression.md), [MATH500](../datasets/math500.md), [MBPP+](../datasets/mbpp.md), [MMLU-Pro](../datasets/mmlu-pro.md), [monitorability](../concepts/monitorability.md), [Omni-MATH](../datasets/omni-math.md), [OpenCodeInstruct](../datasets/opencodeinstruct.md), [overthinking](../concepts/overthinking.md), [Phi-4-reasoning](phi-4-reasoning.md), [Qwen3-1.7B](qwen3-1-7b.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-235B-A22B](qwen3-235b-a22b.md), [Qwen3-30B-A3B](qwen3-30b-a3b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-8B](qwen3-8b.md), [self-correction](../concepts/self-correction.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [TruthfulQA](../datasets/truthfulqa.md), [verbosity](../concepts/verbosity.md)

## Appears in

- [Attend to Your Own Thoughts: Breaking the Barrier for Post-Training Quantization of Reasoning LLMs through the Lens of 1.58-Bit Quantization](../../archive/papers/2026/arxiv-2608-01078/summary.md) — Finds that ternary post-training quantization of a reasoning model collapses because the calibration set is web text, and repairs it by calibrating on chain-of-thought traces the target model generates for itself.
- [How Much Does a Reasoning Summary Reveal? An Observability Ladder for Large Language Models](../../archive/papers/2026/arxiv-2608-02089/summary.md) — Holds one completed reasoning run fixed and varies only what a monitor is allowed to inspect — response, self-summary, full trace, internals — and finds the summary's value nearly vanishes once the monitor already has the prompt, so monitorability is a property of the display and the reader jointly rather than of the text.
- [The Tell-Tale Norm: L2 Magnitude as a Signal for Reasoning Dynamics in Large Language Models](../../archive/papers/2026/local-f92e5f936a3c7422/summary.md) — Argues that the L2 norm of a hidden state is a training-free proxy for how hard a model is reasoning at that layer and token, proves it bounds the activation of SAE-identified reasoning features, and uses norm peaks to decide where to recurse a layer, where to steer, and which sampled response to keep.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
