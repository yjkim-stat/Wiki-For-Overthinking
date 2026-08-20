<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# HardcoreLogic: Challenging Large Reasoning Models with Long-tail Logic Puzzle Games

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10011195>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

HardcoreLogic is a 5,000+ puzzle benchmark across 10 logic games that exposes how much LRM puzzle-solving relies on memorized canonical formats rather than genuine rule application.

## Problem

It is unclear whether large reasoning models genuinely apply logical rules to varying conditions or merely succeed on popular puzzle benchmarks (like standard Sudoku) by memorizing canonical formats and solution patterns, which existing corpora do not distinguish.

## Contributions

- HardcoreLogic, a benchmark of over 5,000 puzzles across 10 games designed to test LRM robustness on long-tail, non-canonical logic puzzle variants
- A systematic transformation methodology along three axes: Increased Complexity, Uncommon Elements, and Unsolvable Puzzles
- An error analysis of solvable and unsolvable puzzles showing gaps between genuine rule-following and memorized solution patterns

## Method

HardcoreLogic transforms canonical logic puzzles (e.g., 9x9 Sudoku and other games) along three dimensions - Increased Complexity, Uncommon Elements, and Unsolvable Puzzles - to reduce the chance that a model can succeed by shortcut memorization of familiar formats, then evaluates a diverse set of large reasoning models on the resulting 5,000+ puzzles across 10 games.

## Results

Evaluations across a diverse set of LRMs show significant performance drops on HardcoreLogic even for models that score highly on existing puzzle benchmarks; increased complexity is reported as the dominant source of difficulty, but models also struggle with subtle rule variations that do not necessarily raise puzzle difficulty.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Tangential: the paper matched only on the generic phrase 'large reasoning model.' It studies whether LRMs generalize logical rules to novel puzzle variants versus relying on memorization, which is a question about reasoning correctness/robustness, not about reasoning length, the accuracy/efficiency tradeoff, or when models should stop or keep computing at test time.

## Entities

- **Concepts**: logic puzzle benchmarking, long-tail generalization, rule generalization, memorization vs reasoning
- **Methods**: HardcoreLogic benchmark construction, puzzle transformation (IC/UE/UP axes)
- **Datasets**: HardcoreLogic (introduced)

Tags: `logic-puzzles`, `benchmark`, `generalization`, `tangential`

## Abstract

Abstract Large Reasoning Models (LRMs) have demonstrated impressive performance on complex tasks, including logical puzzle games that require deriving solutions satisfying all constraints. However, whether they can flexibly apply appropriate rules to varying conditions, particularly when faced with non-canonical game variants, remains an open question. Existing corpora focus on popular puzzles like 9x9 Sudoku, risking overfitting to canonical formats and memorization of solution patterns, which can mask deficiencies in understanding novel rules or adapting strategies to new variants. To address this, we introduce HardcoreLogic , a challenging benchmark of over 5,000 puzzles across 10 games, designed to test the robustness of LRMs on the "long-tail" of logical games. HardcoreLogic systematically transforms canonical puzzles through three dimensions: Increased Complexity (IC) , Uncommon Elements (UE) , and Unsolvable Puzzles (UP) , reducing reliance on shortcut memorization. Evaluations on a diverse set of LRMs reveal significant performance drops, even for models achieving top scores on existing benchmarks, indicating heavy reliance on memorized stereotypes. While increased complexity is the dominant source of difficulty, models also struggle with subtle rule variations that do not necessarily increase puzzle difficulty. Our systematic error analysis on solvable and unsolvable puzzles further highlights gaps in genuine reasoning. Overall, HardcoreLogic exposes the limitations of current LRMs and establishes a benchmark for advancing high-level logical reasoning.

---

Record id: `title:bfff1bebffbf9612`
