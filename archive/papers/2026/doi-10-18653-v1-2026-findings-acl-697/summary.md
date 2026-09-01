<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# O1-Pruner: Length-Harmonizing Fine-Tuning for O1-Like Reasoning Pruning

- **Authors**: Haotian Luo, Haiying He, Yibo Wang, Shiwei Liu, Wei Li, Xiaochun Cao, Dacheng Tao, Naiqiang Tan, Li Shen
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.697/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.697.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.697
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## In one line

O1-Pruner identifies 'length disharmony' -- shorter responses often achieve equal or higher accuracy than longer ones, at both the instance and distribution level -- and fine-tunes long-thought models with a PPO-style Length-Harmonizing Reward that rewards brevity relative to a reference model's own pre-sampled length/accuracy baseline, subject to an accuracy non-degradation constraint, cutting solution length by 34.7-40.5% while improving accuracy.

## Problem

Long-thought reasoning LLMs (O1-style) achieve strong accuracy via extended chain-of-thought but incur substantial inference-time overhead, and the paper identifies that these models struggle to allocate token budgets according to actual problem difficulty and reasoning redundancy -- a phenomenon the paper terms 'length disharmony', where shorter responses frequently achieve equal or higher accuracy than longer ones for the same problem.

## Contributions

- empirical documentation of 'length disharmony' at both the instance level (peak accuracy occurring at inconsistent length intervals across problems) and the distribution level (shorter responses on average achieving higher accuracy), establishing that longer reasoning is not systematically better
- Length-Harmonizing Fine-Tuning (O1-Pruner), formulating reasoning-length reduction as a constrained optimization problem (minimize length subject to non-degraded accuracy) and solving it via a PPO-style reward that compares the policy against its own reference-model baseline length and accuracy per problem
- an off-policy training strategy sampling exclusively from the fixed reference model, reducing training complexity versus on-policy resampling while still achieving strong performance
- 34.7-40.5% solution-length reduction with maintained or improved accuracy across MATH, GSM8K and AIME25 on two model sizes, and the shortest measured inference time among all compared methods

## Method

First empirically documents length disharmony via pre-sampling: 512 solutions per problem (64 MATH problems) with Marco-o1-7B and QwQ-32B, grouped into length-based intervals, showing (a) at the instance level, the length interval with peak accuracy is inconsistent across problems -- sometimes shortest, sometimes longest -- and relatively high accuracy is often preserved even in shorter-length intervals, and (b) at the distribution level, shorter response length is consistently associated with higher average accuracy across intervals. Formulates an RL optimization objective that shortens reasoning paths relative to a fixed reference policy pi_ref (typically the pre-fine-tuning model itself) while constraining that expected accuracy does not decrease, converting the constraint into a penalty term with weight lambda to get a Length-Harmonizing Reward R_LH(x,y) = L_ref(x)/L(y) - 1 + lambda*(A(x,y) - A_ref(x)), where L_ref(x) and A_ref(x) are the reference model's own pre-sampled mean length and mean accuracy for problem x (estimated via K samples from pi_ref before training). Because harder problems inherently need longer correct solutions (per the inference-time scaling law), the accuracy term ensures the model does not over-shorten on genuinely difficult problems -- for a problem with high baseline accuracy expectation, correctly solving it yields little accuracy reward so the model is pushed toward shortening; for a low-baseline-accuracy (hard) problem, correct solutions yield a large accuracy reward, discouraging premature shortening. Uses an off-policy, PPO-style training strategy that samples entirely from the fixed reference model pi_ref rather than the evolving policy pi_theta, avoiding the cost of repeated on-policy resampling during training. Fine-tunes Marco-o1-7B (full-parameter) and QwQ-32B-Preview (Freeze Fine-Tune, last 48 layers, due to compute constraints) on 5K MATH problem-answer pairs, evaluated on MATH, GSM8K, and AIME25 against Fast-Solving Prompt, SFT (trained on the two shortest correct solutions per problem), and DPO (shortest-vs-longest correct solutions as preference pairs) baselines, with an Accuracy-Efficiency Score (AES) composite metric penalizing accuracy loss more heavily than rewarding length reduction (gamma > beta in its weighted formula).

## Results

