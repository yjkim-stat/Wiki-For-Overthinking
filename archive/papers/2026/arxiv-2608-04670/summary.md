<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Easy to Complete, Hard to Choose: Investigating LLM Performance on the ProverbIT Benchmark

- **Authors**: Enrico Mensa, Lorenzo Zane, Calogero Jerik Scozzaro, Matteo Delsanto, Tommaso Milani, Daniele Paolo Radicioni
- **Venue**: Proceedings of the Eleventh Italian Conference on Computational Linguistics (CLiC-it 2025), pages 722-734
- **Published**: 2026-08-05
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.04670>
- **PDF**: <https://arxiv.org/pdf/2608.04670v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.70, test-time-scaling 0.25

## In one line

An Italian proverb benchmark on which models complete proverbs successfully but fail multiple-choice selection when no correct option is present, with CoT analysis showing they name the right ending while failing to notice its absence.

## Problem

It is unclear how LLMs process culturally embedded linguistic expressions, and whether benchmark success on such expressions reflects semantic understanding or recall of memorized patterns.

## Contributions

- ProverbIT, a 100-item Italian proverb benchmark with a no-correct-answer condition
- Evaluation of 13 frontier models including reasoning models across three task formats
- A CoT analysis showing models verbalize the correct ending yet fail to detect its absence, and are biased toward literal synonyms

## Method

ProverbIT is a 100-question Italian multiple-choice benchmark over three tasks: proverb completion, multiple-choice selection where a correct answer is present, and multiple-choice selection where none is. The third condition is the diagnostic: a model that understands the proverb should detect that no option is right. Thirteen frontier models are evaluated, including reasoning models and standard LLMs, and the chains of thought of two reasoning models are inspected in detail.

## Results

Nearly all models demonstrate knowledge of the proverbs through successful completion, but performance drops sharply on multiple-choice selection without a correct answer, including for state-of-the-art reasoning models. CoT analysis of two reasoning models finds a strong bias toward selecting literal synonyms, and finds that models frequently state the correct proverb ending during reasoning while still failing to identify that it is absent from the options.

## Limitations

100 questions in one language, so the estimate is noisy and specific to Italian cultural material. Detailed CoT analysis covers only two models. Absolute accuracies are not given in the abstract. Attribution of the failure to memorized patterns rather than understanding is an interpretation of the pattern, not a controlled test — a contamination check on the proverbs is not reported.

## Why it matters here

- **reasoning-training**: A clean dissociation between producing the right content and using it: the CoT contains the correct proverb ending and the answer still misses that no option matches. That places the failure after the reasoning, in the step from trace to decision, which is the same gap the archive's faithfulness thread tracks from the other direction. It is also a case where more reasoning training did not help, since state-of-the-art reasoning models degrade with the rest.

## Entities

- **Concepts**: [memorization](../../../../wiki/concepts/memorization.md), cultural knowledge, [figurative language](../../../../wiki/concepts/figurative-language.md), [abstention](../../../../wiki/concepts/abstention.md), [construct validity](../../../../wiki/concepts/construct-validity.md), [chain of thought faithfulness](../../../../wiki/concepts/chain-of-thought-faithfulness.md)
- **Methods**: [chain of thought](../../../../wiki/methods/chain-of-thought.md), [multiple-choice evaluation](../../../../wiki/methods/multiple-choice-evaluation.md), manual CoT inspection
- **Datasets**: ProverbIT

Tags: `benchmark`, `italian`, `memorization`, `chain of thought`, `abstention`

## Abstract

Large Language Models (LLMs) have transformed computational linguistics and achieved remarkable performance across numerous natural language processing tasks, yet significant gaps persist in understanding how these systems process culturally embedded linguistic expressions. This paper introduces ProverbIT, a novel Italian benchmark comprising 100 multiple-choice questions designed to evaluate LLMs' ability to complete Italian proverbs. We assess 13 frontier models, including Large Reasoning Models (LRMs) and traditional LLMs, across three tasks: proverb completion, multiple-choice selection with correct answers, and multiple-choice selection without correct answers. Our evaluation reveals surprising results: while nearly all models demonstrate knowledge of the proverbs through successful completion tasks, performance drops dramatically when transitioning to multiple-choice formats without correct answers, with even state-of-the-art reasoning models showing substantial degradation. Through detailed Chain-of-Thought analysis of two LRMs, we uncover that models exhibit a strong bias toward selecting literal synonyms and frequently mention correct proverb endings during reasoning without successfully identifying their absence from the given options. These findings suggest that current LLMs rely heavily on memorized patterns rather than deeper semantic understanding of culturally grounded expressions, highlighting important limitations in their reasoning capabilities for figurative language comprehension.

---

Record id: `arxiv:2608.04670`
