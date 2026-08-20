<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Are Large Reasoning Models Good Translation Evaluators? Analysis and Performance Boost

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/117120>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

Analyzes large reasoning models as machine-translation evaluators, finds they overthink simple instances, and calibrates their thinking via synthetic human-like trajectories to cut thinking budget ~35x while improving correlation with human judgments.

## Problem

It is unclear whether large reasoning models' intermediate thinking process helps or hurts when they are used as automatic judges of machine translation quality; the paper finds LRMs overthink simpler cases and overestimate scores, which the field has not previously characterized.

## Contributions

- First systematic analysis of using large reasoning models as machine-translation quality judges
- Identifies that LRMs used as evaluators overthink simpler instances and have scoring-mechanism issues that lead to overestimation
- Proposes calibrating LRM thinking by training on synthetic, human-like thinking trajectories
- Shows the calibration reduces thinking budget by about 35x while improving evaluation correlation across model scales from 7B to 32B

## Method

The authors analyze LRMs acting as judges for machine translation quality, finding they require tailored evaluation materials, overthink simpler instances (spending excess reasoning tokens on easy cases), and have scoring mechanisms prone to overestimation. To address this they calibrate LRM thinking by training the models on synthetic, human-like thinking trajectories, aiming to align the amount and style of reasoning with what the evaluation task actually requires.

## Results

On WMT24 Metrics benchmarks, calibrated LRMs reduce thinking budget by approximately 35x while improving evaluation performance across model scales from 7B to 32B; R1-Distill-Qwen-7B achieves a +8.7 correlation point improvement.

## Limitations

The abstract does not specify which LRM base models beyond R1-Distill-Qwen-7B were tested, nor the exact composition or size of the synthetic human-like thinking trajectory training data; overestimation and scoring-mechanism issues are noted as problems but not fully quantified beyond the 7B example.

## Why it matters here

- **overthinking**: Directly relevant: it documents overthinking as a concrete failure mode of LRMs on simple evaluation instances and proposes a thinking-calibration method that cuts thinking budget by roughly 35x while improving performance (e.g. +8.7 correlation points for R1-Distill-Qwen-7B), a direct accuracy/efficiency tradeoff intervention, applied in the specific setting of MT quality evaluation.

## Entities

- **Concepts**: LRM-as-a-judge, overthinking on simple instances, thinking calibration, thinking budget
- **Methods**: LRM-as-a-judge, thinking calibration via synthetic trajectory training
- **Datasets**: WMT24 Metrics benchmark

Tags: `overthinking`, `thinking-budget`, `llm-as-judge`, `machine-translation`, `reasoning-length`, `calibration`

## Abstract

Abstract Recent advancements in large reasoning models (LRMs) have introduced an intermediate "thinking" process prior to generating final answers, improving their reasoning capabilities on complex downstream tasks. However, the potential of LRMs as evaluators for machine translation (MT) quality remains underexplored. We provides the first systematic analysis of LRM-as-a-judge in MT evaluation. We identify key challenges, revealing LRMs require tailored evaluation materials, tend to "overthink" simpler instances and have issues with scoring mechanisms leading to overestimation. To address these, we propose to calibrate LRM thinking by training them on synthetic, human-like thinking trajectories. Our experiments on WMT24 Metrics benchmarks demonstrate that this approach largely reduces thinking budgets by ~35x while concurrently improving evaluation performance across different LRM scales from 7B to 32B (e.g., R1-Distill-Qwen-7B achieves a +8.7 correlation point improvement). These findings highlight the potential of efficiently calibrated LRMs to advance fine-grained automatic MT evaluation.

---

Record id: `title:cca25579537de930`
