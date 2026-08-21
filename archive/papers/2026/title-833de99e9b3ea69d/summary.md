<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Stop Unnecessary Reflection: Training LRMs for Efficient Reasoning with Adaptive Reflection and Length Coordinated Penalty

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10008702>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

ARLCP is a reinforcement-learning fine-tuning recipe that adds two coupled reward penalties -- one on reflective steps, one on response length scaled by estimated problem complexity -- to shorten chains of thought in distilled reasoning models without losing accuracy.

## Problem

Large reasoning models trained for test-time scaling emit long chains of thought padded with reflection: repetitive self-questioning and circular reasoning. The paper's observation is that this gets worse as problem complexity rises -- harder problems induce more excessive and unnecessary reflection, which both costs tokens and reduces accuracy, with smaller models affected most. A flat length penalty is the obvious fix and the wrong one, because the token budget a problem genuinely needs varies with its difficulty; the open question is how to penalise the reflection that is redundant while leaving the reflection that is doing work.

## Contributions

- Reports the empirical observation that rising problem complexity induces more unnecessary reflection, which both lowers accuracy and raises token cost, most sharply in smaller models
- Introduces a reflection penalty computed as the sigmoid of a reflection-token count z-scored against correct responses, targeting redundant reflection rather than length as such
- Introduces a length penalty calibrated to estimated problem complexity via three tiers, so the token budget scales with difficulty
- Couples the two penalties through a shared budget alpha = alpha_1 + alpha_2, shifting weight between them by complexity tier instead of applying both independently
- Trains with RLOO and reports 53.1% length reduction with a 5.81% accuracy gain on DeepSeek-R1-Distill-Qwen-1.5B and 35.0% with 2.69% on the 7B model, against seven efficient-reasoning baselines
- Releases code at https://github.com/ZeweiYu1/ARLCP

## Method

ARLCP trains with REINFORCE Leave-One-Out (RLOO) policy optimisation using a composite penalty on the reward. Two statistics are computed per rollout and normalised against the distribution of correct responses: a reflection-token count RTC and a length LEN, each passed through a sigmoid of its z-score relative to the mean and standard deviation over correct responses, giving f(RTC) = sigma((RTC(o) - mean(RTC)_correct) / std(RTC)_correct) and f(LEN) = sigma((LEN(o) - mean(LEN)_correct) / std(LEN)_correct). The two penalties share a fixed total budget alpha: the reflection coefficient alpha_1 is selected from three values {lambda_1, lambda_2, lambda_3} according to which of three estimated complexity tiers the problem falls into, and the length coefficient is the remainder, alpha_2 = alpha - alpha_1. That coupling is what makes the penalties coordinated rather than independent -- as complexity rises, weight shifts between suppressing reflection and suppressing raw length instead of both tightening at once. Normalising against correct responses means the reference length is what the model actually needs to solve that problem, not a global constant.

## Results

Five math benchmarks (GSM8K 1319 problems, MATH500 500, AMC2023 40, AIME 2024 30, AIME 2025 30) on DeepSeek-R1-Distill-Qwen-1.5B and -7B. On 1.5B: average response length down 53.1% with a 5.81% overall accuracy gain; GSM8K accuracy 87.34% against 82.26% for the strongest baseline (LASER). On 7B: length down 35.0% with a 2.69% overall accuracy gain; GSM8K accuracy 89.31%. Baselines: NoThinking, SFT_Shortest, DPO_Shortest, O1-Pruner, TLMRE, AdaptThink, LASER.

## Limitations

The paper states no limitations section, and its own tables qualify the headline in two places. On the 1.5B model ARLCP loses to LASER on AMC2023 (73.28% against 75.94%) -- that is the second-hardest of the five benchmarks and the direction the paper's own complexity argument would predict trouble. On the 7B model ARLCP's GSM8K accuracy of 89.31% is below AdaptThink's 90.29%, so the reported 2.69% average gain is an average over benchmarks rather than a uniform win. The gap between the 1.5B and 7B results (53.1% against 35.0% length reduction, 5.81% against 2.69% accuracy gain) shows the method's benefit shrinking as model scale rises, and no result above 7B is reported, so whether anything remains at 14B or 32B is untested. Evaluation is math-only; no coding, science or commonsense benchmark is included, and reflection-token counting is a lexical proxy whose transfer outside math prose is unestablished. Both models are DeepSeek-R1 distillations, so the method is not shown on a natively-trained reasoning model. The three complexity tiers and their coefficients lambda_1..3 plus the total budget alpha are hyperparameters whose sensitivity is not reported, and because the method requires RL fine-tuning it cannot be applied to a model that is only available for inference.

## Why it matters here

- **overthinking**: Squarely on topic and useful for two distinct reasons. First, it isolates reflection -- repetitive self-questioning, circular reasoning -- as the specific component of chain-of-thought that grows redundantly, rather than treating overthinking as undifferentiated length; the reflection-token penalty acts on that component directly and is separable from the length penalty. Second, it makes the token budget a function of estimated problem complexity rather than a constant, which is the mechanism the topic cares about: the model should stop earlier on easy problems and later on hard ones, and here that is enforced by shifting weight between two penalties across three complexity tiers. The paper's stated observation -- that harder problems induce more unnecessary reflection, and that this reduces accuracy rather than merely costing tokens -- is a claim worth holding against other sources, because it implies overthinking and error share a cause on hard instances. Two cautions for the group: the wins are not uniform (LASER beats it on AMC2023 at 1.5B, AdaptThink on GSM8K at 7B), and the benefit halves from 1.5B to 7B, so this is evidence about small distilled models in math rather than about reasoning models generally.

## Entities

- **Concepts**: [Overthinking](../../../../wiki/concepts/overthinking.md), Unnecessary Reflection, [Length Penalty](../../../../wiki/concepts/length-penalty.md), Problem-Complexity-Adaptive Compute, Reinforcement Learning for Reasoning Length, [Accuracy/Length Tradeoff](../../../../wiki/concepts/accuracy-length-tradeoff.md), [Test-Time Compute Scaling](../../../../wiki/concepts/test-time-compute-scaling.md)
- **Methods**: ARLCP (Adaptive Reflection and Length Coordinated Penalty), REINFORCE Leave-One-Out (RLOO), reflection-token count (RTC) penalty, complexity-tiered length penalty, [NoThinking](../../../../wiki/methods/nothinking.md), SFT_Shortest, DPO_Shortest, [O1-Pruner](../../../../wiki/methods/o1-pruner.md), TLMRE, [AdaptThink](../../../../wiki/methods/adaptthink.md), [LASER](../../../../wiki/methods/laser.md)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), MATH500, AMC2023, [AIME 2024](../../../../wiki/datasets/aime-2024.md), [AIME 2025](../../../../wiki/datasets/aime-2025.md)

Tags: `overthinking`, `efficient reasoning`, `reflection`, `length penalty`, `reinforcement learning`, `rloo`, `chain-of-thought`, `math reasoning`, `iclr-2026`

---

Record id: `title:833de99e9b3ea69d`