O1-Pruner achieves the best AES across all three datasets for both model sizes, substantially outperforming Fast-Solving Prompt, SFT, and DPO. On Marco-o1-7B, O1-Pruner reduces average solution length by 40.5% (1213 -> 630 tokens) while improving average accuracy from 56.8% to 59.0% across MATH/GSM8K/AIME25; on QwQ-32B-Preview, it reduces length by 34.7% (3221 -> 1915 tokens) with accuracy essentially maintained (71.2% -> 72.9%). Fast-Solving Prompt achieves moderate length reduction but at accuracy cost in most cases (its lower AES reflects this trade-off); SFT provides a better balance than prompting but with only marginal length-reduction gains; DPO achieves a reasonable balance but consistently falls short of O1-Pruner, notably showing a notable accuracy decrease on Marco-o1-7B. Inference-time measurements on one A800 GPU (vLLM) confirm the practical payoff: O1-Pruner achieves the shortest inference time among all compared methods for both models -- just over 1 minute for Marco-o1-7B (vs. ~2 minutes baseline) and about 4 minutes for QwQ-32B-Preview (vs. ~6 minutes baseline). A hyperparameter ablation on the constraint weight lambda (0/1/2/5) shows accuracy and required length both increase as lambda rises, with lambda=2 identified as the favorable Marco-o1-7B trade-off point. A difficulty-stratified ablation shows models trained on harder problem subsets produce longer solutions (reflecting problem complexity) and achieve higher accuracy from learning on more challenging examples, while training on easier data yields shorter outputs with no accuracy gains -- confirming O1-Pruner's length adjustment is difficulty-sensitive rather than uniform, and that its performance is tied to the difficulty composition of its training data.

## Limitations

Experiments are limited to models smaller than 32B parameters to ensure stable training and manageable compute cost; scaling behavior to larger long-thought models is untested. Evaluation focuses exclusively on mathematical reasoning tasks (MATH, GSM8K, AIME25), which provide a well-defined testbed for length/accuracy trade-off analysis but leave extension to other reasoning domains (e.g. commonsense or scientific problem solving) as future work. The off-policy training approach (sampling only from the fixed reference model rather than the evolving policy) simplifies training but is an approximation whose fidelity to a fully on-policy approach is not directly quantified.

## Why it matters here

- **overthinking**: Core paper for this topic, and already a repeatedly-cited baseline in this archive's other efficient-reasoning papers (Step Pruner, AutoL2S read this same session both compare against O1-Pruner): its central empirical claim, 'length disharmony' -- shorter responses often match or beat longer ones in accuracy, at both the per-instance and distribution level -- is one of the archive's foundational pieces of evidence that reasoning-trace length and reasoning quality are distinct dimensions, directly supporting the existing finding that 'reasoning-trace length is not a measure of overthinking.' Its reward design (comparing the trained policy against the untrained reference model's own baseline length/accuracy for the same problem, rather than a fixed global token budget) is a widely-imitated mechanism this archive's other length-penalty methods build on or contrast against.

## Entities

- **Concepts**: length disharmony, Length-Harmonizing Reward, accuracy non-degradation constraint, off-policy PPO-style fine-tuning, [Accuracy-Efficiency Score (AES)](../../../../wiki/concepts/accuracy-efficiency-score-aes.md)
- **Methods**: O1-Pruner (Length-Harmonizing Fine-Tuning), Fast-Solving Prompt (baseline), [SFT (baseline)](../../../../wiki/methods/sft-baseline.md), [DPO (baseline)](../../../../wiki/methods/dpo-baseline.md), GRPO (referenced technique)
- **Datasets**: MATH (training and evaluation), [GSM8K](../../../../wiki/datasets/gsm8k.md), [AIME25](../../../../wiki/datasets/aime-2025.md)

Tags: `overthinking`, `efficient-reasoning`, `length-penalty`, `reinforcement-learning`, `length-disharmony`

## Abstract

Recently, long-thought reasoning LLMs, such as OpenAI’s O1, adopt extended reasoning processes similar to how humans ponder over complex problems. This reasoning paradigm significantly enhances the model’s problem-solving abilities and achieves promising results. However, long-thought reasoning process leads to a substantial increase in inference time. A pressing challenge is reducing the inference overhead of long-thought LLMs while ensuring accuracy. In this paper, we identify that long-thought reasoning models struggle to effectively allocate token budgets based on problem difficulty and reasoning redundancies. To address this, we propose Length-Harmonizing Fine-Tuning (O1-Pruner), aiming at minimizing reasoning overhead while maintaining accuracy. This effective fine-tuning method first estimates the LLM’s baseline performance through pre-sampling and then uses RL-style fine-tuning to encourage the model to generate shorter reasoning processes under accuracy constraints. This allows the model to achieve efficient reasoning with lower redundancy while maintaining accuracy. Experiments on various mathematical reasoning benchmarks show that O1-Pruner not only significantly reduces inference overhead but also achieves higher accuracy, providing a novel and promising solution to this challenge.

---

Record id: `doi:10.18653/v1/2026.findings-acl.697`
