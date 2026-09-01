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

Instance-dependent Early Stopping (IES) individualizes training-time early stopping per training instance rather than uniformly, using the second-order difference of an instance's loss trajectory (rather than raw loss) to detect when it is 'mastered' and exclude it from further backpropagation, reducing backpropagation compute by 10-50% while preserving or slightly improving test accuracy and transfer learning.

## Problem

Conventional early stopping applies a uniform stopping criterion across an entire training run or dataset, but different training instances are learned ('mastered') at different points during training, so uniform stopping wastes computation continuing to backpropagate through already-mastered, easy instances.

## Contributions

- Instance-dependent Early Stopping (IES), individualizing the stopping decision per training instance rather than uniformly across a run
- a second-order loss-difference criterion for detecting when an instance is mastered, more reliable than raw loss
- 10-50% backpropagation compute reduction with preserved or improved test accuracy and transfer learning across benchmarks

## Method

Introduces Instance-dependent Early Stopping (IES), which monitors the second-order difference (rate of change of the rate of change) of each instance's loss around zero as a more reliable 'mastered' indicator than raw loss values, uses a standardized threshold on this signal to decide when to exclude an instance from further backpropagation, and shows theoretically/empirically that removing well-learned instances strengthens the gradient norm on the remaining harder instances, accelerating overall training loss reduction.

## Results

Across benchmark experiments, IES reduces backpropagation computation by 10-50% while preserving or marginally improving test accuracy and transfer learning capability compared to standard training without instance-level early stopping.

## Limitations

Not stated in the fetched abstract beyond the general training/backpropagation-efficiency scope described.

## Why it matters here

- **overthinking**: Not directly relevant: this is a training-time compute-saving technique (skipping backpropagation for already-learned training examples), unrelated to inference-time reasoning-trace length; matched to the topic only via the shared term 'early stopping', though the underlying principle -- individualize the stopping decision per instance rather than applying a uniform rule -- parallels instance/difficulty-adaptive reasoning-length control at inference time.

## Entities

- **Concepts**: instance-dependent early stopping, second-order loss-difference mastery signal, gradient-norm strengthening from instance removal
- **Methods**: Instance-dependent Early Stopping (IES)
- **Datasets**: _none recorded_

Tags: `early-stopping`, `training-efficiency`, `instance-level-adaptivity`, `backpropagation`

---

Record id: `title:5f72fe24f143bb5d`
