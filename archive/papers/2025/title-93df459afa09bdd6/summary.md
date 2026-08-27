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

WebThinker gives large reasoning models a Deep Web Explorer module and an Autonomous Think-Search-and-Draft strategy so they can search, navigate, and draft research reports interleaved with reasoning, trained via iterative online DPO, and it outperforms existing methods and strong proprietary systems on complex reasoning and report-generation benchmarks.

## Problem

Large reasoning models rely on static internal knowledge, which limits performance on complex knowledge-intensive tasks and prevents them from producing comprehensive research reports that require synthesizing diverse, current web information.

## Contributions

- a Deep Web Explorer module letting LRMs autonomously search, navigate and extract web information during reasoning
- an Autonomous Think-Search-and-Draft strategy interleaving reasoning, search and report drafting
- an iterative online DPO training strategy improving research-tool utilization, outperforming existing methods and strong proprietary systems

## Method

Integrates a Deep Web Explorer module enabling LRMs to dynamically search, navigate, and extract information from the web when they hit a knowledge gap, and an Autonomous Think-Search-and-Draft strategy that interleaves reasoning, information gathering, and report drafting in real time; adds an RL-based training strategy via iterative online Direct Preference Optimization to improve research-tool use.

## Results

On complex reasoning benchmarks (GPQA, GAIA, WebWalkerQA, HLE) and a scientific report-generation task (Glaive), WebThinker significantly outperforms existing methods and strong proprietary systems (no specific numeric deltas given in the fetched abstract).

## Limitations

Not stated in the fetched abstract; evaluation limited to the listed reasoning/report-generation benchmarks.

## Why it matters here

- **overthinking**: Indirectly relevant: this is about extending LRM reasoning with external web search rather than making a fixed reasoning trace shorter or better-calibrated, but it is an example of the kind of agentic, multi-tool reasoning system where reasoning-length/overthinking concerns compound with tool-call overhead -- relevant background context rather than a direct contribution to the topic's core measurement/mitigation questions.

## Entities

- **Concepts**: Deep Web Explorer, Think-Search-and-Draft strategy, iterative online DPO for tool use
- **Methods**: iterative online Direct Preference Optimization (DPO), agentic web search and navigation
- **Datasets**: [GPQA](../../../../wiki/datasets/gpqa.md), [GAIA](../../../../wiki/datasets/gaia.md), WebWalkerQA, [HLE](../../../../wiki/datasets/hle.md), Glaive

Tags: `deep-research-agent`, `large-reasoning-models`, `web-search`, `tool-use`

## Abstract

Abstract Large reasoning models (LRMs), such as OpenAI-o1 and DeepSeek-R1, demonstrate impressive long-horizon reasoning capabilities. However, their reliance on static internal knowledge limits their performance on complex, knowledge-intensive tasks and hinders their ability to produce comprehensive research reports requiring synthesis of diverse web information. To address this, we propose WebThinker, a deep research agent that empowers LRMs to autonomously search the web, navigate among web pages, and draft reports during the reasoning process. WebThinker integrates a Deep Web Explorer module, enabling LRMs to dynamically search, navigate, and extract information from the web when encountering knowledge gaps. It also employs an Autonomous Think-Search-and-Draft strategy, allowing the model to seamlessly interleave reasoning, information gathering, and report writing in real time. To further enhance research tool utilization, we introduce an RL-based training strategy via iterative online Direct Preference Optimization (DPO). Extensive experiments on complex reasoning benchmarks (GPQA, GAIA, WebWalkerQA, HLE) and scientific report generation tasks (Glaive) demonstrate that WebThinker significantly outperforms existing methods and strong proprietary systems. Our approach enhances LRM reliability and applicability in complex scenarios, paving the way for more capable and versatile deep research systems. The code is available at https://github.com/RUC-NLPIR/WebThinker.

---

Record id: `title:93df459afa09bdd6`
