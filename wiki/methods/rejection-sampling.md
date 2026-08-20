# rejection sampling

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [advantage estimation](../concepts/advantage-estimation.md), [backtracking](../concepts/backtracking.md), [Bamboogle](../datasets/bamboogle.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [component ablation](component-ablation.md), [credit assignment](../concepts/credit-assignment.md), [error compounding](../concepts/error-compounding.md), [expected calibration error](../concepts/expected-calibration-error.md), [GiGPO](gigpo.md), [GPT-4o](../models/gpt-4o.md), [GPT-5.5](../models/gpt-5-5.md), [group-relative advantage](../concepts/group-relative-advantage.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [hallucination](../concepts/hallucination.md), [HotpotQA](../datasets/hotpotqa.md), [HumanEval+](../datasets/humaneval.md), [Kimi-K2.6](../models/kimi-k2-6.md), [knowledge distillation](knowledge-distillation.md), [LiveCodeBench](../datasets/livecodebench.md), [LLM-as-a-judge](llm-as-a-judge.md), [LoRA](lora.md), [MATH](../datasets/math.md), [MBPP+](../datasets/mbpp.md), [MuSiQue](../datasets/musique.md), [Natural Questions](../datasets/natural-questions.md), [outcome reward](../concepts/outcome-reward.md), [PathVQA](../datasets/pathvqa.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [privileged information](../concepts/privileged-information.md), [process reward](../concepts/process-reward.md), [process supervision](../concepts/process-supervision.md), [Qwen2.5-3B](../models/qwen2-5-3b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen2.5-Coder-7B](../models/qwen2-5-coder-7b.md), [Qwen2.5-VL-7B-Instruct](../models/qwen2-5-vl-7b-instruct.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3.5-4B](../models/qwen3-5-4b.md), [Qwen3.6-27B](../models/qwen3-6-27b.md), [retrieval-augmented generation](retrieval-augmented-generation.md), [reward hacking](../concepts/reward-hacking.md), [reward shaping](../concepts/reward-shaping.md), [selective prediction](../concepts/selective-prediction.md), [self-correction](../concepts/self-correction.md), [Skywork-OR1](../models/skywork-or1.md), [supervised fine-tuning](supervised-fine-tuning.md), [teacher-student gap](../concepts/teacher-student-gap.md), [TriviaQA](../datasets/triviaqa.md), [verifiable reward](../concepts/verifiable-reward.md), [VQA-RAD](../datasets/vqa-rad.md), [zero-advantage group](../concepts/zero-advantage-group.md)

## Appears in

- [DiDPO: Diff-in-Diff Policy Optimization for Coding Agent Training](../../archive/papers/2026/arxiv-2608-07147/summary.md) — Assigns credit in coding-agent RL by splitting each code diff into sub-diffs, matching semantically similar sub-diffs across rollouts to form advantage groups, and projecting the resulting diff-level advantage back onto the tokens that produced it.
- [CARE: Confidence-Aware Reasoning for Reliable Medical VQA](../../archive/papers/2026/arxiv-2608-10964/summary.md) — Adds a correctness-conditioned confidence term to the GRPO reward for medical visual question answering -- rewarding answer-token confidence when the answer is right and penalising it when wrong -- on top of an SFT cold start built from answer-conditioned reasoning traces filtered by a verifier.
- [LoongReflect: Boosting Long-Horizon Reflection in Search Agents via Global Perspective Distillation](../../archive/papers/2026/arxiv-2608-11967/summary.md) — Gives a search agent an explicitly reversible trajectory tree with reflect and backtrack as first-class actions, and trains the reflection policy with a dense local signal distilled from a teacher that can see the whole trajectory alongside the sparse terminal reward the local decision is ultimately judged by.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
