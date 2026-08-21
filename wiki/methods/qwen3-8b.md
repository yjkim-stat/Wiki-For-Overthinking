# Qwen3-8B

<!-- auto:begin -->

Qwen3-8B is a language model that archived papers train and evaluate on, not a concept, method or dataset; the wiki has no kind for a model, so it is filed under the least wrong of the three available. It is the archive's most frequently used 8B backbone: TabRank fine-tunes it into a listwise table reranker distilled from DeepSeek-R1 rationales, raising Accuracy@10 over the base Qwen3-8B from 0.6200 to 0.8091 on HybridQA and 0.3816 to 0.5835 on TabFact, while ReCo runs it as one of three compression testbeds, holding 69.6% six-benchmark accuracy against 72.3% for full-cache CoT with generation cut from 6,788 to 3,652 tokens and a 2.18x latency speedup. The token-pricing paper calibrates its accuracy-versus-budget curve on it under s1-style budget forcing and finds the saturation rate varying by roughly an order of magnitude across tasks (b = 2.66e-3 on GSM8K against 9.25e-5 on AIME 2024); Sonata and Risky Business use it as one backbone among several. No archived paper describes the model's own architecture or training.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 5

**Related**: [adaptive test-time compute](../concepts/adaptive-test-time-compute.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Budget Forcing](budget-forcing.md), [Chain-of-Thought Distillation](chain-of-thought-distillation.md), [Chain-of-thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [Chain-of-thought monitorability](../concepts/chain-of-thought-monitorability.md), [Compute-optimal inference](../concepts/compute-optimal-inference.md), [Confidence-based early stopping](confidence-based-early-stopping.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [Dynasor](dynasor.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-oss-120b](gpt-oss-120b.md), [GSM8K](../datasets/gsm8k.md), [HMMT 2025](../datasets/hmmt-2025.md), [KV-cache compression](kv-cache-compression.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [Out-of-Distribution Generalization](../concepts/out-of-distribution-generalization.md), [Overthinking](../concepts/overthinking.md), [process reward model](process-reward-model.md), [QwQ-32B](qwq-32b.md), [R-KV](r-kv.md), [Self-Consistency](self-consistency.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [vLLM](vllm.md)

## Appears in

- [TabRank: Chain-of-Thought Distillation for Table Re-Rankers](../../archive/papers/2026/arxiv-2607-25182/summary.md) — TabRank distills DeepSeek-R1 reranking rationales into a Qwen3-8B listwise table reranker by placing the teacher's reasoning trace in the student's input prompt and computing loss only over the final ranking, rather than training the student to reproduce the trace.
- [Risky Business: Measuring The Faithfulness-Safety Tension](../../archive/papers/2026/arxiv-2608-03745/summary.md) — Introduces HazMart (77 hand-written agentic shopkeeper scenarios) and Targeted Reasoning Replacement, a search-and-replace edit of a model's own reasoning trace, and shows that models which follow their traces more faithfully also follow tampered unsafe traces more often, with two anti-correlated residual-stream directions in QwQ-32B that can be steered independently.
- [Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning](../../archive/papers/2026/arxiv-2608-04771/summary.md) — ReCo uses a 30M process-reward estimator to set, per reasoning step, both the KV-cache retention ratio and generation-side controls (a reflection-token logit penalty and confidence-based early stopping), cutting generated tokens by 37-65% and end-to-end latency by 2.08-2.35x versus full-cache CoT.
- [Keep, Customize, or Exit: Default Design and Token Pricing in LLM Reasoning Services](../../archive/papers/2026/arxiv-2608-13315/summary.md) — Models an LLM reasoning service as a Stackelberg game in which the provider sets a per-token price and a default reasoning-token budget while the user may keep the default, customize it, or exit, and shows the provider's optimal default sits above the budget the user would choose.
- [Adaptive Thinking: Large Language Models Know When to Think in Latent Space](../../archive/papers/2026/title-cc91145094e2b147/summary.md) — Sonata predicts a query's self-consistency from the last-layer hidden state at prefill and uses that prediction to set the thinking budget before the model starts reasoning.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
