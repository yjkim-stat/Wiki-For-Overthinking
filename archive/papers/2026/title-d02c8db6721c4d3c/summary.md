<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Sample More to Think Less: Group Filtered Policy Optimization for Concise Reasoning

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10009238>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

GFPO samples a larger group of rollouts per problem during RL training and updates only on the top-k by length or by reward-per-token, converting extra training-time compute into shorter responses at inference.

## Problem

Reinforcement learning with verifiable rewards inflates response length: the policy buys accuracy gains with tokens, and much of what it adds is filler — repetitive, verbose text that makes no progress on the problem. GRPO's scalar reward gives no way to express a preference among correct answers, so nothing in the objective distinguishes a concise correct trace from a padded one.

## Contributions

- GFPO, which filters a sampled group by a chosen metric and zeroes the advantage of everything outside the top-k, letting a scalar-reward RL objective express a preference among correct responses
- Token efficiency (reward per token) as a selection metric, giving larger length cuts than selecting on length alone
- Identification of the retained fraction k/G as the control knob for response length
- Adaptive Difficulty GFPO, which sets k per question from a t-digest difficulty estimate so that harder problems retain more long solutions
- The trade it names explicitly: additional training-time sampling converts into reduced test-time compute

## Method

GFPO keeps GRPO's group-relative structure but changes what enters the gradient. For each question it samples a group of G responses (G tested at 8, 16, 24), scores each by a selection metric, and retains the top-k; every response outside the retained subset is assigned zero advantage and so contributes nothing to the policy update. Two metrics are used: shortest response length, and token efficiency, defined as reward divided by token count. k is held at 8 or below so the number of responses actually producing gradient signal matches GRPO's, making the comparison fair — the extra compute goes into selection, not into a larger effective batch. The paper identifies the retained proportion k/G as the knob that controls length: lowering it, by cutting k or raising G, buys more reduction. Adaptive Difficulty GFPO varies k with a running difficulty estimate maintained in a t-digest over recent reward statistics: k=4 for easy questions, k=6 for medium, k=8 for hard and very hard, all out of G=16, so harder problems keep more of their long solutions.

## Results

Base model is Phi-4-reasoning, and the metric is reduction in GRPO's excess length (the length inflation over the pre-RL model), not raw length. Shortest-8/16 GFPO cuts excess length by 23.8% on AIME 25, 33.0% on AIME 24, 23.7% on GPQA, 31.5% on Omni-MATH and 36.5% on LiveCodeBench. Token Efficiency GFPO cuts it by 70.9%, 84.6%, 79.7%, 82.6% and 79.7% on the same five benchmarks. Adaptive Difficulty GFPO cuts 50.8%, 52.9%, 41.7%, 35.1% and 49.4%, and exceeds GRPO's accuracy on medium and very hard problems while reducing excess length by 47%-60%. Significance testing found no statistically significant accuracy difference between any GFPO variant and GRPO across tasks. End-to-end latency falls by roughly 30%, with about 90 seconds cut from response time on hard queries. The abstract's headline range of 46-71% (rising to 71-85% for reward per token) is a summary across benchmarks; the per-benchmark shortest-response numbers above are lower than that range at its bottom end.

## Limitations

The paper's own numbers qualify the headline in four places. Token Efficiency GFPO, which produces the largest cuts, shows minor accuracy degradations — not statistically significant — together with higher training variance, so the 71-85% figure is the variant with the weakest accuracy guarantee. Adaptive Difficulty GFPO takes a modest accuracy drop on hard problems, because filtering to the shortest responses is riskiest exactly where few correct long solutions exist. Training was on mathematics only, and on LiveCodeBench the Adaptive Difficulty variant transferred less well than the others. Returns diminish at extreme filtering: k/G of 4/24 adds little over 6/24. Beyond these, the accuracy claim rests on failure to reject a null hypothesis rather than on a demonstrated equivalence, the training cost is roughly doubled at G=16 versus G=8, and results come from a single base model.

## Why it matters here

- **overthinking**: Directly on topic, and it locates the cause rather than treating the symptom. The paper's claim is that length inflation is an artifact of the RL objective itself — a scalar verifiable reward cannot prefer a short correct answer to a padded one, so the policy drifts long — and that the fix needs no length penalty, no auxiliary reward term and no separate controller: simply refusing to learn from the verbose members of each sampled group is enough. That makes it a different kind of intervention from budget-setting or trace-truncation methods, because the shortening is baked into the policy and costs nothing at inference. Two results are worth carrying. First, the knob is the retained fraction k/G, which gives a single dial trading length against the diversity of the gradient signal. Second, and more useful for the group's central question, Adaptive Difficulty GFPO shows the dial should not be set uniformly: filtering hard on easy problems is free, and filtering hard on genuinely difficult ones costs accuracy, because the long correct solutions are the only correct solutions there. That is direct evidence that some long reasoning is load-bearing, and it marks the boundary the topic is about. The counterweight is that accuracy preservation is established by non-significance across a single base model, and the largest cuts come from the variant with the least stable accuracy.

## Entities

- **Concepts**: Length inflation under RLVR, Filler tokens, Token efficiency (reward per token), [Group-relative advantage](../../../../wiki/concepts/group-relative-advantage.md), Response filtering, Retained fraction k/G, Adaptive difficulty allocation, Training-time compute traded for test-time compute
- **Methods**: [GFPO](../../../../wiki/methods/gfpo.md), Group Filtered Policy Optimization, Adaptive Difficulty GFPO, [GRPO](../../../../wiki/methods/grpo.md), [Reinforcement learning with verifiable rewards](../../../../wiki/methods/rlvr.md), t-digest, [Phi-4-reasoning](../../../../wiki/methods/phi-4-reasoning.md)
- **Datasets**: [AIME 24](../../../../wiki/datasets/aime-2024.md), [AIME 25](../../../../wiki/datasets/aime-2025.md), [GPQA](../../../../wiki/datasets/gpqa.md), [Omni-MATH](../../../../wiki/datasets/omni-math.md), [LiveCodeBench](../../../../wiki/datasets/livecodebench.md)

Tags: `overthinking`, `concise-reasoning`, `rlvr`, `grpo`, `length-inflation`, `token-efficiency`, `response-filtering`, `efficient-reasoning`

---

Record id: `title:d02c8db6721c4d3c`
