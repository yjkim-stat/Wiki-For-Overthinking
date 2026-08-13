# LoRA

<!-- auto:begin -->

Fine-tuning by learning low-rank updates to frozen weights instead of all parameters. Neither source studies it; both use it as the cheap adaptation that makes their comparison affordable, and its presence marks how their results should be scoped — a finding established under low-rank adaptation is a finding about what that adaptation reaches, not about full fine-tuning. One uses it to train students on compressed reasoning traces so that three importance criteria can be compared at matched compression ratios on the same traces. The other uses it in the pipeline that scores hidden-state trajectory geometry for progress and stability.

- **Kind**: method
- **Also called**: Low-Rank Adaptation
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [AIME24](../datasets/aime24.md), [AMC23](../datasets/amc23.md), [chain-of-thought compression](chain-of-thought-compression.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [GEMBA-MQM](gemba-mqm.md), [Gemini-2.0-flash](../models/gemini-2-0-flash.md), [Gemini-2.5-Flash](../models/gemini-2-5-flash.md), [generative rewriting](generative-rewriting.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-4](../models/gpt-4.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [GPT-4o](../models/gpt-4o.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [knowledge distillation](knowledge-distillation.md), [linear probe](linear-probe.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [Llama-3-70B-Instruct](../models/llama-3-70b-instruct.md), [LLM-as-a-judge](llm-as-a-judge.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MMLU-Pro](../datasets/mmlu-pro.md), [overthinking](../concepts/overthinking.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen2.5](../models/qwen2-5.md), [Qwen2.5-0.5B](../models/qwen2-5-0-5b.md), [Qwen2.5-1.5B](../models/qwen2-5-1-5b.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [Qwen3-8B](../models/qwen3-8b.md), [reasoning distillation](reasoning-distillation.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [reasoning skeleton](../concepts/reasoning-skeleton.md), [restructuring level](../concepts/restructuring-level.md), [supervised fine-tuning](supervised-fine-tuning.md), [supervised finetuning](supervised-finetuning.md), [WMT22](../datasets/wmt22.md)

## Appears in

- [TQLite: Multi-LLM Jury Guided Distillation for Real-time MQM Translation Quality Evaluation](../../archive/papers/2026/arxiv-2608-02975/summary.md) — Benchmarks 20-plus models as MQM translation-quality judges, finds reasoning models best and a jury of different ones better than any member, then distils that jury's agreement-filtered annotations into a 12B student that beats every open reasoning-model judge tested.
- [When Compression Helps and When It Hurts: Condition-Aware Analysis of Chain-of-Thought Distillation](../../archive/papers/2026/local-4acfffb647c2e41f/summary.md) — Runs the head-to-head this literature had been missing, comparing three importance criteria on the same traces at matched compression ratios, and finds step-level criteria agree on what to keep while disagreeing on what to cut — because redundancy is diffuse rather than located in any identifiable class of step.
- [Beyond Scalars: Evaluating and Understanding LLM Reasoning via Geometric Progress and Stability](../../archive/papers/2026/local-85a70e78b4a93190/summary.md) — TRACED scores a reasoning chain by the geometry of its hidden-state trajectory -- net displacement as progress and curvature as stability -- and uses the two as features for a Gaussian classifier that separates correct from incorrect chains without reading the text.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
