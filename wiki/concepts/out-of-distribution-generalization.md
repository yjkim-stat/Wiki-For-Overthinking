# out-of-distribution generalization

<!-- auto:begin -->

Whether a capability survives inputs unlike those trained on, and the measurement this archive keeps finding discriminating. In-distribution accuracy dissociates from it repeatedly: models generalize systematically for comparison but not for composition despite similar in-distribution performance; RL-trained models lose 20-95% when benchmark constants are changed; a compositional benchmark pairing one commonsense step with one mathematical step drops accuracy by nearly 30% against solving each in isolation, where humans show no such gap; and a routing method's difficulty estimates transfer only when difficulty is modelled as a function of the query rather than as a free per-item parameter. One entry bounds the whole question: for transformers of depth two or beyond no computable bound exists on how long the training inputs must be for correctness to extend to longer ones, so in the general case the recurring empirical failures are not a tuning problem.

- **Kind**: concept
- **Also called**: OOD generalization, systematicity
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 5

**Related**: [activation probing](../methods/activation-probing.md), [AIME24](../datasets/aime24.md), [attention analysis](../methods/attention-analysis.md), [calibration](../methods/calibration.md), [causal analysis](../methods/causal-analysis.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [circuit analysis](../methods/circuit-analysis.md), [compositional generalization](compositional-generalization.md), [construct validity](construct-validity.md), [effective depth](effective-depth.md), [error detection](error-detection.md), [expressivity](expressivity.md), [finite precision](finite-precision.md), [generalization](generalization.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [implicit reasoning](implicit-reasoning.md), [length generalization](length-generalization.md), [linear probe](../methods/linear-probe.md), [LiveCodeBench](../datasets/livecodebench.md), [localization](localization.md), [MATH500](../datasets/math500.md), [membership inference](../methods/membership-inference.md), [memorization](memorization.md), [MMLU](../datasets/mmlu.md), [prompt difficulty](prompt-difficulty.md), [reasoning trajectory](reasoning-trajectory.md), [residual stream](residual-stream.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [scaling laws](scaling-laws.md), [test-time compute](test-time-compute.md)

## Appears in

- [Reasoning Errors Have a Region and a Direction in the Residual-Stream Trajectory of LLMs](../../archive/papers/2026/arxiv-2608-05660/summary.md) — Detects flawed reasoning from residual-stream trajectories by combining layerwise motion with a quantized region reader and a normalized direction reader, rather than probing full states.
- [AgentCoMa: A Compositional Benchmark Mixing Commonsense and Mathematical Reasoning in Real-World Scenarios](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-380/summary.md) — A benchmark where each task needs one commonsense step and one math step, on which model accuracy drops nearly 30% relative to solving the steps in isolation while humans show no such gap.
- [Grokked Transformers are Implicit Reasoners: A Mechanistic Journey to the Edge of Generalization](../../archive/papers/2024/local-6252abed1b134f57/summary.md) — Shows that transformers can learn implicit multi-step reasoning over stored knowledge, but only through grokking — extended training far past overfitting — and that whether the resulting circuit generalizes out of distribution depends on the reasoning type, succeeding for comparison and failing for composition.
- [RADAR: Reasoning-Ability and Difficulty-Aware Routing for Reasoning LLMs](../../archive/papers/2026/local-acb4e6ecc12e897d/summary.md) — Routes each query to a {model, reasoning budget} configuration by fitting an item response theory model over an evaluation matrix, yielding interpretable query difficulties and configuration abilities, and sending harder queries to higher-ability configurations.
- [Length Generalization Bounds for Transformers](../../archive/papers/2026/local-bd58c1406f4a1ef5/summary.md) — Proves that no computable length-generalization bound exists for transformers of depth two or beyond, and gives a matching exponential bound for the positive fragment that corresponds to fixed-precision transformers.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
