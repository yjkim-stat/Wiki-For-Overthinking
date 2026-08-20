# adversarial robustness

<!-- auto:begin -->

Whether a behaviour survives inputs written to defeat it, and in both sources the axis on which a method's ranking reverses. One builds three tiers of camouflage that disguise mathematics problems as bug reports and finds trained classifier heads collapsing to 0.00 while statistical readings of the same activations retain 92.33 and 80.67 on the first two tiers — then reports that the hardest tier defeats every lightweight method equally, at or near zero, against 64 percent for a frontier model call. The other treats self-reflection as a safety intervention against jailbreaks. Both therefore use it the same way: not as a score to improve but as the condition under which a clean-input ranking stops holding.

- **Kind**: concept
- **Also called**: robustness to adversarial inputs
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [benchmark design](benchmark-design.md), [calibration](../methods/calibration.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [CLIP](../models/clip.md), [cosine similarity](../methods/cosine-similarity.md), [DeepSeek-V4-Flash](../models/deepseek-v4-flash.md), [distribution shift](distribution-shift.md), [FinQA](../datasets/finqa.md), [GPT-4o](../models/gpt-4o.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [GPT-5](../models/gpt-5.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [GSM8K](../datasets/gsm8k.md), [hidden-state geometry](hidden-state-geometry.md), [HumanEval+](../datasets/humaneval.md), [jailbreak](jailbreak.md), [linear probe](../methods/linear-probe.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [Llama-3.3-70B](../models/llama-3-3-70b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [out-of-distribution generalization](out-of-distribution-generalization.md), [post-training](../methods/post-training.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3.5-9B](../models/qwen3-5-9b.md), [Qwen3-8B](../models/qwen3-8b.md), [reasoning depth](reasoning-depth.md), [RoBERTa](../models/roberta.md), [routing](routing.md), [safety alignment](safety-alignment.md), [sample complexity](sample-complexity.md), [self-correction](self-correction.md), [self-reflection](../methods/self-reflection.md), [superposition](superposition.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time scaling](test-time-scaling.md), [uncertainty quantification](uncertainty-quantification.md)

## Appears in

- [Training-Free versus Training-Based Intent Classification in LLMs: Accuracy, Robustness, and Failure Modes](../../archive/papers/2026/arxiv-2608-02415/summary.md) — Compares two training-free intent classifiers built from summary statistics of prefill-time activations against trained heads on the same features, and finds the trade-off is not accuracy but where each fails — trained heads win fine-grained distinctions, statistical ones give better uncertainty on mixed prompts and survive adversarial rephrasing that collapses the trained heads to zero.
- [Test-Time Scaling for Safe Text-Guided Image Generation via Intermediate Clean Estimates](../../archive/papers/2026/arxiv-2608-03284/summary.md) — Triggers a safety intervention in image diffusion from the intermediate clean-image estimate rather than from the prompt, and spends optimization only from the first timestep where a violation actually appears — so extra test-time compute is incurred on unsafe inputs and benign latency stays flat as the budget grows.
- [V-FiLLM: Verified Financial LLM Reasoning Benchmark](../../archive/papers/2026/arxiv-2608-11047/summary.md) — Generates financial reasoning benchmarks from executable computation trees over real tables so that answers are correct by construction with no model in the labelling loop, exposes four independently controllable difficulty axes, and finds that unit and scale perturbations collapse the strongest model from 98.4 percent to 3.0.
- [Self-Reflection Improves Safety of Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-678/summary.md) — Adds a Self-Reflection token that lets reasoning models recover from harmful output mid-generation, cutting harmful completion rate from 13.8% to 4.1%.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
