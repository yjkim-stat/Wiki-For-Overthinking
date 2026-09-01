# Nemotron-32B

<!-- auto:begin -->

Nemotron-32B is one of the model sizes examined in a truncation-based diagnostic across 11 languages measuring how strongly large reasoning models already know the answer before finishing their explicit reasoning trace (multilingual latent reasoning), and appears in a study extending reasoning depth via recurrence, memory and test-time methods on a controlled cellular-automata benchmark designed to preclude memorization.

- **Kind**: model
- **Also called**: Nemotron-32B
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [DeepSeek-R1-Distill-Qwen-14B](deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [Gemini 2.5 Flash](gemini-2-5-flash.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [Latent reasoning](../concepts/latent-reasoning.md), [Llama 3.3 70B](llama-3-3-70b.md), [logit lens](../methods/logit-lens.md), [Qwen2.5-32B-Instruct](qwen2-5-32b-instruct.md)

## Appears in

- [Large Reasoning Models Are (Not Yet) Multilingual Latent Reasoners](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1121/summary.md) — Using a truncation-based diagnostic across 11 languages, 3 model sizes, and 2 benchmarks, this paper measures how strongly LRMs already know the answer before finishing their explicit reasoning trace ('latent reasoning'), finding it exists but is uneven -- strong in resource-rich languages on easy tasks, weak in low-resource languages, and largely absent on harder benchmarks -- and that the internal layer-wise dynamics driving it are strikingly consistent across languages, converging toward an English-centered latent pathway that is not explained by memorization alone.
- [Beyond Memorization: Extending Reasoning Depth with Recurrence, Memory and Test-Time Compute Scaling](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2103/summary.md) — Using a controlled 1D-cellular-automata benchmark with disjoint train/test rule sets (precluding memorization), this paper shows models can genuinely infer unseen local rules but fixed-depth architectures collapse sharply beyond one-step-ahead prediction, that most frontier LLMs (except Gemini-2.5-Pro) fail even the simplest natural-language proxy of this task, and that depth -- not width -- is what drives multi-step accuracy, with chain-of-thought-style token-level supervision reaching near-perfect accuracy up to 4 look-ahead steps while RL (GRPO) without intermediate supervision reaches only 3 steps and architectural depth-extension tricks (ACT, recurrent memory) each add only about one effective step.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
