# bootstrap resampling

<!-- auto:begin -->

Resampling the observed data many times to get an interval or a null for a statistic that has no convenient closed form. Both sources use it on quantities where no analytic distribution is available. The student-simulation work resamples 500 times to put intervals on Wasserstein distances between the distribution of model-generated code and real student submissions, which is what makes a comparison of distributional fidelity across models readable at all. The symbolic-benchmark work uses it on multi-instance consistency scores, where the quantity of interest is whether a model solves several instantiations of the same problem rather than the accuracy on any one. Neither source studies the estimator; between them they mark where it earns its keep -- distances between distributions and consistency rates across paired instances are exactly the statistics that a standard error formula does not cover.

- **Kind**: method
- **Also called**: bootstrap
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [benchmark contamination](../concepts/benchmark-contamination.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [DAPO](dapo.md), [DAPO-Qwen-32B](../models/dapo-qwen-32b.md), [GPT-5](../models/gpt-5.md), [GSM8K](../datasets/gsm8k.md), [knowledge distillation](knowledge-distillation.md), [Llama](../models/llama.md), [LLM-as-a-judge](llm-as-a-judge.md), [MATH500](../datasets/math500.md), [memorization](../concepts/memorization.md), [OlympiadBench](../datasets/olympiadbench.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [PRIME](prime.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-235B-A22B](../models/qwen3-235b-a22b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [RLVR](rlvr.md), [Skywork-OR1-Math-7B](../models/skywork-or1-math-7b.md), [supervised fine-tuning](supervised-fine-tuning.md), [vLLM](vllm.md), [Wasserstein distance](wasserstein-distance.md), [Wilson confidence interval](wilson-confidence-interval.md)

## Appears in

- [INSIDE the Student's Mind: Jointly Modeling Latent Reasoning and Action in LLM Student Simulators](../../archive/papers/2026/arxiv-2608-10492/summary.md) — Fine-tunes student simulators on paired internal-dialogue traces and code edits rather than on actions alone, and measures the result on two axes at once -- how closely generated code matches the distribution of real student submissions, and how well the generated reasoning explains the specific edit that followed.
- [VAR-MATH: Probing True Mathematical Reasoning in LLMs via Symbolic Multi-Instance Benchmarks](../../archive/papers/2026/local-d62cc27b0209da49/summary.md) — Converts AMC23 and AIME24/25 into symbolic templates whose constants are replaced by sampled variables, requires a model to solve several instantiations of each problem, and finds RL-finetuned models lose most of their reported accuracy under that consistency requirement.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
