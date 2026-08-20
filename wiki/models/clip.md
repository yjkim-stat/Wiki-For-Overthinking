# CLIP

<!-- auto:begin -->

A contrastive vision-language embedding model, used across 3 sources both as a component and as a metric of image-text alignment. Its most informative appearance in this archive is as the axis on which a safety intervention's collateral damage is read: a weight-preserving method holds alignment at 25.25 against the base model's 25.93 while a training-required baseline reaches lower detection rates at 23.59 alignment and much worse image quality -- so the comparison shows the training route buying suppression by damaging general generation and the weight-preserving route not doing so. Elsewhere it supplies features for label-free screening and appears as an alternative conditioning pathway in robotic manipulation, where replacing a visual task token with its language encoding costs 8.6 points.

- **Kind**: model
- **Also called**: CLIP encoder, CLIP score
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [activation steering](../methods/activation-steering.md), [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [adversarial robustness](../concepts/adversarial-robustness.md), [bootstrap confidence intervals](../methods/bootstrap-confidence-intervals.md), [causal intervention](../methods/causal-intervention.md), [class imbalance](../concepts/class-imbalance.md), [COCO](../datasets/coco.md), [contrastive activation addition](../methods/contrastive-activation-addition.md), [cosine similarity](../methods/cosine-similarity.md), [detection versus control](../concepts/detection-versus-control.md), [difference-in-means direction](../methods/difference-in-means-direction.md), [flow matching](../methods/flow-matching.md), [foresight](../concepts/foresight.md), [GPT-4o-mini](gpt-4o-mini.md), [jailbreak](../concepts/jailbreak.md), [latent reasoning](../concepts/latent-reasoning.md), [linear probe](../methods/linear-probe.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [permutation test](../methods/permutation-test.md), [Qwen3-VL-2B](qwen3-vl-2b.md), [ROC analysis](../methods/roc-analysis.md), [safety alignment](../concepts/safety-alignment.md), [shortcut learning](../concepts/shortcut-learning.md), [steering vector](../methods/steering-vector.md), [t-SNE](../methods/t-sne.md), [test-time scaling](../concepts/test-time-scaling.md), [visual grounding](../concepts/visual-grounding.md)

## Appears in

- [Test-Time Scaling for Safe Text-Guided Image Generation via Intermediate Clean Estimates](../../archive/papers/2026/arxiv-2608-03284/summary.md) — Triggers a safety intervention in image diffusion from the intermediate clean-image estimate rather than from the prompt, and spends optimization only from the first timestep where a violation actually appears — so extra test-time compute is incurred on unsafe inputs and benign latency stays flat as the budget grows.
- [LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipulation](../../archive/papers/2026/arxiv-2608-03701/summary.md) — Builds a 0.5B world-action model for robot manipulation whose future-state prediction and action generation share one compact latent in a single token stream, specifies the task as a direction in visual feature space instead of language, and shows a frozen self-supervised vision encoder beating a four-times-larger pretrained vision-language backbone at the same training budget.
- [Label-Free Parkinson's Disease Screening from Face and Voice through Mechanistic Interpretability](../../archive/papers/2026/arxiv-2608-08976/summary.md) — Builds a Parkinson's screen from control data alone using a contrastive activation direction derived from synthetically degraded healthy speech and a nearest-neighbour anomaly score in face-encoder space, and gives a measurable precondition -- positive cosine between the synthetic and real disease directions -- that predicts in advance which modality the steering primitive will work on.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
