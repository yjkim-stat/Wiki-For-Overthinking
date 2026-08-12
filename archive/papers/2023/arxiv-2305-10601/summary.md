<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Tree of Thoughts: Deliberate Problem Solving with Large Language Models

- **Authors**: Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan
- **Venue**: cs.CL
- **Published**: 2023-05-17
- **Source**: seed
- **Link**: <https://arxiv.org/abs/2305.10601>
- **PDF**: <https://arxiv.org/pdf/2305.10601v2>
- **Topics**: test-time-scaling
- **Relevance score**: reasoning-training 0.25, test-time-scaling 0.62

## In one line

Generalizes chain-of-thought into a search over a tree of intermediate 'thoughts', letting a model self-evaluate branches, look ahead and backtrack instead of committing to one left-to-right path.

## Problem

Inference is confined to token-level, left-to-right decision making, which fails on tasks needing exploration, strategic lookahead, or where an early decision is pivotal. A single chain has no mechanism for reconsidering a branch once taken.

## Contributions

- The Tree of Thoughts framework, in which coherent units of text serve as nodes and the model explores over them rather than over tokens.
- Self-evaluation of candidate thoughts as the search heuristic, so the model itself decides which branch to pursue.
- Lookahead and backtracking as available moves, making the decision global rather than greedy.
- Three tasks requiring non-trivial planning or search — Game of 24, Creative Writing, Mini Crosswords — on which the framework is evaluated.

## Method

Problem solving is cast as search over a tree whose nodes are 'thoughts', coherent intermediate text units. At each node the model generates candidate next thoughts and evaluates them itself, and a search procedure over those evaluations decides where to expand, with backtracking permitted. The abstract does not specify the search algorithm, branching factor or evaluation prompt format.

## Results

On Game of 24, GPT-4 with chain-of-thought prompting solves 4% of tasks while Tree of Thoughts reaches 74%. Results on Creative Writing and Mini Crosswords are reported as improvements but the abstract gives no figures for them. Summarized from the abstract alone, so the figures below are only those the abstract states; the paper's full evaluation is not represented here.

## Limitations

Not discussed in the abstract. The obvious cost, unpriced here, is compute: a tree search issues many model calls per problem, so the 4% to 74% comparison is not budget-matched against chain-of-thought. Later archived work makes this explicit by comparing decoding methods at fixed sample counts, where tree search does not dominate.

## Why it matters here

- **test-time-scaling**: The canonical structured-search entry in this topic, and the ancestor of every subsequent method that spends inference compute on exploration rather than on repeated sampling. Its Game of 24 result — 4% to 74% — is the most-cited demonstration that inference procedure alone can move a fixed model that far. It is most useful in this archive as a foil: the archived visualization study runs ToT against chain-of-thought, least-to-most and MCTS at a matched budget and finds ToT at 81.6% against CoT's 84.4% on AQuA, so the enormous gain on a search-shaped puzzle does not transfer to ordinary mathematical reasoning. Holding both results together is what this topic is for.

## Entities

- **Concepts**: deliberate decision making, search over thoughts, self-evaluation, lookahead, backtracking, chain of thought
- **Methods**: Tree of Thoughts, [chain-of-thought prompting](../../../../wiki/methods/chain-of-thought-prompting.md), self-evaluation, tree search
- **Datasets**: [Game of 24](../../../../wiki/datasets/game-of-24.md), Creative Writing, Mini Crosswords

Tags: `tree of thoughts`, `search`, `planning`, `test-time scaling`, `self-evaluation`

## Abstract

Language models are increasingly being deployed for general problem solving across a wide range of tasks, but are still confined to token-level, left-to-right decision-making processes during inference. This means they can fall short in tasks that require exploration, strategic lookahead, or where initial decisions play a pivotal role. To surmount these challenges, we introduce a new framework for language model inference, Tree of Thoughts (ToT), which generalizes over the popular Chain of Thought approach to prompting language models, and enables exploration over coherent units of text (thoughts) that serve as intermediate steps toward problem solving. ToT allows LMs to perform deliberate decision making by considering multiple different reasoning paths and self-evaluating choices to decide the next course of action, as well as looking ahead or backtracking when necessary to make global choices. Our experiments show that ToT significantly enhances language models' problem-solving abilities on three novel tasks requiring non-trivial planning or search: Game of 24, Creative Writing, and Mini Crosswords. For instance, in Game of 24, while GPT-4 with chain-of-thought prompting only solved 4% of tasks, our method achieved a success rate of 74%. Code repo with all prompts: https://github.com/princeton-nlp/tree-of-thought-llm.

---

Record id: `arxiv:2305.10601`
