# MM-Vet

<!-- auto:begin -->

MM-Vet is a multimodal reasoning/visual-question-answering benchmark. GPRO evaluates on it as one of five multimodal reasoning benchmarks (with MathVision, MathVerse, MathVista, DynaMath) on which its perception/reasoning-routing method redefines the efficiency-accuracy Pareto frontier versus base models and slow-thinking baselines. Heima evaluates zero-shot on it as one of six benchmarks (with MMStar, MMBench, MathVista, AI2D, HallusionBench) used to check that replacing textual CoT with latent 'thinking tokens' does not cost much accuracy -- averaged across that six-benchmark suite, Heima trails its CoT baseline by 3.1 points (58.0% vs. 61.1%) though it exceeds its own un-tuned Llama-3.2-11B-Vision-Instruct base (52.1%), without an MM-Vet-specific number broken out.

- **Kind**: dataset
- **Also called**: MMVet
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AI2D](ai2d.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [DynaMath](dynamath.md), [Latent reasoning](../concepts/latent-reasoning.md), [LLaMA-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [LLaVA-CoT](../models/llava-cot.md), [MathVerse](mathverse.md), [MathVision](mathvision.md), [MathVista](mathvista.md), [MMStar](mmstar.md), [Qwen2.5-VL-3B](../models/qwen2-5-vl-3b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [ViRL39k](virl39k.md)

## Appears in

- [Addressing Overthinking in Large Vision-Language Models via Gated Perception-Reasoning Optimization](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-215/summary.md) — GPRO diagnoses that visual perception failures (not reasoning errors) cause over twice as many incorrect predictions across model scales in vision-language models, then routes each generated token through one of three paths -- a fast FFN, a slow cross-attention perception path for re-examining the image, or a slow self-reflection reasoning path -- via a lightweight meta-reasoning controller trained with PPO on a multi-objective reward (task accuracy, path-cost penalty, and an uncertainty-calibration term derived from ~790K GPT-4-labeled perception-vs-reasoning failure attributions); GPRO-7B matches/beats far larger closed models and long-CoT distillation baselines while cutting response length up to 51.5%, activating slow paths sparsely (73% Fast/17% Perception/10% Reasoning) and correctly, targeting perception re-examination at high-frequency visual tokens and reasoning refinement at logical connectives.
- [Efficient Reasoning with Hidden Thinking](../../archive/papers/2026/title-725397e20ebf1509/summary.md) — Heima replaces each stage of a multimodal model's textual chain of thought with a single learned 'thinking token' generated in latent space, and trains a separate decoder that can expand those tokens back into readable reasoning.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
