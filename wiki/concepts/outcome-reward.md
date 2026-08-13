# outcome reward

<!-- auto:begin -->

A single scalar awarded for the finished answer, and across these sources the baseline whose insufficiency each of them is arguing. Two treat it as an anchor that must be kept: one finds that removing the terminal reward while retaining dense per-step supervision is its largest single ablation loss (6.3 F1, degrading every benchmark), and the other bounds its privileged correction by the outcome advantage so that privileged information can never generate an update where the outcome reward is silent. The third names what it cannot express: treating one output stream as a sequence of episodes and scoring it by cumulative regret, it finds that current models' progress toward a correct answer is not monotone across the stream, and that a 0/1 terminal reward applies no pressure for it to be. The shared position is that outcome reward determines the direction of learning and cannot determine its distribution over a trajectory.

- **Kind**: concept
- **Also called**: outcome supervision, outcome-based reward, terminal reward
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [advantage estimation](advantage-estimation.md), [AIME24](../datasets/aime24.md), [Bamboogle](../datasets/bamboogle.md), [credit assignment](credit-assignment.md), [E5-base-v2](../models/e5-base-v2.md), [exploration-exploitation trade-off](exploration-exploitation-trade-off.md), [GiGPO](../methods/gigpo.md), [GRPO](../methods/grpo.md), [HotpotQA](../datasets/hotpotqa.md), [MATH](../datasets/math.md), [multi-hop reasoning](multi-hop-reasoning.md), [MuSiQue](../datasets/musique.md), [Natural Questions](../datasets/natural-questions.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [overthinking](overthinking.md), [PopQA](../datasets/popqa.md), [PPO](../methods/ppo.md), [privileged information](privileged-information.md), [process reward](process-reward.md), [process reward model](../methods/process-reward-model.md), [process supervision](process-supervision.md), [Qwen2.5-3B-Instruct](../models/qwen2-5-3b-instruct.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-8B](../models/qwen3-8b.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [reward hacking](reward-hacking.md), [reward sparsity](reward-sparsity.md), [RLVR](../methods/rlvr.md), [search-augmented reasoning](search-augmented-reasoning.md), [Search-R1](../methods/search-r1.md), [test-time compute](test-time-compute.md), [token efficiency](token-efficiency.md), [TriviaQA](../datasets/triviaqa.md)

## Appears in

- [BiCAA: Bidirectional Credit Assignment for Search-Augmented Agent](../../archive/papers/2026/arxiv-2608-01321/summary.md) — Gives each retrieval step of a search agent a dense reward built from two ground-truth-conditioned signals — how much the step raised the model's likelihood of the correct answer, and how necessary the step looks in hindsight — and fuses them asymmetrically so that a step which helps locally but is redundant globally is discounted.
- [EviSD: Evidence-Conditioned Self-Distillation for Search-Augmented Agents](../../archive/papers/2026/arxiv-2608-01359/summary.md) — Re-scores a search agent's own sampled tokens under a teacher that has been shown the instance's supporting evidence, and uses the detached teacher-student gap to nudge the GRPO advantage up or down on search and answer tokens only, without adding a distillation loss or changing anything at inference.
- [Optimizing Test-Time Compute via Meta Reinforcement Fine-Tuning](../../archive/papers/2025/local-c45962c819666804/summary.md) — Formalizes 'spend test-time compute well' as a meta-reinforcement-learning problem — treating one long output stream as a sequence of episodes and scoring it by cumulative regret over tokens — and trains against a dense progress bonus that outcome-only reward cannot express.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
