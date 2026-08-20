<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Distilled Pretraining: A modern lens of Data, In-Context Learning and Test-Time Scaling

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10009683>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Studies how distillation during LLM pretraining improves test-time scaling but impairs in-context learning (via induction heads), explained through a bigram-model sandbox.

## Problem

Distillation has returned to prominence in LLM pretraining, but its effect on capabilities central to modern LLMs — test-time scaling and in-context learning — was underexplored.

## Contributions

- Shows pretraining with distillation yields models that exhibit better test-time scaling
- Shows this benefit trades off against in-context learning ability, particularly the mechanism modeled via induction heads
- Uses a bigram-model sandbox to isolate the common factor behind the test-time-scaling / in-context-learning tradeoff
- Derives design-choice guidance for pretraining with distillation

## Method

Studies distillation during LLM pretraining (as used in Llama-3.2 and Gemma) and its effect on two downstream capabilities: test-time scaling and in-context learning. To explain the observed tradeoff, the authors build a simplified bigram-model sandbox that isolates the principal factor driving both effects.

## Results

No specific benchmark numbers are given in the available abstract; the paper reports qualitative findings (distillation improves test-time scaling, impairs in-context learning) plus a mechanistic explanation via the bigram sandbox.

## Limitations

Not stated in the abstract; the core analysis is carried out in a simplified bigram-model sandbox rather than on full-scale LLM pretraining runs.

## Why it matters here

- **overthinking**: Not substantively connected. 'Test-time scaling' here means how well a distilled-pretrained model's downstream performance improves with additional inference-time compute/examples in general, and the paper's focus is the tradeoff between that and in-context-learning ability (induction heads), studied in a bigram sandbox. It contains no treatment of reasoning-chain length, overthinking, or when a reasoning model should stop generating — the match is the shared generic phrase 'test-time scaling' only.

## Entities

- **Concepts**: [distillation](../../../../wiki/concepts/distillation.md), [test-time scaling](../../../../wiki/concepts/test-time-scaling.md), in-context learning, induction heads, bigram model sandbox
- **Methods**: distilled pretraining, bigram model analysis
- **Datasets**: _none recorded_

Tags: `distillation`, `pretraining`, `in-context-learning`, `test-time-scaling`, `induction-heads`

---

Record id: `title:5d210749910cf061`
