# self-distillation

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [AdvBench](../datasets/advbench.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [benchmark contamination](benchmark-contamination.md), [credit assignment](credit-assignment.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DeepSeek-V3.2](../models/deepseek-v3-2.md), [EOPD](../methods/eopd.md), [exponential tilting](../methods/exponential-tilting.md), [factorial ablation](../methods/factorial-ablation.md), [few-shot prompting](../methods/few-shot-prompting.md), [forward KL divergence](../methods/forward-kl-divergence.md), [GCG](../methods/gcg.md), [GKD](../methods/gkd.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [HarmBench](../datasets/harmbench.md), [hindsight](hindsight.md), [HMMT 2025](../datasets/hmmt-2025.md), [jailbreak](jailbreak.md), [KL regularization](../methods/kl-regularization.md), [knowledge distillation](../methods/knowledge-distillation.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [MMLU-Pro](../datasets/mmlu-pro.md), [on-policy distillation](../methods/on-policy-distillation.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [out-of-distribution generalization](out-of-distribution-generalization.md), [PAIR](../methods/pair.md), [paired bootstrap](../methods/paired-bootstrap.md), [pass@k](pass-k.md), [privileged information](privileged-information.md), [Qwen3-0.6B](../models/qwen3-0-6b.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-1.7B-Base](../models/qwen3-1-7b-base.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [Qwen3-8B](../models/qwen3-8b.md), [safety alignment](safety-alignment.md), [StrongREJECT](../datasets/strongreject.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [teacher-student gap](teacher-student-gap.md), [verifiable reward](verifiable-reward.md), [zero-advantage group](zero-advantage-group.md)

## Appears in

- [PAST: Privileged Adaptation from Complete Student Trajectories for On-Policy Self-Distillation](../../archive/papers/2026/arxiv-2608-08726/summary.md) — Gives the teacher in on-policy self-distillation access to each completed student rollout and its verified outcome, adapting it to preserve behaviour on successes and redirect failures toward verified success, while the student keeps a prefix-only interface it can actually deploy.
- [Dual-Adversarial Safety Alignment: Cultivating Intrinsic Threat Comprehension in LRMs](../../archive/papers/2026/arxiv-2608-09542/summary.md) — Builds safety-alignment training data by first having an agent jailbreak a strong teacher and only then asking that teacher to explain why the successful attack worked, so the student is supervised on the mechanism of the attack rather than on the refusal.
- [Distill Skills into Weights, Not Prompts: Abstract Skills as Privileged Signals for On-Policy Self-Distillation](../../archive/papers/2026/arxiv-2608-09826/summary.md) — Gives the teacher branch of an on-policy self-distillation setup an abstract skill card -- a principle, when it applies, and the mistakes to avoid -- instead of the reference solution, so the privileged signal carries no answer and the gain lands on exactly the rollout groups where group-relative reward is algebraically silent.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
