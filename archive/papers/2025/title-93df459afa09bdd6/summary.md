<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# WebThinker: Empowering Large Reasoning Models with Deep Research Capability

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/119715>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

WebThinker gives large reasoning models an autonomous web-search-and-report-drafting loop, trained via iterative online DPO, for knowledge-intensive deep research tasks.

## Problem

Large reasoning models rely on static internal knowledge, which limits performance on complex, knowledge-intensive tasks and their ability to produce research reports that synthesize diverse web information.

## Contributions

- WebThinker: a deep research agent giving LRMs autonomous web search, navigation and report drafting during reasoning
- Deep Web Explorer module for dynamic search/navigation/extraction when the model hits a knowledge gap
- Autonomous Think-Search-and-Draft strategy interleaving reasoning, information gathering and report writing
- RL-based training via iterative online Direct Preference Optimization (DPO) to improve tool utilization

## Method

WebThinker adds a Deep Web Explorer module that lets the LRM search, navigate and extract information from the web mid-reasoning, combined with an Autonomous Think-Search-and-Draft strategy that interleaves reasoning, information gathering and report writing in real time. The system is further trained with an RL-based strategy using iterative online DPO to improve how it uses the search tools.

## Results

Reported to significantly outperform existing methods and strong proprietary systems on GPQA, GAIA, WebWalkerQA, HLE and the Glaive report-generation task; no specific numeric scores given in the abstract.

## Limitations

Abstract does not report specific numeric results or failure cases; no discussion of cost or latency overhead of the added web-browsing loop.

## Why it matters here

- **overthinking**: Only shares the generic 'large reasoning model' keyword. The paper is about extending LRMs with web search, navigation and report-drafting capability, not about reasoning length, when a model should stop or keep going, or the accuracy/efficiency tradeoff of test-time compute. No treatment of overthinking or underthinking.

## Entities

- **Concepts**: deep research agent, tool-augmented reasoning, online preference optimization
- **Methods**: Deep Web Explorer, Think-Search-and-Draft strategy, iterative online Direct Preference Optimization (DPO)
- **Datasets**: [GPQA](../../../../wiki/datasets/gpqa.md), [GAIA](../../../../wiki/datasets/gaia.md), WebWalkerQA, [HLE](../../../../wiki/datasets/hle.md), Glaive

Tags: `web-agent`, `deep-research`, `tool-use`, `dpo`

## Abstract

Abstract Large reasoning models (LRMs), such as OpenAI-o1 and DeepSeek-R1, demonstrate impressive long-horizon reasoning capabilities. However, their reliance on static internal knowledge limits their performance on complex, knowledge-intensive tasks and hinders their ability to produce comprehensive research reports requiring synthesis of diverse web information. To address this, we propose WebThinker, a deep research agent that empowers LRMs to autonomously search the web, navigate among web pages, and draft reports during the reasoning process. WebThinker integrates a Deep Web Explorer module, enabling LRMs to dynamically search, navigate, and extract information from the web when encountering knowledge gaps. It also employs an Autonomous Think-Search-and-Draft strategy, allowing the model to seamlessly interleave reasoning, information gathering, and report writing in real time. To further enhance research tool utilization, we introduce an RL-based training strategy via iterative online Direct Preference Optimization (DPO). Extensive experiments on complex reasoning benchmarks (GPQA, GAIA, WebWalkerQA, HLE) and scientific report generation tasks (Glaive) demonstrate that WebThinker significantly outperforms existing methods and strong proprietary systems. Our approach enhances LRM reliability and applicability in complex scenarios, paving the way for more capable and versatile deep research systems. The code is available at https://github.com/RUC-NLPIR/WebThinker.

---

Record id: `title:93df459afa09bdd6`
