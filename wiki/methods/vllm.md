# vLLM

<!-- auto:begin -->

None of the five sources describe vLLM directly in the material given; it appears as a named reference alongside their own contributions to multi-model reasoning evaluation, reasoning-service pricing, parallel-reasoning control, difficulty-adaptive inference, and long-generation decoder architecture. What role vLLM specifically plays in each is not stated in the supplied notes.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 5

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [Budget Forcing](budget-forcing.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DEER](deer.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-OSS-20B](gpt-oss-20b.md), [GSM8K](../datasets/gsm8k.md), [Hidden-State Probing](../concepts/hidden-state-probing.md), [HMMT 2025](../datasets/hmmt-2025.md), [LLM-as-a-Judge](llm-as-a-judge.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [MMLU-Pro](../datasets/mmlu-pro.md), [OlympiadBench](../datasets/olympiadbench.md), [process reward model](process-reward-model.md), [Qwen3-8B](qwen3-8b.md), [Self-Consistency](self-consistency.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [ThinkPrune](thinkprune.md)

## Appears in

- [Reasoning Jury: Multi-Model Consensus for Evaluating Reasoning Traces](../../archive/papers/2026/arxiv-2608-12585/summary.md) — Replaces the single LLM judge of a long reasoning trace with a panel of jurors that first judge independently and then reach consensus through a blind moderator's deliberation or a consolidation pass, letting cheap open-weight models beat frontier single judges at step-level defect localization for a fraction of the dollar cost.
- [Keep, Customize, or Exit: Default Design and Token Pricing in LLM Reasoning Services](../../archive/papers/2026/arxiv-2608-13315/summary.md) — Models an LLM reasoning service as a Stackelberg game in which the provider sets a per-token price and a default reasoning-token budget while the user may keep the default, customize it, or exit, and shows the provider's optimal default sits above the budget the user would choose.
- [ParaTempo: Efficient Parallel Reasoning via Temporal Confidence](../../archive/papers/2026/arxiv-2608-16425/summary.md) — A training-free controller for parallel reasoning that probes each branch every 500 tokens for a tentative answer distribution, averages recent probes into a 'temporal confidence' score, and uses that one signal to prune, retire, fork and globally stop branches.
- [DiffAdapt: Difficulty-Adaptive Reasoning for Token-Efficient LLM Inference](../../archive/papers/2026/title-18b94d8204ec3367/summary.md) — DiffAdapt trains a small probe on a reasoning model's hidden state to classify each question as Easy/Normal/Hard and picks a matching prompt, temperature and token limit, cutting token use without retraining the model.
- [Decoder-Hybrid-Decoder Architecture for Efficient Reasoning with Long Generation](../../archive/papers/2025/title-70a0c3f7ce6097f6/summary.md) — Introduces the Gated Memory Unit, a mechanism for sharing memory readout states across layers, and uses it to build SambaY, a decoder-hybrid-decoder architecture whose 3.8B instance (Phi4-mini-Flash-Reasoning) matches or beats Phi4-mini-Reasoning on math and science benchmarks while decoding up to 10x faster on 32K-token generations.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
