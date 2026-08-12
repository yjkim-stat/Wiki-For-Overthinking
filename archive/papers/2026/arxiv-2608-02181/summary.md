<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Start Classifying: Categorical Critics for LLM Reinforcement Learning

- **Authors**: Zhijian Zhou, Long Li, Xuan Zhang, Zongkai Liu, Yulei Qin, Ke Li, Xing Sun, Xiaoyu Tan, Chao Qu, Yuan Qi
- **Venue**: cs.LG
- **Published**: 2026-08-03
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.02181>
- **PDF**: <https://arxiv.org/pdf/2608.02181v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-evaluation 0.25, reasoning-training 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Proximal Policy Optimization (PPO) for large language models typically trains its critic by mean-squared-error (MSE) regression on scalar value targets. Although scalar MSE is statistically valid for estimating the conditional expected return, sparse binary rewards in reinforcement learning with verifiable rewards (RLVR) make critic optimization and calibration especially consequential: small value errors directly distort the scalar advantages used by PPO. We study whether a classification-based training objective can improve this critic signal. HL-Gauss PPO replaces the scalar MSE head with a categorical predictor over a discretized value support, trained by cross-entropy against smoothed HL-Gauss targets. Its output is decoded to a scalar expectation for standard GAE and PPO; the actor update is therefore unchanged and is not distributional. Across mathematical reasoning, tool-augmented math, and Search-R1, and on both Qwen2.5 and Qwen3 backbones, HL-Gauss PPO consistently improves over strong PPO and DAPO baselines. Controls with one-hot, two-hot, and Bernoulli two-bin critics show that neither a larger output head nor binary classification alone explains the gains. On a common collection of reasoning prefixes, HL-Gauss improves Brier score and calibration error and yields more symmetric, lower-variance advantages. These results position categorical value learning as an effective optimization surrogate for PPO critics in RLVR.

---

Record id: `arxiv:2608.02181`
