<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# When Simple Problems Wear Complex Costumes: Improving Efficiency in LRM's Adaptive Reasoning

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/62755>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Trains an adaptive reasoning model in two stages -- SFT on simple problems presented in both concise and verbose phrasings, then GRPO with a custom reward -- so that its choice between explicit reasoning and a direct answer tracks actual task difficulty rather than how wordy the question is.

## Problem

Adaptive reasoning models that can switch between explicit reasoning and direct answering are meant to fix overthinking, where a large reasoning model spends multi-step reasoning on a simple task and pays unnecessary compute and latency for it. The paper identifies a failure in that fix: the switch is driven by superficial linguistic complexity, so a simple problem phrased verbosely is mistaken for a complex one and gets the expensive mode. The mode selector is reading surface form where it should be reading difficulty.

## Contributions

- Identifies a specific failure mode of adaptive reasoning models: they mistake verbosely phrased simple problems for complex ones, so the mode switch keys on superficial linguistic complexity rather than task difficulty.
- A data augmentation for SFT that pairs each simple problem with a redundant restatement of itself, teaching the model to disregard surface verbosity.
- A GRPO stage with a custom reward that refines the adaptive policy to select the reasoning mode by task complexity.
- Claims reduced computational overhead without sacrificing accuracy, and improved robustness against misleading linguistic cues.

## Method

Two stages. Stage one is supervised fine-tuning on augmented data in which the same simple problem appears in both a concise and a redundant, verbosely phrased form, so that the model learns the two phrasings warrant the same reasoning mode and that surface verbosity is not evidence of difficulty. Stage two applies Group Relative Policy Optimization with a custom reward function to refine the adaptive policy, so that mode selection is conditioned on actual task complexity rather than on surface linguistic cues. The available material does not state the backbone models, the reward function's terms, the source of the augmented data, or the evaluation setup.

## Results

_not recorded_

## Limitations

The available material is the ICML 2026 poster abstract only; no preprint or full text was reachable, so no benchmark, model, baseline or number can be attributed to this paper yet, and the central claims -- 'reduces computational overhead without sacrificing accuracy' and 'improved robustness' -- are unquantified here. A reader should also notice that the training signal for stage one is constructed by restating simple problems verbosely, so the demonstrated robustness may be specific to the augmentation's own style of verbosity rather than to naturally occurring wordy problems; and that the framing treats difficulty as a property the model can be taught to read, without the material stating how ground-truth difficulty was labelled.

## Why it matters here

- **overthinking**: Sharpens what the topic means by adaptive reasoning. Most of the literature asks whether a model can learn to stop early; this asks what signal the stopping decision is actually reading, and answers that it is partly reading prose length rather than problem difficulty -- a simple problem in a wordy costume gets the long reasoning mode. That is a concrete confound for every method in the archive that routes on estimated difficulty, and it suggests an evaluation the group does not currently have: hold the problem fixed, vary its phrasing, and see whether the reasoning budget moves. The proposed fix (SFT on concise/verbose pairs, then GRPO on a complexity-based reward) is a plausible remedy but, on the material available, an unquantified one -- the record carries the diagnosis with more confidence than the cure until the full paper can be read.

## Entities

- **Concepts**: [Overthinking](../../../../wiki/concepts/overthinking.md), [Adaptive Reasoning](../../../../wiki/concepts/adaptive-reasoning.md), Reasoning Mode Selection, Superficial Linguistic Complexity, Difficulty Estimation, Robustness to Surface Cues, [Reward Shaping](../../../../wiki/concepts/reward-shaping.md)
- **Methods**: two-stage SFT + RL training, [Group Relative Policy Optimization (GRPO)](../../../../wiki/methods/grpo.md), data augmentation by verbose restatement
- **Datasets**: _none recorded_

Tags: `overthinking`, `adaptive reasoning`, `grpo`, `efficient reasoning`, `difficulty estimation`, `robustness`, `large reasoning models`

---

Record id: `title:75760913d4d6cfa4`
