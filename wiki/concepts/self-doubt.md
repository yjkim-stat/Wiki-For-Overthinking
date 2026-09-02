# self-doubt

<!-- auto:begin -->

The two sources here use 'self-doubt' for different things and should not be read as one phenomenon. In the paper that makes it a lens on overthinking, self-doubt is redundant re-verification of an answer the model has already got right: traces are judged into self-doubt, overthinking-without-self-doubt and non-overthinking categories, self-doubt is found to be a major cause of the overall length, and a prompt that first asks whether the question contains the information needed cuts response length 37.1% on average while improving accuracy 3.6% across four models. In the interruption study, self-doubt is instead one of three failure modes observed when reasoning is cut short or the context changes mid-trace — named there as accuracy degrading when the model tries to incorporate updated information — alongside reasoning leakage and panic. The first sense is an internal cause of excess length; the second is an externally induced instability, and only the first bears on why an uninterrupted model keeps going.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [GSM8K](../datasets/gsm8k.md), [GSM8K-Zero](../datasets/gsm8k-zero.md), [MATH500](../datasets/math500.md), [Overthinking](overthinking.md), [Qwen2.5-72B-Instruct](../models/qwen2-5-72b-instruct.md), [Qwen3-32B](../models/qwen3-32b.md), [Reasoning Completion Point (RCP)](reasoning-completion-point-rcp.md)

## Appears in

- [Revisiting Overthinking in Long Chain-of-Thought from the Perspective of Self-Doubt](../../archive/papers/2025/local-ca12364e006462a5/summary.md) — The paper quantifies overthinking in long chain-of-thought reasoning through a new self-doubt lens (LLM-judged categories SD / OT-without-SD / NOT), finds self-doubt (redundant re-verification of an already-correct answer) is a major cause, and shows a simple input-validity-checking prompt reduces response length by 37.1% on average while improving accuracy by 3.6% across four RLLMs, and improves abstain behavior on missing-premise datasets.
- [Are Large Reasoning Models Interruptible?](../../archive/papers/2026/title-f1e27aad3e870b08/summary.md) — Evaluates large reasoning models under budget-constrained interruptions and mid-reasoning context changes, finding accuracy drops of up to 60% and three recurring failure modes not visible under static evaluation.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
