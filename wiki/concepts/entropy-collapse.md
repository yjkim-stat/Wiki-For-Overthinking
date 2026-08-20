# entropy collapse

<!-- auto:begin -->

The failure mode in which a policy's output distribution becomes progressively more deterministic during reinforcement learning, eliminating exploration and saturating performance. At nine sources it has moved from a constraint the methods cite to an object several of them study, and they explain it differently. One attributes it to a covariance between log-probability and probability-weighted advantage that stays positive throughout training. One recasts it as an imbalance of flow, with entropy-decreasing tokens persistently outweighing entropy-increasing ones inside each update. One derives a bifurcation in second-order Renyi entropy at the policy's collision probability, so updating dominant tokens collapses entropy while updating long-tail tokens inflates it. One reduces the direction of change to the sign of a single scalar per token, and to that scalar's deviation from a policy-weighted baseline once a GRPO step is substituted in. A theoretical entry ties the remedies together, proving the classical entropy bonus relocates the optimum while covariance-targeted control is asymptotically unbiased once its coefficient is annealed. Two findings cut against the consensus: one source reports training entropy falling while accuracy improves, and another finds entropy tracks response diversity far more reliably than accuracy.

- **Kind**: concept
- **Also called**: Entropy Collapse
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 15

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [advantage estimation](advantage-estimation.md), [advantage function](advantage-function.md), [AIME](../datasets/aime.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [backtracking](backtracking.md), [calibration](../methods/calibration.md), [causal intervention](causal-intervention.md), [chain of thought](../methods/chain-of-thought.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Clip-Cov](../methods/clip-cov.md), [clip-higher](../methods/clip-higher.md), [Coconut](../methods/coconut.md), [component ablation](../methods/component-ablation.md), [covariance of probability and advantage](covariance-of-probability-and-advantage.md), [coverage](coverage.md), [credit assignment](credit-assignment.md), [DAPO](../methods/dapo.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DAPO-Qwen-32B](../models/dapo-qwen-32b.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [degenerate generation](degenerate-generation.md), [effective sample size](../methods/effective-sample-size.md), [entropy bonus](entropy-bonus.md), [entropy regularization](../methods/entropy-regularization.md), [entropy trajectory](entropy-trajectory.md), [exploration](exploration.md), [exploration-exploitation trade-off](exploration-exploitation-trade-off.md), [Gemini-2.5-pro](../models/gemini-2-5-pro.md), [GPQA](../datasets/gpqa.md), [GPT-2](../models/gpt-2.md), [gpt-5.6-luna](../models/gpt-5-6-luna.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [GSPO](../methods/gspo.md), [HumanEval+](../datasets/humaneval.md), [Humanity's Last Exam](../datasets/humanity-s-last-exam.md), [IFEval](../datasets/ifeval.md), [implicit reasoning](implicit-reasoning.md), [KL-Cov](../methods/kl-cov.md), [KL divergence](kl-divergence.md), [KodCode](../datasets/kodcode.md), [latent chain of thought](../methods/latent-chain-of-thought.md), [latent reasoning](latent-reasoning.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [Llama-3.2-3B-Instruct](../models/llama-3-2-3b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [logit lens](../methods/logit-lens.md), [long chain-of-thought distillation](../methods/long-chain-of-thought-distillation.md), [LoRA](../methods/lora.md), [machine unlearning](machine-unlearning.md), [majority voting](../methods/majority-voting.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MathVision](../datasets/mathvision.md), [MathVista](../datasets/mathvista.md), [Minerva](../datasets/minerva.md), [Mistral-7B](../models/mistral-7b.md), [MMLU-Pro](../datasets/mmlu-pro.md), [MMLU-STEM](../datasets/mmlu-stem.md), [monitorability](monitorability.md), [OlympiadBench](../datasets/olympiadbench.md), [Omni-MATH](../datasets/omni-math.md), [outcome reward](outcome-reward.md), [pass@k](pass-k.md), [performance ceiling](performance-ceiling.md), [policy entropy](policy-entropy.md), [policy gradient](../methods/policy-gradient.md), [policy gradient masking](../methods/policy-gradient-masking.md), [PPO](../methods/ppo.md), [PRIME](../methods/prime.md), [process reward model](process-reward-model.md), [process supervision](process-supervision.md), [ProntoQA](../datasets/prontoqa.md), [ProsQA](../datasets/prosqa.md), [Qwen2.5-0.5B](../models/qwen2-5-0-5b.md), [Qwen2.5-1.5B](../models/qwen2-5-1-5b.md), [Qwen2.5-14B](../models/qwen2-5-14b.md), [Qwen2.5-14B-Instruct](../models/qwen2-5-14b-instruct.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-32B-Instruct](../models/qwen2-5-32b-instruct.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen2.5-VL](../models/qwen2-5-vl.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [Qwen3-1.7B-Base](../models/qwen3-1-7b-base.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [Qwen3-4B-Instruct-2507](../models/qwen3-4b-instruct-2507.md), [Qwen3-8B-Base](../models/qwen3-8b-base.md), [QwQ-32B](../models/qwq-32b.md), [randomized control](randomized-control.md), [reasoning boundary](reasoning-boundary.md), [reasoning distillation](../methods/reasoning-distillation.md), [REINFORCE](../methods/reinforce.md), [reward hacking](reward-hacking.md), [reward shaping](reward-shaping.md), [RLOO](../methods/rloo.md), [RLVR](../methods/rlvr.md), [scaling laws](scaling-laws.md), [self-certainty](../methods/self-certainty.md), [self-consistency](../methods/self-consistency.md), [soft thinking](../methods/soft-thinking.md), [softmax policy](softmax-policy.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [tabular softmax parameterization](tabular-softmax-parameterization.md), [token-level entropy](token-level-entropy.md), [training dynamics](training-dynamics.md), [trajectory diversity](trajectory-diversity.md), [VeRL](../methods/verl.md), [zero-advantage group](zero-advantage-group.md)

## What we have settled

- **Established** — RLVR narrows the set of semantically distinct solution paths a model will produce while widening the set of errors it can recover from; the two effects are separable, both real, and a single pass@k number cannot show either.
  - Measuring a model's preference between two specific verifier-equivalent continuations at a shared branch point, RLVR-trained policies show lower branch entropy than distilled counterparts on 95.5-100% of sampled branches across four model families, and the collapse is significantly stronger in the semantic contrast than in the syntactic one — so the pruning is of inferences, not of phrasing. The same work shows the compensating gain: backtracking probability at dead ends rises from 0.0068 to 0.1537 and from 0.0647 to 0.1687 on two maze models, and recovery from an injected distractor improves by 4.18 to 29.09 points on mathematics. Masking illegal continuations makes the trade explicit — with invalid options removed the flatter distilled policy outperforms the RL one by about 60 percent. This reconciles the archive's standing disagreement rather than picking a side: under plain pass@k the base model overtakes at large k because valid-but-different paths were pruned, while under CoT-Pass@K the RLVR model leads at every k because invalid paths were pruned harder.

## Appears in

- [BODHI: Do LLMs Branch Out and Discover Heterogeneous Inferences?](../../archive/papers/2026/arxiv-2608-02867/summary.md) — Builds prefix trees of semantically equivalent reasoning statements and measures how RLVR changes a model's preference between branches, finding the entropy collapse is not stylistic — the collapse is stronger for semantically distinct continuations than for syntactic variants of the same statement.
- [Don't Peek at the Answer: Outcome-Masked Group Relative Policy Optimization for Label-Free RLVR](../../archive/papers/2026/arxiv-2608-03119/summary.md) — Diagnoses label-free RLVR's collapse as a shortcut in which the same answer-level consensus signal both estimates the reward and receives the gradient, and fixes it by masking the answer span from updates entirely — so a reward can only be raised by improving the reasoning that produces the answer.
- [When Correct Solutions Repeat: Rarity-Aware Credit Redistribution for GRPO](../../archive/papers/2026/arxiv-2608-03467/summary.md) — Shows that GRPO's per-completion uniformity is frequency-skewed once credit is aggregated by solution structure — a recurring correct form accumulates positive coefficient mass proportional to how often it is sampled — and rebalances it by a rarity exponent over a partition built from deterministic cue signatures rather than a judge model.
- [Parameter Exploration for RLVR via Variational Learning](../../archive/papers/2026/arxiv-2608-09805/summary.md) — Explores in weight space rather than token space during RLVR by sampling policies from a variational posterior at rollout time, and introduces a training-time exploration metric -- how often a method produces a correct rollout on a prompt where GRPO produced none -- because entropy and pass@k cannot tell exploration from degeneration.
- [LEMUR: Latent Entropy-aware Multimodal Unlearning via Visual-anchored Reasoning Redirection](../../archive/papers/2026/arxiv-2608-11691/summary.md) — Finds that a fact successfully unlearned from a multimodal model's final answer can still be reproduced in its reasoning trace, far more in natively RL-trained models than in their base versions, and uses the token-level entropy signature RL leaves behind as a training-free control signal for redirecting the trace at decoding time.
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
