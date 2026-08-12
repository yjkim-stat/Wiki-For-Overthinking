# token-level entropy

<!-- auto:begin -->

The Shannon entropy of the model's next-token distribution at one generation step, computed over the whole vocabulary. All the sources stress it is a property of the distribution at a position, not of the token sampled there — the same token at two positions can carry different entropy. They disagree about how much it explains. Several treat it as the signal that matters: roughly 20% of chain-of-thought tokens are high-entropy and act as forks steering the reasoning path, a trajectory-level instability score built on it selects better rollouts, and step confidence decides whether to switch to latent reasoning or to stop generating. Others argue it is the wrong criterion. One notes distributions with identical entropy can have very different shapes and selects tokens instead by the divergence of their logit distribution from the group average, reporting that the tokens chosen that way split roughly evenly between the high- and low-entropy populations. Another shows that under a GRPO update the governing quantity is not a token's entropy but the deviation of a per-token discriminator from its policy-weighted expectation — so a criterion measured absolutely and one measured against a baseline pick different tokens from the same distribution.

- **Kind**: concept
- **Also called**: generation entropy, token entropy
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 7

**Related**: [advantage function](advantage-function.md), [AIME 24](../datasets/aime-24.md), [AIME 25](../datasets/aime-25.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC23](../datasets/amc23.md), [chain of thought](../methods/chain-of-thought.md), [Clip-Cov](../methods/clip-cov.md), [clip-higher](../methods/clip-higher.md), [covariance of probability and advantage](covariance-of-probability-and-advantage.md), [credit assignment](credit-assignment.md), [DAPO](../methods/dapo.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER](../methods/deer.md), [early exit](../methods/early-exit.md), [entropy bonus](entropy-bonus.md), [entropy collapse](entropy-collapse.md), [entropy regularization](../methods/entropy-regularization.md), [entropy trajectory](entropy-trajectory.md), [exploration-exploitation trade-off](exploration-exploitation-trade-off.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [HumanEval+](../datasets/humaneval.md), [implicit reasoning](implicit-reasoning.md), [KL-Cov](../methods/kl-cov.md), [KodCode](../datasets/kodcode.md), [latent chain of thought](../methods/latent-chain-of-thought.md), [latent reasoning](latent-reasoning.md), [LiveCodeBench](../datasets/livecodebench.md), [majority voting](../methods/majority-voting.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [Mistral-7B](../models/mistral-7b.md), [MMLU-STEM](../datasets/mmlu-stem.md), [OlympiadBench](../datasets/olympiadbench.md), [Omni-MATH](../datasets/omni-math.md), [overthinking](overthinking.md), [pass-k](../methods/pass-k.md), [performance ceiling](performance-ceiling.md), [policy entropy](policy-entropy.md), [policy gradient masking](../methods/policy-gradient-masking.md), [PPO](../methods/ppo.md), [PRIME](../methods/prime.md), [process supervision](process-supervision.md), [Qwen2.5-0.5B](../models/qwen2-5-0-5b.md), [Qwen2.5-1.5B](../models/qwen2-5-1-5b.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [Qwen3-8B](../models/qwen3-8b.md), [QwQ-32B](../models/qwq-32b.md), [reasoning redundancy](reasoning-redundancy.md), [REINFORCE](../methods/reinforce.md), [RLOO](../methods/rloo.md), [RLVR](../methods/rlvr.md), [scaling laws](scaling-laws.md), [self-certainty](../methods/self-certainty.md), [self-consistency](../methods/self-consistency.md), [softmax policy](softmax-policy.md), [test-time compute](test-time-compute.md), [VeRL](../methods/verl.md), [vLLM](../methods/vllm.md)

## Appears in

- [SeLaR: Selective Latent Reasoning in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-320/summary.md) — Switches to soft-embedding latent reasoning only at low-confidence steps, keeping discrete decoding elsewhere, and pushes the soft embeddings away from the top token to stop them collapsing.
- [Beyond Entropy: Learning from Token-Level Distributional Deviations for LLM Reasoning](../../archive/papers/2026/local-2175408b166d313f/summary.md) — Argues that Shannon entropy is the wrong criterion for picking which tokens to train on in RLVR, and selects tokens instead by the Jensen-Shannon divergence of their logit distribution from the group average, updating only the top 10% of these 'unique' tokens.
- [The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models](../../archive/papers/2025/local-5175928072823010/summary.md) — Establishes that RL trades policy entropy for reward along a predictable exponential curve R = -a·exp(H) + b, derives that entropy change is driven by the covariance between action probability and advantage, and controls it by restricting updates to the highest-covariance tokens.
- [Beyond the 80/20 Rule: High-Entropy Minority Tokens Drive Effective Reinforcement Learning for LLM Reasoning](../../archive/papers/2025/local-7d5e3edea2d46b92/summary.md) — Shows that the roughly 20% of CoT tokens with the highest entropy act as decision forks, and that restricting RLVR policy-gradient updates to only those tokens matches or beats full-gradient training, with the advantage growing with model size.
- [On the Entropy Dynamics in Reinforcement Fine-Tuning of Large Language Models](../../archive/papers/2026/local-837612b527cb427c/summary.md) — Reduces the question of whether an update raises or lowers entropy to the sign of one scalar per token, shows that under GRPO what matters is that scalar's deviation from a policy-weighted baseline rather than its own value, and proves the deviation averages to zero over a batch.
- [Dynamic Early Exit in Reasoning Models](../../archive/papers/2025/local-a1d9fa1eb8899dfc/summary.md) — Detects the points where a reasoning model switches thought chains, interrupts to induce a trial answer, and stops generation when that answer's confidence is high enough — cutting chain-of-thought length substantially while raising accuracy, with no training.
- [EDIS: Diagnosing LLM Reasoning via Entropy Dynamics](../../archive/papers/2026/local-e64d3a8c4788daf7/summary.md) — Introduces EDIS, a trajectory-level score that measures how unstably token entropy evolves during generation, and uses it to select better reasoning rollouts at inference and to curate training samples in RL.

<!-- auto:end -->

## Notes

### Correction (2026-08-08)

An earlier version claimed no pairwise overlap between the token-selection
criteria had been measured, while citing such a measurement three paragraphs
later. One pair *is* measured: the JS-divergence-selected set splits **1.03 on
GSM8K and 0.99 on MATH** by entropy rank.

### Five criteria, one measured pair

The archive now holds **five** proposals for which tokens an intervention should
act on, each with its own derivation and each beating GRPO.

| Criterion | Claim | Derived from |
| --- | --- | --- |
| High entropy | top 20% are "forking tokens" | empirical; +4.10 avg at 32B |
| Distributional uniqueness | JS divergence from group mean | Rényi entropy bifurcation |
| High covariance | Cov(log π, advantage) drives entropy change | first-order softmax derivation |
| Positive advantage | positive-advantage tokens concentrate mass | gradient of GRPO w.r.t. logit |
| **Elliptical bonus on representations** | novelty in hidden-state space | linear bandits / active learning |

**Correction on the fifth (2026-08-08, on close reading).** RepExp's primary
criterion is **response-level** — it selects a diverse coreset from N sampled
generations, so it belongs with best-of-N and self-consistency, not with the
token-selection family. It does have a token-level variant (its §4.2), which
perturbs the per-position logit vector with a token-level elliptic bonus, but
that is a proof of concept, not where its evidence sits. The honest count is
therefore **four token-level criteria → six pairwise overlaps, one measured,
five unmeasured**, with RepExp's token variant a sixth candidate whose evidence
is thinner than the others'.

Each unmeasured overlap is a counting exercise on tokens the papers' code
already computes.

The fifth is categorically different from the other four: it is a property of
the response's **semantic content**, not of the output distribution at a
position. That it also works — and eliminates diversity collapse, which none of
the distributional criteria does — is the strongest evidence that the first four
are not exhausting the space.

### The evidence that entropy alone is the wrong variable

- The divergence-selected set splits ~1:1 by entropy. If entropy were operative
  it should skew high.
- **Randomly** zeroing gradients of positive-advantage tokens performs comparably
  to covariance-targeted clipping.
- Entropy's correlation with performance ranges **−0.894 to +0.627** across
  benchmarks and metrics.
- A representation-space criterion recovers pass@k coverage that entropy-based
  RL loses.

### A confound none of them discusses

DIET proves that in group-normalized RL, multiplying the reward by any
per-problem weight interacts with the normalization so the intended weighting is
**distorted — weakened exactly where outcome variance is highest** — and that
applying the weight to the *advantage* instead fixes it. Several archived methods
reweight rollouts by a per-sample quantity (entropy instability, positive-advantage
reweighting) and none mentions this. It is an implementation-level correctness
issue that could account for part of the small, inconsistent margins this
literature keeps producing.

### The threshold that does double duty

The 80/20 paper sets its high-entropy threshold at **0.672**; **DEER cites that
paper by name and reuses 0.672** to locate inference-time exit points. One
threshold, two jobs — which if not coincidental means "forking token" and
"reasoning transition" are the same event, and the two halves of this archive
study one phenomenon from opposite ends. Untested.

### Definitional care

This is the entropy of the *distribution* at a position, not a property of the
sampled token. "'wait' is a high-entropy token" is shorthand for a statement
about average entropy at positions where that token appears.
