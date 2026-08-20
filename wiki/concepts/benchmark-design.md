# benchmark design

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [advantage estimation](advantage-estimation.md), [benchmark contamination](benchmark-contamination.md), [calibration](../methods/calibration.md), [chain-of-thought distillation](../methods/chain-of-thought-distillation.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [decontamination](../methods/decontamination.md), [DeepSeek-R1](../models/deepseek-r1.md), [dense retrieval](../methods/dense-retrieval.md), [Gemini-3.1-Pro](../models/gemini-3-1-pro.md), [Gemini-3.5-Flash](../models/gemini-3-5-flash.md), [GPT-5.5](../models/gpt-5-5.md), [gpt-5.6-luna](../models/gpt-5-6-luna.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [knowledge distillation](../methods/knowledge-distillation.md), [latent reasoning](latent-reasoning.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [multi-hop reasoning](multi-hop-reasoning.md), [multiple-choice evaluation](../methods/multiple-choice-evaluation.md), [position bias](position-bias.md), [privileged information](privileged-information.md), [Qwen3-235B-A22B](../models/qwen3-235b-a22b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3.5-9B](../models/qwen3-5-9b.md), [Qwen3.6-27B](../models/qwen3-6-27b.md), [reranking](../methods/reranking.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [reward shaping](reward-shaping.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [verification](verification.md)

## Appears in

- [Training Verifiers to Solve Math Word Problems](../../archive/papers/2021/arxiv-2110-14168/summary.md) — Introduces GSM8K, 8.5K grade-school math word problems, and shows that training a verifier to rank many sampled solutions beats finetuning the generator directly.
- [SkillReason: Reasoning-Enhanced Agent Skill Retrieval for Implicit User Requests](../../archive/papers/2026/arxiv-2608-08640/summary.md) — Uses chain-of-thought about required capabilities as training-time supervision for a skill retriever -- distilled from a teacher in stage one and refined by retrieval-rewarded GRPO in stage two -- so that at inference the model encodes the bare query with no generation at all.
- [SafeSceneReason: A Multimodal Reasoning Benchmark Connecting Industrial Hazards with Accident Knowledge](../../archive/papers/2026/arxiv-2608-09230/summary.md) — Builds an industrial-safety reasoning benchmark from two pipelines -- program execution over safety scene graphs, and evidence graphs extracted from real accident-investigation reports -- and shows that general multimodal capability does not transfer to it while a 9B model fine-tuned on its chain-of-thought split matches frontier systems.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
