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

GRACE stabilizes and speeds up automatic LLM prompt optimization using update-gating and adaptive compression of the prompt/optimization trace when search stalls.

## Problem

Automatic prompt optimization for LLMs is unstable and inefficient, and often gets trapped in local optima during the search for better prompts.

## Contributions

- Proposes GRACE, a prompt-optimization framework combining gated refinement and adaptive compression.
- Introduces a feedback regulation gate and an update rejection gate to stabilize prompt update signals.
- Introduces an adaptive compression strategy that distills a prompt's core concepts and restructures the optimization trace when search stagnates.
- Reports gains on 11 tasks across BIG-Bench Hard, domain-specific, and general NLP settings while using a quarter of the prompt-generation budget of prior methods.

## Method

GRACE integrates two strategies for optimizing a prompt's text. Gated refinement uses a feedback regulation gate and an update rejection gate to filter and stabilize proposed prompt edits, aiming to avoid noisy or harmful updates. Adaptive compression is triggered when optimization stagnates: it distills the prompt down to its core concepts and restructures the optimization trace/history, opening new search directions. Both strategies deliberately introduce information loss (refinement and compression) to improve the search.

## Results

Average relative performance improvements of 4.7% (BBH), 4.4% (domain-specific tasks), and 2.7% (general NLP tasks) over prior state-of-the-art prompt optimization methods across 11 tasks, achieved using only 25% of the prompt-generation budget required by prior methods.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Tangential. This paper optimizes the text of an input prompt through an iterative search process; 'adaptive compression' here means compressing the prompt itself and its optimization trace, not compressing or controlling the length of a model's reasoning/chain-of-thought at inference time. It shares only the surface phrase 'adaptive compression' with the topic and has no treatment of reasoning-length overthinking or test-time compute scaling.

## Entities

- **Concepts**: automatic prompt optimization, gated refinement, adaptive compression, local optima in prompt search
- **Methods**: GRACE framework, feedback regulation gate, update rejection gate, adaptive prompt compression
- **Datasets**: BIG-Bench Hard (BBH), domain-specific tasks (unspecified), general NLP tasks (unspecified)

Tags: `prompt-optimization`, `prompt-engineering`, `search`

## Abstract

Abstract Prompt engineering is crucial for leveraging the full potential of large language models (LLMs). While automatic prompt optimization offers a scalable alternative to costly manual design, generating effective prompts remains challenging. Existing methods often struggle to stably generate improved prompts, leading to low efficiency, and overlook that prompt optimization easily gets trapped in local optima. Addressing this, we propose GRACE, a framework that integrates two synergistic strategies: Gated Refinement and Adaptive Compression, achieving Efficient prompt optimization. The gated refinement strategy introduces a feedback regulation gate and an update rejection gate, which refine update signals to produce stable and effective prompt improvements. When optimization stagnates, the adaptive compression strategy distills the prompt’s core concepts, restructuring the optimization trace and opening new paths. By strategically introducing information loss through refinement and compression, GRACE delivers substantial gains in performance and efficiency. In extensive experiments on 11 tasks across three practical domains, including BIG-Bench Hard (BBH), domain-specific, and general NLP tasks, GRACE achieves significant average relative performance improvements of 4.7\%, 4.4\% and 2.7\% over state-of-the-art methods, respectively. Further analysis shows that GRACE achieves these gains using only 25\% of the prompt generation budget required by prior methods, highlighting its high optimization efficiency and low computational overhead. Our code is available at https://github.com/Eric8932/GRACE.

---

Record id: `title:46b721af432d8a4e`
