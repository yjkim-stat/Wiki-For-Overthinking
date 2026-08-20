<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Inverse Scaling: When Bigger Isn't Better

- **Authors**: _unknown_
- **Venue**: ICLR 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2025/poster/31511>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Reports 11 tasks, found via the Inverse Scaling Prize contest, on which language model accuracy declines as model parameter count and training compute increase, and analyzes why.

## Problem

Whether scaling up model size and training compute reliably improves language model performance; this paper shows the assumption fails for a specific set of tasks and analyzes the mechanisms responsible.

## Contributions

- Runs and analyzes the Inverse Scaling Prize contest, collecting 11 tasks on which language model performance declines as model scale increases
- Identifies four mechanisms behind inverse scaling: preferring memorized sequences over instructions, learning undesirable training-data patterns, focusing on easy distractor tasks over the intended objective, and being misled by few-shot examples
- Documents U-shaped and inverted-U scaling trends where early gains with scale reverse at larger sizes

## Method

Ran a public contest (the Inverse Scaling Prize) soliciting tasks on which larger language models perform worse; collected 11 winning datasets, evaluated them across model families and sizes, and categorized the underlying causes of the observed performance decline into four mechanisms.

## Results

11 datasets from the Inverse Scaling Prize show declining accuracy, or U-shaped/inverted-U accuracy trends, as model scale increases, attributable to four identified mechanisms; no test-time-compute or reasoning-length results are reported.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: This is a distinct paper from the 'Inverse Scaling in Test-Time Compute' work already in the archive. It studies inverse scaling with respect to model parameter count and training compute across 11 static benchmark tasks, not reasoning length or test-time compute allocation. It shares only the keyword 'inverse scaling' with the topic and has no bearing on when a model reasons more or less than a problem needs.

## Entities

- **Concepts**: [inverse scaling](../../../../wiki/concepts/inverse-scaling.md), U-shaped scaling, scaling laws
- **Methods**: _none recorded_
- **Datasets**: Inverse Scaling Prize task suite (11 datasets)

Tags: `scaling-laws`, `model-size`, `inverse-scaling`

---

Record id: `title:cb7f41c5af287a91`
