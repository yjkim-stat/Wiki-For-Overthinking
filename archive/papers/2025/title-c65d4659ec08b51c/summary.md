<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Beyond Greedy Exits: Improved Early Exit Decisions for Risk Control and Reliability

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/118222>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

UAT (Uncertain-Aware Thresholding) uses a Multi-Armed Bandit to adapt early-exit confidence thresholds online and unsupervised, replacing greedy static-threshold exits, with provable risk guarantees and 1.70-2.10x speedup at under 2% performance drop across vision-language, text-generation and classification tasks.

## Problem

Standard early-exit deep neural networks greedily exit at an intermediate layer once class-prediction confidence exceeds a predefined static threshold, but the model can be confidently wrong, and static thresholds are not robust to distribution shift encountered after deployment.

## Contributions

- UAT, replacing greedy static-threshold early exit with an online, unsupervised Multi-Armed-Bandit-adapted threshold
- a reward function jointly assessing predictive certainty and its reliability
- theoretical risk guarantees plus 1.70-2.10x speedup with <2% performance drop across three task types

## Method

Proposes UAT, which adapts the exit-decision threshold online and unsupervised using a Multi-Armed Bandit framework, driven by a new reward function that assesses both predictive certainty and its reliability, balancing computational efficiency against prediction quality while penalizing unnecessary late exits; provides theoretical guarantees on the risk UAT achieves.

## Results

Across vision-language understanding, text generation, and classification tasks, UAT delivers consistent speedups of 1.70-2.10x with a minimal performance drop of less than 2% compared to full-model performance.

## Limitations

Not stated in the fetched abstract beyond the reported speedup/accuracy tradeoff range.

## Why it matters here

- **overthinking**: A general adaptive-computation result outside the LLM-reasoning-trace setting: UAT's core idea -- stop as soon as a *reliability-checked* confidence threshold is met, rather than a static one -- is the same principle behind proposed fixes for overthinking (stop generating once the model is reliably confident), demonstrated here for classic early-exit DNNs including a text-generation task.

## Entities

- **Concepts**: adaptive early-exit thresholding, Multi-Armed Bandit exit-decision policy, risk-controlled inference
- **Methods**: Multi-Armed Bandit, early-exit deep neural networks, risk-controlled prediction
- **Datasets**: _none recorded_

Tags: `early-exit`, `adaptive-inference`, `risk-control`, `test-time-efficiency`

## Abstract

Abstract Early-Exit Deep Neural Networks enable adaptive inference by allowing prediction at intermediary layers, significantly reducing computational costs and latency. Most of the early exit strategies greedily exit a sample at an intermediary layer if the confidence in class prediction exceeds a predefined threshold that is set using a static validation set. This is problematic as the model might be overconfident in a wrong class. Also, they are not robust to distribution shifts encountered in deployment, which can undermine model trustworthiness and accuracy. To address these challenges, we propose UAT that adapts the threshold for exit decisions using a Multi-Armed Bandit framework, enabling online, unsupervised adjustment of exit decisions. UAT makes decisions based on a new reward function that assesses predictive certainty and its reliability to balance computational efficiency and prediction quality while penalizing unnecessary late exits. We provide guarantees on risk achieved by UAT and validate its performance on diverse tasks spanning vision-language understanding, text generation, and classification. Our framework demonstrates consistent improvements in speedup $(1.70-2.10\times)$ with a minimal performance drop $(<2)$\% as compared to full model performance.

---

Record id: `title:c65d4659ec08b51c`
