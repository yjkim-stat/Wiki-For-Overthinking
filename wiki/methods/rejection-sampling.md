# rejection sampling

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [advantage estimation](../concepts/advantage-estimation.md), [backtracking](../concepts/backtracking.md), [Bamboogle](../datasets/bamboogle.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [component ablation](component-ablation.md), [credit assignment](../concepts/credit-assignment.md), [error compounding](../concepts/error-compounding.md), [GiGPO](gigpo.md), [GPT-5.5](../models/gpt-5-5.md), [group-relative advantage](../concepts/group-relative-advantage.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [HotpotQA](../datasets/hotpotqa.md), [HumanEval+](../datasets/humaneval.md), [Kimi-K2.6](../models/kimi-k2-6.md), [knowledge distillation](knowledge-distillation.md), [LiveCodeBench](../datasets/livecodebench.md), [LoRA](lora.md), [MATH](../datasets/math.md), [MBPP+](../datasets/mbpp.md), [MuSiQue](../datasets/musique.md), [Natural Questions](../datasets/natural-questions.md), [outcome reward](../concepts/outcome-reward.md), [privileged information](../concepts/privileged-information.md), [process reward](../concepts/process-reward.md), [process supervision](../concepts/process-supervision.md), [Qwen2.5-3B](../models/qwen2-5-3b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen2.5-Coder-7B](../models/qwen2-5-coder-7b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3.5-4B](../models/qwen3-5-4b.md), [Qwen3.6-27B](../models/qwen3-6-27b.md), [retrieval-augmented generation](retrieval-augmented-generation.md), [reward hacking](../concepts/reward-hacking.md), [self-correction](../concepts/self-correction.md), [Skywork-OR1](../models/skywork-or1.md), [supervised fine-tuning](supervised-fine-tuning.md), [teacher-student gap](../concepts/teacher-student-gap.md), [TriviaQA](../datasets/triviaqa.md), [verifiable reward](../concepts/verifiable-reward.md), [zero-advantage group](../concepts/zero-advantage-group.md)

## Appears in

- [DiDPO: Diff-in-Diff Policy Optimization for Coding Agent Training](../../archive/papers/2026/arxiv-2608-07147/summary.md) — Assigns credit in coding-agent RL by splitting each code diff into sub-diffs, matching semantically similar sub-diffs across rollouts to form advantage groups, and projecting the resulting diff-level advantage back onto the tokens that produced it.
- [LoongReflect: Boosting Long-Horizon Reflection in Search Agents via Global Perspective Distillation](../../archive/papers/2026/arxiv-2608-11967/summary.md) — Gives a search agent an explicitly reversible trajectory tree with reflect and backtrack as first-class actions, and trains the reflection policy with a dense local signal distilled from a teacher that can see the whole trajectory alongside the sparse terminal reward the local decision is ultimately judged by.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
