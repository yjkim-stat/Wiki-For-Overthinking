# TokenSkip

<!-- auto:begin -->

A token-level chain-of-thought compression method: it shortens a reasoning trace by dropping individual tokens, as against the step-, chunk- and chain-level pruning or rewriting approaches it sits beside in this archive's compression taxonomy. Its role in the sources is entirely as a baseline -- later efficient-reasoning methods report beating it jointly on accuracy and length -- and the archive still holds no standalone numbers for it, so nothing here says how much it compresses or at what accuracy cost on its own. What is confirmed is that it has an official public code release at github.com/hemingkx/TokenSkip, published alongside its EMNLP 2025 paper.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [A*-Thought](a-thought.md), [Ada-R1](ada-r1.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AdaptThink](adaptthink.md), [AIME 2024](../datasets/aime-2024.md), [AMC23](../datasets/amc23.md), [BBH (Big Bench Hard)](../datasets/bbh-big-bench-hard.md), [Chain-of-Draft](chain-of-draft.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DAST](dast.md), [DEER](deer.md), [DRP](drp.md), [Early Exit](early-exit.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [Laser](laser.md), [LC-R1](lc-r1.md), [Manifold Steering](manifold-steering.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [NOWAIT](nowait.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [PLAN-AND-BUDGET](plan-and-budget.md), [QwQ-32B](qwq-32b.md), [S-GRPO](s-grpo.md), [s1K-1.1](../datasets/s1k-1-1.md), [SEAL](seal.md), [SelfBudgeter](selfbudgeter.md), [SPIRIT](spirit.md), [SuperGPQA](../datasets/supergpqa.md), [Thinkless](thinkless.md), [Token Budget](../concepts/token-budget.md), [VeriThinker](verithinker.md)

## What we have settled

- **Established** — TokenSkip has an official public code release at github.com/hemingkx/TokenSkip, published alongside its EMNLP 2025 paper.
  - Checked the repository directly; it is the paper authors' own implementation of the token-level chain-of-thought compression method.

## Appears in

- [Segment-Level Attribution for Selective Learning of Long Reasoning Traces](../../archive/papers/2026/arxiv-2602-00425/summary.md) — Uses integrated-gradient token attribution, aggregated into per-segment strength and direction-consistency scores, to pick which segments of a long chain-of-thought an SFT run should compute loss on, masking the rest.
- [Don't Overthink It: A Survey of Efficient R1-style Large Reasoning Models](../../archive/papers/2025/local-6c80b6fd388d671e/summary.md) — A survey that organizes methods for making R1-style large reasoning models reason efficiently (i.e., avoid overthinking) into two axes: single-model optimization and multi-model collaboration.
- [Think Right: Learning to Mitigate Under-Over Thinking via Adaptive, Attentive Compression](../../archive/papers/2025/local-da3fbe3617acc5f8/summary.md) — TRAAC is an online GRPO-based RL method that prunes a reasoning model's chain-of-thought using attention scores from the </think> token and calibrates how aggressively it prunes based on estimated problem difficulty, so it thinks less on easy problems and more on hard ones.
- [A*-Thought: Efficient Reasoning via Bidirectional Compression for Low-Resource Settings](../../archive/papers/2025/title-6ac5c2757444abad/summary.md) — A*-Thought treats a long reasoning trace as a search tree over reasoning spans and uses A* search with a bidirectional importance score to select a short, high-information subset of it as supervised fine-tuning data for compressed reasoning.

## Checked against

- [https://github.com/hemingkx/TokenSkip](https://github.com/hemingkx/TokenSkip) — github.com · code · retrieved 2026-08-21
  - _a simple yet effective approach that enables LLMs to selectively skip redundant tokens during Chain-of-Thought generation and learn shortcuts between critical reasoning tokens, thereby allowing for controllable CoT compression with adjustable ratios._

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
