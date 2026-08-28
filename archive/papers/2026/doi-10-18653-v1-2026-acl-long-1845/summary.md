<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# AttnPO: Attention-Guided Process Supervision for Efficient Reasoning

- **Authors**: Shuaiyi Nie, Dingsiyu, Wenyuan Zhang, Linhao Yu, Tianmeng Yang, Yao Chen, Weichong Yin, Yu Sun, Hua Wu, Tingwen Liu
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1845/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1845.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1845
- **Topics**: overthinking
- **Relevance score**: overthinking 0.67

## In one line

Discovers Key-Focus Heads (KFHs) -- a small subset of attention heads that, during final-answer generation, naturally attend more to essential reasoning steps than redundant ones -- and builds ATTNPO, an RL framework that rescales GRPO's outcome-level advantage per reasoning step using KFH attention scores, cutting reasoning length 55-61% while improving accuracy +2.9 to +7.3 points on DeepSeek-R1-Distill-Qwen-1.5B/7B.

## Problem

Outcome-supervised RL with length penalties treats all reasoning steps uniformly, applying the same credit/penalty to every step in a response regardless of whether it was essential or redundant, which fails to effectively shorten reasoning without degrading accuracy; process-supervised alternatives (sample-based marginal-gain estimation, reward-model-based first-correct-answer detection) fix this but are resource-intensive (extra sampling or a trained reward model) and prone to inaccurate credit assignment.

## Contributions

- discovery of Key-Focus Heads, a small subset of attention heads whose attention weights during final-answer generation naturally distinguish essential from redundant reasoning steps, requiring no extra sampling or reward model
- ATTNPO, a low-overhead process-supervised RL framework using KFH attention scores to rescale GRPO's outcome-level advantage per step via two complementary attenuation strategies (positive-advantage attenuation for redundant steps, negative-advantage attenuation for essential steps)
- best-or-second-best efficiency-accuracy trade-off (Average Efficiency Score) across six math benchmarks and two model scales versus outcome-supervised, process-supervised and adaptive-mode baselines, with generalization to out-of-domain coding/QA/science tasks despite math-only training
- evidence that KFHs are stable under RL training, sparse (few heads suffice), and behaviorally interpretable (their attenuation reduces confused/reflective phrase frequency specifically)

## Method

Segments each reasoning trace into steps via special transition phrases (confused/progression/summary phrases like 'Wait', 'First', 'Therefore'), then probes DeepSeek-R1-Distill-Qwen-1.5B/7B's attention heads during final-answer generation (after </think>) for Key-Focus Heads (KFHs) -- heads whose attention weights on essential vs. redundant steps (labeled by 3-LLM-judge consensus on an easy, high-accuracy probing subset) achieve high Step Ranking Accuracy (top heads reach 95-96% SRA; most heads are near-random). KFHs are found mainly in middle-to-late layers, stable across RL training checkpoints, and only a small top-N set is needed (ensembling more heads gives diminishing returns). ATTNPO (Attention-guided Policy Optimization) uses the top-N KFHs' attention scores to compute a per-step redundancy score and a response-specific, difficulty-aware baseline threshold, then rescales the GRPO/RLOO outcome-level advantage per step via two complementary strategies applied only to correct responses: Positive-Advantage Attenuation reduces the reinforcement given to steps scored below the baseline (redundant) to discourage over-encouraging them, while Negative-Advantage Attenuation zeros out the penalty on steps scored above the baseline (essential) when the response as a whole received a negative advantage, protecting necessary reasoning from being suppressed.

## Results

