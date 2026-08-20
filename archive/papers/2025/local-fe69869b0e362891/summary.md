<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Transformers Provably Learn Chain-of-Thought Reasoning with Length Generalization

- **Authors**: Yu Huang, Zixin Wen, Aarti Singh, Yuejie Chi, Yuxin Chen
- **Venue**: NeurIPS
- **Published**: 2025-01-01
- **Source**: local
- **Topics**: reasoning-training, test-time-scaling, reasoning-interpretability
- **Relevance score**: reasoning-training 0.50, test-time-scaling 0.50

## In one line

Gives the first optimization guarantee that gradient descent trains constant-depth transformers to solve NC1-complete problems with chain of thought, and shows the algebraic structure of the task decides how far the learned reasoning extrapolates.

## Problem

Expressivity results establish that CoT lets constant-depth transformers reach beyond TC^0, but they say only what can be represented. Prior optimization analyses covered simple, highly parallelizable tasks inside TC^0 that need no sequential reasoning, leaving a gap between what transformers can express and what training actually finds. A second gap is length generalization: whether reasoning learned on short problems extends to longer chains, on which empirical evidence is mixed.

## Contributions

- The first optimization guarantee that constant-depth transformers trained by gradient descent learn NC^1-complete problems with CoT, beyond prior results confined to TC^0
- A proof that the algebraic structure of a state-tracking task governs how far the learned CoT extrapolates, with simply transitive actions generalizing and symmetry group actions generalizing only partly
- Attention concentration as the mechanism connecting the attention layer's retrieval robustness to length generalization
- A proof that recursive self-training progressively extends the range of solvable problem lengths for transformers with limited reasoning length
- Experiments confirming both the length-generalization behaviour and the attention-concentration mechanism

## Method

A minimally viable setting is analysed so gradient dynamics remain tractable: a one-layer transformer block with softmax attention and a feed-forward network, trained by gradient descent with no positional encoding. The tasks are LEGO state-tracking problems, which distil skills like entity tracking, game-state updates and code evaluation. Two task families with different algebraic structure are compared — simply transitive group actions against symmetry group actions — and attention patterns are tracked through training to see how the reasoning capability emerges. Length generalization is explained through attention concentration, tying the attention layer's retrieval robustness to the task's state-tracking structure. For transformers whose reasoning length is limited, a recursive self-training scheme is analysed.

## Results

A one-layer NoPE transformer trained by gradient descent provably solves constant-length LEGO state-tracking with CoT. Extrapolation is governed by algebraic structure: when the group action is simply transitive, the learned transformer generalizes directly to substantially longer problems; for the canonical action of the symmetry group S_n on Z_n it generalizes only up to a limited range. Recursive self-training progressively extends the range of solvable lengths. The headline is the first optimization guarantee that constant-depth transformers provably learn NC^1-complete problems with CoT, going beyond prior optimization results confined to TC^0 unless TC^0 = NC^1. Experiments confirm the length-generalization behaviour and the attention-concentration mechanism.

## Limitations

The tractable setting is a one-layer block on synthetic LEGO tasks with no positional encoding, so the guarantee is for a minimal model on structured problems rather than a deployed architecture on natural reasoning. The extrapolation characterization is stated in terms of group-action structure, which is available for synthetic tasks and not obviously identifiable for real ones. The separation from TC^0 rests on the conjecture that TC^0 != NC^1. Recursive self-training extends the solvable range progressively rather than without limit.

## Why it matters here

- **reasoning-interpretability**: Supplies a mechanism, attention concentration, and then confirms it experimentally rather than leaving it as a proof device. That is the shape of explanation this topic wants — a named, checkable property of the attention layer that predicts a behavioural outcome — and it is unusual in coming from the optimization side rather than from post-hoc probing. It also connects to the archive's state-tracking entries, which measure the failure behaviourally while this identifies what in the attention layer produces it.
- **reasoning-training**: Closes the loop the archive's theory papers leave open. Expressivity says a constant-depth transformer with CoT can reach NC^1; sample complexity says the data cost is logarithmic; this says gradient descent actually gets there. Prior optimization analyses had only covered TC^0 tasks that need no sequential reasoning, so the interesting regime was exactly the unproven one. Its substantive claim for this topic is that extrapolation is decided by the task's algebraic structure rather than by scale or data — a simply transitive action generalizes and a symmetry group action does not — which predicts that some reasoning tasks will never length-generalize however much they are trained, and identifies the property that decides it. The recursive self-training result also gives the archive's self-training thread its first guarantee, that iterating on one's own solutions provably extends reach rather than merely appearing to.

## Entities

- **Concepts**: [length generalization](../../../../wiki/concepts/length-generalization.md), [state tracking](../../../../wiki/concepts/state-tracking.md), optimization guarantee, attention concentration, [expressivity-learnability gap](../../../../wiki/concepts/expressivity-learnability-gap.md), self-training, [circuit complexity](../../../../wiki/concepts/circuit-complexity.md), [training dynamics](../../../../wiki/concepts/training-dynamics.md), context rot
- **Methods**: [gradient descent analysis](../../../../wiki/methods/gradient-descent-analysis.md), chain of thought, recursive self-training, [attention analysis](../../../../wiki/methods/attention-analysis.md), LEGO state-tracking
- **Datasets**: LEGO

Tags: `optimization guarantee`, `length generalization`, `state tracking`, `attention concentration`, `theory`

## Abstract

The ability to reason lies at the core of artificial intelligence (AI), and challenging problems usually call for deeper and longer reasoning to tackle. A crucial question about AI reasoning is whether models can extrapolate learned reasoning patterns to solve harder tasks with longer chain-of-thought (CoT). In this work, we present a theoretical analysis of transformers learning on synthetic state-tracking tasks with gradient descent. We mathematically prove how the algebraic structure of state-tracking problems governs the degree of extrapolation of the learned CoT. Specifically, our theory characterizes the length generalization of transformers through the mechanism of attention concentration, linking the retrieval robustness of the attention layer to the state-tracking task structure of long-context reasoning. Moreover, for transformers with limited reasoning length, we prove that a recursive self-training scheme can progressively extend the range of solvable problem lengths. To our knowledge, we provide the first optimization guarantee that constant-depth transformers provably learn NC1-complete problems with CoT, significantly going beyond prior art confined in TC0, unless the widely held conjecture TC0 != NC1 fails. Finally, we present a broad set of experiments supporting our theoretical results, confirming the length generalization behaviors and the mechanism of attention concentration.

---

Record id: `local:fe69869b0e362891`
