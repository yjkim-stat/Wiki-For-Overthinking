<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Test-Time Scaling in the Wild: Why Exploitation, Not Exploration, Is the Bottleneck

- **Authors**: Davide Romano, Kanak Raj, Jerrod Parker, Daniele Giofrè
- **Venue**: cs.CL
- **Published**: 2026-08-19
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.18931>
- **PDF**: <https://arxiv.org/pdf/2608.18931v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

A compute-normalised, five-benchmark comparison of test-time scaling methods on open-ended generation finds that the candidate pool improves steadily with compute, but exploitation - selecting or synthesising the final answer from that pool - is the bottleneck, with reward-model-based selection near random (verifier correlation ~0.12) and even the best method (Fusion) recovering only ~40% of available quality.

## Problem

Test-time scaling techniques (best-of-N, tree search, refinement) have been developed and validated almost exclusively on tasks with straightforward automatic verification (math, code), leaving open whether their gains hold on open-ended generation tasks (medicine, law, finance, general chat, creative writing) where verification is rubric-based rather than exact-match, and whether the mechanism of failure, when it occurs, is due to insufficiently diverse/high-quality candidate generation (exploration) or to poor selection/synthesis from an already-good pool (exploitation).

## Contributions

- First compute-normalised, systematic comparison of five test-time scaling (TTS) families (Best-of-N, Beam Search, Particle Filter, Sequential Refinement, Fusion) across five open-ended generation benchmarks (HealthBench, PRBench, LEXam, WildBench, WritingBench).
- Introduces a unified framework decomposing a TTS method's token budget effect into exploration headroom (oracle quality minus single-sample quality) and net exploitation effect (realised quality minus oracle quality), with a headroom-capture metric h = (Q(T)-mu)/(Q*(T)-mu).
- Derives and empirically validates that headroom capture for Best-of-N approximately equals the verifier's correlation with true quality (h^BoN ~ rho_v), confirmed by a regression slope of 1.198 (R^2=0.66, rho=0.81, p<1e-36) across 152 (generator, RM, benchmark) combinations.
- Provides a bias-corrected oracle estimator that corrects for judge-noise inflation in naive max-over-pool oracle estimates.
- Shows Fusion (synthesis across candidates) is the only method that consistently improves over single-sample baselines across all five benchmarks, though it still captures only ~40% of available headroom.

## Method

