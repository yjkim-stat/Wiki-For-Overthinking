# theory of mind

<!-- auto:begin -->

Reasoning about what another agent knows, wants or intends, and in both sources here a capability whose apparent presence in language models has to be argued for rather than read off a score. One argues the gains reasoning models show are increased robustness to prompt and task perturbation rather than a theory-of-mind-specific ability -- the models are better at reaching the correct answer under variation, which reproduces on these tasks without requiring anything new. The other decomposes the capability into a 2x2 taxonomy crossing epistemic against motivational mental states and passive inference against active action, and validates that the decomposition is real by permutation test: item difficulty loads on the epistemic axis (-8.5 pp, p < 0.001) while the benefit of chain-of-thought loads on the orthogonal inference-action axis (-7.9 pp, p = 0.008), a double dissociation. Its central finding is that the failure is one of expression rather than representation -- linear probes recover 77 to 82 percent where the same models' own chain of thought reaches 62 to 70, injecting the ground-truth answer lifts accuracy 12.6 points across all 28 models without ever backfiring, and steering along a class-mean direction lifts output accuracy onto the probe ceiling. Neither source claims models possess theory of mind; both explain a measured score by something other than the capability its name implies.

- **Kind**: concept
- **Also called**: ToM
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [activation steering](../methods/activation-steering.md), [benchmark design](benchmark-design.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [class imbalance](class-imbalance.md), [construct validity](construct-validity.md), [detection versus control](detection-versus-control.md), [difference-in-means direction](../methods/difference-in-means-direction.md), [Gemini-2.5-Flash](../models/gemini-2-5-flash.md), [Gemini-2.5-pro](../models/gemini-2-5-pro.md), [GPT-5](../models/gpt-5.md), [linear probe](../methods/linear-probe.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [permutation test](../methods/permutation-test.md), [prompt sensitivity](prompt-sensitivity.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [Qwen3.5-2B](../models/qwen3-5-2b.md), [Qwen3-8B](../models/qwen3-8b.md), [representation versus readout](representation-versus-readout.md), [RLVR](../methods/rlvr.md), [robustness](robustness.md), [test-time scaling](test-time-scaling.md), [zero-shot prompting](../methods/zero-shot-prompting.md)

## Appears in

- [Evaluating Theory of Mind in Reasoning Models: Robustness over Reasoning](../../archive/papers/2026/arxiv-2608-04646/summary.md) — Tests reasoning models on Theory of Mind tasks and argues their gains are increased robustness to prompt and task perturbation rather than a new ToM-specific ability.
- [Avalon-ToM-Bench: Evaluating Fine-Grained Theory of Mind via Asymmetric Game Mechanics](../../archive/papers/2026/arxiv-2608-09638/summary.md) — Turns the hidden-role game Avalon into a diagnostic instrument rather than an arena, decomposing theory of mind into a 2x2 taxonomy of perspective-constrained binary statements, and shows by probing, ground-truth injection and steering that models represent the right answer internally while failing to say it.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
