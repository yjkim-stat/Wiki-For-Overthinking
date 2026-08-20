# Llama-3.3-70B

<!-- auto:begin -->

A 70-billion-parameter Llama model that appears in this archive twice, in both cases as one member of a panel rather than as the object of study. It is one of six models, spanning GPT-2 to Llama-3.1-405B-Instruct, across which dense low-rank trained lenses are attached at every layer and at residual, attention and MLP hookpoints alike. It is separately one of ten judges in the large-scale LLM-as-a-judge reliability evaluation, whose findings -- kappa deflation universal across every judge and provider, and judge rankings shifting by up to fifteen positions between benchmarks -- are reported over the panel rather than per model. Neither source reports a result attributed specifically to it.

- **Kind**: model
- **Also called**: Llama 3.3 70B
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [activation patching](../methods/activation-patching.md), [activation steering](../methods/activation-steering.md), [circuit analysis](../methods/circuit-analysis.md), [construct validity](../concepts/construct-validity.md), [DeepSeek-V3.2](deepseek-v3-2.md), [detection versus control](../concepts/detection-versus-control.md), [factorial ablation](../methods/factorial-ablation.md), [Gemini-2.0-flash](gemini-2-0-flash.md), [Gemini-2.5-Flash](gemini-2-5-flash.md), [Gemini-3.1-Pro](gemini-3-1-pro.md), [GPT-2](gpt-2.md), [GPT-2 XL](gpt-2-xl.md), [GPT-4o](gpt-4o.md), [GPT-4o-mini](gpt-4o-mini.md), [gpt-oss-120b](gpt-oss-120b.md), [importance sampling](../methods/importance-sampling.md), [Kimi-K2.5](kimi-k2-5.md), [KL divergence](../concepts/kl-divergence.md), [knowledge distillation](../methods/knowledge-distillation.md), [linear probe](../methods/linear-probe.md), [Llama-3.1-8B](llama-3-1-8b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [logit lens](../methods/logit-lens.md), [LoRA](../methods/lora.md), [meta-evaluation](../concepts/meta-evaluation.md), [MT-Bench](../datasets/mt-bench.md), [position bias](../concepts/position-bias.md), [Qwen2.5-coder-7B](qwen2-5-coder-7b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-8B](qwen3-8b.md), [Qwen3-VL-235B](qwen3-vl-235b.md), [ReAct](../methods/react.md), [residual stream](../concepts/residual-stream.md), [SciQ](../datasets/sciq.md), [self-verification](../concepts/self-verification.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [the Pile](../datasets/the-pile.md), [tuned lens](../methods/tuned-lens.md), [WikiText-2](../datasets/wikitext-2.md)

## Appears in

- [Persistent Semantic Entities in Tool-Augmented LLM Systems](../../archive/papers/2026/arxiv-2608-07952/summary.md) — Formalises implicit agent state that survives session boundaries as Persistent Semantic Entities defined by name binding, event triggering and propagation, and measures across 24 models that whether injected contamination decays depends on what kind of contamination it is rather than on model scale or deployment.
- [Interpreting Language Model Hidden States at Scale](../../archive/papers/2026/arxiv-2608-10260/summary.md) — Makes trained lenses cheap enough to attach densely across a whole model — every layer, and residual, attention and MLP alike — and then uses that coverage to show that where a behaviour is most visible is not where intervening on it works best.
- [Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias](../../archive/papers/2026/local-504cc53656b06ab4/summary.md) — Evaluates 21 LLM judges across three benchmarks and three protocols over ~541,000 judgments, and shows the field's standard validation metric — exact-match agreement — overstates chance-corrected discrimination by 34-41 points universally, while high test-retest reliability can coexist with severe position bias.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
