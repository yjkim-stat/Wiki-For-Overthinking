<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# No Loss, No Gain: Gated Refinement and Adaptive Compression for Prompt Optimization

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/118743>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

GRACE improves automatic prompt optimization by combining a gated-refinement mechanism (to stabilize update signals) with adaptive compression (distilling a stagnating prompt to escape local optima), reaching better task performance using only 25% of the prompt-generation budget of prior methods.

## Problem

Automatic prompt optimization methods often generate unstable, inefficient prompt updates and get trapped in local optima, and existing approaches overlook this stagnation problem.

## Contributions

- GRACE, a prompt-optimization framework combining gated refinement and adaptive compression
- feedback-regulation and update-rejection gates that stabilize prompt update signals
- a compression strategy that escapes optimization stagnation by distilling and restructuring the prompt

## Method

Introduces GRACE, combining (1) gated refinement -- a feedback regulation gate and an update rejection gate that filter update signals for stable, effective prompt improvements -- with (2) adaptive compression -- when optimization stagnates, the prompt's core concepts are distilled and the optimization trace restructured to open new search paths, deliberately introducing information loss to escape local optima.

## Results

Across 11 tasks in BIG-Bench Hard, domain-specific, and general NLP settings, GRACE achieves average relative improvements of 4.7%, 4.4% and 2.7% over state-of-the-art prompt-optimization methods respectively, using only 25% of the prompt-generation budget required by prior methods.

## Limitations

Not stated beyond the tested task domains (BBH, domain-specific, general NLP); no discussion of when deliberate information loss via compression might hurt rather than help.

## Why it matters here

- **overthinking**: Indirectly relevant: matched on 'adaptive compression,' but this compresses and restructures an evolving *prompt* during optimization, not a model's reasoning trace at inference time -- it is a budget-efficiency result in a related but distinct part of the LLM pipeline (prompt engineering rather than inference-time reasoning).

## Entities

- **Concepts**: gated refinement, adaptive prompt compression, prompt-optimization stagnation / local optima
- **Methods**: gated refinement, adaptive compression, automatic prompt optimization
- **Datasets**: BIG-Bench Hard (BBH)

Tags: `prompt-optimization`, `adaptive-compression`, `efficiency`, `local-optima`

## Abstract

Abstract Prompt engineering is crucial for leveraging the full potential of large language models (LLMs). While automatic prompt optimization offers a scalable alternative to costly manual design, generating effective prompts remains challenging. Existing methods often struggle to stably generate improved prompts, leading to low efficiency, and overlook that prompt optimization easily gets trapped in local optima. Addressing this, we propose GRACE, a framework that integrates two synergistic strategies: Gated Refinement and Adaptive Compression, achieving Efficient prompt optimization. The gated refinement strategy introduces a feedback regulation gate and an update rejection gate, which refine update signals to produce stable and effective prompt improvements. When optimization stagnates, the adaptive compression strategy distills the prompt’s core concepts, restructuring the optimization trace and opening new paths. By strategically introducing information loss through refinement and compression, GRACE delivers substantial gains in performance and efficiency. In extensive experiments on 11 tasks across three practical domains, including BIG-Bench Hard (BBH), domain-specific, and general NLP tasks, GRACE achieves significant average relative performance improvements of 4.7\%, 4.4\% and 2.7\% over state-of-the-art methods, respectively. Further analysis shows that GRACE achieves these gains using only 25\% of the prompt generation budget required by prior methods, highlighting its high optimization efficiency and low computational overhead. Our code is available at https://github.com/Eric8932/GRACE.

---

Record id: `title:46b721af432d8a4e`
