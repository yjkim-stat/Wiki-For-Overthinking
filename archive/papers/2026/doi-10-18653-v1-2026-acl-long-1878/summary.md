<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Scaling Reasoning, Losing Control: Evaluating Instruction Following in Large Reasoning Models

- **Authors**: Tingchen Fu, Yafu Li, Jiawei Gu, Xiaoye Qu, Yu Cheng
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1878/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1878.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1878
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

MathIF is a 420-query, 15-constraint controlled benchmark showing that as large reasoning models' chain-of-thought grows longer via reasoning-oriented SFT/RL, their instruction-following obedience degrades -- even the best open model (Qwen3-14B) satisfies only 50.71% of constraints strictly, and artificially lengthening CoT (budget forcing) or reasoning-oriented training both directly and measurably erode compliance, exposing a persistent intelligence-obedience trade-off.

## Problem

Existing instruction-following benchmarks (IFEval, FollowBench) use queries simple enough to be solved without deep reasoning, so they fall within an Instruct model's performance envelope and cannot reveal how a large reasoning model's obedience behaves under its actual real-world use case: long, effortful chain-of-thought reasoning on hard problems, leaving unmeasured whether reasoning capacity and instruction adherence trade off against each other.

## Contributions

- MathIF, a controlled, objectively-evaluable (Python-verifiable) instruction-following benchmark embedded within mathematical reasoning, with 15 constraints across 4 categories and single/double/triple compositional combinations across 5 difficulty sources
- a large-scale evaluation of 26 recent LRMs revealing systematically poor instruction-following (even the best open model reaches only 50.71% strict compliance), that model scale alone does not determine controllability, and that adding constraints reduces reasoning correctness across difficulty levels
- empirical dissection of the intelligence-obedience trade-off from three angles -- error analysis by CoT length bin, comparison of SFT/SFT+RL/cold-start-RL post-training paradigms, and inference-time/training-time CoT-length interventions -- consistently showing longer or reasoning-oriented-trained CoT degrades instruction-following, while shorter/capped CoT (or repeating the constraint near the answer) partially restores it at a reasoning-accuracy cost

## Method

Builds MathIF, a controlled evaluation framework embedding 15 Python-verifiable constraints (four categories: length, lexical, format, affix) into math problems spanning five difficulty sources (GSM8K, MATH500, Minerva, OlympiadBench, AIME2024/25), including compositional double- and triple-constraint queries (420 total samples), and measures both hard accuracy (all constraints satisfied) and soft accuracy (fraction satisfied) alongside math-solving correctness with vs. without constraints, across 26 recent LRMs (1.5B to 70B+, open and closed) spanning small/medium/large scale tiers. Investigates the mechanism via three angles: (1) fine-grained error analysis correlating CoT length bins with instruction-following accuracy; (2) comparing three post-training paradigms (SFT-only, SFT+RL, cold-start RL) using GRPO on Qwen2.5/Qwen2.5-Math backbones, with and without a format-aware reward bonus; (3) inference-time and training-time interventions -- artificially extending CoT via budget forcing (appending 'Wait' tokens) and, conversely, capping maximum RL rollout length or repeating the constraint at the end of the CoT.

## Results

