# process reward

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [adaptive compute allocation](adaptive-compute-allocation.md), [advantage estimation](advantage-estimation.md), [Bamboogle](../datasets/bamboogle.md), [credit assignment](credit-assignment.md), [early exit](../methods/early-exit.md), [GiGPO](../methods/gigpo.md), [GRPO](../methods/grpo.md), [HotpotQA](../datasets/hotpotqa.md), [KV cache compression](../methods/kv-cache-compression.md), [multi-hop reasoning](multi-hop-reasoning.md), [MuSiQue](../datasets/musique.md), [Natural Questions](../datasets/natural-questions.md), [outcome reward](outcome-reward.md), [overthinking](overthinking.md), [PopQA](../datasets/popqa.md), [PPO](../methods/ppo.md), [process reward model](../methods/process-reward-model.md), [reasoning redundancy](reasoning-redundancy.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [search-augmented reasoning](search-augmented-reasoning.md), [Search-R1](../methods/search-r1.md), [TriviaQA](../datasets/triviaqa.md)

## Appears in

- [BiCAA: Bidirectional Credit Assignment for Search-Augmented Agent](../../archive/papers/2026/arxiv-2608-01321/summary.md) — Gives each retrieval step of a search agent a dense reward built from two ground-truth-conditioned signals — how much the step raised the model's likelihood of the correct answer, and how necessary the step looks in hindsight — and fuses them asymmetrically so that a step which helps locally but is redundant globally is discounted.
- [Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning](../../archive/papers/2026/arxiv-2608-04771/summary.md) — Couples KV-cache compression and generation-length control under a single process-reward signal, compressing harder at high-reward reasoning steps and stopping early when confidence is high.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
