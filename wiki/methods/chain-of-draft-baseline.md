# Chain-of-Draft (baseline)

<!-- auto:begin -->

Chain-of-Draft (CoD), a prompting strategy that constrains reasoning to short, terse draft-like steps, is used in these sources as a prompt-based conciseness baseline: WHISPER and Budget Guidance both compare their own persuasive-prompting/steering methods against CoD among other training-free length-control baselines, generally finding it less robust or less effective under tight budgets than their proposed methods.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [Claude-3.7-Sonnet-Thinking](../models/claude-3-7-sonnet-thinking.md), [CommonsenseQA](../datasets/commonsenseqa.md), [compression ratio](../concepts/compression-ratio.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [Dynasor (baseline)](dynasor-baseline.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md), [NoThinking (baseline)](nothinking-baseline.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-8B](../models/qwen3-8b.md), [SEAL (baseline)](seal-baseline.md)

## Appears in

- [Merlin’s Whisper: Enabling Efficient Reasoning in Large Language Models via Black-box Persuasive Prompting](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-917/summary.md) — WHISPER treats a large reasoning model purely as a black-box communicator and mitigates overthinking with no training or model access at all, using an iterative refinement loop over persuasive prompts (psychological, evidence-based, role-play, threat, instruction) that finds a single deployable prompt suffix cutting response length up to 3x on simple questions with preserved accuracy.
- [Steering LLM Thinking with Budget Guidance](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1866/summary.md) — Budget guidance adapts diffusion-model classifier guidance to LLM reasoning: a lightweight BERT-based predictor estimates a Gamma distribution over each candidate next token's remaining-thinking-length (from the frozen target LLM's hidden states), and its CDF up to the budget is multiplied elementwise into the LLM's own token distribution -- steering generation smoothly toward a token budget without fine-tuning the LLM or hard-cutting it off, beating budget forcing by up to 26% accuracy on MATH-500 under tight budgets while using 37% fewer thinking tokens, and generalizing across model families, sizes, and out-of-domain tasks despite training only on math data.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
