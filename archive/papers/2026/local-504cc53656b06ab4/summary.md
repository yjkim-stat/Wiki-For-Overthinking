<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias

- **Authors**: Justin D. Norman, Michael U. Rivera, D. Alex Hughes
- **Venue**: preprint
- **Published**: 2026-01-01
- **Source**: local
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.50

## In one line

Evaluates 21 LLM judges across three benchmarks and three protocols over ~541,000 judgments, and shows the field's standard validation metric — exact-match agreement — overstates chance-corrected discrimination by 34-41 points universally, while high test-retest reliability can coexist with severe position bias.

## Problem

LLM-as-a-Judge is the dominant evaluation paradigm and is deployed across hundreds of production pipelines, but judge validation in practice relies on exact-match agreement with human labels. That metric does not correct for agreement expected by chance, so it is sensitive to the label distribution of whatever benchmark it is computed on and systematically overstates a judge's discriminative ability. Established judge benchmarks all privilege raw agreement as the headline number. No prior work had run a large-scale, cross-benchmark, multi-protocol evaluation of judge reliability across model families and generations, so there was no basis for comparing judges on equal footing or for knowing how large the distortion is.

## Contributions

- Kappa deflation, named and measured: the gap between exact match and Cohen's kappa for a judge-benchmark pair, shown to be universal across all 21 judges, every provider, every capability tier and every generation through the April 2026 frontier.
- The consistency-bias paradox: high test-retest reliability can coexist with severe position bias in the same judge, because test-retest measures the stability of outputs rather than the correctness of the decision process — a judge that deterministically prefers position A scores perfectly on test-retest while being maximally biased.
- Cross-benchmark rank instability: judge rankings shift by up to 15 positions between benchmarks, so no single leaderboard predicts another.
- Evidence that verbosity bias, a major concern in 2023-era work, is now small under a single pairwise rubric — with an explicit caution against reading that as solved.
- A Minimum Viable Validation Protocol distilling the findings into five checkable steps, plus release of the full 541,000-judgment dataset and evaluation library.

## Method

Twenty-one general-purpose LLM judges from nine providers, spanning 8B to over 100B parameters and grouped into three capability tiers, are evaluated on three benchmarks chosen for increasing difficulty and differing label structure: MT-Bench (2,391 pairwise comparisons with expert human judgments, balanced A/B/Tie), JudgeBench (350 items across mathematics, coding, creative writing and analysis, labelled for objective correctness rather than aesthetic preference), and RewardBench (2,981 chosen-versus-rejected pairs with per-item position randomization). Three protocols run over them. The agreement protocol produces one judgment per item and reports Cohen's kappa, Krippendorff's alpha and tie-excluded exact match against the human label. The consistency protocol runs three to five independent evaluations per item with response caching disabled, presenting each pair in both AB and BA orderings, and reports test-retest reliability, self-consistency and position flip rate. The bias-audit protocol presents both orderings together with response-length analysis and reports position bias, operationalized as the absolute deviation of P(A wins) from 0.5, and verbosity bias as the Pearson correlation between the response-length differential and the verdict. All runs use temperature 0. Seven hypotheses are pre-registered before the frontier-model evaluation so findings can be assessed against a priori predictions. For models with a built-in reasoning trace, the reasoning channel is suppressed to maintain comparability and prevent verdict-token truncation.

## Results

Kappa deflation is universal: on MT-Bench, exact match overstates chance-corrected agreement by between 33.8 and 41.3 percentage points across all 21 models, cohort mean 38.6 pp, with all ten frontier-tier judges above 30 pp. Even the best judge on chance-corrected agreement, Gemini 3.1 Pro, shows a 33.8 pp gap (exact match 0.849, kappa 0.511). The practical translation the paper gives: a judge reporting '85% agreement' on MT-Bench has kappa around 0.48. Deflation magnitude tracks label balance — 38.6 pp on balanced-ternary MT-Bench, 23.7 pp on JudgeBench, 10.2 pp on RewardBench's binary pairs. Position bias spans nearly two orders of magnitude, from Gemini 2.5 Pro at 0.002 to Qwen 3 8B at 0.192, with large within-family heterogeneity: Gemini 2.5 Pro and 2.5 Flash differ by a factor of 70. Rank instability: more than half (11 of 21) shift by four or more positions between benchmarks, the largest being Llama 3.3 70B moving from 5th on MT-Bench to 20th on JudgeBench; only Gemini 3.1 Pro and Claude Opus 4.6 hold a top-three position on all three. This is amplified by differing discriminability — MT-Bench compresses all 21 judges into a 13.5 pp kappa band while JudgeBench spreads the same models over 60.4 pp, 4.5x wider. The consistency-bias paradox is instantiated by two production-deployed judges: Qwen 3 8B has the highest test-retest reliability in the study (0.992) alongside the most severe position bias (0.192) and the third-lowest JudgeBench kappa (0.289); Gemini 2.5 Flash shows the same pattern more mildly (0.988, 0.125). Consistency degrades on harder items: seven of sixteen judges show position flip rates increasing by at least 1.5x from MT-Bench to JudgeBench (Llama 3.3 70B 3.3x, from 0.077 to 0.253), while two frontier judges move the other way. Cohort mean test-retest falls from 0.943 to 0.911. Verbosity bias is small everywhere — all 21 below 0.011, seventeen below 0.005 — an order of magnitude below 2023-era reports. Family patterns: the three Anthropic judges average kappa 0.770 on JudgeBench with the lowest cohort-level position bias (0.020), while the three OpenAI flagships average 0.467; within OpenAI the generational progression is legible on JudgeBench (0.309, 0.487, 0.606 for GPT-4o, GPT-4.1, GPT-5.4) and nearly invisible on MT-Bench (0.451, 0.451, 0.457).

