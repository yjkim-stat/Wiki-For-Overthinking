# jailbreak

<!-- auto:begin -->

Eliciting behaviour a model was trained to refuse, which in the reasoning-model setting the sources treat as an attack on the reasoning process rather than on the prompt or the output. Two propose defences placed mid-trajectory, one injecting safety reflections at attention-identified points, the other extracting visual intent before generation after finding that risk cues are perceived and then overridden by narrative coherence. The third shows the attack side is far ahead: automated hijacking reaches approaching 100% success within one or a few turns against GPT-o3/o4-mini and Gemini-2.5-Flash, refining attempts from reasoning patterns the target leaks through its own refusals. Its conclusion is that reasoning transparency is itself an exploitable surface.

- **Kind**: concept
- **Also called**: guardrail bypass, jailbreaking, safety bypass
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [adversarial robustness](adversarial-robustness.md), [aha moment](aha-moment.md), [attention analysis](../methods/attention-analysis.md), [attention pattern](attention-pattern.md), [chain of thought](../methods/chain-of-thought.md), [CLIP](../models/clip.md), [Gemini-2.5-Flash](../models/gemini-2-5-flash.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [HarmBench](../datasets/harmbench.md), [Inference Time Intervention](inference-time-intervention.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [monitorability](monitorability.md), [multimodal reasoning](multimodal-reasoning.md), [safety alignment](safety-alignment.md), [test-time compute](test-time-compute.md), [test-time scaling](../methods/test-time-scaling.md)

## Appears in

- [Test-Time Scaling for Safe Text-Guided Image Generation via Intermediate Clean Estimates](../../archive/papers/2026/arxiv-2608-03284/summary.md) — Triggers a safety intervention in image diffusion from the intermediate clean-image estimate rather than from the prompt, and spends optimization only from the first timestep where a violation actually appears — so extra test-time compute is incurred on unsafe inputs and benign latency stays flat as the budget grows.
- [ReasoningGuard: Safeguarding Large Reasoning Models with Inference-time Safety Aha Moments](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1453/summary.md) — An inference-time safeguard that reads a reasoning model's attention to find key points in its reasoning path and injects safety reflections there, then scales sampling to pick a safe path.
- [Mitigating Safety Context Amnesia in Multimodal Reasoning Models via Intent-Guided Safety Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1821/summary.md) — Identifies a multimodal failure where models see the risky visual cue but let narrative coherence override safety as reasoning proceeds, and defends against it by extracting intent before generation.
- [AutoRAN: Automated Hijacking of Safety Reasoning in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1988/summary.md) — Automates the hijacking of a reasoning model's own safety reasoning by using a weaker, less-aligned model to simulate execution reasoning and refining attacks from patterns leaked in refusals.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
