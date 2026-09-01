<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Theoretical Guarantees for One-Shot Magnitude Pruning and Compute-Adaptive Early Exit

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/63550>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Proves concentration theorems giving explicit convergence rates for one-shot magnitude pruning in asymptotic single-neuron settings, introduces the 'conditional perceptron' for early exit with generalization-error bounds tied to a compute-gap parameter, and extends the analysis to deep networks and a neural-network-Gaussian-process framework deriving compute-accuracy tradeoffs for frozen-backbone early-exit systems, validated on vision and language models.

## Problem

Two common neural-network compute-reduction techniques -- one-shot magnitude pruning and early exit -- lack rigorous theoretical guarantees characterizing their convergence behavior and compute-accuracy tradeoffs, particularly for deep networks and frozen-backbone early-exit systems.

## Contributions

- concentration theorems with explicit convergence rates for one-shot magnitude pruning in asymptotic single-neuron settings
- the conditional perceptron formalism for early exit, with generalization-error bounds as a function of a compute-gap parameter
- an extension to deep networks characterizing accumulated pruning distortion across layers, and an NNGP-based derivation of compute-accuracy tradeoffs for frozen-backbone early-exit systems, validated experimentally on vision and language models

## Method

Proves concentration theorems for one-shot magnitude pruning with explicit convergence rates in asymptotic single-neuron settings; introduces the 'conditional perceptron' formalism for early exit and establishes that generalization error decreases as a function of a compute-gap parameter (with faster improvement when the partial computation aligns closely with the full computation); extends the pruning analysis to deep networks, characterizing how pruning-induced distortions accumulate across layers; derives compute-accuracy tradeoffs for frozen-backbone early-exit systems under a neural-network-Gaussian-process (NNGP) framework.

## Results

Experimental results on vision and language models validate the theoretical scaling predictions derived from the concentration theorems and the NNGP-based compute-accuracy tradeoff analysis (no specific numeric deltas given in the fetched abstract).

## Limitations

Not stated in the fetched abstract beyond the asymptotic single-neuron setting used for the pruning concentration theorems and the frozen-backbone assumption for the early-exit compute-accuracy analysis.

## Why it matters here

- **overthinking**: Indirectly relevant: this is a theoretical analysis of pruning and early-exit compute-accuracy tradeoffs for general neural networks (validated on vision and language models), not specifically LLM reasoning-trace length, but it provides a rigorous mathematical foundation (concentration theorems, NNGP-derived tradeoff curves) for the same class of early-exit techniques that overthinking-mitigation methods in this archive apply empirically to reasoning traces.

## Entities

- **Concepts**: one-shot magnitude pruning concentration theorems, conditional perceptron (early exit), compute-gap parameter, neural network Gaussian process (NNGP) framework
- **Methods**: one-shot magnitude pruning, conditional perceptron (early exit), neural network Gaussian process (NNGP) analysis
- **Datasets**: _none recorded_

Tags: `early-exit`, `pruning`, `theory`, `compute-accuracy-tradeoff`

---

Record id: `title:eaf8c68124e5ee94`
