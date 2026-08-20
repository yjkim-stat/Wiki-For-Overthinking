# Qwen3.5-4B

<!-- auto:begin -->

A 4B general-purpose model used as a training backbone in two archived studies. In the coding-agent work it is the stronger of two backbones, reaching 58.6 average on standard code benchmarks after diff-level credit assignment against 53.7 for the strongest baseline, and 22.1 on competition benchmarks -- where the gains land on introductory and interview tiers while the hardest tiers stay near zero for every method. In the financial reasoning benchmark it is among the evaluated systems. Neither source describes the model. Its use here is as evidence that the credit-assignment result holds at two scales rather than one.

- **Kind**: model
- **Also called**: Qwen3.5-4B
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [adversarial robustness](../concepts/adversarial-robustness.md), [benchmark design](../concepts/benchmark-design.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [credit assignment](../concepts/credit-assignment.md), [DeepSeek-V4-Flash](deepseek-v4-flash.md), [FinQA](../datasets/finqa.md), [GiGPO](../methods/gigpo.md), [GPT-5.5](gpt-5-5.md), [gpt-oss-120b](gpt-oss-120b.md), [group-relative advantage](../concepts/group-relative-advantage.md), [GRPO](../methods/grpo.md), [HumanEval+](../datasets/humaneval.md), [Kimi-K2.6](kimi-k2-6.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.3-70B](llama-3-3-70b.md), [long-horizon agency](../concepts/long-horizon-agency.md), [LoRA](../methods/lora.md), [MBPP+](../datasets/mbpp.md), [outcome reward](../concepts/outcome-reward.md), [Qwen2.5-Coder-7B](qwen2-5-coder-7b.md), [Qwen3.5-9B](qwen3-5-9b.md), [Qwen3.6-27B](qwen3-6-27b.md), [reasoning depth](../concepts/reasoning-depth.md), [rejection sampling](../methods/rejection-sampling.md), [Skywork-OR1](skywork-or1.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [verifiable reward](../concepts/verifiable-reward.md), [zero-advantage group](../concepts/zero-advantage-group.md)

## Appears in

- [DiDPO: Diff-in-Diff Policy Optimization for Coding Agent Training](../../archive/papers/2026/arxiv-2608-07147/summary.md) — Assigns credit in coding-agent RL by splitting each code diff into sub-diffs, matching semantically similar sub-diffs across rollouts to form advantage groups, and projecting the resulting diff-level advantage back onto the tokens that produced it.
- [V-FiLLM: Verified Financial LLM Reasoning Benchmark](../../archive/papers/2026/arxiv-2608-11047/summary.md) — Generates financial reasoning benchmarks from executable computation trees over real tables so that answers are correct by construction with no model in the labelling loop, exposes four independently controllable difficulty axes, and finds that unit and scale perturbations collapse the strongest model from 98.4 percent to 3.0.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
