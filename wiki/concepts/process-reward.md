# process reward

<!-- auto:begin -->

A reward attached to an intermediate step rather than to the finished answer, and in these sources a signal used for two quite different purposes. One uses it to train: each retrieval step of a search agent is scored by how much it raised the likelihood of the correct answer and by how necessary it looks once the answer is known, and the resulting dense reward replaces a single trajectory-level scalar. The other uses it at inference to allocate resources: a lightweight per-step estimator drives how hard the KV cache is compressed at that step, how heavily reflection tokens are penalized, and when to stop early, reporting 37% to 65% fewer generated tokens and 2.08x to 2.35x lower latency. The sources therefore agree the useful property is that it varies along a trajectory, and disagree about what to spend that variation on.

- **Kind**: concept
- **Also called**: process supervision, process-level reward, step-level reward
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [adaptive compute allocation](adaptive-compute-allocation.md), [advantage estimation](advantage-estimation.md), [Bamboogle](../datasets/bamboogle.md), [credit assignment](credit-assignment.md), [E5-base-v2](../models/e5-base-v2.md), [early exit](../methods/early-exit.md), [Gemini-3.1-Pro](../models/gemini-3-1-pro.md), [GiGPO](../methods/gigpo.md), [GRPO](../methods/grpo.md), [HotpotQA](../datasets/hotpotqa.md), [KV cache compression](../methods/kv-cache-compression.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [multi-hop reasoning](multi-hop-reasoning.md), [MuSiQue](../datasets/musique.md), [Natural Questions](../datasets/natural-questions.md), [outcome reward](outcome-reward.md), [overthinking](overthinking.md), [PopQA](../datasets/popqa.md), [PPO](../methods/ppo.md), [process reward model](../methods/process-reward-model.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-8B](../models/qwen3-8b.md), [reasoning redundancy](reasoning-redundancy.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [reward hacking](reward-hacking.md), [reward sparsity](reward-sparsity.md), [RLVR](../methods/rlvr.md), [search-augmented reasoning](search-augmented-reasoning.md), [Search-R1](../methods/search-r1.md), [TriviaQA](../datasets/triviaqa.md)

## Appears in

- [BiCAA: Bidirectional Credit Assignment for Search-Augmented Agent](../../archive/papers/2026/arxiv-2608-01321/summary.md) — Gives each retrieval step of a search agent a dense reward built from two ground-truth-conditioned signals — how much the step raised the model's likelihood of the correct answer, and how necessary the step looks in hindsight — and fuses them asymmetrically so that a step which helps locally but is redundant globally is discounted.
- [Reinforcement Learning with Evolving Rubrics as Rewards for Audio Reasoning](../../archive/papers/2026/arxiv-2608-02831/summary.md) — Supervises audio reasoning with per-question rubrics generated from the raw waveform, and keeps the signal alive as the policy improves by regenerating the rubrics from the model's own rollouts each step and pruning any criterion that every rollout satisfies or none does.
- [Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning](../../archive/papers/2026/arxiv-2608-04771/summary.md) — Couples KV-cache compression and generation-length control under a single process-reward signal, compressing harder at high-reward reasoning steps and stopping early when confidence is high.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
