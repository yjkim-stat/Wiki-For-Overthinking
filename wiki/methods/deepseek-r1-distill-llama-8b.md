# DeepSeek-R1-Distill-Llama-8B

<!-- auto:begin -->

DeepSeek-R1-Distill-Llama-8B is a language model that two archived papers run experiments on, not a concept, method or dataset; the wiki has no kind for a model, so it is filed under the least wrong of the three available. In ReCo it is one of three evaluated models and the one where cache compression is hardest: reward-coordinated compression holds 60.2% six-benchmark accuracy against 62.8% for full-cache CoT at 37% fewer tokens, while the baselines it is compared with collapse on this model (R-KV 48.1%, SnapKV 37.5%), and at a 25% R-KV retention rate its MATH-500 generations grow from 4,409.8 to 7,891.7 tokens, an increase of 79.0%. Keep, Customize, or Exit uses it with Qwen3-8B only to calibrate an accuracy-versus-reasoning-token curve, Q(r) = D + A(1 - e^{-br}), under s1-style budget forcing on AIME 2024, AIME 2025, GPQA Diamond, GSM8K and HMMT 2025, three samples per question -- the model supplies the empirical shape that a pricing game is then built on, rather than being the object of study. Neither paper reports its architecture or training.

- **Kind**: method
- **Also called**: Llama-8B
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [budget forcing](budget-forcing.md), [confidence-based early stopping](confidence-based-early-stopping.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [distillation](../concepts/distillation.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [HMMT 2025](../datasets/hmmt-2025.md), [KV cache compression](kv-cache-compression.md), [MATH-500](../datasets/math-500.md), [overthinking](../concepts/overthinking.md), [process reward model](../concepts/process-reward-model.md), [Qwen3-8B](qwen3-8b.md), [R-KV](r-kv.md), [test-time compute scaling](../concepts/test-time-compute-scaling.md), [vLLM](vllm.md)

## Appears in

- [Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning](../../archive/papers/2026/arxiv-2608-04771/summary.md) — ReCo uses a 30M process-reward estimator to set, per reasoning step, both the KV-cache retention ratio and generation-side controls (a reflection-token logit penalty and confidence-based early stopping), cutting generated tokens by 37-65% and end-to-end latency by 2.08-2.35x versus full-cache CoT.
- [Keep, Customize, or Exit: Default Design and Token Pricing in LLM Reasoning Services](../../archive/papers/2026/arxiv-2608-13315/summary.md) — Models an LLM reasoning service as a Stackelberg game in which the provider sets a per-token price and a default reasoning-token budget while the user may keep the default, customize it, or exit, and shows the provider's optimal default sits above the budget the user would choose.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
