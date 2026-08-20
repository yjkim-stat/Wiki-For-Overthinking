# GiGPO

<!-- auto:begin -->

A group-based policy optimization variant for agent training that compares actions taken from similar intermediate states across rollouts, rather than assigning one trajectory-level reward uniformly to every step. Both sources cite it as the strongest or near-strongest baseline they face and neither beats it everywhere: one reports 47.2 average F1 against its own 52.1 while losing Bamboogle to it by nearly ten points, and the other's single outright per-benchmark win is Bamboogle at 74.6 against its 68.9. Its position in these papers is as the credible alternative account of where localized credit should come from — rollout structure and state similarity, rather than an explicitly measured per-step signal.

- **Kind**: method
- **Also called**: Group-in-Group Policy Optimization
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [advantage estimation](../concepts/advantage-estimation.md), [Bamboogle](../datasets/bamboogle.md), [credit assignment](../concepts/credit-assignment.md), [dense retrieval](dense-retrieval.md), [E5-base-v2](../models/e5-base-v2.md), [GPT-5.5](../models/gpt-5-5.md), [GRPO](grpo.md), [HotpotQA](../datasets/hotpotqa.md), [multi-hop reasoning](../concepts/multi-hop-reasoning.md), [MuSiQue](../datasets/musique.md), [Natural Questions](../datasets/natural-questions.md), [on-policy self-distillation](on-policy-self-distillation.md), [outcome reward](../concepts/outcome-reward.md), [PopQA](../datasets/popqa.md), [PPO](ppo.md), [privileged information](../concepts/privileged-information.md), [process reward](../concepts/process-reward.md), [Qwen2.5-3B-Instruct](../models/qwen2-5-3b-instruct.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-8B](../models/qwen3-8b.md), [retrieval-augmented generation](retrieval-augmented-generation.md), [reward sparsity](../concepts/reward-sparsity.md), [search-augmented reasoning](../concepts/search-augmented-reasoning.md), [Search-R1](search-r1.md), [teacher-student gap](../concepts/teacher-student-gap.md), [TriviaQA](../datasets/triviaqa.md)

## Appears in

- [BiCAA: Bidirectional Credit Assignment for Search-Augmented Agent](../../archive/papers/2026/arxiv-2608-01321/summary.md) — Gives each retrieval step of a search agent a dense reward built from two ground-truth-conditioned signals — how much the step raised the model's likelihood of the correct answer, and how necessary the step looks in hindsight — and fuses them asymmetrically so that a step which helps locally but is redundant globally is discounted.
- [EviSD: Evidence-Conditioned Self-Distillation for Search-Augmented Agents](../../archive/papers/2026/arxiv-2608-01359/summary.md) — Re-scores a search agent's own sampled tokens under a teacher that has been shown the instance's supporting evidence, and uses the detached teacher-student gap to nudge the GRPO advantage up or down on search and answer tokens only, without adding a distillation loss or changing anything at inference.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
