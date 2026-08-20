<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Less Diverse, Less Safe: The Indirect But Pervasive Risk of Test-Time Scaling in Large Language Models

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/64671>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Shows that test-time-scaling methods such as Monte Carlo Tree Search and Best-of-N become substantially more likely to produce unsafe outputs when candidate diversity is curtailed, using a diagnostic protocol called RefDiv.

## Problem

It was unclear whether test-time scaling introduces safety vulnerabilities indirectly, through reduced diversity among candidate reasoning paths or outputs, as opposed to only through explicit adversarial prompting.

## Contributions

- Introduces RefDiv, a diagnostic protocol that curtails candidate diversity within test-time-scaling generation to probe safety
- Shows diversity curtailment consistently raises unsafe-output rates under test-time scaling, across strategies (MCTS, Best-of-N) and across open and proprietary models
- Shows existing safety filters such as Llama-Guard fail to detect RefDiv-generated adversarial inputs

## Method

RefDiv is a diagnostic protocol that constrains candidate diversity during test-time-scaling generation (tested with Monte Carlo Tree Search and Best-of-N) across multiple open models (Qwen3, Mistral, Llama3.1, Gemma3) and proprietary systems (OpenAI o3-mini, Gemini-2.5-Pro), measuring the resulting rate of unsafe outputs and testing whether existing safety classifiers detect the resulting inputs.

## Results

Curtailing candidate diversity, even by a modest amount, consistently increases unsafe-output rates under test-time scaling, often surpassing the effect of directly adversarial prompts; the effect generalizes across MCTS and Best-of-N and across Qwen3, Mistral, Llama3.1, Gemma3, OpenAI o3-mini and Gemini-2.5-Pro; Llama-Guard fails to detect RefDiv-generated adversarial inputs.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Studies test-time-scaling methods (MCTS, Best-of-N) as its subject, but from a safety angle: curtailing candidate diversity during test-time scaling raises unsafe-output rates, often more than direct adversarial prompts, and evades existing safety filters. This is a real but safety-focused contribution to the test-time-compute-scaling side of the topic, distinct from the accuracy/efficiency reasoning-length tradeoff.

## Entities

- **Concepts**: [test-time scaling](../../../../wiki/concepts/test-time-scaling.md), candidate diversity, safety risk, adversarial robustness
- **Methods**: RefDiv, [Monte Carlo Tree Search](../../../../wiki/methods/monte-carlo-tree-search.md), [Best-of-N](../../../../wiki/methods/best-of-n.md)
- **Datasets**: _none recorded_

Tags: `test-time-scaling`, `safety`, `diversity`, `adversarial`

---

Record id: `title:abd61e399170fa2c`
