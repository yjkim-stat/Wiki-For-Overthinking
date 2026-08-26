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

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large Reasoning Models (LRMs) such as OpenAI o1 and DeepSeek-R1 have shown remarkable reasoning capabilities by scaling test-time compute and generating long Chain-of-Thought (CoT). Distillation post-training on LRMs-generated data is a straightforward yet effective method to enhance the reasoning abilities of smaller models, but faces a critical bottleneck: we found that distilled long CoT data poses learning difficulty for small models and leads to the inheritance of biases (i.e., formalistic long-time thinking) when using Supervised Fine-tuning (SFT) and Reinforcement Learning (RL) methods. To alleviate this bottleneck, we propose constructing data from scratch using Monte Carlo Tree Search (MCTS). We then exploit a set of CoT-aware approaches, including Thoughts Length Balance, Fine-grained DPO, and Joint Post-training Objective, to enhance SFT and RL on the MCTS data. We conducted evaluation on various benchmarks such as math (GSM8K, MATH, AIME). instruction-following (Multi-IF) and planning (Blocksworld), results demonstrate our CoT-aware approaches substantially improve the reasoning performance of distilled models compared to standard distilled models via reducing the hallucinations in long-time thinking.

---

Record id: `doi:10.18653/v1/2025.acl-long.1145`
