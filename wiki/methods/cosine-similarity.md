# cosine similarity

<!-- auto:begin -->

The angle between two vectors, used as a similarity that ignores magnitude, and in both sources the readout that turns a geometric claim into a number. One proves when it suffices and when it does not: a coordinate-aware comparison of activation summaries separates classes whose means differ in direction, where a norm-only rule is at chance, while the converse holds when classes share a mean and differ only in scale — so choosing between angle and magnitude is a fact about the task, not a convention. The other uses it as the supervision signal itself, computing a per-token loss between decoded latent features and the frozen encoder's features of the true future observation, and separately as the readout in an intervention probe. Between them the pair marks the two uses that get conflated: a similarity used to compare, and a similarity used to train.

- **Kind**: method
- **Also called**: cosine distance
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [adversarial robustness](../concepts/adversarial-robustness.md), [calibration](calibration.md), [causal intervention](causal-intervention.md), [CLIP](../models/clip.md), [flow matching](flow-matching.md), [foresight](../concepts/foresight.md), [GPT-4o](../models/gpt-4o.md), [GPT-5](../models/gpt-5.md), [GSM8K](../datasets/gsm8k.md), [hidden-state geometry](../concepts/hidden-state-geometry.md), [HumanEval+](../datasets/humaneval.md), [latent reasoning](../concepts/latent-reasoning.md), [linear probe](linear-probe.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [LLM-as-a-judge](llm-as-a-judge.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [RoBERTa](../models/roberta.md), [routing](../concepts/routing.md), [sample complexity](../concepts/sample-complexity.md), [superposition](../concepts/superposition.md), [t-SNE](t-sne.md), [uncertainty quantification](../concepts/uncertainty-quantification.md)

## Appears in

- [Training-Free versus Training-Based Intent Classification in LLMs: Accuracy, Robustness, and Failure Modes](../../archive/papers/2026/arxiv-2608-02415/summary.md) — Compares two training-free intent classifiers built from summary statistics of prefill-time activations against trained heads on the same features, and finds the trade-off is not accuracy but where each fails — trained heads win fine-grained distinctions, statistical ones give better uncertainty on mixed prompts and survive adversarial rephrasing that collapses the trained heads to zero.
- [LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipulation](../../archive/papers/2026/arxiv-2608-03701/summary.md) — Builds a 0.5B world-action model for robot manipulation whose future-state prediction and action generation share one compact latent in a single token stream, specifies the task as a direction in visual feature space instead of language, and shows a frozen self-supervised vision encoder beating a four-times-larger pretrained vision-language backbone at the same training budget.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
