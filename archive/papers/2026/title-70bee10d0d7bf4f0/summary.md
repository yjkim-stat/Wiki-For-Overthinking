<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Training Large Reasoning Models Efficiently via Progressive Thought Encoding

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10007286>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

A parameter-efficient fine-tuning method that compresses intermediate reasoning into compact representations so large reasoning models can be RL-trained and run under a fixed-size cache without the memory blowup of long rollouts.

## Problem

RL training of large reasoning models requires long rollouts for outcome-based rewards, and autoregressive decoding under a full KV cache dominates training time and memory; sliding-window cache strategies bound memory but disrupt long-context reasoning and degrade performance.

## Contributions

- A parameter-efficient fine-tuning method (Progressive Thought Encoding) that lets LRMs reason under a fixed-size cache without backpropagating through full-cache rollouts.
- Reduced training-time memory usage for RL of LRMs while keeping constant memory during inference.
- Consistent accuracy gains over LoRA and a baseline across three models and six math benchmarks.

## Method

Progressive Thought Encoding progressively encodes intermediate reasoning steps into compact representations during RL training, so the model can be trained with outcome-based rewards under a fixed-size KV cache without needing to backpropagate through the full-length rollout cache, while inference also runs under constant memory.

## Results

On Qwen2.5-3B-Instruct, Qwen2.5-7B-Instruct, and DeepSeek-R1-Distill-Llama-8B across six math benchmarks, the method reports +19.3% average improvement over LoRA and +29.9% over the baseline, with up to +23.4 absolute points on AIME2024/2025 under tight cache budgets.

## Limitations

The abstract does not state the specific benchmarks beyond AIME2024/2025, nor does it report wall-clock or FLOP costs, and no failure modes or domains where the method underperforms are described.

## Why it matters here

- **overthinking**: The method targets the cost side of the accuracy/length tradeoff directly: instead of shortening reasoning, it makes long-rollout RL training and long-CoT inference tractable under a fixed compute/memory budget, which is a mechanism for sustaining test-time compute scaling rather than a method for deciding when a model should stop thinking.

## Entities

- **Concepts**: fixed-size KV cache under RL rollouts, compact latent encoding of intermediate reasoning
- **Methods**: Progressive Thought Encoding, LoRA (baseline comparison)
- **Datasets**: six widely used mathematical benchmarks (including AIME2024, AIME2025)

Tags: `kv-cache`, `rl-training`, `memory-efficiency`, `lrm-training`, `parameter-efficient-finetuning`

## Abstract

Abstract Large reasoning models (LRMs) excel on complex problems but face a critical barrier to efficiency: reinforcement learning (RL) training requires long rollouts for outcome-based rewards, where autoregressive decoding dominates time and memory usage. While sliding-window cache strategies can bound memory, they disrupt long-context reasoning and degrade performance. We introduce Progressive Thought Encoding, a parameter-efficient fine-tuning method that enables LRMs to reason effectively under fixed-size caches. By progressively encoding intermediate reasoning into compact representations, our approach eliminates the need to backpropagate through full-cache rollouts, thereby reducing training-time memory usage, while maintaining constant memory during inference. Experiments on three models, including Qwen2.5-3B-Instruct, Qwen2.5-7B-Instruct, and DeepSeek-R1-Distill-Llama-8B, across six widely used challenging mathematical benchmarks show consistent gains: our method achieves +19.3\% improvement over LoRA and +29.9\% over the baseline on average, with up to +23.4 absolute gains on AIME2024/2025 under tight cache budgets. These results demonstrate that Progressive Thought Encoding not only improves reasoning accuracy but also makes RL training of LRMs substantially more efficient and scalable under real-world memory constraints.

---

Record id: `title:70bee10d0d7bf4f0`
