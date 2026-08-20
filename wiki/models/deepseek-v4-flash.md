# DeepSeek-V4-Flash

<!-- auto:begin -->

A fast DeepSeek model appearing twice in this archive as an evaluation subject. On the verified financial-reasoning benchmark it is one of two models carried through the full robustness suite, scoring 96.4 and 95.6 percent clean and then falling by 29.6 and 47.0 points on average under six perturbation types -- with unit and scale shifts costing the most (down to 22.0 percent on real filings) and all perturbations combined leaving 17.0 percent, at which point its gap to the stronger model narrows to 9 points. It also appears in the contamination-mitigation work that replaces a summary metric scoreable by cancellation with a per-question stratified one. Neither source describes the model itself; its value here is as the second point in a paired robustness comparison.

- **Kind**: model
- **Also called**: DeepSeek-v4-Flash
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [adversarial robustness](../concepts/adversarial-robustness.md), [ALFWorld](../datasets/alfworld.md), [benchmark contamination](../concepts/benchmark-contamination.md), [benchmark design](../concepts/benchmark-design.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [compute allocation](../concepts/compute-allocation.md), [construct validity](../concepts/construct-validity.md), [FinQA](../datasets/finqa.md), [gpt-oss-120b](gpt-oss-120b.md), [greedy decoding](../methods/greedy-decoding.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [in-context learning](../concepts/in-context-learning.md), [Llama-3.3-70B](llama-3-3-70b.md), [long-horizon agency](../concepts/long-horizon-agency.md), [LoRA](../methods/lora.md), [memorization](../concepts/memorization.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [Qwen3.5-27B](qwen3-5-27b.md), [Qwen3.5-4B](qwen3-5-4b.md), [Qwen3.5-9B](qwen3-5-9b.md), [Qwen3.6-27B](qwen3-6-27b.md), [Qwen3-8B](qwen3-8b.md), [reasoning depth](../concepts/reasoning-depth.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [selective prediction](../concepts/selective-prediction.md), [self-correction](../concepts/self-correction.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [tool orchestration](../concepts/tool-orchestration.md)

## Appears in

- [Zero Gap Is Not Restoration: Stratified Per-Question Probability Evaluation and Step-wise Mitigation of Benchmark Contamination](../../archive/papers/2026/arxiv-2608-07341/summary.md) — Shows that the standard metric for judging contamination-mitigation strategies can be scored by cancellation rather than by restoration, replaces it with a per-question stratified metric under which the published ranking reverses, and proposes a mitigation that decides its intervention during decoding instead of from a prior estimate.
- [V-FiLLM: Verified Financial LLM Reasoning Benchmark](../../archive/papers/2026/arxiv-2608-11047/summary.md) — Generates financial reasoning benchmarks from executable computation trees over real tables so that answers are correct by construction with no model in the labelling loop, exposes four independently controllable difficulty axes, and finds that unit and scale perturbations collapse the strongest model from 98.4 percent to 3.0.
- [Diagnosis Before Recovery: Turning Agent Failures into Selective Self-Correction](../../archive/papers/2026/arxiv-2608-11772/summary.md) — Profiles the dominant failure mode of an agent task family on development data, then freezes a policy that permits only the recovery interventions matched to that failure -- so a failure decides which repair is admissible and how much evidence to spend, rather than triggering more context indiscriminately.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
