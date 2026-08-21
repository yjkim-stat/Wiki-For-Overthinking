<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ParoQuant: Pairwise Rotation Quantization for Efficient Reasoning LLM Inference

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10011824>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

ParoQuant is a 4-bit weight-only post-training quantization method that applies a series of independent Givens (pairwise) rotations plus channel-wise scaling to weights before quantization, with a fused CUDA kernel, in order to keep accuracy on reasoning benchmarks where quantization error accumulates over long chains of thought.

## Problem

Post-training quantization of LLM weights and activations is limited by outliers, which widen the dynamic range of a quantization group and produce large errors. The paper argues the cost is worse for reasoning models than for short-answer models because errors accumulate across a long generated chain of thought. Existing methods either suppress outliers insufficiently (channel-wise scaling alone, as in AWQ) or use full/Hadamard rotations that cost meaningful inference overhead.

## Contributions

- Scaled pairwise rotation: a sparsely parameterized transform combining K independent Givens rotations with channel-wise scaling, argued to match full-rotation expressiveness at a fraction of the parameters.
- A layer-wise optimization scheme that fits rotations and scales against the output of already-quantized preceding layers, plus a second EfficientQAT-style stage over weights and quantization parameters.
- A fused CUDA kernel parallelized at token, channel-group and pair level, reported up to about 5x faster than the fast Hadamard transform at large channel dimension.
- Evaluation on reasoning benchmarks specifically, with the argument that the accuracy gap between quantized and FP16 models is larger there because long generations accumulate error.

## Method

The transform applied to a weight matrix before quantization is a product of K independent Givens rotations composed with a diagonal channel-wise scaling: T(W) = (prod_t R(P_t, Theta_t)) . diag(alpha) . W. Each rotation acts on disjoint channel pairs, so it has n/2 tunable parameters rather than the n(n-1)/2 of a full orthogonal matrix; the paper compensates by stacking several (8 in the experiments) with pair selection that skips pairs already used by an earlier rotation. Channel-wise scaling evens out average magnitude across channels, which the sparse rotations cannot do on their own, and is folded into the rotation kernel. Rotation pairs, angles and scales are fit by layer-wise optimization minimizing the decoder-layer output error against the original model, taking as input the output of the already-quantized preceding layers so later layers can compensate for earlier error. A second stage fine-tunes the weights and the linear quantization parameters s and z in the manner of EfficientQAT. Inference uses one fused CUDA kernel parallelized over tokens, channel groups and pairs; the paper reports the transform is up to about 5x faster than the fast Hadamard transform at channel dimension 2^15 on an RTX A6000.

## Results

4-bit weight-only, group size 128, on LLaMA-2 7B, LLaMA-3 8B/70B, LLaMA-3.1-Instruct 8B, DeepSeek-R1-distilled-LLaMA-3.1 8B and Qwen3 1.7B/4B/8B/14B. Reasoning tasks (MMLU-Pro 12k samples, GPQA Diamond 198, AIME-24 30, AIME-25 30), average over the four models: ParoQuant 61.9 vs FP16 62.8, QTIP 61.0, AWQ 59.5, EfficientQAT 55.6 - i.e. 0.9 points below FP16, and +2.4 over AWQ, +6.3 over EfficientQAT, +0.9 over QTIP. Non-reasoning tasks (BoolQ, ARC-C, ARC-E, HellaSwag) average: ParoQuant 69.9 vs FP16 70.1, ahead of AWQ by 0.9, EfficientQAT by 0.7, QTIP by 0.2. Perplexity: LLaMA-3-8B WikiText2 5.73 (FP16 5.54, AWQ 5.92, QTIP 5.69). Decoding throughput at batch size 1 on an RTX A6000: Qwen3-1.7B 278 tok/s (1.6x FP16) vs AWQ 320 (1.9x) and QTIP 209 (1.2x); Qwen3-14B 65 tok/s (2.6x) vs AWQ 70 (2.8x) and QTIP 55 (2.2x) - about 10% slower than AWQ and 15-30% faster than QTIP. Ablation: 8 rotations plus scaling plus the second stage gives C4 perplexity 7.27 on LLaMA-3-8B against 7.56 for no transform and no second stage; 128 calibration samples already reach 7.30.

## Limitations

The paper notes the GPQA and AIME results are noisy because those benchmarks have 198 and 30 samples respectively, and its own tables bear this out: AWQ beats ParoQuant on several individual cells (Qwen3-8B GPQA 60.2 vs 57.7; Qwen3-14B AIME-24 80.0 vs 77.8), so the headline 2.4-point average is carried mostly by MMLU-Pro. Pair selection skips pairs used by earlier rotations, which the authors say may leave some rotations with too few pairs. Scope: 4-bit weight-only linear quantization with group size 128 only; the claim to match weight-activation methods is a claim about accuracy, not about the activation-quantization speedups those methods offer. The throughput advantage is measured at batch size 1 on a single RTX A6000. There is no separate limitations section. Notably absent: the paper's motivating claim is that error accumulates over long chains of thought, but it never measures accuracy as a function of trace length or reports how quantization changes the length of generated traces - the reasoning/non-reasoning accuracy gap is offered as indirect evidence instead.

## Why it matters here

- **overthinking**: Tangential, and on the same side of the line the archive has already put ThinKV, AsyncSpade and BeaconKV: it lowers the serving cost of whatever reasoning trace the model produces rather than changing how long that trace should be. Nothing in the method observes the trace, decides when to stop, or trades accuracy against length; the length decision is untouched, and the throughput gains (1.6x-2.6x over FP16 at batch size 1) would apply equally to a trace that is ten times longer than it needs to be. One narrow thing does connect to the topic and is worth keeping: the paper's premise, supported by its own split between reasoning and non-reasoning results (0.9 points below FP16 on MMLU-Pro/GPQA/AIME against 0.2 on BoolQ/ARC/HellaSwag, which the authors attribute to those benchmarks generating only a few tokens), is that per-token quantization error compounds along the trace. If that holds, then trace length is a cost multiplier on quantization error and not only on latency - which would make a length-control method and a quantization method interact rather than compose independently. The paper does not test that: it never plots accuracy against trace length. Treat this as background on the serving stack, not as evidence about when a model should stop.

## Entities

- **Concepts**: Post-training quantization, Activation and weight outliers, Rotation-based outlier suppression, Error accumulation over long chains of thought, Quantization group dynamic range, Kernel co-design
- **Methods**: ParoQuant, Givens / pairwise rotation, channel-wise scaling, AWQ, EfficientQAT, QTIP, QuIP#, OmniQuant, SpinQuant, fast Hadamard transform
- **Datasets**: WikiText2, C4, [MMLU-Pro](../../../../wiki/datasets/mmlu-pro.md), [GPQA Diamond](../../../../wiki/datasets/gpqa-diamond.md), AIME-24, AIME-25, BoolQ, [ARC-Challenge](../../../../wiki/datasets/arc-challenge.md), ARC-Easy, [HellaSwag](../../../../wiki/datasets/hellaswag.md), RedPajama (calibration), Pile (validation)

Tags: `quantization`, `post-training-quantization`, `inference-efficiency`, `givens-rotation`, `outliers`, `cuda-kernel`, `serving-cost`, `iclr2026`

---

Record id: `title:fe3c313c25254076`
