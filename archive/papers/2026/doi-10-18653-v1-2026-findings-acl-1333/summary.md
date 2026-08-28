<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Stabilizing Efficient Reasoning with Step-Level Advantage Selection

- **Authors**: Han Wang, Xiaodong Yu, Jialian Wu, Jiang Liu, Ximeng Sun, Mohit Bansal, Zicheng Liu
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1333/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1333.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1333
- **Topics**: overthinking
- **Relevance score**: overthinking 0.62

## In one line

Shows that short-context (4K-token) post-training alone -- with pure GRPO and no length-aware reward at all -- already induces reasoning compression comparable to dedicated length-control RL methods, isolating training context length as a confound in prior efficient-reasoning work; but this compression destabilizes training because truncated-yet-correct rollouts get zero reward, so Step-level Advantage Selection (SAS) zeros the advantage of low-confidence steps in correct rollouts and high-confidence steps in verifier-failed rollouts, cutting average reasoning length 30%+ while improving Pass@1 by 3.79 points over the strongest length-aware baseline.

## Problem

Efficient-reasoning RL methods typically post-train under a much shorter context window (e.g. 4K tokens) than the base model's original training context (16-24K tokens), a confound between context-length effects and explicit length-aware reward design that has not been isolated; separately, when context is genuinely restricted, standard GRPO assigns rollout-level (not step-level) advantages, so a rollout truncated before reaching an answer receives zero reward even if its intermediate reasoning was entirely correct, injecting noisy, misaligned credit into training and destabilizing policy updates.

## Contributions

- an isolation of training context length as a confound in prior efficient-reasoning RL work: short-context post-training with pure GRPO and no length-aware reward already produces substantial reasoning compression comparable to dedicated length-control methods, but with degrading, unstable accuracy over training
- a diagnosis that this instability stems from truncated rollouts receiving zero reward for often-correct intermediate reasoning (~29% of an 8K-correct sample set becomes verifier-failed when truncated to 4K), injecting misaligned credit into standard rollout-level GRPO advantages
- Step-level Advantage Selection (SAS), zeroing the advantage of low-confidence steps in correct rollouts and high-confidence steps in verifier-failed rollouts, using only the policy's own token-log-probabilities as a step-confidence signal (validated against an external PRM, nDCG@k=0.90)
- state-of-the-art accuracy-efficiency trade-off across five math benchmarks and generalization to three out-of-domain general-reasoning benchmarks, with substantially more stable training dynamics (higher, more stable policy entropy) than uncorrected short-context GRPO

## Method

First isolates the effect of training context length alone: trains a long-context-capable base model (DeepScaleR-1.5B-Preview) with pure GRPO under a fixed 4K context window and a correctness-only reward (no length term at all), finding this alone induces substantial compression comparable to dedicated length-control baselines (LAPO, ThinkPrune) but with degrading, increasingly unstable accuracy over training. Diagnoses the cause: re-running the rule-based verifier on 8K-length rollouts truncated to 4K shows ~29% of originally-correct responses become verifier-failed after truncation, mostly losing only the final boxed answer or closing steps of an otherwise-correct derivation -- meaning a substantial fraction of 'incorrect' rollouts under short-context training are not logically flawed, just incomplete, and pure GRPO systematically penalizes their genuinely-good intermediate reasoning. Proposes Step-level Advantage Selection (SAS): partitions each rollout into reasoning steps (delimited by double newlines) and computes each step's confidence as the mean token-level log-probability under the current policy. For correct rollouts, the lowest-confidence fraction r of steps (ratio r=0.3 tuned) have their GRPO advantage zeroed out (masking redundant or low-confidence detours from reinforcement, while retaining positive advantage on the reliable majority). For verifier-failed rollouts, the highest-confidence fraction r of steps have their advantage zeroed (shielding likely-correct-but-truncated intermediate reasoning from undue negative penalization, while the remaining, less-confident steps retain their original negative advantage). This is a training-signal modification only -- no architecture change, no auxiliary reward model, no additional forward passes or rollouts.

## Results

