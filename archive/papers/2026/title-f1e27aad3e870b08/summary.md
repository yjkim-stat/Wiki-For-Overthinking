<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Are Large Reasoning Models Interruptible?

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/61807>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Evaluates large reasoning models under budget-constrained interruptions and mid-reasoning context changes, finding accuracy drops of up to 60% and three recurring failure modes not visible under static evaluation.

## Problem

Large reasoning models are conventionally evaluated under a 'frozen world' assumption -- instantaneous responses to an immutable prompt -- which does not hold for real tasks like assistive programming where reasoning can take hours and the context can change before the model finishes.

## Contributions

- An evaluation framework that tests large reasoning models under interruptions (limited output budget) and dynamic context (in-flight changes to the problem)
- Empirical demonstration that static 'frozen world' evaluations overestimate LRM robustness, with accuracy dropping by up to 60% when context updates arrive late in reasoning
- Identification of three failure modes: reasoning leakage, panic, and self-doubt

## Method

The authors evaluate large reasoning models under two dynamic scenarios that break the standard 'frozen world' evaluation assumption: interruptions, where the model must produce an answer from a partial reasoning trace under a limited compute/time budget, and dynamic context, where the problem statement changes while the model is still reasoning. Testing spans mathematics and programming benchmarks requiring long-form reasoning.

## Results

State-of-the-art LRMs that score highly under static evaluation can fail unpredictably when interrupted or given changing context, with accuracy dropping by up to 60% when updates arrive late in the reasoning process. Three failure modes are identified: reasoning leakage (unfinished reasoning folds into the final answer when interrupted), panic (the model abandons structured reasoning under time pressure and returns an incorrect answer), and self-doubt (accuracy degrades when the model tries to incorporate updated information).

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Studies precisely what happens when a reasoning model is forced to stop before it would otherwise finish (budget-constrained interruption) or must adapt reasoning already in progress -- the operational version of 'making a model stop at the right point.' It shows that cutting reasoning short is not a benign efficiency lever: it induces specific failure modes (reasoning leakage, panic, self-doubt) and accuracy drops of up to 60%, which bears directly on the safety of budget-based methods for curbing overthinking.

## Entities

- **Concepts**: frozen world assumption, interruption robustness, dynamic context adaptation, reasoning leakage, panic, [self-doubt](../../../../wiki/concepts/self-doubt.md)
- **Methods**: interruption evaluation protocol, dynamic context evaluation protocol
- **Datasets**: _none recorded_

Tags: `overthinking`, `interruptibility`, `test-time-compute`, `reasoning-robustness`, `budget-constrained-reasoning`

---

Record id: `title:f1e27aad3e870b08`
