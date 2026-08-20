<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# TUMIX: Multi-Agent Test-Time Scaling with Tool-Use Mixture

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10010417>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

An ensemble of parallel agents using different tool-use strategies that iteratively refine and share answers, with a confidence-based rule to stop early and cut inference cost.

## Problem

LLMs given tools like code interpreters and search can reason more effectively, but there is little practical guidance on how to combine textual reasoning, coding and search across diverse question types, and running many agents or rounds indiscriminately is costly.

## Contributions

- Proposes TUMIX (Tool-Use Mixture), an ensemble framework that runs multiple agents in parallel, each with a distinct tool-use strategy (text-only, code-executing, web-searching) and answer path
- Has agents iteratively share and refine responses conditioned on the question and prior agents' answers
- Shows agent diversity and quality, tunable by using an LLM to auto-optimize agent designs, are the key drivers of ensemble gains
- Introduces a confidence-based mechanism that halts further refinement rounds once agents have converged sufficiently, cutting inference cost

## Method

TUMIX runs a heterogeneous set of agents in parallel on the same question, each using a different tool-use strategy (pure chain-of-thought, code execution, or web search) and therefore a different answer path. Across iterative rounds, agents condition on the original question and on the other agents' previous answers to refine their own. Agent designs (prompts/strategies) can themselves be auto-optimized by an LLM to increase diversity and quality. An LLM-based judge monitors confidence across agents and halts further refinement rounds once agreement is sufficient, rather than always running to a fixed depth.

## Results

Up to 3.55% average accuracy improvement over the best baseline on Gemini-2.5-Pro and Gemini-2.5-Flash across reasoning benchmarks, at near-equal inference cost to those baselines; confidence-based early stopping preserves performance while using only 49% of the inference cost of running refinement to full depth; further scaling of rounds/agents yields higher performance at proportionally higher cost.

## Limitations

Further scaling of the number of agents/rounds achieves higher performance but at a proportionally greater inference cost; the specific reasoning benchmarks used were not named in the material reviewed.

## Why it matters here

- **overthinking**: Addresses the test-time-compute side of the topic: rather than scaling a single chain's reasoning length, it scales the number of parallel tool-using agents, and it includes an explicit stopping rule (confidence-based early termination) that preserves accuracy while using only 49% of the inference cost of full-depth refinement. It is a genuine treatment of the accuracy/compute-cost tradeoff and of stopping at the right point, though at the multi-agent level rather than within one reasoning chain.

## Entities

- **Concepts**: [test-time scaling](../../../../wiki/concepts/test-time-scaling.md), multi-agent ensembling, tool-use diversity, confidence-based early stopping
- **Methods**: TUMIX, tool-use mixture, multi-agent ensembling, [confidence-based early stopping](../../../../wiki/methods/confidence-based-early-stopping.md)
- **Datasets**: _none recorded_

Tags: `test-time-scaling`, `multi-agent`, `tool-use`, `early-stopping`, `inference-cost`

---

Record id: `title:545becf86760af05`
