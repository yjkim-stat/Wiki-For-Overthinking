# Claude-3.7-Sonnet-Thinking

<!-- auto:begin -->

Claude-3.7-Sonnet-Thinking appears in these sources both as an evaluated model and as a mitigation target: RFMDataset finds it, like other top reasoning models, achieves under 20-60% accuracy on a curated mathematical-proof benchmark dominated by logical-violation and vague-argument failures; WHISPER separately shows its own black-box persuasive-prompting method cuts this model's average token usage 46% on MATH-500 while preserving (nominally improving) accuracy.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AMC23](../datasets/amc23.md), [Chain-of-Draft (baseline)](../methods/chain-of-draft-baseline.md), [CommonsenseQA](../datasets/commonsenseqa.md), [compression ratio](../concepts/compression-ratio.md), [DeepSeek-R1-0528](deepseek-r1-0528.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-14B](deepseek-r1-distill-qwen-14b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-o1](gpt-o1.md), [GSM8K](../datasets/gsm8k.md), [MATH500](../datasets/math500.md), [NoThinking (baseline)](../methods/nothinking-baseline.md), [Overthinking](../concepts/overthinking.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-235B-A22B](qwen3-235b-a22b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-4B](qwen3-4b.md), [Qwen3-8B](qwen3-8b.md)

## Appears in

- [Mathematical Proof as a Litmus Test: Revealing Failure Modes of Advanced Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-582/summary.md) — RFMDataset uses 200 manually-curated mathematical proof problems and a 10-category fine-grained error taxonomy (judged by LLM-as-a-judge, validated against human labels) to reveal that even top reasoning models (GPT-o1/o3, Claude-3.7-Sonnet-Thinking, Qwen3-235B, DeepSeek-R1) achieve under 20-60% proof accuracy, dominated by logical violation, hidden assumption, vague argument, and incomplete proof failures that self-reflection prompting only modestly improves.
- [Merlin’s Whisper: Enabling Efficient Reasoning in Large Language Models via Black-box Persuasive Prompting](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-917/summary.md) — WHISPER treats a large reasoning model purely as a black-box communicator and mitigates overthinking with no training or model access at all, using an iterative refinement loop over persuasive prompts (psychological, evidence-based, role-play, threat, instruction) that finds a single deployable prompt suffix cutting response length up to 3x on simple questions with preserved accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
