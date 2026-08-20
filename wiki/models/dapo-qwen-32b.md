# DAPO-Qwen-32B

<!-- auto:begin -->

A 32B Qwen2.5 checkpoint trained with the DAPO recipe on roughly 17k mathematical problems, used in the archive as the worked example of a post-RLVR model. It carries the central measurement in the reasoning-boundary dispute: against its base Qwen2.5-32B it loses on plain Pass@K at large K and wins on CoT-Pass@K at every K up to 1024, the gap being widest on AIME 2025, which postdates the base model's training cutoff. It also appears in symbolic-perturbation testing of whether mathematical reasoning survives changed numbers.

- **Kind**: model
- **Also called**: DAPO-Qwen2.5-32B
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [AIME](../datasets/aime.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [backtracking](../concepts/backtracking.md), [benchmark contamination](../concepts/benchmark-contamination.md), [bootstrap resampling](../methods/bootstrap-resampling.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [DAPO](../methods/dapo.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DeepSeek-R1-0528-Qwen3-8B](deepseek-r1-0528-qwen3-8b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [entropy collapse](../concepts/entropy-collapse.md), [exploration](../concepts/exploration.md), [gpt-5.6-luna](gpt-5-6-luna.md), [gpt-oss-120b](gpt-oss-120b.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [judge reliability](../concepts/judge-reliability.md), [LiveCodeBench](../datasets/livecodebench.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [long chain-of-thought distillation](../methods/long-chain-of-thought-distillation.md), [MATH500](../datasets/math500.md), [memorization](../concepts/memorization.md), [Minerva](../datasets/minerva.md), [OlympiadBench](../datasets/olympiadbench.md), [pass@k](../concepts/pass-k.md), [policy entropy](../concepts/policy-entropy.md), [PRIME](../methods/prime.md), [process evaluation](../methods/process-evaluation.md), [Qwen2.5-32B](qwen2-5-32b.md), [Qwen2.5-Math-7B](qwen2-5-math-7b.md), [Qwen3-235B-A22B](qwen3-235b-a22b.md), [Qwen3-8B-Base](qwen3-8b-base.md), [reasoning boundary](../concepts/reasoning-boundary.md), [RLVR](../methods/rlvr.md), [Skywork-OR1](skywork-or1.md), [Skywork-OR1-Math-7B](skywork-or1-math-7b.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [training dynamics](../concepts/training-dynamics.md), [trajectory diversity](../concepts/trajectory-diversity.md), [verification](../concepts/verification.md), [vLLM](../methods/vllm.md)

## Appears in

- [BODHI: Do LLMs Branch Out and Discover Heterogeneous Inferences?](../../archive/papers/2026/arxiv-2608-02867/summary.md) — Builds prefix trees of semantically equivalent reasoning statements and measures how RLVR changes a model's preference between branches, finding the entropy collapse is not stylistic — the collapse is stronger for semantically distinct continuations than for syntactic variants of the same statement.
- [VAR-MATH: Probing True Mathematical Reasoning in LLMs via Symbolic Multi-Instance Benchmarks](../../archive/papers/2026/local-d62cc27b0209da49/summary.md) — Converts AMC23 and AIME24/25 into symbolic templates whose constants are replaced by sampled variables, requires a model to solve several instantiations of each problem, and finds RL-finetuned models lose most of their reported accuracy under that consistency requirement.
- [Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs](../../archive/papers/2025/local-fb100130d8c7c2bd/summary.md) — Shows that base models win pass@K on mathematics by producing wrong chains that land on right answers, and that scoring the chain too — CoT-Pass@K — reverses the verdict in RLVR's favour at every K.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
