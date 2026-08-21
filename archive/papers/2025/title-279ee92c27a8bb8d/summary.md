<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# How Far Are We from Optimal Reasoning Efficiency?

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/118341>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.70

## In one line

Defines an empirical accuracy-vs-token-budget frontier for a fixed base reasoning model, measures how far existing efficiency methods fall short of it with a single metric (REG), and proposes REO-RL, an RL objective that targets a handful of token budgets to close most of that gap.

## Problem

Methods for making reasoning models shorter are reported on incompatible axes — one trades accuracy for brevity, another keeps accuracy but spends far more tokens than needed — so there is no way to say which is better, or how much room is left. What is missing is a reference point: the best accuracy any fine-tune of a given base model attains at each token budget. Without it, 'efficient reasoning' results cannot be compared across papers and no one can say how far from optimal the field is.

## Contributions

- The reasoning efficiency frontier: an empirical accuracy-per-token-budget upper envelope over many fine-tunes of a fixed base LRM
- Reasoning Efficiency Gap (REG), one metric summing the shortfall from that frontier across all budgets, making accuracy-vs-length methods comparable
- A systematic finding that existing efficiency methods fail in one of two distinct ways: brevity bought with accuracy, or high accuracy bought with far more tokens than the frontier requires
- REO-RL, an RL algorithm approximating the full efficiency objective by numerical integration over a sparse set of token budgets (N=5 gives <1% approximation error)
- Two budget-selection schemes, Oracle (greedy from estimated frontiers) and Exp (exponentially spaced), with ablations showing both work

## Method

Fine-tune one base LRM many ways and many configurations, then take the pointwise upper envelope of their accuracy-at-budget curves: J_optimal(D, Theta, L) = max over theta in the fine-tuned set of J(D, theta, L), for every token budget L. That envelope is the reasoning efficiency frontier — empirical, not theoretical, and defined relative to the pool of fine-tunes used to build it. The Reasoning Efficiency Gap of a model is the summed shortfall against it: d_REG(theta) = sum over L of [J_optimal(D, Theta, L) - J(D, theta, L)], which folds accuracy and length into one number. REO-RL then optimizes that objective directly. Because summing over every budget is prohibitive, it approximates the integral over a sparse set of N budgets with trapezoidal weights c_i = (L_{i+1} - L_{i-1})/2; the paper reports N=5 budgets suffice for under 1% approximation error. Two budget-selection variants: REO-RL (Oracle) greedily picks budgets from estimated frontiers, REO-RL (Exp) spaces them exponentially, L_i = L_min * (L_max/L_min)^((i-1)/N). The effect is a dense reward that rewards being correct at each of several truncation points rather than only at the end.

## Results

Base models DeepSeek-R1-Distill-Qwen-1.5B/7B and Qwen3-4B/8B, trained on 135k problems from DeepScaleR and AReaL, max generation 32K tokens, evaluated on AMC23, AIME24, AIME25 and Minerva Math. On DeepSeek-R1-Distill-Qwen-7B: vanilla RL reaches 64.4% accuracy at 11,282.6 average tokens; REO-RL (Exp) reaches 62.9% (-1.5 points) at 5,966.0 tokens, a 55.9% REG reduction; RL with a fixed 4K token budget reaches 54.1% at 2,677.0 tokens for only 27.5% REG reduction. Abstract-level headline is 74.5% and 64.2% REG reduction over vanilla outcome-reward RL at 1.5B and 7B. REO-RL gives >=50% REG reduction across all four models. Baselines compared: vanilla RL, RL with length-based rewards, hybrid reasoning (HGPO), SFT, and preference learning (SimPO). Note the frontier is constructed from the authors' own pool of fine-tunes, so REG is a relative measure and a method outside that pool could in principle sit above the frontier.

## Limitations

The paper states that matching the frontier exactly remains open — REO-RL closes most of the gap but does not eliminate it. Two things a reader should notice. First, the frontier is empirical and pool-dependent: it is the upper envelope of the fine-tunes the authors happened to train, so REG measures distance from the best thing they built, not from an optimum, and adding one better fine-tune to the pool moves everyone's score. Second, the claim that the 7B model surpasses Qwen3 and Claude Sonnet 3.7 in conciseness is a claim about length, made against models the frontier was not built from; conciseness at comparable accuracy is the only version of that comparison that carries weight. Evaluation is mathematics only (AMC/AIME/Minerva), so nothing is established about token budgets on non-math reasoning.

