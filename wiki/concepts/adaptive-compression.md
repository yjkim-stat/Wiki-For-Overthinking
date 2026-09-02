# adaptive compression

<!-- auto:begin -->

The two sources carrying this term do not use it for the same thing, and the pairing is a vocabulary collision rather than a shared idea. One is about compressing a model's own chain of thought: it defines a per-question token complexity, the minimum reasoning length that model needs to answer correctly, and shows that 31 different compression prompts trace a single accuracy-versus-length curve per model and benchmark rather than one curve per prompt family, with the achieved compression far short of the computable bound. The other uses adaptive compression as a step inside automatic prompt optimization, distilling a prompt that has stopped improving in order to escape a local optimum, and reports reaching better task performance on a quarter of the prompt-generation budget of prior methods. Only the first is about reasoning length; a reader arriving from the overthinking literature wants that one.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Claude-3.5-Sonnet](../models/claude-3-5-sonnet.md), [GPT-4o](../models/gpt-4o.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [Llama-3.3-70B-Instruct](../models/llama-3-3-70b-instruct.md), [MATH500](../datasets/math500.md)

## Appears in

- [How Well do LLMs Compress Their Own Chain-of-Thought? A Token Complexity Approach](../../archive/papers/2025/local-d9f4b7637d373d00/summary.md) — Defines a per-question 'token complexity' - the minimum chain-of-thought length needed for a model to answer correctly - and uses it to show that 31 different CoT-compression prompts all sit on one universal accuracy-vs-length curve that is empirically predictable and provably far from the achievable optimum.
- [No Loss, No Gain: Gated Refinement and Adaptive Compression for Prompt Optimization](../../archive/papers/2025/title-46b721af432d8a4e/summary.md) — GRACE improves automatic prompt optimization by combining a gated-refinement mechanism (to stabilize update signals) with adaptive compression (distilling a stagnating prompt to escape local optima), reaching better task performance using only 25% of the prompt-generation budget of prior methods.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
