# policy entropy

<!-- auto:begin -->

The token-level average entropy of the policy, and the quantity the RLVR sources here treat as the resource that exploration spends. They disagree about how tightly it binds performance. One establishes an exponential exchange law R = -a*exp(H) + b — fitted over 200-plus data points rather than derived — which makes a performance ceiling predictable at zero entropy. One measures Spearman correlations between entropy and benchmark performance ranging from -0.894 to +0.627 depending on task and metric, and shows accuracy improving while entropy is held at its pre-training level, which is hard to reconcile with a strict trade. One reframes it as a flow rather than a level, arguing what matters is the balance of entropy-increasing against entropy-decreasing updates. One argues the level is the wrong object entirely: under a GRPO step the driver is a per-token discriminator's deviation from a policy-weighted baseline, and that deviation averages to zero over a batch. A theoretical entry supplies the account the classical remedy lacked, proving an entropy bonus does not merely need tuning but relocates the optimum, while covariance-targeted control reaches the unregularized one if its coefficient is annealed. What no source yet does is separate entropy being the controlled quantity from entropy being a statistic that moves when something else is controlled.

- **Kind**: concept
- **Also called**: model entropy
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 8

**Related**: [advantage estimation](advantage-estimation.md), [advantage function](advantage-function.md), [AIME](../datasets/aime.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [backtracking](backtracking.md), [best-of-n](../methods/best-of-n.md), [calibration](../methods/calibration.md), [Clip-Cov](../methods/clip-cov.md), [clip-higher](../methods/clip-higher.md), [covariance of probability and advantage](covariance-of-probability-and-advantage.md), [DAPO](../methods/dapo.md), [DAPO-Math-17k](../datasets/dapo-math-17k.md), [data efficiency](data-efficiency.md), [entropy bonus](entropy-bonus.md), [entropy collapse](entropy-collapse.md), [entropy regularization](../methods/entropy-regularization.md), [exploration](exploration.md), [exploration-exploitation trade-off](exploration-exploitation-trade-off.md), [Game of 24](../datasets/game-of-24.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [KL-Cov](../methods/kl-cov.md), [KodCode](../datasets/kodcode.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH](../datasets/math.md), [MATH-500](../datasets/math-500.md), [MATH500](../datasets/math500.md), [MBPP+](../datasets/mbpp.md), [Minerva](../datasets/minerva.md), [Mistral-7B](../models/mistral-7b.md), [OlympiadBench](../datasets/olympiadbench.md), [Omni-MATH](../datasets/omni-math.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [pass@k](../methods/pass-k.md), [performance ceiling](performance-ceiling.md), [Phi-4](../models/phi-4.md), [policy gradient](../methods/policy-gradient.md), [policy gradient masking](../methods/policy-gradient-masking.md), [post-hoc rationalization](post-hoc-rationalization.md), [PPO](../methods/ppo.md), [PRIME](../methods/prime.md), [privileged information](privileged-information.md), [prompt difficulty](prompt-difficulty.md), [Qwen2.5-14B-Instruct](../models/qwen2-5-14b-instruct.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-1.7B-Base](../models/qwen3-1-7b-base.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [Qwen3-8B-Base](../models/qwen3-8b-base.md), [reasoning boundary](reasoning-boundary.md), [REINFORCE](../methods/reinforce.md), [reward sparsity](reward-sparsity.md), [RLOO](../methods/rloo.md), [RLVR](../methods/rlvr.md), [scaling laws](scaling-laws.md), [softmax policy](softmax-policy.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [tabular softmax parameterization](tabular-softmax-parameterization.md), [token-level entropy](token-level-entropy.md), [VeRL](../methods/verl.md)

## What we have settled

- **Established** — RLVR narrows the set of semantically distinct solution paths a model will produce while widening the set of errors it can recover from; the two effects are separable, both real, and a single pass@k number cannot show either.
  - Measuring a model's preference between two specific verifier-equivalent continuations at a shared branch point, RLVR-trained policies show lower branch entropy than distilled counterparts on 95.5-100% of sampled branches across four model families, and the collapse is significantly stronger in the semantic contrast than in the syntactic one — so the pruning is of inferences, not of phrasing. The same work shows the compensating gain: backtracking probability at dead ends rises from 0.0068 to 0.1537 and from 0.0647 to 0.1687 on two maze models, and recovery from an injected distractor improves by 4.18 to 29.09 points on mathematics. Masking illegal continuations makes the trade explicit — with invalid options removed the flatter distilled policy outperforms the RL one by about 60 percent. This reconciles the archive's standing disagreement rather than picking a side: under plain pass@k the base model overtakes at large k because valid-but-different paths were pruned, while under CoT-Pass@K the RLVR model leads at every k because invalid paths were pruned harder.

## Appears in

- [Self-Improving Large Language Models via Progressive Experience Evolution](../../archive/papers/2026/arxiv-2608-02139/summary.md) — Inserts a stage before RL in which the model extracts textual lessons from its own successful and failed rollouts, filters them by measured marginal utility on a held-out probe set, and distills the surviving pool into its own weights — so that GRPO starts from a policy that fails all-eight-samples less often.
- [BODHI: Do LLMs Branch Out and Discover Heterogeneous Inferences?](../../archive/papers/2026/arxiv-2608-02867/summary.md) — Builds prefix trees of semantically equivalent reasoning statements and measures how RLVR changes a model's preference between branches, finding the entropy collapse is not stylistic — the collapse is stronger for semantically distinct continuations than for syntactic variants of the same statement.
- [Representation-Based Exploration for Language Models: From Test-Time to Post-Training](../../archive/papers/2026/local-1fadd9f07b138261/summary.md) — Uses elliptical bonuses over a language model's own hidden-state representations as a diversity signal, validates it in a clean inference-time selection setting, then transfers the same signal into RL post-training — where it eliminates the diversity collapse that degrades pass@k at large k.
- [The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models](../../archive/papers/2025/local-5175928072823010/summary.md) — Establishes that RL trades policy entropy for reward along a predictable exponential curve R = -a·exp(H) + b, derives that entropy change is driven by the covariance between action probability and advantage, and controls it by restricting updates to the highest-covariance tokens.
- [On the Entropy Dynamics in Reinforcement Fine-Tuning of Large Language Models](../../archive/papers/2026/local-837612b527cb427c/summary.md) — Reduces the question of whether an update raises or lowers entropy to the sign of one scalar per token, shows that under GRPO what matters is that scalar's deviation from a policy-weighted baseline rather than its own value, and proves the deviation averages to zero over a batch.
- [Understanding and Preventing Entropy Collapse in RLVR with On-Policy Entropy Flow Optimization](../../archive/papers/2026/local-8efebbee3585a141/summary.md) — Recasts entropy collapse as an imbalance of 'entropy flow' — tokens whose update lowers entropy persistently outweigh those that raise it — and rebalances the two sets with a closed-form coefficient computed from each batch, without reference policies or entropy bonuses.
- [Revisiting Entropy in Reinforcement Learning for Large Reasoning Models](../../archive/papers/2026/local-c70c8f6b2ab7db16/summary.md) — A systematic empirical study of entropy in RLVR that finds entropy correlates with response diversity but only weakly and inconsistently with accuracy, identifies clipping thresholds, off-policy updates and data diversity as its drivers, and argues positive-advantage tokens are what collapses it.
- [A Comparative Theoretical Analysis of Entropy Control Methods in Reinforcement Learning for Reasoning Language Models](../../archive/papers/2026/local-ed740509686ff305/summary.md) — Proves that an entropy bonus permanently moves the stationary point of RL training while covariance-targeted control reaches the unregularized optimum once its coefficient is annealed, and that the bonus shrinks the stability margin where the targeted methods leave it intact.

<!-- auto:end -->

## Notes

### The seam is closed

This note previously recorded that the archive stated the same trade-off twice —
policy entropy during RL training, decisional certainty during inference — with
**no paper connecting them**. Two now do, from opposite directions.

**Inference → training.** *Representation-Based Exploration* validates a
diversity bonus in a clean inference-time selection problem (no optimization or
generalization confound), then installs the same signal as an RL reward bonus.
Its organizing hypothesis is exactly the seam: *a diversity bonus that works at
inference works in post-training*. Its bonus is a fifth answer to this archive's
"which quantity should the intervention target" dispute, and the first that is a
property of the response's **semantic content** rather than of the output
distribution:

| Criterion | What it measures |
| --- | --- |
| entropy / divergence / covariance / advantage sign | the output distribution at a position |
| **elliptical bonus on hidden states** | how much a response's representation adds to the span of those already chosen |

**Training → inference.** *MRT* inverts the direction: rather than engineering
inference around a fixed model, it changes the training objective so the model's
own token stream is efficient. Test-time compute becomes a meta-RL problem, one
output stream is a sequence of episodes, and efficacy is **cumulative regret
over output tokens** — the area between an oracle's success-versus-budget curve
and the model's. State-of-the-art models do not minimize it.

### Why this matters more than another 2-point gain

RepExp eliminates **diversity collapse** — the phenomenon where RL improves
pass@k at small k while degrading it at large k relative to the base model. That
is a direct counter-case to the archive's entropy-exchange law, which claims
performance is traded from entropy along a predictable curve toward a fixed
ceiling. Here coverage the base model had, and entropy-based RL loses, is
recovered by a **non-entropy** mechanism. Either the exchange law is conditional
on the training recipe rather than on the model, or exploration and entropy are
less tightly coupled than the law implies. The archive cannot yet say which.

MRT's regret framing also subsumes several things this archive tracks
separately: overthinking becomes regret incurred after the answer is settled,
and the failure of outcome-only supervision gets a second explanation alongside
the complexity-theoretic one — a 0/1 signal cannot distinguish a segment that
earned its tokens from one that did not.

### Both are conditional, in the same direction

RepExp's benefit **grows with model strength and with question difficulty**:
the weakest models are degraded, not merely unhelped, and the largest gains fall
on the hardest question bins (3x on the hardest Game-of-24 problems). That is
the mirror image of the archive's adaptive-allocation result, where the PRM
signal driving allocation *degrades* exactly where compute is most needed. Two
difficulty-conditional methods, opposite conditional behaviour — worth
resolving, since it decides whether difficulty is a knob one can act on.

One caution travels with the diversity framing: RepExp beats nucleus, min-p and
low-temperature sampling but **not** high-temperature sampling, diagnosed as
high temperature manufacturing novelty in representation space without
correctness. Diversity is not usefulness.

### Is entropy the mechanism, or the language we describe it in?

The section above leaves a question open — whether the exchange law is
conditional on the training recipe, or whether exploration and entropy are less
tightly coupled than the law implies. Three results already in the archive push
toward the second horn. None of the three papers draws that conclusion, because
each holds only its own piece.

**A random control matches the targeted one.** *Revisiting Entropy* runs
Rand-Pos-Clip, which zeroes the gradients of a **randomly chosen** subset of
positive-advantage tokens, and reports it performing comparably to Clip-Cov,
which selects tokens by covariance. If random selection matches covariance
selection, what does the work may be the reduction in effective gradient on
positive-advantage tokens rather than the criterion that picks them. The paper
reports this without dwelling on it.

**The entropy criterion does not select what it is taken to select.** *Beyond
Entropy* measures where its distributionally-unique tokens come from and finds
them drawn about equally from the high- and low-entropy populations — ratio 1.03
on GSM8K, 0.99 on MATH. Scalar entropy at a position and distributional
deviation from the group are close to independent, so the two criteria pick
different sets while both improve results.

**The mechanism's own share is small.** In *OPEFO* the larger part of the gain
over standard GRPO comes from switching to strict on-policy training — a
separate change — with entropy-flow balancing contributing 2.3 and 1.8 points.

Together these do not show the entropy account is wrong. They show the archive's
evidence does not cleanly separate *entropy is the quantity being controlled*
from *entropy is a summary statistic that moves when something else is
controlled*, and the Spearman range recorded above, -0.894 to +0.627, is what
one would expect of a correlate.

**Revised at six sources.** Two entries added since this was written push the
other way, so the question is now two-sided rather than open by default. *On the
Entropy Dynamics in RFT* runs close to the experiment the paragraph above says
nobody had run: it predicts the sign of the entropy change from one scalar per
token, then separately retains and masks gradients by that sign on positive and
on negative samples, and obtains all four predicted outcomes. That is
interventional evidence for a mechanism rather than a correlate, at the level of
a single step. *A Comparative Theoretical Analysis* independently supplies the
explanation this archive lacked for its own repeated finding that the entropy
bonus disappoints — a proof that the bonus moves the stationary point, so the
loss is structural rather than a tuning failure. What none of the six supplies
is the discriminating experiment: vary the selection criterion while holding the
reduction in effective gradient fixed. Until that is run, the random control
matching a covariance-targeted one stays unexplained.

### The theorems are local; the claims are global

Every *entropy* derivation in this cluster is a **one-step first-order expansion
under a tabular-softmax assumption**: Lemma 1 and Theorem 1 of the exchange-law
paper, OPEFO's entropy-flow sign decomposition, *Beyond Entropy*'s second-order
Rényi bifurcation, *Revisiting Entropy*'s logit derivative, and — added since —
the entropy-discriminator identity and the unified framework of the two 2026
theory entries. Six sources, one technique. Each says which way a single update
pushes entropy.

One partial exception has arrived and is worth naming precisely. *A Comparative
Theoretical Analysis* also proves asymptotic convergence results — O(1/T) to a
stationary point, of the regularized objective for the entropy bonus and of the
original objective for annealed covariance control. Those are statements about
where training ends up, not about one step, so the local-to-global gap is
genuinely bridged there. It is bridged for the *optimum*, however, and not for
the entropy trajectory: nothing yet derives the shape of the entropy curve over
training, and the exponential law remains what it always was.

The claims are about trajectories — monotone collapse over hundreds of steps,
73% of entropy consumed in the first 200, and a ceiling at H = 0. Note what the
exchange law is and is not: it is an **empirical law fitted with two
coefficients over 200+ data points**, listed separately from the covariance
theorem. The covariance result explains why entropy falls monotonically; it does
**not** derive the exponential form. What joins the one-step theorem to the
trajectory claim is curve fitting, and the most-cited consequence — a
predictable ceiling at H = 0 — rests on the fitted half.

### Why this thread cannot meet the archive's theory papers

This section was written when the two literatures were disjoint: no archived
paper declared entities from both vocabularies, and `reasoning boundary` and
`expressivity` were unlinked in the wiki graph. **That is no longer strictly
true, and the way it stopped being true is the interesting part.** One paper now
carries terms from both sides — but the term it shares is `tabular softmax
parameterization`, which is the *name of the gap* rather than a crossing of it.
The structural account below therefore stands, with one genuine amendment
recorded at the end.

The theory papers idealize the **architecture** — hard attention, saturated
attention, C-RASP, no layer normalization, fixed positional encodings — and
specify the task exactly. This cluster idealizes the **policy**, assuming a
tabular softmax, and keeps the architecture real. "Tabular" means every action
carries its own free parameter, that is, **no function approximation** — which
is the whole object of the expressivity results. Each side's idealization
deletes the other side's subject matter.

One consequence is worth stating because it is actionable. `reasoning boundary`
is defined as the set of problems solvable given unlimited attempts, which is a
reachability question, and the theory papers have apparatus for exactly that —
CoT(t(n)) is a characterization of a reachable set. Yet the dispute is settled
empirically with pass@k at k up to 1024, and the decisive evidence on one side,
that RLVR-generated paths lie inside the base model's distribution by
perplexity, is a support argument that is never formalized. *Does RLVR move the
policy outside the base model's reachable set, or redistribute mass within it?*
is askable in the theory papers' language and has not been asked.

**The amendment.** Two convergence entries added since do move past the tabular
assumption, which the paragraph above treats as the blocker. *Global linear
convergence beyond tabular MDPs* analyses entropy-regularized policy gradient
under log-linear policies with linear function approximation, so entropy and
function approximation now appear together in one archived result for the first
time. *Rethinking the Global Convergence of Softmax PG* does the same without
the entropy term and adds the sharper finding that approximation error cannot
characterize convergence at all — what decides it is whether the feature
geometry preserves the ordering of rewards. So the gap has narrowed from
"nothing addresses this" to "the addressing stops one class short": a log-linear
policy over fixed features is not a transformer, both results are for idealized
optimization with exact gradients, and neither treats a language model. The
junction that is still empty is specific and can now be named — the entropy
dynamics of a policy whose parameters are *shared across states*.

### Revised at seven sources: the quantity entropy is standing in for

The seventh entry does not argue about entropy at all, which is why it is
useful. *SPEE* inserts an experience-distillation stage **before** RL and
measures its effect on a quantity this thread has been circling without naming:
**the fraction of prompts whose rollout group contains any reward variation.**
When all eight sampled responses to a problem are wrong they share a reward, the
group-relative advantage is identically zero, and the update carries no gradient
for that prompt. Stage I cuts that all-incorrect share by 4.95 points at 4B and
2.75 at 8B.

Two things make this bear on the open question above.

**It is a direct measure where entropy is a summary.** Two policies can hold the
same token-level average entropy and differ in how many prompts produce a usable
group — entropy is computed per position over the vocabulary, the all-incorrect
rate is computed per prompt over outcomes. The second is what actually gates
whether a gradient exists. That reframes the note's dichotomy: the choice is not
only *mechanism versus correlate* but **correlate of what**, and here the
downstream quantity is cheap to measure and nobody in the cluster reports it.

**Entropy appears as a control, not a target.** SPEE reports 0.047 after its
pre-stage against GRPO's 0.029 — used to rule out the cheap explanation that the
better initialization came from collapsing diversity. This is the correct use of
the statistic and it is the third non-entropy mechanism in this note to improve
exploration: RepExp's elliptical bonus on hidden states, MRT's regret objective,
and now a textual experience pool distilled into the weights. Its ablation is
the sharpest form of the point — removing the experience pool costs more than
removing the reinforcement-learning stage entirely (34.13 against 35.16, full
36.67), so most of what the method achieves happens before any entropy is spent.

**What it does not settle.** SPEE's margin over GRPO is 0.75 to 1.92 average
points with no seeds, so nothing here rests on the headline. And it does not run
the discriminating experiment this note has now asked for twice — vary the
selection criterion while holding the reduction in effective gradient fixed. It
does supply a **second** experiment worth running and cheaper than that one:
report the all-incorrect group rate alongside entropy in any paper claiming an
entropy intervention improved exploration. If the two move together the
distinction collapses; if they come apart, the exchange law is a law about the
wrong variable.

### Revised at eight sources: the collapse is semantic, and it was testable

The section above closes by saying the archive cannot separate *entropy is the
controlled quantity* from *entropy is a statistic that moves when something else
is controlled*, and that the discriminating experiment has not been run. An
eighth entry runs a different discriminating experiment, and it settles the half
of the question that was actually answerable.

**The question it answers.** A policy can lose entropy by calcifying stylistic
choices — variable names, the order of commutative operations, phrasing — which
would make the collapse real and uninteresting. *BODHI* builds prefix trees in
which nodes are sets of semantically equivalent reasoning statements, so two
continuations from the same child differ only in syntax while one from a sibling
child differs in inference, and applies the same preference-entropy measure to
both pairs. Across four model families the RLVR policy is more decided than its
distilled counterpart on 95.5-100% of branches, and **the collapse is
significantly stronger in the semantic contrast than the syntactic one.** The
comfortable reading is closed off: what is being pruned is inferences.

**Why this is a better control than anything else in this note.** Both arms are
post-trained by the same authors from the same base checkpoints on the same
data, with distillation as the comparison rather than the raw base model. Every
other entry here compares an intervention against GRPO on a vendor checkpoint
whose pre/post pair is not available, which is exactly the confound the paper
names as its reason for doing the training itself.

**What it does not settle.** It measures what the collapse *is*, not whether
entropy is the quantity being controlled. The experiment this note has asked for
twice — vary the selection criterion while holding the reduction in effective
gradient fixed — is still unrun, and the random-control result stays
unexplained. What has changed is that one horn of the dichotomy is now costly to
defend: a statistic that moves only because something else is controlled would
not be expected to move *more* on semantic branches than syntactic ones.

**The compensating gain, which this note had not recorded.** The same work
measures what RLVR buys with the diversity it spends: backtracking probability
at dead ends rises from 0.0068 to 0.1537 and from 0.0647 to 0.1687 on two maze
models, and recovery from an injected distractor improves by 4.18 to 29.09
points on mathematics. Masking illegal continuations prices the trade — with
invalid options removed, the flatter distilled policy beats the RL one by about
60%. So the exchange law's framing of entropy as a resource spent for reward is
not wrong so much as underspecified: it is spent for *validity*, and what it
buys and what it costs are separately measurable. Recorded as
finding:8ff7e486af43c153.

<!-- analysis-sources: 8 -->
