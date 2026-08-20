# long-horizon agency

<!-- auto:begin -->

Acting over many turns where the reward arrives only at the end, and where what makes it hard is different at each level of the stack. The three sources here occupy three of those levels. At the training-signal level, a single coding action packs several unrelated changes into one code version, so an outcome reward cannot say which change earned it -- and the fix, matching sub-parts of actions across rollouts, is worth 7.5 points while removing the trajectory-level advantage costs 20.9, so localised credit is a modifier on the terminal check rather than a replacement. At the serving level, agentic rollouts have the opposite profile from single-turn ones -- median input 37,757 tokens against 156, median output 148 against 47,583 -- and retain their key-value cache across tool-interleaved turns, which makes admitting a session a commitment of capacity rather than a placement decision. At the recovery level, a failure late in a long episode carries no diagnostic information unless something supplies it, which is why a matched recovery interface is worth 49 points where a generic playbook is worth 12. The reading is that long-horizon is not one problem: credit, capacity and diagnosis each break separately at length.

- **Kind**: concept
- **Also called**: long-horizon agents
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [advantage estimation](advantage-estimation.md), [ALFWorld](../datasets/alfworld.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [compute allocation](compute-allocation.md), [credit assignment](credit-assignment.md), [DeepSeek-V4-Flash](../models/deepseek-v4-flash.md), [GiGPO](../methods/gigpo.md), [GPT-5.5](../models/gpt-5-5.md), [group-relative advantage](group-relative-advantage.md), [GRPO](../methods/grpo.md), [HumanEval+](../datasets/humaneval.md), [in-context learning](in-context-learning.md), [Kimi-K2.6](../models/kimi-k2-6.md), [KV cache](kv-cache.md), [LiveCodeBench](../datasets/livecodebench.md), [MBPP+](../datasets/mbpp.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [outcome reward](outcome-reward.md), [prefix caching](../methods/prefix-caching.md), [Qwen2.5-Coder-7B](../models/qwen2-5-coder-7b.md), [Qwen3.5-27B](../models/qwen3-5-27b.md), [Qwen3.5-4B](../models/qwen3-5-4b.md), [Qwen3.6-27B](../models/qwen3-6-27b.md), [Qwen3.6-35B-A3B](../models/qwen3-6-35b-a3b.md), [Qwen3-8B](../models/qwen3-8b.md), [rejection sampling](../methods/rejection-sampling.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [selective prediction](selective-prediction.md), [self-correction](self-correction.md), [Skywork-OR1](../models/skywork-or1.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [tool orchestration](tool-orchestration.md), [verifiable reward](verifiable-reward.md), [zero-advantage group](zero-advantage-group.md)

## Appears in

- [DiDPO: Diff-in-Diff Policy Optimization for Coding Agent Training](../../archive/papers/2026/arxiv-2608-07147/summary.md) — Assigns credit in coding-agent RL by splitting each code diff into sub-diffs, matching semantically similar sub-diffs across rollouts to form advantage groups, and projecting the resulting diff-level advantage back onto the tokens that produced it.
- [Scheduling Mixed RL Rollouts Beyond Prefix Locality](../../archive/papers/2026/arxiv-2608-11152/summary.md) — A routing-layer admission policy for RL post-training that treats admitting a rollout session as a commitment of KV-cache capacity, allocates protected capacity per workload class by footprint and observed residency time, and leaves the workload mixture itself under the trainer's control.
- [Diagnosis Before Recovery: Turning Agent Failures into Selective Self-Correction](../../archive/papers/2026/arxiv-2608-11772/summary.md) — Profiles the dominant failure mode of an agent task family on development data, then freezes a policy that permits only the recovery interventions matched to that failure -- so a failure decides which repair is admissible and how much evidence to spend, rather than triggering more context indiscriminately.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
