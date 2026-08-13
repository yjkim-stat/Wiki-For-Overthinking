<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# SciVQR: A Multidisciplinary Multimodal Benchmark for Advanced Scientific Reasoning Evaluation

- **Authors**: Longteng Guo, Xuanxu Lin, Dongze Hao, Tongtian Yue, Pengkang Huo, Jiatong Ma, Yuchen Liu, Jing Liu 0001
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.findings-acl.28>
- **DOI**: 10.18653/V1/2026.FINDINGS-ACL.28
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.50

## In one line

A multimodal scientific reasoning benchmark over 54 subfields with domain-specific visuals and expert solutions for 46% of items, scoring the reasoning process as well as the answer.

## Problem

Scientific reasoning requires integrating multimodal inputs, domain expertise and multi-step inference across subjects. Existing multimodal benchmarks do not capture the complexity or the traceability of the reasoning processes needed for rigorous evaluation.

## Contributions

- SciVQR, a multimodal scientific reasoning benchmark spanning 54 subfields in six disciplines
- Domain-specific visuals including equations, charts and diagrams requiring joint visual and reasoning competence
- A difficulty range from factual recall to multi-step inference
- Expert-authored solutions for 46% of items enabling reasoning-process evaluation
- Evaluation of leading proprietary and open-source multimodal LLMs, with dataset and code released

## Method

SciVQR covers 54 subfields across mathematics, physics, chemistry, geography, astronomy and biology, with domain-specific visuals — equations, charts, diagrams — requiring visual comprehension to be combined with reasoning. Tasks range from basic factual recall to complex multi-step inference, and 46% include expert-authored solutions, which is what makes process evaluation possible rather than only answer checking. Both final answers and the reasoning process are evaluated.

## Results

Evaluation of leading proprietary and open-source multimodal LLMs reveals significant limitations on complex multimodal reasoning tasks, indicating a need for better multi-step reasoning and interdisciplinary knowledge integration. No numbers or model names are given in the abstract.

## Limitations

No quantitative results or named models in the abstract. Expert solutions cover 46% of items, so process evaluation is available on under half the benchmark. 54 subfields across six disciplines implies few items per subfield, limiting per-subfield conclusions. How the reasoning process is scored — by human experts or a model judge — is not stated, which determines how much weight the process claims carry.

## Why it matters here

- **reasoning-evaluation**: Adds breadth the archive lacks — the collection is dominated by competition mathematics, and 54 scientific subfields with domain visuals is a different distribution. The design choice worth recording is that expert-authored solutions are what license process evaluation, and this benchmark has them for only 46% of items, which is an honest statement of the real constraint: scoring reasoning rather than answers requires reference reasoning, and that is expensive enough that even a benchmark built for it covers under half. That cost is why so much of the field scores final answers, and it makes the 46% figure more informative than the headline result.

## Entities

- **Concepts**: [multimodal reasoning](../../../../wiki/concepts/multimodal-reasoning.md), scientific reasoning, process evaluation, [traceability](../../../../wiki/concepts/traceability.md), domain expertise, multi-step inference
- **Methods**: SciVQR, process-level evaluation, expert-authored reference solutions
- **Datasets**: SciVQR

Tags: `benchmark`, `multimodal`, `scientific reasoning`, `process evaluation`

## Abstract

Scientific reasoning is a key aspect of human intelligence, requiring the integration of multimodal inputs, domain expertise, and multi-step inference across various subjects. Existing benchmarks for multimodal large language models (MLLMs) often fail to capture the complexity and traceability of reasoning processes necessary for rigorous evaluation. To fill this gap, we introduce SciVQR, a multimodal benchmark covering 54 subfields in mathematics, physics, chemistry, geography, astronomy, and biology. SciVQR includes domain-specific visuals, such as equations, charts, and diagrams, and challenges models to combine visual comprehension with reasoning. The tasks range from basic factual recall to complex, multi-step inferences, with 46% including expert-authored solutions. SciVQR not only evaluates final answers but also examines the reasoning process, providing insights into how models reach their conclusions. Our evaluation of leading MLLMs, including both proprietary and open-source models, reveals significant limitations in handling complex multimodal reasoning tasks, underscoring the need for improved multi-step reasoning and better integration of interdisciplinary knowledge in advancing MLLMs toward true scientific intelligence. The dataset and evaluation code are publicly available at https://github.com/CASIA-IVA-Lab/SciVQR.

---

Record id: `doi:10.18653/v1/2026.findings-acl.28`
