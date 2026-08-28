<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Learning While Staying Curious: Entropy-Preserving Supervised Fine-Tuning via Adaptive Self-Distillation for Large Reasoning Models

- **Authors**: Hao Wang, Hao Gu, Hongming Piao, Kaixiong Gong, Yuxiao Ye, Xiangyu Yue, Sirui Han, Yike Guo, Dapeng Wu
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.617/>
- **PDF**: <https://aclanthology.org/2026.acl-long.617.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.617
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

CurioSFT diagnoses that standard SFT causes 'entropy collapse' (overconfidence, narrowed exploration) that limits the subsequent RL stage in the SFT-then-RL pipeline, and fixes it with Self-Exploratory Distillation toward a self-generated, temperature-scaled teacher plus Entropy-Guided Temperature Selection that concentrates exploration on high-entropy reasoning-connector tokens while preserving low-entropy factual tokens, improving downstream RL accuracy by 5.0 points on average.

## Problem

The standard 'SFT-then-RL' post-training recipe for large reasoning models has SFT imitate expert demonstrations via cross-entropy loss, which drives overconfidence and narrows the model's generation diversity (entropy collapse), leaving the subsequent RL stage with a constricted search space to explore -- and naive entropy regularization during SFT is not a fix, since it indiscriminately flattens token distributions toward uniformity (including on low-entropy factual tokens) without improving meaningful exploration, and can induce knowledge forgetting.

## Contributions

- a diagnosis that standard cross-entropy SFT causes rapid entropy collapse that constricts the exploration space available to a subsequent RL stage, and that naive token-agnostic entropy regularization fails to fix this (it either does nothing or destabilizes training/forgets knowledge)
- Self-Exploratory Distillation, aligning the model toward a self-generated, temperature-scaled higher-entropy teacher that preserves token-probability ordering, encouraging exploration only within the model's own valid space
- Entropy-Guided Temperature Selection, adaptively assigning per-token teacher temperatures via binary search so exploration concentrates on high-entropy reasoning-connector tokens while low-entropy factual tokens stay stable
- empirical results showing CurioSFT improves both SFT-stage accuracy and, more importantly, the ceiling reachable by subsequent RL (+5.0 points average), outperforming single-stage hybrid SFT+RL alternatives, across multiple model backbones and both math and code domains

## Method

Self-Exploratory Distillation constructs a higher-entropy 'teacher' distribution by rescaling the current model's own logits with an increased temperature (exploiting that entropy increases monotonically with temperature), then distills the student toward this self-generated teacher via a KL-style loss (K2-loss) -- since the teacher strictly preserves the relative order of token probabilities, this encourages exploration only within the model's own valid exploration space rather than injecting uninformative entropy everywhere, and using a separate, EMA-updated teacher (rather than the live model) stabilizes the distillation target. Entropy-Guided Temperature Selection then adaptively assigns a per-token teacher temperature: for each token, an entropy increment is computed from a sigmoid function of how far the current token's entropy is above an 'entropy pivot' threshold, and a binary search finds the temperature that achieves that target entropy increment for the teacher distribution at that token -- so high-entropy tokens (reasoning connectors like 'wait') get a large entropy boost while low-entropy tokens (factual/deterministic content) are left nearly unchanged. Trained on OpenR1-Math-46K (Qwen2.5-Math-7B base) for SFT, then GRPO for the RL stage.

## Results

In the SFT stage, CurioSFT improves the in-distribution average from vanilla SFT's 48.5% to 51.0% (+2.5 points across AIME24/25, AMC23, MATH, Minerva, OlympiadBench) and the out-of-distribution average from 51.3% to 54.2% (+2.9 points across GPQA, MMLU-Pro, ARC-Challenge), while preserving higher token entropy (0.31->0.43, +0.12 nats) than vanilla SFT -- outperforming both naive entropy-loss regularization (which either barely changes entropy at low weight or causes 'entropy explosion'/training destabilization at higher weight, and still underperforms) and other SFT variants (GEM, DFT, PSFT). In the subsequent RL stage, the CurioSFT+GRPO pipeline reaches 58.7% in-distribution average (vs. 53.7% for vanilla SFT+RL, +5.0 points) and 61.7% OOD average (+2.4 points vs. 59.3%), with the largest gains on the hardest AIME benchmarks (39.2% vs. 32.1% AIME24 for SFT+RL) -- evidence that a better-preserved exploration space during SFT unlocks a higher RL performance ceiling, and CurioSFT+GRPO also outperforms single-stage hybrid SFT+RL methods (LUFFY, Prefix-RFT, RL-PLUS) that fuse demonstrations and exploration into one stage. Ablations confirm both components matter: removing Entropy-Guided Temperature Selection (fixed temperature) causes a clear OOD drop (54.2%->52.2%), and removing the separate teacher model (using the live model as its own teacher) causes modest performance degradation, supporting the role of a stable teacher signal. Restricting a naive entropy loss to only the top-20%-highest-entropy tokens (rather than all tokens) substantially improves OOD performance (51.3%->52.3%) versus applying it to all tokens, corroborating the paper's mechanistic claim that low-entropy tokens encode deterministic facts where forced entropy weakens factual consistency, while high-entropy tokens act as reasoning connectors that are the natural targets for exploration. Results generalize across two additional backbones (Qwen3-4B-Base, Llama-3.1-8B-Instruct) and to code generation tasks (HumanEval+, MBPP+, LiveCodeBench: +1.3 points average over vanilla SFT).

