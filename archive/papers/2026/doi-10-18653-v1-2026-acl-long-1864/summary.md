<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# AdaMix: Adaptive Mixing for Short and Long Reasoning Adapters

- **Authors**: Hao Luo, Xiao Yan, Xinyan Li, Qiming Zeng, Yuhao Lin, Shanshan Feng, Hao Wang, Jiawei Jiang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1864/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1864.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1864
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

AdaMix decouples efficiency and accuracy into two separately-trained LoRA adapters (a short adapter and a long adapter), then uses a BERT-based difficulty-aware router to predict a per-problem complexity coefficient that linearly interpolates the two adapters via task arithmetic, cutting DeepSeek-R1-Distill-Qwen-7B's average response length 54.9% while improving accuracy up to 4.8% across five math benchmarks and outperforming ShorterBetter/TLMRE/CoT-Valve/model-merging/SwitchCoT baselines on an accuracy-efficiency score.

## Problem

Jointly optimizing a single model for both reasoning depth (accuracy) and conciseness (efficiency) with one reward function creates conflicting optimization signals and training instability, while existing static model-merging or coarse binary long/short routing approaches lack the fine-grained adaptability needed to match reasoning intensity to each problem's actual difficulty.

## Contributions

- a decoupled optimization strategy training two specialized LoRA adapters (short/efficiency-oriented, long/accuracy-oriented) with distinct dynamic reward functions, avoiding the conflicting-objective instability of jointly optimizing accuracy and conciseness in one model
- a continuous, task-arithmetic-based interpolation mechanism between the two adapters, driven by a lightweight BERT-based difficulty-aware router that predicts a per-instance complexity coefficient, enabling fine-grained (not binary) adaptive reasoning intensity
- empirical evidence that AdaMix achieves the best accuracy-efficiency trade-off (Accuracy-Efficiency Score) among six compared baselines across two model scales and five math benchmarks, generalizing across backbones and (with lightweight router fine-tuning) across domains
- internal representation analysis (near-orthogonal weight updates, layer-depth specialization) confirming the decoupled training produces genuinely distinct short/long reasoning capabilities rather than redundant ones

## Method

