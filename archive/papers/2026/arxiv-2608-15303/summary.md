<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Divergent-Convergent Reasoning: Scaling Test-Time Compute through Structured Solution Synthesis

- **Authors**: Bo Wen, Yuhao Chen, Erhan Bilal, Carla Agurto Rios, Chen Wang, Junchen Jiang
- **Venue**: cs.AI
- **Published**: 2026-08-15
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.15303>
- **PDF**: <https://arxiv.org/pdf/2608.15303v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Divergent-Convergent Reasoning generates diverse candidate solutions and then uses reviewer-style reconciliation calls (optionally run recursively with a verifier-free unanimous-consent stopping rule) to recover correct answers even when they start out as a minority, reaching 93.3% on AIME 2024 and 92.0% on AIME 2025 while using about 27% less compute than a fixed single-round baseline.

## Problem

How and when additional test-time compute helps LLM reasoning is poorly understood; disagreement among sampled candidate solutions is typically treated as noise to be averaged away via majority voting, but majority voting fails whenever the correct answer is itself a minority view among sampled proposals, and there is no established, verifier-free way to decide when to keep spending test-time compute versus stop.

## Contributions

- Shows single-round DCR (divergent exploration + one reconciliation round with reviewer width K=25) consistently improves both trial accuracy (Best-of-N proxy) and consistency (majority-vote proxy) over plain sampling, and specifically recovers the correct answer even when correct exploration outputs are in the minority -- a regime where majority voting fails
- Introduces recursive DCR, which reapplies convergent reconciliation in rounds with a verifier-free unanimous-consent stopping rule (stop when all K reviewer calls in a round agree), achieving higher accuracy than fixed-compute single-round DCR while using ~27% less average compute
- Defines a training-free dispersion metric (centroid-based spread of embedded exploration answers) and shows it predicts when reconciliation is most beneficial: near-zero dispersion (already confident) and extreme dispersion (capability collapse / overwhelmed) both show weaker gains, with a 'sweet spot' of moderate dispersion where reconciliation gain is largest
- Compares against a replicated ReConcile peer-discussion baseline, showing DCR's reviewer-author reconciliation structure beats round-table peer debate by ~40 accuracy points on the same models

## Method

Divergent-Convergent Reasoning (DCR) has two phases run under a fixed API-call budget with no verifier or ground-truth feedback available at inference. Phase 1 (Divergent Exploration): given a problem, one or more LLM instances independently generate N diverse candidate solutions (via different seeds/temperatures or a heterogeneous ensemble), forming a solution pool. Phase 2 (Convergent Reconciliation): a set of K independent reviewer calls receive the pooled proposals and are prompted to identify consensus steps (common across most proposals, likely correct), pinpoint divergent steps (where proposals disagree, the hardest parts), and synthesize a single reconciled answer by combining verified consensus steps with newly reasoned resolutions of the divergent steps, explicitly considering whether a minority proposal contains a crucial correction the majority missed. Recursive DCR iterates Phase 2 in rounds, feeding each round's reconciled outputs back in as the next round's proposal pool, and stops early once a round's K reviewer calls reach unanimous agreement (or a max round/call budget is exhausted, in which case a majority answer plus minority report is returned). Separately, a training-free dispersion diagnostic embeds the N exploration answers with a Sentence-BERT encoder and computes the mean squared distance to their centroid, used post hoc to characterize when reconciliation helps.

## Results

Table 1 (single-round DCR, K=25, vs. sampling baseline): consistent gains across all 4 datasets/models. Notable examples: AIME 2024 GPT-OSS trial accuracy improves from 74.3% (sampling) to 88.1% (DCR-single) and consistency from 76.7% to 90.0%; Llama-3.3 on MATH500 improves from 20.8% to 51.4% trial accuracy (single) / 72.9% (mixed pool); AIME 2025 Granite-4 improves from 0.9% to 8.9%/39.5%. Table 2 (recursive vs single-round DCR at budget=50): on AIME 2024, recursive DCR reaches 93.3% accuracy using an average of 36.4 calls, versus single-round DCR's 88.1% at a fixed 50 calls; on AIME 2025, recursive DCR reaches 92.0% accuracy at 36.1 average calls versus single-round's 87.2% at 50 calls -- roughly 27% less compute on average with higher accuracy. Figure 3 shows recursive DCR achieves both higher accuracy and lower budget than single-round DCR ('win-win'), converging in a single round (~33 total calls) on easy problems and escalating up to 80 calls on hard, persistently-disagreeing problems. A replicated ReConcile peer-discussion baseline (same models) reaches only 40.0% (AIME 2024) and 53.3% (AIME 2025) trial accuracy -- nearly 40 points lower than DCR's reviewer-author reconciliation. Stability check: across 10 repeated runs per problem, recursive DCR typically either solves a problem in every trial (100% consistency) or fails in every trial (0%), with very few problems showing intermediate success rates (e.g. only one problem in AIME 2025). Dispersion analysis (Figure 4) shows baseline (sampling) accuracy declines monotonically as dispersion increases, and DCR's accuracy gain over sampling is largest in a moderate-dispersion 'Recoverable Uncertainty' zone, near-zero at very low dispersion (already confident, little to reconcile), and diminishing at very high dispersion (extreme disagreement / capability collapse, i.e. d >~ 0.3).

