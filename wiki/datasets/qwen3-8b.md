# Qwen3-8B

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 5

**Related**: [adaptive test-time compute](../concepts/adaptive-test-time-compute.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [budget forcing](../methods/budget-forcing.md), [chain-of-thought distillation](../methods/chain-of-thought-distillation.md), [Chain-of-thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [Chain-of-thought monitorability](../concepts/chain-of-thought-monitorability.md), [Compute-optimal inference](../concepts/compute-optimal-inference.md), [confidence-based early stopping](../methods/confidence-based-early-stopping.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [GPQA](gpqa.md), [GPQA-Diamond](gpqa-diamond.md), [gpt-oss-120b](../methods/gpt-oss-120b.md), [GSM8K](gsm8k.md), [HMMT 2025](hmmt-2025.md), [KV cache compression](../concepts/kv-cache-compression.md), [MATH-500](math-500.md), [MMLU](mmlu.md), [Out-of-Distribution Generalization](../concepts/out-of-distribution-generalization.md), [overthinking](../concepts/overthinking.md), [process reward model](../concepts/process-reward-model.md), [QwQ-32B](../methods/qwq-32b.md), [R-KV](../methods/r-kv.md), [self-consistency](../methods/self-consistency.md), [test-time compute scaling](../concepts/test-time-compute-scaling.md), [vLLM](../methods/vllm.md)

## Appears in

- [TabRank: Chain-of-Thought Distillation for Table Re-Rankers](../../archive/papers/2026/arxiv-2607-25182/summary.md) — TabRank distills DeepSeek-R1 reranking rationales into a Qwen3-8B listwise table reranker by placing the teacher's reasoning trace in the student's input prompt and computing loss only over the final ranking, rather than training the student to reproduce the trace.
- [Risky Business: Measuring The Faithfulness-Safety Tension](../../archive/papers/2026/arxiv-2608-03745/summary.md) — Introduces HazMart (77 hand-written agentic shopkeeper scenarios) and Targeted Reasoning Replacement, a search-and-replace edit of a model's own reasoning trace, and shows that models which follow their traces more faithfully also follow tampered unsafe traces more often, with two anti-correlated residual-stream directions in QwQ-32B that can be steered independently.
- [Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning](../../archive/papers/2026/arxiv-2608-04771/summary.md) — ReCo uses a 30M process-reward estimator to set, per reasoning step, both the KV-cache retention ratio and generation-side controls (a reflection-token logit penalty and confidence-based early stopping), cutting generated tokens by 37-65% and end-to-end latency by 2.08-2.35x versus full-cache CoT.
- [Keep, Customize, or Exit: Default Design and Token Pricing in LLM Reasoning Services](../../archive/papers/2026/arxiv-2608-13315/summary.md) — Models an LLM reasoning service as a Stackelberg game in which the provider sets a per-token price and a default reasoning-token budget while the user may keep the default, customize it, or exit, and shows the provider's optimal default sits above the budget the user would choose.
- [Adaptive Thinking: Large Language Models Know When to Think in Latent Space](../../archive/papers/2026/title-cc91145094e2b147/summary.md) — Sonata predicts a query's self-consistency from the last-layer hidden state at prefill and uses that prediction to set the thinking budget before the model starts reasoning.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