## Limitations

The paper's own, stated at length: coverage is three English-language text-only benchmarks, with multilingual and multimodal judging uncharacterized and explicitly not to be extrapolated to; all runs fall in a five-week window in March-April 2026, and hosted endpoints drift silently, so the numbers are a snapshot rather than a stable property; every judge is evaluated under one pairwise template and one operationalization per metric, so the verbosity finding must not be read as a universal claim that verbosity bias is solved; calibration metrics requiring token-level log-probabilities are deferred because most providers do not expose them; and for models with built-in reasoning traces the reasoning channel was suppressed, so the results do not characterize the thinking-on configuration — which is a real gap for anyone applying these findings to reasoning models. A reader should add that human labels are treated as ground truth throughout, so kappa measures agreement with a particular annotation process rather than correctness, and that the three benchmarks measure different latent constructs (preference alignment, objective correctness, chosen-versus-rejected discrimination), which is itself part of why ranks move.

## Why it matters here

- **reasoning-evaluation**: This is the paper that lets the group audit the evidence base of the rest of the archive, because LLM judges do load-bearing work in several archived papers — supplying collapse-mode taxonomies over 4,800 generations, out-of-distribution step-correctness labels that a probe is trained against, and the disentanglement scores in a central causal test. Two findings hit that dependence directly. First, kappa deflation means any judge validated by exact-match agreement is 34-41 points less discriminating than its reported number suggests, which is a uniform discount to apply wherever an archived paper cites judge agreement as evidence of label quality. Second, and sharper: at least one archived paper defends its judge-derived measurements by reporting inter-judge agreement of 94.87-98.75% with Gwet's AC1 between 0.96 and 0.99. The consistency-bias paradox is precisely the demonstration that this reasoning is invalid — test-retest and inter-judge agreement measure output stability, not correctness of the decision process, and the study's most reproducible judge is among its least valid. The Minimum Viable Validation Protocol is directly adoptable as a standard this group can require before accepting a judge-labelled result: chance-correct by default, swap positions, replicate at least three runs, cross-validate on two benchmarks spanning preference-style and correctness-style labels, and audit high test-retest for hidden bias. The caveat that matters most here is the paper's own: reasoning traces were suppressed in judges that have them, so how these failure modes behave when the judge is itself a reasoning model — the configuration this archive cares about — is unmeasured.

## Entities

- **Concepts**: LLM as a judge, kappa deflation, consistency-bias paradox, Cohen's kappa, Krippendorff's alpha, chance-corrected agreement, test-retest reliability, [position bias](../../../../wiki/concepts/position-bias.md), verbosity bias, [construct validity](../../../../wiki/concepts/construct-validity.md), benchmark discriminability, [meta-evaluation](../../../../wiki/concepts/meta-evaluation.md)
- **Methods**: [LLM as a judge](../../../../wiki/methods/llm-as-a-judge.md), position-swap debiasing, Minimum Viable Validation Protocol, bias audit protocol, pre-registered hypotheses
- **Datasets**: [MT-Bench](../../../../wiki/datasets/mt-bench.md), JudgeBench, RewardBench

Tags: `llm-as-a-judge`, `evaluation`, `reliability`, `validity`, `meta-evaluation`, `position bias`, `cohen's kappa`, `reproducibility`

## Abstract

LLM-as-a-Judge has become the dominant evaluation paradigm for language models, but judge validation in practice relies on exact-match agreement, a metric that does not correct for chance and systematically overstates discriminative ability. We present the largest systematic evaluation of LLM-as-a-Judge to date: 21 judges from nine providers across MT-Bench, JudgeBench, and RewardBench, evaluated under three protocols (agreement, consistency, bias audit) over 118 runs and approximately 541,000 individual judgments. Four findings emerge, consistent across the full cohort, including the April 2026 frontier: kappa deflation between exact match and Cohen's kappa is universal (33--41 pp on MT-Bench), judge rankings shift by up to 14 positions across benchmarks, high test--retest reliability (>0.95) coexists with severe position bias (>0.10) in two production-deployed judges (instantiating a consistency--bias paradox), and verbosity bias is small (<0.011) across our cohort under a single pairwise rubric. We distill these into a Minimum Viable Validation Protocol.

---

Record id: `local:504cc53656b06ab4`
