# Qwen3-235B-A22B-Thinking-2507

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME](../datasets/aime.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [ARC-Challenge](../datasets/arc-challenge.md), [Claude Sonnet 4.5](claude-sonnet-4-5.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-R1-0528-Qwen3-8B](deepseek-r1-0528-qwen3-8b.md), [DeepSeek-R1-Distill-Qwen-14B](deepseek-r1-distill-qwen-14b.md), [DeepSeek-V3.2](deepseek-v3-2.md), [Gemini-2.5-Flash-Thinking](gemini-2-5-flash-thinking.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [Gemini-3-Pro](gemini-3-pro.md), [GLM-4.6](glm-4-6.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-5](gpt-5.md), [gpt-oss-120b](gpt-oss-120b.md), [GPT-OSS-20B](gpt-oss-20b.md), [GSM8K](../datasets/gsm8k.md), [HMMT 2025](../datasets/hmmt-2025.md), [Kimi-K2-Thinking](kimi-k2-thinking.md), [Overthinking](../concepts/overthinking.md), [Qwen3-30B-A3B-Thinking-2507](qwen3-30b-a3b-thinking-2507.md), [Qwen3-Max](qwen3-max.md)

## Appears in

- [PaCoRe: Learning to Scale Test-Time Compute with Parallel Coordinated Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1253/summary.md) — PaCoRe (Parallel Coordinated Reasoning) decouples test-time compute scaling from a fixed context window by running rounds of massively parallel reasoning trajectories, compacting each trajectory's conclusion into a short message, and RL-training the model to synthesize (not just vote on) these messages into better subsequent exploration -- letting an 8B model reach 94.5% on HMMT 2025 by scaling effective test-time compute to ~2 million tokens, surpassing GPT-5's 93.2%.
- [ReasonIF: Large Reasoning Models Fail to Follow Instructions During Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1456/summary.md) — ReasonIF is a 300-sample, six-instruction-type benchmark (multilinguality, word limit, disclaimer, JSON formatting, uppercase-only, remove-commas) showing large reasoning models comply with instructions far less inside their reasoning trace (average IFS 15.6%) than in their main response (57.3%), that reasoning instruction-following degrades further as problem difficulty rises (positive correlation up to 0.863 with accuracy), and that both multi-turn self-reflection and supervised fine-tuning on synthetic reasoning-instruction data (RIF) only partially close the gap, the latter trading a measurable accuracy drop for the IFS gain.
- [CoTJudger: A Graph-Driven Framework for Automatic Evaluation of Chain-of-Thought Efficiency and Redundancy in LRMs](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2077/summary.md) — CoTJudger converts free-form CoTs into directed dependency graphs (capturing backtracking, repetition, and self-correction via classified node/edge types) and extracts the Shortest Effective Path (SEP) -- the minimal, verified-sufficient reasoning skeleton -- to compute a scale-invariant Redundancy Ratio; across 21 LRMs it finds redundancy pervasive but structurally distinct by model family (DeepSeek-R1's high-in-degree 'Cyclic Complexity' looping vs. Qwen3-Max's high-uncertainty 'Semantic Verbosity' vs. Gemini-3-Pro's low-degree 'Local Over-Optimization'), that distilled models inherit and often amplify their teacher's redundancy (a 'reasoning illusion' where distillation transfers verbosity without the underlying verification capability), and that post-answer redundancy specifically includes 'Destructive Revision' where a correct answer is unstably discarded for a wrong one.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
