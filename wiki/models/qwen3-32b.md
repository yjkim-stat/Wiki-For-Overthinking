# Qwen3-32B

<!-- auto:begin -->

The 32B member of the Qwen3 family. It appears in these sources as a scale check rather than a primary subject — used to verify that numerical-precision reproducibility findings established at 7-8B also hold at larger scale, and as a large model in entropy-mechanism experiments. Results for it are generally deferred to appendices in the sources that use it.

- **Kind**: model
- **Also called**: Qwen3-32B
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [activation steering](../methods/activation-steering.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 24](../datasets/aime-24.md), [AIME 25](../datasets/aime-25.md), [AIME24](../datasets/aime24.md), [BBH](../datasets/bbh.md), [clip-higher](../methods/clip-higher.md), [credit assignment](../concepts/credit-assignment.md), [DAPO](../methods/dapo.md), [DAPO-Math-17k](../datasets/dapo-math-17k.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [entropy bonus](../concepts/entropy-bonus.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [greedy decoding](../methods/greedy-decoding.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [MMLU-Pro](../datasets/mmlu-pro.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](../concepts/overthinking.md), [pass-k](../methods/pass-k.md), [policy gradient masking](../methods/policy-gradient-masking.md), [PPO](../methods/ppo.md), [Qwen2.5-7B](qwen2-5-7b.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-8B](qwen3-8b.md), [reproducibility](../concepts/reproducibility.md), [RLVR](../methods/rlvr.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [token-level entropy](../concepts/token-level-entropy.md), [VeRL](../methods/verl.md), [vLLM](../methods/vllm.md)

## Appears in

- [Beyond the 80/20 Rule: High-Entropy Minority Tokens Drive Effective Reinforcement Learning for LLM Reasoning](../../archive/papers/2025/local-7d5e3edea2d46b92/summary.md) — Shows that the roughly 20% of CoT tokens with the highest entropy act as decision forks, and that restricting RLVR policy-gradient updates to only those tokens matches or beats full-gradient training, with the advantage growing with model size.
- [Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference](../../archive/papers/2025/local-de572e138fc98639/summary.md) — Shows that greedy decoding is not deterministic across hardware: changing GPU type, GPU count or evaluation batch size shifts a reasoning model's AIME'24 accuracy by up to 9 percentage points and its response length by 9,000 tokens under BF16, because floating-point addition is non-associative.
- [The Tell-Tale Norm: L2 Magnitude as a Signal for Reasoning Dynamics in Large Language Models](../../archive/papers/2026/local-f92e5f936a3c7422/summary.md) — Argues that the L2 norm of a hidden state is a training-free proxy for how hard a model is reasoning at that layer and token, proves it bounds the activation of SAE-identified reasoning features, and uses norm peaks to decide where to recurse a layer, where to steer, and which sampled response to keep.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
