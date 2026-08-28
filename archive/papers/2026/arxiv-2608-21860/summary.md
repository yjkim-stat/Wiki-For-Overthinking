<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ChainPrune: Evaluating and Reducing Redundancy in Long Chain-of-Thought Reasoning

- **Authors**: Weihang Pan, Zhengxu Yu, Yuxiang Zhang, Wenzhi Li, Zhongming Jin, Binbin Lin, Xiaofei He, Jieping Ye
- **Venue**: cs.LG
- **Published**: 2026-08-22
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.21860>
- **PDF**: <https://arxiv.org/pdf/2608.21860v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## In one line

ChainPrune merges semantically equivalent steps from 16 sampled reasoning paths into a tree, picks Pareto-dominant short paths as DPO preference data, and fine-tunes with an added NLL term, cutting tokens 28.1% and reasoning steps 26.8% on two R1-distilled models without losing accuracy.

## Problem

Length-penalty methods for shortening long CoT reduce token count but leave the reasoning structure redundant -- the paper calls this 'pseudo-conciseness'. Its own Table 1 measures an instance: on AIME24 with R1-Distill-Qwen-7B, Kimi-1.5 cuts tokens from 7346 to 6144 while chain length rises from 253 to 306 steps. Optimizing one length axis can therefore worsen the other, and accuracy drops (0.5479 to 0.5125). The open question is how to compress the reasoning path itself rather than its surface token count.

## Contributions

- Names and measures 'pseudo-conciseness': token-length rewards that cut tokens while leaving or increasing the number of reasoning steps.
- Reasoning-path merging that consolidates 16 sampled paths into a tree by embedding cosine similarity, gated by a token-entropy check that rejects merges which raise predictive uncertainty.
- Pareto-dominant path selection over the joint (token length, chain length) objective, with a two-rule rejection filter requiring rejected samples to be worse on both axes.
- A DPO + NLL objective that counters reward synchronization collapse, shown in an identical-data ablation to lift the accuracy of two competing baselines as well.
- An LLM-as-a-Judge protocol scoring reasoning paths on faulty reasoning, invalid reflection and redundant steps, separating structural redundancy from token count.

## Method

Three stages. (1) Reasoning Paths Merging: sample K=16 paths per problem, embed each step, and merge a new step u into existing node v when cosine similarity >= theta_sim; to guard against lexically similar but logically different merges, the candidate merge is simulated and accepted only if the Shannon entropy of the token distribution over the whole chain does not increase (delta_H <= epsilon). (2) Multi-criteria Dominant Path Selection: among correct paths, minimize the joint efficiency score E(tau) = sqrt(l_token^2 + l_step^2), taking the uniquely Pareto-dominant path if one exists, else the shortest-token path on the Pareto front; rejected samples must be unambiguously worse on both axes -- correct-but-overlong (l_step >= l_step+ + 5 AND l_token >= 1.5 * l_token+) or incorrect-and-longer on both. (3) Preference Optimization: DPO plus a supervised NLL term on the preferred response, lambda-weighted, to counter what the paper calls reward synchronization collapse, where margin-based objectives lower the log-probability of chosen and rejected responses together.

## Results

All numbers are from 8xA100 fine-tuning of DeepSeek-R1-Distill-Qwen-7B and -1.5B; each evaluation is run 16 times and averaged. 7B vs base model: AIME24 accuracy 0.5479 -> 0.5833 with tokens 7346 -> 5688 (-22.6%) and chains 253 -> 225; AIME25 0.4229 -> 0.4250, 6892 -> 5351, 240 -> 189; AMC23 0.9047 -> 0.9125, 5407 -> 3771, 189 -> 122; LiveCodeBench 0.3127 -> 0.3498, 3961 -> 3048 (-23.0%), 166 -> 116; MATH500 0.9240 -> 0.9300, 3709 -> 2170. Headline averages: -28.1% tokens, -26.8% steps. 1.5B accuracy also rises on all four (AIME24 0.3104 -> 0.3292, AIME25 0.2167 -> 0.2458, AMC23 0.7016 -> 0.7250, LiveCodeBench 0.1455 -> 0.1734). Both length baselines lose accuracy relative to base on 7B AIME24 (Kimi-1.5 0.5125, DAST reproduce 0.5375, SFT 0.5437). LLM-as-a-Judge on MATH500 with GPT-o1, DeepSeek-R1 and Qwen-QwQ majority-voted: faulty reasoning 102 -> 43 (-57.8%), invalid reflection 124 -> 47 (-62.1%), redundant steps 132 -> 45 (-65.9%). Table 2 is the only place all-response averages are given (All Tokens 4621 -> 2643, All Chains 146 -> 72). Ablation (Table 3, identical training data): adding the NLL term rescues both baselines -- Kimi-1.5 AIME24 0.5125 -> 0.5583, DAST 0.5375 -> 0.5833 -- so part of the accuracy gain is attributable to the NLL term rather than to the tree merging.

