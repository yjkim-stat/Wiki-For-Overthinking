# Kimi-k1.5

<!-- auto:begin -->

Kimi k1.5 is used in these sources as an evaluated LRM: SafeChain includes it among 13 large reasoning models evaluated for safety on StrongReject/WildJailbreak, finding unsafe responses are consistently longer than safe ones and that thought-length-controlling decoding (ZeroThink) improves safety without training; BloomEval's cited note does not name Kimi k1.5 specifically.

- **Kind**: model
- **Also called**: Kimi k1.5
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [Claude-3.7-Sonnet](claude-3-7-sonnet.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-V3](deepseek-v3.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [GPT-4o](gpt-4o.md), [Grok-3](grok-3.md), [GSM8K](../datasets/gsm8k.md), [HumanEval](../datasets/humaneval.md), [LiveCodeBench (v5)](../datasets/livecodebench-v5.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MBPP](../datasets/mbpp.md), [Omni-MATH](../datasets/omni-math.md), [OpenAI o1-mini](openai-o1-mini.md), [Qwen3-Max](qwen3-max.md), [QwQ](qwq.md), [s1-32B](s1-32b.md), [Sky-T1](sky-t1.md), [StrongReject](../datasets/strongreject.md), [WildJailbreak](../datasets/wildjailbreak.md), [XSTest](../datasets/xstest.md)

## Appears in

- [SafeChain: Safety of Language Models with Long Chain-of-Thought Reasoning Capabilities](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-1197/summary.md) — SafeChain systematically evaluates 13 large reasoning models' safety on StrongReject/WildJailbreak, finding no model is safe on both, that unsafe responses are consistently longer than safe ones, that safety improves within a model family as it scales but long-CoT fine-tuning itself does not inherently improve safety over the base instruction-tuned model, and that training-free decoding strategies controlling thought length (ZeroThink most effectively) improve safety without training -- motivating a new CoT-style safety training dataset that preserves reasoning performance while improving safety.
- [BloomEval: A Bloom’s Cognitive Taxonomy-Based Benchmark for Evaluating LRMs via Cognitive Hierarchy Trace](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1262/summary.md) — BloomEval maps each step of an LRM's reasoning trace onto Bloom's six-level cognitive taxonomy (Remember through Create) via a Cognitive Hierarchy Trace (CHT), defining structural anomalies -- hierarchy break (reasoning never reaches the required cognitive level), hierarchy jump (skipping intermediate levels), and overthinking (invoking cognitive operations exceeding what the task needs) -- and finds these anomalies are common even in *correct* answers (e.g. Grok-3 shows a 0.185 hierarchy-jump rate on correct answers), demonstrating that answer accuracy alone cannot detect incoherent or wasteful reasoning structure.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
