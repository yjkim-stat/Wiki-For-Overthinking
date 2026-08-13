<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Finding Usable Weight Mechanisms with Tiled SVD

- **Authors**: Ash Manvi, Samreena Tajreen
- **Venue**: cs.AI
- **Published**: 2026-08-07
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.06969>
- **PDF**: <https://arxiv.org/pdf/2608.06969v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.40

## In one line

Extracts interpretable units directly from a transformer's weight matrices by column-tiled SVD, so a unit's identity is the weight rule itself rather than an atom of a separately trained dictionary, and judges them with a pre-registered suite whose central move is refusing a metric that a trivial baseline would win.

## Problem

The standard route to naming directions in a network trains a proxy dictionary such as a sparse autoencoder on activations and labels features from max-activating text. That aligns interpretation to a separately learned codebook rather than to any weight matrix inside the network, so 'what this direction means' is answered in the proxy space and the rule that actually writes into the residual stream is left implicit. Singular vectors of weight matrices are already known to form interpretable token clusters and to act as detector-effector pairs, but SVD has been used as a lens or a circuit primitive rather than tested as a fair answer to which chunking of a weight matrix yields usable on-distribution mechanisms.

## Contributions

- Mechanism mounts: a triple of trigger, write and strength read off a column tile of a linear weight, whose identity is the weight rule and which carries no verbal label
- A negative result about the obvious metric -- tile-local energy lift is won tautologically by one-column tiles, so the suite scores full-write energy lift instead
- Coverage saturation: on residual writes, one or two modes per tile capture nearly all the achievable coverage and extra modes add redundancy
- A depth-conditioned causal check separating what a write direction looks like under an unembedding lens from what steering along it actually does
- Effective-path mounts for the two maps whose raw module weights are not the map used on distribution

## Method

A linear weight is partitioned by input columns into tiles, each tile is factored by SVD, and each retained mode becomes a mount: the right singular vector is the trigger, the normalized left singular vector is the write direction, the singular value is the strength. Tile widths are site-aware. Four constructions are compared under a matched mount budget -- per-tile SVD, SVD of the full matrix, high-norm column sampling, and a random unit direction -- which is what makes the chunking question answerable rather than assumed. The metric choice is the methodological core. Tile-local energy lift, the natural score, is approximately 1 for column sampling by construction, so it rewards the degenerate chunking; the pass criteria therefore use full-write energy lift measured against the whole site's write tensor, with random directions as the reference. Coverage is the fraction of weight energy kept by per-tile rank-k reconstruction, and saturation is required to peak above a site-dependent floor early in the mode sweep and not collapse afterwards. The causal check applies only where the write is a residual direction: an unembedding lens predicts the final-logit geometry of a write direction, steering injects that direction after the post-sublayer RMSNorm, and the Spearman correlation between steered logit changes and the lens prediction is required to clear a threshold, waived below layer 6. Two maps get special treatment because their raw module weights are not the map used on distribution -- the up-projection is scored through a mean-gate effective matrix and the value projection through a ridge least-squares fit from residual to mixed value -- and everything runs on Gemma-2-2B over a 16,384-token WikiText-2 subsample.

## Results

Tiling beats every alternative on both residual-write sites at essentially every depth. At layer 18 the attention output projection scores 0.383 full-write lift for tiles against 0.102 for whole-matrix SVD, 0.011 for column sampling and about zero for random; the MLP down-projection at the same depth scores 0.172 against 0.016 and 0.001. The one exception is the down-projection at the final layer, where tile and whole coincide. The reading offered is that local column structure in a weight matrix is not well summarized by one global SVD when the quantity of interest is on-distribution write energy. Coverage saturates immediately: on the attention output at layer 6 the lift is 0.779 at one mode per tile and 0.793 at two, and is 0.785 at sixteen, so all 52 residual site-layers pass the early-saturation rule and extra modes are redundancy. The causal check produces a clean depth curve rather than a single verdict. Steer-versus-lens agreement is near zero in the earliest layers -- about -0.03 to 0.07 on the down-projection -- rises through the middle of the network, and reaches about 0.91 on the down-projection and 0.75 on the attention output at the final layer, which is why the early-layer waiver exists and is stated as motivated by the curve rather than by convenience. Aggregate: all 182 site-layers across all seven linear maps pass, 52 of 52 on the full A/B/C suite and 130 of 130 on the A/B tier, once the two maps use effective rather than raw weights.

