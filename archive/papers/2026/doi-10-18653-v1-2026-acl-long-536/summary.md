<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ReProbe: Efficient Test-Time Scaling of Multi-Step Reasoning by Probing Internal States of Large Language Models

- **Authors**: Jingwei Ni, Ekaterina Fadeeva, Tianyi Wu, Mubashara Akhtar, Jiaheng Zhang, Elliott Ash, Markus Leippold, Timothy Baldwin, See-Kiong Ng, Artem Shelmanov, Mrinmaya Sachan
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.536/>
- **PDF**: <https://aclanthology.org/2026.acl-long.536.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.536
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

ReProbe is a lightweight (<10M-parameter) transformer probe trained on a frozen LLM's internal states (hidden states, attention, logits) to predict step-level reasoning correctness, matching or exceeding Process Reward Models up to 810x larger for test-time-scaling verification, at 2.6-25x faster inference, and can be trained fully self-supervised (the model annotating its own reasoning) with no human labels or Monte Carlo rollouts.

## Problem

Test-time scaling (best-of-N, beam search) relies on scoring intermediate reasoning steps to select promising continuations, and the dominant approach -- Process Reward Models (PRMs) -- is computationally expensive (1.5B-8B-parameter separate models adding substantial inference-time memory and latency), typically domain-specific (mostly math, generalizing poorly to unseen domains), and costly to train (requiring Monte Carlo rollouts, human annotation, or large model-generated datasets).

## Contributions

- ReProbe, a lightweight (<10M-parameter) trainable probe that verifies reasoning-step correctness by introspecting a frozen LLM's internal states rather than relying on an external, much larger critic model
- empirical evidence across math, planning and QA tasks and multiple LLM families/modes that ReProbe matches or exceeds PRMs up to 810x larger, with a clear advantage on out-of-domain generalization, at 2.6-25x lower inference cost
- a fully self-supervised training recipe (the target LLM annotates its own reasoning) performing comparably to externally-supervised training, removing the need for human annotation or Monte Carlo rollouts
- demonstration that ReProbe-guided test-time scaling lets a smaller model (Qwen3-8B) outperform a larger sibling (Qwen3-14B) on several benchmarks, and that combining ReProbe with a PRM yields further gains

## Method

ReProbe is a plug-and-play module on top of a frozen LLM: at each reasoning step, it extracts token-level internal-state features from the base LLM (attention weights and logits, or hidden states, across all layers), projects them, processes with transformer layers, aggregates per-token features into a step-level vector via mean pooling, and classifies step correctness with a two-layer NN, trained with binary cross-entropy while the underlying LLM remains entirely frozen -- only the probe's fewer-than-10M parameters are updated. Training data is constructed via external verification (a larger LLM, DeepSeek-R1, judges step correctness) or self-supervised (the same LLM annotates its own generated CoT), using 10.8K math problems (~32K trajectories) from PRM800K.

## Results

For step-level correctness detection (PR-AUC) on Qwen3-8B, unsupervised UQ baselines substantially underperform, small PRMs show limited OOD generalization, and large PRMs (750-810x larger) reach the strongest in-domain math scores but degrade OOD; ReProbe achieves the best overall average PR-AUC (0.604), matching or exceeding the strongest PRMs on out-of-domain planning/QA tasks specifically (0.553 OOD average vs. best PRM's 0.429-0.518) while remaining competitive on in-domain math. This pattern holds in native think mode for Qwen3-1.7B/32B and Phi-4. In best-of-N test-time scaling on Qwen3-8B, ReProbe achieves the best average accuracy among all methods, with especially strong OOD planning gains. In beam-search test-time scaling, ReProbe achieves the strongest overall performance, notably enabling probed Qwen3-8B to outperform larger Qwen3-14B (pass@1) on multiple benchmarks. The self-supervised ReProbe variant achieves comparable performance to the externally-supervised one. Combining PRM and ReProbe scores yields further PR-AUC improvements, suggesting complementary signals. Scaling analysis shows performance improves with more training questions/trajectories and with higher training-data diversity. Runtime measurements show a 2.6x-25x speedup over state-of-the-art PRMs.

## Limitations

Performance of both ReProbe and PRMs degrades (slightly for ReProbe) as reasoning length increases. Step extraction relies on the base LLM following an instructed one-step-per-line format for structured CoT, or treats each sentence as a step for native thinking mode -- an approximation rather than semantically grounded segmentation. Primary training data uses 10.8K problems from a single source (PRM800K), and the paper's own scaling analysis shows PR-AUC continues improving with more training questions.

## Why it matters here

- **overthinking**: Directly relevant as efficient infrastructure for test-time scaling: rather than reducing reasoning length, it makes the verification signal that guides best-of-N/beam-search test-time scaling far cheaper (2.6-25x speedup, <10M vs. 1.5B-8B parameters) and more generalizable, which matters because most parallel test-time-scaling methods discussed elsewhere in this archive incur significant overhead from the verifier itself -- ReProbe's finding that internal states already encode reliable step-correctness signals is a complementary efficiency lever to reasoning-length-reduction methods, targeting the cost of evaluating reasoning rather than the cost of generating it.

## Entities

- **Concepts**: Reasoning Probe (ReProbe), internal-state-based step verification, self-supervised step-level annotation, PRM/ReProbe complementarity
- **Methods**: ReProbe (internal-state step-level probe), Process Reward Models (PRM baselines), unsupervised uncertainty quantification baselines, best-of-N and beam-search test-time scaling
- **Datasets**: PRM800K, [MATH](../../../../wiki/datasets/math.md), [GSM8K](../../../../wiki/datasets/gsm8k.md), ProofNet, Trip Planning, Meeting Planning, Calendar Scheduling, [StrategyQA](../../../../wiki/datasets/strategyqa.md), [ScienceQA](../../../../wiki/datasets/scienceqa.md)

Tags: `test-time-scaling`, `process-reward-model`, `internal-state-probing`, `step-level-verification`, `efficient-reasoning`

## Abstract

LLMs can solve complex tasks by generating long, multi-step reasoning chains. Test-time scaling (TTS) can further improve LLM performance by sampling multiple variants of intermediate reasoning steps, verifying their correctness, and strategically choosing the best steps for continuation. However, existing verification approaches, such as Process Reward Models (PRMs), are computationally expensive, limited to specific domains, and require large-scale human or model-generated annotations. We propose a lightweight alternative for step-level reasoning verification based on probing the internal states of LLMs. We train a transformer-based probe that uses the internal states of the frozen LLM to estimate the credibility of its reasoning steps during generation. Annotation can be generated either by another larger LLM (e.g., DeepSeek-R1) or in a self-supervised manner by the original model itself. The probes are both effective and lightweight, containing fewer than 10M parameters. Across multiple domains, including mathematics, planning, and general knowledge question answering, our probes match or even exceed the performance of PRMs that are up to 810× larger. Our findings suggest that the internal states of LLMs encode their confidence in reasoning processes and can serve as reliable signals for reasoning step verification, offering a promising direction towards scalable and generalizable TTS and introspective LLMs.

---

Record id: `doi:10.18653/v1/2026.acl-long.536`
