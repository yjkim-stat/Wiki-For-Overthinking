<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Mitigating Factual Hallucination in Large Reasoning Models via Mixed-Mode Advantage Regularization

- **Authors**: Kaishen Wang, Tong Zheng, Xuehao Cui, Ruibo Chen, Tianyi Xiong, Heng Huang
- **Venue**: arXiv
- **Published**: 2026-07-07
- **Source**: semanticscholar
- **Link**: <https://www.semanticscholar.org/paper/0294e3ee8794087f78b1cd58a21c3b4ab12f7f56>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

This paper shows that explicit reasoning traces can overturn otherwise-correct direct answers in factual QA (thinking-induced hallucination), and proposes an RL method (MARGO) that uses the model's own non-thinking answers as a reference to suppress harmful thinking while keeping useful thinking.

## Problem

In factuality-oriented QA, explicit chain-of-thought reasoning improves average accuracy by helping recover relevant knowledge, but at the instance level it can also overturn an answer that would have been correct without thinking, producing factual drift; existing training does not distinguish these two effects of thinking.

## Contributions

- Identifies and names 'thinking-induced hallucination': explicit thinking traces in factuality-oriented QA can overturn an already-correct non-thinking answer and introduce factual drift, at the instance level, even though thinking improves average performance.
- Formulates explicit thinking as a 'thinking residual' over the model's direct-answer tendency, which can either recover missing knowledge (helpful) or introduce unsupported associations (harmful).
- Proposes MARGO (Mixed-Mode Advantage Regularization for Grounded Optimization), an RL framework that uses non-thinking rollouts from the same model as reference points in advantage estimation, built from mixed-mode rollout groups containing both thinking and non-thinking trajectories.
- Shows MARGO improves factual reliability over strong baselines on multiple factuality-oriented QA benchmarks while preserving general reasoning ability on mathematical benchmarks.

## Method

MARGO is a reinforcement learning framework for large reasoning models. For a given question it constructs mixed-mode rollout groups that include both explicit-thinking trajectories and non-thinking (direct-answer) trajectories from the same model. It uses the non-thinking rollouts as same-model reference points when computing the advantage for RL updates, which lets the framework evaluate whether a given instance of explicit thinking actually adds factual value beyond what a direct answer would give. Thinking that does not add value (and instead drifts away from a correct direct answer) is penalized, suppressing hallucination-prone thinking, while thinking that recovers genuinely missing knowledge is preserved and reinforced.

## Results

The abstract states MARGO 'improves factual reliability over strong baselines' on multiple factuality-oriented QA benchmarks and 'preserves general reasoning ability' as shown on mathematical benchmarks, but gives no specific numeric results.

## Limitations

The abstract does not name the specific QA or math benchmarks used, nor does it report numeric results (accuracy, hallucination rate reduction, or reasoning-preservation figures). No ablation details, model sizes, or comparison baselines are specified beyond 'strong baselines'.

## Why it matters here

- **overthinking**: Directly relevant, from the 'thinking hurts' side of the tradeoff: it documents a concrete failure mode where a reasoning model's explicit thinking (rather than its length per se) overturns an already-correct answer, and proposes an RL method that uses non-thinking rollouts as a reference to decide when thinking should be suppressed versus preserved -- a mechanism for deciding whether the model should reason at all rather than for how long, which is a specific instance of 'making a model stop (or keep going) at the right point.'

## Entities

- **Concepts**: thinking-induced hallucination, thinking residual over direct-answer tendency, mixed-mode advantage estimation, same-model non-thinking reference
- **Methods**: MARGO (Mixed-Mode Advantage Regularization for Grounded Optimization), reinforcement learning with mixed-mode (thinking / non-thinking) rollout groups, advantage estimation using same-model non-thinking references
- **Datasets**: multiple factuality-oriented QA benchmarks (unspecified by name in abstract), mathematical reasoning benchmarks (unspecified by name in abstract)

Tags: `hallucination`, `factuality`, `chain-of-thought`, `reinforcement-learning`, `advantage-estimation`, `thinking-vs-non-thinking`

## Abstract

Large reasoning models (LRMs) improve language model capabilities by generating explicit thinking traces before final answers. In factuality-oriented question answering (QA), such thinking often improves overall performance by helping the model recover relevant knowledge and refine its answers. However, we find that this benefit is not uniform at the instance level: explicit thinking can also overturn correct non-thinking answers and lead to factual drift. We refer to this failure mode as \emph{thinking-induced hallucination}. To explain this phenomenon, we formulate explicit thinking in factuality QA as a thinking residual over the model's direct-answer tendency, which can either recover missing knowledge or introduce unsupported associations. Based on this formulation, we propose MARGO, \underline{\textit{M}}ixed-Mode \underline{\textit{A}}dvantage \underline{\textit{R}}egularization for \underline{\textit{G}}rounded \underline{\textit{O}}ptimization, a reinforcement learning framework that uses non-thinking rollouts as same-model references in advantage estimation. By constructing mixed-mode rollout groups with both thinking and non-thinking trajectories, MARGO evaluates whether explicit thinking adds factual value beyond direct answering, thereby suppressing hallucination-prone thinking while preserving beneficial thinking behaviors. Experiments across multiple factuality-oriented QA benchmarks demonstrate that MARGO improves factual reliability over strong baselines, while evaluations on mathematical benchmarks show that it preserves general reasoning ability.

---

Record id: `arxiv:2607.05861`