## Limitations

Discussion section (6) and Future Work (7) state several limits: (1) Upfront cost of estimation -- computing dispersion as a gating signal requires generating N proposals (N=25 in experiments) before assessing difficulty, which may be prohibitive in latency-sensitive production settings; adaptive probing or hybrid human-triage strategies are left to future work. (2) Bias in low-dispersion regimes -- low dispersion signals high model confidence but not correctness; a model can be consistently and confidently wrong ('confident hallucination'), and DCR is less effective there; addressing this would need heterogeneous ensembles rather than single-model resampling. (3) The recursive system's unanimous-consent stopping rule is strict and may be overly conservative; the paper suggests future work on 'soft consensus' or probabilistic stopping rules. (4) The dispersion metric currently uses only final-answer embeddings; the authors note additional signals (reasoning-path dispersion, confidence dispersion, token-level entropy) are not yet incorporated. (5) A distinct failure mode is observed in mixed-proposal (DCR-Mix) settings: weaker models' incorrect proposals can 'pollute' a stronger reviewer's judgment, causing it to hallucinate or drift from a correct path, so mixing is only reliably helpful when it lifts weaker models toward a strong consensus rather than diluting strong experts with weak noise.

## Why it matters here

- **overthinking**: Directly relevant to the test-time-compute-allocation and stopping-point strands of the topic: recursive DCR is explicitly a mechanism for deciding when to keep spending inference-time compute (running further reconciliation rounds) versus stop (unanimous-consent stopping), achieving higher accuracy than a fixed-compute baseline while using ~27% less compute on average by converging early on easy problems and escalating only on hard ones. Its dispersion diagnostic also directly targets 'how much test-time compute a problem needs,' the accuracy/efficiency tradeoff at the core of the topic. It operates at the granularity of multi-agent proposal generation and reviewer rounds rather than the length of a single chain-of-thought trace, so it is a coarser-grained instance of the same stop-at-the-right-point problem rather than a study of within-trace overthinking/underthinking.

## Entities

- **Concepts**: Divergent-Convergent Reasoning (DCR) as a two-phase test-time primitive, minority-report amplification (correct answers recovered even when correct exploration outputs are a minority), recursive/autoregressive reconciliation with unanimous-consent stopping, dispersion of exploration outputs as a training-free proxy for task difficulty, selection-is-easier-than-generation as the mechanistic intuition behind reconciliation gains
- **Methods**: Divergent-Convergent Reasoning (DCR), single-round DCR (K=25 reviewer width), recursive DCR (K=8 per round, unanimous-consent stopping), dispersion metric (Sentence-BERT centroid distance), ReConcile peer-discussion baseline (replicated for comparison)
- **Datasets**: [MATH500](../../../../wiki/datasets/math500.md), [AIME 2024](../../../../wiki/datasets/aime-2024.md), [AIME 2025](../../../../wiki/datasets/aime-2025.md), [MMLU-PRO](../../../../wiki/datasets/mmlu-pro.md)

Tags: `test-time-scaling`, `multi-agent-reconciliation`, `self-consistency`, `adaptive-compute-allocation`, `minority-report`, `dispersion`

## Abstract

Test-time compute can substantially improve Large Language Model (LLM) reasoning performance, yet how and when additional compute helps remains poorly understood. We study Divergent-Convergent Reasoning (DCR), a simple two-phase primitive consisting of an exploration phase that generates multiple candidate solutions followed by a convergent reconciliation phase. We present three core results. First, we show that even a single reconciliation step can reliably amplify correct minority reports: across datasets, DCR often recovers the correct answer when correct exploration outputs are in the minority, a regime where majority voting fails. Second, we introduce recursive DCR, an autoregressive reconciliation system that iteratively analyzes disagreements and allocates additional test-time compute. Recursive DCR achieves higher accuracy than fixed-compute baselines-reaching 93.3% on AIME 2024 and 92.0% on AIME 2025-while using roughly 27% less compute on average, demonstrating that attentive resource allocation is superior to uniform scaling. Third, we analyze disagreement among exploration outputs via a simple, training-free dispersion metric. Dispersion reveals a structured relationship between disagreement and test-time gains: in regimes where DCR is effective, higher disagreement among exploration outputs is associated with larger accuracy improvements from reconciliation. Together, these results show that disagreement, often viewed as noise, can be systematically exploited to improve test-time reasoning and reveal emerging scaling laws for agentic LLM systems.

---

Record id: `arxiv:2608.15303`
