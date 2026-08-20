<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models

- **Authors**: Hengyuan Zhang, Zhihao Zhang 0002, Ercong Nie, Mingyang Wang 0003, Zunhai Su, Yiwei Wang, Qianli Wang, Shuzhou Yuan, Xufeng Duan, Qibo Xue, Zeping Yu, Chenming Shang, Xiao Liang, Jing Xiong, Hui Shen 0008, Chaofan Tao, Zhengwu Liu, Senjie Jin, Zhiheng Xi, Dongdong Zhang, Sophia Ananiadou, Tao Gui, Ruobing Xie, Hayden Kwok-Hay So, Hinrich Schütze, Xuanjing Huang 0001, Qi Zhang 0001, Ngai Wong 0001
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.findings-acl.502>
- **DOI**: 10.18653/V1/2026.FINDINGS-ACL.502
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.50

## In one line

A survey reorganizing mechanistic interpretability from observation into a Locate-Steer-Improve intervention pipeline, categorized by the interpretable object being acted on.

## Problem

Existing reviews treat mechanistic interpretability as an observational science, summarizing analytical insights without a systematic framework for actionable intervention — so findings do not translate into changes to models.

## Contributions

- A reframing of mechanistic interpretability from observational science to an actionable Locate-Steer-Improve pipeline
- Formal categorization of localizing and steering methods by the interpretable object they target
- A demonstration of how the framework maps onto improvements in alignment, capability and efficiency
- A curated paper list

## Method

A practical survey structured around a Locate, Steer, Improve pipeline. Localizing methods (diagnosis) and Steering methods (intervention) are formally categorized by the specific Interpretable Object they act on, which is what turns a method list into an intervention protocol. The framework is then used to show how interpretability yields improvements in Alignment, Capability and Efficiency.

## Results

A survey; it contributes a framework and a curated paper list rather than empirical results.

## Limitations

No empirical contribution, and no stated selection criteria or coverage for the surveyed work, so it is not a systematic review. Organizing by interpretable object presumes those objects are well defined, which is contested — the run-to-run inconsistency in doi:10.18653/v1/2026.acl-long.99 in this same drain shows SAE features are not stable across seeds. Claims that the framework enables improvements in alignment, capability and efficiency are organizational rather than measured.

## Why it matters here

- **reasoning-interpretability**: Useful to this archive as an organizing check rather than a finding, and it is the second survey of this field in one drain — doi:10.18653/v1/2026.acl-long.889 organizes the same area by training dynamics, mechanisms and failures, while this one organizes it by intervention. Two incompatible taxonomies of one field arriving together is itself the state of the field. The locate-then-steer framing does match the archive's own trajectory, where SAE work has moved from reading features to steering them, and its weak point is named by its neighbour acl-long.99: an intervention protocol indexed by interpretable objects assumes those objects are stable across training runs, which they are not by default.

## Entities

- **Concepts**: mechanistic interpretability, [localization](../../../../wiki/concepts/localization.md), steering, actionable interpretability, intervention protocol, interpretable object
- **Methods**: [literature survey](../../../../wiki/methods/literature-survey.md), [activation steering](../../../../wiki/methods/activation-steering.md), localization methods
- **Datasets**: _none recorded_

Tags: `survey`, `interpretability`, `steering`, `framework`, `actionable`

## Abstract

Mechanistic Interpretability (MI) has emerged as a vital approach to demystify the opaque decision-making of Large Language Models (LLMs). However, existing reviews primarily treat MI as an observational science, summarizing analytical insights while lacking a systematic framework for actionable intervention. To bridge this gap, we present a practical survey structured around the pipeline: “Locate, Steer, and Improve.” We formally categorize Localizing (diagnosis) and Steering (intervention) methods based on specific Interpretable Objects to establish a rigorous intervention protocol. Furthermore, we demonstrate how this framework enables tangible improvements in Alignment, Capability, and Efficiency, effectively operationalizing MI as a practical engineering toolkit for model optimization. The curated paper list of this work is available at https://anonymous.4open.science/r/Act-MI-F068.

---

Record id: `doi:10.18653/v1/2026.findings-acl.502`
