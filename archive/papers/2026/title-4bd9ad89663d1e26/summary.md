<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# IAPO: Information-Aware Policy Optimization for Token-Efficient Reasoning

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/63983>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

IAPO shapes token-level RL advantages by each reasoning token's conditional mutual information with the final answer, so uninformative exploration is suppressed rather than length being penalized in aggregate, reporting up to 36% shorter reasoning at equal or better accuracy on math benchmarks.

## Problem

Long chains of thought raise accuracy but cost inference-time compute. Existing token-efficient post-training shapes the reward at the sequence level — a length penalty applied to the whole trajectory — which gives no control over where within the trace the effort should be cut. Existing token-level schemes assign credit by length or position heuristics, which are content-agnostic: they cannot tell an informative reasoning step from a verbose one, so shortening pressure lands indiscriminately on both. What is missing is a per-token criterion for whether a token is doing work toward the answer.

## Contributions

- A token-level advantage derived from each token's conditional mutual information with the final answer, replacing content-agnostic length- and position-based heuristics for credit assignment in token-efficient RL.
- An early-exit conditional MI estimator that elicits the answer distribution at an intermediate position with a short '</think><answer>' postfix and measures entropy reduction.
- KV-cache preloading and chunk-wise forwarding, reducing MI-estimation complexity from O(L^3 d) to about O((K^3 + L^2) d).
- A theoretical analysis claiming monotonic reduction in reasoning verbosity without loss of correctness.
- Empirical comparison against DAPO, GFPO, GTPO and S-GRPO on Qwen2.5 0.5B/1.5B/7B over GSM8K, MATH-500 and DAPO-Math-17k, reporting up to 36% length reduction and the best Pass@k/Length@k ratio.
- Released code at https://github.com/YinhanHe123/IAPO

## Method

IAPO assigns a token-wise advantage from an information-theoretic quantity: the conditional mutual information between token o_{i,t} and the final answer y_i given the question and the preceding tokens, I(y_i ; o_{i,t} | q, o_{i,<t}). Estimating this at every position is the expensive part, and three techniques make it tractable. (1) An early-exit estimator approximates the MI as the reduction in entropy of the answer distribution before and after the token is generated; the answer distribution at an intermediate position is elicited by appending a short postfix prompt ('</think><answer>') and reading the model's answer logits, so no separate probe model is trained. (2) KV-cache preloading stores the transformer states from a single full forward pass over the trace and reuses them for the entropy evaluations at intermediate positions, removing redundant prefix recomputation. (3) Chunk-wise forwarding batches the MI computations for groups of tokens into single forward passes. The final token advantage combines the sequence-level reward, the normalized MI informativeness score, and an exploration adjustment term that keeps the policy from collapsing to a single mode. The paper also gives a theoretical argument that this shaping induces monotonic reduction in verbosity without harming correctness.

## Results

Base models are Qwen2.5 at 0.5B, 1.5B and 7B-Instruct; data are GSM8K, MATH-500 and DAPO-Math-17k. The reported headline is up to 36% reduction in reasoning length while accuracy is maintained or improved. The concrete instance given is Qwen2.5-7B-Instruct on GSM8K, where IAPO reaches 100% Pass@32 using 111.83 tokens against 177.62 tokens for the S-GRPO baseline, roughly a 37% reduction. Across settings IAPO reports the best token-efficiency ratio (Pass@k divided by Length@k) against DAPO, GFPO, GTPO and S-GRPO. On cost: the acceleration techniques are stated to reduce MI-estimation complexity from O(L^3 d) to about O((K^3 + L^2) d) with postfix length K much smaller than completion length L, and wall-clock inference time is reported improved by more than 11%.

## Limitations

No limitations section is stated. Several should be noticed from the numbers. The showcase result is 100% Pass@32 on GSM8K, a saturated benchmark at 7B under 32 samples — at ceiling accuracy any method can trade tokens freely, so this instance demonstrates compression, not a preserved accuracy/length frontier, and the 'up to 36%' is drawn from the most favourable such setting. The evaluation is math-only (GSM8K, MATH-500, DAPO-Math-17k) at 0.5B to 7B, so nothing is established for other domains or larger reasoning models. Pass@k over 32 samples is a lenient accuracy criterion relative to greedy or Pass@1 and can hide degradation in the modal answer. The MI estimate itself rests on an approximation — entropy reduction in an answer distribution elicited by a forced early-exit postfix — whose fidelity to the true conditional mutual information is not something the reported numbers verify, and the theoretical monotonicity guarantee is stated for the idealized quantity rather than for the estimator. The training-time overhead of MI estimation is characterized asymptotically rather than as measured training cost against the baselines.

## Why it matters here

- **overthinking**: Directly on topic, and it sharpens the question the topic asks. Most length-control work asks how long a trace should be and applies pressure to the trajectory as a whole; IAPO argues that this is the wrong granularity, because a sequence-level length penalty cannot distinguish an informative step from filler and so shortens both. Its criterion — a token's conditional mutual information with the final answer — is a candidate operational definition of a token doing work, which is exactly the quantity the topic has lacked when it says a model 'thought more than the problem needed'. It also pairs instructively with truncation-based measurement: MI per token and reward-versus-truncation curves are two ways of asking which part of a trace is load-bearing, one during training, one at evaluation. The archive should record the mechanism rather than the headline: the 36% figure comes from a setting at 100% Pass@32 on GSM8K, where accuracy is saturated and tokens can be traded away for free, so the numbers demonstrate that the MI signal compresses traces without collapsing them, not that the accuracy/length frontier was moved on a hard benchmark. Evidence is math-only at 0.5B-7B.

## Entities

- **Concepts**: Token-efficient reasoning, Conditional mutual information, Token-wise advantage shaping, Reasoning verbosity, Low-utility exploration, Test-time compute cost, Pass@k per token efficiency, [Overthinking](../../../../wiki/concepts/overthinking.md)
- **Methods**: IAPO, conditional mutual information advantage shaping, early-exit MI estimator, KV-cache preloading, chunk-wise forwarding, [GRPO](../../../../wiki/methods/grpo.md), [S-GRPO](../../../../wiki/methods/s-grpo.md), DAPO, [GFPO](../../../../wiki/methods/gfpo.md), GTPO, [Qwen2.5-Instruct](../../../../wiki/methods/qwen2-5-instruct.md)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH-500](../../../../wiki/datasets/math-500.md), [DAPO-Math-17k](../../../../wiki/datasets/dapo-math-17k.md)

Tags: `overthinking`, `token-efficient-reasoning`, `mutual-information`, `advantage-shaping`, `reinforcement-learning`, `chain-of-thought`, `reasoning-length`, `inference-cost`, `math-reasoning`

---

Record id: `title:4bd9ad89663d1e26`
