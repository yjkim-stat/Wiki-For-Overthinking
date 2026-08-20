<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Trajectory-Relative Hindsight Distillation for Agentic Reinforcement Learning

- **Authors**: Haoyu Zheng, Yun Zhu, Qing Wang, Wenqiao Zhang
- **Venue**: cs.LG
- **Published**: 2026-08-07
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.07371>
- **PDF**: <https://arxiv.org/pdf/2608.07371v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.40

## In one line

Distributes hindsight supervision across the turns of an agent trajectory by comparing each turn's share of total revision magnitude against its share of eligible tokens, holding the average multiplier at one so the total supervision is fixed and only its allocation changes -- and isolates that allocation with a permutation control that keeps the multiplier values and scrambles which turn receives which.

## Problem

Agentic reinforcement learning optimises a sparse outcome reward over a whole rollout, which says nothing about how credit should be divided among the turns that produced it. Hindsight distillation supplies dense supervision by re-evaluating each realised action against its realised consequence, but a completed rollout produces discrepancies at many turns at once, and a signed token-level gap encodes a local revision without stating how strongly that turn should be emphasised relative to the others in the same interaction. Existing work reduces the granularity mismatch with finer groupings while remaining centred on estimating outcome-based advantages, so the allocation question is left open.

## Contributions

- A trajectory-relative allocation of hindsight supervision across turns, comparing each turn's share of total revision magnitude against its share of eligible tokens, with the eligible-token-weighted mean of the multipliers fixed at one so that supervision is redistributed rather than increased.
- Signed token-level supervision derived from the log-probability gap between ordinary and hindsight-conditioned evaluations of the same realised response, so direction and local strength come from the same quantity.
- A uniform-multiplier control establishing that dense hindsight alone accounts for only part of the gain -- 6.4 points on one metric and nothing consistent on three others.
- A permutation control that preserves the multiplier values and their normalisation while scrambling which turn receives which, isolating source-aligned allocation from mere non-uniformity.
- Results reported as a full matrix over all task families rather than only split-level averages, so per-family disagreement with the aggregate is visible.

## Method

For each decision turn an outcome view exposes that decision's locally realised consequence to a training-time scorer, which re-evaluates the same realised response under ordinary and hindsight-conditioned contexts. The signed token-level log-probability gap between the two gives both the direction and the local strength of supervision, so the update is not merely dense but signed by whether hindsight makes the taken action more or less likely. Allocation across turns is then trajectory-relative rather than absolute: absolute gaps are aggregated within each turn and the turn's share of total revision magnitude is compared against its share of eligible tokens, producing multipliers whose eligible-token-weighted mean is exactly one. That constraint is what makes the result about distribution rather than dose -- the same total supervision is redistributed, not increased. The hindsight view exists only during training, so the deployed policy has the ordinary interface with no extra model, hindsight input or routing. Evaluation covers two interactive environments and two backbones, reported as a full matrix including all six task families of one environment rather than only split averages, against five other methods. The ablation is the paper's methodological contribution: three conditions hold the dense hindsight pathway completely fixed and vary only the applied turn profile -- unit multipliers, the proposed gap-dependent profile, and a permuted profile that assigns each active turn another active turn's multiplier from within the same trajectory, preserving the relative multiplier values up to a common rescaling and restoring the same token-weighted mean of one.

## Results

The method exceeds outcome-only optimisation on all eight combinations of backbone, environment and metric, and records or matches the best point estimate among six methods on six of them. The largest gain is on one environment with the smaller backbone, where success rises from 56.4 to 75.2 percent and the dense task score from 78.7 to 85.7 -- and the two metrics agree, which matters because a success-rate gain unaccompanied by a score gain would suggest threshold effects rather than better behaviour. The ablation decomposes that gain in a way most dense-supervision papers do not attempt. Unit-weighted dense hindsight, which is what a method without allocation would deliver, improves success on one environment by 6.4 points over the outcome-only baseline and yields no consistent gain on the other three metrics -- so dense supervision alone does not explain the result. Applying the gap-dependent trajectory-relative profile on top of that raises all four metrics over the uniform condition, by 12.4 and 7.9 points on one environment and 8.6 and 11.2 on the other. The permutation condition is the stricter test and the reason the conclusion is credible: it keeps the non-uniform multiplier values and the mean-one normalisation while scrambling which turn receives which, so it holds constant everything except whether the allocation is aligned with the turn that generated it.

## Limitations

