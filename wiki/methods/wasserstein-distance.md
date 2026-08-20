# Wasserstein distance

<!-- auto:begin -->

A distance between two probability distributions that accounts for how far mass has to move, used in both sources where the object of interest is a distribution rather than a point estimate. The student-simulation work uses it as its primary fidelity metric, measuring how closely a simulator's generated code matches the distribution of real student submissions on pass rate, code length, syntax-tree depth and width, and style violations, with 500 bootstrap resamples for intervals -- which is a stricter and more appropriate target than accuracy when the goal is to resemble a population rather than to solve a task, and which is what exposes the over-competence of prompted models. The flow-based RL work uses the same family of ideas for a different purpose, aligning the distribution of training rollouts with the deterministic sampler used at test time. Neither source studies the metric; between them they mark where it earns its place, which is any claim of the form 'this system behaves like that population' -- a claim an accuracy number cannot express and a mean cannot check.

- **Kind**: method
- **Also called**: earth mover's distance, optimal transport distance
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [bootstrap resampling](bootstrap-resampling.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [exploration](../concepts/exploration.md), [flow matching](flow-matching.md), [GPT-5](../models/gpt-5.md), [GRPO](grpo.md), [knowledge distillation](knowledge-distillation.md), [Llama](../models/llama.md), [LLM-as-a-judge](llm-as-a-judge.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [supervised fine-tuning](supervised-fine-tuning.md), [train-inference gap](../concepts/train-inference-gap.md)

## Appears in

- [LC-GRPO: Bridging Train-Inference Gap for Flow-Based GRPO with Langevin Correction](../../archive/papers/2026/arxiv-2608-05600/summary.md) — A GRPO variant for flow-based generative models that replaces SDE training rollouts with an ODE step plus a Langevin correction, aligning training samples with the deterministic sampler used at test time.
- [INSIDE the Student's Mind: Jointly Modeling Latent Reasoning and Action in LLM Student Simulators](../../archive/papers/2026/arxiv-2608-10492/summary.md) — Fine-tunes student simulators on paired internal-dialogue traces and code edits rather than on actions alone, and measures the result on two axes at once -- how closely generated code matches the distribution of real student submissions, and how well the generated reasoning explains the specific edit that followed.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
