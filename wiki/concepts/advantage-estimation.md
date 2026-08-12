# advantage estimation

<!-- auto:begin -->

Assigning each sampled rollout a learning signal relative to a baseline, which in the critic-free methods the sources use means comparing rollouts within a group. Both sources identify the same structural failure from opposite ends: when every rollout in a group receives the same reward the group-relative advantage is zero and the batch teaches nothing. One hits it on prompts where all rollouts are already correct, wasting the rollouts; the other on negative samples where no valid output exists, and forces a canonical 'None' rollout so the group regains variance. Together they show that group-relative methods depend on within-group disagreement, which makes example selection a requirement rather than an optimization.

- **Kind**: concept
- **Also called**: GRPO advantage, advantage estimate, group-relative advantage
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 5

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [abstention](abstention.md), [Bamboogle](../datasets/bamboogle.md), [credit assignment](credit-assignment.md), [data efficiency](data-efficiency.md), [exploration](exploration.md), [GiGPO](../methods/gigpo.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [hallucination](hallucination.md), [HotpotQA](../datasets/hotpotqa.md), [latent reasoning](latent-reasoning.md), [MATH](../datasets/math.md), [MATH-500](../datasets/math-500.md), [MMLU-STEM](../datasets/mmlu-stem.md), [multi-hop reasoning](multi-hop-reasoning.md), [MuSiQue](../datasets/musique.md), [Natural Questions](../datasets/natural-questions.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [outcome reward](outcome-reward.md), [PopQA](../datasets/popqa.md), [PPO](../methods/ppo.md), [privileged information](privileged-information.md), [process reward](process-reward.md), [prompt difficulty](prompt-difficulty.md), [REINFORCE](../methods/reinforce.md), [reinforcement learning post-training](../methods/reinforcement-learning-post-training.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [reward shaping](reward-shaping.md), [search-augmented reasoning](search-augmented-reasoning.md), [Search-R1](../methods/search-r1.md), [soft thinking](../methods/soft-thinking.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [TriviaQA](../datasets/triviaqa.md)

## Appears in

- [BiCAA: Bidirectional Credit Assignment for Search-Augmented Agent](../../archive/papers/2026/arxiv-2608-01321/summary.md) — Gives each retrieval step of a search agent a dense reward built from two ground-truth-conditioned signals — how much the step raised the model's likelihood of the correct answer, and how necessary the step looks in hindsight — and fuses them asymmetrically so that a step which helps locally but is redundant globally is discounted.
- [EviSD: Evidence-Conditioned Self-Distillation for Search-Augmented Agents](../../archive/papers/2026/arxiv-2608-01359/summary.md) — Re-scores a search agent's own sampled tokens under a teacher that has been shown the instance's supporting evidence, and uses the detached teacher-student gap to nudge the GRPO advantage up or down on search and answer tokens only, without adding a distillation loss or changing anything at inference.
- [Latent Thought Credit: Multi-Answer Credit Assignment for Latent Reasoning](../../archive/papers/2026/arxiv-2608-01593/summary.md) — Estimates what a continuous latent thought is worth by freezing the context after it and averaging the rewards of several answers sampled from that fixed context, then credits latent positions with the resulting thought-level advantage and answer positions with the ordinary group-relative one.
- [Teaching MLLMs to Say No: Generalized Referring Expression Comprehension via Refusal Calibrated GRPO](../../archive/papers/2026/arxiv-2608-04698/summary.md) — A GRPO variant that teaches multimodal models to refuse when a referred object is absent, without losing localization accuracy on cases where it is present.
- [Miner: Mining Intrinsic Mastery for Data-Efficient RL in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-237/summary.md) — Addresses wasted rollouts in critic-free RL on prompts where every sampled rollout is already correct and the advantage estimate is therefore zero.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
