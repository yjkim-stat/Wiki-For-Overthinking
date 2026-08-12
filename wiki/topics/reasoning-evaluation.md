# Reasoning Evaluation

<!-- auto:begin -->

Benchmarks for reasoning and the methodology behind them: what each one actually tests, how contamination and memorization inflate a score, and where a reported gain fails to reproduce. The question the archive answers is which numbers a claim about reasoning can be built on.

- **Slug**: `reasoning-evaluation`
- **Papers**: 41
- **Seminars**: 0
- **Tracked keywords**: `reasoning benchmark`, `mathematical reasoning`, `multi-step reasoning`, `logical reasoning`, `competition math`, `math word problem`, `GSM8K`, `AIME`, `benchmark contamination`, `data contamination`, `LLM as a judge`, `reasoning evaluation`, `evaluating reasoning`, `ARC AGI`

## Most recent papers

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
- [Constraint-First Reasoning: A Training-Free Protocol for Exploiting Answer-Space Constraints in Mathematical Problem Solving](../../archive/papers/2026/arxiv-2608-05254/summary.md) (2026-08-05)
  - A training-free two-stage prompting protocol that extracts a problem's answer-space constraints first and then checks its own intermediate and final results against them, routed on by a regex detector.
- [Self-Improving Large Language Models via Progressive Experience Evolution](../../archive/papers/2026/arxiv-2608-02139/summary.md) (2026-08-03)
  - Inserts a stage before RL in which the model extracts textual lessons from its own successful and failed rollouts, filters them by measured marginal utility on a held-out probe set, and distills the surviving pool into its own weights — so that GRPO starts from a policy that fails all-eight-samples less often.
- [Beyond the Mean: Multi-Moment Policy Optimization for LLM Reasoning](../../archive/papers/2026/arxiv-2608-02149/summary.md) (2026-08-03)
  - Treats a policy's per-problem failure probability as a random variable over the problem distribution and shows that REINFORCE, pass@K training and MaxRL each optimize a single moment of it, then proposes minimizing the first T moments jointly — which is exactly minimizing the expected truncated number of rollouts needed to reach a first success.
- [Reinforcement Learning with Evolving Rubrics as Rewards for Audio Reasoning](../../archive/papers/2026/arxiv-2608-02831/summary.md) (2026-08-03)
- [Cloud-ScPO: Hidden-State Geometry for Semi-Supervised Preference Optimization in LLM Reasoning](../../archive/papers/2026/arxiv-2608-01014/summary.md) (2026-08-02)
  - Scores unlabeled reasoning trajectories by how their mean-pooled hidden states connect to correct and incorrect reference point clouds built from a small labeled set, and uses that score to pick the concrete chosen and rejected responses inside answer clusters that self-consistency has already separated.
- [Your Reasoning Benchmark May Not Test Reasoning: Revealing Perception Bottleneck in Abstract Reasoning Benchmarks](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-826/summary.md) (2026-01-01)
  - Separates perception from reasoning in ARC-style benchmarks with a two-stage pipeline, and finds about 80% of vision-language model failures are perception errors, not reasoning errors.
- [SMART: Evaluating LLMs&apos; Mathematical Reasoning via a Human Cognitive Process-Inspired Benchmark](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1638/summary.md) (2026-01-01)
  - Decomposes mathematical problem-solving into four cognitive dimensions after Polya and tests each separately, finding wide capability gaps that final-answer accuracy hides.
- [VisAidMath: Benchmarking Visual-Aided Mathematical Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1719/summary.md) (2026-01-01)
  - Benchmarks whether multimodal models can construct visual aids for geometry problems, and finds high answer accuracy conceals near-total failure at producing or reasoning from those aids.
- [Revisiting a Pain in the Neck: A Semantic Reasoning Benchmark for Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-210/summary.md) (2026-01-01)
  - Consolidates multiword-expression resources into one evaluation suite covering idioms, noun compounds and verbal constructions across extraction, classification and interpretation tasks.
- [MathSight: A Benchmark Exploring Have Vision-Language Models Really Seen in University-Level Mathematical Reasoning?](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2198/summary.md) (2026-01-01)
  - A university-level multimodal math benchmark with original, hand-drawn, photographed and text-only variants of each problem, on which a model with no image beats its own multimodal variants and GPT-5.
- [AgentCoMa: A Compositional Benchmark Mixing Commonsense and Mathematical Reasoning in Real-World Scenarios](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-380/summary.md) (2026-01-01)
  - A benchmark where each task needs one commonsense step and one math step, on which model accuracy drops nearly 30% relative to solving the steps in isolation while humans show no such gap.
- [MTR-Bench: A Comprehensive Benchmark for Multi-Turn Reasoning Evaluation](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-984/summary.md) (2026-01-01)
  - A fully automated multi-turn reasoning benchmark of 40 tasks and 3600 instances requiring interaction with an environment, on which frontier reasoning models fall short.
- [ErrorRadar: Benchmarking Complex Mathematical Reasoning of Multimodal Large Language Models Via Error Detection](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1217/summary.md) (2026-01-01)
  - Benchmarks multimodal models on detecting and categorizing errors in K-12 math solutions collected from real student interactions, with the best model about 10% behind human experts.
- [The Confidence Paradox: Unveiling the Latent Discriminative Power of Diffusion Large Language Models in Mathematical Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2142/summary.md) (2026-01-01)
  - Finds diffusion language models are badly miscalibrated on math reasoning yet rank correct from incorrect far better than autoregressive baselines, because their confidence tracks structural consistency rather than correctness.
- [MAC-Reasoner: A Multi-Agent Collaborative Framework for Enhancing Logical Reasoning in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-233/summary.md) (2026-01-01)
  - Keeps the LLM as the reasoner while a symbolic solver supplies a Logic-Augmented Context, so conflicts flagged by execution direct attention to violated constraints instead of replacing deduction.
- [SciVQR: A Multidisciplinary Multimodal Benchmark for Advanced Scientific Reasoning Evaluation](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-28/summary.md) (2026-01-01)
  - A multimodal scientific reasoning benchmark over 54 subfields with domain-specific visuals and expert solutions for 46% of items, scoring the reasoning process as well as the answer.
- [PBEBench: A Multi-Step Programming by Examples Reasoning Benchmark inspired by Historical Linguistics](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-432/summary.md) (2026-01-01)
  - An inductive-reasoning benchmark from historical linguistics that requires inducing cascades of string-rewrite programs, with automated contamination-resistant generation and controllable difficulty.
- [CoRE: A Fine-Grained Code Reasoning Benchmark Beyond Output Prediction](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-460/summary.md) (2026-01-01)
  - Evaluates code reasoning by implementation invariance and intermediate-state accuracy, finding models get final outputs right while reasoning incorrectly about execution.
- [On The Fragility of Benchmark Contamination Detection in Reasoning Models](../../archive/papers/2026/local-4cf1061e50d8b3c3/summary.md) (2026-01-01)
  - Shows that benchmark contamination in reasoning models is alarmingly easy to hide: a brief round of GRPO erases the signals contamination detectors rely on, and PPO-style importance sampling and clipping are identified as the cause — implying a broad class of RL methods conceals contamination inherently.
- [Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias](../../archive/papers/2026/local-504cc53656b06ab4/summary.md) (2026-01-01)
  - Evaluates 21 LLM judges across three benchmarks and three protocols over ~541,000 judgments, and shows the field's standard validation metric — exact-match agreement — overstates chance-corrected discrimination by 34-41 points universally, while high test-retest reliability can coexist with severe position bias.

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
