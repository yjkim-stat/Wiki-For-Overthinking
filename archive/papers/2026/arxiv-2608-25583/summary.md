<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# GRIP: Granular Reward-Guided Parameter Interpolation for Efficient Reasoning

- **Authors**: Lam So, Canhui Wu, Han Lin
- **Venue**: cs.CL
- **Published**: 2026-08-26
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.25583>
- **PDF**: <https://arxiv.org/pdf/2608.25583v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

GRIP fuses a reasoning model and an instruction (non-thinking) model of identical architecture by learning a separate sigmoid-controlled interpolation ratio per module (attention, FFN, embedding/LM-head), trained with an RL reward that favors correct and concise responses while keeping both source models frozen, cutting Qwen3-4B-Thinking's average generation length 27.0% while slightly improving average accuracy.

## Problem

Reasoning-oriented LLMs achieve strong accuracy via long chains of thought but at high inference cost and latency, sometimes entering unproductive self-reflection cycles on easy problems (overthinking); instruction-tuned models from the same family answer concisely but with weaker reasoning, and prior model-merging approaches to closing this gap use fixed global interpolation coefficients or black-box search, giving limited task-adaptive control over which modules preserve reasoning versus shift toward conciseness.

## Contributions

- GRIP, combining a reasoning model with a non-thinking instruction model of identical architecture via per-module, RL-learned interpolation ratios for efficient reasoning
- an RL-based update that optimizes only frozen-model interpolation ratios with a reward jointly rewarding answer correctness and response conciseness
- an empirical demonstration that GRIP achieves a stronger accuracy-efficiency trade-off than fixed-ratio merging baselines (Linear, SLERP, TIES, DARE-TIES, DELLA) and black-box search (CMA-ES), and that learned module-wise fusion patterns reveal FFN modules (not attention) as the primary driver of both reasoning length and accuracy

## Method

Given a reasoning model and an instruction model with identical architecture, GRIP assigns one learnable, sigmoid-parameterized interpolation ratio per module (attention blocks, FFN blocks, one for the final RMSNorm, one shared for the tied embedding/LM-head -- 74 fusion logits total for Qwen3-4B) and optimizes only these scalar ratios via a GRPO-style RL objective, while both source models stay frozen. The reward is correctness-gated and length-penalized: incorrect responses get zero reward; correct responses get progressively higher reward for being shorter, via a within-group, correct-responses-only length normalization and sigmoid soft-clipping. Trained with the slime RL framework on DeepScaleR-preview math prompts (750 optimizer steps, rollout group size 16, 32 prompts/rollout); the fused per-token gradient reduces to a chain-rule projection onto the single direction (reasoning-model params minus instruction-model params) per module, keeping optimization lightweight. Evaluated on Qwen3-4B-Thinking/Instruct-2507 across five reasoning benchmarks (AIME25, MATH500, GSM8K, GPQA-D, LiveCodeBench) against the original Thinking/Instruct models, five parameter-space merging baselines (Linear, SLERP, TIES, DARE-TIES, DELLA) at a fixed 0.8 reasoning-model coefficient, and CMA-ES (a black-box evolutionary search baseline over the same 74-dimensional fusion space with matched reward, training prompts and module parameterization).

## Results

