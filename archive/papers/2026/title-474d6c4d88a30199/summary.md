<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# REA-RL: Reflection-Aware Online Reinforcement Learning for Efficient Reasoning

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10010716>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

REA-RL trains a large reasoning model online with a distilled 7B reflection model that supplies both parallel samples and truncated sequential revisions, plus a reflection-density reward, cutting response length about 36% on math benchmarks without losing accuracy.

## Problem

Large reasoning models overthink, producing long chains of thought that raise inference cost. Two existing remedies each fail: offline approaches synthesize shorter reasoning responses for the model to imitate, but the generation-and-filtering loop is too slow to run online; and online RL with a plain length reward pushes the model toward short responses that have lost the ability to reflect, which costs accuracy. The open question is how to shorten reasoning online without destroying the reflection behaviour that makes the reasoning work.

## Contributions

- A small distilled reflection model that identifies the first reflection point in a sampled response likely to reach the final answer, allowing responses to be truncated into shorter revisions during online RL rather than through offline generate-and-filter.
- Sequential revision combined with parallel sampling as a training-time scaling scheme for online efficiency RL.
- A reflection reward penalizing responses whose reflection token density falls below the 20th percentile of the training distribution, blocking short non-reflective responses that a plain length reward rewards.
- An empirical result of about 36% token reduction at unchanged accuracy on a five-benchmark math suite with DeepSeek-R1-Distill-Qwen-7B, against a length-reward GRPO baseline that loses about 3.5 accuracy points for a comparable saving.
- Analysis showing reflection frequency is preserved on hard problems and reduced on easy ones.

## Method

REA-RL adds a small reflection model to online RL over a large reasoning model. The reflection model is obtained by distilling a Qwen2.5-32B detector into Qwen2.5-7B-Instruct via supervised fine-tuning, so that detection is a single step. Given a sampled response, it locates the first reflection position that is already very likely to lead to the final answer, and the response is truncated there to yield a shorter revision. This gives sequential revision alongside ordinary parallel sampling, so training-time scaling produces short-but-complete trajectories cheaply instead of by generate-and-filter. Separately, a reflection reward penalizes responses whose reflection token density falls in the bottom fifth of the training distribution: R_Reflect(s_i) = min(0, D_i / D_0.2 - 1), where D_i = N_Reflect / N_Token. The floor at zero means a response with adequate reflection density is not rewarded for more, only sparse ones are punished, which blocks the degenerate short-and-non-reflective solutions a bare length reward admits. The length reward and the reflection reward and the reflection model are combined on top of GRPO.

## Results

Reported on GSM8K, MATH500, Gaokao23, AMC23 and AIME24 with a 16k token budget, starting from DeepSeek-R1-Distill-Qwen-7B. The unmodified base model scores 80.39% average accuracy at a token ratio of 100. GRPO with a plain length reward drops to 76.88% accuracy at a token ratio of 57.23 — i.e. the length reward buys its shortening with roughly 3.5 points of accuracy, which is the failure the paper is arguing against. The full combination (GRPO + length reward + reflection reward + reflection model) reaches 80.74% accuracy at a token ratio of 63.51, so about 36% fewer tokens at accuracy equal to or slightly above the base model. Analysis reports that reflection frequency is retained on hard problems and reduced on easier ones, rather than being suppressed uniformly.

## Limitations

The authors state the method is validated only on distilled 7B large reasoning models, so it is untested at other scales or on non-distilled models. They state that reflection-position detection cannot guarantee complete elimination of overthinking. They state that sequential scaling adds roughly 10% cost over parallel scaling alone. Beyond the stated limits: the headline 36% is an aggregate token ratio over a five-benchmark suite dominated by easier sets, so it does not establish a per-benchmark saving; the accuracy margin over the base model (80.39 to 80.74) is well inside the noise typical of AMC23 and AIME24, which have few problems each, so the claim supported by the numbers is non-degradation rather than improvement; and the reflection reward is defined against a density quantile of the training data, which ties the notion of adequate reflection to one corpus.

## Why it matters here

- **overthinking**: Directly on topic, and it makes a specific claim about why the obvious fix fails. A plain length reward is the standard online lever for shortening reasoning, and this paper's own numbers give the cost of using it alone: 76.88% versus 80.39% accuracy on the same suite. The paper's answer is that shortening must be constrained to preserve reflection, enforced as a floor on reflection token density rather than as a length target, and that this recovers base accuracy (80.74%) at a similar token ratio (63.51 vs 57.23). The reported pattern — reflection frequency held on hard problems and reduced on easy ones — is the difficulty-adaptive allocation the topic is about, achieved without an explicit difficulty estimator. The reflection model is also a reusable idea for the topic: a small model that decides where a trace could have stopped, rather than a fixed budget imposed in advance. Caveat for the archive: validated on one 7B distilled model and one math suite, so the 36% figure should be read as evidence for the mechanism, not as a transferable rate.

## Entities

- **Concepts**: [Overthinking](../../../../wiki/concepts/overthinking.md), Reflection in reasoning traces, [Length reward](../../../../wiki/concepts/length-reward.md), Reflection reward, [Sequential revision](../../../../wiki/concepts/sequential-revision.md), [Test-time compute scaling](../../../../wiki/concepts/test-time-compute-scaling.md), Online reinforcement learning for efficient reasoning, Difficulty-adaptive reasoning length
- **Methods**: REA-RL, [GRPO](../../../../wiki/methods/grpo.md), reflection reward, sequential revision, parallel sampling, supervised fine-tuning distillation, [DeepSeek-R1-Distill-Qwen-7B](../../../../wiki/methods/deepseek-r1-distill-qwen-7b.md), Qwen2.5-7B-Instruct, Qwen2.5-32B
- **Datasets**: [DeepScaleR](../../../../wiki/datasets/deepscaler.md), [GSM8K](../../../../wiki/datasets/gsm8k.md), MATH500, Gaokao23, [AMC23](../../../../wiki/datasets/amc23.md), AIME24

Tags: `overthinking`, `efficient-reasoning`, `reinforcement-learning`, `grpo`, `reflection`, `length-reward`, `chain-of-thought`, `inference-cost`, `math-reasoning`

---

Record id: `title:474d6c4d88a30199`
