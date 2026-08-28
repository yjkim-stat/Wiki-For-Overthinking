# NoThinking (baseline)

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [AIME 2024](../datasets/aime-2024.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [Chain-of-Draft (baseline)](chain-of-draft-baseline.md), [Claude-3.7-Sonnet-Thinking](../models/claude-3-7-sonnet-thinking.md), [CommonsenseQA](../datasets/commonsenseqa.md), [compression ratio](../concepts/compression-ratio.md), [CoT-Valve (baseline)](cot-valve-baseline.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER (baseline)](deer-baseline.md), [Dynasor (baseline)](dynasor-baseline.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [Olympiad](../datasets/olympiad.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-8B](../models/qwen3-8b.md), [SEAL (baseline)](seal-baseline.md), [TokenSkip (baseline)](tokenskip-baseline.md)

## Appears in

- [Think How to Think: Mitigating Overthinking with Autonomous Difficulty Cognition in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1766/summary.md) — TH2T (Think-How-to-Think) is a two-stage fine-tuning method that first injects an explicit 'difficulty hypnosis' cue into a model's output prefix (prospective, global strategy selection) and then a 'redundancy hypnosis' cue into in-progress reasoning to truncate reflection loops (retrospective, local correction), cutting inference cost over 70% on easy tasks and 40% on hard tasks with minimal accuracy loss and no external difficulty labels at inference time.
- [Merlin’s Whisper: Enabling Efficient Reasoning in Large Language Models via Black-box Persuasive Prompting](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-917/summary.md) — WHISPER treats a large reasoning model purely as a black-box communicator and mitigates overthinking with no training or model access at all, using an iterative refinement loop over persuasive prompts (psychological, evidence-based, role-play, threat, instruction) that finds a single deployable prompt suffix cutting response length up to 3x on simple questions with preserved accuracy.
- [NEAT: Neuron-Based Early Exit for Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1231/summary.md) — NEAT identifies a sparse set of 'exit-associated neurons' whose FFN activation dynamics causally predict the </think> termination token, then monitors these neurons training-free during inference to trigger graded early exit or reflection suppression -- cutting average token generation 22-28% across four benchmarks and six models with accuracy comparable to vanilla decoding, and 21-23% real wall-clock latency reduction versus vanilla and CGRS (which is 41-63% slower than vanilla despite shortening output, due to its own scoring overhead).
- [Steering LLM Thinking with Budget Guidance](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1866/summary.md) — Budget guidance adapts diffusion-model classifier guidance to LLM reasoning: a lightweight BERT-based predictor estimates a Gamma distribution over each candidate next token's remaining-thinking-length (from the frozen target LLM's hidden states), and its CDF up to the budget is multiplied elementwise into the LLM's own token distribution -- steering generation smoothly toward a token budget without fine-tuning the LLM or hard-cutting it off, beating budget forcing by up to 26% accuracy on MATH-500 under tight budgets while using 37% fewer thinking tokens, and generalizing across model families, sizes, and out-of-domain tasks despite training only on math data.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
