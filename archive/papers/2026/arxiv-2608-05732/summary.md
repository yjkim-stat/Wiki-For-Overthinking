<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# CircuitSteer: Geometrically Aligned Multi-Layer Steering via Sparse Autoencoder Circuits

- **Authors**: Mehrshad Saadatinia, Parsa Razmara, Ardalan Aryashad, Ali Abbasi, Seyedarmin Azizi
- **Venue**: cs.LG
- **Published**: 2026-08-06
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.05732>
- **PDF**: <https://arxiv.org/pdf/2608.05732v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.73

## In one line

Builds multi-layer steering vectors from SAE features selected by co-activation and decoder-direction alignment, and intervenes at several points instead of one.

## Problem

Steering methods such as Contrastive Activation Addition rely on fixed single-layer interventions derived from aggregate activation differences. One intervention is imposed across semantically diverse inputs, and the effect often fails to persist across layers, which limits how much behaviour actually changes.

## Contributions

- CircuitSteer: identification of multi-layer semantic subcircuits from SAE features
- A feature flow circuit built from feature co-activation plus geometric alignment of decoder directions
- Synthesis of dense steering vectors from sparse features, applied as multi-point interventions
- Evidence that multi-layer circuit steering preserves fluency where single-point methods do not, including on sycophancy and refusal where baselines fail entirely

## Method

CircuitSteer uses Sparse Autoencoders to find coherent semantic circuits distributed over multiple layers. A feature flow circuit is constructed from feature co-activation together with the geometric alignment of decoder directions — the alignment criterion is what links features across layers into a circuit rather than a set. The isolated multi-layer subcircuit's sparse features are then synthesized into dense steering vectors, applied as multi-point interventions to guide the model's internal semantic trajectory.

## Results

Evaluated with contrastive examples on toxicity, emotion-intensity, sycophancy and refusal across two model families. CircuitSteer is the only method to consistently produce fluency-preserving interventions; competing methods either sacrifice text quality or lack coverage, failing entirely on sycophancy and refusal.

## Limitations

No quantitative results in the abstract and the model families are not named. Behaviours tested are alignment-style attributes, not reasoning, so nothing is shown about steering a reasoning process. Requires a trained SAE for every layer involved, which bounds applicability to models with available SAEs. Fluency preservation is reported as a comparative claim without a stated metric.

## Why it matters here

- **reasoning-interpretability**: Extends the archive's SAE line from reading features to acting on them across layers, and supplies a selection criterion — decoder-direction alignment plus co-activation — for deciding which features form a circuit. The reported failure of single-layer baselines on sycophancy and refusal is the substantive finding: those are the behaviours that do not localize to one layer, which is indirect evidence about which computations are distributed. Nothing here is tested on reasoning, so whether a reasoning circuit is steerable the same way is open, and that gap is the obvious follow-up given the Step-Level SAE work already in the archive.

## Entities

- **Concepts**: sparse autoencoder, [monosemanticity](../../../../wiki/concepts/monosemanticity.md), circuit, [superposition](../../../../wiki/concepts/superposition.md), steering, feature co-activation, geometric alignment, [localization](../../../../wiki/concepts/localization.md)
- **Methods**: [sparse autoencoder](../../../../wiki/methods/sparse-autoencoder.md), [activation steering](../../../../wiki/methods/activation-steering.md), [Contrastive Activation Addition](../../../../wiki/methods/contrastive-activation-addition.md), [circuit discovery](../../../../wiki/methods/circuit-discovery.md), multi-point intervention
- **Datasets**: _none recorded_

Tags: `sparse autoencoder`, `steering`, `circuit`, `multi-layer`, `interpretability`

## Abstract

Controlling the behavior of large language models (LLMs) remains a critical challenge for AI alignment. Existing steering methods, such as Contrastive Activation Addition (CAA), typically rely on fixed single-layer interventions derived from aggregate activation differences. These methods impose a single intervention across semantically diverse inputs and often fail to sustain consistent behavioral changes across layers, limiting the effectiveness of the steering. In this work, we introduce CircuitSteer, a novel framework that leverages Sparse Autoencoders (SAEs) to identify and manipulate coherent semantic circuits distributed across multiple layers. By constructing a feature flow circuit based on feature co-activation and the geometric alignment of decoder directions, we isolate the specific multi-layer subcircuits responsible for a target behavior. We then synthesize dense steering vectors from these sparse features and apply multi-point interventions to guide the model's internal semantic trajectory. We evaluate CircuitSteer using contrastive examples across a diverse set of tasks, including toxicity, emotion-intensity, sycophancy, and refusal, spanning two model families. Across all models and datasets, CircuitSteer is the only method to consistently produce fluency-preserving interventions; competing methods either sacrifice text quality or lack coverage, failing entirely on complex behaviors like sycophancy and refusal. These results demonstrate that multi-layer circuit steering, enabled by enforcing geometric alignment among selected features, yields strictly more robust and effective behavioral control than static single-point interventions. Code is available at https://github.com/mehrshad-sdtn/CircuitSteer.

---

Record id: `arxiv:2608.05732`
