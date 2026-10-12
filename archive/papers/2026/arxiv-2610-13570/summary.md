<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Constructing Pareto Frontiers of Optimal Reasoning Termination Methods for Overthinking in Reasoning Models

- **Authors**: Weixin Guan, Liang Li, Shiyu Xie, Jiapeng Liu, Bing Li, Peng Fu, Chengyang Fang, Xiaoshuai Hao, Can Ma, Weiping Wang
- **Venue**: cs.AI
- **Published**: 2026-10-12
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2610.13570>
- **PDF**: <https://arxiv.org/pdf/2610.13570>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.70

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Reasoning models can benefit from test-time scaling, but continued reasoning may become ineffective or harmful, a phenomenon termed overthinking. Evaluations against full thinking compare accuracy and token usage but lack references for overthinking severity and strategies' theoretical mitigation potential. To characterize overthinking at the model-task level, we first introduce Step-wise Truncation Probing (STP), repeatedly generating answers from multiple retained prefixes along each fixed sampled reasoning trajectory. Using each trajectory's earliest measured position attaining maximum empirical accuracy as a reference, we define Overthinking Ratio and Accuracy Degradation as the fraction of thinking tokens generated afterward and the accuracy decrease from this reference to full thinking, respectively. Secondly, we then formulate dynamic routing, fixed budgets, and dynamic early exit within a unified framework to quantify the theoretical mitigation potential of different termination strategies. Based on this unified framework, we use the complete STP measurements to construct a token-accuracy Pareto frontier for each strategy under a common normalized thinking-token budget. We further develop OTBench, a reusable benchmark built from the STP process, which produced 70.5B reasoning tokens and the corresponding probing measurements across six models and four benchmark groups.

---

Record id: `arxiv:2610.13570`
