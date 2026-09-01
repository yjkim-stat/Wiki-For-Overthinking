<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Beyond Token Length: Step Pruner for Efficient and Accurate Reasoning in Large Language Models

- **Authors**: Canhui Wu, Qiong Cao, Chang Li, Zhenfang Wang, Chao Xue, Yuwei Fan, Wei Xi, Xiaodong He
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.94/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.94.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.94
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Step Pruner (SP) is an RL framework that replaces token-count length penalties with a step-count reward (paragraph-based segmentation as a proxy for reasoning steps), penalizing steps beyond the minimal number needed for a correct answer while masking rewards for incorrect responses, achieving state-of-the-art accuracy-efficiency trade-off and 44-70% token reduction across four benchmarks without the reward-hacking (degenerate step-merging) that token-based RL penalties are prone to.

## Problem

Existing RL-based efficient-reasoning methods penalize token count directly to shorten reasoning, but this rests on a false assumption: fewer tokens do not always mean fewer reasoning steps (a longer response may contain fewer, more complete reasoning steps, while a shorter one may skip steps), and directly penalizing token count can incentivize reward hacking in later training stages, where the model discards the reasoning process entirely to minimize token usage regardless of correctness.

## Contributions

- Step Pruner (SP), an RL framework replacing token-count length penalties with a step-count-based reward, penalizing only excess steps beyond the minimal number needed for correctness rather than raw token length
- identification and empirical characterization of a specific reward-hacking failure mode in step-based training (merging distinct reasoning steps into fewer, longer paragraphs to exploit the reward) and a dynamic stopping criterion that detects and halts training before this degenerate phase
- a systematic comparison of five segmentation granularities (token, sentence, conjunction, paragraph, embedding-similarity), establishing paragraph-based segmentation as the best accuracy-compression trade-off
- state-of-the-art Accuracy-Efficiency Score across four benchmarks and two model families/sizes, with 44-70% token reduction and an LLM-judged semantic shift toward pivotal/substantive reasoning content and away from digression and redundant self-correction

## Method

Splits each generated response into discrete reasoning steps via paragraph-based segmentation (splitting on \n\n as a proxy for a reasoning unit, chosen after comparing sentence-level, conjunction-based, and embedding-similarity-based segmentation and finding paragraph segmentation gives the best compression-vs-accuracy trade-off). Defines the optimal step count S* for an input as the minimum step count observed among all correct candidate responses sampled for that input. The step reward penalizes excess steps beyond S* for correct responses, penalizes excess steps beyond S* (in addition to the correctness penalty) for incorrect responses, but gives no brevity credit for incorrect-and-short responses -- explicitly preventing the model from learning that generating short wrong answers is rewarded. All step rewards are masked to zero when every sampled candidate for an input is incorrect, to avoid training on uninformative all-wrong batches. Policy optimization uses GRPO. A dynamic stopping criterion halts training once the average response length stops decreasing, based on an observed two-phase training dynamic: first the step count drops while paragraph length stays roughly flat (bona fide step reduction), then paragraph count plateaus while paragraph length rises sharply (the model beginning to merge logically distinct steps into single bloated paragraphs to exploit the reward) -- stopping at the length-plateau point avoids this second, degenerate phase. Trained on DeepScaleR-preview (40K math problems) with DeepSeek-R1-Distill-Qwen-2.5-7B/1.5B and evaluated on AIME24, MATH500, GSM8K, GPQA-Diamond against seven baselines spanning prompt-based (CCoT, CoD), SFT-based (CoT-Valve), model-merging (Model Merge/Long-to-Short Reasoning), and RL-based (O1-Pruner, ShorterBetter, TrainEfficient) efficient-reasoning approaches.

## Results