All open-source LRMs exhibit poor instruction-following despite strong closed-source results (o3-mini, Gemini-2.5-pro-preview and GPT-5 reach 70.71-83.33% hard accuracy); the best open model (Qwen3-14B) reaches only 50.71% hard accuracy, and most models fail to satisfy the majority of constraints. Model scale alone does not predict controllability: DeepSeek-R1-Distill-Llama-70B (42.62% HAcc) underperforms the far smaller Qwen3-4B (44.05% HAcc), and within-series scaling trends (e.g. Qwen3-8B, Qwen3-32B) deviate unpredictably from expectation. A trade-off exists between instruction-following and reasoning correctness: for most models, math-solving correctness drops when constraints are added (e.g. up to -40.09% relative for DeepSeek-R1-Distill-Qwen-1.5B), and this correctness-drop pattern holds across difficulty levels -- surprisingly, the drop rate on GSM8K (easiest) is sometimes even higher than on AIME (hardest), indicating the trade-off is general rather than confined to easy or hard problems specifically. Constraint type matters more than problem difficulty for compliance: length constraints are easiest to satisfy, lexical/format constraints demand finer token-level control and reduce accuracy, and affix constraints are hardest; hard accuracy deteriorates sharply as the number of compositional constraints increases (single->double->triple) while soft accuracy stays comparatively stable. Across all three models tested (DeepSeek-R1-Distill-Llama-8B, Qwen3-0.6B, Qwen3-32B), both hard and soft accuracy decline consistently as CoT length increases, suggesting longer reasoning dilutes attention to the original constraint by widening its contextual distance from the final answer. Comparing training paradigms: both SFT and RL reliably boost math-reasoning correctness (e.g. Qwen2.5-7B correctness rising from 23.10 to 29.11-40.65 depending on the pathway) but consistently *decrease* instruction-following (Qwen2.5-1.5B and Qwen2.5-7B both lose more than 10 points in soft accuracy after SFT or RL versus their base counterparts), with trained models sometimes performing worse on instruction-following than their untrained base -- reasoning-oriented post-training does not merely overlook obedience but actively erodes it. A format-aware reward bonus yields slight instruction-following improvement for Qwen2.5-1.5B/7B but negligible effect on the math-specialized series. Artificially extending CoT via budget forcing (appending 'Wait' 2 to 8 times) steadily degrades soft accuracy on DeepSeek-R1-Distill-Qwen-1.5B, directly confirming the causal direction (longer CoT -> worse instruction-following). Capping the maximum RL rollout length during training shows the inverse trend: shorter length caps (1k tokens) improve both reasoning correctness (28.73 vs. 36.13 baseline is a drop; but shows an interior optimum around a specific length) and instruction-following relative to longer caps (8k), i.e. controlling CoT length during training is a lever on this trade-off. A simple remedy -- repeating the original constraint at the end of the CoT (immediately before the final answer) -- clearly improves instruction-following (HAcc/SAcc) on all three tested models (e.g. Qwen3-32B SAcc 62.82->68.34) at a modest correctness cost (Qwen3-32B correctness 70.00->63.81), confirming both the mechanism (contextual distance dilutes attention to constraints) and that the trade-off can be partially, not fully, mitigated.

## Limitations

Evaluation is restricted to 26 LRMs in the text modality; benchmarking large vision-reasoning models is left for future work. The training-paradigm investigation mainly uses GRPO for RL training due to its widespread practical adoption, and other RL algorithms are left unexplored for this analysis. MathIF's constraints are restricted to those automatically verifiable by Python for scalable, deterministic evaluation; more practical instructions requiring human evaluation are not considered.

## Why it matters here

- **overthinking**: Central to the topic and complementary to length-reduction papers elsewhere in the archive: it demonstrates a distinct, previously underexamined cost of long reasoning -- not accuracy plateauing, but the model's ability to obey the user's explicit instructions actively degrading as chain-of-thought grows, whether via reasoning-oriented training (SFT/RL) or via artificially extended CoT (budget forcing). Its causal mechanism (longer CoT widens the contextual distance between the instruction and the final answer, diluting attention to it) gives a concrete, testable reason why 'more thinking' can be actively harmful beyond wasted compute, and its constraint-repetition mitigation is a cheap, general-purpose intervention that other reasoning-length-control methods in this archive could adopt.

## Entities

- **Concepts**: intelligence-obedience trade-off, hard accuracy / soft accuracy, compositional constraints, instruction-constraint contextual distance dilution
- **Methods**: MathIF (compositional Python-verifiable constraint benchmark), budget forcing (CoT-length inference-time extension), GRPO (RL training), constraint-repetition intervention
- **Datasets**: MathIF (new, 420 constrained math queries), [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH500](../../../../wiki/datasets/math500.md), [Minerva](../../../../wiki/datasets/minerva.md), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md), [AIME2024](../../../../wiki/datasets/aime-2024.md), [AIME2025](../../../../wiki/datasets/aime-2025.md), [DeepScaler (training)](../../../../wiki/datasets/deepscaler-training.md)

Tags: `overthinking`, `instruction-following`, `chain-of-thought-length`, `reasoning-oriented-training`, `controllability`

## Abstract

Instruction-following is essential for aligning large language models (LLMs) with user intent. While recent reasoning-oriented models exhibit impressive performance on complex mathematical problems, their ability to adhere to natural language instructions remains underexplored. In this work, we introduce MathIF, a dedicated benchmark for evaluating instruction-following in mathematical reasoning tasks. Our empirical analysis reveals a consistent tension between scaling up reasoning capacity and maintaining controllability, as models that reason more effectively often struggle to comply with user directives. We find that models tuned on distilled long chains-of-thought or trained with reasoning-oriented reinforcement learning often degrade in instruction adherence, especially when generation length increases. Furthermore, we show that even simple interventions can partially recover obedience, though at the cost of reasoning performance. These findings highlight a fundamental tension in current LLM training paradigms and motivate the need for more instruction-aware reasoning models.

---

Record id: `doi:10.18653/v1/2026.acl-long.1878`
