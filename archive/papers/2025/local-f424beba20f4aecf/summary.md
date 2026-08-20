<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Optimal Stopping vs Best-Of-N for Inference Time Optimization

- **Authors**: Yusuf Kalayci, Vinod Raman, Shaddin Dughmi
- **Venue**: preprint
- **Published**: 2025-01-01
- **Source**: local
- **Topics**: test-time-scaling
- **Relevance score**: test-time-scaling 0.50

## In one line

Casts each generation as opening a costly box in Weitzman's Pandora's Box problem and learns the optimal stopping threshold online, matching best-of-N quality with 15-35% fewer generations.

## Problem

Best-of-N fixes the number of generations in advance, so it wastes compute when an acceptable output arrives early or the prompt is easy, and under-spends when it is hard. Existing early-stopping heuristics have no guarantees and underperform on difficult prompts, and no principled framework said when to stop while keeping near-optimal reward.

## Contributions

- A framing of inference-time optimization as the Pandora's Box optimal-stopping problem, with best-of-N as a special case
- UCB Pandora's Box, the first stopping strategy for Pandora's Box with unknown reward distributions, using anytime-valid confidence bounds on the fair-cap value
- A vanishing-regret guarantee against Weitzman's optimal policy, which requires full distributional knowledge
- A Bradley-Terry inspired reward normalization addressing cross-prompt scale differences
- 15-35% fewer generations than non-adaptive best-of-N at equal reward on AlpacaFarm and HH-RLHF

## Method

Generation is mapped onto Pandora's Box: each sample opens a box at cost c revealing a reward drawn from a distribution D induced by the model and the reward model, and the decision is when to stop and keep the best reward seen. The relevant special case is infinitely many boxes with identical distribution and cost, since a single LLM can be queried without limit. Weitzman's algorithm solves this optimally when D is known, by sampling until a reward exceeds the fair-cap value tau defined by E[(v - tau)_+] = c. Because D is unknown in practice, UCB Pandora's Box maintains an anytime-valid upper confidence bound on tau from the rewards seen so far and stops once the maximum observed reward exceeds it. A Bradley-Terry inspired transformation normalizes rewards across prompts, since a reward model's scale is not comparable between questions and a single threshold otherwise means different things for different prompts.

## Results

UCB Pandora's Box attains vanishing regret against Weitzman's optimal policy, which assumes full knowledge of the distribution; performance is measured as an additive sub-optimality gap in net payoff, maximum reward minus total cost. On AlpacaFarm and HH-RLHF across multiple LLM and reward-model pairs, the adaptive strategy reaches the same reward as non-adaptive best-of-N using 15-35% fewer generations on average.

## Limitations

The guarantee needs the unknown distribution to lie in a known family F admitting an anytime-valid confidence sequence — the paper is explicit that a fully adversarial distribution admits no uniformly bounded sub-optimality gap. Results cover the i.i.d. single-distribution case; the authors note Weitzman's algorithm handles multiple box types and expect but do not prove the extension to ensembles. The objective is reward under a given reward model, so the method inherits that model's miscalibration and any gap between reward and correctness — it optimizes stopping, not what is being maximized. Evaluation is on preference datasets rather than reasoning benchmarks, so the compute savings are not demonstrated on mathematics or code.

## Why it matters here

- **test-time-scaling**: Names the decision this topic keeps rediscovering and supplies the classical theory for it. Every stopping signal in this archive — DEER, Dynasor, CUSUM change-point detection, certaindex, confidence-based early exit — is an estimator of when to quit, invented independently and compared to nothing. Pandora's Box says what the optimal rule is when the reward distribution is known, and the fair-cap value E[(v - tau)_+] = c gives those heuristics a common target to be measured against. The practical contribution is the cross-prompt normalization: a single stopping threshold is meaningless while reward scale varies by question, which is a defect the archive's threshold-based methods share and none of them corrects.

## Entities

- **Concepts**: optimal stopping, Pandora's box, fair-cap value, [test-time compute](../../../../wiki/concepts/test-time-compute.md), [adaptive compute allocation](../../../../wiki/concepts/adaptive-compute-allocation.md), regret, best-of-n, reward model calibration, [exploration-exploitation trade-off](../../../../wiki/concepts/exploration-exploitation-trade-off.md)
- **Methods**: UCB Pandora's Box, Weitzman's algorithm, [best-of-n](../../../../wiki/methods/best-of-n.md), Bradley-Terry transformation, anytime-valid confidence sequences
- **Datasets**: AlpacaFarm, HH-RLHF

Tags: `optimal stopping`, `pandora's box`, `best-of-n`, `test-time compute`, `theory`

## Abstract

Large language model (LLM) generation often requires balancing output quality against inference cost, especially when using multiple generations. We introduce a new framework for inference-time optimization based on the classical Pandora's Box problem. Viewing each generation as opening a costly "box" with random reward, we develop algorithms that decide when to stop generating without knowing the underlying reward distribution. Our first contribution is a UCB-style Pandora's Box algorithm, which achieves performance that is provably close to Weitzman's algorithm, the optimal strategy when the distribution is known. We further adapt this method to practical LLM settings by addressing reward scaling across prompts via a Bradley-Terry inspired transformation. This leads to an adaptive inference-time optimization method that normalizes rewards and learns stopping thresholds on the fly. Experiments on the AlpacaFarm and HH-RLHF datasets, using multiple LLM-reward model pairs, show that our adaptive strategy can obtain the same performance as non-adaptive Best-of-N sampling while requiring 15-35% fewer generations on average. Our results establish a principled bridge between optimal stopping theory and inference-time scaling, providing both theoretical performance bounds and practical efficiency gains for LLM deployment.

---

Record id: `local:f424beba20f4aecf`
