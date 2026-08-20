# Llama-3-8B

<!-- auto:begin -->

An 8B Llama, used across 3 sources as the second family in method comparisons. Its recurring role is as the arm where a Qwen-developed method loses or shrinks: one preference method that reaches 62.33 percent on a mathematics set with a Qwen backbone loses to a baseline here (23.01 against 23.51), and a tool-orchestration method's interrelated-split gain on it is 6.2 points from a much lower base against 5.4 on the strong backbone -- which that source's own limitations note flags as the abstract's headline not being the typical case. It also appears in reasoning-failure detection from trace dynamics.

- **Kind**: model
- **Also called**: Llama-3-8B, Llama3-8B
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [backtracking](../concepts/backtracking.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [credit assignment](../concepts/credit-assignment.md), [DPO](../methods/dpo.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [hidden-state geometry](../concepts/hidden-state-geometry.md), [KL regularization](../methods/kl-regularization.md), [Llama-3.1-8B](llama-3-1-8b.md), [Llama-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [Mistral-7B-v0.3](mistral-7b-v0-3.md), [monitorability](../concepts/monitorability.md), [outcome reward](../concepts/outcome-reward.md), [overthinking](../concepts/overthinking.md), [paired bootstrap confidence intervals](../methods/paired-bootstrap-confidence-intervals.md), [preference optimization](../methods/preference-optimization.md), [process reward](../concepts/process-reward.md), [process supervision](../concepts/process-supervision.md), [Qwen2.5-VL](qwen2-5-vl.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-4B-Instruct-2507](qwen3-4b-instruct-2507.md), [Qwen3-8B](qwen3-8b.md), [Qwen3-VL-8B](qwen3-vl-8b.md), [ReAct](../methods/react.md), [reasoning boundary](../concepts/reasoning-boundary.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [reward shaping](../methods/reward-shaping.md), [self-consistency](../methods/self-consistency.md), [self-correction](../concepts/self-correction.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [tool learning](../concepts/tool-learning.md), [tool orchestration](../concepts/tool-orchestration.md), [Vicuna-7B](vicuna-7b.md)

## Appears in

- [Cloud-ScPO: Hidden-State Geometry for Semi-Supervised Preference Optimization in LLM Reasoning](../../archive/papers/2026/arxiv-2608-01014/summary.md) — Scores unlabeled reasoning trajectories by how their mean-pooled hidden states connect to correct and incorrect reference point clouds built from a small labeled set, and uses that score to pick the concrete chosen and rejected responses inside answer clusters that self-consistency has already separated.
- [The Tell-Tale Trace: Detecting Reasoning Failures in LLMs Using Chain-of-Thought Dynamics](../../archive/papers/2026/arxiv-2608-03291/summary.md) — Tags every sentence of a reasoning trace by its function and studies the sequence rather than the content, finding that failing SAT traces collapse into repetitive verification and commit early, that failing UNSAT traces run the wrong procedure entirely, and that a prompt naming the missing procedure recovers 84.6% of them.
- [VTO: Visual Tool Orchestration for Video Anomaly Detection](../../archive/papers/2026/arxiv-2608-08219/summary.md) — Trains a multimodal agent to orchestrate twelve video-analysis tools for anomaly detection with GRPO under a dual reward that combines exact-match rule checks with an LLM judge scoring logicality, relevance and completeness, and releases the benchmark it is evaluated on.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
