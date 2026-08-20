# Reasoning Evaluation

<!-- auto:begin -->

Benchmarks for reasoning and the methodology behind them: what each one actually tests, how contamination and memorization inflate a score, and where a reported gain fails to reproduce. The question the archive answers is which numbers a claim about reasoning can be built on.

- **Slug**: `reasoning-evaluation`
- **Papers**: 56
- **Seminars**: 0
- **Tracked keywords**: `reasoning benchmark`, `mathematical reasoning`, `multi-step reasoning`, `logical reasoning`, `competition math`, `math word problem`, `GSM8K`, `AIME`, `benchmark contamination`, `data contamination`, `LLM as a judge`, `reasoning evaluation`, `evaluating reasoning`, `ARC AGI`

## Most recent papers

- [LoongReflect: Boosting Long-Horizon Reflection in Search Agents via Global Perspective Distillation](../../archive/papers/2026/arxiv-2608-11967/summary.md) (2026-08-12)
  - Gives a search agent an explicitly reversible trajectory tree with reflect and backtrack as first-class actions, and trains the reflection policy with a dense local signal distilled from a teacher that can see the whole trajectory alongside the sparse terminal reward the local decision is ultimately judged by.
- [Calibrating Post-Training Feature Shifts for LLM Data Contamination Detection](../../archive/papers/2026/arxiv-2608-10462/summary.md) (2026-08-11)
  - Calibrates feature-based data-contamination detectors against the systematic feature shifts that post-training introduces, by measuring how controlled prompt variants move scores on known non-members and then correcting only the recurring shift directions, with the gains concentrated at the low-false-positive operating point rather than in AUC.
- [V-FiLLM: Verified Financial LLM Reasoning Benchmark](../../archive/papers/2026/arxiv-2608-11047/summary.md) (2026-08-11)
  - Generates financial reasoning benchmarks from executable computation trees over real tables so that answers are correct by construction with no model in the labelling loop, exposes four independently controllable difficulty axes, and finds that unit and scale perturbations collapse the strongest model from 98.4 percent to 3.0.
- [SafeSceneReason: A Multimodal Reasoning Benchmark Connecting Industrial Hazards with Accident Knowledge](../../archive/papers/2026/arxiv-2608-09230/summary.md) (2026-08-10)
  - Builds an industrial-safety reasoning benchmark from two pipelines -- program execution over safety scene graphs, and evidence graphs extracted from real accident-investigation reports -- and shows that general multimodal capability does not transfer to it while a 9B model fine-tuned on its chain-of-thought split matches frontier systems.
- [Beyond Solvability: Task Learnability as a Static Prior for LLM RL Post-Training](../../archive/papers/2026/arxiv-2608-09217/summary.md) (2026-08-10)
  - Separates how well a policy currently does on a task from how positively that task responds to further training, shows the second is reproducible across independent runs and predicts downstream value at matched current pass rate, and estimates it from a short probe run before RL begins.
- [Mismatch Matters: On-Policy Distillation Beyond Token Agreement](../../archive/papers/2026/arxiv-2608-09836/summary.md) (2026-08-10)
  - Identifies degenerate agreement -- students reaching near-perfect token agreement with a teacher by looping while the response as a whole is broken -- and replaces the agreement objective with two directional mismatch corrections, one bounding runaway excess tokens and one injecting teacher-preferred mass at positions the student almost never samples.
- [Post-Hoc Sparse Coding of Latent Communication Between Vision-Language Model Agents](../../archive/papers/2026/arxiv-2608-10198/summary.md) (2026-08-10)
  - Fits a post-hoc sparse autoencoder to the frozen dense tensors that two vision-language agents exchange, finds a 128-fold payload reduction at near-identical reconstruction and roughly unchanged single-run accuracy, and then spends most of the paper enumerating the alternative explanations its own design cannot rule out.
