<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# SoftCoT: Soft Chain-of-Thought for Efficient Reasoning with LLMs

- **Authors**: Yige Xu, Xu Guo, Zhiwei Zeng, Chunyan Miao
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2025.acl-long.1137/>
- **PDF**: <https://aclanthology.org/2025.acl-long.1137.pdf>
- **DOI**: 10.18653/v1/2025.acl-long.1137
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

SoftCoT keeps the backbone LLM frozen and instead uses a small auxiliary assistant model plus a trainable projection module to generate instance-specific continuous 'soft thought' tokens that prime the LLM's chain-of-thought, avoiding the catastrophic forgetting that full-model fine-tuning for continuous-space reasoning (e.g. Coconut) causes on modern instruction-tuned LLMs, and improving accuracy on five reasoning benchmarks with only ~6 soft tokens versus 24 hard tokens needed by a discrete-token assistant baseline.

## Problem

Continuous-space ('soft') chain-of-thought reasoning methods like Coconut and Compressed CoT are more expressive than discrete token-by-token CoT, but require full-model fine-tuning with a language-modeling objective, which the authors show empirically causes catastrophic forgetting and net performance degradation when applied to modern, already-strong zero-shot-CoT instruction-tuned LLMs (LLaMA-3.1-8B, Qwen2.5-7B) -- unlike the older, weaker GPT-2 backbone these methods were originally validated on.

## Contributions

- an empirical identification that full-model fine-tuning for continuous-space CoT reasoning (as in Coconut, Compressed CoT) causes catastrophic forgetting and net accuracy degradation on modern, already-strong instruction-tuned LLMs, which prior work's GPT-2-backbone validation did not reveal
- SoftCoT, a frozen-backbone method using a small assistant model plus a trainable projection module to generate instance-specific soft thought tokens, avoiding forgetting while improving reasoning accuracy across five benchmarks
- evidence that soft thoughts are far more token-efficient than discrete hard-token prompts (6 vs. 24 tokens for comparable effect) and compose additively with self-consistency

## Method

SoftCoT freezes the backbone LLM entirely. A small, frozen assistant model (e.g. LLaMA-3.2-1B-Instruct) generates instance-specific continuous soft thought tokens from its own last-layer hidden states (rather than decoding discrete tokens), conditioned on a task instruction and the question. A trainable linear projection module maps these soft-thought representations from the assistant's embedding space into the backbone LLM's embedding space (bridging the representational/dimensional gap). The backbone LLM then generates its reasoning steps and final answer conditioned on its own fixed instruction plus the projected soft thoughts; only the projection module's parameters are trained (via next-token-prediction loss over the reasoning steps and answer, masking loss on the soft thoughts themselves), making training parameter-efficient and leaving the LLM's original weights and capabilities untouched.

## Results

On LLaMA-3.1-8B-Instruct across five benchmarks (GSM8K, an augmented harder ASDiv variant called ASDiv-Aug, AQuA, StrategyQA, Date Understanding), SoftCoT reaches 70.52% average accuracy versus 68.21% for zero-shot CoT, 69.67% for a discrete-token assistant baseline (Zero-Shot Assist-CoT), and only 68.49%/70.52%-losing scores for LoRA fine-tuning (68.49%, itself below zero-shot CoT) and a re-implemented Coconut (also below zero-shot CoT) -- confirming that full-model continuous-space fine-tuning degrades these strong backbones while SoftCoT's frozen-backbone approach improves them. The same pattern holds on Qwen2.5-7B-Instruct (SoftCoT 75.06% average vs. 70.29% zero-shot CoT, with LoRA and Coconut again both below the zero-shot baseline). SoftCoT achieves its optimal performance with only 6 soft thought tokens, whereas the discrete-token Zero-Shot Assist-CoT baseline needs 24 hard tokens to reach comparable effectiveness -- a 4x reduction, aligning with a similarly-reported 5x ratio in prior compressed-CoT work. SoftCoT's gains are largest on tasks (commonsense/StrategyQA) where the base LLM otherwise underperforms relative to mathematical reasoning, and it generalizes zero-shot to a held-out task (Date Understanding, which has no training data) when trained on other datasets. Combining SoftCoT with self-consistency (majority voting over N=10 reasoning chains) improves further over either self-consistency alone or SoftCoT alone (e.g. GSM8K: 81.03% at N=1 to 90.63% at N=10), indicating the two techniques are complementary rather than redundant. Assistant-model scale (0.5B/1.5B/7B, tested on Qwen2.5 series for GSM8K) has limited impact on final accuracy (83.70/84.85/84.90 for CoT baselines vs. 85.76/85.81/85.84 for SoftCoT), showing the gain comes from the soft-thought mechanism rather than the assistant's raw capacity.

## Limitations

SoftCoT does not fully replace the reasoning path itself -- the backbone LLM's own decoding stage still functions as the actual search process; soft thoughts primarily enrich the probability space for exploration rather than replacing it. Evaluated only on backbones around 7-8B parameters (LLaMA-3.1-8B-Instruct, Qwen2.5-7B-Instruct); scalability to substantially larger LLMs within the same model families is stated as an open question requiring further empirical validation.

## Why it matters here

- **overthinking**: Directly relevant: it targets reasoning efficiency by cutting the number of tokens needed to prime effective chain-of-thought (6 soft tokens vs. 24 hard tokens for equivalent effect), addressing the token-cost side of the accuracy-efficiency tradeoff, though its efficiency gain is in the prompting/priming stage rather than in the length of the model's own generated reasoning trace. Its central methodological finding -- that full-model fine-tuning for continuous reasoning wrecks a strong zero-shot-CoT model's existing capability, while a frozen-backbone, projection-only approach avoids this -- is a caution relevant to any overthinking-mitigation method that proposes retraining a capable reasoning model rather than steering or wrapping it.

## Entities

- **Concepts**: soft (continuous-space) chain-of-thought, catastrophic forgetting from CoT fine-tuning, assistant-model soft thought generation, parameter-efficient projection-only tuning
- **Methods**: soft (continuous-space) chain-of-thought, prompt tuning (assistant-model variant), projection module (trainable linear mapping), [self-consistency (majority voting)](../../../../wiki/methods/self-consistency-majority-voting.md), Coconut / LoRA fine-tuning (baselines)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), ASDiv / ASDiv-Aug (new, harder augmented variant), AQuA, [StrategyQA](../../../../wiki/datasets/strategyqa.md), Date Understanding (BIG-bench)

Tags: `overthinking`, `soft-cot`, `efficient-reasoning`, `catastrophic-forgetting`, `parameter-efficient-tuning`

## Abstract

Chain-of-Thought (CoT) reasoning enables Large Language Models (LLMs) to solve complex reasoning tasks by generating intermediate reasoning steps. However, most existing approaches focus on hard token decoding, which constrains reasoning within the discrete vocabulary space and may not always be optimal. While recent efforts explore continuous-space reasoning, they often require full-model fine-tuning and suffer from catastrophic forgetting, limiting their applicability to state-of-the-art LLMs that already perform well in zero-shot settings with a proper instruction. To address this challenge, we propose a novel approach for continuous-space reasoning that does not require modifying the LLM. Specifically, we employ a lightweight fixed assistant model to speculatively generate instance-specific soft thought tokens as the initial chain of thoughts, which are then mapped into the LLM’s representation space via a trainable projection module. Experimental results on five reasoning benchmarks demonstrate that our method enhances LLM reasoning performance through supervised, parameter-efficient fine-tuning. Source code is available at https://github.com/xuyige/SoftCoT.

---

Record id: `doi:10.18653/v1/2025.acl-long.1137`
