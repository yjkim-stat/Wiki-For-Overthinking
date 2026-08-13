# long chain-of-thought distillation

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [AIME](../datasets/aime.md), [backtracking](../concepts/backtracking.md), [credit assignment](../concepts/credit-assignment.md), [DAPO](dapo.md), [DAPO-Math-17k](../datasets/dapo-math-17k.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-V3](../models/deepseek-v3.md), [entropy collapse](../concepts/entropy-collapse.md), [exploration](../concepts/exploration.md), [GEMBA-MQM](gemba-mqm.md), [Gemini-2.0-flash](../models/gemini-2-0-flash.md), [GPT-4o](../models/gpt-4o.md), [GPT-5](../models/gpt-5.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [GRPO](grpo.md), [KL regularization](kl-regularization.md), [LLM-as-a-judge](llm-as-a-judge.md), [outcome reward](../concepts/outcome-reward.md), [pass@k](pass-k.md), [policy entropy](../concepts/policy-entropy.md), [process reward](../concepts/process-reward.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-8B-Base](../models/qwen3-8b-base.md), [reasoning boundary](../concepts/reasoning-boundary.md), [reward shaping](../concepts/reward-shaping.md), [RLVR](rlvr.md), [supervised fine-tuning](supervised-fine-tuning.md), [teacher forcing](teacher-forcing.md), [WMT22](../datasets/wmt22.md)

## Appears in

- [BODHI: Do LLMs Branch Out and Discover Heterogeneous Inferences?](../../archive/papers/2026/arxiv-2608-02867/summary.md) — Builds prefix trees of semantically equivalent reasoning statements and measures how RLVR changes a model's preference between branches, finding the entropy collapse is not stylistic — the collapse is stronger for semantically distinct continuations than for syntactic variants of the same statement.
- [PAMT: Process-Aligned Reinforcement Learning for Multi-Domain Machine Translation](../../archive/papers/2026/arxiv-2608-03077/summary.md) — Scores each reasoning step of a translation by how much appending it raises a frozen reference model's teacher-forced likelihood of the gold translation, and adds that as a dense per-step reward on top of sequence-level quality — after first establishing that explicit reasoning helps long and hard inputs while drifting on terminology and style.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
