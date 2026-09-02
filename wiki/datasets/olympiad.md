# Olympiad

<!-- auto:begin -->

OlympiadBench (competition-level math/science problems) is used across these sources as a hard-tier evaluation benchmark for reasoning-efficiency and adaptive-reasoning methods: TH2T reports inference-cost reductions on it as one of its 'hard task' benchmarks, TNT reports accuracy gains on it under its per-query non-thinking token limit, and ADaPT includes it in its Hard task group when evaluating token-level dual-process reasoning.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [CoT-Valve (baseline)](../methods/cot-valve-baseline.md), [DeepScaleR-1.5B](../models/deepscaler-1-5b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [GPQA](gpqa.md), [GRPO](../methods/grpo.md), [GRPO (baseline)](../methods/grpo-baseline.md), [GSM8K](gsm8k.md), [LiveCodeBench](livecodebench.md), [MATH500](math500.md), [Minerva](minerva.md), [MMLU](mmlu.md), [MMLU-Pro](mmlu-pro.md), [NoThinking (baseline)](../methods/nothinking-baseline.md), [Omni-MATH](omni-math.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-3B-Base](../models/qwen2-5-3b-base.md), [Qwen2.5-7B-Base](../models/qwen2-5-7b-base.md), [SFT (baseline)](../methods/sft-baseline.md), [TLMRE (baseline)](../methods/tlmre-baseline.md), [TokenSkip (baseline)](../methods/tokenskip-baseline.md)

## Appears in

- [Think How to Think: Mitigating Overthinking with Autonomous Difficulty Cognition in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1766/summary.md) — TH2T (Think-How-to-Think) is a two-stage fine-tuning method that first injects an explicit 'difficulty hypnosis' cue into a model's output prefix (prospective, global strategy selection) and then a 'redundancy hypnosis' cue into in-progress reasoning to truncate reflection loops (retrospective, local correction), cutting inference cost over 70% on easy tasks and 40% on hard tasks with minimal accuracy loss and no external difficulty labels at inference time.
- [Thinking-Based Non-Thinking: Solving the Reward Hacking Problem in Training Hybrid Reasoning Models via Reinforcement Learning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2122/summary.md) — Identifies reward hacking in RL-trained hybrid (think/no-think) reasoning models -- when non-thinking responses are rewarded more, models embed reasoning inside the response mode misclassified as 'non-thinking' to collect the higher reward -- and fixes it with TNT, which derives a per-query maximum non-thinking token limit from the thinking mode's own solution-segment length rather than a uniform threshold, cutting token usage ~50% while significantly improving accuracy and keeping reward-hacking incidence below 10%.
- [ADaPT: Token-Level Decoupling for Efficient Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-165/summary.md) — ADaPT diagnoses that existing efficiency-oriented RL methods fail because sequence-level efficiency rewards implicitly penalize correct-but-long reasoning (a structural mismatch, since only the first token -- the fast/slow mode choice -- actually determines efficiency, while all subsequent tokens can only affect correctness), and fixes this by applying an efficiency reward exclusively to a dedicated mode-selection <think>/<answer> token via a CISPO-stabilized token-level GRPO variant -- cutting Qwen2.5-7B's average generation length from 1540 to 1031 tokens (SFT+GRPO baseline) with only a 0.4-point accuracy drop, tracing a genuine Pareto frontier other methods stay strictly inside, and letting a single trained model's efficiency be tuned post-hoc by adjusting the mode-token's decoding threshold with no retraining.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
