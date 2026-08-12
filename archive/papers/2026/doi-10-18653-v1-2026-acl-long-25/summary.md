<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Your Reasoning Model Knows What Counts: Self-Guided Chain-of-Thought Pruning for Efficient Reasoning

- **Authors**: Zi-Ao Ma, Xian-Ling Mao, Tian Lan 0003, Chen Xu, Zhijing Wu 0001
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.25>
- **DOI**: 10.18653/V1/2026.ACL-LONG.25
- **Topics**: reasoning-training, test-time-scaling
- **Relevance score**: reasoning-training 0.67, test-time-scaling 0.50

## In one line

Prunes chain-of-thought segments the model's own likelihood landscape marks as extraneous, then trains on the resulting pruning preference pairs.

## Problem

CoT is essential to reasoning-model performance but carries redundant and distracting segments that raise cost and hurt robustness. Existing approaches enforce brevity by external supervision — length penalties, heuristic truncation — which degrades performance because they disregard the model's intrinsic reasoning dependency and cannot tell essential segments from redundant ones.

## Contributions

- The argument that external brevity supervision fails because it ignores the model's intrinsic reasoning dependency
- SGP-CoT, a self-guided pruning framework using internal likelihood signals over semantic units
- A necessity measure combining a unit's contribution to the answer with local coherence
- Construction of pruning-based preference pairs enabling self-optimization
- Reported length reduction with maintained or improved accuracy

## Method

SGP-CoT treats the reasoning trajectory as a sequence of semantic units and assesses each unit's necessity using the model's own internal likelihood signals, measuring its contribution to the answer and to local coherence. Using the model's likelihood landscape rather than an external length rule is what makes the necessity judgement specific to that model's reasoning pattern. Non-essential segments are removed, the removals form pruning-based preference pairs, and the model learns focused reasoning through self-optimization on those pairs.

## Results

Across diverse benchmarks, SGP-CoT significantly reduces output length while maintaining or improving accuracy. No numbers, benchmarks or models are given in the abstract.

## Limitations

No quantitative results, benchmarks or models in the abstract. Necessity is judged by the model's own likelihood, so a segment the model undervalues but that a correct derivation requires would be pruned — the criterion is self-referential. Semantic-unit segmentation is a preprocessing choice whose method is unstated, and it determines what can be pruned.

## Why it matters here

- **reasoning-training**: Another entry in the archive's token-selection dispute, at segment granularity, with the criterion being the model's own likelihood contribution. That places it beside MUTO in this drain, which uses log-probability gain of the ground-truth answer — the difference being that MUTO's signal needs the answer and this one does not, so this one can in principle run without labels. Whether the two select the same segments is measurable and unmeasured, and it is the specific comparison that would tell whether label-free pruning loses anything.
- **test-time-scaling**: The pruning criterion is computed from internal likelihood, which is available during generation, so the same signal could gate an inference-time stopping decision rather than a training-time removal. The paper uses it only for training, which leaves that variant open and connects it to the archive's stopping-signal family.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), [reasoning redundancy](../../../../wiki/concepts/reasoning-redundancy.md), [token selection](../../../../wiki/concepts/token-selection.md), self-guided pruning, preference optimization, semantic unit, likelihood signal
- **Methods**: SGP-CoT, [preference optimization](../../../../wiki/methods/preference-optimization.md), chain of thought pruning, self-optimization
- **Datasets**: _none recorded_

Tags: `overthinking`, `token selection`, `pruning`, `preference optimization`, `self-guided`

## Abstract

,

---

Record id: `doi:10.18653/v1/2026.acl-long.25`