The paper formalises test-time scaling methods as partitioning a fixed token budget T into exploration tokens (generating a candidate pool) and exploitation tokens (converting the pool into a final answer), and defines oracle quality Q*(T) (expected score of the best candidate in the pool under a ground-truth verifier) versus realised quality Q(T) (expected score of the method's actual output). Headroom capture h = (Q(T)-mu)/(Q*(T)-mu) measures what fraction of available exploration headroom a method's exploitation step converts into real gains. Five TTS families are implemented at matched compute across four budget levels (Low/Mid/High/XHigh): Best-of-N with two external outcome reward models, Beam Search and Particle Filtering both guided by a process reward model (VersaPRM-8B), Sequential Refinement (iterative self-critique and rewrite with a bounded history window), and Fusion (single-shot synthesis of a final answer from a random subset of independently generated candidates). Generators are Qwen3.5 (9B, 35B-A3B) and OLMo3 (7B-Think, 32B-Think); an LLM judge (Qwen3.5-397B-A17B) scores all outputs, and a bias-corrected closed-form oracle estimator removes the inflation caused by taking the max of noisy judge scores over a pool.

## Results

For Qwen3.5-35B-A3B (compute-normalised, XHigh budget): Fusion reaches 0.610 overall score vs 0.574 single-sample baseline and 0.584 for the best BoN reward model; BoN captures only ~15% of exploration headroom (verifier correlation rho_v ~0.12, both tested ORMs near-identical), while Fusion captures ~40%. Sequential Refinement is inconsistent: -2.3pp on HealthBench, -4.5pp on LEXam, but +7.3pp on WritingBench and better than Fusion on PRBench (0.342 vs 0.331); WritingBench and WildBench gains are confounded by verbosity bias / a single subtask (Coding & Debugging) respectively. Particle Filtering shows the least output diversity (mean pairwise cosine distance 0.036-0.069 vs 0.123-0.124 for BoN) and headroom capture averaging around -40%, i.e. actively degrading quality. Regressing headroom capture on verifier correlation across 152 (generator, RM, benchmark) combinations gives slope 1.198, intercept -0.011, R^2=0.66, rho=0.81 (p<1e-36), confirming h^BoN ~ rho_v. On MATH-500 and GPQA Diamond (deterministic tasks, reported for contrast), the same generators gain only ~2pp from test-time scaling. Findings hold qualitatively across model scales (9B, 35B-A3B Qwen3.5) and across the Qwen3.5 vs OLMo3 model families, though OLMo3 shows negative headroom capture under Fusion on two of three benchmarks tested.

## Limitations

Conclusions rest on two generator model families (Qwen3.5 and OLMo3) and a single unified LLM judge (Qwen3.5-397B-A17B), not the benchmarks' native judges, though judge agreement was validated against native judges on 5-15% stratified samples (e.g. HealthBench Macro F1 0.679, PRBench criterion-level kappa 0.679, WildBench QWK 0.564, WritingBench per-pair agreement 0.408). The oracle estimator assumes i.i.d. candidates, which is exact for BoN but only approximate for Refinement, Fusion, and Particle Filtering; the authors expect it to slightly underestimate the true oracle for the first two and slightly overestimate it for Particle Filtering. Sequential Refinement's apparent gain on WritingBench is confounded by the benchmark's judge having a stronger length-score correlation (rho=+0.33 for SR vs +0.20 for BoN) than other benchmarks, i.e. a verbosity bias in that specific benchmark's evaluation design. Results do not cover all open-ended use cases and the authors note deploying TTS in high-stakes domains without human oversight remains inadvisable.

## Why it matters here

- **overthinking**: Directly studies test-time compute scaling, a core sub-topic of overthinking: it shows that spending more inference compute on generating candidates (exploration) reliably raises oracle quality, but that most TTS methods fail to convert this into better realised output because exploitation (reward-model selection, tree-search pruning) is unreliable - meaning additional test-time compute is frequently wasted or even actively harmful (e.g. Particle Filtering averages around -40% headroom capture, i.e. compute that hurts performance) rather than yielding proportional accuracy gains. This is direct evidence for where and why more test-time compute does not translate into better answers, informing the accuracy/efficiency tradeoff and where methods to 'know when to stop' scaling would need to intervene.

## Entities

- **Concepts**: exploration-exploitation decomposition of test-time compute budget, oracle quality vs realised quality, headroom capture, verifier correlation as predictor of selection failure, diversity collapse in tree search
- **Methods**: Best-of-N (BoN) with outcome reward models (Skywork-Reward-V2, Llama-3.1-70B-Instruct-RM-RB2), Beam Search (PRM-guided), Particle Filtering (PRM-guided stochastic resampling), Sequential Refinement (iterative self-critique and rewrite), Fusion (generative synthesis across candidates), Budget Forcing (extended single-trajectory thinking), Bias-corrected oracle quality estimator
- **Datasets**: LEXam (516 items, legal reasoning), HealthBench (5,000 items, medicine), PRBench (1,650 items, finance/legal, ScaleAI), WildBench v2 (1,024 items, general chat), WritingBench (555 English items, creative/professional writing), MATH-500 and GPQA Diamond (referenced for contrast with deterministic tasks)

Tags: `test-time-scaling`, `exploration-exploitation`, `best-of-n`, `reward-model`, `open-ended-generation`, `tree-search`, `sequential-refinement`, `fusion`, `overthinking`

## Abstract

Test-time scaling (TTS) improves language model outputs by spending additional inference compute - generating multiple candidates, searching over partial sequences, or iteratively refining drafts. These techniques yield large gains on mathematics and code, but have been developed and stress-tested almost exclusively on tasks where verification is straightforward. We conduct the first compute-normalised comparison of five TTS families across five open-ended generation benchmarks spanning medicine, law, finance, general chat, and creative writing - grounded in a unified framework that decomposes the effectiveness of each method's token budget into exploration and exploitation. The answer depends on which side of that decomposition you examine. Scaling exploration works: the best candidate in the pool improves steadily with compute across all settings. What breaks is exploitation - the step that converts a rich candidate pool into a final output. With state-of-the-art generators, reward models correlate at only $ρ_v \approx 0.12$ with true quality, rendering selection near-random regardless of budget. Tree search amplifies this failure through diversity collapse. Refinement helps on one of five benchmarks; its apparent gains elsewhere are confounded. Only synthesis across candidates (Fusion) consistently improves over single-sample baselines, yet still recovers only ~40% of available quality. The candidate pool is not the bottleneck - choosing from it is.

---

Record id: `arxiv:2608.18931`
