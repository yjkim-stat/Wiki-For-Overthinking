<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Think Smart, Not Hard: Difficulty Adaptive Reasoning for Large Audio Language Models

- **Authors**: Zhichao Sheng, Shilin Zhou, Chen Gong, Zhenghua Li
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1640/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1640.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1640
- **Topics**: overthinking
- **Relevance score**: overthinking 0.67

## In one line

Extends difficulty-adaptive reasoning-length control from text LLMs to Large Audio Language Models (LALMs), diagnosing that GRPO helps hard audio questions but SFT wins on easy ones (implying GRPO's reasoning on simple tasks is redundant/error-prone), then proposing two GRPO reward variants -- an outcome-based Group Ratio Difficulty Reward (GRDR) and a process-based, audio-attention-entropy-derived Group Audio Attention Difficulty Reward (GA2DR) -- that cut average reasoning length over 50% while improving accuracy, with GA2DR proving more robust to reward hacking because its difficulty signal is normalized per-batch from audio attention rather than from noisy rollout accuracy.

## Problem

Large Audio Language Models (LALMs) using chain-of-thought reasoning apply a one-size-fits-all reasoning strategy regardless of question difficulty, producing redundant overthinking on simple tasks and insufficient reasoning on complex ones; existing RL approaches for reasoning efficiency (length-penalty rewards with fixed thresholds, or LALM-specific 'when to think' gating) either ignore differences in question difficulty entirely or only decide whether to reason at all without regulating reasoning length once reasoning is invoked.

## Contributions

- a diagnostic analysis of LALM reasoning showing SFT excels on easy questions while GRPO excels on medium/hard ones, and that explicit reasoning helps mainly on hard questions -- evidence that reasoning on simple audio questions tends toward redundancy or error propagation
- two GRPO-compatible, difficulty-adaptive length-based rewards (GRDR: outcome-based via rollout-group accuracy; GA2DR: process-based via audio-attention entropy) that reuse training-time-available signals with no extra training cost
- empirical results across three benchmarks and two LALM backbones showing over 50% average reasoning-length reduction with improved (not merely preserved) accuracy, especially on medium/hard questions
- a diagnosis that outcome-based difficulty signals (GRDR) are vulnerable to reward hacking as rollout accuracy rises during training, while a process-based, batch-normalized attention-entropy signal (GA2DR) is more robust and generalizes better across benchmarks of varying difficulty

## Method

First conducts a diagnostic analysis comparing SFT and GRPO training on Qwen2-Audio-7B-Instruct/Qwen2.5-Omni-7B across an FS training set (audio grounding, sound classification, sound QA, spanning ~72K examples): SFT performs best on easy questions while GRPO shows superior performance on medium/hard questions, and within GRPO, explicit (chain-of-thought) prompting beats implicit (direct-answer) prompting substantially on hard questions but only marginally on easy ones (where implicit even edges ahead on some subsets), together suggesting reasoning on simple tasks tends toward redundancy or error propagation while harder questions genuinely benefit from deeper reasoning. Proposes two length-based rewards, both computed from variables already produced during training (no extra training-time cost): (1) Group Ratio Difficulty Reward (GRDR), outcome-oriented, classifying each question as easy/medium/hard by the count of correct samples in its GRPO rollout group (>=6/8, 3-5/8, <3/8), mapping to a discrete difficulty value gamma in {0, 0.5, 1}; (2) Group Audio Attention Difficulty Reward (GA2DR), process-oriented, computing the entropy of the last token's attention distribution over audio tokens in the final hidden layer, then min-max normalizing this entropy within each training batch to a continuous difficulty score (higher attention dispersion/entropy treated as a proxy for higher model uncertainty, hence higher difficulty). Both difficulty signals feed a shared length-based reward using a negative exponential function of normalized output length, with a difficulty-interpolated decay rate k(gamma): correct samples are rewarded more for shorter length (steeper decay for easy questions, flatter for hard ones, so an easy question needs a shorter length for the same reward as a longer hard-question response), and incorrect samples are penalized less severely as length increases (encouraging further reasoning specifically when currently wrong).

## Results

On MMAU-Test-Mini (primary benchmark), GRDR and GA2DR both consistently improve over a GRPO baseline and a prior Truncation Reward (TR) baseline, especially on medium/hard questions: for Qwen2.5-Omni-7B, GA2DR reaches 70.90% average accuracy (vs. GRPO's 69.40%, TR's 68.40%, GRDR's 70.20%), with statistically significant gains (p<=0.05) specifically on medium (61.21% vs. GRPO's 59.81%) and hard (33.20% vs. 27.41%) subsets under model-perspective difficulty annotation. Both methods achieve over 50% average reasoning-length reduction relative to the GRPO baseline across all difficulty levels: for Qwen2.5-Omni-7B, GRDR cuts average length on Easy samples from 185.38 to 54.49 tokens (~70% reduction) and on Hard from 146.18 to 68.32 (~53% reduction); GA2DR achieves comparable reductions (Easy: 54.58, Hard: 66.48). On the generalization benchmarks MMAU-v0515 and MMAR, GA2DR consistently achieves the best or near-best results (MMAU-v0515: 76.80% avg; MMAR: 62.90% avg, both best among compared methods), while GRDR's performance degrades noticeably on the more challenging MMAR benchmark (61.20% avg, close to GRPO's 59.90% and below GA2DR) -- attributed to GRDR's outcome-based difficulty signal being highly sensitive to noise in rollout samples: as model capability improves, rollout accuracy rises in later training steps, compressing the perceived difficulty gap between samples so most questions get treated as easy, leading to overly short optimization and reward hacking. GA2DR avoids this because its difficulty estimate is derived from audio-attention characteristics (not rollout accuracy) and is normalized within each batch, preserving discrimination among samples and reducing reward-hacking risk, yielding more stable cross-dataset performance. Length-vs-difficulty trend analysis shows a clear mismatch between human-perceived and model-perceived difficulty: from the human perspective, reasoning length stays similarly long on both easy and hard questions (mismatched with actual model-perceived difficulty), while from the model's own perspective (used by GRDR/GA2DR), reasoning length increases monotonically with difficulty as intended -- supporting the design choice to define difficulty from the model's own perspective rather than a fixed human-labeled scale. An ablation on the difficulty-interpolation factor k shows all fixed-k settings outperform the plain GRPO baseline (confirming the length-based reward itself helps), but every fixed-k setting underperforms the full adaptive-difficulty version, confirming that per-question difficulty adaptation (not just any length shaping) is necessary -- a single reward curve for all questions either over-penalizes easy questions or under-penalizes hard ones. An attention-layer ablation for GA2DR (first/mid/last layer) shows performance improves monotonically with layer depth, with the last layer yielding the best results, consistent with deeper layers capturing richer, more holistic semantic understanding of the question.

