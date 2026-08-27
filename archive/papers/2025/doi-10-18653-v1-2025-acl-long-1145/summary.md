<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Marco-o1 v2: Towards Widening The Distillation Bottleneck for Reasoning Models

- **Authors**: Huifeng Yin, Yu Zhao, Minghao Wu, Xuanfan Ni, Bo Zeng, Hao Wang, Tianqi Shi, Liangying Shao, Chenyang Lyu, Longyue Wang, Weihua Luo, Kaifu Zhang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2025.acl-long.1145/>
- **PDF**: <https://aclanthology.org/2025.acl-long.1145.pdf>
- **DOI**: 10.18653/v1/2025.acl-long.1145
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## In one line

Marco-o1 v2 identifies 'formalistic long-time thinking' -- distilled small models mechanically replicating a large reasoning model's surface reasoning patterns (content repetition, over-reflection) without internalizing the underlying logic, often producing no final answer at all -- and fixes it by generating CoT training data from scratch via MCTS plus three CoT-aware post-training techniques (thought-length balance, fine-grained/masking-based DPO, joint SFT+DPO loss).

## Problem

Distilling long chain-of-thought reasoning from large reasoning models (e.g. DeepSeek-R1) into smaller models is a straightforward way to transfer reasoning capability, but the paper observes that distilled small models often exhibit 'formalistic long-time thinking' -- hallucinated content repetition and over-reflection that mechanically mimics the large model's surface reasoning style without internalizing its logic -- sometimes producing no final answer at all, a bias-inheritance and learning-difficulty problem that standard SFT/RL post-training does not address.

## Contributions

- identification of 'formalistic long-time thinking' -- small distilled models mechanically replicating a large reasoning model's surface patterns (repetition, over-reflection) without internalizing the reasoning logic, often failing to produce a final answer
- a tree-based CoT data construction framework building reasoning data from scratch via MCTS over typed thought nodes with multi-model coordination, rather than direct distillation from a large reasoning model's outputs
- three CoT-aware post-training techniques (Thoughts Length Balance, fine-grained/masking-based DPO, Joint SFT+DPO objective) shown to be orthogonal, complementary, and effective at reducing DPO-induced no-answer failures across math, planning and instruction-following tasks and multiple model families/sizes

## Method

Instead of directly distilling completions from a large reasoning model, constructs CoT training data from scratch via Monte Carlo Tree Search (MCTS) over a tree of typed 'thought nodes' (Sub-Task, Reflection, Hypothesis, Double-Check, Reclarify, Answer, etc., each with a role-specific prompt), using general (non-reasoning) LLMs -- Qwen2.5-72B-Instruct for generative nodes, Llama3.1-70B-Instruct for reflection/correction nodes -- so multi-model coordination reduces the risk of a single model repeating its own errors; nodes are selected via UCB, expanded by prompting, and rolled out to rule-checked correctness rewards that backpropagate up the tree, with error backtracking to an earlier node on failure. From the resulting search trees, extracts CoT data for SFT (picking the highest-reward or length-targeted correct path) and for DPO (pairing a correct path with an incorrect path sharing the shortest common prefix, to minimize spurious token-overlap). Three CoT-aware post-training methods address formalistic long-time thinking, empirically found to be induced primarily by DPO on long CoT: (1) Thoughts Length Balance -- using the longest CoT data for SFT but the shortest correct CoT data for DPO, since shorter DPO training paths were found to reduce 'no-answer' failures; (2) Fine-grained DPO -- combining conservative DPO (down-weighting potentially noisy preference labels) with masking-based DPO (zeroing the loss on shared-prefix tokens between chosen/rejected pairs so the model focuses only on the diverging content); (3) Joint Post-training Objective -- adding the SFT loss back into the DPO loss (L = L_DPO + alpha*L_SFT) to counteract the catastrophic forgetting DPO alone induces.

## Results

