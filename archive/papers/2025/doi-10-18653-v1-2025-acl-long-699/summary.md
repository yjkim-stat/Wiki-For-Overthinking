<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Linguistic Generalizability of Test-Time Scaling in Mathematical Reasoning

- **Authors**: Guijin Son, Jiwoo Hong, Hyunwoo Ko, James Thorne
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2025.acl-long.699/>
- **PDF**: <https://aclanthology.org/2025.acl-long.699.pdf>
- **DOI**: 10.18653/v1/2025.acl-long.699
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Under a FLOPs-matched budget across three test-time scaling methods (Outcome Reward Modeling, Process Reward Modeling, Budget Forcing) on a new 55-language competition-math benchmark (MCLM), all three methods yield large gains in English (e.g. Budget Forcing +20 points on AIME) but only ~1.9-2 points average gain across other languages, and reward-model-guided scaling (ORM) matches or beats reasoning-trace-length scaling (Budget Forcing) once FLOPs are equalized -- with more test-time compute also increasing cross-lingual performance variance rather than reducing it.

## Problem

Scaling pre-training compute is known to improve multilinguality, but whether test-time scaling (longer reasoning, reward-model-guided sampling) confers the same cross-lingual benefit is unstudied, partly because existing multilingual math benchmarks (e.g. MGSM) are simple word problems now saturated by strong LLMs and mostly restricted to English/Chinese, understating the difficulty needed to stress-test reasoning at scale.

## Contributions

- MCLM, a 55-language, competition-level (MATH-500/AIME/IMO/regional olympiad derived) multilingual math reasoning benchmark addressing the saturation and English/Chinese-centrism of prior multilingual math benchmarks like MGSM
- a FLOPs-matched comparison of three test-time scaling strategies (ORM, PRM, Budget Forcing) showing all three yield large English-language gains but only ~1.9-2 point average gains across the other 54 languages, with test-time compute sometimes increasing rather than decreasing cross-lingual variance
- a finding that reward-model-guided scaling (ORM) matches or exceeds reasoning-trace-length scaling (Budget Forcing / 'thinking' LLMs) once compute is properly equalized, contrary to the assumption that long-CoT 'system 2' models have an inherent test-time-scaling advantage
- MR1-1.5B, an open multilingual extended-reasoning LLM (Deepseek-R1-1.5B fine-tuned on 14-language-translated R1-distilled trajectories) reaching performance comparable to GPT-4o-mini on multilingual mathematical reasoning

## Method

Builds MCLM (Multilingual Competition Level Math), a 55-language benchmark with four subsets: MT-MATH100 and MT-AIME2024 (GPT-4o machine-translated from MATH-500/AIME, verified for numerical-answer preservation), M-IMO (27 hand-reviewed International Mathematical Olympiad problems, officially translated into 38 languages), and M-MO (human-originated domestic/regional olympiad problems in 11 languages, LLM-judged). Evaluates three test-time scaling strategies on Qwen2.5-Math-1.5B/7B-Instruct, FLOPs-matched via a unified cost model (generator cost 2*N_G*D, verifier cost 4*N_V): Outcome Reward Modeling (ORM, sample k responses, select the highest-scoring via Qwen2.5-Math-72B-RM), Process Reward Modeling (PRM, generate c candidate continuations per step and select the best at each of S steps via Qwen2.5-Math-72B-PRM), and Budget Forcing (BF, truncate/extend a single reasoning trace to a token budget, per Muennighoff et al. 2025). Measures both average accuracy per language and cross-lingual consistency via Fleiss' kappa (whether the same questions are solved across languages, not just similar aggregate accuracy). Also trains MR1-1.5B, a multilingual 'thinking' LLM, by SFT-ing Deepseek-R1-1.5B on 50K R1-distilled reasoning trajectories with the math problem/solution translated into 14 languages (keeping the reasoning process in English) via GPT-4o, terminating at 0.5 epochs to avoid degradation from longer multilingual fine-tuning.

## Results

