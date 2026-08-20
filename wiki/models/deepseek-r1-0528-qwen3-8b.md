# DeepSeek-R1-0528-Qwen3-8B

<!-- auto:begin -->

An 8B reasoning model distilled from DeepSeek-R1 onto a Qwen3 base, used in both sources as a mid-scale open reasoning checkpoint rather than as an object of study. One uses it as one of three backbones for a thought-level beam search, where it gains most on the hardest benchmark (HMMT-24, 55.8 to 65.6 against self-consistency at matched budget). The other includes it in the pass@K comparison that finds base models win by producing wrong chains landing on right answers, with chain-aware scoring reversing the verdict. Neither reports anything specific to the checkpoint itself.

- **Kind**: model
- **Also called**: DeepSeek-R1-0528-Qwen3-8B
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [AMC23](../datasets/amc23.md), [answer aggregation](../methods/answer-aggregation.md), [beam search](../methods/beam-search.md), [benchmark contamination](../concepts/benchmark-contamination.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [compute allocation](../concepts/compute-allocation.md), [DAPO](../methods/dapo.md), [DAPO-Qwen-32B](dapo-qwen-32b.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](../methods/grpo.md), [HMMT](../datasets/hmmt.md), [judge reliability](../concepts/judge-reliability.md), [KV cache](../concepts/kv-cache.md), [linear probe](../methods/linear-probe.md), [LiveCodeBench](../datasets/livecodebench.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [Monte Carlo tree search](../methods/monte-carlo-tree-search.md), [pass@k](../concepts/pass-k.md), [process evaluation](../methods/process-evaluation.md), [process reward model](../concepts/process-reward-model.md), [Qwen2.5-32B](qwen2-5-32b.md), [Qwen3-4B-Thinking-2507](qwen3-4b-thinking-2507.md), [Qwen3-8B](qwen3-8b.md), [reasoning boundary](../concepts/reasoning-boundary.md), [reasoning distillation](../methods/reasoning-distillation.md), [RLVR](../methods/rlvr.md), [self-consistency](../methods/self-consistency.md), [Skywork-OR1](skywork-or1.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time compute](../concepts/test-time-compute.md), [training dynamics](../concepts/training-dynamics.md), [trajectory diversity](../concepts/trajectory-diversity.md), [verification](../concepts/verification.md), [vLLM](../methods/vllm.md)

## Appears in

- [Thought-Level Beam Search for Reasoning](../../archive/papers/2026/arxiv-2608-08020/summary.md) — Reformulates test-time reasoning as compute allocation over partial trajectories under a hardware budget, and runs a zero-sum beam search over reasoning steps that prunes weak traces and immediately re-spends the freed capacity by branching from high-scoring prefixes.
- [Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs](../../archive/papers/2025/local-fb100130d8c7c2bd/summary.md) — Shows that base models win pass@K on mathematics by producing wrong chains that land on right answers, and that scoring the chain too — CoT-Pass@K — reverses the verdict in RLVR's favour at every K.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
