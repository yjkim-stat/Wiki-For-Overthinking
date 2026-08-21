# Minerva

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [adaptive reasoning](../concepts/adaptive-reasoning.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [DEER](../methods/deer.md), [DPO_Shortest](../methods/dpo-shortest.md), [DRP](../methods/drp.md), [Efficient Reasoning](../concepts/efficient-reasoning.md), [GPQA](gpqa.md), [GPQA-Diamond](gpqa-diamond.md), [GPT-OSS-20B](../methods/gpt-oss-20b.md), [GSM8K](gsm8k.md), [Hidden-State Probing](../concepts/hidden-state-probing.md), [MATH-500](math-500.md), [MMLU-PRO](mmlu-pro.md), [O1-Pruner](../methods/o1-pruner.md), [OlympiadBench](olympiadbench.md), [overthinking](../concepts/overthinking.md), [Phi-4-reasoning](../methods/phi-4-reasoning.md), [SelfBudgeter](../methods/selfbudgeter.md), [SFT_Shortest](../methods/sft-shortest.md), [test-time scaling](../concepts/test-time-scaling.md), [Thinkless](../methods/thinkless.md), [ThinkPrune](../methods/thinkprune.md), [Token Budget](../concepts/token-budget.md), [TokenSkip](../methods/tokenskip.md), [vLLM](../methods/vllm.md)

## Appears in

- [Segment-Level Attribution for Selective Learning of Long Reasoning Traces](../../archive/papers/2026/arxiv-2602-00425/summary.md) — Uses integrated-gradient token attribution, aggregated into per-segment strength and direction-consistency scores, to pick which segments of a long chain-of-thought an SFT run should compute loss on, masking the rest.
- [DiffAdapt: Difficulty-Adaptive Reasoning for Token-Efficient LLM Inference](../../archive/papers/2026/title-18b94d8204ec3367/summary.md) — DiffAdapt trains a small probe on a reasoning model's hidden state to classify each question as Easy/Normal/Hard and picks a matching prompt, temperature and token limit, cutting token use without retraining the model.
- [FROST: Filtering Reasoning Outliers with Attention for Efficient Reasoning](../../archive/papers/2026/title-e2cdfd631cb4eda0/summary.md) — FROST uses attention weights to identify and prune sentence-level 'reasoning outliers' from a reasoning model's chain of thought, reporting an average 69.68% token reduction and 26.70% accuracy gain over the base model on four maths benchmarks.
- [QFFT, Question-Free Fine-Tuning for Adaptive Reasoning](../../archive/papers/2025/title-ff37e37c3f1ab9b2/summary.md) — QFFT fine-tunes a short-CoT instruct model on Long CoT responses with the question deleted from every training example, so the model keeps its default concise reasoning and switches to reflective Long CoT only when it hits uncertainty or an error, cutting average tokens by roughly 50% at accuracy comparable to ordinary SFT.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