GRIP reduces average generation length by 27.0% relative to Qwen3-Thinking (10,856 to 7,930 tokens) while slightly improving average accuracy (76.0 to 76.5) across the five benchmarks. On AIME25 specifically, GRIP improves accuracy over Thinking by 6.7 points (73.3 to 80.0) while reducing output length by 39.7%, suggesting the hardest math problems contain substantial redundant exploration that can be removed without hurting (and here improving) accuracy. GRIP reaches the same average accuracy as SLERP while using 14.5% fewer tokens, and beats all five fixed-ratio/searched merging baselines on the accuracy/token trade-off (best Avg accuracy at 76.5, with lower or comparable token count than every method except Instruct itself). Although trained only on math data (DeepScaleR-preview), GRIP transfers to out-of-domain benchmarks: GPQA-D shows accuracy gains with shorter reasoning, and LCB achieves the lowest token usage among the strong reasoning variants tested. A module-targeted coefficient sweep shows attention and FFN play sharply different roles: sweeping the attention ratio barely changes macro pass@1 (stays in [0.690, 0.722]) while sweeping FFN raises pass@1 from 0.612 to 0.782 and increases length 178% -- FFN modules drive most of both accuracy and length, and module-wise tuning beats any single global ratio at every alpha>=0.4 tested (best accuracy 0.782 at module-specific alpha=0.9 for FFN vs. 0.760 best global). Learned per-layer ratios differentiate substantially by depth: attention's early layers (0-8) stay Thinking-heavy (alpha ~0.85-0.9) while middle/late layers dip toward Instruct (alpha ~0.5-0.7); FFN's middle layers move most aggressively toward Instruct (alpha ~0.3) versus any attention band. Versus CMA-ES (matched training data/search space/objective), GRIP's optimization trajectory is markedly smoother (median per-coordinate RMS shift between updates: 0.018 for GRIP vs. 0.083 for CMA-ES; path-to-net-displacement ratio 4.9x for GRIP vs. 21.8x for CMA-ES, meaning CMA-ES retraces most of its own path).

## Limitations

Evaluated only at the 4B parameter scale due to compute constraints; whether the accuracy-efficiency trade-off and per-layer differentiation patterns transfer to substantially larger reasoning models (30B+) is left open. All experiments use dense Transformer backbones; the method is not validated on Mixture-of-Experts architectures, where router and expert weights introduce structure the current per-module parameterization does not address. GRIP requires the reasoning and instruction models to share an identical architecture (same depth, width, head count), restricting it to within-family pairs (e.g. Qwen3-Thinking with Qwen3-Instruct); cross-family fusion is not directly supported and is not evaluated.

## Why it matters here

- **overthinking**: Directly on-topic and explicitly framed by the authors as an overthinking mitigation: it targets the same reasoning-oriented models' tendency to generate 'unnecessarily long explanations' and 'cycles of self-reflection... on relatively simple problems,' and its largest gain (39.7% shorter, +6.7 accuracy points on AIME25) is presented as evidence that 'difficult mathematical problems contain substantial redundant exploration.' The module-wise analysis -- FFN, not attention, carries most of the length/accuracy tradeoff, with distinct early/middle/late-layer patterns -- offers a mechanistic, weight-space account of where overthinking-reducible behavior is concentrated, complementary to activation-steering or prompting-based accounts.

## Entities

- **Concepts**: module-wise sigmoid-controlled parameter fusion, reward-guided interpolation (vs. fixed-ratio merging), correctness-gated, length-penalized RL reward
- **Methods**: module-wise sigmoid-parameterized model interpolation, GRPO-style RL with clip-higher/KL-free modifications from DAPO, CMA-ES (black-box search baseline)
- **Datasets**: [DeepScaleR-preview (training)](../../../../wiki/datasets/deepscaler-preview-training.md), [AIME25](../../../../wiki/datasets/aime-2025.md), [MATH500](../../../../wiki/datasets/math500.md), [GSM8K](../../../../wiki/datasets/gsm8k.md), [GPQA-D](../../../../wiki/datasets/gpqa-d.md), [LiveCodeBench](../../../../wiki/datasets/livecodebench.md)

Tags: `overthinking`, `model-merging`, `efficient-reasoning`, `reinforcement-learning`, `reward-guided-interpolation`

## Abstract

Reasoning-oriented large language models often achieve strong problem-solving performance by generating long chains of thought, but this behavior substantially increases inference cost and latency. In contrast, instruction-tuned models tend to answer more concisely, yet often lack comparable reasoning ability. This accuracy-efficiency mismatch motivates a lightweight approach that combines the strengths of both models without full model retraining. In this paper, we propose GRIP (Granular Reward-guided Interpolation of Parameters), a reward-guided parameter interpolation framework for efficient reasoning. Given a reasoning model and an instruction model with identical architectures, GRIP assigns learnable interpolation ratios to individual modules and optimizes only these ratios while keeping both source models frozen. The interpolation ratios are trained with a reward signal that favors responses that are both correct and concise. Experiments show that GRIP achieves a better accuracy-efficiency trade-off than fixed or search-based merging baselines and further reveals module-wise fusion patterns associated with efficient reasoning.

---

Record id: `arxiv:2608.25583`