Evaluated on five benchmarks (GSM8K, MATH, AIME for math; Blocksworld for planning; Multi-IF in Chinese/English/other for instruction-following) across four base models (Llama-3.1-8B/3.2-1B-Instruct, Qwen2.5-7B/1.5B-Instruct). SFT on the MCTS-constructed data alone ('+ Our Data') beats both the un-tuned base model and a Sky-T1-based distillation baseline across nearly every model/benchmark, most sharply on smaller/weaker models -- e.g. Qwen2.5-1.5B-Instruct: GSM8K 67.5 (base) -> 66.7 (+Sky-T1) -> 74.6 (+Our Data); Blocksworld 1.0 -> 0.0 -> 5.4; Llama-3.2-1B-Instruct: AIME 0.0 -> 0.0 -> 0.0 but Blocksworld 0.2 -> 0.0 -> 5.6 and IF(other) 33.1 -> 7.5 -> 47.1. Progressively adding the three CoT-aware post-training methods on top of SFT (baseline 'Our LRM (SFT)') shows plain DPO alone causes a sharp jump in the no-answer rate (parenthetical percentages in Table 5) and a corresponding accuracy collapse (e.g. AIME 30.00% no-answer at baseline -> 55.00% after plain DPO, accuracy dropping 15.0 -> 8.3); each added technique (Data Balance, cDPO, Joint Loss, Masking) progressively reduces the no-answer rate and recovers/improves accuracy and instruction-following, with the full combined method (+Masking) reaching the best or near-best scores across most benchmarks (e.g. GSM8K 87.2, MATH 51.0, Blocksworld 12.6, IF-En 77.2/1.36% no-answer) while keeping no-answer rates comparable to or better than the SFT-only baseline. Applying MCTS at inference time (Test@N sampling, N repeated guesses) further improves solve rate on MATH: the fully post-trained model with MCTS decoding reaches Test@32 = 82.8% versus 79.2% without MCTS decoding and 75.8% for the plain Llama-3.1-8B-Instruct baseline.

## Limitations

Validated on math (GSM8K, MATH, AIME), planning (Blocksworld) and multilingual instruction-following (Multi-IF); the paper explicitly states future work is needed to extend the approach to a broader range of non-mathematical tasks including machine translation and multilingual/multimodal reasoning. The MCTS-based data construction and multi-model coordination pipeline (using two separate 70B-class LLMs for generation vs. reflection) adds construction-time compute and engineering complexity relative to directly distilling from a single teacher model's outputs, though the paper argues this is offset by reducing reliance on large teacher models overall.

## Why it matters here

- **overthinking**: Directly relevant, and gives a specific named mechanism -- 'formalistic long-time thinking' -- distinct from the more commonly discussed 'overthinking on easy problems': here the failure is that a distilled small model mimics the surface form of long reasoning (repeated near-duplicate steps, unresolved reflection loops) without the underlying capability the large teacher had, sometimes never reaching an answer at all. This is directly cited by the paper alongside the standard over-/under-thinking framing (Chen et al. 2024, 'Do NOT think that much') and offers a distillation-specific account of how long CoT training can produce degenerate reasoning length rather than useful reasoning length -- complementary to inference-time or RL-based overthinking accounts.

## Entities

- **Concepts**: formalistic long-time thinking (bias inheritance from distillation), MCTS-based tree CoT data construction, thought node (typed reasoning-step role), thoughts length balance, masking-based / fine-grained DPO, joint SFT+DPO post-training objective
- **Methods**: Monte Carlo Tree Search (MCTS)-based CoT data construction, conservative DPO (cDPO), masking-based DPO, joint SFT+DPO loss
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH](../../../../wiki/datasets/math.md), [AIME](../../../../wiki/datasets/aime.md), Blocksworld, Multi-IF

Tags: `overthinking`, `distillation`, `monte-carlo-tree-search`, `dpo`, `long-cot`

## Abstract

Large Reasoning Models (LRMs) such as OpenAI o1 and DeepSeek-R1 have shown remarkable reasoning capabilities by scaling test-time compute and generating long Chain-of-Thought (CoT). Distillation post-training on LRMs-generated data is a straightforward yet effective method to enhance the reasoning abilities of smaller models, but faces a critical bottleneck: we found that distilled long CoT data poses learning difficulty for small models and leads to the inheritance of biases (i.e., formalistic long-time thinking) when using Supervised Fine-tuning (SFT) and Reinforcement Learning (RL) methods. To alleviate this bottleneck, we propose constructing data from scratch using Monte Carlo Tree Search (MCTS). We then exploit a set of CoT-aware approaches, including Thoughts Length Balance, Fine-grained DPO, and Joint Post-training Objective, to enhance SFT and RL on the MCTS data. We conducted evaluation on various benchmarks such as math (GSM8K, MATH, AIME). instruction-following (Multi-IF) and planning (Blocksworld), results demonstrate our CoT-aware approaches substantially improve the reasoning performance of distilled models compared to standard distilled models via reducing the hallucinations in long-time thinking.

---

Record id: `doi:10.18653/v1/2025.acl-long.1145`
