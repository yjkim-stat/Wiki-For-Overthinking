<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# VisAidMath: Benchmarking Visual-Aided Mathematical Reasoning

- **Authors**: Jingkun Ma, Runzhe Zhan, Yang Li, Di Sun, Hou Pong Chan, Lidia S. Chao, Derek F. Wong
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.1719>
- **DOI**: 10.18653/V1/2026.ACL-LONG.1719
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.50

## In one line

Benchmarks whether multimodal models can construct visual aids for geometry problems, and finds high answer accuracy conceals near-total failure at producing or reasoning from those aids.

## Problem

Advancing from passive visual perception to actively modifying visual information in service of reasoning is a hallmark capability that remains underdeveloped in large multimodal models. The deficiency is masked by metrics that prioritize final-answer accuracy, creating an illusion of competence where genuine reasoning is absent.

## Contributions

- VisAidMath, a benchmark requiring construction of visual aids for geometric problem-solving
- The Three-Layered Funnel Evaluation Framework separating accuracy (ACCU), valid visual aid generation (PVA) and soundness of subsequent reasoning (SPRS)
- Identification of a 'Reasoning Illusion' where high accuracy coexists with failure to produce or use valid visual aids
- A public evaluation platform on CodaBench

## Method

Geometric problem-solving is used as a precise instrument, through tasks that require constructing visual aids. VisAidMath is the benchmark; the Three-Layered Funnel Evaluation Framework moves beyond accuracy (ACCU) to separately score the generation of valid visual aids (PVA) and the soundness of the subsequent reasoning steps (SPRS). Scoring the aid and the reasoning-from-aid separately is what makes the dissociation visible, since a model can reach the right answer without either.

## Results

Experiments on state-of-the-art models including Doubao-Seed-1.6 and o4 reveal a 'Reasoning Illusion': high surface-level accuracy conceals catastrophic failure in producing valid visual aids or reasoning from them. The authors describe this as a fundamental schism between visual perception and logical deduction in modern LMMs. A public evaluation platform is provided on CodaBench.

## Limitations

No numbers in the abstract, so 'catastrophic' is uncalibrated. Geometry with constructed visual aids is a narrow instrument, chosen for precision, and the schism claim is broader than that evidence. PVA and SPRS require judging validity and soundness, and how that judgement is made — human or model — is unstated, which matters because a model judge would inherit the deficiency being measured.

## Why it matters here

- **reasoning-evaluation**: Another instance of the drain's dominant finding, and one of its sharpest: the answer can be right while every intermediate artefact the answer supposedly depends on is wrong. Its layered funnel is a reusable design — score the artefact, then score reasoning from the artefact, then score the answer — and it applies wherever reasoning is supposed to route through an intermediate object. Read with long.826, which finds ARC-style failures are 80% perception rather than reasoning, the two make opposite-facing claims about the same perception/reasoning boundary: one says perception failure is misread as reasoning failure, the other says reasoning failure hides behind accuracy. Both agree the boundary is where the measurement breaks.

## Entities

- **Concepts**: [construct validity](../../../../wiki/concepts/construct-validity.md), reasoning illusion, visual perception, [multimodal reasoning](../../../../wiki/concepts/multimodal-reasoning.md), [process evaluation](../../../../wiki/concepts/process-evaluation.md), [meta-evaluation](../../../../wiki/concepts/meta-evaluation.md)
- **Methods**: VisAidMath, Three-Layered Funnel Evaluation Framework, process-level scoring
- **Datasets**: VisAidMath

Tags: `benchmark`, `multimodal`, `geometry`, `construct validity`, `visual aids`

## Abstract

A hallmark of advanced artificial intelligence is the capacity to progress from passive visual perception to the strategic modification of visual information to facilitate complex reasoning. This advanced capability, however, remains critically underdeveloped in current Large Multi-modal Models (LMMs). The deficiency is often masked by evaluation metrics that prioritize final-answer accuracy, creating an illusion of competence where genuine reasoning is absent. Using the domain of geometric problem-solving as a precise instrument, we probe this issue through tasks that require constructing visual aids.To this end, we introduce VisAidMath, a challenging benchmark, and our novel Three-Layered Funnel Evaluation Framework. This framework moves beyond simple accuracy (ACCU) to scrutinize the generation of valid visual aids (PVA) and the soundness of subsequent reasoning steps (SPRS). Our extensive experiments on state-of-the-art models, including Doubao-Seed-1.6 and o4, reveal a profound “Reasoning Illusion”. We observe that high surface-level accuracy conceals a catastrophic failure in the models’ ability to produce valid visual aids or to reason from them. Our findings expose a fundamental schism between visual perception and logical deduction in modern LMMs. We provide a public evaluation platform on CodaBench and release the project homepage.

---

Record id: `doi:10.18653/v1/2026.acl-long.1719`
