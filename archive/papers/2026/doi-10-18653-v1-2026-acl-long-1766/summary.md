<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Think How to Think: Mitigating Overthinking with Autonomous Difficulty Cognition in Large Reasoning Models

- **Authors**: Yongjiang Liu, Haoxi Li, Xiaosong Ma, Jie Zhang 0076, Song Guo 0001
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.1766>
- **DOI**: 10.18653/V1/2026.ACL-LONG.1766
- **Topics**: reasoning-training, test-time-scaling
- **Relevance score**: reasoning-training 0.80, test-time-scaling 0.50

## In one line

Two-stage fine-tuning that first injects difficulty cues into output prefixes for prospective strategy selection, then injects redundancy cues mid-reasoning for retrospective correction.

## Problem

Reasoning models overthink, generating overly long redundant trajectories. Empirical analysis locates the cause: unlike humans, reasoning models are limited in recognizing task properties such as difficulty before solving a problem, so they apply one reasoning strategy regardless of the problem.

## Contributions

- An empirical diagnosis that reasoning models fail to recognize task difficulty before solving, producing one-size-fits-all reasoning
- TH2T, a two-stage fine-tuning strategy building difficulty cognition then redundancy cognition
- Difficulty Hypnosis in output prefixes as prospective global strategy cues
- Redundancy Hypnosis in in-progress steps as retrospective local correction signals
- Over 70% inference cost reduction on easy tasks and 40% on complex ones across 7B/14B/32B

## Method

TH2T is a two-stage fine-tuning strategy that progressively builds difficulty cognition and redundancy cognition. Stage one injects 'Difficulty Hypnosis' into output prefixes as cues for global, prospective strategy selection, sharpening sensitivity to task complexity and adaptive control of reasoning depth. Stage two incorporates 'Redundancy Hypnosis' into in-progress reasoning steps as local, retrospective signals for behaviour correction, identifying and eliminating superfluous detours. The prefix/in-progress split maps onto prospective versus retrospective control: one decides depth before starting, the other prunes while running.

## Results

Across 7B/14B/32B models, TH2T reduces inference cost by over 70% on easy tasks and 40% on complex ones without compromising performance. The resulting models show a nascent ability for difficulty-aware reasoning and reduced excessive reflection and looping.

## Limitations

'Without compromising performance' is unquantified, and no accuracy numbers or benchmark names appear in the abstract. Difficulty labels are needed to construct the prefix cues, and how they are obtained determines whether the learned sensitivity is to difficulty or to a proxy. The asymmetric savings — over 70% on easy versus 40% on complex — mean the aggregate reduction depends on the difficulty mix of the evaluation set, which is unstated.

## Why it matters here

- **reasoning-training**: Belongs to the archive's difficulty-allocation cluster and separates a distinction the rest of it blurs: deciding how much to think before starting versus cutting redundancy while running are different control problems, and this paper trains them in separate stages. Compare doi:10.18653/v1/2026.acl-industry.152 in the same batch, which reads difficulty from the model's own confidence instead of injecting it as a cue — same target, opposite information source, and no shared evaluation between them.
- **test-time-scaling**: The measured allocation is what this topic wants: over 70% saved on easy problems against 40% on hard ones, which is the shape a correct difficulty-aware allocator should produce. It is trained-in rather than decided at inference, so it is a fixed policy rather than an adaptive one, and that makes it the fine-tuning counterpart to the inference-time stopping-signal family tracked here.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), [prompt difficulty](../../../../wiki/concepts/prompt-difficulty.md), [adaptive compute allocation](../../../../wiki/concepts/adaptive-compute-allocation.md), [reasoning redundancy](../../../../wiki/concepts/reasoning-redundancy.md), [metacognition](../../../../wiki/concepts/metacognition.md), prospective versus retrospective control, looping
- **Methods**: TH2T, two-stage fine-tuning, prefix injection, difficulty estimation
- **Datasets**: _none recorded_

Tags: `overthinking`, `difficulty`, `two-stage fine-tuning`, `adaptive compute`, `efficient reasoning`

## Abstract

Recent Large Reasoning Models (LRMs) excel at complex reasoning tasks but often suffer from overthinking, generating overly long and redundant reasoning trajectories. To explore its essence, our empirical analysis reveals that LRMs are primarily limited to recognizing task properties (i.e., difficulty levels) like humans before solving the problem, leading to a one-size-fits-all reasoning strategy. This observation motivates a fundamental question: Can we explicitly bootstrap such ability to alleviate overthinking in LRMs? To this end, we propose Think-How-to-Think (TH2T), a novel two-stage fine-tuning strategy that progressively inspires LRMs’ difficulty cognition and redundancy cognition of LRMs. Specifically, we first inject Difficulty Dypnosis into output prefixes as cues for global, prospective reasoning strategy selection, stimulating the model’s sharper sensitivity to task complexity and adaptive control of reasoning depth. Then, we incorporate Redundancy Hypnosis into in-progress reasoning steps, which serve as local, retrospective signals for behavior correction by identifying and eliminating superfluous reasoning detours. Experiments across 7B/14B/32B models demonstrate that TH2T significantly reduces inference costs by over 70% on easy tasks and 40% on complex ones without compromising performance. The resultant models exhibit a nascent ability for difficulty-aware reasoning, effectively mitigating behaviors like excessive reflection and looping, thereby paving the way for more cognitively efficient LRMs.

---

Record id: `doi:10.18653/v1/2026.acl-long.1766`
