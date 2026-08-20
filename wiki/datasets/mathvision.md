# MathVision

<!-- auto:begin -->

A visual mathematics benchmark, used in two sources as the multimodal counterpart to the text-only mathematics sets. One audits a perturbation-based selection rule for vision-language test-time scaling on it and finds the rule's reported 31.8-point gain over majority voting is a decoding-format effect rather than a perturbation effect, once a control spends the same short-answer budget on the unperturbed image. The other includes it among the visual tasks where RLVR-trained models are measured against their base models with pass@k. Neither characterizes the benchmark itself, so what the archive records is the two experiments it appears in rather than what it contains.

- **Kind**: dataset
- **Also called**: MATH-Vision, Math-Vision
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME 2024](aime-2024.md), [AMC23](amc23.md), [best-of-n](../methods/best-of-n.md), [Borda count](../methods/borda-count.md), [DAPO](../methods/dapo.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [entropy collapse](../concepts/entropy-collapse.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [HumanEval+](humaneval.md), [LiveCodeBench](livecodebench.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [LLaVA-OneVision-7B](../models/llava-onevision-7b.md), [majority voting](../methods/majority-voting.md), [matched-budget comparison](../concepts/matched-budget-comparison.md), [MATH500](math500.md), [MathVista](mathvista.md), [Minerva](minerva.md), [MMMU](mmmu.md), [OlympiadBench](olympiadbench.md), [paired bootstrap confidence intervals](../methods/paired-bootstrap-confidence-intervals.md), [pass@k](../concepts/pass-k.md), [PPO](../methods/ppo.md), [Qwen2.5-14B](../models/qwen2-5-14b.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [Qwen2.5-VL-7B-Instruct](../models/qwen2-5-vl-7b-instruct.md), [reasoning boundary](../concepts/reasoning-boundary.md), [reasoning distillation](../methods/reasoning-distillation.md), [REINFORCE](../methods/reinforce.md), [RLOO](../methods/rloo.md), [RLVR](../methods/rlvr.md), [selection signal](../concepts/selection-signal.md), [self-consistency](../methods/self-consistency.md), [test-time scaling](../methods/test-time-scaling.md), [visual grounding](../concepts/visual-grounding.md)

## Appears in

- [It's the Decoding Format, Not the Perturbation: Auditing Consistency-Based Selection for Vision-Language Test-Time Scaling](../../archive/papers/2026/arxiv-2608-01207/summary.md) — Shows that a perturbation-based selection rule's apparent 31.8-point gain over majority voting in vision-language test-time scaling is a decoding-format effect, by adding a control that spends the same short-answer budget on the unperturbed image and finds it matches or beats the perturbation rule everywhere.
- [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](../../archive/papers/2025/local-b050d2841cbb4959/summary.md) — Measures RLVR-trained models against their base models with pass@k at large k and finds the base wins, concluding RLVR sharpens sampling toward paths the base already had rather than adding new ones.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
