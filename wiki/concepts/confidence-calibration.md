# confidence calibration

<!-- auto:begin -->

The sources use the ordinary sense — a stated confidence that matches how often the prediction is right — but split on whether it is a target worth optimising or merely a signal to gate on. CaTS and C4 use it as a signal: CaTS allocates sampling budget per query from a self-distilled confidence and stops early once the model is confident, while C4 gates a diffusion LM's global exit on the extracted answer span being both confident and unchanged for several steps. The taxonomy study over 15,282 annotated traces from 15 models on 6 benchmarks puts calibration among the behaviors most associated with answering correctly, and notably not among those reasoning-oriented training amplifies. Rethinking Calibration for Early-Exit Neural Networks argues the opposite of the first group: for early-exit classifiers calibration is the wrong objective, because a well-calibrated exit still ignores whether later layers would have fixed the prediction, and it substitutes Early-Exit Failure Prediction.

- **Kind**: concept
- **Also called**: Confidence Calibration, calibration
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [adaptive test-time compute](adaptive-test-time-compute.md), [ARC-Challenge](../datasets/arc-challenge.md), [Best-of-N](../methods/best-of-n.md), [C4](../methods/c4.md), [confidence-based early stopping](../methods/confidence-based-early-stopping.md), [Confidence Thresholding](../methods/confidence-thresholding.md), [conformal prediction](../methods/conformal-prediction.md), [early exit](../methods/early-exit.md), [early-exit neural networks](early-exit-neural-networks.md), [early stopping](early-stopping.md), [GSM-Hard](../datasets/gsm-hard.md), [GSM8K](../datasets/gsm8k.md), [HellaSwag](../datasets/hellaswag.md), [HumanEval](../datasets/humaneval.md), [ImageNet-1K](../datasets/imagenet-1k.md), [MATH](../datasets/math.md), [MATH-500](../datasets/math-500.md), [MathQA](../datasets/mathqa.md), [MBPP](../datasets/mbpp.md), [MMLU](../datasets/mmlu.md), [MMLU-PRO](../datasets/mmlu-pro.md), [MMMU](../datasets/mmmu.md), [process supervision](process-supervision.md), [self-consistency](../methods/self-consistency.md), [SVAMP](../datasets/svamp.md)

## Appears in

- [Commit Locally, Exit Globally: Coordinating Adaptive Sampling and Early Exit in Diffusion Language Models](../../archive/papers/2026/arxiv-2607-28166/summary.md) — C4 accelerates diffusion language model decoding with two separate gates: one that decides when the whole sequence may stop, by checking that the extracted answer span is both confident and unchanged for several steps, and one that decides which token positions a step may commit, by committing only a boundary-anchored run and confirming deferred positions one step later.
- [Amplified Does Not Mean Predictive: Reasoning Behaviors in Thinking Models](../../archive/papers/2026/arxiv-2608-13760/summary.md) — Annotates 15,282 reasoning traces from 15 models on 6 benchmarks with a nine-behavior taxonomy and shows that the behaviors reasoning-oriented training amplifies most (self-correction, hypothesis testing, uncertainty acknowledgment) are not the behaviors most associated with getting the answer right (confidence calibration, knowledge alignment, self-awareness).
- [CaTS: Calibrated Test-Time Scaling for Efficient LLM Reasoning](../../archive/papers/2026/title-03232c54fde9b57f/summary.md) — Proposes CaTS, a calibrated test-time scaling framework that uses a self-distilled confidence signal to adaptively allocate sampling budget per query, including early stopping once the model is confident.
- [Rethinking Calibration for Early-Exit Neural Networks](../../archive/papers/2026/title-14e8a3607202d3e2/summary.md) — Argues that confidence calibration is the wrong objective for early-exit image classifiers and replaces it with Early-Exit Failure Prediction, a criterion that also accounts for whether later layers could fix the prediction.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
