<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Claim-Level Reliability Assessment for Efficient Test-Time Reasoning

- **Authors**: Sen Xu, Wei Wang, Shixi Liu, Jixin Min, Yingwei Dai, Zhibin Yin, Yirong Chen, Junlin Zhang
- **Venue**: cs.AI
- **Published**: 2026-08-12
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.11994>
- **PDF**: <https://arxiv.org/pdf/2608.11994v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## In one line

CLR reallocates part of the test-time compute budget from generating more solution samples to falsifying a small set of decision-critical claims extracted from each trace, improving accuracy over self-consistency while using fewer tokens on some models.

## Problem

Whole-trace reliability signals (token probabilities, entropy, hidden states, or majority voting over full traces) dilute the discriminative signal needed to catch a single decisive logical flaw buried in an otherwise plausible long reasoning trace, so scaling up sampling or evaluation compute does not reliably translate into more trustworthy answers.

## Contributions

- Proposes claim-level falsification as a test-time-scaling principle: condense each reasoning trace into a compact set of decision-critical claims and verify them rather than evaluating the whole trace
- Instantiates it as Claim-Level Reliability Assessment (CLR), a training-free two-stage framework (solution+claim generation, then claim-level falsification) that reweights self-consistency votes by a nonlinear per-trace reliability score
- Shows CLR improves accuracy over pass@1 and self-consistency (Cons@K) under matched model-call or matched-token budgets across four LLMs and four reasoning benchmarks, in some regimes with fewer generated tokens than baseline self-consistency
- Quantifies a 'rescue rate' showing CLR overturns 16-48% (avg ~37%) of cases where self-consistency's majority vote is wrong despite a correct candidate being present among sampled traces

## Method

CLR runs a two-stage inference pipeline per problem. Stage 1 samples K solution traces from the model; each trace's response is prompted to end with the final boxed answer followed by exactly M decision-critical claims (intermediate mathematical statements whose failure would undermine the final answer, excluding restatements or trivial steps). Stage 2 reuses the same model as a 'rigorous verifier': for each trace it receives only the problem and that trace's M claims (not the original trace or prediction) and is prompted to actively search for a decisive contradiction, counterexample, logical/factual error, or unjustified inference for each claim, returning a binary VALID/REFUTED verdict per claim. Each trace's reliability score is r_k = (mean fraction of claims not refuted)^M, a nonlinear function that increasingly penalizes traces as more claims are refuted. Predictions are grouped into equivalence classes by final answer, each group's support is the sum of its traces' reliability scores, and the group with maximum total support is selected as the final answer (reducing to plain self-consistency/majority-vote when all traces score equally). One full CLR@K flow costs K solution-generation calls plus K claim-verification calls, matching the call budget of Cons@2K.

## Results

Table 1 (matched 64 model calls, CLR@32 vs Cons@64): Gemma-4-12B-it improves accuracy by +7.12 to +12.08 percentage points across four benchmarks (e.g. HMMT25: 76.67% to 88.75%) but uses 22.2-47.8% more tokens. GPT-OSS-20B improves in three of four benchmarks while using 36.3-39.8% fewer tokens on every benchmark (CMIMC25: 77.50% to 82.19%, -37.0% tokens; HMMT25 the one regression: 80.00% to 79.58%, -36.3% tokens). GPT-OSS-120B improves accuracy by up to +5.00pp while reducing tokens 21.6-23.7%. Qwen3.5-27B (near-saturated baseline, Cons@64 already >90% on 3/4 benchmarks) sees smaller gains up to +2.60pp with token reduction up to 14.5%. Stage-2 decomposition on GPT-OSS-20B (Table 2) shows the claim prompt alone (Stage-1-only, unweighted) slightly reduces single-rollout accuracy relative to regular sampling (-0.65 to -4.56pp), while adding Stage-2 falsification-based reweighting over the same 32 candidates adds +4.48 to +7.01pp over unweighted Stage-1 -- i.e. the gains come from the falsification/reweighting step, not the claim prompt itself. Rescue rate (fraction of cases where Cons@K majority is wrong but a correct candidate exists, that CLR corrects) spans ~16-48% across 16 benchmark-budget settings, averaging ~37%. Increasing claim count M from 1 to 3 improves accuracy 3.13-3.79pp on GPT-OSS-20B at K=32; M=5 gives further gains on three of four benchmarks, HMMT26 peaks at M=3.

