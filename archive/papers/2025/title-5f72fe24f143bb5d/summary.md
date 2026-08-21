<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Instance-dependent Early Stopping

- **Authors**: _unknown_
- **Venue**: ICLR 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2025/poster/29782>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Moves early stopping from the whole training set down to the individual training example, dropping an instance from backpropagation once the second-order difference of its loss stays near zero.

## Problem

Conventional early stopping halts the entire training run on one validation criterion, so every instance is trained for the same number of steps regardless of whether the model already fits it. That spends backpropagation on examples that are already learned. The open part is finding a per-instance signal of 'mastered' that is consistent enough across instances to share one threshold.

## Contributions

- Reframes early stopping as a per-instance rather than per-run decision
- Proposes second-order differences of an instance's loss as a threshold-comparable measure of whether it is mastered, allowing one global threshold
- Shows that excluding mastered instances increases gradient norms and thereby accelerates the training-loss decrease
- Reports 10%-50% fewer backpropagated instances at maintained or slightly improved test accuracy and transfer performance

## Method

Instance-dependent Early Stopping (IES) tracks each training instance's loss over epochs and computes second-order differences of that loss sequence. An instance is judged mastered when its second-order differences stay within a small band around zero, meaning its loss curve has flattened. Mastered instances are excluded from further backpropagation (they still may be forward-passed). The authors argue second-order differences are a more consistent measure of learning status than the raw loss value, which lets a single threshold be applied to all instances rather than a per-instance one. They also show that removing mastered instances raises the gradient norm on the remaining batch, which speeds the decrease of training loss.

## Results

Across the benchmarks tested, IES reduces the number of backpropagated instances by 10%-50% while maintaining or slightly improving test accuracy and transfer-learning performance. The abstract does not name the specific datasets or give per-benchmark accuracy figures.

## Limitations

None stated in the available material. Points a reader should notice: the reported saving is in backpropagated instances, not necessarily wall-clock or FLOPs, since deciding mastery still requires tracking each instance's loss; the 10%-50% range is wide and the abstract does not say what determines where in that range a given setting lands; and the mastery test is a flatness test on the loss curve, which cannot distinguish an instance that is learned from one that is stuck.

## Why it matters here

- **overthinking**: Tangential: matched only on the phrase 'early stopping', which here is the classical training-time regularisation sense — when to stop backpropagating on a training example — not stopping a model's reasoning at inference. There is no language model, no reasoning trace and no test-time compute in this work. The one idea with any family resemblance is per-instance compute allocation driven by a signal that the instance is already handled, which in the overthinking literature appears as per-question adaptive reasoning length; but the signal (second-order loss differences over training epochs) has no inference-time analogue here.

## Entities

- **Concepts**: [Early Stopping](../../../../wiki/concepts/early-stopping.md), Per-Instance Compute Allocation, Learning Status Estimation, Gradient Norm, Training Efficiency
- **Methods**: Instance-dependent Early Stopping (IES), second-order loss differences, early stopping, selective backpropagation
- **Datasets**: _none recorded_

Tags: `early-stopping`, `training-efficiency`, `selective-backpropagation`, `curriculum`, `supervised-learning`

---

Record id: `title:5f72fe24f143bb5d`
