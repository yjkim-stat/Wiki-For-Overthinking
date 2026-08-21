<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# S-GRPO: Early Exit via Reinforcement Learning in Reasoning Models

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/115333>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.62

## In one line

S-GRPO trains a reasoning model to stop its chain of thought early by sampling one reasoning path, forcing answers at several truncation points along it, and paying correct answers a reward that decays with how late the exit was.

## Problem

Outcome-reward RL (GRPO and relatives) scores only the final answer, so nothing in training regulates the intermediate reasoning process. Models post-trained this way -- including Qwen3 and DeepSeek-R1 distills -- keep generating redundant thought after they have enough to answer. The open question is how to give a reward signal about the sufficiency of a partial reasoning trace when only the final answer is verifiable.

## Contributions

- Serial-group rollout: instead of GRPO's parallel samples of distinct reasoning paths, sample one path and derive a group from truncations of it at multiple exit positions.
- A decaying reward over exit position (1/2^(N_right-1) for correct, 0 for incorrect) that makes an earlier correct answer strictly more valuable than a later one without penalizing length directly.
- Reported compatibility across two model families and four checkpoints (DeepSeek-R1-Distill-Qwen 7B/14B, Qwen3 8B/14B) on GSM8K, AIME 2024, AMC 2023, MATH-500 and GPQA Diamond.
- An ablation showing that rewarding only the shortest correct response -- the naive length penalty -- loses 2.56% accuracy, locating the failure mode the decaying reward is designed to avoid.

## Method

Each query gets a two-phase rollout. Phase one generates one complete reasoning path. Phase two picks m temporal positions along that path (8 per query in the reported setup, uniformly distributed), truncates the thought at each, and injects the prompt 'Time is limited, stop thinking and start answering' to elicit an answer from that prefix. The full path plus its truncated variants form the 'serial group' -- the serial counterpart to GRPO's parallel group of independently sampled paths. Rewards are assigned within the group by exit position: a correct answer at position i receives r = 1/2^(N_right-1), where N_right counts how many correct answers have accumulated up to and including that position, so the earliest correct exit gets 1 and each later correct exit is halved; an incorrect answer gets 0. Advantages are computed over the serial group as in GRPO. Training used lr 1e-6, Adam, and a combined generation/training batch of 128x8.

## Results

Per-model overall figures (arXiv v2 tables): DeepSeek-R1-Distill-Qwen-7B +6.08% accuracy with 61.1% fewer tokens; DeepSeek-R1-Distill-Qwen-14B +0.72% with 35.4% fewer; Qwen3-8B +2.36% with 40.6% fewer; Qwen3-14B +1.14% with 40.4% fewer. Per-benchmark on the 7B distill: GSM8K +1.4% / -50.6% tokens, AIME 2024 +0.6% / -44.3%, AMC 2023 +10.3% / -63.9%, MATH-500 +6.6% / -59.8%, GPQA Diamond +0.7% / -75.6%. No accuracy drop is reported for any model-benchmark pair. An ablation that rewards only the shortest correct response costs 2.56% accuracy. Note the version drift in the headline range: the NeurIPS-page abstract states 40.4%-61.1% length reduction and 0.72%-3.92% accuracy gain, while arXiv v2 states 35.4%-61.1% and 0.72%-6.08% -- the 35.4% figure is the 14B distill, which the narrower range excludes.

## Limitations

The paper states no limitations section. Things a reader should notice: (1) the headline range moved between versions -- the abstract on the NeurIPS page claims 40.4%-61.1% reduction and up to 3.92% accuracy gain, arXiv v2 claims 35.4%-61.1% and up to 6.08%, so the single number quoted from this paper depends on which version is being read; (2) the gains are strongly uneven across scale -- the 7B distill gets +6.08%/-61.1% while the 14B distill of the same family gets +0.72%/-35.4%, so the case that S-GRPO both shortens and improves is much weaker at the larger size; (3) the exit is induced by injecting a fixed instruction into the trace, so the learned behaviour is conditioned on that intervention rather than on the model deciding to stop unprompted; (4) all five benchmarks are short-answer math or multiple-choice science, where a verifiable final answer exists -- nothing tests domains without one; (5) the ablation showing a 2.56% drop under an aggressive length penalty is evidence that the accuracy/length tradeoff is real and that the decaying schedule is a tuned point on it, not an escape from it.