## Limitations

CurioSFT incurs additional training overhead versus vanilla SFT (an extra forward pass to compute the teacher distribution and per-token temperature search), though the paper reports this stays within a practical range (43.2->53.9 seconds per step). The approach is bounded by the base model's own intrinsic capabilities, since it relies on self-distillation to preserve and amplify the model's own latent exploration rather than introducing external signals -- the paper states benefits may be smaller when the base model lacks sufficient prior knowledge, and leaves incorporating external exploration signals to future work.

## Why it matters here

- **overthinking**: Not directly about overthinking: this paper addresses accuracy/exploration in the SFT-then-RL training pipeline for large reasoning models, not reasoning-trace length or the inference-time accuracy/efficiency tradeoff. It is tangential background on how the training methods used to produce reasoning models (which several overthinking-mitigation papers build on or evaluate) are themselves optimized, but does not measure or mitigate overthinking itself.

## Entities

- **Concepts**: entropy collapse, SFT-then-RL paradigm, self-exploratory distillation, entropy-guided temperature selection, ungrounded entropy, knowledge forgetting
- **Methods**: CurioSFT (Self-Exploratory Distillation + Entropy-Guided Temperature Selection), [GRPO](../../../../wiki/methods/grpo.md), vanilla SFT with entropy regularization, GEM, DFT, PSFT, LUFFY (hybrid SFT+RL baseline), Prefix-RFT (baseline), RL-PLUS (baseline)
- **Datasets**: OpenR1-Math-46K, [AIME24](../../../../wiki/datasets/aime-2024.md), [AIME25](../../../../wiki/datasets/aime-2025.md), [AMC23](../../../../wiki/datasets/amc23.md), [MATH](../../../../wiki/datasets/math.md), [Minerva](../../../../wiki/datasets/minerva.md), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), [MMLU-Pro](../../../../wiki/datasets/mmlu-pro.md), [ARC-Challenge](../../../../wiki/datasets/arc-challenge.md), [HumanEval+](../../../../wiki/datasets/humaneval.md), [MBPP+](../../../../wiki/datasets/mbpp.md), [LiveCodeBench](../../../../wiki/datasets/livecodebench.md), [TACO](../../../../wiki/datasets/taco.md), LeetCodeDataset

Tags: `SFT`, `reinforcement-learning`, `entropy-collapse`, `exploration`, `training-methodology`

## Abstract

The standard post-training recipe for large reasoning models, supervised fine-tuning followed by reinforcement learning (SFT-then-RL), may limit the benefits of the RL stage: while SFT imitates expert demonstrations, it often causes overconfidence and reduces generation diversity, leaving RL with a narrowed solution space to explore. Adding entropy regularization during SFT is not a cure-all; it tends to flatten token distributions toward uniformity, increasing entropy without improving meaningful exploration capability. In this paper, we propose CurioSFT, an entropy-preserving SFT method designed to enhance exploration capabilities through intrinsic curiosity. It consists of (a) Self-Exploratory Distillation, which distills the model toward a self-generated, temperature-scaled teacher to encourage exploration within its capability; and (b) Entropy-Guided Temperature Selection, which adaptively adjusts distillation strength to mitigate knowledge forgetting by amplifying exploration at reasoning tokens while stabilizing factual tokens. Extensive experiments on mathematical reasoning tasks demonstrate that, in SFT stage, CurioSFT outperforms the vanilla SFT by 2.5 points on in-distribution tasks and 2.9 points on out-of-distribution tasks. We also verify that exploration capabilities preserved during SFT successfully translate into concrete gains in RL stage, yielding an average improvement of 5.0 points. Code is available at https://github.com/HaoooWang/CurioSFT.

---

Record id: `doi:10.18653/v1/2026.acl-long.617`
