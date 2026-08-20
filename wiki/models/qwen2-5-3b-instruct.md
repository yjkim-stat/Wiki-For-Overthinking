# Qwen2.5-3B-Instruct

<!-- auto:begin -->

A small instruction-tuned checkpoint, and in both sources the scale at which a credit-assignment method is shown to still work rather than where it is developed. One reports its full seven-benchmark table at this size and wins the macro-average there as at 7B, with the per-benchmark picture differing between the two. The other pairs it with the 7B model of the same family so that a latent-credit result is stated across two scales rather than one. Neither studies the checkpoint; its presence marks the lower bound of the range these methods are claimed over.

- **Kind**: model
- **Also called**: Qwen2.5-3B
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [advantage estimation](../concepts/advantage-estimation.md), [Bamboogle](../datasets/bamboogle.md), [credit assignment](../concepts/credit-assignment.md), [dense retrieval](../methods/dense-retrieval.md), [E5-base-v2](e5-base-v2.md), [exploration](../concepts/exploration.md), [GiGPO](../methods/gigpo.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [HotpotQA](../datasets/hotpotqa.md), [latent reasoning](../concepts/latent-reasoning.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MMLU-STEM](../datasets/mmlu-stem.md), [multi-hop reasoning](../concepts/multi-hop-reasoning.md), [MuSiQue](../datasets/musique.md), [Natural Questions](../datasets/natural-questions.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [outcome reward](../concepts/outcome-reward.md), [PopQA](../datasets/popqa.md), [privileged information](../concepts/privileged-information.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen3-1.7B](qwen3-1-7b.md), [REINFORCE](../methods/reinforce.md), [search-augmented reasoning](../concepts/search-augmented-reasoning.md), [Search-R1](../methods/search-r1.md), [soft thinking](../methods/soft-thinking.md), [teacher-student gap](../concepts/teacher-student-gap.md), [TriviaQA](../datasets/triviaqa.md)

## Appears in

- [EviSD: Evidence-Conditioned Self-Distillation for Search-Augmented Agents](../../archive/papers/2026/arxiv-2608-01359/summary.md) — Re-scores a search agent's own sampled tokens under a teacher that has been shown the instance's supporting evidence, and uses the detached teacher-student gap to nudge the GRPO advantage up or down on search and answer tokens only, without adding a distillation loss or changing anything at inference.
- [Latent Thought Credit: Multi-Answer Credit Assignment for Latent Reasoning](../../archive/papers/2026/arxiv-2608-01593/summary.md) — Estimates what a continuous latent thought is worth by freezing the context after it and averaging the rewards of several answers sampled from that fixed context, then credits latent positions with the resulting thought-level advantage and answer positions with the ordinary group-relative one.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
