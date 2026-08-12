# DAPO-Qwen-32B

<!-- auto:begin -->

A 32B Qwen2.5 checkpoint trained with the DAPO recipe on roughly 17k mathematical problems, used in the archive as the worked example of a post-RLVR model. It carries the central measurement in the reasoning-boundary dispute: against its base Qwen2.5-32B it loses on plain Pass@K at large K and wins on CoT-Pass@K at every K up to 1024, the gap being widest on AIME 2025, which postdates the base model's training cutoff. It also appears in symbolic-perturbation testing of whether mathematical reasoning survives changed numbers.

- **Kind**: model
- **Also called**: DAPO-Qwen2.5-32B
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC23](../datasets/amc23.md), [benchmark contamination](../concepts/benchmark-contamination.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [DAPO](../methods/dapo.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [judge reliability](../concepts/judge-reliability.md), [LiveCodeBench](../datasets/livecodebench.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH-500](../datasets/math-500.md), [MATH500](../datasets/math500.md), [memorization](../concepts/memorization.md), [Minerva](../datasets/minerva.md), [OlympiadBench](../datasets/olympiadbench.md), [pass-k](../methods/pass-k.md), [PRIME](../methods/prime.md), [process evaluation](../methods/process-evaluation.md), [Qwen2.5-32B](qwen2-5-32b.md), [Qwen2.5-Math-7B](qwen2-5-math-7b.md), [reasoning boundary](../concepts/reasoning-boundary.md), [RLVR](../methods/rlvr.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [training dynamics](../concepts/training-dynamics.md), [verification](../concepts/verification.md), [vLLM](../methods/vllm.md)

## Appears in

- [VAR-MATH: Probing True Mathematical Reasoning in LLMs via Symbolic Multi-Instance Benchmarks](../../archive/papers/2026/local-d62cc27b0209da49/summary.md) — Converts AMC23 and AIME24/25 into symbolic templates whose constants are replaced by sampled variables, requires a model to solve several instantiations of each problem, and finds RL-finetuned models lose most of their reported accuracy under that consistency requirement.
- [Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs](../../archive/papers/2025/local-fb100130d8c7c2bd/summary.md) — Shows that base models win pass@K on mathematics by producing wrong chains that land on right answers, and that scoring the chain too — CoT-Pass@K — reverses the verdict in RLVR's favour at every K.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
