# factorial ablation

<!-- auto:begin -->

Toggling each named ingredient of a system on and off across all combinations rather than removing them one at a time, so that interaction between them becomes visible instead of being assumed away. Both sources use it to answer a question a sequential ablation cannot, and reach opposite structural conclusions. The agent-contamination work runs a 2^3 factorial over name binding, event triggering and propagation (5 seeds x 4 scenarios per cell) and finds no synergy at all: name binding alone produces 95 percent and 45 percent contamination while every configuration without it is exactly 0 percent, the other two factors have negligible main effects at |d| <= 0.26, and the authors therefore fit no interaction terms and state that the 0 percent result is partly by construction. The distillation work runs a 2x2 over trajectory access and teacher adaptation and finds the opposite: 0.555 and 0.092 macro points for the single factors against 5.617 for the combination, with each single-factor condition degrading at least one task, so the contribution is the interaction and no ingredient could be credited on its own. Taken together the sources make the case for the design rather than for either result -- a one-at-a-time ablation would have reported a large effect for name binding in the first case and no effect for anything in the second.

- **Kind**: method
- **Also called**: 2x2 ablation, factorial design
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [credit assignment](../concepts/credit-assignment.md), [DeepSeek-V3.2](../models/deepseek-v3-2.md), [Gemini-2.0-flash](../models/gemini-2-0-flash.md), [GPT-4o](../models/gpt-4o.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [GRPO](grpo.md), [KL regularization](kl-regularization.md), [knowledge distillation](knowledge-distillation.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.3-70B](../models/llama-3-3-70b.md), [LLM-as-a-judge](llm-as-a-judge.md), [on-policy distillation](on-policy-distillation.md), [on-policy self-distillation](on-policy-self-distillation.md), [pass@k](../concepts/pass-k.md), [privileged information](../concepts/privileged-information.md), [Qwen2.5-coder-7B](../models/qwen2-5-coder-7b.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-VL-235B](../models/qwen3-vl-235b.md), [ReAct](react.md), [self-verification](../concepts/self-verification.md), [supervised fine-tuning](supervised-fine-tuning.md), [teacher-student gap](../concepts/teacher-student-gap.md)

## Appears in

- [Persistent Semantic Entities in Tool-Augmented LLM Systems](../../archive/papers/2026/arxiv-2608-07952/summary.md) — Formalises implicit agent state that survives session boundaries as Persistent Semantic Entities defined by name binding, event triggering and propagation, and measures across 24 models that whether injected contamination decays depends on what kind of contamination it is rather than on model scale or deployment.
- [PAST: Privileged Adaptation from Complete Student Trajectories for On-Policy Self-Distillation](../../archive/papers/2026/arxiv-2608-08726/summary.md) — Gives the teacher in on-policy self-distillation access to each completed student rollout and its verified outcome, adapting it to preserve behaviour on successes and redirect failures toward verified success, while the student keeps a prefix-only interface it can actually deploy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
