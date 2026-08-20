<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models

- **Authors**: Shaokang Wang, Pei Fu, Ruoceng Zhang, Shaojie Zhang, Xiuwen Xi, Jiahui Yang, Bin Qin, Ying Huang, Zhenbo Luo, Jian Luan
- **Venue**: arXiv.org
- **Published**: 2026-01-26
- **Source**: semanticscholar
- **Link**: <https://www.semanticscholar.org/paper/024b8e6fbfc20171bb77a15a3c2116a29f69f4f6>
- **DOI**: 10.48550/arXiv.2601.18197
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

GAIA trains an iteratively self-improving critic model that filters GUI agent actions by predicted success probability, used as a test-time scaling mechanism for GUI agents.

## Problem

GUI agent actions are often irreversible, so a single wrong action (e.g. a misclick) can cause catastrophic task failure; the paper addresses how to select higher-success-probability actions at inference time without changing the base agent.

## Contributions

- Trains an Intuitive Critic Model (ICM) from positive/negative GUI agent action examples to score the immediate correctness of an agent's intended action before it is executed.
- Uses the first-round critic to guide the base agent's action collection, generating refined positive/negative samples that train a second-round critic with improved discernment.
- Reports that the resulting critic improves test-time performance of both closed-source and open-source GUI agent models, with gains growing as the data-recycling cycle repeats.

## Method

GAIA trains an Intuitive Critic Model (ICM) on positive and negative examples of a base GUI agent's actions to judge whether an intended action is likely to succeed before it is taken, filtering for higher-success-probability operations. The critic-guided agent is then run to collect a refined set of positive/negative samples, which are used to train a second-round critic with better discrimination. This critic-guided data collection and retraining loop (a 'data flywheel') is repeated to progressively improve the critic and, through it, the test-time action-selection quality of the underlying GUI agent.

## Results

The abstract states only that the proposed ICM 'can improve the test-time performance of various closed-source and open-source models' and that performance improves gradually as data is recycled through the flywheel, with no specific benchmark names or numeric accuracy figures given.

## Limitations

The abstract does not report specific benchmark names, accuracy numbers, or ablations; it only states that experiments were run on 'various datasets' and that performance improves 'gradually' as data is recycled. No quantitative results, model list, or failure analysis is given.

## Why it matters here

- **overthinking**: Tangential: the paper matches only on the generic phrase 'Test-Time Scaling', which here refers to letting a critic model filter/select GUI agent actions at inference time, not to the length of a language model's reasoning trace. It does not address chain-of-thought length, the accuracy/efficiency tradeoff of reasoning, or when a reasoning model should stop or keep thinking; its domain is GUI action selection for vision-language agents.

## Entities

- **Concepts**: critic-guided action selection, data flywheel self-improvement, test-time scaling for GUI agents
- **Methods**: Intuitive Critic Model (ICM), GUI Action Critic's Data Flywheel System (GAIA), test-time scaling (TTS) for GUI agents
- **Datasets**: _none recorded_

Tags: `gui-agents`, `critic-model`, `test-time-scaling`, `vision-language-models`, `self-improvement`, `data-flywheel`

## Abstract

While Large Vision-Language Models (LVLMs) have significantly advanced GUI agents'capabilities in parsing textual instructions, interpreting screen content, and executing tasks, a critical challenge persists: the irreversibility of agent operations-where a single erroneous action can trigger catastrophic deviations. To address this, we propose the \textbf{G}UI \textbf{A}ction Cr\textbf{i}tic's Dat\textbf{a} Flywheel System (GAIA), a training framework that enables the models to have iterative critic capabilities, which are used to improve the Test-Time Scaling (TTS) of basic GUI agents'performance. Specifically, we train an \textbf{Intuitive Critic Model} (ICM) using positive and negative action examples from a base agent first. This critic evaluates the immediate correctness of the agent's intended actions, thereby selecting operations with higher success probability. Then, the initial critic guides agent actions to collect refined positive/negative samples, initiating the self-improving cycle. The augmented data then trains a second-round critic with enhanced discernment capability. We conduct experiments on various datasets and demonstrate that the proposed ICM can improve the test-time performance of various closed-source and open-source models, and the performance can be gradually improved as the data is recycled. The code, dataset, and accompanying datasheet will be publicly released at https://github.com/SeerRay-Lab/GAIA.

---

Record id: `arxiv:2601.18197`
