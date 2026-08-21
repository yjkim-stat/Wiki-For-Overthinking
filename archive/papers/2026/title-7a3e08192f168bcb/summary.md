<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Efficient Reasoning with Balanced Thinking

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10008522>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

ReBalance is a training-free inference-time steering method that reads a reasoning model's token confidence to detect overthinking or underthinking and applies a hidden-state steering vector to shorten or extend the chain of thought accordingly.

## Problem

Large reasoning models both overthink (spending redundant steps on easy problems) and underthink (failing to explore enough reasoning paths they are capable of). Existing overthinking remedies -- suppressing reflective keywords, capping or penalising reasoning length -- treat length as the target and can push a model into underthinking, trading tokens for accuracy. The open question the paper takes up is how to detect which of the two failure modes a generation is currently in, and correct only that one, without retraining.

## Contributions

- Uses token confidence as a single continuous signal that separates overthinking (high confidence variance) from underthinking (persistent overconfidence), rather than treating length alone as the symptom
- Builds reasoning-mode prototypes by aggregating hidden states from 500 sampled MATH problems and derives a steering vector from their difference
- Adds a dynamic control function that sets the steering vector's direction and strength from real-time confidence, so the same mechanism can shorten or lengthen a trace
- Reports simultaneous token reduction and Pass@1 improvement on nine benchmarks across models from 1.5B to 32B, against nine efficient-reasoning baselines
- Requires no training or weight updates, so it applies to an already-deployed reasoning model

## Method

ReBalance uses per-step confidence as a continuous read-out of reasoning dynamics: high variance in confidence across the trace is taken as the signature of overthinking, while consistently high confidence is taken as the signature of underthinking. Hidden states are collected from a small probe set (500 randomly sampled MATH problems) and aggregated into prototypes for the two reasoning modes; the difference between the prototypes gives a steering vector. At inference the vector is added to the hidden states, with a dynamic control function setting both its sign and its magnitude from the confidence signal measured in real time -- pruning redundancy when the trace looks like overthinking, promoting further exploration when it looks like underthinking. No weights are updated, so the method is applied on top of an existing model as a decoding-time intervention.

## Results

Evaluated on nine benchmarks across four models. On math (MATH-500, AIME24, AIME25, GSM8K, AMC23, OlympiadBench) Pass@1 rises and tokens fall simultaneously: MATH-500 +0.2 to +3.4 Pass@1 with 18.5%-23.1% fewer tokens; AIME24 +3.3 to +10.0 with 13.1%-27.8% fewer; AIME25 +0 to +10.0 with 7.1%-16.2% fewer; GSM8K +0.5 to +2.4 with 14.4%-35.4% fewer; AMC23 +5.0 to +10.0 with 26.8%-30.2% fewer; OlympiadBench +0.9 to +5.7 with 2.6%-17.6% fewer. Out of domain: GPQA Diamond +4.1 to +6.6 Pass@1 with 15.2%-29.9% fewer tokens; StrategyQA +0.1 to +2.1 with 2.6%-11.4% fewer; LiveCodeBench +0.8 to +3.0 with 7.1%-14.7% fewer. Baselines compared: CoD, DEER, NoThinking, NoWait, Dynasor-CoT, SEAL, Manifold Steering, FlashThink, TrimR.

## Limitations

Gains are reported as ranges over models rather than as a single operating point, and the low end of several ranges is near zero (AIME25 +0 Pass@1, StrategyQA +0.1 with 2.6% token saving), so on some model/benchmark pairs the intervention is close to a no-op. The paper attributes the weak StrategyQA result to the task being relatively saturated, leaving few overthinking states to detect -- which also means the detector's signal depends on the task having visible confidence variance in the first place. The steering vector is extracted from 500 MATH problems, so its transfer to coding and commonsense benchmarks rests on the claim that confidence dynamics are domain-independent rather than on domain-specific calibration. The ablation reports that removing the underthinking side of the control lowers accuracy notably on tasks needing long reasoning, so the two-sided design is load-bearing and a mis-set boundary degrades results. The abstract states a 0.5B-to-32B range, but the models named in the results are DeepSeek-R1-Distill-Qwen-1.5B and 7B, Qwen3-14B, QwQ-32B and openPangu-Embedded-7.1B; no 0.5B result is visible in the tables reviewed. No wall-clock or throughput cost of computing confidence and applying the steering vector at every step is reported.

## Why it matters here

- **overthinking**: Directly on topic, and it argues the topic's central tension explicitly: methods that attack overthinking by suppressing reflection or capping length can induce underthinking, so length is the wrong control variable. The paper's alternative is to treat overthinking and underthinking as two states of one axis and detect which one is active from confidence statistics -- high variance for overthinking, sustained overconfidence for underthinking -- then steer in the corresponding direction. That gives the group a concrete, training-free detector for when a model should stop and when it should keep going, plus a baseline set (CoD, DEER, NoThinking, NoWait, Dynasor-CoT, SEAL, Manifold Steering, FlashThink, TrimR) covering the current efficient-reasoning field. The evidence that accuracy can rise while tokens fall on nine benchmarks is a data point against treating the accuracy/efficiency tradeoff as strictly monotone, though the near-zero low ends of several reported ranges keep that claim qualified.

## Entities

- **Concepts**: [Overthinking](../../../../wiki/concepts/overthinking.md), [Underthinking](../../../../wiki/concepts/underthinking.md), [Test-Time Compute Scaling](../../../../wiki/concepts/test-time-compute-scaling.md), Activation Steering, Model Confidence as a Stopping Signal, Training-Free Efficient Reasoning, [Accuracy/Length Tradeoff](../../../../wiki/concepts/accuracy-length-tradeoff.md)
- **Methods**: ReBalance, activation steering / steering vectors, reasoning mode prototypes from hidden states, confidence-based dynamic control function, CoD, [DEER](../../../../wiki/methods/deer.md), [NoThinking](../../../../wiki/methods/nothinking.md), [NoWait](../../../../wiki/methods/nowait.md), Dynasor-CoT, [SEAL](../../../../wiki/methods/seal.md), [Manifold Steering](../../../../wiki/methods/manifold-steering.md), FlashThink, [TrimR](../../../../wiki/methods/trimr.md)
- **Datasets**: [MATH-500](../../../../wiki/datasets/math-500.md), AIME24, AIME25, [AMC23](../../../../wiki/datasets/amc23.md), [GSM8K](../../../../wiki/datasets/gsm8k.md), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md), [GPQA Diamond](../../../../wiki/datasets/gpqa-diamond.md), [StrategyQA](../../../../wiki/datasets/strategyqa.md), [LiveCodeBench](../../../../wiki/datasets/livecodebench.md), MATH (500 sampled problems, for steering vector extraction)

Tags: `overthinking`, `underthinking`, `efficient reasoning`, `steering vectors`, `test-time compute`, `training-free`, `confidence`, `chain-of-thought`, `iclr-2026`

---

Record id: `title:7a3e08192f168bcb`
