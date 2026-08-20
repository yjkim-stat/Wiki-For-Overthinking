<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Thoughts Are All Over the Place: On the Underthinking of Long Reasoning Models

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/117581>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

Identifies 'underthinking' in long reasoning models, where frequent switching between reasoning thoughts prevents sufficient exploration and hurts accuracy, and proposes a decoding-time penalty to fix it.

## Problem

Long reasoning models sometimes fail not by reasoning too much but by reasoning too shallowly on each path, jumping between thoughts before exploring any of them fully, which reduces accuracy especially on hard math problems.

## Contributions

- Identifies and names 'underthinking': LRMs frequently switch between reasoning thoughts without sufficiently exploring promising paths
- Shows frequent thought switching correlates with incorrect responses on challenging math problems, across experiments on three test sets and two open-source LRMs
- Introduces a metric to quantify underthinking by measuring token efficiency in incorrect answers
- Proposes a decoding strategy, Thought Switching Penalty (TIP), that discourages premature transitions between thoughts
- Shows TIP improves accuracy on challenging datasets without requiring model fine-tuning

## Method

Analyzes reasoning traces from two open-source LRMs on three challenging test sets, tracking how often the model switches between distinct reasoning thoughts. Defines a token-efficiency metric over incorrect answers to quantify underthinking. Proposes Thought Switching Penalty (TIP), a decoding-time modification that penalizes premature switches away from a reasoning thought, applied without any fine-tuning.

## Results

Frequent thought switching is shown to correlate with incorrect responses across three challenging test sets and two open-source LRMs. TIP decoding improves accuracy across challenging datasets relative to standard decoding, without fine-tuning; specific accuracy numbers are not given in the abstract.

## Limitations

The abstract does not name the specific test sets or LRMs used, nor does it give numeric accuracy improvements from TIP; the analysis is focused on mathematical reasoning problems, so generality to other task types is not established in the abstract.

## Why it matters here

- **overthinking**: Directly addresses the underthinking side of the reasoning-length tradeoff: rather than models thinking too long, this paper shows they can think too shakily, switching thoughts prematurely, and proposes a decoding intervention (TIP) that makes reasoning depth per thought more sufficient without fine-tuning.

## Entities

- **Concepts**: [underthinking](../../../../wiki/concepts/underthinking.md), thought switching, token efficiency of incorrect answers
- **Methods**: Thought Switching Penalty (TIP) decoding strategy
- **Datasets**: three challenging math test sets (unnamed in abstract)

Tags: `underthinking`, `thought-switching`, `decoding-strategy`, `reasoning-depth`, `test-time`

## Abstract

Abstract Long reasoning models (LRMs) such as OpenAI's o1 and DeepSeek's R1 have demonstrated remarkable abilities in complex reasoning tasks by scaling test-time compute and exhibiting human-like deep thinking. However, we identify a phenomenon we term underthinking, where LRMs frequently switch between different reasoning thoughts without sufficiently exploring promising paths to reach a correct solution. This behavior leads to inadequate depth of reasoning and decreased performance, particularly on challenging mathematical problems. To systematically analyze this issue, we conduct experiments on three challenging test sets and two representative open-source LRMs, revealing that frequent thought switching correlates with incorrect responses. We introduce a novel metric to quantify underthinking by measuring token efficiency in incorrect answers. To address underthinking, we propose a decoding strategy with thought switching penalty (Tip) that discourages premature transitions between thoughts, encouraging deeper exploration of each reasoning path. Experimental results demonstrate that our approach improves accuracy across challenging datasets without requiring model fine-tuning. Our findings contribute to understanding reasoning inefficiencies in LRMs and offer a practical solution to enhance their problem-solving capabilities. Our code is open-source and available at https://github.com/wangyuenlp/underthinking.

---

Record id: `title:2e5e00164f8a905d`
