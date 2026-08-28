<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Exploration-Exploitation Reshaping towards Efficient Reasoning for Large Language Models

- **Authors**: Yufeng Shi, Weilin Luo, Yuxiang Zhang, Zongmeng Zhang, Haoyang Liu, Yubing Wang, Bin Wang, Wengang Zhou, Houqiang Li
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1520/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1520.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1520
- **Topics**: overthinking
- **Relevance score**: overthinking 0.67

## In one line

SIGMA reframes token-efficient RL as a classical exploration-exploitation problem: a self-imitation exploitation module prioritizes training on prompts/rollouts with high compression potential via a dynamic priority table and a compression-ratio-weighted self-imitation loss, while a self-guidance exploration module directs otherwise-undirected long-response exploration via prompt-based token-budget regeneration or random truncation -- improving average accuracy by 7.9%/2.9% while cutting average reasoning length 43.4%/40.3% on 1.5B/7B DeepSeek-R1-Distill models across six benchmarks, beating eight RL-based efficient-reasoning baselines.

## Problem

RL methods for mitigating LRM overthinking mostly rely on length-based reward shaping, applying negative feedback to randomly sampled lengthy responses with no explicit guidance toward a concise reasoning path -- the classical RL inefficient-exploitation/exploration problem -- making them sample-inefficient and non-robust.

## Contributions

- a reframing of token-efficient RL for LRMs as a classical exploration-exploitation tradeoff, distinct from the length-based-reward-shaping framing common to prior efficient-reasoning RL work
- a self-imitation exploitation module combining a compression-ratio-weighted self-imitation loss with a dynamic, compressibility-based priority table for prompt sampling (rather than uniform sampling)
- a self-guidance exploration module that directs exploration of overly-long responses toward the model's own demonstrated compression capability via prompt-based regeneration or truncation, instead of relying purely on reward signal to discourage length
- state-of-the-art results on the accuracy-length Pareto frontier across six benchmarks and two model scales versus eight RL-based efficient-reasoning baselines, plus an explicit, tunable accuracy/efficiency control dial via the exploitation-strength hyperparameter

## Method

Views token-efficient RL through the classical exploration-exploitation lens and adds two GRPO-compatible modules. Exploitation (self-imitation): defines a per-response compression ratio C(o_i) = max(0, (mean* - |o_i|)/mean*) for correct responses (0 for incorrect ones), where mean* is the mean length of correct responses in the group; adds a clipped, importance-sampling-corrected self-imitation loss L_SIL weighted by C(o_i) (so more-compressed-than-average correct responses get stronger imitation signal), combined additively with the standard GRPO loss (L_total = L_GRPO + alpha*L_SIL). A dynamic priority table tracks each training prompt's maximum observed compression ratio and is used to probabilistically oversample prompts with higher compressibility (rather than uniform sampling), so training focuses where efficiency gains are most attainable; priorities decay as a prompt's compression rate is exploited over training, naturally shifting sampling toward other high-potential prompts. Exploration (self-guidance): for responses that hit the maximum length without producing an answer (an early length threshold check, not the full group), one of three self-guidance strategies is applied with equal probability: prompt-based regeneration (re-generate with an inserted 'use less than m tokens' instruction), random truncation (cut the response at a randomly sampled point within [T_min, T_max] then append a stop-thinking token and continue generation), or original-response retention (keep the overly-long response unmodified, found empirically to still contribute a useful negative training signal). This directs otherwise-undirected long-response exploration toward responses within the model's demonstrated compression capability, rather than relying on the reward signal alone to discourage length.

## Results

