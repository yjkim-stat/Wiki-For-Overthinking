# Process Supervision

<!-- auto:begin -->

Supervising the intermediate steps of a reasoning chain rather than only its final answer. The archive's one worked instance is a safety method: it locates 'safety trigger' points and 'compliance cue' patterns inside the chain, replaces a compliance-cue step with a corrected one to build preference pairs, and trains on them with Intervened Preference Optimization, reporting over 30% harmfulness reduction against baselines on jailbreak and adversarial benchmarks - the archived record names neither the benchmarks nor the baseline numbers. The second source is a caution about what such supervision should reward: annotating 15,282 traces from 15 models across 6 benchmarks, it finds the behaviours reasoning training amplifies most (self-correction, hypothesis testing, uncertainty acknowledgment) sit at the bottom of its correctness-association ranking, uncertainty acknowledgment at -16.1% and -13.9% Behavioral Lift, while the top-ranked confidence calibration, knowledge alignment and self-awareness are barely amplified at all. The archive therefore supports process supervision as a place to intervene without establishing which step-level behaviours are worth rewarding.

- **Kind**: concept
- **Also called**: Process Supervision, process supervision
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [Chain-of-thought monitorability](chain-of-thought-monitorability.md), [Confidence Calibration](confidence-calibration.md), [MATH500](../datasets/math500.md), [MMLU-Pro](../datasets/mmlu-pro.md), [MMMU](../datasets/mmmu.md), [process reward model](../methods/process-reward-model.md)

## Appears in

- [Amplified Does Not Mean Predictive: Reasoning Behaviors in Thinking Models](../../archive/papers/2026/arxiv-2608-13760/summary.md) — Annotates 15,282 reasoning traces from 15 models on 6 benchmarks with a nine-behavior taxonomy and shows that the behaviors reasoning-oriented training amplifies most (self-correction, hypothesis testing, uncertainty acknowledgment) are not the behaviors most associated with getting the answer right (confidence calibration, knowledge alignment, self-awareness).

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
