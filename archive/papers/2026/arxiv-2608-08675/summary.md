<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Efficient Test-Time Scaling for LLM-based Time Series Forecasting

- **Authors**: Xuan-May Le, Minh-Tuan Tran, Ling Luo, Uwe Aickelin, Dinh Phung, Trung Le
- **Venue**: cs.LG
- **Published**: 2026-08-09
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.08675>
- **PDF**: <https://arxiv.org/pdf/2608.08675v1>
- **Topics**: test-time-scaling
- **Relevance score**: test-time-scaling 0.50

## In one line

Replaces open-ended iterative refinement in LLM time-series forecasting with a fixed-step coarse-to-fine loop anchored to an explicitly predicted downscaled future shape, so test-time compute is spent enriching detail rather than re-deciding the global trajectory.

## Problem

Test-time scaling for LLM forecasters -- sampling several futures, selecting with a reward model, or refining iteratively -- costs inference time that grows with horizon length, and repeated local corrections accumulate into global-shape drift, so trends and seasonality distort exactly as the horizon gets long enough for them to matter.

## Contributions

- A two-stage forecaster in which a lightweight Transformer predicts an explicit downscaled future shape and a frozen LLM spends a fixed K-step budget refining it from coarse to fine, giving deterministic inference cost with no candidate sampling or reward-model selection.
- A shared multi-scale encoder that tokenises the history once so refinement steps never reprocess the raw input.
- An ablation pricing each alternative use of test-time compute in normalised inference and training time: full-resolution shape 1.84x, description tokens 2.34x, reward-model selection 5.51x, LoRA 8.21x training, full fine-tuning 15.21x training -- none of which beats the default.
- A horizon sweep to 2160 steps showing the advantage over refinement-only baselines widening past H=720.

## Method

Two stages over a shared multi-scale encoder that tokenises the history once, so no stage reprocesses the raw input. Stage I is a lightweight Transformer that predicts a downscaled coarse future shape carrying the horizon's low-frequency structure, supervised against the downscaled ground-truth future. Stage II runs a frozen pretrained LLM for a fixed K steps: at step k it predicts the scale-k token block conditioned on the history tokens and the growing context of coarser shape tokens, appends it, and continues; the finest-scale context is decoded back to the original resolution. Training combines a shape loss on Stage I, a per-step refinement loss and a time-domain loss on the final forecast, weighted by lambda and beta. Because the budget is a fixed number of steps rather than a sampling-and-selection procedure, the inference cost is deterministic and no reward model is needed. The LLM's parameters are never updated.

## Results

Long-term forecasting over seven benchmarks and four horizons, averaged over five seeds: SCALER takes 6 of the first-place MSE counts across all dataset-horizon pairs against 1 for both TimeReasoner and Chronos. The margins are small in absolute terms -- ETTh1 0.376 MSE against 0.381 for LVICL and 0.403 for TimeReasoner; ECL 0.154 against 0.154 for TimeReasoner; Weather 0.217 against 0.218. It also leads short-term (M4) and both zero-shot transfer directions (M3 to M4 average sMAPE 12.36 against 12.4; M4 to M3 12.76 against 12.975). The ablation table is where the paper is most informative, and it locates almost all of the gain in Stage I: removing the global forecaster costs 0.026 MSE on ETTh1 (0.407 against 0.381) while saving only 4 percent of inference time, whereas every remaining variant lands within 0.006 of the default. Predicting a full-resolution rather than downscaled shape matches the default's accuracy at 1.84x inference and 1.72x training time; adding natural-language description tokens costs 2.34x for no gain; reward-model candidate selection costs 5.51x inference and 5.61x training and is slightly worse on all four datasets. LoRA and full fine-tuning of the LLM cost 8.21x and 15.21x training time to move ETTh1 MSE by at most 0.001. Backbone sweep from GPT-2 (124M) to LLaMA-7B moves ETTh1 MSE only from 0.379 to 0.376 and ECL from 0.159 to 0.154, so the frozen LLM contributes little that a 124M model does not. The long-horizon sweep to H=2160 is where the claim is strongest: the gap over TimeReasoner and TimeLLM widens steadily for H at or above 720. Average inference is reported as 7x faster than standard test-time-scaling forecasters.

## Limitations

The authors state that the refinement schedule is fixed and that performance may depend on the LLM backbone and tokenisation. Reader-visible limits are larger. The margins in the main tables are of order 0.005 MSE, which the paper does not accompany with intervals despite averaging five seeds, so most of the head-to-head claims rest on differences smaller than a seed's plausible spread. The ablation shows the LLM stage is close to inert: a 124M backbone is within 0.003 of a 7B one and fine-tuning the backbone changes nothing, so what the paper demonstrates is mainly that a lightweight coarse forecaster in front of a refiner beats a refiner alone, not that the LLM's pretrained prior is doing the work its framing attributes to it. The global-shape-drift claim is illustrated by one representative 96-step figure rather than measured. Long-term numbers for all baselines are copied from another paper's setup with only TimeReasoner rerun, so the comparison is not uniformly under this paper's protocol.

## Why it matters here

- **test-time-scaling**: A test-time-scaling paper whose own ablation argues against the premise. Reward-model candidate selection costs 5.5x inference here and is slightly worse than a fixed-step schedule; extra description tokens cost 2.3x for nothing; and the backbone sweep shows a 124M model within 0.003 MSE of a 7B one, so the compute that matters is spent on a cheap task-specific forecaster before the LLM rather than on scaling the LLM's inference. That is the sharpest form of a pattern the archive has been collecting: an adaptive-compute claim should be checked against a fixed-budget control and against a much smaller backbone, because both are cheap and both frequently match it. The one place the scaling story does hold is the horizon sweep beyond 720 steps, where the advantage widens -- the condition under which the headline is real.

## Entities

- **Concepts**: [test-time scaling](../../../../wiki/concepts/test-time-scaling.md), iterative refinement, coarse-to-fine, [compute allocation](../../../../wiki/concepts/compute-allocation.md), [adaptive compute allocation](../../../../wiki/concepts/adaptive-compute-allocation.md), reward model selection, frozen backbone
- **Methods**: SCALER, TimeReasoner, LVICL, AutoTimes, TimeLLM, FPT, [LoRA](../../../../wiki/methods/lora.md), prompt tuning, reward-model candidate selection
- **Datasets**: ETTh1, ETTh2, ETTm1, ETTm2, Electricity (ECL), Traffic, Weather, ILI, M3, M4

Tags: `test-time-scaling`, `time-series`, `iterative-refinement`, `inference-cost`, `frozen-llm`

## Abstract

Long-term time series forecasting benefits from preserving global structure such as trends and seasonality. Recent LLM-based forecasters often improve accuracy through test-time scaling (e.g., iterative refinement), but these methods are computationally expensive and increasingly prone to global-shape mismatch as the prediction horizon extends. We propose SCALER, a coarse-to-fine forecasting framework that first employs a lightweight Transformer tailored to long-term shape modeling to predict a coarse representation of future dynamics. This predicted shape then serves as a compact guide for an LLM to perform test-time scaling via iterative coarse-to-fine residual token refinement, while processing substantially fewer tokens at each step. By guiding refinement with an explicit future-shape prediction, SCALER reduces reliance on long description prompts, and its fixed-step refinement avoids costly reward-model-based selection, further lowering computational overhead. Experimental results demonstrate that SCALER outperforms strong forecasting baselines in long-term, short-term and zero-shot forecasting while significantly reducing the inference cost associated with scaled LLM for time series forecasting. Code: https://github.com/xuanmay2701/SCALER.

---

Record id: `arxiv:2608.08675`
