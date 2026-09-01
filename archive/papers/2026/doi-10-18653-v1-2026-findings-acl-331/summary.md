<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Select2Reason: Efficient Instruction-Tuning Data Selection for Long-CoT Reasoning

- **Authors**: Cehao Yang, Xueyuan Lin, Xiaojun Wu, Chengjin Xu, Xuhui Jiang, Honghao Liu, Hui Xiong, Jian Guo
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.331/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.331.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.331
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## In one line

SELECT2REASON selects the top 10% of a large long-CoT instruction pool for SFT by jointly ranking questions on a learned difficulty score and (deduplicated) reasoning-trace length, matching or beating models trained on 8-94x more data.

## Problem

Supervised fine-tuning on large-scale long-CoT instruction sets synthesized by strong reasoning models is a cheaper alternative to RL for activating long-CoT reasoning, but training on hundreds of thousands of instructions is costly, and effective automatic strategies for selecting a small high-utility subset remain unexplored.

## Contributions

- an empirical finding that longer reasoning traces contain systematically more rethinking-behavior tokens, especially on hard questions, motivating trace length as a data-selection heuristic
- SELECT2REASON, combining a rollout-based difficulty-aware reward model with normalized reasoning-trace length via a weighted joint ranker for instruction-tuning data selection
- state-of-the-art or matching results using only 10% of a 196K-instruction pool, transferring without retraining to a separate 110K Chinese instruction pool, and cutting training time by ~75%

## Method

Motivated by an empirical finding that longer reasoning traces contain more 'rethinking tokens' (Wait, Alternatively, Maybe, However) especially on hard questions, SELECT2REASON scores each candidate instruction on two axes: (1) a difficulty-aware reward model trained to regress a continuous difficulty score derived from Monte Carlo rollout pass-rate against the base model, and (2) a normalized reasoning-trace length that deduplicates exact-repeat reasoning steps before counting (to penalize verbatim looping rather than reward it). The two rankings are combined via a weighted joint ranker (rank_j = w*rank_difficulty + (1-w)*rank_length, best at w=0.25) to select the top-K subset for SFT.

## Results

Fine-tuning Qwen2.5-Math-7B-Instruct on only the top 10% (19.6K of 196K) of OpenR1-Math-220k selected by SELECT2REASON matches or exceeds full-pool training (196K) and beats four baselines (random, diversity-based, longest-only, difficulty-only) across nine math benchmarks -- e.g. AIME24 Pass@1 0.433 vs. 0.465 for full-pool but with a ~75% reduction in training time (Table 4), and matches/exceeds OpenR1-Qwen-7B (94K samples) and DeepSeek-R1-Distill-Qwen-7B (800K samples) despite far less data. On a separate 110K-sample Chinese instruction pool, the same joint ranker (not retrained) still outperforms baselines, showing the difficulty/length signals transfer without retraining. Diversity-based selection (uniform category sampling) does not meaningfully outperform the full-pool baseline and sometimes overlaps it (e.g. Major@16 on AMC23), suggesting diversity alone is not a useful selection criterion here. A raw-rethinking-keyword-frequency selection metric consistently underperforms the length/difficulty joint ranker across AIME24/25 and AMC23, so the paper uses rethinking-token frequency only for qualitative validation, not as a direct selection signal. Models fine-tuned on SELECT2REASON-selected data use fewer rethinking tokens at inference than full-pool-trained models while matching or exceeding accuracy -- the paper reads this as more efficient exploratory reasoning resulting from higher-quality (not just longer) training data.

## Limitations

Training with the full pool retains a slight edge over the SELECT2REASON subset on OlympiadBench specifically, which the paper attributes to a generalization limitation of small high-quality subsets versus full-pool diversity on that particular benchmark. The reasoning-trace-length heuristic and rethinking-token analysis are validated primarily on mathematical reasoning; broader-domain generalization (logical reasoning, scientific/commonsense QA) is tested but with the same underlying instruction-selection method rather than a domain-specific one. The joint ranker's optimal weighting (w=0.25) is tuned empirically per this data regime.

## Why it matters here

- **overthinking**: Directly relevant and somewhat counter-intuitive relative to length-penalty approaches: instead of treating long reasoning traces as waste to be shortened at inference time, this paper treats them (when they contain genuine, non-duplicated rethinking steps) as a *positive* training signal -- selecting on longer, difficulty-matched traces for SFT produces a model that uses *fewer* rethinking tokens at inference while matching or beating full-data training. It separates 'long because working through something hard' from 'long because looping/repeating' via explicit deduplication, and shows a naive rethinking-keyword-frequency signal is actually a worse selection criterion than trace length itself -- a useful caution for any overthinking-measurement approach that treats keyword-frequency as a proxy for redundant reasoning.

## Entities

- **Concepts**: rethinking tokens, difficulty-aware reward model, joint ranker for instruction utility, reasoning-trace normalization (deduplication)
- **Methods**: difficulty-aware reward-model-as-judge, reasoning-trace-length-based selection, weighted joint ranker, supervised fine-tuning
- **Datasets**: [OpenR1-Math-220k](../../../../wiki/datasets/openr1-math-220k.md), Chinese-DeepSeek-R1-Distill-data (110K), [AIME 2024](../../../../wiki/datasets/aime-2024.md), [AIME 2025](../../../../wiki/datasets/aime-2025.md), [AMC 2023](../../../../wiki/datasets/amc23.md), [MATH-500](../../../../wiki/datasets/math500.md), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md), GAOKAO (2023/2024), GAOKAO-Math, [KAOYAN](../../../../wiki/datasets/kaoyan.md), [ZebraLogic](../../../../wiki/datasets/zebralogic.md), [GPQA](../../../../wiki/datasets/gpqa.md)

Tags: `data-selection`, `long-CoT`, `instruction-tuning`, `efficient-reasoning`, `reasoning-trace-length`

## Abstract

A practical approach to activate long chain-of-thoughts reasoning ability in large language models is to perform supervised fine-tuning on instruction datasets synthesized by strong large reasoning models, offering a cost-effective alternative to reinforcement learning. However, large-scale instruction sets incur significant training overhead, while effective strategies for automatic data selection still remain unexplored. We propose Select2Reason, a novel and efficient instruction-tuning data selection framework for long-CoT reasoning. From the perspective of emergence of rethinking behaviors like self-correction and backtracking, we investigate metrics that may determine the quality of long-CoT instructions. Select2Reason leverages a difficulty-aware reward model to estimate the learning value of questions and jointly incorporates a reasoning trace length-based heuristic through a weighted scheme for ranking to prioritize high-utility examples. Empirical results on OpenR1-Math-220k demonstrate that fine-tuning LLM on only 10% of the data selected by our method achieves performance competitive with or superior to full-data tuning and open-source baseline across nine competition-level mathematical benchmarks and four broader reasoning tasks. Further experiments highlight the scalability in varying data size, efficiency during inference, and adaptability to other instruction pools of Select2Reason with minimal cost.

---

Record id: `doi:10.18653/v1/2026.findings-acl.331`
