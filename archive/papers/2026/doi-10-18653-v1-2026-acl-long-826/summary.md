<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Your Reasoning Benchmark May Not Test Reasoning: Revealing Perception Bottleneck in Abstract Reasoning Benchmarks

- **Authors**: Xinhe Wang 0001, Jin Huang, Xingjian Zhang 0002, Tianhao Wang, Jiaqi W. Ma
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.826>
- **DOI**: 10.18653/V1/2026.ACL-LONG.826
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.67

## In one line

Separates perception from reasoning in ARC-style benchmarks with a two-stage pipeline, and finds about 80% of vision-language model failures are perception errors, not reasoning errors.

## Problem

ARC and ARC-AGI are read as probes of core fluid reasoning, and the gap between human and frontier vision-language model performance is commonly attributed to deficient machine reasoning. That attribution is untested: the tasks require seeing the grids before reasoning about them, so a perception failure is indistinguishable from a reasoning failure under end-to-end scoring.

## Contributions

- The hypothesis that the ARC-style human-model gap is primarily perceptual rather than inductive
- A two-stage pipeline that isolates reasoning from perception while preventing cross-image inductive leakage
- Evidence across Mini-ARC, ACRE and Bongard-LOGO that perception dominates the gap
- A manual trace analysis attributing approximately 80% of failures to perception errors
- The conclusion that ARC-style benchmarks conflate perception with reasoning

## Method

A two-stage pipeline explicitly separates the two. In the perception stage each image is independently converted into a natural-language description; in the reasoning stage a model induces and applies rules using only those descriptions. Converting each image independently is essential — it prevents leakage of cross-image inductive signal into the perception stage, so the reasoning stage is genuinely isolated from perception. Two-stage results are compared against standard end-to-end one-stage evaluation, and reasoning traces are manually inspected.

## Results

Across Mini-ARC, ACRE and Bongard-LOGO, perception capability is the dominant factor behind the observed performance gap. Manual inspection of VLM reasoning traces finds approximately 80% of model failures stem from perception errors. The authors conclude ARC-style benchmarks conflate perceptual and reasoning challenges and that observed gaps may overstate deficiencies in machine reasoning.

## Limitations

Three ARC-style datasets, so the conclusion is about this benchmark family. The perception stage's output is a natural-language description, so reasoning is evaluated over a lossy re-encoding — an upper bound on reasoning given perfect description is not the same as reasoning over the image. The 80% figure comes from manual inspection whose protocol, sample size and agreement are not given in the abstract. Models are not named.

## Why it matters here

- **reasoning-evaluation**: Directly attacks the interpretation of the benchmark family most often cited as evidence about machine reasoning. If 80% of failures are perceptual, then ARC-AGI scores are largely a vision measurement, and progress reported on them is not progress on reasoning. The methodological contribution is the leakage control: converting each image independently is what makes the isolation valid, and without it the perception stage could smuggle the induction. This is the fourth paper in one drain arguing a reasoning benchmark measures something else — with SMART on aggregation, VisAidMath on visual aids, CoRE on code execution — which is enough co-occurrence to treat construct validity as the drain's dominant theme rather than four separate findings.

## Entities

- **Concepts**: [construct validity](../../../../wiki/concepts/construct-validity.md), [perception bottleneck](../../../../wiki/concepts/perception-bottleneck.md), abstract reasoning, fluid reasoning, confounding, [meta-evaluation](../../../../wiki/concepts/meta-evaluation.md), information leakage
- **Methods**: two-stage perception-reasoning decomposition, manual trace analysis, end-to-end versus staged comparison
- **Datasets**: Mini-ARC, ACRE, Bongard-LOGO, ARC, [ARC-AGI](../../../../wiki/datasets/arc-agi.md)

Tags: `arc`, `construct validity`, `perception`, `vision-language models`, `benchmark critique`

## Abstract

Reasoning benchmarks such as the Abstraction and Reasoning Corpus (ARC) and ARC-AGI are widely used to assess progress in artificial intelligence and are often interpreted as probes of core, so-called “fluid” reasoning abilities. Despite their apparent simplicity for humans, these tasks remain challenging for frontier vision-language models (VLMs), a gap commonly attributed to deficiencies in machine reasoning. We challenge this interpretation and hypothesize that the gap arises primarily from limitations in visual perception rather than from shortcomings in inductive reasoning.To verify this hypothesis, we introduce a two-stage experimental pipeline that explicitly separates perception and reasoning. In the perception stage, each image is independently converted into a natural-language description, while in the reasoning stage a model induces and applies rules using these descriptions. This design prevents leakage of cross-image inductive signals and isolates reasoning from perception bottlenecks. Across three ARC-style datasets, Mini-ARC, ACRE, and Bongard-LOGO, we show that the perception capability is the dominant factor underlying the observed performance gap by comparing the two-stage pipeline with against standard end-to-end one-stage evaluation. Manual inspection of reasoning traces in the VLM outputs further reveals that approximately 80 percent of model failures stem from perception errors. Together, these results demonstrate that ARC-style benchmarks conflate perceptual and reasoning challenges and that observed performance gaps may overstate deficiencies in machine reasoning. Our findings underscore the need for evaluation protocols that disentangle perception from reasoning when assessing progress in machine intelligence.

---

Record id: `doi:10.18653/v1/2026.acl-long.826`
