# token-level entropy

<!-- auto:begin -->

The Shannon entropy of the model's next-token distribution at one generation step, computed over the whole vocabulary. All the sources stress it is a property of the distribution at a position, not of the token sampled there — the same token at two positions can carry different entropy. They disagree about how much it explains. Several treat it as the signal that matters: roughly 20% of chain-of-thought tokens are high-entropy and act as forks steering the reasoning path, a trajectory-level instability score built on it selects better rollouts, and step confidence decides whether to switch to latent reasoning or to stop generating. Others argue it is the wrong criterion. One notes distributions with identical entropy can have very different shapes and selects tokens instead by the divergence of their logit distribution from the group average, reporting that the tokens chosen that way split roughly evenly between the high- and low-entropy populations. Another shows that under a GRPO update the governing quantity is not a token's entropy but the deviation of a per-token discriminator from its policy-weighted expectation — so a criterion measured absolutely and one measured against a baseline pick different tokens from the same distribution.

- **Kind**: concept
- **Also called**: generation entropy, token entropy
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 7

**Related**: [advantage function](advantage-function.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [BigCodeBench](../datasets/bigcodebench.md), [chain of thought](chain-of-thought.md), [Clip-Cov](../methods/clip-cov.md), [clip-higher](../methods/clip-higher.md), [covariance of probability and advantage](covariance-of-probability-and-advantage.md), [credit assignment](credit-assignment.md), [DAPO](../methods/dapo.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER](../methods/deer.md), [Dynasor](../methods/dynasor.md), [early exit](../methods/early-exit.md), [entropy bonus](entropy-bonus.md), [entropy collapse](entropy-collapse.md), [entropy regularization](../methods/entropy-regularization.md), [entropy trajectory](entropy-trajectory.md), [exploration-exploitation trade-off](exploration-exploitation-trade-off.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [GSPO](../methods/gspo.md), [HumanEval+](../datasets/humaneval.md), [implicit reasoning](implicit-reasoning.md), [Jensen-Shannon divergence](../methods/jensen-shannon-divergence.md), [KL-Cov](../methods/kl-cov.md), [KodCode](../datasets/kodcode.md), [latent chain of thought](latent-chain-of-thought.md), [latent reasoning](latent-reasoning.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [majority voting](../methods/majority-voting.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [Mistral-7B](../models/mistral-7b.md), [MMLU-STEM](../datasets/mmlu-stem.md), [OlympiadBench](../datasets/olympiadbench.md), [Omni-MATH](../datasets/omni-math.md), [overthinking](overthinking.md), [pass@k](pass-k.md), [performance ceiling](performance-ceiling.md), [policy entropy](policy-entropy.md), [policy gradient masking](../methods/policy-gradient-masking.md), [PPO](../methods/ppo.md), [PRIME](../methods/prime.md), [process supervision](process-supervision.md), [Qwen2.5-0.5B](../models/qwen2-5-0-5b.md), [Qwen2.5-1.5B](../models/qwen2-5-1-5b.md), [Qwen2.5-14B-Instruct](../models/qwen2-5-14b-instruct.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [Qwen3-4B-Instruct-2507](../models/qwen3-4b-instruct-2507.md), [Qwen3-8B](../models/qwen3-8b.md), [QwQ-32B](../models/qwq-32b.md), [reasoning redundancy](reasoning-redundancy.md), [REINFORCE](../methods/reinforce.md), [RLOO](../methods/rloo.md), [RLVR](../methods/rlvr.md), [scaling laws](scaling-laws.md), [self-certainty](../methods/self-certainty.md), [self-consistency](../methods/self-consistency.md), [softmax policy](softmax-policy.md), [test-time compute](test-time-compute.md), [training dynamics](training-dynamics.md), [VeRL](../methods/verl.md), [vLLM](../methods/vllm.md)

## What we have settled

- **Established** — A generation-time signal read against an absolute threshold does not transfer between models or tasks; the same signal read relative to its own running distribution or to a group baseline does — and for the stopping decision the absolute version is provably able to be arbitrarily far from optimal.
  - Six sources test this and none dissents. Hidden-state norm: replacing the adaptive interquartile detector with a fixed threshold collapses AIME24 from 70.00 to 23.33 for recursion and 66.67 to 16.67 for steering, and the paper states the reason plainly — a high norm on GSM8K is a low norm on GPQA. Predictive entropy: CUSUM's two regime densities are re-estimated per model from 100 calibration trajectories, so nothing about the cut-point is portable. Entropy trajectory: EDIS's window size, rebound threshold and spike weighting must be recalibrated per model family because entropy dynamics depend on vocabulary size and training distribution. Token selection: replacing an absolute entropy threshold with the Jensen-Shannon divergence of a token's logit distribution from the group average changes the selected set outright, with the chosen tokens splitting roughly evenly between the high- and low-entropy populations (ratio 1.03 on GSM8K, 0.99 on MATH). Policy updates: under GRPO the governing quantity is not a token's entropy but the deviation of a per-token discriminator from its policy-weighted expectation, which is the same absolute-versus-relative substitution one level down. And the negative result is a theorem rather than a measurement: for a fixed cost coefficient and any constant K there is a finite-horizon stopping problem where the optimal policy's value exceeds K times that of the best fixed-threshold policy, even when the probability that the prefix is already correct is known exactly — because the quantity that decides is the value of continuing, not the value of stopping. The practical reading is that the open problem in this cluster is not which signal to measure but what to measure it against.
- **Established** — A small set of reflective transition tokens does disproportionate work in a reasoning trace, and the asymmetry holds on three quantities measured independently of one another — mutual information with the answer, the change in the answer's own log-probability, and what removing them costs.
  - Three papers, three different instruments, one ordering. Mutual information between a step's representation and the correct answer spikes at only 0.51-4.80% of steps depending on model, with gaps of 28-87 steps between peaks, and those peaks decode to discourse markers of reflection and transition; suppressing up to 17 such tokens drops accuracy from about 85% to 68% on GSM8K, 78% to 48% on MATH500 and 33% to 18% on AIME24, while suppressing the same number of randomly chosen non-thinking tokens leaves accuracy essentially flat -- the matched random control this archive demands elsewhere, and it passes. Reading the trajectory as an optimization, the same tokens move the objective by orders of magnitude more than an average one: log-scale changes in the answer's negative log-probability of 279.50 for 'Hold on' and 16.33 for 'Alternatively' against 0.96 averaged over all tokens and 0.76 for 'Therefore'. And the third comes from the other direction: injecting a bare doubt cue into a failed trajectory recovers about 15% of incorrect rollouts without naming what went wrong, while self-distillation on 800 of a model's own correct traces generated under an instruction not to express uncertainty cuts AIME24 pass@1 from 80.0 to 43.3. The accounts differ -- information peaks, saddle-point escape, epistemic verbalization -- and none is established over the others.

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

### Entropy has now been raced against another endogenous signal, and lost

Every comparison above is between token-selection criteria. The archive now
holds one comparison against a signal from a different layer of the model
altogether, and it is not close.

The Tell-Tale Norm work identifies reasoning features with per-layer sparse
autoencoders and correlates candidate signals against their activation.
Layer-wise L2 norm of the hidden state scores Spearman **86.47, 85.15, 87.62
and 84.11** across four models; final output entropy scores **63.52 down to
52.10**; three other intrinsic statistics correlate *negatively*, from −19.94
to −72.15. Both signals are free at inference and neither needs a label.

The reading that fits the rest of this note is structural rather than about
quality. Entropy is computed from the output distribution — the last thing the
model produces before a token is drawn, after everything has been projected
onto the vocabulary. The norm is read before that projection. On this evidence
the vocabulary projection is where the information is lost, which is a
different objection from the one ICT raises (that a scalar cannot distinguish
distributions of the same entropy but different shape) and compatible with it.

Two caveats keep this from being a verdict. The SAE reasoning features are
*defined* as whatever differs between thinking and non-thinking responses on
one dataset, so what is being correlated against is that contrast rather than
reasoning as such. And the two signals have never been compared on the task
this note cares about — which tokens to update, or where to stop — only on
agreement with the SAE contrast.

### The axis nobody in this cluster names: absolute against relative

`finding:e2e90a383e6902f1` collects the pattern. Setting it beside the table
above makes something visible that reads as six unrelated caveats otherwise:
**every criterion in this literature that was reported to work is relative, and
every one reported to fail is absolute.**

- The 80/20 threshold is recomputed **per batch**, not fixed — the paper is
  explicit, and its `rho = 0.2` selects a quantile rather than a value.
- ICT's whole move is replacing an absolute entropy cut with divergence from
  the **group** average.
- The covariance criterion is a deviation from a policy-weighted expectation,
  which is the same substitution one level down.
- On the inference side, the norm work's adaptive interquartile detector is
  load-bearing to the point of absurdity: a fixed threshold takes AIME24 from
  **70.00 to 23.33**.

Which puts the note's own observation about 0.672 in a harsher light. The 80/20
paper uses that number as a *per-batch quantile*; DEER reuses it as a **fixed
constant** across eleven models from 1.5B to 671B. Those are not the same
object, and the coincidence this note flagged as possibly meaningful may be an
artefact of one paper freezing another's quantile into a literal. Testing that
costs one ablation: recompute DEER's transition threshold per trajectory and
see whether the exit points move.
