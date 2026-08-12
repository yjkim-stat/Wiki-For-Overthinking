<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning

- **Authors**: Hamed Damirchi, Imezadelajara, Ehsan Abbasnejad, Afshar Shamsi, Zhen Zhang 0008, Javen Qinfeng Shi
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.2073>
- **DOI**: 10.18653/V1/2026.ACL-LONG.2073
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.67

## In one line

Reads reasoning validity from layer-to-layer displacement of hidden states rather than from the states themselves, on the grounds that static activations let probes latch onto lexical surface patterns.

## Problem

Explainability methods treat hidden states as static points in activation space and assume correct and incorrect inferences separate at a single layer. But activations are saturated with polysemantic features, so linear probes learn surface-level lexical patterns instead of reasoning structure — the probe succeeds for the wrong reason.

## Contributions

- The argument that static-activation probing learns lexical surface patterns because activations are polysemantic
- Truth as a Trajectory: modelling inference as an unfolded trajectory and analyzing layer-wise geometric displacement
- A probe that uses only cross-layer changes, never the activations themselves
- Evaluation across dense and MoE architectures on commonsense reasoning, QA and toxicity detection
- Evidence that trajectory analysis outperforms conventional probing while reducing lexical confounds

## Method

Truth as a Trajectory models transformer inference as an unfolded trajectory of iterative refinements, moving analysis from static activations to layer-wise geometric displacement. Analyzing only displacement across layers, and never the activations themselves, is what removes the static lexical confound: a lexical feature present at every layer contributes nothing to the difference between layers.

## Results

Evaluated across dense and Mixture-of-Experts architectures on benchmarks spanning commonsense reasoning, question answering and toxicity detection. Using only changes in activations across layers and no access to the activations themselves, TaT mitigates reliance on static lexical confounds and outperforms conventional probing.

## Limitations

No numbers in the abstract and the models are not named. Displacement discards the originating state, which is exactly the trade-off arxiv:2608.05660 identifies and tries to repair by adding restricted location information — so this paper takes the position that paper argues is incomplete. Whether the residual signal is reasoning structure or a different confound is not established beyond the lexical case.

## Why it matters here

- **reasoning-interpretability**: Lands directly on a dispute this drain has now populated from both sides. This paper argues displacement is the right representation because it strips lexical confounds; arxiv:2608.05660, collected in the same drain, argues displacement alone is insufficient because it discards the originating state, and adds a quantized region plus a normalized direction to restore location without shortcuts. Both report gains over the same single-layer probing baseline, on different benchmarks, with no shared model — which is precisely the incomparability that doi:10.18653/v1/2026.acl-long.159 in this drain calls the field's auditing failure. The resolvable question is whether the location information the one paper adds is the lexical confound the other removes.

## Entities

- **Concepts**: [residual stream](../../../../wiki/concepts/residual-stream.md), [reasoning trajectory](../../../../wiki/concepts/reasoning-trajectory.md), [polysemanticity](../../../../wiki/concepts/polysemanticity.md), [superposition](../../../../wiki/concepts/superposition.md), linear probe, lexical confound, [localization](../../../../wiki/concepts/localization.md), [effective depth](../../../../wiki/concepts/effective-depth.md)
- **Methods**: Truth as a Trajectory, [linear probe](../../../../wiki/methods/linear-probe.md), layer-wise displacement analysis, [activation probing](../../../../wiki/methods/activation-probing.md)
- **Datasets**: _none recorded_

Tags: `probing`, `trajectory`, `residual stream`, `interpretability`, `lexical confound`

## Abstract

Existing explainability methods for Large Language Models (LLMs) typically treat hidden states as static points in activation space, assuming that correct and incorrect inferences can be separated using representations from an individual layer. However, these activations are saturated with polysemantic features, leading to linear probes learning surface-level lexical patterns rather than underlying reasoning structures. We introduce Truth as a Trajectory (TaT), which models the transformer inference as an unfolded trajectory of iterative refinements, shifting analysis from static activations to layer-wise geometric displacement. By analyzing displacement of representations across layers, TaT captures structural patterns in the evolution of inference that distinguish valid reasoning from spurious behavior. We evaluate TaT across dense and Mixture-of-Experts (MoE) architectures on benchmarks spanning commonsense reasoning, question answering, and toxicity detection. Without access to the activations themselves and using only changes in activations across layers, we show that TaT effectively mitigates reliance on static lexical confounds, outperforming conventional probing, and establishes trajectory analysis as a complementary perspective on LLM explainability.

---

Record id: `doi:10.18653/v1/2026.acl-long.2073`