On five math benchmarks (AIME24/25, MATH, AMC, OlympiadBench), SAS achieves the best accuracy-efficiency trade-off (AES=0.46) among all compared methods, improving average Pass@1 by more than 2 points over the base DeepScaleR-1.5B-Preview model (52.37%->54.54%) while reducing output length by ~1,700 tokens (5118->3407), and beating the strongest length-aware baselines (LAPO-I, ThinkPrune-4K, L1-Max) which either under-compress (LAPO/ThinkPrune, weaker efficiency gains despite comparable/lower accuracy) or over-compress at accuracy cost (L1-Max: most aggressive compression, but lower accuracy, e.g. AIME24 25.63% vs. SAS's 39.79%). Pure short-context GRPO (GRPO-4K, no length reward) already compresses substantially and slightly improves accuracy over the base model on average (53.61% vs. 52.37%), confirming context length itself is a previously-underexamined but strong compression signal independent of explicit length rewards -- but its accuracy is markedly volatile across training steps (Figure 2b) while SAS remains stable, and SAS's policy entropy stays substantially higher and more stable throughout training (Figure 3) versus GRPO-4K's rapid entropy collapse into brittle, repetitive reasoning patterns. Results extend to three out-of-domain general-reasoning benchmarks (GPQA-Diamond, LSAT, MMLU) with a similar pattern: SAS preserves or improves accuracy with substantially shorter outputs (highest AES of 0.46 among stable methods), while pure short-context GRPO again shows accuracy degradation relative to the base model on these unseen domains, indicating over-compression when uncorrected. Ablations isolate each design choice: restricting SAS to only correct-rollout masking ('Only Correct') drops AES from 0.46 to 0.43 and lengthens output, confirming the verifier-failed-rollout shielding component specifically matters for stabilizing training against truncation-induced noisy credit; replacing confidence-based step selection with random step selection degrades AES to 0.38, confirming gains depend on *which* steps are selected, not merely sparsifying the advantage signal; a token-level (rather than step-level) granularity variant underperforms (AES 0.39 vs. 0.46) with lower accuracy and longer outputs, confirming semantically-meaningful step aggregation is more effective than fine-grained per-token masking. A validation check finds strong agreement (nDCG@k = 0.9022) between the policy's own token-log-probability-based step confidence ranking and an external Process Reward Model's (Qwen2.5-Math-PRM-7B) step-quality ranking on MATH500, supporting that cheap intrinsic log-probabilities are a reliable proxy for step quality without needing an auxiliary trained verifier. A selection-ratio sweep (r from 0.1 to 0.9) shows r=0.3 is optimal (highest AES 0.46) but performance remains reasonably robust across the full range (AES stays above 0.36 even at extreme ratios), and SAS adds only ~17% wall-clock training overhead versus standard GRPO (327.15s vs. 279.08s per step), from step segmentation and advantage computation rather than extra forward passes or rollouts.

## Limitations

The paper's context-length isolation experiment is conducted on a single base model (DeepScaleR-1.5B-Preview, 1.5B parameters); generalization of the short-context-compression finding to larger models is not directly tested. SAS still incurs a measurable (~17%) training-time overhead versus standard GRPO from step segmentation and per-step confidence computation, though the paper argues this is practically acceptable given no extra rollouts or forward passes are needed. The step-delimiter choice (double newline) is a fixed heuristic rather than a learned or task-adaptive segmentation.

## Why it matters here

- **overthinking**: Directly and methodologically important: it isolates a confound in prior efficient-reasoning RL literature -- much of the reported length reduction attributed to explicit length-aware rewards may actually be, or be confounded with, a byproduct of the shorter training context window itself -- a caution worth applying when reading any length-penalty RL method's claimed compression gains elsewhere in this archive. Its step-level credit-assignment fix (distinguishing truncated-but-correct reasoning from genuinely-redundant reasoning) is also a specific, general-purpose training-stability technique relevant to any RL-based overthinking mitigation that risks penalizing good reasoning caught by an incomplete or noisy verifier signal.

## Entities

- **Concepts**: overthinking (via short-context-induced reasoning compression), truncation-induced noisy credit assignment, step-level advantage selection, step-level confidence score, verifier-failed-but-correct rollout
- **Methods**: Step-level Advantage Selection (SAS), [GRPO (Group Relative Policy Optimization)](../../../../wiki/methods/grpo.md), L1-Max / LCPO (baseline), ThinkPrune-4K (baseline), LAPO-I (baseline)
- **Datasets**: DeepScaleR-Preview-Dataset (training, ~40K problems: AIME 1984-2023, AMC pre-2023, Omni-MATH, Still), [AIME24](../../../../wiki/datasets/aime-2024.md), [AIME25](../../../../wiki/datasets/aime-2025.md), [MATH](../../../../wiki/datasets/math.md), [AMC](../../../../wiki/datasets/amc.md), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), [LSAT](../../../../wiki/datasets/lsat.md), [MMLU](../../../../wiki/datasets/mmlu.md)

Tags: `overthinking`, `reinforcement-learning`, `GRPO`, `context-length`, `training-stability`, `step-level-credit-assignment`

## Abstract

Large language models (LLMs) achieve strong reasoning performance by allocating substantial computation at inference time, often generating long and verbose reasoning traces. While recent work on efficient reasoning reduces this overhead through length-based rewards or pruning, many approaches are post-trained under a much shorter context window than base-model training, a factor whose effect has not been systematically isolated. We first show that short-context post-training alone, using standard GRPO without any length-aware objective, already induces substantial reasoning compression—but at the cost of increasingly unstable training dynamics and accuracy degradation. To address this, we propose Step-level Advantage Selection (SAS), which operates at the reasoning-step level and assigns a zero advantage to low-confidence steps in correct rollouts and to high-confidence steps in verifier-failed rollouts, where failures often arise from truncation or verifier issues rather than incorrect reasoning. Across diverse mathematical and general reasoning benchmarks, SAS reduces average reasoning length by over 30% while improving Pass@1 accuracy by 3.79 points over the strongest length-aware baseline, yielding a better accuracy–efficiency trade-off.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1333`