Trained on DeepScaleR-Preview with VeRL, ATTNPO achieves the best or second-best Average Efficiency Score across all six in-domain math benchmarks (GSM8K, MATH500, AMC23, OlympiadBench, AIME2024, AIME2025) at both 1.5B and 7B scale, beating outcome-supervised RL baselines (TLMRE, ThinkPrune, DIET, ACPO, Laser variants), process-supervised RL baselines (LC-R1, VSRM-R++, S-GRPO, DEPO, DECS), and reported adaptive-mode methods (AdaptThink, AutoThink). At 1.5B: 61% average length reduction with +7.3 points accuracy versus the base model (e.g. AIME2024: 54% length reduction with +9.6 accuracy points); at 7B: 55% length reduction with +2.9 accuracy points. Versus TLMRE specifically (the outcome-level-advantage baseline ATTNPO builds on), ATTNPO achieves 23% (1.5B) / 31% (7B) further length reduction with only 0.4/0.6-point accuracy cost. Generalizes to out-of-domain LiveCodeBench, GPQA-Diamond and MMLU despite training only on math, with reduced length and maintained or slightly improved accuracy at both scales. Pass@k analysis (k=2 to 128) on AIME2024/2025 shows ATTNPO matches or exceeds the base model's exploration capacity across sampling budgets, and under fixed token budgets (2048-32768) ATTNPO outperforms both the base model and TLMRE at tight budgets while matching TLMRE at loose budgets with substantially shorter outputs. Ablations show Positive-Advantage Attenuation alone drives most of the length reduction; adding Negative-Advantage Attenuation further improves accuracy with little added length change; removing the difficulty-aware baseline/magnitude modulation shortens responses further but degrades accuracy, confirming conservative compression on harder problems is necessary. Behavioral analysis shows Confused-Phrase (redundant self-reflection) frequency drops sharply during ATTNPO training while Summary-Phrase frequency rises slightly, consistent with reduced redundant reflection and more consolidated reasoning.

## Limitations

Experiments are conducted only on 1.5B and 7B models due to limited computational resources, though the paper reports consistent effectiveness across both scales tested. Training uses only mathematical datasets, chosen because they provide readily available and accurate verifiable reward signals; while LiveCodeBench/GPQA/MMLU evaluations show generalization to out-of-domain tasks, the paper anticipates further improvement would require verifiable training data from broader domains that was not available.

## Why it matters here

- **overthinking**: Central to the topic: identifies an intrinsic, near-cost-free signal (a small set of attention heads that already distinguish essential from redundant reasoning steps at inference time) for step-level overthinking detection, avoiding the extra sampling or reward-model cost of prior process-supervised methods, and uses it to achieve one of the stronger reported efficiency-accuracy trade-offs in the archive (55-61% length reduction with accuracy *gains* rather than losses). Its finding that KFHs are stable across RL checkpoints and generalize to out-of-domain tasks suggests essential-vs-redundant step structure is a fairly robust property of how these models already organize their reasoning, not something that has to be trained in from scratch.

## Entities

- **Concepts**: Key-Focus Heads (KFHs), Step Ranking Accuracy (SRA), Stepwise Outcome-level Advantage Rescaling, difficulty-aware advantage attenuation
- **Methods**: ATTNPO (Attention-guided Policy Optimization), Key-Focus Heads (KFH) probing, GRPO / RLOO, TLMRE (baseline), ThinkPrune, DIET, ACPO, Laser (outcome-supervised baselines), LC-R1, VSRM-R++, S-GRPO, DEPO, DECS (process-supervised baselines)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH500](../../../../wiki/datasets/math500.md), [AMC23](../../../../wiki/datasets/amc23.md), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md), [AIME2024](../../../../wiki/datasets/aime-2024.md), [AIME2025](../../../../wiki/datasets/aime-2025.md), [LiveCodeBench-v6](../../../../wiki/datasets/livecodebench-v6.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), [MMLU](../../../../wiki/datasets/mmlu.md), [DeepScaleR-Preview (training)](../../../../wiki/datasets/deepscaler-preview-training.md)

Tags: `overthinking`, `process-supervision`, `attention-mechanism`, `reinforcement-learning`, `efficient-reasoning`

## Abstract

Large reasoning models trained with reinforcement learning and verifiable rewards (RLVR) achieve strong performance on complex reasoning tasks, yet often overthink, generating redundant reasoning without performance gains. Existing trajectory-level length penalties often fail to effectively shorten reasoning length and degrade accuracy, as they uniformly treat all reasoning steps and lack fine-grained signals to distinguish redundancy from necessity. Meanwhile, process-supervised methods are typically resource-intensive and suffer from inaccurate credit assignment. To address these issues, we propose ATTNPO, a low-overhead process-supervised RL framework that leverages the model’s intrinsic attention signals for step-level credit assignment. We first identify a set of special attention heads that naturally focus on essential steps while suppressing redundant ones. By leveraging the attention scores of these heads, We then employ two sub-strategies to mitigate overthinking by discouraging redundant steps while preserving accuracy by reducing penalties on essential steps. Experimental results show that ATTNPO substantially reduces reasoning length while significantly improving performance across 9 benchmarks.

---

Record id: `doi:10.18653/v1/2026.acl-long.1845`