- [MathShikkha: A Controlled Study of Answer-Only and Chain-of-Thought Supervision for Bangla Mathematical Reasoning in Small Language Models](../../archive/papers/2026/arxiv-2608-08503/summary.md) (2026-08-09)
- [MedCalc-R1: Knowledge-Guided Reward Framework for Medical Mathematical Reasoning](../../archive/papers/2026/arxiv-2608-08623/summary.md) (2026-08-09)
- [PAST: Privileged Adaptation from Complete Student Trajectories for On-Policy Self-Distillation](../../archive/papers/2026/arxiv-2608-08726/summary.md) (2026-08-09)
  - Gives the teacher in on-policy self-distillation access to each completed student rollout and its verified outcome, adapting it to preserve behaviour on successes and redirect failures toward verified success, while the student keeps a prefix-only interface it can actually deploy.
- [When Is Benchmark Contamination Detectable? Information Limits and Power-Calibrated Audits](../../archive/papers/2026/arxiv-2608-07914/summary.md) (2026-08-08)
  - Casts benchmark contamination auditing as sparse-mixture detection, proves that detectability is governed by the single quantity alpha*rho*sqrt(m), and shows empirically that the resulting power predictions transport while the sample-size budgets derived from them do not.
- [Think Deep, Speak Once: Relit, A Recursive Latent Implicit Transformer Framework](../../archive/papers/2026/arxiv-2608-08113/summary.md) (2026-08-08)
  - Bolts a small trainable recurrent block between a frozen 1.1B language model's body and its output head, so reasoning happens as repeated refinement of two latent vectors rather than as generated tokens.
- [VTO: Visual Tool Orchestration for Video Anomaly Detection](../../archive/papers/2026/arxiv-2608-08219/summary.md) (2026-08-08)
  - Trains a multimodal agent to orchestrate twelve video-analysis tools for anomaly detection with GRPO under a dual reward that combines exact-match rule checks with an LLM judge scoring logicality, relevance and completeness, and releases the benchmark it is evaluated on.
- [Zero Gap Is Not Restoration: Stratified Per-Question Probability Evaluation and Step-wise Mitigation of Benchmark Contamination](../../archive/papers/2026/arxiv-2608-07341/summary.md) (2026-08-07)
  - Shows that the standard metric for judging contamination-mitigation strategies can be scored by cancellation rather than by restoration, replaces it with a per-question stratified metric under which the published ranking reverses, and proposes a mitigation that decides its intervention during decoding instead of from a prior estimate.
- [Mitigating Scoring Bias in LLM-as-a-Judge via Random Number Generation](../../archive/papers/2026/arxiv-2608-05726/summary.md) (2026-08-06)
  - Measures an LLM judge's latent number bias by asking it to emit random numbers, then rectifies its scoring token probabilities against that measured bias.
- [Hierarchical Latent Prediction for Language Models](../../archive/papers/2026/arxiv-2608-05806/summary.md) (2026-08-06)
  - Adds a higher-level abstract latent as an auxiliary pretraining target to reduce compounding error in latent-space rollouts, aiming at longer-horizon coherence than multi-token or next-latent prediction.
- [DASH: Divergence-Adaptive Supervision Horizons for On-Policy Self-Distillation of Reasoning Models](../../archive/papers/2026/arxiv-2608-06243/summary.md) (2026-08-06)
  - Weights on-policy self-distillation supervision by how each local teacher-student divergence compares to the sequence mean, gating backward multi-step aggregation on that comparison.
- [RP-OPSD: Reasoning-Pivot-Guided On-Policy Self-Distillation for Multilingual Reasoning Transfer](../../archive/papers/2026/arxiv-2608-06347/summary.md) (2026-08-06)
  - Concentrates privileged self-distillation on reasoning pivots identified by the teacher's distributional shift when an English reference solution is added or removed, for multilingual reasoning transfer.
- [Reasoning Errors Have a Region and a Direction in the Residual-Stream Trajectory of LLMs](../../archive/papers/2026/arxiv-2608-05660/summary.md) (2026-08-06)
  - Detects flawed reasoning from residual-stream trajectories by combining layerwise motion with a quantized region reader and a normalized direction reader, rather than probing full states.
