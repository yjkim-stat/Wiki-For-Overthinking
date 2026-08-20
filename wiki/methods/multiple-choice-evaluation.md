# multiple-choice evaluation

<!-- auto:begin -->

Scoring a model by whether it selects the reference option, which buys unambiguous labels at the cost of compressing a capability into verification. Both sources use it and both record a distortion it introduces. The industrial-safety benchmark scores exclusively by exact option match with unparseable outputs counted incorrect, and its own diagnostics catch what that hides: on a set deliberately balanced across answer positions, a base model scores 52.4 percent when the correct option is A and 31.6 to 33.6 percent for the other positions, a response-format shortcut that an unbalanced set would have scored as competence. The proverb benchmark isolates the format effect directly, finding models that complete proverbs successfully yet fail the multiple-choice version when no correct option is present, with chain-of-thought analysis showing they name the right ending while failing to notice its absence. Read together the sources say that a multiple-choice score measures selection under a fixed option set, that position balance is a minimum precaution rather than a refinement, and that the none-of-the-above case is where the format and the underlying capability come apart most sharply.

- **Kind**: method
- **Also called**: multiple choice
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [abstention](../concepts/abstention.md), [benchmark contamination](../concepts/benchmark-contamination.md), [benchmark design](../concepts/benchmark-design.md), [calibration](calibration.md), [chain of thought](chain-of-thought.md), [chain-of-thought distillation](chain-of-thought-distillation.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [construct validity](../concepts/construct-validity.md), [decontamination](decontamination.md), [figurative language](../concepts/figurative-language.md), [Gemini-3.1-Pro](../models/gemini-3-1-pro.md), [Gemini-3.5-Flash](../models/gemini-3-5-flash.md), [GPT-5.5](../models/gpt-5-5.md), [GPT-5.6-Sol](../models/gpt-5-6-sol.md), [LoRA](lora.md), [macro versus micro accuracy](../concepts/macro-versus-micro-accuracy.md), [memorization](../concepts/memorization.md), [multi-hop reasoning](../concepts/multi-hop-reasoning.md), [position bias](../concepts/position-bias.md), [Qwen3.5-9B](../models/qwen3-5-9b.md), [Qwen3.6-27B](../models/qwen3-6-27b.md), [supervised fine-tuning](supervised-fine-tuning.md)

## Appears in

- [Easy to Complete, Hard to Choose: Investigating LLM Performance on the ProverbIT Benchmark](../../archive/papers/2026/arxiv-2608-04670/summary.md) — An Italian proverb benchmark on which models complete proverbs successfully but fail multiple-choice selection when no correct option is present, with CoT analysis showing they name the right ending while failing to notice its absence.
- [SafeSceneReason: A Multimodal Reasoning Benchmark Connecting Industrial Hazards with Accident Knowledge](../../archive/papers/2026/arxiv-2608-09230/summary.md) — Builds an industrial-safety reasoning benchmark from two pipelines -- program execution over safety scene graphs, and evidence graphs extracted from real accident-investigation reports -- and shows that general multimodal capability does not transfer to it while a 9B model fine-tuned on its chain-of-thought split matches frontier systems.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
