# Llama3-8B

<!-- auto:begin -->

Llama3-8B is a language model that two archived papers evaluate on, not a concept, method or dataset; the wiki has no kind for a model, so it is filed under the least wrong of the three available. RAEE uses it as one of four early-exit backbones, reporting 57.39 average accuracy across eight classification tasks against a 36.06-41.80 baseline range, and roughly halved inference latency on the billion-parameter backbones (it and Gemma-7B) where the smaller ones gained little. TRACE runs implicit-reward-hacking detection mainly on Qwen2.5 from 1.5B to 72B 'with some Llama3-8B evaluations', so there it is a secondary check rather than the main testbed. Neither paper describes the model itself, and the two spell it differently.

- **Kind**: method
- **Also called**: Llama-3-8B
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [early exit](early-exit.md), [GRPO](grpo.md), [overthinking](../concepts/overthinking.md), [reasoning effort](../concepts/reasoning-effort.md), [RLOO](rloo.md), [SST-2](../datasets/sst-2.md), [T5-Large](t5-large.md)

## Appears in

- [Is it Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort](../../archive/papers/2026/title-49c61dced5ecc63a/summary.md) — TRACE detects implicit reward hacking by truncating a model's chain of thought at increasing fractions, forcing an answer at each cut, and scoring the area under the resulting reward-versus-CoT-length curve — a hacking model reaches high reward with little of its reasoning consumed.
- [RAEE: A Robust Retrieval-Augmented Early Exit Framework for Efficient Inference](../../archive/papers/2026/title-5e9b243e4d404cc8/summary.md) — RAEE decides which transformer layer to exit at by retrieving the exit behaviour of similar training examples from a pre-built database, instead of training internal classifiers or using heuristics.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
