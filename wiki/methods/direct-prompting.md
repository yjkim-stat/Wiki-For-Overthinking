# Direct Prompting

<!-- auto:begin -->

Prompting an LLM to answer a question directly without any explicit reasoning steps, used across sources as the zero-extra-compute baseline against which chain-of-thought and other test-time-scaling prompting strategies are measured. Sources note it can sometimes outperform CoT on questions that do not actually require reasoning (an overthinking symptom), and it is the fastest-recovering strategy the EchoCoT security study exploits via ordinary API tool-calling.

- **Kind**: method
- **Also called**: direct answering, no-CoT prompting
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME](../datasets/aime.md), [chain-of-thought baseline](chain-of-thought-baseline.md), [deepseek-v4-flash](../models/deepseek-v4-flash.md), [GLM-5.2](../models/glm-5-2.md), [GPQA](../datasets/gpqa.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [GPT-5-Nano](../models/gpt-5-nano.md), [GSM-Hard](../datasets/gsm-hard.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [LLaMA-3-8B-Instruct](../models/llama-3-8b-instruct.md), [majority voting / self-consistency](majority-voting-self-consistency.md), [MATH500](../datasets/math500.md), [Multi-Agent Debate](multi-agent-debate.md), [o4-mini](../models/o4-mini.md), [OpenThoughts](../datasets/openthoughts.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3.5-Plus](../models/qwen3-5-plus.md), [self-refine](self-refine.md)

## Appears in

- [EchoCoT: Extracting Hidden Chain-of-Thought from Large Reasoning Models](../../archive/papers/2026/arxiv-2608-20055/summary.md) — A security study showing that the hidden chain-of-thought of a black-box reasoning model can be recovered near-verbatim through ordinary API tool-calling, because reasoning state must be retained across tool calls within a turn.
- [Rethinking the Role of Prompting Strategies in LLM Test-Time Scaling: A Perspective of Probability Theory](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-1356/summary.md) — Systematically compares 8 prompting strategies under equal sampling budget for majority-vote test-time scaling across 6 LLMs x 6 benchmarks, finding plain Chain-of-Thought eventually dominates every more elaborate strategy as sampling time N grows -- because CoT has more easy/fewer hard questions and a flatter wrong-answer distribution -- and shows combining per-question difficulty-adaptive scaling with per-question optimal-strategy selection lifts GSM8K accuracy from 86.0% to 97.4% (Majority@10) and MATH-500 from 15.2% to 61.0%.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
