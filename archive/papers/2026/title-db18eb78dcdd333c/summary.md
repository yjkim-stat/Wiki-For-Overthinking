<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Reasoning or Retrieval? A Study of Answer Attribution on Large Reasoning Models

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10010758>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Shows that large reasoning models' final answers are produced by two competing mechanisms, chain-of-thought reasoning and memory retrieval, and introduces FARL, a fine-tuning method that suppresses the retrieval shortcut to encourage genuine reasoning.

## Problem

Large reasoning models' final answers sometimes contradict their own reasoning traces; the paper investigates whether this comes from a retrieval mechanism competing with chain-of-thought reasoning, and whether reinforcement-learning fine-tuning inadvertently rewards this retrieval shortcut ('hacking' the reward signal) instead of genuine reasoning.

## Contributions

- A controlled experimental protocol (misleading reasoning cues and/or corrupted retrieval cues) that attributes LRM final answers to chain-of-thought reasoning versus memory retrieval
- Finding that the relative dominance of reasoning versus retrieval varies by problem domain, model scale, and fine-tuning approach (reinforcement learning versus distillation)
- FARL: a fine-tuning framework combining memory unlearning with reinforcement learning to suppress the retrieval shortcut and promote reasoning-dominant behavior

## Method

The authors run controlled experiments that challenge large reasoning models with misleading cues during reasoning and/or corrupted answers during retrieval, across models and datasets, to determine whether a final answer was produced by chain-of-thought reasoning or by a competing memory-retrieval mechanism, and how their relative dominance depends on problem domain, model scale, and fine-tuning approach. FARL then integrates memory unlearning with reinforcement learning to suppress the retrieval shortcut during fine-tuning, aiming to promote reasoning-dominant behavior.

## Results

_not recorded_

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Investigates the faithfulness of LRM reasoning traces (whether the chain-of-thought causally produces the answer versus a memory-retrieval shortcut) and reward hacking during RL fine-tuning; it does not address reasoning length, redundant or excessive thinking, or the stopping/compute-allocation tradeoff this topic tracks. Tangential: it matched only on the generic 'large reasoning model' keyword, not on any substantive treatment of overthinking or test-time compute scaling.

## Entities

- **Concepts**: answer attribution, reasoning vs retrieval shortcut, reward hacking in RL fine-tuning
- **Methods**: FARL, memory unlearning, reinforcement learning fine-tuning
- **Datasets**: _none recorded_

Tags: `answer-attribution`, `reward-hacking`, `chain-of-thought-faithfulness`, `reinforcement-learning`, `tangential`

## Abstract

Abstract Large reasoning models (LRMs) exhibit unprecedented capabilities in solving complex problems through Chain-of-Thought (CoT) reasoning. However, recent studies reveal that their final answers often contradict their own reasoning traces. We hypothesize that this inconsistency stems from two competing mechanisms for generating answers: CoT reasoning and memory retrieval. To test this hypothesis, we conduct controlled experiments that challenge LRMs with misleading cues during reasoning and/or corrupted answers during retrieval. Our results across models and datasets confirm that both mechanisms operate simultaneously, with their relative dominance influenced by multiple factors: problem domains, model scales, and fine-tuning approaches (e.g., reinforcement learning vs. distillation). The findings reveal a critical limitation in current reasoning fine-tuning paradigms: models can exploit the retrieval mechanism as a shortcut, effectively "hacking" the reward signal and undermining genuine reasoning development. To address this challenge, we introduce FARL, a novel fine-tuning framework that integrates memory unlearning with reinforcement learning. By carefully suppressing retrieval shortcuts during the fine-tuning process, FARL promotes reasoning-dominant behavior and enhances generalizable reasoning capabilities. The code is available at https://github.com/ZJUWYH/FARL.

---

Record id: `title:db18eb78dcdd333c`
