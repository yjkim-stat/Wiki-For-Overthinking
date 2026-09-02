# Qwen2.5-72B-Instruct

<!-- auto:begin -->

Qwen2.5-72B-Instruct is used as a backbone in a training-free generate-critique-revise self-reflection loop that stops when a critique emits a CONFIRMED sentinel or a depth cap is hit, and is evaluated in ReTraceQA (a 2,421-instance expert-annotated benchmark showing small language models reach a correct final answer via a flawed reasoning trace 14-24% of the time).

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [CommonsenseQA](../datasets/commonsenseqa.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Qwen-14B](deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](deepseek-r1-distill-qwen-32b.md), [deepseek-v4-flash](deepseek-v4-flash.md), [Gemini-2.0-Flash](gemini-2-0-flash.md), [GPT-4o](gpt-4o.md), [GPT-4o-mini](gpt-4o-mini.md), [GSM8K](../datasets/gsm8k.md), [GSM8K-Zero](../datasets/gsm8k-zero.md), [LLaMA-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [Llama-3.3-70B-Instruct](llama-3-3-70b-instruct.md), [MATH500](../datasets/math500.md), [o1-mini](o1-mini.md), [OpenBookQA](../datasets/openbookqa.md), [Overthinking](../concepts/overthinking.md), [Qwen3-32B](qwen3-32b.md), [self-doubt](../concepts/self-doubt.md), [Self-verification](../methods/self-verification.md), [StrategyQA](../datasets/strategyqa.md)

## Appears in

- [Training-Free Inference-Time Self-Reflection and Cost-Bounded Early Stopping for Large Language Models](../../archive/papers/2026/arxiv-2608-18884/summary.md) — A training-free generate-critique-revise loop over a frozen backbone that stops when the critique emits a CONFIRMED sentinel or a depth cap is hit, measured across nine experiments to show the sentinel halts 82-88% of items at about 2.1 generations, with accuracy flat on BBH and significantly higher on GSM8K and MATH.
- [ReTraceQA: Evaluating Reasoning Traces of Small Language Models in Commonsense Question Answering](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1798/summary.md) — ReTraceQA is a 2,421-instance expert-annotated benchmark showing that small language models (SLMs) reach the correct final answer via a flawed reasoning trace 14-24% of the time on commonsense QA, and that LLM-as-judge and PRM evaluators reliably detect overall trace correctness but struggle to localize the specific erroneous step, inflating answer-only accuracy scores by up to 25%.
- [Revisiting Overthinking in Long Chain-of-Thought from the Perspective of Self-Doubt](../../archive/papers/2025/local-ca12364e006462a5/summary.md) — The paper quantifies overthinking in long chain-of-thought reasoning through a new self-doubt lens (LLM-judged categories SD / OT-without-SD / NOT), finds self-doubt (redundant re-verification of an already-correct answer) is a major cause, and shows a simple input-validity-checking prompt reduces response length by 37.1% on average while improving accuracy by 3.6% across four RLLMs, and improves abstain behavior on missing-premise datasets.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