## Why it matters here

- **overthinking**: This is the measurement paper the topic needs. Every method in this area reports 'X% fewer tokens at comparable accuracy', and those numbers are not comparable across papers because each picks its own operating point on its own base model; REG replaces the pair with one number defined against a common frontier. Two findings matter for how the group reads other work here. First, the failure taxonomy — methods either buy brevity with accuracy or hit good accuracy at budgets far above what the frontier shows is attainable — means a paper reporting high accuracy is not thereby efficient, and vice versa. Second, targeting only five token budgets approximates the whole accuracy-per-budget curve to under 1% error, which says the tradeoff curve is smooth enough that dense supervision at every length is unnecessary. Caveat when citing: the frontier is the envelope of the authors' own fine-tune pool, so REG is a relative yardstick, and the evaluation is math-only.

## Entities

- **Concepts**: [Overthinking](../../../../wiki/concepts/overthinking.md), Reasoning Efficiency Frontier, Reasoning Efficiency Gap, [Token Budget](../../../../wiki/concepts/token-budget.md), [Accuracy-Efficiency Tradeoff](../../../../wiki/concepts/accuracy-efficiency-tradeoff.md), [Test-Time Compute Scaling](../../../../wiki/concepts/test-time-compute-scaling.md)
- **Methods**: REO-RL, Reasoning Efficiency Gap (REG), reasoning efficiency frontier, reinforcement learning with outcome reward, length-based reward RL, HGPO, SimPO, supervised fine-tuning, numerical integration over token budgets
- **Datasets**: AMC 2023, [AIME 2024](../../../../wiki/datasets/aime-2024.md), [AIME 2025](../../../../wiki/datasets/aime-2025.md), [Minerva Math](../../../../wiki/datasets/minerva-math.md), [DeepScaleR](../../../../wiki/datasets/deepscaler.md), AReaL

Tags: `overthinking`, `reasoning-efficiency`, `token-budget`, `benchmark`, `metric`, `rl`, `test-time-compute`

## Abstract

Abstract Large Reasoning Models (LRMs) demonstrate remarkable problem-solving capabilities through extended Chain-of-Thought (CoT) reasoning but often produce excessively verbose and redundant reasoning traces. This inefficiency incurs high inference costs and limits practical deployment. While existing fine-tuning methods aim to improve reasoning efficiency, assessing their efficiency gains remains challenging due to inconsistent evaluations. In this work, we introduce the reasoning efficiency frontiers , empirical upper bounds derived from fine-tuning a base LRM (DeepSeek-R1-Distill-Qwen-1.5B/7B) across diverse approaches and training configurations. Based on these frontiers, we propose the Reasoning Efficiency Gap (REG) , a unified metric quantifying deviations of any fine-tuned LRMs from these frontiers. Systematic evaluation on challenging mathematical benchmarks, AMC23, AIME24, and AIME25, reveals significant gaps in current methods: they either sacrifice accuracy for short length or use excessive tokens to achieve sub-optimal accuracies despite high overall accuracy. To reduce the efficiency gap, we propose REO-RL , a Reinforcement Learning algorithm that optimizes reasoning efficiency by targeting a sparse set of token budgets. Leveraging numerical integration over strategically selected budgets, REO-RL approximates the full efficiency objective with low error using a small set of token budgets. Experiments show that, compared to vanilla RL with outcome reward, REO-RL reduces the reasoning efficiency gap by 74.5\% and 64.2\% in the 1.5B and 7B settings. The 7B LRM fine-tuned with REO-RL achieves reasoning conciseness surpassing frontier LRMs like Qwen3 and Claude Sonnet 3.7. Ablation studies confirm the efficacy of our token budget strategy and highlight REO-RL’s flexibility across design choices. This work establishes a systematic framework for evaluating and optimizing reasoning efficiency in LRMs. We will release the related code, data, and models to support future research on efficient reasoning in LRMs.

---

Record id: `title:279ee92c27a8bb8d`