ORM's relative gains over a greedy-decoding baseline are consistent across K in {2,4,8} on the easier MT-MATH100 subset but become indistinguishable from each other -- and sometimes negative -- on the harder MT-AIME2024 subset across the 55-language average, even though English alone shows steady gains with K (1.5B model: 16.67->26.67->36.67; 7B: 20.00->26.67->36.67), indicating ORM's benefit is substantially weaker outside English on hard problems, likely because the 1.5B/7B generators struggle to produce high-quality non-English candidates for the reward model to select among. PRM shows unstable multilingual scaling too: average accuracy across 14 tested languages increases with FLOPs budget, but a larger reward model (72B) beats a smaller one (7B) at matched compute despite the 7B model enabling a wider search (more steps for the same cost), and neither Fleiss' kappa nor score standard deviation shows a clear monotonic trend with more compute -- i.e. added budget does not reliably improve cross-lingual consistency even on the easier MT-MATH100. Comparing ORM to PRM directly at matched FLOPs, ORM consistently achieves higher average accuracy than PRM on both MATH and AIME subsets and both model sizes despite PRM's more frequent verifier calls (and correspondingly higher latency), leading the authors to prefer ORM as the more reliable choice. Budget Forcing on MR1-1.5B yields nearly linear gains for English as the token budget (BF) rises 2048->8192, but the 55-language average rises only 1.9% over the same range, and for some languages (Latvian, Romanian) performance actually declines as budget increases -- directly paralleling the ORM/PRM finding that gains do not transfer robustly outside English. Once all three methods are FLOPs-matched, they achieve comparable levels of improvement to each other (contrary to the intuition that 'thinking'/R1-like long-CoT scaling would have a clear edge over classic reward-model-guided scaling) -- e.g. Qwen2.5-Math-1.5B with ORM reaches 35.8 on MCLM while MR1-1.5B with BF reaches 35.2. Training-side results: adding translated (14-language) SFT data to Qwen2.5-Math-1.5B gives only a modest +1.98% average MCLM improvement over English-only SFT, and initializing from Deepseek-R1-1.5B (already extended-reasoning-capable) before multilingual SFT gives a larger gain, reaching 30.93 average (+2.1% over the R1-1.5B baseline) with just 0.5 epochs of training -- longer training was found to degrade performance and was explicitly avoided.

## Limitations

The study focuses solely on mathematical reasoning tasks; the authors state the multilingual generalization gap observed here could be even more pronounced in tasks requiring extensive cultural or domain-specific understanding, which is left to future work. Due to budget constraints, experiments primarily use smaller-scale models (Qwen2.5-Math-1.5B/7B-Instruct); whether the lack of multilingual generalization in test-time scaling observed at this scale extends to significantly larger models (70B+) is untested, and the authors note prior work has scaled best-of-N to as many as 1,162 candidates using far more compute (2,500+ A100 GPU hours) than used here. Given that the 'curse of multilinguality' is known to disappear as pre-training compute scales by orders of magnitude, the authors explicitly flag it as plausible that larger models could behave differently for test-time scaling too, so their findings at smaller scale should be read as revealing potential boundaries for less resource-rich setups rather than a universal claim.

## Why it matters here

- **overthinking**: Directly relevant to the topic's core question of when more test-time compute actually helps: it shows, under a controlled FLOPs-matched comparison across three distinct scaling mechanisms, that added test-time compute's benefit is highly uneven -- large in English, minimal (and sometimes negative) in most other languages -- and that budget forcing specifically (extending a reasoning trace) sometimes hurts non-English performance as the budget grows. This is a concrete, quantified instance of the overthinking-adjacent finding that generating more reasoning tokens does not uniformly buy accuracy, here demonstrated as a language-dependent property rather than a difficulty-dependent one, and it directly compares reward-guided (ORM/PRM) versus trace-length-based (Budget Forcing) test-time scaling mechanisms head-to-head under equal compute, which is methodologically valuable for the topic's broader survey of mitigation/measurement approaches.

## Entities

- **Concepts**: linguistic generalizability of test-time scaling, cross-lingual consistency (Fleiss' kappa across language 'annotators'), FLOPs-matched test-time scaling comparison, Outcome Reward Modeling (ORM), Process Reward Modeling (PRM), Budget Forcing (BF)
- **Methods**: Outcome Reward Modeling (ORM), Process Reward Modeling (PRM), Budget Forcing (BF), FLOPs-matched inference-cost accounting, Fleiss' kappa cross-lingual consistency measurement
- **Datasets**: MCLM (new: MT-MATH100, MT-AIME2024, M-IMO, M-MO), [MATH-500](../../../../wiki/datasets/math500.md), [AIME 2024](../../../../wiki/datasets/aime-2024.md), IMO (2006-2024), MGSM (cited as saturated), OpenR1-220K (R1-distilled training data)

Tags: `overthinking`, `test-time-scaling`, `multilinguality`, `budget-forcing`, `reward-modeling`

## Abstract

Scaling pre-training compute has proven effective for achieving multilinguality, but does the same hold for test-time scaling? In this work, we introduce MCLM, a multilingual math benchmark featuring competition-level problems in 55 languages. We then compare three test-time scaling methods—Outcome Reward Modeling, Process Reward Modeling, and Budget Forcing. Our findings indicate that although “thinking LLMs” have recently garnered significant attention, their performance is comparable to traditional scaling methods like best-of-N once constrained to similar levels of inference FLOPs. More importantly, all tested methods fail to generalize robustly across languages, achieving only modest gains that are smaller than those observed in English, with no improvements in variance or consistency. To foster further research, we release MCLM and MR1-1.5B (a multilingual LLM with reasoning capabilities) and our evaluation results.

---

Record id: `doi:10.18653/v1/2025.acl-long.699`
