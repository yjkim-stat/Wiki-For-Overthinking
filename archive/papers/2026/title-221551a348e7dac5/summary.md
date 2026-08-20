<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# When More is Less: Understanding Chain-of-Thought Length in LLMs

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10011380>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

Shows chain-of-thought accuracy follows an inverted U-shape in reasoning length, derives how the optimal CoT length scales with task difficulty and model capability, and uses this to explain and mitigate overthinking via RL-based length calibration and length-aware filtering.

## Problem

It is commonly assumed that longer chain-of-thought reasoning always helps LLM accuracy, but static-length CoT training data is reused across models and tasks without adapting to how much reasoning a given task/model pair actually needs, and there was no principled account of why and when longer reasoning starts to hurt.

## Contributions

- Demonstrates, across real-world LLMs and theoretical models, that task accuracy follows an inverted U-shape with respect to chain-of-thought length: performance rises then falls as reasoning chains grow too long.
- Shows the optimal CoT length increases with task difficulty and decreases with model capability, exposing a mismatch with current practice of reusing the same CoT training data across models and tasks without adapting length.
- Shows reinforcement learning can dynamically calibrate CoT length and close this gap, improving accuracy over supervised fine-tuning that reuses fixed-length CoT data.
- Introduces an error-accumulation analysis that models how reasoning errors propagate across steps and derives the observed scaling behavior of optimal CoT length.
- Shows training with optimally sized CoTs and applying length-aware filtering at inference yields substantial performance improvements, and frames this as a principled explanation of the 'overthinking' effect.

## Method

The paper combines controlled empirical experiments on real LLMs and theoretical/toy models with an error-accumulation analysis: it characterizes how per-step reasoning errors accumulate as CoT length grows, deriving why accuracy first improves (errors from insufficient reasoning are reduced) then declines (accumulated errors from unnecessary extra steps dominate) as chains lengthen. It then uses this to derive scaling laws for optimal CoT length as a function of task difficulty and model capability, and applies RL to dynamically calibrate CoT length during training, plus length-aware filtering at inference time.

## Results

Task accuracy follows an inverted U-shaped curve with respect to CoT length across both real-world LLMs and theoretical models; optimal CoT length increases with task difficulty and decreases with model capability; RL-based dynamic length calibration improves accuracy over static-length supervised fine-tuning; training with optimally sized CoTs plus length-aware inference-time filtering yields substantial performance improvements. Specific numeric results and benchmark names are not given in the abstract.

## Limitations

The abstract does not name the specific real-world LLMs, benchmarks, or numeric accuracy figures used in the controlled experiments; specific dataset names are not given in the available material.

## Why it matters here

- **overthinking**: This paper is a direct, central study of the overthinking topic: it establishes empirically and theoretically that accuracy is an inverted-U function of CoT length, characterizes how the optimal length scales with task difficulty and model capability, explains the mechanism via error accumulation, and proposes RL-based length calibration and length-aware filtering as concrete methods to keep reasoning length matched to the problem.

## Entities

- **Concepts**: inverted U-shaped accuracy vs. CoT length, optimal CoT length, error-accumulation analysis, length-aware filtering
- **Methods**: reinforcement learning for length calibration, error-accumulation analysis, length-aware filtering, supervised fine-tuning (as baseline)
- **Datasets**: _none recorded_

Tags: `overthinking`, `chain-of-thought-length`, `inverted-u`, `error-accumulation`, `reinforcement-learning`, `length-calibration`

## Abstract

Abstract Large Language Models (LLMs) increasingly rely on Chain-of-Thought (CoT) reasoning to solve complex problems. Contrary to the common belief that longer CoTs always improve performance, we demonstrate that longer is not always better . Across both real-world LLMs and theoretical models, task accuracy follows an inverted U-shaped curve with respect to CoT length: performance rises initially but declines once reasoning chains become too long. Through controlled experiments, we uncover scaling behaviors of the optimal CoT length : it increases with task difficulty but decreases with model capability. This exposes a significant mismatch with current practice, where supervised training often reuses the same CoT data across models and tasks without adaptivity. We further show that Reinforcement Learning (RL) can mitigate this gap by dynamically calibrating CoT length, thereby improving accuracy and offering a new perspective on differences between supervised fine-tuning and RL training. To explain these phenomena, we introduce an error-accumulation analysis that characterizes how reasoning errors propagate across steps and derives the scaling behaviors of CoT length observed empirically. Building on these insights, we show that training with optimally sized CoTs and applying length-aware filtering during inference yields substantial improvements in performance. Taken together, these findings establish a principled explanation of the ''overthinking'' effect and yield practical guidelines for calibrating CoT length in accordance with task complexity and model capability.

---

Record id: `title:221551a348e7dac5`
