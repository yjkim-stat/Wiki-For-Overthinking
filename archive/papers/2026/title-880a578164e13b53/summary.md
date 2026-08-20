<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Multi-Objective Protein Design via Memory-Aware Test-Time Scaling in Diffusion Models

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/65578>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Adds a memory bank and self-contrastive preference signal to test-time diffusion sampling so a protein-design model can balance multiple, sometimes conflicting, functional objectives without retraining.

## Problem

Multi-objective protein design requires optimizing several functions at once, and existing test-time diffusion approaches learn poorly from their own interaction history (repeating design errors), overweight successful outcomes for reward, and struggle to balance competing objectives.

## Contributions

- MoMST, a test-time diffusion framework for multi-objective protein design that requires no retraining to adapt to new objectives.
- A memory bank that captures generalizable reasoning experience from historical design iterations to avoid repetitive design errors.
- Self-contrastive learning that derives preference signals from both successful and unsuccessful past attempts, plus a Pareto alignment strategy for balancing conflicting design objectives during inference.

## Method

During iterative test-time diffusion sampling for protein sequences/structures, MoMST maintains a memory bank of past design iterations and their outcomes, from which it extracts generalizable experience rather than relying only on the most recent successful sample. A self-contrastive learning signal is derived by contrasting successful and unsuccessful past iterations, and a Pareto alignment strategy balances multiple, potentially competing, functional objectives during generation, all without retraining the underlying diffusion model.

## Results

No specific benchmark numbers were available in the retrieved material (no PDF or numeric results found on the paper's ICML page); the paper reports strong performance on single- and multi-objective design tasks relative to baselines.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Tangential, as expected from the domain: this paper applies 'test-time scaling' to diffusion-model-based protein design, not to a large reasoning model's chain-of-thought. It shares only the generic phrase 'test-time scaling' with the tracked topic; there is no reasoning-length, chain-of-thought, or stopping-criterion content connecting it to overthinking/underthinking in LRMs.

## Entities

- **Concepts**: memory-aware test-time diffusion, self-contrastive preference learning, Pareto alignment for multi-objective design
- **Methods**: MoMST, test-time diffusion, self-contrastive learning, Pareto alignment
- **Datasets**: _none recorded_

Tags: `protein-design`, `diffusion-models`, `test-time-scaling`, `multi-objective`

---

Record id: `title:880a578164e13b53`
