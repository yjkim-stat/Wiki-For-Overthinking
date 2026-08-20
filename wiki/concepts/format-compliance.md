# format compliance

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Brumo](../datasets/brumo.md), [CMIMC](../datasets/cmimc.md), [component ablation](../methods/component-ablation.md), [coverage](coverage.md), [credit assignment](credit-assignment.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [degenerate generation](degenerate-generation.md), [distribution mismatch](distribution-mismatch.md), [distribution shift](distribution-shift.md), [GRPO](../methods/grpo.md), [HMMT](../datasets/hmmt.md), [knowledge distillation](../methods/knowledge-distillation.md), [MATH](../datasets/math.md), [MathVista](../datasets/mathvista.md), [Minerva](../datasets/minerva.md), [OlympiadBench](../datasets/olympiadbench.md), [on-policy distillation](../methods/on-policy-distillation.md), [out-of-distribution generalization](out-of-distribution-generalization.md), [outcome reward](outcome-reward.md), [pass@k](pass-k.md), [prompt sensitivity](prompt-sensitivity.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [Qwen3-1.7B-Base](../models/qwen3-1-7b-base.md), [Qwen3-8B](../models/qwen3-8b.md), [Qwen3-VL-8B](../models/qwen3-vl-8b.md), [reward hacking](reward-hacking.md), [reward shaping](reward-shaping.md), [RLVR](../methods/rlvr.md), [teacher-student gap](teacher-student-gap.md), [token selection](token-selection.md)

## What we have settled

- **Established** — A local metric — per-step correctness, token agreement, trace length — can be driven to its ceiling by a globally degenerate generation, so its satisfaction certifies nothing about the trajectory; only a terminal check on the whole output separates the two.
  - Three independent groups in three unrelated settings, each catching the same failure only because they reported a global diagnostic alongside the local one. In video-anomaly tool orchestration, removing the task-completion reward leaves decision accuracy and tool-selection accuracy at a perfect 100.00% while whole-response accuracy falls to 29.92%: the agent picks the right tool at every step and never stops, which the authors read as endless tool-use loops. In on-policy distillation, the objective's own metric is the one that degenerates — students reach near-perfect token agreement with the teacher by falling into repetitive loops, and under strong teacher-student mismatch standard distillation produces 22,395-token responses of which 65.5% contain no boxed answer at all, against 7,294 tokens and 5.4% for the method that fixes it; the accuracy gap of 6.9 to 20.3 is therefore largely a termination gap rather than a capability gap. In subjective verification, a length target that is not conditioned on correctness is met with roughly 990 tokens of coherent but functionally useless filler at macro-F1 0.760, indistinguishable from the collapsed baseline, while an unconstrained version is exploited to the 8192-token context limit with F1 falling to 0.210. Two further observations sharpen the practical rule. The same distillation paper's ablation shows a configuration that improves the headline while worsening the behaviour — selection alone lifts Avg@8 from 6.87 to 14.58 while pushing response length from 22.4K to 29.7K tokens — and its hyperparameter sweep moves accuracy by 0.3 points across four settings while moving response length from 26.9K to 5.1K and format errors from 5,510 to 482, so a sweep judged on accuracy alone would have called the parameter inert. The reading is that response length, format-failure rate and whole-trajectory success are not appendix material: whenever a training signal can affect generation behaviour, they are the only things separating a saturated local metric from a working system.

## Appears in

- [Improving Generalization Robustness of Multimodal RLVR](../../archive/papers/2026/arxiv-2608-08802/summary.md) — Traces the brittleness of multimodal RLVR gains under paraphrase and template change to two properties of the standard objective -- a binary verifier that cannot distinguish a wrong answer from a misformatted one, and a training distribution covering a thin slice of the prompts a deployed model meets -- and fixes both with a trinary reward and an invariance penalty across semantically equivalent prompts.
- [Mismatch Matters: On-Policy Distillation Beyond Token Agreement](../../archive/papers/2026/arxiv-2608-09836/summary.md) — Identifies degenerate agreement -- students reaching near-perfect token agreement with a teacher by looping while the response as a whole is broken -- and replaces the agreement objective with two directional mismatch corrections, one bounding runaway excess tokens and one injecting teacher-preferred mass at positions the student almost never samples.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