- [On-Policy Self-Distillation without Any Supervision](../../archive/papers/2026/arxiv-2608-06296/summary.md) (2026-08-06)
- [Constraint-First Reasoning: A Training-Free Protocol for Exploiting Answer-Space Constraints in Mathematical Problem Solving](../../archive/papers/2026/arxiv-2608-05254/summary.md) (2026-08-05)
  - A training-free two-stage prompting protocol that extracts a problem's answer-space constraints first and then checks its own intermediate and final results against them, routed on by a regex detector.
- [Self-Improving Large Language Models via Progressive Experience Evolution](../../archive/papers/2026/arxiv-2608-02139/summary.md) (2026-08-03)
  - Inserts a stage before RL in which the model extracts textual lessons from its own successful and failed rollouts, filters them by measured marginal utility on a held-out probe set, and distills the surviving pool into its own weights — so that GRPO starts from a policy that fails all-eight-samples less often.
- [Beyond the Mean: Multi-Moment Policy Optimization for LLM Reasoning](../../archive/papers/2026/arxiv-2608-02149/summary.md) (2026-08-03)
  - Treats a policy's per-problem failure probability as a random variable over the problem distribution and shows that REINFORCE, pass@K training and MaxRL each optimize a single moment of it, then proposes minimizing the first T moments jointly — which is exactly minimizing the expected truncated number of rollouts needed to reach a first success.
- [Reinforcement Learning with Evolving Rubrics as Rewards for Audio Reasoning](../../archive/papers/2026/arxiv-2608-02831/summary.md) (2026-08-03)
  - Supervises audio reasoning with per-question rubrics generated from the raw waveform, and keeps the signal alive as the policy improves by regenerating the rubrics from the model's own rollouts each step and pruning any criterion that every rollout satisfies or none does.
- [Cloud-ScPO: Hidden-State Geometry for Semi-Supervised Preference Optimization in LLM Reasoning](../../archive/papers/2026/arxiv-2608-01014/summary.md) (2026-08-02)
  - Scores unlabeled reasoning trajectories by how their mean-pooled hidden states connect to correct and incorrect reference point clouds built from a small labeled set, and uses that score to pick the concrete chosen and rejected responses inside answer clusters that self-consistency has already separated.

<!-- auto:end -->

## Notes

### Four independent sources of noise, all now measured

Every quantitative claim in this archive rests on benchmarks of 30-500 problems.
Four separate effects degrade them. They are independent, so they compound.

**1. Sampling noise (derived).** 30 AIME problems as a fixed population, only
sampling randomness; worst case `p=0.5` gives `SEM = 0.5/sqrt(30k)`:

| k | SEM (pp) | reported at this k by |
| --- | --- | --- |
| 4 | 4.6 | DEER |
| 16 | 2.3 | 80/20, CUSUM |
| 64 | 1.1 | Revisiting Entropy |

**2. Hardware and precision (measured).** Greedy decoding is not deterministic.
On AIME'24 with DeepSeek-R1-Distill-Qwen-7B — the model most of this archive's
early-exit work uses — across 12 runtime configs (GPU type × count × batch size):

| precision | Std@Acc | Std of output length |
| --- | --- | --- |
| BF16 | **9.15 pp** | **9,189 tokens** |
| FP32 | 0 | 0 |

Cause: non-associative floating-point addition, plus minimal top1-top2 gaps in
reasoning models, so 7 mantissa bits flip an argmax and one early token forks
the chain. **Audited: 1 of 45 archived papers reports precision or hardware —
the paper about it.**

**3. Construct fragility (measured).** Re-instantiating the same problems with
different numbers drops RL-trained models 20-95% on the strict metric, 2.6-7.2%
on the loose one.

**4. Contamination opacity (measured).** This is the newest and the worst.
SFT-stage contamination *is* detectable — until a brief GRPO run conceals the
signals detectors rely on, with **PPO-style importance sampling and clipping
identified as the cause**, so a broad class of RL methods launders it. And when
CoT contamination is applied to an already-trained reasoning model, most
detectors perform **near random**. For exactly the class of models this archive
studies, contamination is plausible and undetectable.

### What the four together mean

