<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ConPress: Learning Efficient Reasoning from Multi-Question Contextual Pressure

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/61485>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

ConPress observes that a reasoning model shortens its traces when several independent questions share one prompt, and harvests those shortened traces as self-supervised fine-tuning data for the single-question setting.

## Problem

Large reasoning models spend many tokens on chain-of-thought for every question. Existing remedies need something extra: a stronger teacher model to distil from, hand-written pruning rules, or a reinforcement learning loop with a length reward. The paper asks whether the model already contains a shorter reasoning policy that can be elicited without any of those.

## Contributions

- Reports Self-Compression: a model given several independent questions in one prompt spontaneously shortens the reasoning trace for each, reproducibly across models and benchmarks
- Proposes ConPress, which harvests and filters those per-question traces and fine-tunes on them, requiring no teacher model, no manual pruning and no reinforcement learning
- Reports 30-60% token reduction with sub-point accuracy change on three backbones from 8k fine-tuning examples, against rejection-FT, DPO and RL baselines
- Shows that multi-question prompting cannot be used directly at inference - it costs 31.3 accuracy points on average - which is what motivates the fine-tuning transfer

## Method

The authors identify an inference-time effect they call Self-Compression: when several independent, individually answerable questions are placed in a single prompt, the model produces a shorter reasoning trace for each of them than it would for the same question asked alone. They attribute this to multi-question contextual pressure during generation and report it reproducibly across models and benchmarks. ConPress turns it into training data. It builds multi-question prompts to induce the compression, samples the model's outputs, parses the response back into per-question traces, and filters for traces that are both concise and reach the correct answer. Those trajectories are then used directly for supervised fine-tuning, so the compressed behaviour is internalised and appears when the model is later asked one question at a time. Nothing outside the model is involved: no teacher, no manual pruning rule, no RL.

## Results

With 8k fine-tuning examples: on Qwen3-4B-Thinking, MATH500 goes 95.6% to 96.0% with 48.7% fewer tokens, and AIME25 goes 72.5% to 70.1% with 33.6% fewer. On R1-Distill-Qwen-7B, MATH500 goes 91.6% to 92.4% with 45.0% fewer tokens, AIME25 37.9% to 37.5% with 18.3% fewer. On R1-Distill-Qwen-1.5B, MATH500 goes 81.2% to 80.8% with 51.2% fewer tokens. Token reduction across models and benchmarks lands in the 30-60% band with accuracy changes usually under one point. Baselines are shortest-trace rejection fine-tuning, shortest-trace DPO, and the RL methods ThinkPrune, LC-R1 and AdaptThink. The abstract's 59% MATH500 figure is the best case; the per-model table shows 45-51% on the three backbones listed. Note also that the two AIME25 rows both lose accuracy (-2.4 and -0.4) while compressing least, so the method compresses hardest exactly where the problems are easiest.

## Limitations

Stated or visible from the tables: compression is weaker and accuracy loss larger on the harder benchmark (AIME25) than on MATH500, so the savings are concentrated on problems that needed fewer tokens anyway; the compression signal is stronger for questions placed earlier in the multi-question prompt than later, so the harvested data is position-biased; using multi-question prompts directly at test time is not viable, costing 31.3 accuracy points on average, which is why the fine-tuning transfer is necessary; gains saturate beyond about 3 questions per prompt, with N=8 adding little over N=4; and the magnitude of self-compression varies by model, some being more stable under contextual pressure than others. A reader should add that the paper does not explain why contextual pressure shortens traces - the effect is reported and exploited, not accounted for - and that all evaluation is mathematics and STEM multiple choice.

## Why it matters here

- **overthinking**: Directly on topic, and the most interesting thing in it for the group is the mechanism rather than the method. Self-Compression is evidence that a shorter correct reasoning policy already exists inside the model and can be elicited by nothing more than prompt context - which lines up with the ellipsis finding in the AutoThink work and strengthens the reading that overthinking is a decoding habit rather than a capability limit. It also supplies an unusually cheap data recipe: 8k self-generated examples, no teacher, no RL, against RL baselines (ThinkPrune, LC-R1, AdaptThink) that need far more machinery. The caveat to carry is the difficulty asymmetry visible in the numbers: compression is largest on MATH500 and smallest on AIME25, where accuracy also drops - so the method mostly removes tokens from problems that were already cheap, which is the pattern to check before treating a headline token-reduction percentage as a claim about hard reasoning.

## Entities

- **Concepts**: [Overthinking](../../../../wiki/concepts/overthinking.md), Self-Compression, Contextual Pressure, Reasoning Trace Compression, Self-Distillation, [Accuracy-Efficiency Tradeoff](../../../../wiki/concepts/accuracy-efficiency-tradeoff.md), Difficulty-Dependent Compression
- **Methods**: ConPress, self-supervised supervised fine-tuning, Self-Compression (multi-question prompting), rejection-style trace filtering
- **Datasets**: MATH500, AIME25, [GSM8K](../../../../wiki/datasets/gsm8k.md), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md), [AMC](../../../../wiki/datasets/amc.md), [MMLU-STEM](../../../../wiki/datasets/mmlu-stem.md)

Tags: `overthinking`, `efficient-reasoning`, `self-compression`, `chain-of-thought`, `supervised-fine-tuning`, `token-efficiency`, `self-distillation`, `math-reasoning`

---

Record id: `title:11f96b3e58a44cf5`
