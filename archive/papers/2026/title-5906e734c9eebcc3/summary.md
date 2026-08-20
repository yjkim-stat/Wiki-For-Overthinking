<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Real-Time Monitoring and Calibration of Chain-of-Thought Sycophancy in Large Reasoning Models

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/61298>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

A step-level monitoring and calibration framework that detects and suppresses sycophantic drift as a large reasoning model generates its chain of thought.

## Problem

Large reasoning models tend to agree with users' incorrect beliefs (sycophancy) rather than reasoning independently, and existing mitigation methods only judge and correct final answers without addressing how sycophancy develops during the reasoning process itself.

## Contributions

- Proposes MONICA, a framework that monitors sycophantic drift during chain-of-thought generation at the level of individual reasoning steps rather than only judging the final answer
- Introduces a calibrator that intervenes during generation to suppress sycophantic behavior once a monitored drift score exceeds a threshold
- Evaluates the framework across 12 datasets and 3 large reasoning models, reducing sycophancy in both intermediate reasoning steps and final answers

## Method

MONICA combines two components applied during inference: a sycophantic monitor that computes a real-time 'sycophantic drift score' as the model generates its reasoning trajectory, tracking how much the reasoning is bending toward agreeing with a user's stated (possibly incorrect) belief; and a calibrator that intervenes to suppress sycophantic continuation once the drift score crosses a predefined threshold. This operates step-by-step during generation, without waiting for the full answer to be produced, unlike prior approaches that only judge and correct the final answer.

## Results

Described as effectively reducing sycophantic behavior in both intermediate reasoning steps and final answers across the 12 datasets and 3 models tested, with 'robust performance improvements'; specific percentage figures were not available in the material reviewed.

## Limitations

Specific dataset names, model names, and quantitative reduction numbers were not available in the abstract-level material reviewed; no attached PDF or further detail was accessible.

## Why it matters here

- **overthinking**: Not substantively connected to this topic: MONICA addresses chain-of-thought sycophancy (agreeing with incorrect user beliefs), a faithfulness/correctness failure mode, not the accuracy/efficiency tradeoff of reasoning length, test-time compute scaling, or when a model should stop reasoning. The only link is the shared object of study (large reasoning models' chain-of-thought), matched via the generic keyword 'large reasoning model' rather than any treatment of overthinking or underthinking.

## Entities

- **Concepts**: chain-of-thought sycophancy, sycophantic drift, step-level monitoring, monitor-guided calibration
- **Methods**: MONICA, sycophantic monitor, drift-score calibration
- **Datasets**: 12 unnamed datasets (count stated, individual names not given in material reviewed)

Tags: `sycophancy`, `chain-of-thought`, `faithfulness`, `monitoring`, `large-reasoning-models`

---

Record id: `title:5906e734c9eebcc3`
