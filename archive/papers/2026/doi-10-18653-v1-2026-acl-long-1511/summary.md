<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Quantifying and Understanding Uncertainty in Large Reasoning Models

- **Authors**: Yangyi Li, Chenxu Zhao, Mengdi Huai
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.1511>
- **DOI**: 10.18653/V1/2026.ACL-LONG.1511
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.80

## In one line

Applies conformal prediction to the joint reasoning-answer structure of reasoning models, then attributes coverage to specific training examples and reasoning steps with Shapley values.

## Problem

Quantifying generation uncertainty in reasoning models matters, but traditional methods give no finite-sample guarantees for reasoning-answer generation. Conformal prediction is model-agnostic and statistically rigorous, yet existing CP methods ignore the logical connection between the reasoning trace and the final answer. Separately, prior work does not explain where coverage comes from, because it overlooks the training factors that drive valid reasoning, and reasoning quality is hard to disentangle from answer correctness.

## Contributions

- A conformal method giving finite-sample uncertainty guarantees over the joint reasoning-answer structure rather than the answer alone
- An example-to-step explanation framework using Shapley values that identifies a provably sufficient subset of training data and reasoning steps for coverage
- Theoretical analysis for both the uncertainty and the explanation methods

## Method

A conformal method that provides uncertainty over the reasoning-answer structure with statistical guarantees, rather than over the answer alone. On top of it, a unified example-to-step explanation framework using Shapley values identifies a provably sufficient subset of training data and the specific reasoning steps within it that suffice to achieve coverage. Theoretical analysis is given for both parts.

## Results

Extensive experiments on challenging reasoning datasets verify the effectiveness of both methods. No numbers, datasets or models are named in the abstract.

## Limitations

No quantitative results, datasets or models in the abstract. Conformal guarantees are exchangeability-dependent, and the abstract does not state the calibration setup or how exchangeability is argued for reasoning traces. Shapley attribution over training examples is expensive, and the abstract claims efficiency without stating the cost. Coverage over a reasoning-answer structure requires a notion of an admissible trace, whose definition governs what the guarantee means.

## Why it matters here

- **reasoning-training**: The one paper in this drain that offers a finite-sample statistical guarantee, and it puts the guarantee on the trace-and-answer pair rather than the answer, which is the coupling the archive's faithfulness thread keeps finding broken. Its second half is more unusual: attributing coverage back to specific training examples and specific reasoning steps within them is a training-signal question answered with an attribution method, which is a route to 'which supervision produced valid reasoning' that no other paper here takes. Both claims rest on theory the abstract does not expose, so this one needs a full read before the archive relies on it.

## Entities

- **Concepts**: conformal prediction, [uncertainty quantification](../../../../wiki/concepts/uncertainty-quantification.md), [calibration](../../../../wiki/concepts/calibration.md), coverage guarantee, [Shapley value](../../../../wiki/concepts/shapley-value.md), training data attribution, reasoning-answer coupling
- **Methods**: conformal prediction, Shapley values, training data attribution, uncertainty set construction
- **Datasets**: _none recorded_

Tags: `conformal prediction`, `uncertainty`, `shapley`, `attribution`, `guarantees`

## Abstract

Large Reasoning Models (LRMs) have recently demonstrated significant improvements in complex reasoning. While quantifying generation uncertainty in LRMs is crucial, traditional methods are often insufficient because they do not provide finite-sample guarantees for reasoning-answer generation. Conformal prediction (CP) stands out as a model-agnostic methodology that constructs statistically rigorous uncertainty sets. However, existing CP methods ignore the logical connection between the reasoning trace and the final answer. Additionally, prior studies fail to interpret the origins of uncertainty coverage for LRMs as they typically overlook the specific training factors driving valid reasoning. Notably, it is challenging to disentangle reasoning quality from answer correctness, while simultaneously establishing theoretical guarantees for computationally efficient explanation methods. To address these challenges, we first propose a novel methodology that provides the uncertainty of the reasoning-answer structure with statistical guarantees. Subsequently, we develop a unified example-to-step explanation framework using Shapley values that identifies a provably sufficient subset of training data and their specific reasoning steps sufficient to achieve coverage. We also provide the theoretical analysis for our proposed methods. Extensive experiments on challenging reasoning datasets verify the effectiveness of the proposed methods.

---

Record id: `doi:10.18653/v1/2026.acl-long.1511`
