<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# DRPO: Efficient Reasoning via Decoupled Reward Policy Optimization

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10010492>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Diagnoses why adding a length penalty to GRPO degrades accuracy — the group-relative advantage can turn correct-but-long rollouts negative — and fixes it by normalising the reward of correct rollouts only against other correct rollouts.

## Problem

Large reasoning models trained with RL (e.g. GRPO) overthink: they emit long redundant chains even on easy questions, raising cost and latency. The obvious remedy, adding a length reward, causes marked accuracy loss. The paper identifies the cause: GRPO's advantage is normalised over the whole group of rollouts, so once a correct but long rollout is length-penalised its reward can fall below the group mean and receive a negative advantage, so training actively pushes the policy away from a valid solution. Getting length reduction without that side effect is the open problem.

## Contributions

- Identifies that GRPO's group-relative advantage assigns negative advantage to correct but length-penalised rollouts, explaining the accuracy loss of length-reward methods
- Proposes DRPO, which normalises correct-rollout rewards only within the positive group so length penalties cannot invert their sign
- Derives a closed-form solution for the KL-regularised optimised positive distribution, making the objective computable from on-policy data with importance weighting and no extra rollout overhead
- Generalises the formulation to arbitrary preference rewards over positive data, not just length
- Reports 77% length reduction at 1.1% accuracy loss on GSM8K with a 1.5B model, against 68% for 4.3% for the strongest baseline, over six efficient-reasoning baselines at two model scales

## Method

Decoupled Reward Policy Optimization (DRPO) separates the length-based learning signal of correct rollouts from that of incorrect ones. Rewards for correct rollouts are normalised solely within the positive group, so a length penalty can only shrink a correct rollout's positive signal, never drive it negative. The objective is constructed by defining an optimised positive-data distribution that maximises the length-based reward under a KL regulariser, and integrating that distribution into a discriminative objective. The authors derive a closed-form solution for the optimised distribution, which makes the objective and its gradients computable from on-policy data alone with importance weighting, adding no extra rollout cost. The formulation is not specific to length: any preference reward over positive data can be substituted. A coefficient lambda trades length reduction against accuracy.

## Results

Fine-tuned from DeepSeek-R1-Distill-Qwen-1.5B and -7B on DeepScaleR-Preview-Dataset (~40.3k QA pairs from AIME, AMC, Omni-MATH, Still), evaluated on GSM8K, MATH-500, OlympiadBench and AIME, against six efficient-reasoning baselines. At 1.5B with lambda=0.1: 77.2% length reduction on GSM8K for 1.1% accuracy loss, where the next-best baseline gives 68% reduction for 4.3% loss; average Pass@1 0.624 at 1,527 tokens against RLOO-LP at 0.567 and 2,531 tokens. At 7B: 73.1% length reduction on GSM8K for 0.6% loss; average Pass@1 0.714 at 1,502 tokens against RLOO-LP at 0.692 and 2,649 tokens. On the combined Accuracy-Efficiency Score, DRPO is positive (0.178 at 1.5B, 0.249 at 7B) while all baselines are negative.

## Limitations

The authors state experiments were confined to 1.5B and 7B models for compute reasons and leave larger models to future work. The paper's own numbers also qualify the headline: the large length reductions are on GSM8K, the easiest benchmark, and on AIME — the hardest — DRPO's Accuracy-Efficiency Score is negative, i.e. the accuracy given up is not repaid by the tokens saved once problems are genuinely difficult. So the method is best evidenced as a cure for overthinking on easy questions rather than as a general efficiency gain, which is consistent with its framing but not with reading the 77% figure as an average. Evaluation is mathematical reasoning only, and the tradeoff is governed by a hand-set lambda.

## Why it matters here

- **overthinking**: On topic, and directly so. It names overthinking as the target, and its contribution is a mechanism-level account of why the standard fix fails: with a group-relative advantage, penalising length can make a correct long rollout a negative example, so the policy is trained away from valid reasoning. That is a concrete failure mode for any length-reward scheme the group might consider, independent of DRPO's own remedy. The paper also supplies a clean accuracy-versus-length operating point (77% shorter for 1.1% accuracy at 1.5B) and, in its AES numbers, evidence for where the tradeoff stops paying: negative on AIME, meaning length pressure hurts on genuinely hard problems while paying off on easy ones. That difficulty-dependence is the shape the overthinking topic cares about.

## Entities

- **Concepts**: [Overthinking](../../../../wiki/concepts/overthinking.md), [Length Reward](../../../../wiki/concepts/length-reward.md), [Group-Relative Advantage](../../../../wiki/concepts/group-relative-advantage.md), [Accuracy-Efficiency Tradeoff](../../../../wiki/concepts/accuracy-efficiency-tradeoff.md), [Efficient Reasoning](../../../../wiki/concepts/efficient-reasoning.md), Reinforcement Learning from Verifiable Rewards
- **Methods**: DRPO (Decoupled Reward Policy Optimization), [GRPO](../../../../wiki/methods/grpo.md), [RLOO](../../../../wiki/methods/rloo.md), length reward / length penalty, KL-regularised optimal distribution, importance weighting, Accuracy Efficiency Score (AES)
- **Datasets**: DeepScaleR-Preview-Dataset, [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH-500](../../../../wiki/datasets/math500.md), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md), [AIME](../../../../wiki/datasets/aime.md)

Tags: `overthinking`, `efficient-reasoning`, `grpo`, `rl-post-training`, `length-penalty`, `reasoning-length`

---

Record id: `title:68327bf6b9e4e869`
