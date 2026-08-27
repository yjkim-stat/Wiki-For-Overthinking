# GPT-4o

<!-- auto:begin -->

A closed-source LLM used across sources both as an evaluated subject (e.g. in the POBs preference/opinion/belief benchmark, where test-time compute is found to only weakly and inconsistently improve neutrality/consistency) and as a data-generation or agent component in other papers' pipelines (generating temporal-reasoning training traces for TISER, acting as one of the specialized VLM agents in METAL's chart-generation framework, and serving as a reference model in TALE's token-budget experiments).

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [GPT-4o-mini](gpt-4o-mini.md), [GSM8K](../datasets/gsm8k.md), [LLaMA-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [Llama-3.3-70B-Instruct](llama-3-3-70b-instruct.md), [LoRA fine-tuning](../methods/lora-fine-tuning.md), [Mistral 7B](mistral-7b.md), [o3-mini](o3-mini.md), [Qwen2.5 7B](qwen2-5-7b.md)

## Appears in

- [Think Again! The Effect of Test-Time Compute on Preferences, Opinions, and Beliefs of Large Language Models](../../archive/papers/2025/doi-10-18653-v1-2025-acl-industry-45/summary.md) — Introduces POBs, a 20-topic Likert-scale benchmark for LLM preferences/opinions/beliefs on controversial topics, finding models consistently lean progressive-collectivist (with newer versions more strongly and less consistently so), and that adding reasoning or self-reflection prompting gives only limited improvement to reliability, neutrality, or consistency.
- [Learning to Reason Over Time: Timeline Self-Reflection for Improved Temporal Reasoning in Language Models](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-1358/summary.md) — TISER (Temporal Self-Reflective Prompting) extends chain-of-thought into a four-stage test-time-scaling pipeline -- reasoning, explicit timeline construction, iterative self-reflection, then answer generation -- for temporal reasoning, and fine-tuning smaller open models (Mistral-7B, Qwen2.5-7B) on TISER-formatted synthetic traces lets them match or beat GPT-4o on in-domain and out-of-distribution temporal reasoning benchmarks.
- [METAL: A Multi-Agent Framework for Chart Generation with Test-Time Scaling](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-1452/summary.md) — METAL decomposes chart-to-code generation into four specialized VLM agents (Generation, Visual Critique, Code Critique, Revision) that iteratively refine the code until a multi-criteria verifier passes, beating direct prompting, hint-enhanced prompting, and Best-of-N by 5.2-11.3 F1 points, with performance rising near-linearly in the log of test-time compute budget from 2^9 to 2^13 tokens.
- [Token-Budget-Aware LLM Reasoning](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-1274/summary.md) — TALE (Token-Budget-Aware LLM rEasoning) identifies that reasoning LLMs will follow a token budget stated in the prompt but that the effective budget must be chosen carefully -- too small a budget triggers 'token elasticity' where the model gives up complying and produces even longer output than an unconstrained baseline -- and offers two implementations, zero-shot budget estimation-and-prompting (TALE-EP, 67% token reduction with <3% accuracy loss) and post-training internalization (TALE-PT, ~50% reduction via SFT or DPO), both found via a binary-search 'optimal budget' procedure motivated by an 'implicit monotonicity assumption' verified on 90.91% of sampled GSM8K problems.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
