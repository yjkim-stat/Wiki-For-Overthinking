# Qwen2.5-3B

<!-- auto:begin -->

A 3B Qwen2.5 model, used across 3 sources as the smaller of two scales in agentic reinforcement-learning studies -- recursive self-distillation, hindsight allocation and long-horizon search reflection all report it alongside a 7B version. Its role is to show a method's effect at two sizes on the same environments, which in this corpus generally means a smaller absolute score with the same ordering.

- **Kind**: model
- **Also called**: Qwen2.5-3B
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [advantage estimation](../concepts/advantage-estimation.md), [ALFWorld](../datasets/alfworld.md), [backtracking](../concepts/backtracking.md), [Bamboogle](../datasets/bamboogle.md), [belief state](../concepts/belief-state.md), [component ablation](../methods/component-ablation.md), [credit assignment](../concepts/credit-assignment.md), [error compounding](../concepts/error-compounding.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [hindsight](../concepts/hindsight.md), [HotpotQA](../datasets/hotpotqa.md), [knowledge distillation](../methods/knowledge-distillation.md), [long-horizon reasoning](../concepts/long-horizon-reasoning.md), [LoRA](../methods/lora.md), [MATH](../datasets/math.md), [multi-agent pipeline](../concepts/multi-agent-pipeline.md), [MuSiQue](../datasets/musique.md), [Natural Questions](../datasets/natural-questions.md), [on-policy distillation](../methods/on-policy-distillation.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [outcome reward](../concepts/outcome-reward.md), [privileged information](../concepts/privileged-information.md), [process reward](../concepts/process-reward.md), [process supervision](../concepts/process-supervision.md), [Qwen2.5-3B-Instruct](qwen2-5-3b-instruct.md), [Qwen2.5-7B](qwen2-5-7b.md), [Qwen3-1.7B](qwen3-1-7b.md), [Qwen3-32B](qwen3-32b.md), [rejection sampling](../methods/rejection-sampling.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [reward hacking](../concepts/reward-hacking.md), [RLVR](../methods/rlvr.md), [selectivity control](../methods/selectivity-control.md), [self-correction](../concepts/self-correction.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [teacher-student gap](../concepts/teacher-student-gap.md), [token-level distillation](../methods/token-level-distillation.md), [TriviaQA](../datasets/triviaqa.md), [WebShop](../datasets/webshop.md)

## Appears in

- [AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning](../../archive/papers/2026/arxiv-2608-05987/summary.md) — Turns token-level teacher-student log-probability gaps into turn-level credit for agentic RL by recursively updating a Bayesian belief in log-odds space, identifying pivotal turns without a critic.
- [Trajectory-Relative Hindsight Distillation for Agentic Reinforcement Learning](../../archive/papers/2026/arxiv-2608-07371/summary.md) — Distributes hindsight supervision across the turns of an agent trajectory by comparing each turn's share of total revision magnitude against its share of eligible tokens, holding the average multiplier at one so the total supervision is fixed and only its allocation changes -- and isolates that allocation with a permutation control that keeps the multiplier values and scrambles which turn receives which.
- [LoongReflect: Boosting Long-Horizon Reflection in Search Agents via Global Perspective Distillation](../../archive/papers/2026/arxiv-2608-11967/summary.md) — Gives a search agent an explicitly reversible trajectory tree with reflect and backtrack as first-class actions, and trains the reflection policy with a dense local signal distilled from a teacher that can see the whole trajectory alongside the sparse terminal reward the local decision is ultimately judged by.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
