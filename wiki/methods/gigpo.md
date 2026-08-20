# GiGPO

<!-- auto:begin -->

A group-relative variant that adds a state-level advantage by grouping actions taken from recurring states across episodes, on the observation that states recur in agentic rollouts and the trajectory-level advantage wastes that redundancy. Across 3 sources it is the strongest agentic-RL baseline the archive holds. Its limitation is identified by the method that beats it: grouping by identical environment states fails when functionally analogous edits modify different regions, which is why matching decomposed sub-parts across rollouts gains 4.2 to 4.9 average points over it -- with the advantage most pronounced (+10.4) where a solution spans several functions. Its training dynamics are also reported: it plateaus after about step 40 where the sub-diff method continues to climb.

- **Kind**: method
- **Also called**: Group-in-Group Policy Optimization
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [advantage estimation](../concepts/advantage-estimation.md), [Bamboogle](../datasets/bamboogle.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [credit assignment](../concepts/credit-assignment.md), [dense retrieval](dense-retrieval.md), [E5-base-v2](../models/e5-base-v2.md), [GPT-5.5](../models/gpt-5-5.md), [group-relative advantage](../concepts/group-relative-advantage.md), [GRPO](grpo.md), [HotpotQA](../datasets/hotpotqa.md), [HumanEval+](../datasets/humaneval.md), [Kimi-K2.6](../models/kimi-k2-6.md), [LiveCodeBench](../datasets/livecodebench.md), [long-horizon agency](../concepts/long-horizon-agency.md), [MBPP+](../datasets/mbpp.md), [multi-hop reasoning](../concepts/multi-hop-reasoning.md), [MuSiQue](../datasets/musique.md), [Natural Questions](../datasets/natural-questions.md), [on-policy self-distillation](on-policy-self-distillation.md), [outcome reward](../concepts/outcome-reward.md), [PopQA](../datasets/popqa.md), [PPO](ppo.md), [privileged information](../concepts/privileged-information.md), [process reward](../concepts/process-reward.md), [Qwen2.5-3B-Instruct](../models/qwen2-5-3b-instruct.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen2.5-Coder-7B](../models/qwen2-5-coder-7b.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3.5-4B](../models/qwen3-5-4b.md), [Qwen3.6-27B](../models/qwen3-6-27b.md), [Qwen3-8B](../models/qwen3-8b.md), [rejection sampling](rejection-sampling.md), [retrieval-augmented generation](retrieval-augmented-generation.md), [reward sparsity](../concepts/reward-sparsity.md), [search-augmented reasoning](../concepts/search-augmented-reasoning.md), [Search-R1](search-r1.md), [Skywork-OR1](../models/skywork-or1.md), [supervised fine-tuning](supervised-fine-tuning.md), [teacher-student gap](../concepts/teacher-student-gap.md), [TriviaQA](../datasets/triviaqa.md), [verifiable reward](../concepts/verifiable-reward.md), [zero-advantage group](../concepts/zero-advantage-group.md)

## Appears in

- [BiCAA: Bidirectional Credit Assignment for Search-Augmented Agent](../../archive/papers/2026/arxiv-2608-01321/summary.md) — Gives each retrieval step of a search agent a dense reward built from two ground-truth-conditioned signals — how much the step raised the model's likelihood of the correct answer, and how necessary the step looks in hindsight — and fuses them asymmetrically so that a step which helps locally but is redundant globally is discounted.
- [EviSD: Evidence-Conditioned Self-Distillation for Search-Augmented Agents](../../archive/papers/2026/arxiv-2608-01359/summary.md) — Re-scores a search agent's own sampled tokens under a teacher that has been shown the instance's supporting evidence, and uses the detached teacher-student gap to nudge the GRPO advantage up or down on search and answer tokens only, without adding a distillation loss or changing anything at inference.
- [DiDPO: Diff-in-Diff Policy Optimization for Coding Agent Training](../../archive/papers/2026/arxiv-2608-07147/summary.md) — Assigns credit in coding-agent RL by splitting each code diff into sub-diffs, matching semantically similar sub-diffs across rollouts to form advantage groups, and projecting the resulting diff-level advantage back onto the tokens that produced it.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
