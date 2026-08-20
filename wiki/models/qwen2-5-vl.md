# Qwen2.5-VL

<!-- auto:begin -->

The Qwen2.5 vision-language line referred to generically across 3 sources -- as the backbone for tool orchestration in video anomaly detection, as the subject of a multimodal unlearning study finding that a fact removed from the answer survives in the reasoning trace, and as one of four checkpoints supported by an open mechanistic-interpretability library for vision-language models. The entry records the family dependency: most of the archive's multimodal interpretability and multimodal reinforcement-learning results are measured on this line.

- **Kind**: model
- **Also called**: Qwen2.5-VL, Qwen2.5-VL-72B
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [activation patching](../methods/activation-patching.md), [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [advantage estimation](../concepts/advantage-estimation.md), [attention pattern](../concepts/attention-pattern.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [component ablation](../methods/component-ablation.md), [credit assignment](../concepts/credit-assignment.md), [degenerate generation](../concepts/degenerate-generation.md), [entropy collapse](../concepts/entropy-collapse.md), [Gemini-2.5-pro](gemini-2-5-pro.md), [GRPO](../methods/grpo.md), [KL regularization](../methods/kl-regularization.md), [latent reasoning](../concepts/latent-reasoning.md), [Llama-3-8B](llama-3-8b.md), [LLaVA-1.5](llava-1-5.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [machine unlearning](../concepts/machine-unlearning.md), [mechanistic interpretability](../concepts/mechanistic-interpretability.md), [monitorability](../concepts/monitorability.md), [outcome reward](../concepts/outcome-reward.md), [process reward](../concepts/process-reward.md), [process supervision](../concepts/process-supervision.md), [Qwen2.5-VL-3B](qwen2-5-vl-3b.md), [Qwen2.5-VL-7B](qwen2-5-vl-7b.md), [Qwen3-VL](qwen3-vl.md), [Qwen3-VL-8B](qwen3-vl-8b.md), [ReAct](../methods/react.md), [reproducibility](../concepts/reproducibility.md), [reward shaping](../methods/reward-shaping.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [tool learning](../concepts/tool-learning.md), [tool orchestration](../concepts/tool-orchestration.md), [Vicuna-7B](vicuna-7b.md)

## Appears in

- [VTO: Visual Tool Orchestration for Video Anomaly Detection](../../archive/papers/2026/arxiv-2608-08219/summary.md) — Trains a multimodal agent to orchestrate twelve video-analysis tools for anomaly detection with GRPO under a dual reward that combines exact-match rule checks with an LLM judge scoring logicality, relevance and completeness, and releases the benchmark it is evaluated on.
- [LEMUR: Latent Entropy-aware Multimodal Unlearning via Visual-anchored Reasoning Redirection](../../archive/papers/2026/arxiv-2608-11691/summary.md) — Finds that a fact successfully unlearned from a multimodal model's final answer can still be reproduced in its reasoning trace, far more in natively RL-trained models than in their base versions, and uses the token-level entropy signature RL leaves behind as a training-free control signal for redirecting the trace at decoding time.
- [Spectra: A Mechanistic Interpretability Library for Vision-Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-demo-78/summary.md) — An open library giving vision-language models the mechanistic-interpretability tooling that text-only models already have: activation patching, attention analysis and meta-functions behind one interface.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
