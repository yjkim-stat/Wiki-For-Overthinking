<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# STaR: Bootstrapping Reasoning With Reasoning

- **Authors**: Eric Zelikman, Yuhuai Wu, Jesse Mu, Noah D. Goodman
- **Venue**: cs.LG
- **Published**: 2022-03-28
- **Source**: seed
- **Link**: <https://arxiv.org/abs/2203.14465>
- **PDF**: <https://arxiv.org/pdf/2203.14465v2>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.40, test-time-scaling 0.25

## In one line

Bootstraps a model's reasoning ability from a handful of rationale examples by generating rationales, keeping only those that reach the right answer, and finetuning on them in a loop.

## Problem

Chain-of-thought rationales improve performance, but eliciting them required either constructing a massive rationale dataset by hand or accepting the accuracy cost of few-shot inference. Neither scales.

## Contributions

- The STaR loop: prompt with a few rationale examples to generate rationales for many questions, finetune on those that produced correct answers, and repeat.
- Rationalization as the fix for the loop's dead end: when the generated answer is wrong, regenerate the rationale with the correct answer supplied as a hint, so hard problems still contribute training signal.
- Evidence that a model can improve itself from its own generated reasoning, without external rationale annotation.

## Method

A small set of rationale examples seeds few-shot generation of rationales across a large unlabelled-for-rationale dataset. Generated rationales whose final answers are correct are kept; for the incorrect ones the model is given the correct answer and asked to produce a rationale for it. The model is finetuned on all rationales that ultimately yielded correct answers, and the process repeats, each iteration starting from a stronger model.

## Results

The abstract reports that STaR significantly improves over a model finetuned to predict final answers directly, and performs comparably to finetuning a 30x larger state-of-the-art model on CommonsenseQA. No other figures are given. Summarized from the abstract alone, so the figures below are only those the abstract states; the paper's full evaluation is not represented here.

## Limitations

Not discussed in the abstract. A reader should note the structural risk the method carries: correctness of the final answer is the only filter, so a rationale that reaches the right answer by faulty reasoning is kept and trained on. Later work in this archive on unfaithful reasoning makes that failure mode concrete rather than hypothetical.

## Why it matters here

- **reasoning-training**: The origin of self-training for reasoning and the ancestor of the RLVR line that dominates this topic. The core move — filter self-generated traces by verifiable answer correctness and train on the survivors — is exactly the reward signal RLVR later formalizes, so reading this first makes clear that RLVR's novelty is the optimization, not the supervision. Rationalization is the piece most worth carrying forward: it is an early answer to the problem that outcome filtering discards all signal from problems the model cannot yet solve, which is the same gradient-starvation issue archived work addresses through sample weighting rather than through hints.

## Entities

- **Concepts**: [self-training](../../../../wiki/concepts/self-training.md), bootstrapping, rationale generation, rationalization, outcome-based filtering, chain of thought
- **Methods**: STaR, [few-shot prompting](../../../../wiki/methods/few-shot-prompting.md), [supervised finetuning](../../../../wiki/methods/supervised-fine-tuning.md), iterative self-improvement
- **Datasets**: [CommonsenseQA](../../../../wiki/datasets/commonsenseqa.md)

Tags: `self-training`, `star`, `rationales`, `bootstrapping`, `chain of thought`

## Abstract

Generating step-by-step "chain-of-thought" rationales improves language model performance on complex reasoning tasks like mathematics or commonsense question-answering. However, inducing language model rationale generation currently requires either constructing massive rationale datasets or sacrificing accuracy by using only few-shot inference. We propose a technique to iteratively leverage a small number of rationale examples and a large dataset without rationales, to bootstrap the ability to perform successively more complex reasoning. This technique, the "Self-Taught Reasoner" (STaR), relies on a simple loop: generate rationales to answer many questions, prompted with a few rationale examples; if the generated answers are wrong, try again to generate a rationale given the correct answer; fine-tune on all the rationales that ultimately yielded correct answers; repeat. We show that STaR significantly improves performance on multiple datasets compared to a model fine-tuned to directly predict final answers, and performs comparably to fine-tuning a 30$\times$ larger state-of-the-art language model on CommensenseQA. Thus, STaR lets a model improve itself by learning from its own generated reasoning.

---

Record id: `arxiv:2203.14465`
