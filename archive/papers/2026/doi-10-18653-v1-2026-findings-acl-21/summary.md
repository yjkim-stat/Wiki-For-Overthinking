<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# BrowseConf: Confidence-Guided Test-Time Scaling for Web Agents

- **Authors**: Litu Ou, Kuan Li, Huifeng Yin, Liwen Zhang, Zhongwang Zhang, Xixi Wu, Rui Ye, Zile Qiao, Yong Jiang, Pengjun Xie, Fei Huang, Jingren Zhou
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.21/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.21.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.21
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

BrowseConf shows that despite web-search agents being poorly calibrated in absolute terms (verbalized confidence systematically exceeds actual accuracy), their confidence is strongly rank-correlated with correctness -- near-zero accuracy below 70% confidence, more than double the average accuracy above 95% -- and exploits this by triggering additional search attempts only when confidence falls below a calibrated threshold rather than always sampling a fixed number, matching or beating fixed-budget Self-Consistency/CISC on BrowseComp while cutting average attempts from a fixed 10 down to 2.06-5.72.

## Problem

Test-time-scaling methods for LLM-based web-search agents (self-consistency, confidence-informed self-consistency) uniformly apply a fixed sampling budget to every query regardless of how confident or uncertain the agent actually is, wasting compute on queries the agent could already answer reliably in one attempt; separately, whether verbalized confidence is even a meaningful signal after long multi-turn agentic action sequences (as opposed to single-turn scenarios where it has been more studied) is underexplored, since long-horizon agents are known to forget previously acquired information and struggle to recover from earlier errors.

## Contributions

- an empirical demonstration that verbalized confidence in long-horizon, multi-turn web-search agents, while poorly calibrated in absolute terms, remains strongly rank-correlated with task accuracy on a challenging benchmark, extending prior single-turn confidence-reliability findings to complex agentic settings
- BrowseConf, a confidence-guided test-time-scaling method that dynamically allocates additional search attempts only when an agent's confidence falls below a leakage-free-calibrated threshold, rather than sampling a fixed budget for every query
- two information-carryover variants (Summary-Guided, Negative-Constrained) that propagate knowledge from low-confidence prior attempts to guide subsequent ones, shown to reduce redundant search/browsing interactions substantially versus restarting from scratch
- empirical results on BrowseComp/BrowseComp-zh showing BrowseConf matches or exceeds fixed-budget-10 Self-Consistency and CISC baselines while cutting average attempts to 2.06-5.72

## Method

First measures whether verbalized confidence (the agent self-reports a 0-100 confidence score after its final answer, following a simple prompt instruction) predicts task accuracy on the challenging BrowseComp benchmark, binning confidence scores into 5-point intervals and comparing interval accuracy against overall accuracy. Confirms both models tested (DeepSeek-V3.1, gpt-oss-120b) are poorly calibrated in absolute terms (verbalized confidence substantially exceeds actual accuracy in every bin -- e.g. the top 90-94% confidence bin for DeepSeek-V3.1 achieves only 53.33% actual accuracy) but shows a strong positive rank correlation: accuracy approaches zero for confidence scores below 70% and more than doubles the overall average above 95%. BrowseConf then exploits this relative (not absolute) reliability: for a query, it defines a confidence threshold tau, calibrated (leakage-free, on a held-out SailorFog-QA validation subset) as the minimum threshold ensuring at least a k% relative accuracy improvement on samples exceeding it versus the overall validation accuracy. At inference (Algorithm 1, 'Restart from Scratch'), the agent generates an answer and confidence score for attempt i; if confidence meets or exceeds tau, generation terminates immediately and that answer is returned; otherwise a new attempt begins, up to a maximum budget N=10, with the highest-confidence answer across all attempts returned if the budget is exhausted without meeting threshold. Two variants retain information across attempts rather than restarting from scratch each time: BrowseConf-Summary conditions each new attempt on a teacher-generated summary of the prior attempt's key entities, identified contradictions, and incomplete reasoning steps; BrowseConf-Neg explicitly provides all prior attempts' low-confidence answers and prompts the model to generate a different one.

## Results

