# self-reflection

<!-- auto:begin -->

A model reviewing and critiquing its own reasoning before committing. The sources place it differently. One reports it emerging from reinforcement learning on verifiable outcomes without being demonstrated, alongside verification and dynamic strategy adaptation. The other treats it as one selectable tool among several in an adaptive inference agent, and finds it outperforms plain chain-of-thought specifically at low iteration counts — explicit self-critique is most valuable when only a few attempts are available, with the gap narrowing as iterations increase. The archive's faithfulness work complicates both readings: spontaneous self-corrections have measured precision of 24.4%, and much of the language that looks like self-critique falls after the answer is already fixed.

- **Kind**: method
- **Also called**: self-critique
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [adversarial robustness](../concepts/adversarial-robustness.md), [AIME24](../datasets/aime24.md), [beam search](beam-search.md), [best-of-n](best-of-n.md), [chain of thought](chain-of-thought.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [circuit analysis](circuit-analysis.md), [credit assignment](../concepts/credit-assignment.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [latent reasoning](../concepts/latent-reasoning.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [Llama-3.2-3B-Instruct](../models/llama-3-2-3b-instruct.md), [MATH-500](../datasets/math-500.md), [MATH500](../datasets/math500.md), [Monte Carlo tree search](monte-carlo-tree-search.md), [policy gradient](policy-gradient.md), [post-training](post-training.md), [process reward model](process-reward-model.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen2.5-14B-Instruct](../models/qwen2-5-14b-instruct.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-4B-Instruct-2507](../models/qwen3-4b-instruct-2507.md), [reasoning distillation](reasoning-distillation.md), [reinforcement learning with verifiable rewards](../concepts/reinforcement-learning-with-verifiable-rewards.md), [safety alignment](../concepts/safety-alignment.md), [self-consistency](self-consistency.md), [self-correction](../concepts/self-correction.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](test-time-scaling.md), [verification](../concepts/verification.md)

## Appears in

- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](../../archive/papers/2025/arxiv-2501-12948/summary.md) — Shows that reasoning ability can be incentivized in an LLM by pure reinforcement learning on verifiable tasks, with no human-annotated reasoning trajectories, and that the resulting reasoning patterns can be transferred to smaller models.
- [GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Time Latent Reasoning](../../archive/papers/2026/arxiv-2608-02585/summary.md) — Inserts optimizable latent states at an intermediate Transformer layer rather than at the output, so self-attention makes every continuation token's log-probability differentiable with respect to every latent and reward-weighted gradients reach them from the whole continuation instead of only through their own decoded token.
- [Self-Reflection Improves Safety of Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-678/summary.md) — Adds a Self-Reflection token that lets reasoning models recover from harmful output mid-generation, cutting harmful completion rate from 13.8% to 4.1%.
- [What If We Allocate Test-Time Compute Adaptively?](../../archive/papers/2026/local-80ef8b5ce7217f7c/summary.md) — Replaces uniform test-time compute allocation with a training-free agent that picks reasoning tools, a search strategy and an exploration parameter per problem, using a process reward model both to prune within a trajectory and to select across iterations.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
