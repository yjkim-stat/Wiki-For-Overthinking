<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# REATS: LLM Reasoning-based Ensemble Learning for Adaptive Time Series Forecasting

- **Authors**: Xu Zhang, Chang Xu, Hui Sun, Nan Ma, Zijian Zhang, Peng Wang, Wei Wang, Li Zhao
- **Venue**: cs.LG
- **Published**: 2026-08-10
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.10149>
- **PDF**: <https://arxiv.org/pdf/2608.10149v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.50, test-time-scaling 0.25

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Due to the diversity of real-world time series, no single forecasting model consistently dominates across all samples. Ensemble learning addresses this by combining complementary model strengths, yet existing methods rely on fixed rules or black-box models based solely on numerical inputs, failing to leverage LLM reasoning for interpretable weighting decisions. We propose REATS, which leverages LLM reasoning capabilities as an intelligent ensemble router that jointly processes textual temporal pattern descriptions and numerical features to produce interpretable, sample-adaptive ensemble weights through chain-of-thought reasoning. To enable effective LLM-based ensembling, we study its key design choices and propose: (i) a structured input pipeline that transforms raw time series into hybrid textual--numerical representations with fixed token cost, enabling rule-based chain-of-thought construction without API dependency, augmented with retrieved similar-sample priors; (ii) a diverse multi-row weight supervision scheme coupled with a token-efficient percentage-table format that reduces numerical complexity and mitigates LLM hallucinations; and (iii) a two-stage fine-tuning framework combining SFT with GRPO, where a reciprocal reward mapping transforms the continuous unbounded MSE gap into bounded signals with amplified near-oracle sensitivity, addressing the uniform sensitivity and outlier-dominated advantage compression inherent in naive reward designs for regression-based GRPO. Experiments on eight benchmarks demonstrate that REATS outperforms competitive ensemble baselines while providing natural language explanations and demonstrating strong transfer learning and out-of-domain generalization to unseen candidate models.

---

Record id: `arxiv:2608.10149`
