# entropy collapse

<!-- auto:begin -->

The failure mode in which a policy's output distribution becomes progressively more deterministic during reinforcement learning, eliminating exploration and saturating performance. At nine sources it has moved from a constraint the methods cite to an object several of them study, and they explain it differently. One attributes it to a covariance between log-probability and probability-weighted advantage that stays positive throughout training. One recasts it as an imbalance of flow, with entropy-decreasing tokens persistently outweighing entropy-increasing ones inside each update. One derives a bifurcation in second-order Renyi entropy at the policy's collision probability, so updating dominant tokens collapses entropy while updating long-tail tokens inflates it. One reduces the direction of change to the sign of a single scalar per token, and to that scalar's deviation from a policy-weighted baseline once a GRPO step is substituted in. A theoretical entry ties the remedies together, proving the classical entropy bonus relocates the optimum while covariance-targeted control is asymptotically unbiased once its coefficient is annealed. Two findings cut against the consensus: one source reports training entropy falling while accuracy improves, and another finds entropy tracks response diversity far more reliably than accuracy.

- **Kind**: concept
- **Also called**: Entropy Collapse
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 10

**Related**: [advantage function](advantage-function.md), [AIME 2024](../datasets/aime-2024.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [calibration](../methods/calibration.md), [causal intervention](../methods/causal-intervention.md), [chain of thought](../methods/chain-of-thought.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Clip-Cov](../methods/clip-cov.md), [clip-higher](../methods/clip-higher.md), [Coconut](../methods/coconut.md), [covariance of probability and advantage](covariance-of-probability-and-advantage.md), [DAPO](../methods/dapo.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [entropy bonus](entropy-bonus.md), [entropy regularization](../methods/entropy-regularization.md), [entropy trajectory](entropy-trajectory.md), [exploration-exploitation trade-off](exploration-exploitation-trade-off.md), [GPQA](../datasets/gpqa.md), [GPT-2](../models/gpt-2.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [HumanEval](../datasets/humaneval.md), [implicit reasoning](implicit-reasoning.md), [KL-Cov](../methods/kl-cov.md), [KodCode](../datasets/kodcode.md), [latent chain of thought](../methods/latent-chain-of-thought.md), [latent reasoning](latent-reasoning.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [Logit Lens](../methods/logit-lens.md), [majority voting](../methods/majority-voting.md), [MATH](../datasets/math.md), [MATH-500](../datasets/math-500.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [Mistral-7B](../models/mistral-7b.md), [OlympiadBench](../datasets/olympiadbench.md), [OMNI-MATH](../datasets/omni-math.md), [pass-k](../methods/pass-k.md), [performance ceiling](performance-ceiling.md), [policy entropy](policy-entropy.md), [policy gradient](../methods/policy-gradient.md), [policy gradient masking](../methods/policy-gradient-masking.md), [PPO](../methods/ppo.md), [PRIME](../methods/prime.md), [process supervision](process-supervision.md), [ProntoQA](../datasets/prontoqa.md), [ProsQA](../datasets/prosqa.md), [Qwen2.5-0.5B](../models/qwen2-5-0-5b.md), [Qwen2.5-1.5B](../models/qwen2-5-1-5b.md), [Qwen2.5-14B](../models/qwen2-5-14b.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [QwQ-32B](../models/qwq-32b.md), [reasoning boundary](reasoning-boundary.md), [reasoning distillation](../methods/reasoning-distillation.md), [REINFORCE++](../methods/reinforce.md), [RLOO](../methods/rloo.md), [RLVR](../methods/rlvr.md), [scaling laws](scaling-laws.md), [self-certainty](../methods/self-certainty.md), [self-consistency](../methods/self-consistency.md), [softmax policy](softmax-policy.md), [tabular softmax parameterization](tabular-softmax-parameterization.md), [token-level entropy](token-level-entropy.md), [VeRL](../methods/verl.md)

## Appears in

- [SeLaR: Selective Latent Reasoning in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-320/summary.md) — Switches to soft-embedding latent reasoning only at low-confidence steps, keeping discrete decoding elsewhere, and pushes the soft embeddings away from the top token to stop them collapsing.
- [The Illusion of Superposition? A Principled Analysis of Latent Thinking in Language Models](../../archive/papers/2026/local-043e84b0b0ae0a39/summary.md) — Tests the claim that continuous chain-of-thought lets a model hold several candidate solutions at once, and finds it holds only for models trained from scratch: off-the-shelf models collapse a superposed input to a single token within a few layers, and fine-tuned latent reasoners solve the task in one forward pass and copy the answer through the latent slots.
- [Beyond Entropy: Learning from Token-Level Distributional Deviations for LLM Reasoning](../../archive/papers/2026/local-2175408b166d313f/summary.md) — Argues that Shannon entropy is the wrong criterion for picking which tokens to train on in RLVR, and selects tokens instead by the Jensen-Shannon divergence of their logit distribution from the group average, updating only the top 10% of these 'unique' tokens.
- [The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models](../../archive/papers/2025/local-5175928072823010/summary.md) — Establishes that RL trades policy entropy for reward along a predictable exponential curve R = -a·exp(H) + b, derives that entropy change is driven by the covariance between action probability and advantage, and controls it by restricting updates to the highest-covariance tokens.
- [On the Entropy Dynamics in Reinforcement Fine-Tuning of Large Language Models](../../archive/papers/2026/local-837612b527cb427c/summary.md) — Reduces the question of whether an update raises or lowers entropy to the sign of one scalar per token, shows that under GRPO what matters is that scalar's deviation from a policy-weighted baseline rather than its own value, and proves the deviation averages to zero over a batch.
- [Understanding and Preventing Entropy Collapse in RLVR with On-Policy Entropy Flow Optimization](../../archive/papers/2026/local-8efebbee3585a141/summary.md) — Recasts entropy collapse as an imbalance of 'entropy flow' — tokens whose update lowers entropy persistently outweigh those that raise it — and rebalances the two sets with a closed-form coefficient computed from each batch, without reference policies or entropy bonuses.
- [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](../../archive/papers/2025/local-b050d2841cbb4959/summary.md) — Measures RLVR-trained models against their base models with pass@k at large k and finds the base wins, concluding RLVR sharpens sampling toward paths the base already had rather than adding new ones.
- [Revisiting Entropy in Reinforcement Learning for Large Reasoning Models](../../archive/papers/2026/local-c70c8f6b2ab7db16/summary.md) — A systematic empirical study of entropy in RLVR that finds entropy correlates with response diversity but only weakly and inconsistently with accuracy, identifies clipping thresholds, off-policy updates and data diversity as its drivers, and argues positive-advantage tokens are what collapses it.
- [EDIS: Diagnosing LLM Reasoning via Entropy Dynamics](../../archive/papers/2026/local-e64d3a8c4788daf7/summary.md) — Introduces EDIS, a trajectory-level score that measures how unstably token entropy evolves during generation, and uses it to select better reasoning rollouts at inference and to curate training samples in RL.
- [A Comparative Theoretical Analysis of Entropy Control Methods in Reinforcement Learning for Reasoning Language Models](../../archive/papers/2026/local-ed740509686ff305/summary.md) — Proves that an entropy bonus permanently moves the stationary point of RL training while covariance-targeted control reaches the unregularized optimum once its coefficient is annealed, and that the bonus shrinks the stability margin where the targeted methods leave it intact.

<!-- auto:end -->

## Notes

### Collapse is not the same as low entropy

Worth stating because the term invites the confusion. One archived paper reports
its entropy-informed training driving training entropy **down** (0.07-0.09 versus
0.16-0.18 for baseline) while accuracy goes **up**. Low entropy is not the
pathology. The pathology is entropy falling for the wrong reason — determinism
arriving before the policy has explored — and the two are indistinguishable from
the entropy value alone.

### The claim that entropy is a currency, and the case against

The strongest formulation in the archive is the exchange law
`R = -a·exp(H) + b`, fitted over 200+ points, algorithm-irrelevant across GRPO,
RLOO, PRIME and REINFORCE++, and predictive to within ~1% RMSE from the first 36
training steps. If true, RL compute has a knowable ceiling at `H = 0` and every
algorithmic improvement is rearranging the path to a fixed endpoint. That is the
most consequential claim in this topic.

**It does not survive unchallenged.** A later paper holds entropy at its
pre-training level with adaptive regularization and reports AIME24 accuracy
*rising above* the unregularized run — performance not traded from entropy — and
measures entropy-performance correlations that flip sign across benchmarks. The
two are not trivially reconcilable. Possibilities worth separating before
accepting either: the exchange law may hold within a run but not across
interventions that change the entropy trajectory itself; or the fitted `b` may
move when the training regime changes, making the "ceiling" conditional on the
recipe rather than on the model.

### Mechanisms on offer

Three, in increasing order of directness:

1. **Covariance.** Entropy change ≈ −Cov(log π, Δlogit), which under policy
   gradient is proportional to advantage. Covariance stays positive throughout
   training, hence monotone decrease. First-order, tabular-softmax.
2. **Entropy flow imbalance.** Partition tokens by the sign of their entropy
   change; collapse is persistent dominance of the decreasing set. Agnostic
   about *why* — measures the change rather than what drives it.
3. **Positive advantage.** Differentiating the GRPO objective w.r.t. a logit:
   positive advantage raises sampled (already-likely) tokens and suppresses
   unsampled ones, concentrating mass. Verified by training on advantage-sign
   subsets — non-negative only gives the most severe collapse, non-positive only
   gives entropy 0.884 against ~0.015 baseline.

Mechanism 3 subsumes much of 1 and is easier to check. See
[[token-level-entropy]] for why the four selection criteria in this archive may
be one criterion.

### Something nobody here has done

Entropy collapse coincides with **miscalibration**: after GRPO the model raises
probabilities of correct *and* incorrect responses and the gap between them
narrows, with miscalibration severity ordered the same way as collapse severity.
Meanwhile, step-level probing elsewhere in this archive shows step correctness is
linearly decodable from internal representations at 78-86%. Nobody has asked
whether RLVR degrades that probe. If entropy control preserves calibration, it
should also preserve the internal correctness signal — a measurable prediction
linking this topic to [[chain-of-thought-faithfulness]].
