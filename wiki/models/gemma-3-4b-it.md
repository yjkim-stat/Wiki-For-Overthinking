# Gemma-3-4B-it

<!-- auto:begin -->

A 4-billion-parameter instruction-tuned Gemma model appearing twice in this archive. In the persona-anatomy work it is the single model whose sparse-autoencoder features are decomposed across three speaker settings, and therefore the model behind that paper's finding that roleplay personas retain an Assistant-associated feature core while story characters do not -- a result explicitly bounded to one model and one autoencoder, with the split factor treated as a heuristic because no feature-splitting measurement exists for that exact dictionary. It appears again among the twenty-plus models benchmarked as translation-quality judges under a single prompt. Neither source describes the model itself.

- **Kind**: model
- **Also called**: Gemma-3-4B-IT
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [ablation](../methods/ablation.md), [activation steering](../methods/activation-steering.md), [annotation agreement](../concepts/annotation-agreement.md), [Aya-expanse-8B](aya-expanse-8b.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Cohen's kappa](../methods/cohen-s-kappa.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [detection versus control](../concepts/detection-versus-control.md), [GEMBA-MQM](../methods/gemba-mqm.md), [Gemini-2.0-flash](gemini-2-0-flash.md), [Gemini-2.5-pro](gemini-2-5-pro.md), [GPT-4](gpt-4.md), [GPT-4.1-mini](gpt-4-1-mini.md), [GPT-4o](gpt-4o.md), [GPT-4o-mini](gpt-4o-mini.md), [human evaluation](../methods/human-evaluation.md), [jury aggregation](../methods/jury-aggregation.md), [knowledge distillation](../methods/knowledge-distillation.md), [Llama-3-70B-Instruct](llama-3-70b-instruct.md), [Llama-3-8B-Instruct](llama-3-8b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [monosemanticity](../concepts/monosemanticity.md), [o4-mini](o4-mini.md), [persona conditioning](../methods/persona-conditioning.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-8B](qwen3-8b.md), [selectivity control](../methods/selectivity-control.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [sparse dictionary learning](../methods/sparse-dictionary-learning.md), [steering vector](../methods/steering-vector.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [WMT22](../datasets/wmt22.md)

## Appears in

- [TQLite: Multi-LLM Jury Guided Distillation for Real-time MQM Translation Quality Evaluation](../../archive/papers/2026/arxiv-2608-02975/summary.md) — Benchmarks 20-plus models as MQM translation-quality judges, finds reasoning models best and a jury of different ones better than any member, then distils that jury's agreement-filtered annotations into a 12B student that beats every open reasoning-model judge tested.
- ["Many Are My Names": The Anatomy of the Assistant and Its Personas via Sparse Autoencoders](../../archive/papers/2026/arxiv-2608-07852/summary.md) — Decomposes three speaker settings -- the default Assistant, an assigned roleplay persona, and a narrated story character -- into sparse-autoencoder features at turn boundaries and pronoun tokens, and finds that roleplay personas retain an Assistant-associated feature core while differentiating from it across depth, where story characters never acquire that core at all.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
