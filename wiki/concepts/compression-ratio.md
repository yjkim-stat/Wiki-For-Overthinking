# compression ratio

<!-- auto:begin -->

Compression ratio, in these sources, quantifies how much a reasoning trace or response has been shortened relative to a baseline: WHISPER reports up to 3x response-length reduction on simple questions via persuasive prompting, and SIGMA defines a per-response compression ratio C(o_i) (relative to the mean length of correct responses in a GRPO training group) that weights its self-imitation loss, oversampling prompts with higher demonstrated compressibility.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AdaptThink (baseline)](../methods/adaptthink-baseline.md), [AIME 2024](../datasets/aime-2024.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [Chain-of-Draft (baseline)](../methods/chain-of-draft-baseline.md), [Claude-3.7-Sonnet-Thinking](../models/claude-3-7-sonnet-thinking.md), [CommonsenseQA](../datasets/commonsenseqa.md), [DAPO (baseline)](../methods/dapo-baseline.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DPO (baseline)](../methods/dpo-baseline.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [LC-R1 (baseline)](../methods/lc-r1-baseline.md), [MATH500](../datasets/math500.md), [NoThinking (baseline)](../methods/nothinking-baseline.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](overthinking.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-8B](../models/qwen3-8b.md), [SFT (baseline)](../methods/sft-baseline.md)

## Appears in

- [Merlin’s Whisper: Enabling Efficient Reasoning in Large Language Models via Black-box Persuasive Prompting](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-917/summary.md) — WHISPER treats a large reasoning model purely as a black-box communicator and mitigates overthinking with no training or model access at all, using an iterative refinement loop over persuasive prompts (psychological, evidence-based, role-play, threat, instruction) that finds a single deployable prompt suffix cutting response length up to 3x on simple questions with preserved accuracy.
- [Exploration-Exploitation Reshaping towards Efficient Reasoning for Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1520/summary.md) — SIGMA reframes token-efficient RL as a classical exploration-exploitation problem: a self-imitation exploitation module prioritizes training on prompts/rollouts with high compression potential via a dynamic priority table and a compression-ratio-weighted self-imitation loss, while a self-guidance exploration module directs otherwise-undirected long-response exploration via prompt-based token-budget regeneration or random truncation -- improving average accuracy by 7.9%/2.9% while cutting average reasoning length 43.4%/40.3% on 1.5B/7B DeepSeek-R1-Distill models across six benchmarks, beating eight RL-based efficient-reasoning baselines.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
