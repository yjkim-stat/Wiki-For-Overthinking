# self-reflection

<!-- auto:begin -->

A model reviewing and critiquing its own reasoning before committing. The sources place it differently. One reports it emerging from reinforcement learning on verifiable outcomes without being demonstrated, alongside verification and dynamic strategy adaptation. The other treats it as one selectable tool among several in an adaptive inference agent, and finds it outperforms plain chain-of-thought specifically at low iteration counts — explicit self-critique is most valuable when only a few attempts are available, with the gap narrowing as iterations increase. The archive's faithfulness work complicates both readings: spontaneous self-corrections have measured precision of 24.4%, and much of the language that looks like self-critique falls after the answer is already fixed.

- **Kind**: method
- **Also called**: self-critique
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [adversarial robustness](../concepts/adversarial-robustness.md), [AIME24](../datasets/aime24.md), [beam search](beam-search.md), [best-of-n](best-of-n.md), [chain of thought](chain-of-thought.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [MATH500](../datasets/math500.md), [Monte Carlo tree search](monte-carlo-tree-search.md), [post-training](post-training.md), [process reward model](process-reward-model.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [reasoning distillation](reasoning-distillation.md), [reinforcement learning with verifiable rewards](../concepts/reinforcement-learning-with-verifiable-rewards.md), [safety alignment](../concepts/safety-alignment.md), [self-correction](../concepts/self-correction.md), [test-time compute](../concepts/test-time-compute.md), [verification](../concepts/verification.md)

## Appears in

- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](../../archive/papers/2025/arxiv-2501-12948/summary.md) — Shows that reasoning ability can be incentivized in an LLM by pure reinforcement learning on verifiable tasks, with no human-annotated reasoning trajectories, and that the resulting reasoning patterns can be transferred to smaller models.
- [Self-Reflection Improves Safety of Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-678/summary.md) — Adds a Self-Reflection token that lets reasoning models recover from harmful output mid-generation, cutting harmful completion rate from 13.8% to 4.1%.
- [What If We Allocate Test-Time Compute Adaptively?](../../archive/papers/2026/local-80ef8b5ce7217f7c/summary.md) — Replaces uniform test-time compute allocation with a training-free agent that picks reasoning tools, a search strategy and an exploration parameter per problem, using a process reward model both to prune within a trajectory and to select across iterations.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