## Limitations

The paper's own list is unusually direct, and its discussion opens by saying the novelty is thin: singular vectors of transformer weights, detector-effector units and unembedding readouts all already exist, no human-readable concept names are claimed, and no replacement for sparse autoencoders in concept discovery is claimed -- the contribution is fair chunking, a negative result about the tile-local metric, coverage saturation, and a reproducible depth-conditioned causal check. Stated limits: one model family and size; the causal experiment applies only to residual-write sites; a WikiText-2 subsample may bias which mounts look strong; energy lift is not human meaning and mounts carry no semantic labels; steering uses short texts, a fixed multiplier and last-token logits; the early-layer waiver is a design choice; the final-layer down-projection is marginal on one criterion and still passes. What a reader should add is the shape of the headline: a pre-registered suite on which every one of 182 site-layers passes has not discriminated anything on this model, and the runner searches tile sizes and effective-path pools and keeps the best passing trial -- so 182/182 is a statement that a configuration exists per site, not that the default one works. The interesting numbers are the per-construction gaps in Experiment A and the depth curve in Experiment C, both of which would survive a stricter bar.

## Why it matters here

- **reasoning-interpretability**: Supplies a measurement this archive's standing finding has been missing a curve for. The archive holds that how well a direction detects a property licenses no claim about what intervening on it does; here the two are computed for the same direction at every depth, and the correlation between the unembedding lens's prediction and the effect of actually steering runs from about zero in the first six layers to 0.91 at the last. So the gap between detection and intervention is not constant -- it is a function of depth, and it is worst exactly where most probing work reads representations. It also offers a concrete alternative to the sparse-autoencoder route the archive's interpretability cluster is built on: units whose identity is a weight rule rather than a dictionary atom, with the honest caveat, stated by the authors, that they come with no names.

## Entities

- **Concepts**: mechanism mount, [residual stream](../../../../wiki/concepts/residual-stream.md), write direction, energy lift, coverage saturation, [detection versus control](../../../../wiki/concepts/detection-versus-control.md), [monosemanticity](../../../../wiki/concepts/monosemanticity.md), effective path, weight-based interpretability
- **Methods**: singular value decomposition, [logit lens](../../../../wiki/methods/logit-lens.md), [activation steering](../../../../wiki/methods/activation-steering.md), [sparse autoencoder](../../../../wiki/methods/sparse-autoencoder.md), [ridge regression](../../../../wiki/methods/ridge-regression.md), [ablation](../../../../wiki/methods/ablation.md)
- **Datasets**: WikiText-2

Tags: `mechanistic-interpretability`, `svd`, `weights`, `steering`, `evaluation-protocol`

## Abstract

The dominant approach to mechanistic interpretability trains proxy dictionaries such as sparse autoencoders and labels features from max-activating text. The best such atlases identify con- cepts, but that identity lives in the learned dictionary rather than in the network weights them- selves. We propose extracting mechanism mounts directly from linear sites by column-tiled SVD: each mount is a triple (v,u,σ) read as trigger, write, and strength. Identity is the weight rule. We evaluate mounts with a pre-registered suite judged on full-write energy lift rather than tile-local lift. On Gemma-2-2B with WikiText-2 (16,384-token subsample), all seven linear maps are scored: residual writes (mlp.down, attn.o) receive full A/B/C with steer after post-sublayer RMSNorm and pass 52/52 site-layers; other maps receive A/B only (mlp.gate/attn.q/attn.k/effective mlp.up/attn.v 26/26 each). Aggregate: 182/182 GO. We release library code, the corpus builder, the experiment entrypoint, and unit tests.

---

Record id: `arxiv:2608.06969`
