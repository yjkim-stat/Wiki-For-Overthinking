# Qwen2.5-VL

<!-- auto:begin -->

A Qwen vision-language family used in this archive in three distinct roles within a single paper, which is itself the point worth recording. In the video-anomaly tool-orchestration work, Qwen2.5-VL writes the initial ReAct ground-truth trajectories and augments the training queries, Qwen2.5-VL-72B serves as the LLM judge supplying the training reward, and Qwen2.5-VL-72B is also the strong baseline the trained 8B agent is reported to beat (67.40 percent against 95.14 percent on interrelated tool responses) -- so one family sits on both sides of the comparison, which the archive's reading of that paper flags as making the result hard to read as independent. It is separately one of four checkpoints supported by the Spectra interpretability library, alongside Qwen3-VL, LLaVA 1.5 and SmolVLM. Neither source describes the model's own architecture or training.

- **Kind**: model
- **Also called**: Qwen2.5-VL, Qwen2.5-VL-72B
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [activation patching](../methods/activation-patching.md), [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [advantage estimation](../concepts/advantage-estimation.md), [attention pattern](../concepts/attention-pattern.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [component ablation](../methods/component-ablation.md), [credit assignment](../concepts/credit-assignment.md), [degenerate generation](../concepts/degenerate-generation.md), [entropy collapse](../concepts/entropy-collapse.md), [Gemini-2.5-pro](gemini-2-5-pro.md), [GRPO](../methods/grpo.md), [KL regularization](../methods/kl-regularization.md), [latent reasoning](../concepts/latent-reasoning.md), [Llama-3-8B](llama-3-8b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [machine unlearning](../concepts/machine-unlearning.md), [mechanistic interpretability](../concepts/mechanistic-interpretability.md), [monitorability](../concepts/monitorability.md), [outcome reward](../concepts/outcome-reward.md), [process reward](../concepts/process-reward.md), [process supervision](../concepts/process-supervision.md), [Qwen3-VL](qwen3-vl.md), [Qwen3-VL-8B](qwen3-vl-8b.md), [ReAct](../methods/react.md), [reproducibility](../concepts/reproducibility.md), [reward shaping](../concepts/reward-shaping.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [Vicuna-7B](vicuna-7b.md)

## Appears in

- [VTO: Visual Tool Orchestration for Video Anomaly Detection](../../archive/papers/2026/arxiv-2608-08219/summary.md) — Trains a multimodal agent to orchestrate twelve video-analysis tools for anomaly detection with GRPO under a dual reward that combines exact-match rule checks with an LLM judge scoring logicality, relevance and completeness, and releases the benchmark it is evaluated on.
- [LEMUR: Latent Entropy-aware Multimodal Unlearning via Visual-anchored Reasoning Redirection](../../archive/papers/2026/arxiv-2608-11691/summary.md) — Finds that a fact successfully unlearned from a multimodal model's final answer can still be reproduced in its reasoning trace, far more in natively RL-trained models than in their base versions, and uses the token-level entropy signature RL leaves behind as a training-free control signal for redirecting the trace at decoding time.
- [Spectra: A Mechanistic Interpretability Library for Vision-Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-demo-78/summary.md) — An open library giving vision-language models the mechanistic-interpretability tooling that text-only models already have: activation patching, attention analysis and meta-functions behind one interface.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
