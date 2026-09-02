# Claude-3.5-Sonnet

<!-- auto:begin -->

Claude 3.5 Sonnet appears as one of the target large reasoning/language models attacked in jailbreak red-teaming studies: Mousetrap's 'Chaos Machine' iterative reversible cipher-based prompt transformation, and SEAL's stacked-cipher adaptive jailbreak method.

- **Kind**: model
- **Also called**: Claude 3.5 Sonnet
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [adaptive compression](../concepts/adaptive-compression.md), [AdvBench](../datasets/advbench.md), [Claude-3.7-Sonnet](claude-3-7-sonnet.md), [Claude-Sonnet-4](claude-sonnet-4.md), [DeepSeek-R1](deepseek-r1.md), [Gemini-1.5-Pro](gemini-1-5-pro.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [GPT-4o](gpt-4o.md), [GPT-4o-mini](gpt-4o-mini.md), [Grok-3](grok-3.md), [HarmBench](../datasets/harmbench.md), [JailbreakBench](../datasets/jailbreakbench.md), [Llama-3.3-70B-Instruct](llama-3-3-70b-instruct.md), [MATH500](../datasets/math500.md), [o1](o1.md), [o1-mini](o1-mini.md), [o3-mini](o3-mini.md), [o4-mini](o4-mini.md), [QwQ-32B](qwq-32b.md), [StrongReject](../datasets/strongreject.md)

## Appears in

- [A Mousetrap: Fooling Large Reasoning Models for Jailbreak with Chain of Iterative Chaos](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-408/summary.md) — Mousetrap is the first jailbreak attack framework designed against large reasoning models: a 'Chaos Machine' iteratively applies reversible one-to-one prompt mappings (character/word/sentence-level ciphers) to embed a toxic query inside a multi-step reconstruction task, exploiting the finding that LRMs exhibit 'reasoning inertia' -- once started, they follow the reasoning chain to completion by inertia and neglect to re-evaluate safety -- achieving up to 96-98% attack success against o1-mini, Claude-3.5-Sonnet and Gemini-2.0-Thinking and 87.5-93.13% on standard safety benchmarks against Claude-Sonnet.
- [Three Minds, One Legend: Jailbreak Large Reasoning Model with Adaptive Stacked Ciphers](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-355/summary.md) — SEAL red-teams large reasoning models by stacking multiple lightweight ciphers (Caesar, ASCII, HEX, word/character reversal, etc.) to encrypt a harmful prompt just past the point an LRM's safety mechanism can flag it but still within its decryption/reasoning capability -- exploiting the same chain-of-thought reasoning that improves task performance as an attack surface -- with a reinforcement-learning-based adaptive cipher-selection strategy (a gradient-bandit policy over cipher groups, updated only on failures) reaching up to 100% attack success on some LRMs and beating seven baseline jailbreak methods, while showing attack success and the model's own ability to recover the original harmful intent from ciphertext both peak at a moderate 'sweet spot' cipher complexity and decline beyond it.
- [When Slower Isn’t Truer: Inverse Scaling Law of Truthfulness in Multimodal Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-63/summary.md) — TRUTHFULVQA, a 5,000-image hierarchical human-annotated benchmark testing multimodal LLM truthfulness under progressively misleading visual-linguistic prompts, uncovers an inverse scaling law of truthfulness: slow-thinking (reasoning) MLLMs are consistently less truthful than their fast-thinking chat counterparts of the same family, and larger reasoning models show worse calibration despite generating more reasoning tokens.
- [How Well do LLMs Compress Their Own Chain-of-Thought? A Token Complexity Approach](../../archive/papers/2025/local-d9f4b7637d373d00/summary.md) — Defines a per-question 'token complexity' - the minimum chain-of-thought length needed for a model to answer correctly - and uses it to show that 31 different CoT-compression prompts all sit on one universal accuracy-vs-length curve that is empirically predictable and provably far from the achievable optimum.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