The natural defence of any archived result — "contamination would have been
detected" — is closed by (4). The natural defence "the effect is larger than
noise" is closed by (1) and (2) for anything under ~10 points on AIME. And (3)
says even a clean, well-powered measurement may not measure reasoning.

**None of this makes any individual paper wrong.** It means the field currently
lacks the instrumentation to adjudicate its own disputes at the 2-5 point scale
where most of them live — which is precisely the scale of the entropy-method
comparisons, the early-exit accuracy claims, and the RLVR token-selection
competition.

### The judge layer fails at three levels

At least four archived papers depend on LLM judges for labels.

- **The metric.** Exact-match agreement overstates chance-corrected
  discrimination by 33.8-41.3 pp across 21 judges. "85% agreement" ≈ κ 0.48.
  And high test-retest reliability coexists with severe position bias — the most
  reproducible judge measured is among the least valid.
- **The ground truth.** Under rating indeterminacy, forced-choice elicitation
  selects judges **up to 31% worse** than response-set elicitation.
- **The construct.** Judge preference does not correlate with concrete measures
  of safety, world knowledge or instruction following; judges prioritize style
  over factuality.

One archived paper defends its judge-derived measurements by citing inter-judge
agreement of 94.87-98.75% and Gwet's AC1 0.96-0.99. That is exactly the
inference the consistency-bias paradox invalidates.

*Unresolved:* the 2026 judge audit finds verbosity bias below 0.011 while the
2024 study finds style outweighing substance. Whether style bias receded or
merely moved to properties the audit did not measure is open.

### Reading rules

- **Never compare deltas across papers.** Absolute scores at matched budgets, or
  methods within one paper.
- **Ask for `k`.** A 3-point gain at k=4 and k=64 are not the same claim.
- **Ask for precision and hardware.** Almost nobody reports them.
- **Prefer larger benchmarks** for load-bearing claims.
- **Prefer pass@k trends** to accuracy deltas — a margin widening monotonically
  with k is harder to produce by chance.
- **Prefer OOD systematicity to in-distribution accuracy** where the claim is
  about a learned procedure.
- **Discount judge-labelled results**, especially interpretive labels
  (reactive vs proactive correction; collapse-mode taxonomies).
- **Treat contamination as unfalsifiable** for RL-post-trained models. Argue
  from construct-varied benchmarks instead.



---

## An opening the field has named twice and not filled

Recorded here as a state-of-the-literature finding, not as a plan.

**Two archived papers independently ask for a variance decomposition of
evaluation, and neither performs one:**

- The judge audit's release section lists "large-scale meta-analysis across
  judges and benchmarks (**including variance-component decompositions across
  runs, items, and position orderings**)" among "three use cases we cannot
  pursue here" — and releases its ~541,000-judgment corpus specifically to
  enable them.
- The nondeterminism paper states that reporting standard deviations without
  accounting for numerical nondeterminism risks "severely overestimating a
  model's true uncertainty, since the **reported variance reflects a mixture of
  intrinsic model uncertainty and variance introduced by finite numerical
  precision**" — a variance-components problem stated in prose and left there.

**Audited: 0 of 45 archived papers performs a variance decomposition.**

### Why the gap persists

It is classical measurement statistics — generalizability theory, random-effects
estimation — rather than machine learning, so the field has the data and the
motivation without the tradition. The archive contains one paper that does reach
into that tradition: RADAR imports item response theory to model query difficulty
and configuration ability. G-theory is IRT's variance-side complement, and the
absence of the second alongside the presence of the first is the shape of the
gap.

### What filling it would settle

The four noise sources catalogued above are currently listed and not jointly
modelled, so their relative sizes are unknown and no design rule follows from
them. A fitted decomposition over item, replicate, system configuration and
precision would convert this note's warnings into two things the field lacks: a
reporting standard with correct intervals, and a statement of which published
2-5 point results survive them.

### Reading consequence for this archive

Until then, treat every archived result in the 2-5 point range as unreplicated
rather than established, and prefer the archive's structural findings — the
commitment boundary, the four-vs-heuristic circuit dispute, the entropy-flow
mechanisms, the label-free process reward derivation — which do not depend on
small benchmark deltas.