Across six benchmarks (GSM8K, MATH500, AIME24, AMC, OlympiadBench, GPQA-Diamond) and two backbones, SIGMA improves average accuracy by +7.9pp (1.5B: 54.5%->62.4%) and +2.9pp (7B: 70.0%->72.9%) versus the base model while achieving the largest average length reduction of all compared methods (43.4% on 1.5B: 6012->3405 tokens; 40.3% on 7B: 5392->3221 tokens), outperforming eight baselines (SFT, DPO, DAPO, AdaptThink, LC-R1, Laser-D, Laser-DE, JET) on the accuracy-length Pareto frontier (Figure 1). Notably SIGMA improves accuracy on nearly every individual benchmark (e.g. 1.5B AIME24: 28.7%->36.7%, +7.9pp; 7B GSM8K: 87.0%->89.6%, +2.6pp) while simultaneously shortening responses, rather than trading one for the other as most length-penalty baselines do (several baselines show accuracy *drops* alongside length reduction, e.g. Laser-D on 1.5B AMC: 42.5% vs. base 47.0%). Component ablations (Table 2) show: removing self-guidance exploration (w/o SGE) causes accuracy to degrade sharply (7B: 72.0%->64.5%; similar on 1.5B), confirming undirected exploration fails to find a high-performance concise-reasoning policy; removing self-imitation learning (w/o SIL) leaves the model still overthinking, with reasoning length growing 55.1% (7B) / 44.8% (1.5B) versus the full method despite comparable accuracy, showing SIL is specifically responsible for driving length reduction rather than accuracy; removing dynamic priority sampling (w/o Dyn) reduces average accuracy, particularly on harder benchmarks (AIME24, Olympiad), because high-difficulty problems are no longer preferentially sampled and exploited -- though on the 1.5B model this ablation nominally shows a slightly *higher* AIME24 accuracy (38.0% vs. SIGMA's 36.7%), attributed to the smaller model's limited capacity to compress length on harder problems without sacrificing correctness, so dynamic sampling ends up favoring easier-to-compress medium-difficulty problems (like Olympiad) over harder ones, reducing training exposure to the hardest problems specifically. Removing all exploitation-module designs (equivalent to +SGE alone) produces results similar to the w/o-SIL ablation, with both LLMs reverting to sacrificing inference efficiency for higher accuracy -- their 'natural' overthinking tendency. Sensitivity analysis over the exploitation-strength hyperparameter alpha (0.1 to 1.5) shows a clear, mostly monotonic accuracy-length tradeoff dial: larger alpha yields shorter responses with somewhat lower accuracy across AIME24/GSM8K/GPQA-Diamond on both model scales, giving practitioners an explicit control interface. An ablation removing original-response retention specifically (keeping only the two active regeneration/truncation strategies) causes reasoning cost to grow substantially (55.1% for 7B, 44.8% for 1.5B) to an intolerable degree, indicating that occasionally retaining unmodified long negative samples is itself informative training signal, not merely inert data.

## Limitations

The paper does not discuss limitations explicitly in the excerpted sections; its self-guidance exploration strategies (prompt-based regeneration, random truncation) are applied with a fixed equal-probability (1/3 each) scheme rather than an adaptively-learned mixture, which the paper notes as extensible but does not itself tune; the dynamic-sampling ablation result shows the method's benefit is sensitive to model capacity (the 1.5B model's limited ability to compress hard problems without losing correctness causes dynamic sampling to systematically favor easier problems), an interaction the paper documents but does not resolve.

## Why it matters here

- **overthinking**: Directly and centrally relevant: it names overthinking explicitly and reframes its RL-based mitigation as a classical exploration-exploitation problem, arguing prior length-penalty RL methods fail because they punish long responses without any directed exploration toward a concise alternative -- a distinct diagnostic framing from entropy-trend, step-structure, or budget-based accounts elsewhere in this archive, and one that (unusually) improves accuracy while shortening responses rather than trading one for the other.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), exploration-exploitation reshaping (in token-efficient RL), self-imitation exploitation, compression ratio, dynamic priority table, self-guidance exploration
- **Methods**: SIGMA (Self-Imitation and self-Guidance MechAnism), [GRPO](../../../../wiki/methods/grpo.md), SFT (baseline), [DPO (baseline)](../../../../wiki/methods/dpo-baseline.md), [DAPO (baseline)](../../../../wiki/methods/dapo-baseline.md), AdaptThink (baseline), LC-R1 (baseline), Laser-D / Laser-DE (baseline), JET (baseline)
- **Datasets**: DeepScaleR-Preview-Dataset (training, ~40k problems), [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH500](../../../../wiki/datasets/math500.md), [AIME24](../../../../wiki/datasets/aime-2024.md), [AMC](../../../../wiki/datasets/amc.md), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md)

Tags: `overthinking`, `reinforcement-learning`, `GRPO`, `self-imitation-learning`, `exploration-exploitation`, `length-control`

## Abstract

While excelling at solving complex problems, Large Reasoning Models (LRMs) are still constrained by the overthinking issue. Most current studies rely on reward shaping in Reinforcement Learning (RL) to shorten the Chain-of-Thought (CoT) of LRMs, remaining sample-inefficient and non-robust due to the absence of guided exploration and prioritized exploitation. To address these issues, we propose a novel policy optimization framework with Self-Imitation and self-Guidance MechAnisms (SIGMA), which reshapes the exploration and exploitation through two core components: (i) self-imitation exploitation, which enables the prioritized exploitation of high-value prompts and rollouts by introducing a self-imitated loss and a dynamic sampling strategy based on compression rate; (ii) self-guidance exploration, which provides a preference-aware exploration guidance through diverse and pluggable self-rewriting strategies. Experiments across various datasets indicate that our method achieves superior reasoning efficiency without compromising, and even facilitating, the overall accuracy. Furthermore, ablation studies show that the proposed mechanisms can provide flexible control interfaces for the tradeoff between the reasoning accuracy and efficiency of LRMs.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1520`
