# in-context learning

<!-- auto:begin -->

Supplying examples in the prompt so the model infers the task without weight updates. Both sources here report that the standard static form has stopped paying on reasoning-specialized models: few-shot chain-of-thought with dataset examples now underperforms simply asking the question -- 74.2% against 86.1% on GSM8K for one model -- and the other treats input-level exemplars as the baseline its in-trace retrieval improves on. The distinction both draw is between retrieving once before generation, where the context is then static, and supplying examples during reasoning, which is what they find still helps.

- **Kind**: concept
- **Also called**: few-shot prompting, in-context learning
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [AIME 2025](../datasets/aime-2025.md), [annotation agreement](annotation-agreement.md), [answer extraction](answer-extraction.md), [budget forcing](../methods/budget-forcing.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Claude-Sonnet-4](../models/claude-sonnet-4.md), [Coconut](../methods/coconut.md), [compositional generalization](compositional-generalization.md), [construct validity](construct-validity.md), [decontamination](../methods/decontamination.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [dense retrieval](../methods/dense-retrieval.md), [error compounding](error-compounding.md), [few-shot prompting](../methods/few-shot-prompting.md), [GPT-4](../models/gpt-4.md), [GSM8K](../datasets/gsm8k.md), [human evaluation](../methods/human-evaluation.md), [implicit chain of thought](implicit-chain-of-thought.md), [latent reasoning](latent-reasoning.md), [Llama-3.1-70B](../models/llama-3-1-70b.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [MATH500](../datasets/math500.md), [McNemar test](../methods/mcnemar-test.md), [monitorability](monitorability.md), [pass@k](pass-k.md), [predictive entropy](predictive-entropy.md), [prompt sensitivity](prompt-sensitivity.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3.5-2B](../models/qwen3-5-2b.md), [Qwen3-8B](../models/qwen3-8b.md), [reasoning drift](reasoning-drift.md), [recurrent depth](recurrent-depth.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [RoBERTa](../models/roberta.md), [SciQ](../datasets/sciq.md), [self-reflection](../methods/self-reflection.md), [test-time scaling](test-time-scaling.md), [Tree of Thoughts](../methods/tree-of-thoughts.md), [Wilson confidence interval](../methods/wilson-confidence-interval.md), [zero-shot prompting](../methods/zero-shot-prompting.md)

## Appears in

- [Soft Guidance Starts to Outperform CoT Prompting as LLMs Improve](../../archive/papers/2026/arxiv-2608-03550/summary.md) — Finds that few-shot chain-of-thought prompting with dataset examples now performs worse than simply asking a reasoning-specialized model the question — 74.2% against 86.1% on GSM8K for one model — so the field's standard baseline systematically understates modern models and overstates anything benchmarked against it.
- [PROSLEX: A Novel Dataset for Expert-Annotated Legal Statute Prediction for Indian Judiciary](../../archive/papers/2026/arxiv-2608-08830/summary.md) — Builds an expert-annotated Indian Supreme Court dataset in which each applicable statute is paired with the specific text span a legal expert says establishes it, and uses it to show that predicting the right statute and giving the right reason are separable abilities.
- [BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](../../archive/papers/2026/arxiv-2608-09888/summary.md) — Combines in-context learning through evolving recurrent memory with iterative reasoning in a continuous latent workspace that is never decoded into language, reaching 29.5% pass@2 on public ARC-AGI-1 at $0.0007 per task from 150M parameters, and then probes with controlled tasks what the resulting demonstration-bound operators can and cannot do.
- [ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling](../../archive/papers/2026/arxiv-2608-10928/summary.md) — Injects a retrieved solved problem, with its full worked solution, into the middle of a reasoning model's own thinking trace at each step boundary, using the model's current intermediate answer as the retrieval query.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
