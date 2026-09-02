# GSM8K-Zero

<!-- auto:begin -->

GSM8K-Zero is a variant of GSM8K built, per TALE, so the correct answer is embeddable directly from the question -- purpose-built to isolate over-reasoning/redundancy rather than test math ability. TALE shows Vanilla CoT accuracy on it (78.73%) falls below Direct Answering's (97.21%), its direct evidence that extra reasoning steps introduce errors when none are needed. The self-doubt paper evaluates on it alongside GSM8K and MATH-500 and finds it has the highest baseline overthinking rate of the three (92.3%, with a 35.5% self-doubt share), and that its input-validity-checking prompt raises accuracy on it by +16.7 and +14.7 points for DeepSeek-R1-Distill-Qwen-32B and DeepSeek-R1-Distill-Llama-70B respectively.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [GPT-4o](../models/gpt-4o.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [GSM8K](gsm8k.md), [LLaMA-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [MATH500](math500.md), [o3-mini](../models/o3-mini.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-72B-Instruct](../models/qwen2-5-72b-instruct.md), [Qwen3-32B](../models/qwen3-32b.md), [self-doubt](../concepts/self-doubt.md)

## Appears in

- [Token-Budget-Aware LLM Reasoning](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-1274/summary.md) — TALE (Token-Budget-Aware LLM rEasoning) identifies that reasoning LLMs will follow a token budget stated in the prompt but that the effective budget must be chosen carefully -- too small a budget triggers 'token elasticity' where the model gives up complying and produces even longer output than an unconstrained baseline -- and offers two implementations, zero-shot budget estimation-and-prompting (TALE-EP, 67% token reduction with <3% accuracy loss) and post-training internalization (TALE-PT, ~50% reduction via SFT or DPO), both found via a binary-search 'optimal budget' procedure motivated by an 'implicit monotonicity assumption' verified on 90.91% of sampled GSM8K problems.
- [Revisiting Overthinking in Long Chain-of-Thought from the Perspective of Self-Doubt](../../archive/papers/2025/local-ca12364e006462a5/summary.md) — The paper quantifies overthinking in long chain-of-thought reasoning through a new self-doubt lens (LLM-judged categories SD / OT-without-SD / NOT), finds self-doubt (redundant re-verification of an already-correct answer) is a major cause, and shows a simple input-validity-checking prompt reduces response length by 37.1% on average while improving accuracy by 3.6% across four RLLMs, and improves abstain behavior on missing-premise datasets.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
