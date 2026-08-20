# benchmark design

<!-- auto:begin -->

How an evaluation set is constructed, and what that construction lets a score mean. Only three sources here address it as a subject, and they converge on making ground truth mechanical rather than authored. The earliest builds a corpus deliberately to diagnose multi-step failure on a distribution that model size alone did not solve, and pairs it with a verifier that ranks sampled solutions. The industrial-safety benchmark derives its scene-centric answers by program execution over an executable scene graph of objects, relations and rules, so the answer is deterministic and replayable rather than written by a model, and it decontaminates by sample, source-document, normalised-question and image-path identity while grouping splits by source document. The skill-retrieval benchmark takes the opposite risk knowingly and controls for it: its queries are filtered and reviewed by models rather than people, and it responds with an independent two-judge quality audit of 300 stratified samples reporting inter-judge agreement and a leakage rate, plus a sensitivity analysis crediting functionally valid but unannotated alternative answers, which moves every retriever by a comparable margin and leaves the ordering intact. Read together the three make one point that none states outright: the useful question about a benchmark is not how large it is but what its ground truth is a function of, and whether the authors measured the distortion introduced by whatever they could not make mechanical.

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