Stated. The evidence covers text-based interactive environments with discrete actions, and the framework assumes a completed trajectory exposes serialisable post-action evidence that can be aligned with the decision that produced it -- extending the interface to less structured interaction is left open. Each update requires an additional hindsight-conditioned forward pass over generated responses, so training costs more than outcome-only optimisation, though the authors note the deployed policy is unchanged. And the reported runs use a single seed, with cross-seed variance and statistical robustness explicitly unmeasured. Not stated but worth noticing: with a single seed, the eight-of-eight and six-of-six counts that carry the headline are counts over correlated metrics from one run rather than independent successes, and several of the per-task-family numbers in the full matrix move by ten or more points between methods in directions that do not follow the aggregate -- which is why the full matrix is worth having and also why the aggregates should be read loosely. The scorer that produces the hindsight-conditioned evaluation is the same model, so the supervision inherits whatever that model believes about its own realised actions.

## Why it matters here

- **reasoning-training**: The permutation control is the contribution the archive should keep, and it is the second independent instance of the same idea here. This paper preserves its non-uniform multiplier values and their mean-one normalisation while scrambling which turn receives which, so the permuted condition has identical supervision magnitude, identical distribution of multiplier values, and only the assignment broken. The privileged-distillation entry in this archive reaches the same design from a different direction, shuffling completed trajectories across problems so the teacher retains an extra input whose correspondence to the current prefix is destroyed. Both are asking the question a plain ablation cannot: is the benefit from having a structured signal, or from having it matched to the thing it describes. Any paper claiming that per-step or per-turn supervision helps should be asked for that control, because removing the signal and scrambling it are different experiments and only the second distinguishes alignment from volume. The mean-one normalisation deserves its own note. Fixing the eligible-token-weighted mean of the multipliers at exactly one makes the claim about distribution rather than dose, which forecloses the most common confound in dense-supervision work -- that a method labelled as better credit assignment is really just more total gradient on the same trajectories. Combined with the uniform-multiplier baseline showing dense hindsight alone buys 6.4 points on one metric and nothing consistent on three others, the decomposition is unusually complete: signal present but flat, signal present and shaped, signal present and misassigned. Two cautions. Everything rests on a single seed, which the authors state, so the eight-of-eight and six-of-six tallies are counts over correlated metrics from one run. And the hindsight scorer is the same model re-reading its own realised actions, so the supervision inherits that model's beliefs about what its actions accomplished -- a limit the paper does not discuss and which distinguishes this from hindsight grounded in an external verifier.

## Entities

- **Concepts**: [credit assignment](../../../../wiki/concepts/credit-assignment.md), [advantage estimation](../../../../wiki/concepts/advantage-estimation.md), [hindsight](../../../../wiki/concepts/hindsight.md), [process reward](../../../../wiki/concepts/process-reward.md), [outcome reward](../../../../wiki/concepts/outcome-reward.md), [teacher-student gap](../../../../wiki/concepts/teacher-student-gap.md), [privileged information](../../../../wiki/concepts/privileged-information.md), selectivity control, [multi-agent pipeline](../../../../wiki/concepts/multi-agent-pipeline.md)
- **Methods**: [GRPO](../../../../wiki/methods/grpo.md), hindsight distillation, [on-policy distillation](../../../../wiki/methods/on-policy-distillation.md), advantage estimation, privileged information, permutation control, [component ablation](../../../../wiki/methods/component-ablation.md)
- **Datasets**: [WebShop](../../../../wiki/datasets/webshop.md), [ALFWorld](../../../../wiki/datasets/alfworld.md)

Tags: `agentic-rl`, `hindsight`, `credit-assignment`, `turn-level`, `permutation-control`, `distillation`

## Abstract

Recent agentic reinforcement learning methods use hindsight to complement sparse outcome rewards. However, a completed rollout can yield many such signals, leaving their appropriate allocation across turns unclear. We introduce TRIAL, a trajectory-relative hindsight distillation framework with a unified turn-aligned scoring protocol. For each decision turn, TRIAL extracts an outcome view of that decision's realized consequence and evaluates the same response under ordinary and hindsight-conditioned contexts. The signed log-probability gap determines the direction and local strength of token-level supervision, while turn-level magnitudes are normalized jointly over the realized trajectory. The resulting allocation multipliers have an eligible-token-weighted mean of one, redistributing dense supervision across turns while fixing its average multiplier. Experiments on WebShop and ALFWorld with different backbones show that TRIAL outperforms GRPO across all eight combinations of backbone, environment, and evaluation metric, while achieving the best or tied-best performance among six methods on six of them. On WebShop with Qwen3-1.7B, TRIAL improves the success rate from 56.4% to 75.2% and the task score from 78.7% to 85.7%. Controlled ablations further show that trajectory-relative turn allocation provides substantial gains beyond those of dense hindsight distillation alone.

---

Record id: `arxiv:2608.07371`
