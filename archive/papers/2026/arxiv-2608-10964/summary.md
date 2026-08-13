<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# CARE: Confidence-Aware Reasoning for Reliable Medical VQA

- **Authors**: Yuetian Du, Yucheng Wang, Zhenyuan Chen, Luyuan Chen, Rongyu Zhang, Jinjian Zhang, Wei Zhou, Zhijie Xu, Ming Kong, Zhan Zhou, Jie Liu, Qiang Zhu
- **Venue**: cs.CV
- **Published**: 2026-08-11
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.10964>
- **PDF**: <https://arxiv.org/pdf/2608.10964v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.40, test-time-scaling 0.25

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Reinforcement Fine-Tuning (RFT) has enabled medical Multimodal Large Language Models (MLLMs) to produce Chain-of-Thought (CoT) reasoning for visual question answering, yet these models suffer from $\textit{confidence miscalibration}$---a systematic gap between expressed certainty and actual diagnostic accuracy that undermines clinical trust. We propose $\textbf{CARE}$, a $\textbf{C}$onfidence-$\textbf{A}$ware medical $\textbf{RE}$asoning framework that jointly optimizes accuracy and calibration through a dual-stage pipeline. First, a scalable Medical-CoT synthesis provides structured cold-start data for Supervised Fine-Tuning. Second, Group Relative Policy Optimization (GRPO) with a novel $\textbf{Confidence-Aware Reward (CAR)}$ mechanism ties the model's confidence to diagnostic correctness within the reward signal. Across three Medical VQA benchmarks, $\textbf{CARE}$ achieves the highest diagnostic accuracy while obtaining the lowest Expected Calibration Error and Hallucination Rate, establishing a foundation for trustworthy clinical decision support. Our code is available at https://github.com/anotherbricki/CARE.

---

Record id: `arxiv:2608.10964`