## Why it matters here

- **overthinking**: This is the primary paper for S-GRPO, which the archive's 'Don't Overthink It' survey catalogues under adaptive early exit. It is a direct attack on the topic's central mechanism: it argues overthinking is caused by outcome-only rewards that never grade the intermediate trace, and supplies a reward shape -- exponential decay over exit position within a serial group -- that grades one. It is evidence for the claim that length and accuracy are not strictly traded on these benchmarks: four checkpoints cut 35-61% of tokens while gaining 0.72-6.08% accuracy. Its own ablation supplies the counterweight the topic needs, showing that pushing the same idea to its limit (reward only the shortest correct answer) costs 2.56% accuracy -- so the tradeoff reappears once the pressure is strong enough. The uneven scaling (7B gains far more than 14B) is the number to carry forward: it suggests the redundancy S-GRPO removes may be more abundant in smaller distilled models than in larger ones.

## Entities

- **Concepts**: [Overthinking](../../../../wiki/concepts/overthinking.md), Early Exit, [Test-Time Scaling](../../../../wiki/concepts/test-time-scaling.md), [Chain-of-Thought Compression](../../../../wiki/concepts/chain-of-thought-compression.md), Outcome-Reward Reinforcement Learning, Serial Group Rollout, Decaying Reward, Sufficiency of Intermediate Reasoning
- **Methods**: S-GRPO (Serial-Group Decaying-Reward Policy Optimization), [GRPO](../../../../wiki/methods/grpo.md), early-exit prompting via injected instruction, DeepSeek-R1-Distill-Qwen-7B/14B, Qwen3-8B/14B
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [AIME 2024](../../../../wiki/datasets/aime-2024.md), AMC 2023, [MATH-500](../../../../wiki/datasets/math-500.md), [GPQA Diamond](../../../../wiki/datasets/gpqa-diamond.md)

Tags: `overthinking`, `early exit`, `reinforcement learning`, `grpo`, `chain-of-thought`, `test-time scaling`, `efficient reasoning`, `reward shaping`

## Abstract

Abstract As Test-Time Scaling emerges as an active research focus in the large language model community, advanced post-training methods increasingly emphasize extending chain-of-thought (CoT) generation length, thereby enhancing reasoning capabilities to approach Deepseek R1-like reasoning models. However, recent studies reveal that reasoning models (even Qwen3) consistently exhibit excessive thought redundancy in CoT generation. This overthinking issue arises from the inherent limitations of conventional outcome-reward reinforcement learning, which systematically overlooks the regulation of intermediate reasoning processes. This paper introduces Serial-Group Decaying-Reward Policy Optimization (S-GRPO), a novel reinforcement learning paradigm that enables models to implicitly evaluate the sufficiency of intermediate reasoning steps, thereby facilitating early exit in CoT generation. Unlike GRPO, which samples multiple possible reasoning paths in parallel (parallel group), S-GRPO only samples one reasoning path and serially selects multiple temporal positions from the path to exit thinking and directly generate answers (serial group). For correct answers within a serial group, rewards gradually decrease based on the exit positions along the reasoning path from front to back. This design encourages the model to produce more accurate and concise thoughts, while also incentivizing early thinking termination when appropriate. Empirical evaluations demonstrate that S-GRPO is compatible with state-of-the-art reasoning models, including Qwen3 and Deepseek-distill. Across diverse benchmarks such as GSM8K, AIME 2024, AMC 2023, MATH-500, and GPQA Diamond, S-GRPO achieves a substantial reduction in sequence length (40.4%～61.1%) while simultaneously improving accuracy (absolute 0.72%～3.92%).

---

Record id: `title:69eddf96377a8095`
