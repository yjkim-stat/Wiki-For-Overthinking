<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# CiPO: Counterfactual Unlearning for Large Reasoning Models through Iterative Preference Optimization

- **Authors**: Junyi Li, Yongqiang Chen, Ningning Ding
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.143>
- **DOI**: 10.18653/V1/2026.ACL-LONG.143
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.80

## In one line

Reframes unlearning in reasoning models as an intervention on the CoT itself, having the model generate logically valid counterfactual traces and iteratively preference-tuning toward them.

## Problem

Unlearning removes privacy-sensitive or copyrighted knowledge from language models. Reasoning models create a dilemma for it: existing methods either fail to eliminate the unwanted knowledge from the CoT traces, or they degrade reasoning performance by interfering with the reasoning process. Knowledge that survives in an intermediate step is not unlearned.

## Contributions

- A statement of the unlearning dilemma specific to reasoning models: knowledge surviving in CoT traces versus reasoning degradation
- CiPO, recasting unlearning as targeted intervention on the CoT via model-generated logically valid counterfactual traces
- An iterative preference-data update that increases divergence from the original model while keeping optimization smooth
- Reported removal from both intermediate steps and final answers with preserved reasoning ability

## Method

CiPO redefines unlearning as targeted intervention on the CoT. Given a desired unlearning target answer, it instructs the model to generate a logically valid counterfactual reasoning trace, which becomes the preferred side of a preference-tuning pair. As the model adjusts to the counterfactual trace, CiPO iteratively updates the preference data to increase divergence from the original model. Requiring the counterfactual trace to be logically valid is what keeps the reasoning process intact while the target knowledge is replaced — the model learns a different valid path, not a broken one.

## Results

On challenging benchmarks, CiPO removes knowledge from both intermediate CoT steps and the final answer while preserving the reasoning abilities of the models. No numbers or benchmark names are given in the abstract.

## Limitations

No quantitative results, benchmarks or models named in the abstract. 'Completely removing' knowledge is a strong claim that depends on the extraction attacks used to verify it, which are not described. Generating a counterfactual trace requires the model to be able to reason validly toward a false target, and how validity is checked is unstated. The iterative loop increases divergence from the original model, so the cost in unrelated capabilities is a risk the abstract addresses only as a general claim of preserved reasoning.

## Why it matters here

- **reasoning-training**: Useful to this topic less as an unlearning method than as evidence about where knowledge sits in a reasoning model: interventions on the final answer leave it recoverable from the intermediate steps, so the CoT is a second storage site that has to be edited separately. That is a structural fact about reasoning models the archive's memorization thread should hold. The counterfactual-trace construction is also a training signal of a kind not otherwise represented here — supervision toward a trace that is valid but counterfactual, which separates reasoning form from factual content.

## Entities

- **Concepts**: machine unlearning, counterfactual reasoning, chain of thought, [memorization](../../../../wiki/concepts/memorization.md), preference optimization, knowledge localization
- **Methods**: CiPO, iterative preference optimization, counterfactual trace generation, [machine unlearning](../../../../wiki/methods/machine-unlearning.md)
- **Datasets**: _none recorded_

Tags: `unlearning`, `counterfactual`, `preference optimization`, `chain of thought`, `memorization`

## Abstract

Machine unlearning has gained increasing attention in recent years, as a promising technique to selectively remove unwanted privacy or copyrighted information from Large Language Models that are trained on a massive scale of human data. However, the emergence of Large Reasoning Models (LRMs), which emphasize long chain-of-thought (CoT) reasoning to address complex questions, presents a dilemma to unlearning: existing methods either struggle to completely eliminate undesired knowledge from the CoT traces or degrade the reasoning performances due to the interference with the reasoning process. To this end, we introduce Counterfactual Unlearning through iterative Preference Optimization (CiPO), a novel framework that redefines unlearning as the targeted intervention of the CoT reasoning in LRMs. More specifically, given a desired unlearning target answer, CiPO instructs LRMs to generate a logically valid counterfactual reasoning trace for preference tuning. As the LRM adjusts to the counterfactual trace, CiPO iteratively updates the preference learning data to increase the discrepancy from the original model. This iterative loop ensures both desirable unlearning and smooth optimization, effectively mitigating the dilemma. Experiments on challenging benchmarks demonstrate that CiPO excels at unlearning, completely removing knowledge from both the intermediate CoT steps and the final answer, while preserving the reasoning abilities of LRMs.

---

Record id: `doi:10.18653/v1/2026.acl-long.143`
