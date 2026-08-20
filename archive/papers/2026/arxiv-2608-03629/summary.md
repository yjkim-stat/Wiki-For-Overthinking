<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Cross-Layer Interaction under Weight-Space Ablation: A Closed-Form Attention Jacobian Bound and a Test on a Real Pretrained Model

- **Authors**: Abdallah Khemais
- **Venue**: cs.AI
- **Published**: 2026-08-04
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.03629>
- **PDF**: <https://arxiv.org/pdf/2608.03629v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.50

## In one line

Extends a single-block interaction theorem to ablated subsets spanning many layers, isolates the cross-layer remainder as an exact double integral rather than bounding it, supplies the one missing closed-form ingredient (a local attention Jacobian bound, verified without a violation on a real 1.5B model), and tests the whole picture on an emergent circuit nobody designed for it — reporting the mixed outcome as mixed.

## Problem

The companion result computes exactly the interaction between two carriers written into the same residual block when an ablation treats them as independent. That stops at one block. A real transformer is a sequential composition of many, and the components an experimenter chooses to ablate together are routinely drawn from different layers, sometimes many apart — indeed a component selected for its causal role is, if anything, more likely to interact with a distant component than with the MLP three lines below it in the same block. The single-block theorem is silent there. A second gap is empirical: every check in the companion paper runs on small transformers trained specifically to exhibit a clean two-branch conditional, which removes ambiguity about the ground-truth mechanism at the cost of saying nothing about a mechanism nobody built to have one.

## Contributions

- An exact decomposition of the interaction produced by an arbitrarily distributed multi-layer ablated subset into a sum of same-block terms, one per touched layer, plus a single cross-layer remainder — with no approximation anywhere in the identity itself
- Two of the three quantities pinned down without a new curvature argument: a same-block term is identically zero when that layer's ablated carriers are MLP-only, and equals the companion's bounded interaction term when that layer feeds the readout directly
- An exact identity for the remaining cross-layer term, for two touched layers, as a double integral of a mixed second derivative over a two-parameter interpolation between the clean and fully edited networks
- A closed-form local Jacobian bound for the attention sub-block — the one ingredient missing to close that identity to a numerical bound — verified pointwise against finite differences on a real model's real weights
- The curvature constant the companion's second-order bound leaves unexhibited, computed in closed form from trained weights alone
- A test of the qualitative predictions on an emergent circuit found by the original activation-patching method for that task, on a pretrained model two orders of magnitude larger than the synthetic instances

## Method

For an ablated subset spanning several blocks, the true weight-edited selector is compared against the idealized prediction by splitting the removed mass termwise across layers and defining, per touched layer, the effect of editing that layer's carriers in isolation. What is left over after summing those is named the cross-layer remainder and isolated rather than bounded; for two touched layers it is then written exactly as a mixed second derivative integrated over a two-parameter interpolation, the same fundamental-theorem-of-calculus technique the companion applies one level down, applied twice. The attention Jacobian is derived for a single perturbed key or value token — a local, pointwise bound evaluated at real activations rather than a supremum over all inputs, because the softmax attention sub-block has no useful global Lipschitz constant — and checked against finite differences before being used for anything. On the real model, four candidate mechanisms are pre-registered and screened for clean matched pairs; only indirect object identification survives on all five lexical instances at a margin above one logit, and the other three are reported because they were pre-registered rather than because they matter. A greedy activation-patching search over every attention head and MLP output, followed by redundancy pruning, produces a circuit per instance, on which three probes are run — collapse under joint zero-ablation, the gap between patching and ablation effects, and the interaction between a head and an MLP — with the operation realizing each one stated precisely, since the three are not the same kind of intervention.

## Results

The decomposition and the two pinned-down cases are proved rather than measured. The Jacobian bound is verified pointwise on a real 1.5B model with zero violations across twelve probed sites. On the real model, the circuit search reproduces the structure other work predicts: one attention head appears in all five instances and another in four, while the remaining sixteen sites appear in at most three and mostly in exactly one — a small shared core plus instance-specific support, the redundant-code pattern reported for superposed and self-repairing networks. Pruning removed nothing on any instance, and four of five circuits reach recovery at or above 0.96 within the six-site budget while the fifth plateaus at 0.673. The three probes give a genuinely mixed verdict, reported as such. Collapse is clear to partial on four instances (ratio 0.168 to 0.396) and absent on the fifth, where ablating its own six-site circuit barely narrows the gap between branches (0.761). Dissociation is never small: the gap between the patching effect and the ablation effect is at least 0.224 and as large as 0.852 on all five, so the two interventions never coincide on this circuit — consistent with the claim that they are different operations, though absent a theorem-derived target value this is evidence of a real, always-present gap rather than a quantitative confirmation. Interaction is measurable on only three instances, since two circuits contain no MLP at all, and ranges from 0.066 to 0.327 — but the paper points out against itself that none of those three layer pairs sits in the same-block configuration the companion theorem was proven for, so what they measure bears on this paper's own open multi-layer case rather than on that theorem.

