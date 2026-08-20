<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10011763>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Introduces RFEval, a benchmark that uses counterfactual interventions to test whether an LRM's stated chain-of-thought causally drives its answer, finding 49.7% of outputs unfaithful.

## Problem

Large reasoning models often produce rationales that sound plausible but do not reflect their true decision process, undermining reliability and trust; the paper asks how to formally test and measure this 'faithfulness' independent of whether the final answer is correct.

## Contributions

- Formalizes reasoning faithfulness via two testable conditions: stance consistency and causal influence, decoupled from accuracy
- Introduces RFEval, a 7,186-instance benchmark across seven tasks probing faithfulness via controlled output-level counterfactual interventions
- Finds 49.7% of outputs unfaithful across twelve open-source LRMs, mostly from stance inconsistency, concentrated in math and code
- Shows faithfulness correlates more with post-training regime than model scale: adding RL-style objectives on top of SFT can reduce faithfulness even when accuracy is maintained
- Shows the accuracy-faithfulness link is weak and statistically insignificant once controlling for model and task

## Method

RFEval defines reasoning faithfulness as requiring both stance consistency (a coherent stance linking the reasoning to the answer) and causal influence (the stated reasoning causally drives the answer, tested via output-level interventions). The benchmark applies controlled counterfactual interventions at the output level across seven tasks to twelve open-source LRMs, and compares faithfulness against accuracy and against post-training regime (SFT-only vs. SFT plus RL-style objectives).

## Results

49.7% of outputs judged unfaithful across twelve open-source LRMs, predominantly from stance inconsistency; failures concentrate in math and code; RL-style objectives on top of SFT reduce faithfulness even when accuracy is maintained; the accuracy-faithfulness correlation is weak and statistically insignificant once controlling for model and task.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Tangential: measures whether a model's stated reasoning causally explains its answer (faithfulness), not how much reasoning is used or when a model should stop. It shares only the 'large reasoning model' keyword with the topic, though its finding that RL-style post-training can reduce faithfulness even while accuracy is maintained is adjacent to the topic's interest in what RL training changes about reasoning behavior.

## Entities

- **Concepts**: reasoning faithfulness, stance consistency, causal influence, counterfactual intervention
- **Methods**: RFEval benchmark, counterfactual output-level intervention, stance consistency / causal influence framework
- **Datasets**: RFEval (7,186 instances across 7 tasks)

Tags: `faithfulness`, `interpretability`, `chain-of-thought`, `benchmark`, `counterfactual`

## Abstract

Abstract Large Reasoning Models (LRMs) exhibit strong performance, yet often produce rationales that sound plausible but fail to reflect their true decision process, undermining reliability and trust. We introduce a formal framework for reasoning faithfulness , defined by two testable conditions: stance consistency (a coherent stance linking reasoning to answer) and causal influence (the stated reasoning causally drives the answer under output-level interventions), explicitly decoupled from accuracy. To operationalize this, we present RFEval , a benchmark of 7,186 instances across seven tasks that probes faithfulness via controlled, output-level counterfactual interventions. Evaluating twelve open-source LRMs, we find unfaithfulness in 49.7% of outputs, predominantly from stance inconsistency. Failures are concentrated in brittle, convergent domains such as math and code, and correlate more with post-training regimes than with scale: within-family ablations indicate that adding current RL-style objectives on top of supervised fine-tuning can reduce reasoning faithfulness, even when accuracy is maintained. Crucially, accuracy is neither a sufficient nor a reliable proxy for faithfulness : once controlling for model and task, the accuracy–faithfulness link is weak and statistically insignificant. Our work establishes a rigorous methodology for auditing LRM reliability and shows that trustworthy AI requires optimizing not only for correct outcomes but also for the structural integrity of the reasoning process. Our code and dataset can be found at project page: https://aidaslab.github.io/RFEval/

---

Record id: `title:9f5aee65dee28f12`