## Limitations

Stated: the work is offline preference optimization only; extension to online RL such as PPO was not implemented for time and resource reasons. Noticed by the reader: (a) token and chain length in Table 1 are averaged over correct answers only, so a method that solves more hard problems is charged for their length -- the paper flags this in the caption but supplies all-response averages for MATH500 alone, leaving the AIME/AMC/LiveCodeBench length claims confounded with accuracy; (b) Kimi-1.5 and DAST are reproductions, not the released systems, and Kimi-1.5 is a different scale; (c) a 'reasoning step' is segmented lexically by '\n\n' following Qwen convention, so chain length measures paragraph breaks rather than reasoning acts; (d) the merge thresholds theta_sim and epsilon carry the semantic-equivalence judgement but the main text reports neither their values nor a sensitivity analysis; (e) training data is the cleaned MATH set only (9,967 pairs), with LiveCodeBench the sole out-of-domain evaluation; (f) the redundancy counts come from three LLM judges by majority vote, with human review only of high-disagreement cases; (g) both backbones are 1.5B/7B R1 distillations, so nothing is shown for frontier-scale reasoning models.

## Why it matters here

- **overthinking**: Supplies a measured counterexample to the assumption that token count is a sufficient overthinking metric. On AIME24 with R1-Distill-Qwen-7B, Kimi-1.5's length reward cuts tokens 7346 -> 6144 while chain length rises 253 -> 306 and accuracy falls 0.5479 -> 0.5125: the intensity metric improves as the phenomenon worsens. This bears directly on the archive's trace-based measurement family, which reads a proxy off a single run -- token count and step count are shown here to move in opposite directions under intervention, so a claim about overthinking intensity is relative to which of the two was measured. The paper also supplies a redundancy decomposition (faulty reasoning / invalid reflection / redundant steps) judged separately from length, and its own Table 1 caption states the confound the archive should apply to any length comparison: averaging length over correct answers only means a more accurate method is charged for the harder problems it newly solves.

## Entities

- **Concepts**: [Overthinking](../../../../wiki/concepts/overthinking.md), Pseudo-Conciseness, Chain Length, Reasoning Path Merging, Pareto-Dominant Path Selection, Reward Synchronization Collapse, Gradient Entanglement, Direct Preference Optimization, LLM-as-a-Judge, [Redundant Reasoning Steps](../../../../wiki/concepts/redundant-reasoning-steps.md), Invalid Reflection
- **Methods**: ChainPrune, [Direct Preference Optimization (DPO)](../../../../wiki/methods/direct-preference-optimization-dpo.md), DPO + NLL regularization, [SimPO](../../../../wiki/methods/simpo.md), Supervised Fine-Tuning, Kimi-1.5 length reward, [DAST](../../../../wiki/methods/dast.md), Semantic node merging, Pareto dominance selection, LLM-as-a-Judge majority voting
- **Datasets**: MATH (cleaned, 9,967 problem-answer pairs, training), [MATH500](../../../../wiki/datasets/math500.md), [AMC23](../../../../wiki/datasets/amc23.md), [AIME24](../../../../wiki/datasets/aime-2024.md), [AIME25](../../../../wiki/datasets/aime-2025.md), LiveCodeBench (v5, Aug 2024 - Jan 2025)

Tags: `overthinking`, `efficient reasoning`, `chain-of-thought`, `dpo`, `preference optimization`, `reasoning compression`, `pseudo-conciseness`, `chain length`, `llm-as-a-judge`

## Abstract

Chain-of-Thought (CoT) reasoning has significantly enhanced the multi-step problem-solving capabilities of large language models (LLMs) by introducing explicit intermediate reasoning. However, advanced Large Reasoning Models (LRMs) often exhibit overthinking behaviors, including excessively long reasoning steps, redundant steps, and high computational overhead. Existing token-length reward strategies aim to promote concise outputs, but often result in pseudo-conciseness, where token count is reduced, yet redundant reasoning persists, leading to longer and less structurally efficient chains. To address these limitations, we propose ChainPrune, a novel reasoning path semantic structural optimization method to efficiently and controllably synthesize self-generated high-quality training data. We initially consolidate self-generated reasoning paths into a tree-based structure, followed by a multi-criteria dominant path selection process for preference data construction that formulates shallow reasoning trajectories while preserving essential reasoning steps. To further enhance the quality of reasoning, we incorporate a DPO-based preference learning method combined with supervised loss, effectively mitigating false reward suppression. This innovative integration significantly enhances both the efficiency and effectiveness of our reasoning framework. Comprehensive experimental results demonstrate significant reductions in step length and computational overhead, while maintaining or even enhancing accuracy.

---

Record id: `arxiv:2608.21860`