## Limitations

The paper is unusually precise about what it did not close, and the closing sentences are worth quoting in effect: a theory that only ever gets confirmed on the networks built to confirm it is not yet a theory of anything else. The cross-layer remainder's closed-form bound is the central open item — the missing ingredient is named exactly (chaining the per-layer attention and normalization-MLP Jacobian bounds across every block between two touched layers) and not supplied, and a structural argument is given for why no simple sign rule for it should be expected. The attention Jacobian bound is verified at a single layer and a single perturbed token; whether the per-layer factors compound into something numerically vacuous after a handful of blocks is left as an open empirical question, given four to six orders of magnitude of looseness already present at one layer. The real-model result is one model and one mechanism, not systematic replication: one instance shows no real collapse, the interaction probe applies to only three of five circuits, and none of those three is in the configuration any theorem here covers. The three rejected candidate mechanisms are reported because they were pre-registered, which is the right practice and also means the retained mechanism was selected for cleanliness.

## Why it matters here

- **reasoning-interpretability**: Read with its companion, this is the archive's most complete account of why two standard interpretability interventions can disagree — and the half that matters most for practice is the real-model measurement. On an emergent circuit in a pretrained model, found by the field's own method and never designed for these claims, the gap between what patching says a component is worth and what ablating it says ranges from 0.224 to 0.852 and is never small on any instance. So the theoretical dissociation is not a corner case: it is what happens when either instrument is used on an ordinary circuit. Every claim in this archive resting on patching or on ablation should therefore name which one, and treat the other as an open question rather than a corroboration. Two further things transfer. The circuit search reproduces the shared-core-plus-idiosyncratic-support pattern independently, which is a replication of the redundancy account rather than an assumption of it. And the paper's conduct is the model this archive's findings on baseline validity and randomized controls keep pointing toward — pre-registering candidate mechanisms and reporting the rejected ones, verifying a bound before using it, and stating a mixed result as mixed rather than rounding it toward the theory it was written to support.

## Entities

- **Concepts**: activation patching, weight-space ablation, causal intervention, circuit analysis, cross-layer interaction, [self-repair](../../../../wiki/concepts/self-repair.md), [superposition](../../../../wiki/concepts/superposition.md), [detection versus control](../../../../wiki/concepts/detection-versus-control.md), indirect object identification, pre-registration
- **Methods**: [activation patching](../../../../wiki/methods/activation-patching.md), [low-rank weight ablation](../../../../wiki/methods/low-rank-weight-ablation.md), greedy circuit search, [causal tracing](../../../../wiki/methods/causal-tracing.md), finite-difference verification, Jacobian bound
- **Datasets**: _none recorded_

Tags: `mechanistic interpretability`, `activation patching`, `ablation`, `circuit discovery`, `theory`

## Abstract

A companion paper studies when activation patching and weight-space ablation agree, inside an idealized model where a conditional computation is carried additively through a residual stream. For the one composition in that model where two carriers are architecturally dependent, an attention head and its own layer's normalization-MLP composition, it derives an exact first-order interaction formula, zero when only the MLP is ablated and second-order bounded when the head is also ablated. That result is confined to a single residual block and checked only on small transformers on a synthetic task. This paper extends the result past both limits. First, the interaction from ablating carriers spanning several layers decomposes exactly into same-block terms, one per touched layer, plus a cross-layer remainder on which the decomposition makes no claim of smallness. Second, we isolate that remainder exactly, for two layers, as a double integral of a mixed second derivative, and name the missing ingredient needed to bound it: a Jacobian bound for the attention sub-block. We derive this bound in closed form and verify it, without a single violation, against Qwen2.5-1.5B-Instruct's real weights, though we do not yet chain it across layers. We also give, in closed form, the curvature constant the companion paper's bound leaves unexhibited. Third, on that same model, we search for and find an emergent circuit for indirect object identification, never designed into it, using the original activation-patching method for this task, and test collapse, dissociation, and interaction on it. The result is mixed: a shared carrier emerges across all five tested instances, collapse and dissociation hold on most but not all, and a nonzero interaction is measurable on three of five, at layer pairs outside the same-block case the companion theorem covers.

---

Record id: `arxiv:2608.03629`