Stratifies training data into easy and hard subsets via LLM-based difficulty scoring, then trains two LoRA adapters independently with GRPO: a short adapter, restricted to problems where both the target reasoning model and a non-reasoning counterpart (e.g. Qwen2.5-Math-Instruct) succeed, rewarded via a dynamic relative-length penalty (target length derived from the shorter model's average correct-response length, tolerance widening when group accuracy is low, and zero reward for incorrect responses); and a long adapter, restricted to 'reasoning frontier' problems where the model achieves partial (not zero, not full) success, rewarded via a capability-gated length penalty that only kicks in once group accuracy exceeds a threshold, so accuracy is prioritized before conciseness is refined. The two adapters are treated as task vectors and linearly interpolated via task arithmetic (theta_alpha = alpha*theta_long + (1-alpha)*theta_short) to synthesize any intermediate reasoning-intensity adapter. A BERT-based router is trained (via cross-entropy against a utility function balancing accuracy against a normalized length penalty) to predict, for each input problem, the interpolation coefficient alpha that should be applied at inference, letting the router dynamically compose a per-instance active adapter; a request-grouping strategy batches together requests assigned the same interpolation weight to keep multi-adapter serving overhead low.

## Results

Across five math benchmarks (GSM8K, MATH500, AMC23, AIME24, AIME25) on DeepSeek-R1-Distill-Qwen-1.5B and -7B, AdaMix reduces average response length by 54.2% (1.5B) / 54.9% (7B) while improving average accuracy by +1.2% / +1.9%, achieving the highest Accuracy-Efficiency Score (0.58 / 0.59) among all compared methods -- beating DPO, ShorterBetter (best token reduction at -83.6%/-66.0% but -17.5%/-9.3% accuracy loss), TLMRE, static ModelMerging, CoT-Valve, and SwitchCoT, all of which trade off more accuracy for less or comparable token reduction. On individual benchmarks, gains are largest on GSM8K (up to ~74-87% token reduction with maintained/improved accuracy) and hold with smaller but positive margins on the harder AIME24/25 sets. AdaMix generalizes across backbones (DeepSeek-R1-Distill-Llama-8B, Qwen3-4B) with consistent substantial length reduction and comparable-or-better accuracy on MATH500/AIME24/25, and transfers to out-of-math domains (code: LiveCodeBench, science: GPQA-Diamond, general knowledge: MMLU) with sustained length reduction (34-49%) though a modest zero-shot accuracy drop that is largely recovered by fine-tuning only the lightweight router on a small mixed-domain dataset (without retraining either adapter). The router-selected interpolation weight tracks problem difficulty as intended: for easy (Level 1) problems the router assigns dominant weight to the short adapter, and the long-adapter proportion rises monotonically through Level 5, where the long adapter becomes primary -- confirming difficulty-adaptive routing rather than a fixed policy. Layer-wise weight-update visualization shows the short adapter's updates concentrate in shallow-to-middle layers while the long adapter's dominate in deeper layers, and cosine similarity between the two adapters' weight matrices stays near zero across all layers, confirming decoupled training induces genuinely distinct (near-orthogonal) internal representations rather than redundant ones. A frontier-model (GPT-5) router achieves more aggressive token reduction (-60.4%) but a lower AES (0.50) than AdaMix's lightweight BERT router (0.58) due to a larger accuracy drop (-5.7% vs. +1.2%), showing the purpose-trained router better balances the tradeoff than a much larger general-purpose model used as a router.

## Limitations

The router's perception of problem difficulty is inherently domain-dependent, so extending AdaMix to significantly different domains typically requires lightweight fine-tuning to recalibrate the routing module (as shown for code/science/knowledge tasks), even though the underlying adapters transfer without retraining. The framework uses a discrete set of candidate interpolation weights (e.g. {0, 0.1, ..., 1.0}) rather than continuous regression, which theoretically limits fine-grained modulation of reasoning behavior compared to a continuous approach, though the paper reports this discrete resolution is empirically sufficient to distinguish necessary reasoning depths on the benchmarks tested.

## Why it matters here

- **overthinking**: Central to the topic: directly frames overthinking as models applying a uniform, computation-intensive reasoning strategy regardless of problem difficulty, and proposes a fine-grained fix (continuous adapter interpolation guided by a difficulty router) rather than the binary long/short routing or single-objective RL penalties common elsewhere. Its explicit finding that the short and long adapters develop near-orthogonal, layer-depth-specialized internal representations gives mechanistic grounding for why decoupling accuracy and efficiency objectives (rather than optimizing them jointly) resolves the training-instability problem several other archive papers on length-penalty RL report.

## Entities

- **Concepts**: dual-adapter decoupled optimization, difficulty-aware adaptive routing, task-arithmetic adapter interpolation, capability-gated length penalty
- **Methods**: AdaMix (dual-adapter decoupled optimization + difficulty-aware routing), [LoRA](../../../../wiki/methods/lora.md), [GRPO](../../../../wiki/methods/grpo.md), task arithmetic (adapter interpolation), [DPO (baseline)](../../../../wiki/methods/dpo-baseline.md), [ShorterBetter (baseline)](../../../../wiki/methods/shorterbetter-baseline.md), [TLMRE (baseline)](../../../../wiki/methods/tlmre-baseline.md), [ModelMerging (baseline)](../../../../wiki/methods/modelmerging-baseline.md), [CoT-Valve (baseline)](../../../../wiki/methods/cot-valve-baseline.md), SwitchCoT (baseline)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH500](../../../../wiki/datasets/math500.md), [AMC23](../../../../wiki/datasets/amc23.md), [AIME24](../../../../wiki/datasets/aime-2024.md), [AIME25](../../../../wiki/datasets/aime-2025.md), DeepMath-103K (training, difficulty-annotated), [LiveCodeBench](../../../../wiki/datasets/livecodebench.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), [MMLU](../../../../wiki/datasets/mmlu.md)

Tags: `overthinking`, `adaptive-reasoning`, `model-merging`, `reinforcement-learning`, `difficulty-aware-routing`

## Abstract

Large Reasoning Models (LRMs) have achieved remarkable success on complex tasks by generating detailed Chain-of-Thought (CoT) reasoning. However, they tend to apply a uniform, computation-intensive deep reasoning strategy to all problems, leading to unnecessary overhead on simple tasks. This significantly hinders their efficiency in real-world applications. While existing methods have improved reasoning efficiency to some extent, they still face critical challenges such as conflicting objectives, limited adaptability. To address these limitations, we propose AdaMix, an adaptive reasoning framework via decoupled optimization. To mitigate optimization conflicts, AdaMix first constructs two specialized adapters: an efficiency-oriented short adapter and an accuracy-oriented long adapter. It then incorporates a difficulty-aware routing model that assesses problem complexity to predict a reasoning intensity coefficient. This coefficient is used to dynamically interpolate a mixed adapter from the two base adapters, enabling fine-grained reasoning control. Our experiment demonstrates that our AdaMix reduces the average response length of DeepSeek-R1-Distill-Qwen-7B by 54.9% while improving accuracy by up to 4.8% on five mathematical datasets, thus indicating a favorable accuracy-efficiency trade-off.

---

Record id: `doi:10.18653/v1/2026.acl-long.1864`