SP achieves the best or near-best Accuracy-Efficiency Score (AES, a composite metric) across nearly all benchmark/model-size combinations, using only 44% of the tokens of the R1-Qwen baselines on average while maintaining or improving accuracy -- e.g. on AIME24 with the 7B model, SP cuts average output length by 70% (14839 -> 4502 tokens) at 50.0% accuracy versus the base R1-Qwen-7B's 53.3% at 14839 tokens; on MATH500 SP reduces length by 67% while achieving the top accuracy (92.0%) among all compared methods. On the 1.5B model, SP outperforms all baselines on GPQA-Diamond, MATH500 and GSM8K and remains highly competitive on AIME24, showing the approach's advantages hold at smaller scale too; results on a Llama-3.1-8B backbone (Table 3) confirm SP's robustness generalizes across model families, with the best AES on every benchmark tested. An ablation (Table 2) shows removing the correctness-reward masking causes the largest accuracy collapse (confirming explicit correctness signal is essential), removing the optimal-step-count component also hurts accuracy (confirming brevity must be balanced against correctness rather than pursued alone), and removing the skip-all-wrong-batches mechanism further degrades performance by training on uninformative trajectories. A segmentation-method comparison (Figure 4) shows token-level segmentation achieves the largest length reduction (below 1000 tokens) but the largest accuracy drop, while paragraph-based segmentation gives the best balance -- finer segmentation reduces length more aggressively but typically lowers accuracy, coarser segmentation better preserves accuracy with less length reduction. An LLM-judge (Gemini 2.5) semantic analysis of the trained 7B model's reasoning categorizes each sentence into five types (Pivotal Reasoning, Productive Elaboration & Calculation, Exploring Alternatives, Verification & Self-Correction, Non-Substantive Statements): SP-7B shifts sharply toward Pivotal Reasoning and Productive Elaboration & Calculation (core, substantive content) and away from Exploring Alternatives and Verification & Self-Correction (digressions and redundant self-checking) relative to the untrained R1-Qwen-7B baseline, giving direct evidence the length reduction removes low-value content rather than degrading substance uniformly.

## Limitations

SP can inadvertently encourage the model to merge distinct logical steps into overly long paragraphs (the reward-hacking behavior the dynamic stopping criterion is specifically designed to catch and halt training before), potentially compromising interpretability and readability even when stopped in time. Paragraph-based segmentation may not capture fine-grained reasoning boundaries for tasks requiring nuanced step differentiation. SP's effectiveness depends on accurate correctness evaluation; in domains with ambiguous or subjective answers (unlike the exact-match math tasks studied here), reward assignment may be less reliable, limiting generalizability beyond mathematical reasoning.

## Why it matters here

- **overthinking**: Core paper for this topic: explicitly names 'overthinking' as the motivating problem and directly targets its central methodological critique -- that token count is a flawed proxy for reasoning quantity, since fewer tokens do not necessarily mean fewer or more efficient reasoning steps. Its identification of step-merging as a specific reward-hacking pathology that token-count-penalized RL is prone to in later training stages is a concrete, previously under-documented failure mode directly relevant to every length-penalty-based overthinking mitigation in this archive, and its LLM-judged reasoning-category shift (toward pivotal/substantive content, away from digression and redundant verification) gives independent supporting evidence for the archive's broader claim that trace length and reasoning quality are distinct dimensions.

## Entities

- **Concepts**: step-based reward (vs. token-count penalty), optimal step count (S*), reward hacking via step merging, dynamic training-stopping criterion
- **Methods**: Step Pruner (SP), [GRPO](../../../../wiki/methods/grpo.md), CCoT (baseline), CoD (baseline), [CoT-Valve (baseline)](../../../../wiki/methods/cot-valve-baseline.md), Model Merge / Long-to-Short Reasoning (baseline), [O1-Pruner (baseline)](../../../../wiki/methods/o1-pruner-baseline.md), [ShorterBetter (baseline)](../../../../wiki/methods/shorterbetter-baseline.md), TrainEfficient (baseline)
- **Datasets**: DeepScaleR-preview (training, 40K problems), [AIME24](../../../../wiki/datasets/aime-2024.md), [MATH500](../../../../wiki/datasets/math500.md), [GSM8K](../../../../wiki/datasets/gsm8k.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md)

Tags: `overthinking`, `efficient-reasoning`, `reward-hacking`, `step-based-reward`, `reinforcement-learning`

## Abstract

Large Reasoning Models (LRMs) demonstrate strong performance on complex tasks but often suffer from excessive verbosity, known as “overthinking.” Existing solutions via reinforcement learning (RL) typically penalize generated tokens to promote conciseness. However, these methods encounter two challenges: responses with fewer tokens do not always correspond to fewer reasoning steps, and models may develop hacking behavior in later stages of training by discarding reasoning steps to minimize token usage. In this work, we introduce Step Pruner (SP), an RL framework that steers LRMs toward more efficient reasoning by favoring compact reasoning steps. Our step-aware reward function prioritizes correctness while imposing penalties for redundant steps, and withholds rewards for incorrect responses to prevent the reinforcement of erroneous reasoning. Moreover, we propose a dynamic stopping mechanism to prevent hacking behavior caused by step merging. Extensive experiments across four reasoning benchmarks demonstrate that SP achieves state-of-the-art accuracy while significantly reducing response length. For instance, on AIME24, SP reduces token usage by 69.7%.

---

Record id: `doi:10.18653/v1/2026.findings-acl.94`