## Limitations

The paper notes the falsification asymmetry (refuting is easier than constructing a correct solution) is treated as an inductive bias, not a guaranteed property -- 'we treat this asymmetry as an inductive bias rather than a guarantee that falsification is uniformly easier than generation.' The nonlinear reliability score (trace score = mean claim survival raised to the Mth power) is described as 'a heuristic, not a joint correctness probability' and does not assume claim independence. Results are model- and regime-dependent: on Gemma-4-12B-it, CLR improves accuracy by 7.12-12.08 points but costs 22.2-47.8% more tokens; on the already near-saturated Qwen3.5-27B (Cons@64 already >90% on three benchmarks), CLR's gains are small (up to +2.60pp) and its largest token reduction is 14.5%; the accuracy-token curves versus self-consistency can cross at intermediate budgets, so CLR is 'not uniformly dominant at every operating point.' It is published as a COLM 2026 workshop paper.

## Why it matters here

- **overthinking**: Relevant to the test-time-compute-allocation side of the topic: CLR is explicitly framed as a test-time scaling method that reallocates compute away from generating additional parallel solution samples toward targeted verification, and demonstrates cases (e.g. GPT-OSS-20B on CMIMC25: 82.19% vs Cons@64's 77.50%, using 37.0% fewer tokens) where the same or better accuracy is reached with fewer generated tokens under a matched budget. It is about parallel self-consistency sampling (K independent full solution rollouts) rather than the length of a single sequential reasoning trace, so it addresses the 'how to spend test-time compute efficiently' question but not directly the 'when should one trace stop thinking' question that is the core of overthinking/underthinking in a single chain-of-thought.

## Entities

- **Concepts**: claim-level falsification, signal dilution in whole-trace reliability evaluation, asymmetry between solution construction and claim refutation, nonlinear reliability-weighted consensus aggregation, rescue rate (overturning incorrect majority consensus)
- **Methods**: Claim-Level Reliability Assessment (CLR), self-consistency / Cons@K majority voting, pass@1, claim-level falsification, nonlinear reliability scoring
- **Datasets**: HMMT25, HMMT26, CMIMC25, Apex-shortlist

Tags: `test-time-scaling`, `self-consistency`, `verification`, `reliability-scoring`, `efficient-inference`, `reasoning-benchmarks`

## Abstract

We propose claim-level falsification as a principle for test-time scaling and instantiate it through Claim-Level Reliability Assessment (CLR), a training-free framework that reallocates test-time compute from additional solution sampling to targeted verification. Since whole-trace evaluation often obscures decisive errors due to signal dilution from routine tokens, CLR condenses each reasoning trace into a compact set of decision-critical claims, thereby isolating its logical anchors. Furthermore, recognizing the inherent difficulty of generating entirely correct solutions under fixed model capabilities, CLR shifts the focus to semantic falsification. This approach exploits a fundamental asymmetry between solution construction and claim refutation. Constructing a valid solution requires a flawless reasoning path, whereas refuting an incorrect claim requires identifying only a single decisive flaw. This targeted search for negative evidence systematically compresses the survival space of high-confidence incorrect traces, effectively suppressing erroneous consensus via nonlinear reliability scoring. Across four LLMs and four reasoning benchmarks under matched budgets, CLR generally improves upon pass@1 and self-consistency. On GPT-OSS-20B/CMIMC25, for instance, CLR exceeds pass@1 by 27.15 percentage-points and raises self-consistency accuracy from 77.50\% to 82.19\% with 37.0\% fewer tokens.

---

Record id: `arxiv:2608.11994`