On BrowseComp and its Chinese counterpart BrowseComp-zh, all three BrowseConf variants consistently outperform or perform competitively against fixed-budget-10 baselines (Self-Consistency, Confidence-Informed Self-Consistency/CISC) while requiring far fewer average attempts: for gpt-oss-120b, BrowseConf-Neg achieves the highest accuracy on both benchmarks (54.5% BrowseComp, 54.0% BrowseComp-zh) at 3.87/2.43 average attempts respectively, versus Self-Consistency's 47.5%/50.5% at a fixed 10 attempts each and CISC's 52.2%/53.3% likewise at 10; for DeepSeek-V3.1, BrowseConf variants reach up to 41.8% BrowseComp accuracy (BrowseConf-Neg) at only 5.72 average attempts, versus CISC's 38.7% at a full 10 attempts. Among the three BrowseConf variants, BrowseConf-Neg (which explicitly avoids repeating prior low-confidence answers) consistently yields the highest accuracy; BrowseConf-Summary consistently requires the fewest rollouts across models and benchmarks (as low as 2.06 for gpt-oss-120b); BrowseConf-Zero (restart from scratch, no information carryover) provides a balanced middle ground between efficiency and performance. Confidence-threshold ablation (varying k%, the relative-improvement calibration criterion) shows a tighter threshold (higher k%) yields better final accuracy but requires more attempts on average, with a clearly diminishing-returns pattern: the accuracy gain from k=5 to k=10 is much larger than from k=10 to k=20, indicating an overly restrictive threshold does not meaningfully improve performance and leads to unnecessary extra attempts; across the full attempt-budget range (1 to 10), all tested k values eventually surpass the Pass@1 baseline, with k=10 consistently outperforming k=20 until the final attempt (where k=20's stricter threshold produces a sharp late-stage accuracy jump from being forced to exhaust the full budget and fall back to the single highest-confidence answer found). Interaction-count analysis (tracking the number of thought-action-observation cycles per attempt across consecutive attempts) shows BrowseConf-Summary and BrowseConf-Neg -- the two variants that carry information forward -- exhibit a significant decline in interactions needed between the first and second attempts specifically, while BrowseConf-Zero (which restarts from scratch each time) shows much smaller fluctuations, indicating that retaining summative information from past attempts lets the agent solve the task with less redundant search/browsing on subsequent tries, with the largest efficiency improvement occurring immediately after the first attempt.

## Limitations

The study exclusively uses verbalized confidence (a single self-reported 0-100 score) due to its simplicity and model-agnostic, low-overhead nature, without comparing against other confidence-estimation techniques (white-box internal-state probes, token-level entropy, self-consistency-based estimators) that could offer different performance/computational-overhead/calibration tradeoffs -- the paper explicitly flags this comparison as important future work. The experiments are restricted to text-only, information-seeking web-agent tasks (BrowseComp, BrowseComp-zh); generalizability to other agentic domains (tool use beyond web search, software engineering, scientific reasoning) or to multi-modal agents (image/audio/video) is not evaluated and explicitly noted as an open direction.

## Why it matters here

- **overthinking**: Indirectly relevant to test-time compute efficiency, extending this archive's confidence-based test-time-scaling theme (also seen in Guided by Gut, Chronos, STEP) from single-trace reasoning or parallel sampling into multi-turn agentic web search: it shows that even in a setting where confidence is known to be poorly calibrated in absolute terms and where agents are known to forget or fail to recover from earlier errors, relative confidence signal is reliable enough to gate additional 'thinking' (in this case, additional full search attempts) rather than always paying a fixed compute budget -- directly analogous to the token-budget or early-stopping decisions single-trace overthinking-mitigation methods make, but applied at the level of whole agentic episodes.

## Entities

- **Concepts**: verbalized confidence (relative reliability despite poor absolute calibration), confidence-guided test-time scaling, confidence-threshold calibration (leakage-free), restart-from-scratch vs. information-carryover TTS, Confidence-Informed Self-Consistency (CISC, baseline)
- **Methods**: BrowseConf (BrowseConf-Zero / Summary / Neg), [Self-Consistency (baseline)](../../../../wiki/methods/self-consistency-baseline.md), [Confidence-Informed Self-Consistency (CISC, baseline)](../../../../wiki/methods/confidence-informed-self-consistency-cisc-baseline.md), Pass@1 / Pass@10 (reference)
- **Datasets**: [BrowseComp](../../../../wiki/datasets/browsecomp.md), BrowseComp-zh, SailorFog-QA (validation/threshold-calibration subset)

Tags: `test-time-scaling`, `confidence-calibration`, `web-agents`, `agentic-reasoning`, `compute-allocation`

## Abstract

Confidence in LLMs is a useful indicator of model uncertainty and answer reliability. Existing work mainly focused on single-turn scenarios, while research on confidence in complex multi-turn interactions is limited. In this paper, we investigate whether LLM-based search agents have the ability to communicate their own confidence through verbalized confidence scores after long sequences of actions, a significantly more challenging task compared to outputting confidence in a single interaction. Experimenting on open-source agentic models, we first find that models exhibit much higher task accuracy at high confidence while having near-zero accuracy when confidence is low. Based on this observation, we propose Test-Time Scaling (TTS) methods that use confidence scores to determine answer quality, encourage the model to try again until reaching a satisfactory confidence level. Results show that our proposed methods significantly reduce token consumption while demonstrating competitive performance compared to baseline fixed budget TTS methods.

---

Record id: `doi:10.18653/v1/2026.findings-acl.21`
