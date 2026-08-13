<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# FoE: Forest of Errors Makes the First Solution the Best in Large Reasoning Models

- **Authors**: Kehan Jiang, Haonan Dong, Zhaolu Kang, Zhengzhou Zhu, Guojie Song
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.1128>
- **DOI**: 10.18653/V1/2026.ACL-LONG.1128
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.80

## In one line

Finds that a reasoning model's first solution is usually its best and that later alternatives are actively harmful, characterizes the errors as a forest structure, and prunes accordingly.

## Problem

Reasoning models explore multiple alternative solutions in a human-like way, and test-time scaling laws predict that helps. Closer inspection suggests the opposite: alternative solutions are not merely suboptimal but potentially detrimental, which would mean errors accumulate along with test-time compute.

## Contributions

- The 'First is The Best' phenomenon: later alternative solutions are detrimental rather than merely suboptimal
- A forest-structured characterization of errors along the reasoning path, with theoretical analysis
- RED, combining Refining First to suppress in-branch error growth with Discarding Subs to prune alternatives by dual-consistency
- Gains up to 19.0% with 37.7%-70.4% token reduction against eight baselines on five benchmarks and six backbones
- FoE metrics as a diagnostic for why the method works

## Method

Empirical analysis characterizes errors within the reasoning path as a forest-structured Forest of Errors, and argues with theoretical support that this structure makes the first solution the best. RED follows from the diagnosis in two parts: Refining First suppresses FoE growth within the first solution, and Discarding Subs prunes subsequent alternatives using dual-consistency. The two components map onto the two ways the forest hurts — growth inside a branch and proliferation of branches.

## Results

Across five benchmarks and six backbone models, RED outperforms eight competitive baselines with gains up to 19.0% while cutting token consumption by 37.7% to 70.4%. Comparative experiments on FoE metrics are reported to explain the mechanism.

## Limitations

The 19.0% gain is an upper bound, not a typical one. Benchmarks and backbones are not named in the abstract. 'The First is The Best' is a claim about the models and benchmarks tested; it conflicts with the sizeable literature where self-consistency over many samples helps, and the abstract does not delimit when it holds. The theoretical analysis is asserted here without its assumptions.

## Why it matters here

- **reasoning-training**: Makes an unusually strong claim against test-time scaling: that exploration of alternatives is net negative because errors scale with compute, so the first solution should be refined and the rest discarded. If it holds, it inverts the premise of the best-of-N and self-consistency lines this archive tracks in depth. It also cuts directly against arxiv:2608.05643 in this same drain, which keeps breadth precisely to preserve diverse initial attempts and reports gains from doing so — same year, same problem, opposite prescription, and neither cites a shared model. That collision is the kind the archive exists to record, and resolving it needs the overlap in their benchmarks and backbones, which neither abstract gives.

## Entities

- **Concepts**: test-time scaling, [overthinking](../../../../wiki/concepts/overthinking.md), [reasoning redundancy](../../../../wiki/concepts/reasoning-redundancy.md), [error propagation](../../../../wiki/concepts/compounding-error.md), self-consistency, [answer stabilization](../../../../wiki/concepts/answer-stabilization.md), forest of errors
- **Methods**: RED, dual-consistency pruning, [test-time scaling](../../../../wiki/methods/test-time-scaling.md), [self-consistency](../../../../wiki/methods/self-consistency.md)
- **Datasets**: _none recorded_

Tags: `test-time scaling`, `overthinking`, `error propagation`, `pruning`, `efficient reasoning`

## Abstract

Recent Large Reasoning Models (LRMs) like DeepSeek-R1 have demonstrated remarkable success in complex reasoning tasks, exhibiting human-like patterns in exploring multiple alternative solutions. Upon closer inspection, however, we uncover a surprising phenomenon: The First is The Best, where alternative solutions are not merely suboptimal but potentially detrimental. This observation challenges widely accepted test-time scaling laws, leading us to hypothesize that errors within the reasoning path scale concurrently with test time. Through comprehensive empirical analysis, we characterize errors as a forest-structured Forest of Errors (FoE) and conclude that FoE makes the First the Best, which is underpinned by rigorous theoretical analysis. Leveraging these insights, we propose RED, a self-guided efficient reasoning framework comprising two components: I) Refining First, which suppresses FoE growth in the first solution; and II) Discarding Subs, which prunes subsequent FoE via dual-consistency. Extensive experiments across five benchmarks and six backbone models demonstrate that RED outperforms eight competitive baselines, achieving performance gains of up to 19.0% while reducing token consumption by 37.7%   70.4%. Moreover, comparative experiments on FoE metrics shed light on how RED achieves effectiveness.

---

Record id: `doi:10.18653/v1/2026.acl-long.1128`
