# CLIP

<!-- auto:begin -->

A vision-language encoder trained to align image and text embeddings, used by both sources as fixed infrastructure rather than as a subject. One uses it as the safety encoder against whose prohibited-concept embeddings intermediate clean-image estimates are scored, and names the consequence in its own limitations: the method inherits whatever ambiguity that encoder has about what a concept is. The other uses it to encode language instructions in an ablation, where replacing a visual task representation with such encoded instructions costs 8.6 points. Its role in both is as a component whose failure modes propagate into results built on it — which is worth recording, since neither paper is in a position to audit it.

- **Kind**: model
- **Also called**: CLIP encoder
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [adversarial robustness](../concepts/adversarial-robustness.md), [causal intervention](../methods/causal-intervention.md), [cosine similarity](../methods/cosine-similarity.md), [flow matching](../methods/flow-matching.md), [foresight](../concepts/foresight.md), [GPT-4o-mini](gpt-4o-mini.md), [jailbreak](../concepts/jailbreak.md), [latent reasoning](../concepts/latent-reasoning.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [safety alignment](../concepts/safety-alignment.md), [t-SNE](../methods/t-sne.md), [test-time scaling](../methods/test-time-scaling.md)

## Appears in

- [Test-Time Scaling for Safe Text-Guided Image Generation via Intermediate Clean Estimates](../../archive/papers/2026/arxiv-2608-03284/summary.md) — Triggers a safety intervention in image diffusion from the intermediate clean-image estimate rather than from the prompt, and spends optimization only from the first timestep where a violation actually appears — so extra test-time compute is incurred on unsafe inputs and benign latency stays flat as the budget grows.
- [LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipulation](../../archive/papers/2026/arxiv-2608-03701/summary.md) — Builds a 0.5B world-action model for robot manipulation whose future-state prediction and action generation share one compact latent in a single token stream, specifies the task as a direction in visual feature space instead of language, and shows a frozen self-supervised vision encoder beating a four-times-larger pretrained vision-language backbone at the same training budget.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
