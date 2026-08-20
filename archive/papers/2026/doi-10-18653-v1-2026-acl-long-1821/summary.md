<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Mitigating Safety Context Amnesia in Multimodal Reasoning Models via Intent-Guided Safety Reasoning

- **Authors**: Xiyao Dong, Guangsheng Cheng, YiLong Chen, Xiaojin Zhang, Kun He
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.1821>
- **DOI**: 10.18653/V1/2026.ACL-LONG.1821
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.67

## In one line

Identifies a multimodal failure where models see the risky visual cue but let narrative coherence override safety as reasoning proceeds, and defends against it by extracting intent before generation.

## Problem

Multimodal reasoning models perform explicit CoT across vision and language, and the reasoning process itself introduces a vulnerability. Harmful objectives embedded in ostensibly benign contexts lead models to over-prioritize narrative coherence: they correctly perceive risk-relevant visual cues yet fail to enforce safety constraints once reasoning becomes dominated by contextual alignment. The paper names this Safety Context Amnesia.

## Contributions

- Identification and naming of Safety Context Amnesia: correct perception of risk cues followed by safety failure as contextual alignment dominates reasoning
- IGSR, a parameter-free inference-time defence
- A Perception Decoupler that extracts visual evidence into a structured intent representation separated from narrative context
- A Cognitive Arbiter enforcing explicit safety constraints before generation
- Over 62% improvement in defence success rate across multiple multimodal safety benchmarks

## Method

Intent-Guided Safety Reasoning is an inference-time defence requiring no change to target model parameters. A Perception Decoupler extracts objective visual evidence into a structured intent output, separating what is seen from the narrative it is embedded in — which is the step that prevents context from absorbing the cue. A Cognitive Arbiter then enforces explicit safety constraints before generation.

## Results

Across multiple multimodal safety benchmarks, IGSR improves defence success rates by over 62% compared to baselines while largely preserving task utility.

## Limitations

'Over 62%' is a relative improvement whose baseline is unstated, and 'largely preserving task utility' is unquantified. Benchmarks and models are not named in the abstract. Two extra inference stages add cost that is not reported. As an inference-time wrapper it does not change the underlying tendency, so the failure mode remains present in the model.

## Why it matters here

- **reasoning-training**: Its finding for this topic is positional and matches a pattern the archive is accumulating: the model has the right information early and loses it during reasoning. That is the same shape as the Self-Jailbreak result in doi:10.18653/v1/2026.findings-acl.1118 and the reasoning-answer hit gap in findings-acl.204 — harm or error enters mid-trajectory rather than at input or output. Three independent papers in one drain locating failure in the middle of the trace is a stronger claim than any of them alone, and it argues against trajectory-uniform safety training.

## Entities

- **Concepts**: safety context amnesia, [multimodal reasoning](../../../../wiki/concepts/multimodal-reasoning.md), narrative coherence, inference-time intervention, perception versus reasoning, [jailbreak](../../../../wiki/concepts/jailbreak.md)
- **Methods**: Intent-Guided Safety Reasoning, perception decoupling, chain of thought
- **Datasets**: _none recorded_

Tags: `multimodal`, `safety`, `inference-time defense`, `perception`, `chain of thought`

## Abstract

Recent advances in Multimodal Large Reasoning Models (MLRMs) have enabled explicit chain-of-thought inference across vision and language, substantially improving performance on complex reasoning tasks. Despite these gains, the reasoning process introduces a subtle yet critical vulnerability. We identify an un-derexplored multimodal safety failure mode in which harmful objectives are embedded within ostensibly benign contexts, leading models to over-prioritize narrative coherence during reasoning. We term this phenomenon Safety Con-text Amnesia (SCA), wherein models correctly perceive risk-relevant visual cues but fail to enforce safety constraints as the reasoning process becomes dominated by contextual alignment. To mitigate SCA, we propose Intent-Guided Safety Reasoning (IGSR), an inference-time defense that operates without modifying target model parameters. IGSR employs a Perception Decoupler to extract objective visual evidence into a structured intent output, followed by a Cognitive Arbiter that enforces explicit safety constraints prior to generation. Extensive experiments across multiple multimodal safety benchmarks demonstrate that IGSR improves defense success rates by over 62% compared to baselines, while largely preserving task utility. These results highlight the critical role of structured, intent-aware reasoning in achieving robust safety reasoning for multi-modal reasoning models. Warning: This paper contains unsafe examples.

---

Record id: `doi:10.18653/v1/2026.acl-long.1821`