## Limitations

GRDR's outcome-based difficulty estimation is shown to be noise-sensitive and prone to reward hacking as training progresses and rollout accuracy improves, causing performance degradation on the harder MMAR benchmark specifically -- a limitation the paper diagnoses in its own proposed method rather than only in baselines. The paper does not report experiments beyond the tested LALM backbones (Qwen2-Audio-7B-Instruct, Qwen2.5-Omni-7B) and three primary evaluation datasets (with MMSU results deferred to an appendix), so generalization to substantially different audio-reasoning model architectures or modalities is not directly established within the reported main experiments.

## Why it matters here

- **overthinking**: Directly relevant as a cross-modal extension of this archive's central themes: it explicitly frames LALM reasoning behavior in terms of redundant overthinking on easy tasks and insufficient reasoning on hard ones, applies a difficulty-adaptive length reward analogous to text-domain approaches elsewhere in this archive, and adds a genuinely novel difficulty signal (audio-attention entropy) unavailable in text-only settings -- while its diagnosis that an outcome-based (rollout-accuracy) difficulty signal degrades via reward hacking as training progresses is a transferable caution for any GRPO-based length-shaping method in this archive that similarly derives difficulty from rollout correctness rather than a training-dynamics-robust internal signal.

## Entities

- **Concepts**: overthinking (in large audio language models), difficulty-adaptive reasoning length, Group Ratio Difficulty Reward (GRDR), Group Audio Attention Difficulty Reward (GA2DR), audio-attention entropy as a difficulty proxy, model-perspective vs. human-perspective difficulty
- **Methods**: [GRPO](../../../../wiki/methods/grpo.md), Group Ratio Difficulty Reward (GRDR), Group Audio Attention Difficulty Reward (GA2DR), Truncation Reward (TR, baseline), [SFT (baseline)](../../../../wiki/methods/sft-baseline.md)
- **Datasets**: FS (training, ~72K examples: AudioGrounding, VocalSound, TUT2017, Clotho-AQA, AVQA), AVQA (training), MMAU-Test-Mini, MMAU-Test-Mini-v05.15.25, MMAR, MMSU (appendix)

Tags: `overthinking`, `multimodal`, `audio`, `reinforcement-learning`, `GRPO`, `difficulty-adaptive-reasoning`

## Abstract

Large Audio Language Models (LALMs) employing the Chain-of-Thought paradigm have demonstrated remarkable reasoning capabilities. Though different problems naturally require varying depths of reasoning, existing methods often determine whether to perform reasoning, lacking fine-grained mechanisms to adapt reasoning length to problem complexity. As a result, LALMs often adopt a one-size-fits-all reasoning strategy, leading to redundant overthinking for simple tasks and insufficient reasoning for complex ones. In this paper, we conduct an in-depth analysis of LALM reasoning behavior and argue that effective and efficient reasoning should be adaptively aligned with task difficulty. To this end, we propose a difficulty-adaptive reasoning method for LALMs. Specifically, we introduce a reward function that dynamically links reasoning length to the model’s perceived problem difficulty, encouraging shorter reasoning for easy tasks and longer reasoning for more complex ones. Extensive experiments on three datasets demonstrate that our method consistently improves performance while reducing average reasoning length by at least 50%, achieving higher efficiency without sacrificing accuracy.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1640`
