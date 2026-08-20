# Gemma-3-12B

<!-- auto:begin -->

A 12-billion-parameter Gemma model appearing twice in this archive as an evaluated subject. In the CAD generation study it is one of the two weaker of four generators, and consequently the one where consensus selection helps most -- 8 to 10 percent relative reduction in Chamfer distance against 1 to 3 percent for the stronger models, which is that paper's evidence that a selection rule's value is inversely related to the quality of what it selects among. It also appears in the inverted-steering-vector study, whose finding is that a direction can be highly discriminative for a concept and reliably steer the model the opposite way. Neither source characterises the model itself.

- **Kind**: model
- **Also called**: Gemma 3 12B
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation steering](../methods/activation-steering.md), [attention head](../concepts/attention-head.md), [best-of-n](../methods/best-of-n.md), [causal intervention](../methods/causal-intervention.md), [consensus](../concepts/consensus.md), [contrastive activation addition](../methods/contrastive-activation-addition.md), [detection versus control](../concepts/detection-versus-control.md), [difference-of-means probe](../methods/difference-of-means-probe.md), [Gemini-3-Flash](gemini-3-flash.md), [generation-verification gap](../concepts/generation-verification-gap.md), [GPT-4.1-mini](gpt-4-1-mini.md), [gpt-oss-20b](gpt-oss-20b.md), [Inference Time Intervention](../methods/inference-time-intervention.md), [linear probe](../methods/linear-probe.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [majority voting](../methods/majority-voting.md), [matched-budget comparison](../methods/matched-budget-comparison.md), [pool oracle](../concepts/pool-oracle.md), [Qwen2.5-14B](qwen2-5-14b.md), [representation versus readout](../concepts/representation-versus-readout.md), [selection signal](../concepts/selection-signal.md), [self-consistency](../methods/self-consistency.md), [steering vector](../methods/steering-vector.md), [test-time scaling](../concepts/test-time-scaling.md), [TruthfulQA](../datasets/truthfulqa.md), [verifier-free verification](../methods/verifier-free-verification.md)

## Appears in

- [Inverted Detection and Control in Steering Vectors](../../archive/papers/2026/arxiv-2608-02957/summary.md) — Finds directions that are highly discriminative for a concept and aligned with its positive examples yet reliably steer the model the opposite way, characterizes them geometrically as spoofing the concept's absence downstream, and turns that characterization into a training-free test that fixes the sign — improving a standard steering pipeline in 27 of 30 experiments.
- [Test-Time Scaling for CAD Generation via Verifier-Free Consensus Selection](../../archive/papers/2026/arxiv-2608-09706/summary.md) — Asks whether a candidate pool contains enough signal to select from itself, by compiling sampled CAD programs into 3D models and returning the one that agrees most with the rest -- and finds this verifier-free rule beats a vision-language verifier on every geometric metric when both select from the identical pool.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
