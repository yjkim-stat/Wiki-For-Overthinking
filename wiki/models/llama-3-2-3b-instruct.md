# LLaMA 3.2 3B Instruct

<!-- auto:begin -->

Llama-3.2-3B-Instruct is used in these sources as one of the evaluated LLMs in a preferences/opinions/beliefs benchmark (POBs), where models including it are found to lean progressive-collectivist with only limited reliability improvement from added reasoning or self-reflection prompting; a second source (ROSE) is unrelated to this specific model in its cited note.

- **Kind**: model
- **Also called**: Llama-3.2-3B-Instruct, Llama3.2-3B-Instruct
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [CoT-Valve (baseline)](../methods/cot-valve-baseline.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [difficulty estimation](../concepts/difficulty-estimation.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-4o](gpt-4o.md), [GSM8K](../datasets/gsm8k.md), [LLaMA-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [Llama-3.2-1B-Instruct](llama-3-2-1b-instruct.md), [Llama-3.3-70B-Instruct](llama-3-3-70b-instruct.md), [MATH (training)](../datasets/math-training.md), [MATH500](../datasets/math500.md), [MMLU-Pro](../datasets/mmlu-pro.md), [O1-Pruner (baseline)](../methods/o1-pruner-baseline.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-72B-Instruct](qwen2-5-72b-instruct.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen3-4B-Base](qwen3-4b-base.md), [Qwen3-8B-Base](qwen3-8b-base.md), [QwQ-32B](qwq-32b.md), [QwQ-32B-Preview](qwq-32b-preview.md), [TokenSkip (baseline)](../methods/tokenskip-baseline.md), [ZebraLogic](../datasets/zebralogic.md)

## Appears in

- [Think Again! The Effect of Test-Time Compute on Preferences, Opinions, and Beliefs of Large Language Models](../../archive/papers/2025/doi-10-18653-v1-2025-acl-industry-45/summary.md) — Introduces POBs, a 20-topic Likert-scale benchmark for LLM preferences/opinions/beliefs on controversial topics, finding models consistently lean progressive-collectivist (with newer versions more strongly and less consistently so), and that adding reasoning or self-reflection prompting gives only limited improvement to reliability, neutrality, or consistency.
- [Reinforced Efficient Reasoning via Semantically Diverse Exploration](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2216/summary.md) — ROSE improves MCTS-based RLVR by branching reasoning rollouts at semantic-entropy positions (generation entropy weighted by embedding-space token dispersion, not raw token-probability entropy, which conflates functionally-equivalent tokens like 'can'/'need' as diverse) plus an epsilon-exploration mechanism, combined with a length-aware segment-level advantage estimator that penalizes unnecessarily long correct branches, outperforming GRPO variants and MCTS baselines (TreePO, FR3E) on AIME/MATH500/AMC23 while producing measurably shorter, less overthought reasoning.
- [AutoL2S: Auto Long-Short Reasoning for Efficient Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-831/summary.md) — AutoL2S distills non-reasoning LLMs into models that jointly generate a lightweight <EASY> switching token and correspondingly select long or short chain-of-thought paths per instance, then refines this with GRPO-style RL on the induced long-short rollouts, cutting reasoning length by up to 71.7% with negligible accuracy loss across six benchmarks.
- [THOUGHTTERMINATOR: Benchmarking, Calibrating, and Mitigating Overthinking in Reasoning Models](../../archive/papers/2025/local-eff598a06b1089db/summary.md) — The paper defines model-relative measures of overthinking (local/global overthinking scores) built from observed token-spend distributions, introduces the DUMB500 easy-question dataset to probe overthinking on trivial inputs, and proposes THOUGHTTERMINATOR, a training-free decoding-time technique that interrupts a reasoning model with token-budget reminders and forces an answer at a difficulty-calibrated deadline.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
