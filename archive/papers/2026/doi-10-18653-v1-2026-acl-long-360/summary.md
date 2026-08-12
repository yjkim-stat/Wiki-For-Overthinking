<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ChessArena: A Chess Testbed for Evaluating Strategic Reasoning Capabilities of Large Language Models

- **Authors**: Jincheng Liu, Sijun He, Jingjing Wu, Xiangsen Wang, Yang Chen, Zhaoqi Kuang, Siqi Bao, Yuan Yao
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.360>
- **DOI**: 10.18653/V1/2026.ACL-LONG.360
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.67

## In one line

A competitive chess testbed where 13 models play each other, and no model beats a human-amateur-level engine while some lose to random play.

## Problem

Whether models possess genuine strategic reasoning or primarily excel at pattern recognition is unresolved. Chess is proposed as the instrument because it demands strategic reasoning, precise rule adherence and tracking of complex game state simultaneously — and it has an absolute external reference in engine strength.

## Contributions

- ChessArena, a competitive chess testbed with four play modes covering understanding, move selection and puzzle solving
- Evaluation of 13 LLMs over 800+ games against each other and against calibrated engines
- The result that no model beats Maia-1100 and some lose to random play
- A fine-tuned Qwen3-8B baseline approaching much larger reasoning models

## Method

ChessArena is a competitive framework in which models play against each other under four play modes, testing basic understanding, move selection and puzzle solving. Play against a calibrated engine gives an absolute scale rather than a relative ranking. A fine-tuned baseline is also trained.

## Results

Across 13 LLMs and over 800 games: no model beats Maia-1100, which is human amateur level, and some lose to random play. A fine-tuned Qwen3-8B substantially improves performance, approaching much larger state-of-the-art reasoning models.

## Limitations

Over 800 games across 13 models and four modes is few games per condition, and chess outcomes are high-variance, so per-model rankings are noisy. Models are not listed. Losing to random play may partly reflect illegal-move handling and state-tracking failures rather than strategic weakness, and the abstract does not separate rule adherence from strategy. Chess is heavily represented in pretraining data, so puzzle performance is contamination-exposed in a way game play is not.

## Why it matters here

- **reasoning-training**: Its value for this topic is having an absolute yardstick, which almost nothing else in the archive does. Math benchmarks measure models against each other and against a ceiling of 100%, so a field-wide plateau is invisible; here a fixed engine at human-amateur strength beats every model tested, which converts a relative ranking into an absolute statement about capability. That a fine-tuned 8B model then approaches far larger reasoning models also suggests the gap is not primarily scale, and belongs beside the drain's other data-efficiency results. Contamination on puzzles is the caveat that keeps this from being a clean measurement.

## Entities

- **Concepts**: strategic reasoning, [pattern recognition versus reasoning](../../../../wiki/concepts/pattern-recognition-versus-reasoning.md), [state tracking](../../../../wiki/concepts/state-tracking.md), [construct validity](../../../../wiki/concepts/construct-validity.md), absolute reference scale, [long-horizon reasoning](../../../../wiki/concepts/long-horizon-reasoning.md)
- **Methods**: ChessArena, competitive self-play evaluation, [supervised fine-tuning](../../../../wiki/methods/supervised-fine-tuning.md)
- **Datasets**: ChessArena

Tags: `chess`, `strategic reasoning`, `benchmark`, `absolute baseline`, `state tracking`

## Abstract

Recent large language models (LLMs) have shown strong reasoning capabilities. However, a critical question remains: do these models possess genuine strategic reasoning, or do they primarily excel at pattern recognition? To address this, we present ChessArena, a chess-based testbed for evaluating LLMs. Chess demands strategic reasoning, precise rule adherence, and the ability to track complex game states. ChessArena is a competitive framework where LLMs play against each other under four play modes. We evaluate 13 LLMs across over 800 games, testing basic understanding, move selection, and puzzle solving. Results reveal significant shortcomings: no model beats Maia-1100 (human amateur level), and some lose to random play. We also present a strong baseline: our fine-tuned Qwen3-8B substantially improves performance, approaching much larger state-of-the-art reasoning models.

---

Record id: `doi:10.18653/v1/2026.acl-long.360`
