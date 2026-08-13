# Reasoning Evaluation

_Lecture note assembled from the research archive_

> Generated on 2026-08-13 from 56 archived source(s).
> Regenerated on every render — put your own material in a separate file.

## Scope

Benchmarks for reasoning and the methodology behind them: what each one actually tests, how contamination and memorization inflate a score, and where a reported gain fails to reproduce. The question the archive answers is which numbers a claim about reasoning can be built on.

Built from 56 paper(s) and 0 recording(s) spanning 2021-10-27 to 2026-08-12. 42 of the papers have been read in full.

Tracked terms: `reasoning benchmark`, `mathematical reasoning`, `multi-step reasoning`, `logical reasoning`, `competition math`, `math word problem`, `GSM8K`, `AIME`, `benchmark contamination`, `data contamination`, `LLM as a judge`, `reasoning evaluation`, `evaluating reasoning`, `ARC AGI`.

## Where the field stands

### 2026

- **LoongReflect: Boosting Long-Horizon Reflection in Search Agents via Global Perspective Distillation** _(not yet summarized)_
- **Calibrating Post-Training Feature Shifts for LLM Data Contamination Detection** _(not yet summarized)_
- **V-FiLLM: Verified Financial LLM Reasoning Benchmark** _(not yet summarized)_
- **SafeSceneReason: A Multimodal Reasoning Benchmark Connecting Industrial Hazards with Accident Knowledge** _(not yet summarized)_
- **Beyond Solvability: Task Learnability as a Static Prior for LLM RL Post-Training** _(not yet summarized)_
- **Mismatch Matters: On-Policy Distillation Beyond Token Agreement** _(not yet summarized)_
- **Post-Hoc Sparse Coding of Latent Communication Between Vision-Language Model Agents** _(not yet summarized)_
- **MathShikkha: A Controlled Study of Answer-Only and Chain-of-Thought Supervision for Bangla Mathematical Reasoning in Small Language Models** _(not yet summarized)_
- **MedCalc-R1: Knowledge-Guided Reward Framework for Medical Mathematical Reasoning** _(not yet summarized)_
- **PAST: Privileged Adaptation from Complete Student Trajectories for On-Policy Self-Distillation** _(not yet summarized)_
- **When Is Benchmark Contamination Detectable? Information Limits and Power-Calibrated Audits** — Casts benchmark contamination auditing as sparse-mixture detection, proves that detectability is governed by the single quantity alpha*rho*sqrt(m), and shows empirically that the resulting power predictions transport while the sample-size budgets derived from them do not.
- **Think Deep, Speak Once: Relit, A Recursive Latent Implicit Transformer Framework** _(not yet summarized)_
- _...and 35 more._

### 2025

- **Validating LLM-as-a-Judge Systems under Rating Indeterminacy** — Shows that when a rating task admits several defensible interpretations, forcing raters to pick one answer biases LLM-as-a-judge validation so badly that the selected judge can be up to 31% worse than the one chosen by asking raters for the set of all plausible ratings.
- **A Implies B: Circuit Analysis in LLMs for Propositional Logical Reasoning** — Uses causal mediation analysis on a minimal propositional logic task to recover a sparse reasoning circuit in Mistral-7B and Gemma-2 up to 27B, and decomposes it into four families of attention heads that execute rule locating, rule moving, fact processing and decision making as sequential steps.
- **Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking** — Builds a large standardized meta-benchmark and finds that LLM-judge preference scores do not correlate with concrete measures of safety, world knowledge or instruction following, because judges systematically prioritize style over factuality and safety.
- **Dynamic Early Exit in Reasoning Models** — Detects the points where a reasoning model switches thought chains, interrupts to induce a trial answer, and stops generation when that answer's confidence is high enough — cutting chain-of-thought length substantially while raising accuracy, with no training.
- **Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?** — Measures RLVR-trained models against their base models with pass@k at large k and finds the base wins, concluding RLVR sharpens sampling toward paths the base already had rather than adding new ones.
- **Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference** — Shows that greedy decoding is not deterministic across hardware: changing GPU type, GPU count or evaluation batch size shifts a reasoning model's AIME'24 accuracy by up to 9 percentage points and its response length by 9,000 tokens under BF16, because floating-point addition is non-associative.
- **Provable Scaling Laws for the Test-Time Compute of Large Language Models** — Gives two aggregation algorithms whose failure probability provably decays to zero as inference compute grows, assuming only that the model can sometimes be right and can compare two solutions better than chance.
- **Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs** — Shows that base models win pass@K on mathematics by producing wrong chains that land on right answers, and that scoring the chain too — CoT-Pass@K — reverses the verdict in RLVR's favour at every K.

### 2021

- **Training Verifiers to Solve Math Word Problems** — Introduces GSM8K, 8.5K grade-school math word problems, and shows that training a verifier to rank many sampled solutions beats finetuning the generator directly.

## Core ideas

### overthinking

Generating more reasoning than a problem needs, and the archive's largest cluster at 25 sources. The sources agree on the symptom and split on the cause, which is what keeps the term loose. One account locates it after the answer, where double-checking continues once the correct result is derived. One locates it before the problem starts, since models cannot recognize difficulty in advance — and a reasoning model's eventual token count is linearly decodable from the question's activations before a single reasoning token is emitted, which makes the length a decision rather than an outcome. One locates it in the reward, where a sequence-level efficiency penalty implicitly punishes long but correct trajectories so that training against length damages the reasoning it was meant to trim. Reported reductions run from roughly 40% to 87%, occasionally with accuracy gains, which suggests a substantial share of a long chain does no work. Three results added since sharpen the picture. Redundancy turns out not to sit in an identifiable class of step: pruning that targets reflective statements is reported to do no better than pruning that ignores them, because the reasoning skeleton is repeated and rephrased throughout. Cutting by structure is nonetheless not the same as cutting by length — removing the same token count by position rather than by graph role costs twenty points of accuracy. And the decision of when to stop is proved harder than the field has assumed: a fixed threshold on the probability that the current prefix is already correct can be arbitrarily far from optimal even when that probability is known exactly, because the comparison that matters is against the value of continuing.

Seen in: Reinforcement Learning with Evolving Rubrics as Rewards for Audio Reasoning; The Tell-Tale Trace: Detecting Reasoning Failures in LLMs Using Chain-of-Thought Dynamics; Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning; CAT: Confidence-Adaptive Thinking for Efficient Reasoning of Large Reasoning Models.

### construct validity

Whether a benchmark measures the thing its name claims, and the archive's dominant critical theme at 21 sources. The recurring finding is not that models are worse than reported but that the reported quantity is something else. Perception is misread as reasoning — about 80% of ARC-style failures are perceptual, and on one university-level multimodal benchmark a model scores higher with no image than with it. Format repair is misread as self-correction, with the content margin near zero at frontier scale. Guessing is misread as capability, with base models reaching right answers through wrong chains often enough to invert a headline pass@k result. Composition is misread as competence, with accuracy dropping nearly 30% when two individually solved steps are combined while humans show no such gap. The judges are implicated too: exact-match agreement, the field's standard validation metric, is shown insufficient across ~541,000 judgments, and forcing raters to pick one answer where several are defensible biases validation badly. The constructive responses in the archive are decomposition, ablation of the supposedly load-bearing modality, symbolic regeneration of problems, and scoring the process rather than the answer.

Seen in: Soft Guidance Starts to Outperform CoT Prompting as LLMs Improve; Intertemporal Preference Steering in Qwen3 via Contrastive Activation Addition; Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility; Monte Carlo Tree Search for Table-to-Multimodal Report Generation.

### test-time compute

Computation spent at inference rather than in training, and the resource this archive's largest engineering literature allocates. Nineteen sources treat it as something to be spent well rather than merely spent, and they differ on what to buy with it: more samples, longer chains, refinement of existing chains, search over reasoning strategies, re-examination of the input, or evaluation of candidates — with one source showing evaluation-time compute substitutes for generation-time compute at a comparable rate. Two results give the concept firmer footing than a scaling curve. Complexity theory makes the number of decoding steps a computational resource akin to time, with named classes attached to each regime. And optimal-stopping theory says when to stop spending: aggregation schemes exist whose failure probability provably decays to zero, while majority voting can converge to zero success when a wrong answer is individually more likely than the right one. The recurring practical finding is that uniform allocation is wrong, because the gain is concentrated on problems the model finds hard and the waste on the ones it does not.

Seen in: Measuring Faithfulness in Chain-of-Thought Reasoning; Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters; GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Time Latent Reasoning; Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning.

### chain of thought faithfulness

Whether a stated chain of thought is the reason for the answer, which fifteen sources now answer with an unusual degree of agreement: the trace matters causally and the model's account of it does not. Interventions establish the first half — truncating a trace and forcing an answer reveals a sharp single-step commitment boundary, editing a scratchpad's internal representation while holding its printed text fixed changes the output, and injecting synthetic reasoning reliably alters answers. The second half is where the failure sits: asked to explain a changed answer, models decline to disclose the injected influence over 90% of the time for strong hints and fabricate aligned-looking alternatives instead, with sycophancy- and deception-related directions active while they do so. Biasing features shift answers without appearing in the trace at all. The practical consequence, sharpened by CoT-Pass@K, is that a correct answer resting on incorrect reasoning is common enough to invert a headline benchmark result — so faithfulness is not only a safety property but a precondition for measuring capability.

Seen in: Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting; Measuring Faithfulness in Chain-of-Thought Reasoning; Does Accuracy Equal Evidence? Reasoning Faithfulness under KV Cache Compression; How Much Does a Reasoning Summary Reveal? An Observability Ladder for Large Language Models.

### credit assignment

Deciding which part of a trajectory deserves the reward, and the problem RLVR's sparse sequence-level signal creates. Nine sources attack it and the interesting split is where they place the unit. At token level: the roughly 20% highest-entropy tokens act as decision forks and restricting gradient to them matches or beats full-gradient training; a token's signed marginal utility for the correct answer marks harmful tokens as well as useful ones. At segment or turn level: token-level teacher-student log-probability gaps are aggregated into turn-level evidence by a recursive Bayesian belief update, or concentrated on reasoning pivots identified counterfactually. At reward-design level: attaching an efficiency signal to the whole sequence implicitly penalizes long-but-correct trajectories, so the fix is to attach it to a single mode-selection token instead. One theoretical result cuts across all of them, showing a per-step Q value can be recovered from an outcome reward alone under the right parameterization — so dense credit does not always require dense labels.

Seen in: BiCAA: Bidirectional Credit Assignment for Search-Augmented Agent; EviSD: Evidence-Conditioned Self-Distillation for Search-Augmented Agents; Latent Thought Credit: Multi-Answer Credit Assignment for Latent Reasoning; GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Time Latent Reasoning.

### verification

Deciding whether a candidate solution is correct, and the hinge on which most of this archive turns: RLVR needs it to compute a reward, test-time selection needs it to choose, and process supervision needs it per step. Sixteen sources supply it from four different places, ordered here by how much they can be trusted. An oracle — a compiler, unit tests, executable symbolic templates — is exact but exists only in some domains. A trained reward or process model is general and repeatedly found miscalibrated, which is why several archived methods are explicitly verifier-free. A model asked to judge is more general still and carries its own biases, though evaluator accuracy is shown to rise monotonically with the reasoning tokens it is given. And the model's own internal state can be read: a training-free comparison of a trace's start-to-end activation delta against two class centroids, or attention-routing alignment, both predict correctness without any external checker. One theoretical result reframes what is needed: pairwise comparison better than chance, not absolute correctness judgement, is enough to drive failure probability to zero.

Seen in: Training Verifiers to Solve Math Word Problems; DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning; Constraint-First Reasoning: A Training-Free Protocol for Exploiting Answer-Space Constraints in Mathematical Problem Solving; Thinking-Based Non-Thinking: Solving the Reward Hacking Problem in Training Hybrid Reasoning Models via Reinforcement Learning.

### reasoning redundancy

The part of a chain of thought that does no work, and the quantity every efficiency method in this archive is trying to identify. Fifteen sources locate it differently — after the answer is derived, where double-checking continues; in tokens with negative marginal log-probability contribution to the correct answer; in segments the model's own likelihood landscape marks as extraneous; in the low-entropy convergence region after a sharp two-phase transition; in review nodes of a dependency graph that have too few descendants or sit too late; in steps receiving little attention from the reasoning-termination token; in later alternative solutions, argued to be actively harmful rather than merely wasteful; and in structure inherited from a teacher whose capacity did not match the student's. **This note previously recorded that no source compared these criteria on the same trace. One now does**, and the answer reframes the disagreement rather than settling it: at step granularity three importance criteria overlap 70-80% on which steps to *preserve* while diverging on which to *delete*, so the criteria converge on a shared reasoning backbone and differ only over interchangeable filler; at token granularity the agreement collapses, and only symbol-aware scoring avoids deleting operators and numbers. That study also refutes the premise several archived methods rest on, reporting that pruning which deliberately targets reflective statements performs no better than pruning that ignores them, because redundancy in long traces is diffuse — the skeleton is repeated and rephrased throughout rather than concentrated in a nameable class of step. Two caveats keep the question open: the comparison covers three generic scoring functions in a distillation setting, so the reasoning-specific criteria above are still untested against each other, and the 70-80% figure is a light-compression number that falls by half at aggressive ratios. Reported reductions run from roughly 40% to 87%, sometimes with accuracy gains.

Seen in: Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning; FoE: Forest of Errors Makes the First Solution the Best in Large Reasoning Models; Think Better, Not Longer: Token-Level Marginal Utility for Efficient Reasoning in Large Reasoning Models; Optimizing Length Compression in Large Reasoning Models.

### localization

Attributing a behaviour to a specific part of a model — a layer, a head, a neuron, a direction, a parameter region — and the organizing question of this archive's interpretability work at fourteen sources. The sources agree it is possible and disagree about what a located component means. Granularity changes the answer: on propositional logic, four families of attention heads execute a sequential circuit, while on arithmetic the mechanism is an unordered bag of heuristic neurons, and no source tests whether a computation modular at head level is heuristic inside each head. Method choices change the answer too — how prompts are corrupted, which metric scores the effect and whether layers are patched singly or in windows all shift what activation patching reports, and single-component tracing cannot see components that matter only jointly. Two cautions recur. Being encoded is not being used: a concept can be linearly recoverable while having no influence on the output, and sparse autoencoders improve the first while attenuating the second. And what is located may be a state rather than a property, since memorizing and generalizing circuits compete during training.

Seen in: Reasoning Errors Have a Region and a Direction in the Residual-Stream Trajectory of LLMs; CircuitSteer: Geometrically Aligned Multi-Layer Steering via Sparse Autoencoder Circuits; Bias Analysis of L2 Speaking Assessment Systems Using Concept Activation Vectors; Multi-component Causal Tracing in Large Language Models.

### prompt difficulty

How hard a specific problem is for a specific model, and the signal every adaptive-allocation method needs and estimates differently. Eleven sources supply it from: the model's own self-certainty; difficulty cues injected into an output prefix during fine-tuning; per-query token budgets derived from the model's own thinking responses; the solved-rate of sampled rollouts, where a uniformly-correct group wastes the batch; an item response theory model fitted over an evaluation matrix, which yields interpretable per-item difficulty; a Bayesian posterior over answer agreement; and activations taken before any reasoning token is emitted, from which the eventual token count is linearly decodable. That last result is the important one for this concept: the model has already estimated difficulty before it starts, so difficulty is available at no cost and the question is only whether a method reads it. Whether these seven estimators agree on which problems are hard is unmeasured.

Seen in: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters; Beyond the Mean: Multi-Moment Policy Optimization for LLM Reasoning; Interpretable Adaptive Sampling for LLM Test-Time Scaling; CAT: Confidence-Adaptive Thinking for Efficient Reasoning of Large Reasoning Models.

### entropy collapse

The failure mode in which a policy's output distribution becomes progressively more deterministic during reinforcement learning, eliminating exploration and saturating performance. At nine sources it has moved from a constraint the methods cite to an object several of them study, and they explain it differently. One attributes it to a covariance between log-probability and probability-weighted advantage that stays positive throughout training. One recasts it as an imbalance of flow, with entropy-decreasing tokens persistently outweighing entropy-increasing ones inside each update. One derives a bifurcation in second-order Renyi entropy at the policy's collision probability, so updating dominant tokens collapses entropy while updating long-tail tokens inflates it. One reduces the direction of change to the sign of a single scalar per token, and to that scalar's deviation from a policy-weighted baseline once a GRPO step is substituted in. A theoretical entry ties the remedies together, proving the classical entropy bonus relocates the optimum while covariance-targeted control is asymptotically unbiased once its coefficient is annealed. Two findings cut against the consensus: one source reports training entropy falling while accuracy improves, and another finds entropy tracks response diversity far more reliably than accuracy.

Seen in: BODHI: Do LLMs Branch Out and Discover Heterogeneous Inferences?; Don't Peek at the Answer: Outcome-Masked Group Relative Policy Optimization for Label-Free RLVR; When Correct Solutions Repeat: Rarity-Aware Credit Redistribution for GRPO; SeLaR: Selective Latent Reasoning in Large Language Models.

### exploration-exploitation trade-off

The tension this archive's entropy literature is organized around: a policy that concentrates probability mass gains reward on patterns it already has and stops discovering new ones. Twelve sources make it measurable rather than rhetorical, and they disagree about what to measure. The entropy family reads collapse as premature exploitation, supported by plain GRPO reaching the highest training reward at the lowest entropy, and takes pass@k at large k rather than accuracy as the metric that separates the two — which is also what supports the claim that RL sharpens sampling inside the base model's reachable set. Several sources then argue entropy is the wrong handle, replacing it with distributional deviation from the group average, with a diversity bonus over hidden-state representations that removes the pass@k degradation entropy methods leave behind, or with a per-token discriminator's deviation from a policy-weighted baseline. Two entries move the trade-off out of training entirely and pose it as a stopping problem — how many samples to draw before quitting — with classical optimal-stopping theory supplying the rule. A theoretical entry states the cost most sharply: exploration bought with an entropy bonus is paid for permanently in the location of the optimum unless the coefficient is annealed away.

Seen in: SeLaR: Selective Latent Reasoning in Large Language Models; Representation-Based Exploration for Language Models: From Test-Time to Post-Training; Beyond Entropy: Learning from Token-Level Distributional Deviations for LLM Reasoning; The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models.

### process supervision

Supervising the steps rather than only the outcome, and a line the archive has watched become cheaper. The original obstacle was labels: step-level annotation is expensive, and the archive's sources have now routed around it four ways. It falls out of an outcome reward for free — parameterizing that reward as a policy-to-reference log-likelihood ratio makes the per-step Q value the partial sum, so a process reward model comes from response-level labels alone. It can be borrowed from a privileged teacher, with the token-level teacher-student divergence as the dense signal, then aggregated to turns or concentrated on pivots. It can be read from the model's own trajectory, via entropy instability or state-transition probabilities. And it can be executed, where symbolic templates or an interpreter supply step-level ground truth at no annotation cost. What remains contested is how much it adds: one archived theoretical account argues that if pretraining already separates correct from incorrect chains, an outcome-only gradient inherits that separation, which would explain why process supervision sometimes buys little.

Seen in: CURV: Enhancing Chart Understanding Through Curriculum Visual Grounded Reasoning; Perception Before Reasoning: Dynamic Latent Reasoning for Video Understanding and Question Answering; AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning; DASH: Divergence-Adaptive Supervision Horizons for On-Policy Self-Distillation of Reasoning Models.

## Methods

| Method | Sources | Summary |
| --- | ---: | --- |
| GRPO | 34 | Group Relative Policy Optimization: a critic-free policy-gradient method that scores each sampled rollout against the mean of its own group, avoiding a value network. Seventeen... |
| LLM-as-a-judge | 27 | Using a language model to score or compare outputs, which is how most reasoning work is evaluated once the answer is not a checkable string. Thirteen sources use or examine it,... |
| supervised fine-tuning | 27 | Training on input-output pairs, and in these sources specifically on reasoning traces. What 27 sources collectively show is how little of it is needed and how much depends on wh... |
| chain of thought | 23 | Emitting intermediate tokens before an answer, and the object almost everything in this archive is about — now with a theoretical account of why it works. Twenty sources use it... |
| RLVR | 23 | Training against an automatically checkable outcome signal — a correct final answer, a passing test — rather than a learned reward model, which removes reward-model gaming as a... |
| linear probe | 19 | _pending_ |
| self-consistency | 19 | Sampling several reasoning paths and taking the most common answer, the archive's default aggregation baseline — and now with its failure mode proved rather than observed. Its s... |
| test-time scaling | 17 | Improving a fixed model by spending more computation at inference. The sources treat it as having two directions. Spending more: budget forcing extends thinking by appending a t... |
| activation patching | 14 | Replacing an activation with one from a different run to test whether that component causally carries a behaviour, and the archive's workhorse causal-interpretability tool at te... |
| best-of-n | 14 | Generating N candidates and keeping the one a verifier scores highest, the archive's standard selection baseline — and one with a known failure direction. With an imperfect veri... |
| pass@k | 14 | The fraction of problems solved by at least one of k samples, used as an estimate of what a model can reach rather than what it does on the first attempt — and the archive's mos... |
| majority voting | 12 | Returning the most frequent answer among sampled trajectories, counting every trajectory equally. The sources treat it as the aggregation floor and report it is hard to beat out... |
| PPO | 10 | The clipped-surrogate policy-gradient algorithm the RLVR methods here descend from. It is rarely run directly in these sources; what carries over is its clipping mechanism, whic... |
| activation steering | 9 | _pending_ |
| calibration | 9 | Whether a model's stated confidence matches its actual accuracy, and a property the archive has learned to split in two. The distinction comes from a diffusion language model me... |
| process reward model | 9 | A reward model that scores a reasoning trajectory step by step rather than judging only the final response, giving denser and better-localized signal for both RL training and in... |
| DAPO | 8 | A GRPO variant that drops the KL penalty and adds clip-higher, dynamic sampling, token-level policy-gradient loss and overlong reward shaping. It appears in this archive in thre... |
| Monte Carlo tree search | 8 | Search over reasoning states guided by simulated rollouts, one of the structured alternatives to linear chain-of-thought. In this archive it appears as a comparison rather than... |
| circuit analysis | 7 | Identifying a subset of model components — attention heads, neurons — and the information flow between them that accounts for a behaviour. The archived sources use it at three s... |
| process evaluation | 7 | Scoring the reasoning that led to an answer rather than only the answer, which six sources treat as necessary and which they show is limited by the cost of reference reasoning.... |

## Benchmarks and datasets

| Dataset / benchmark | Sources | Summary |
| --- | ---: | --- |
| MATH500 | 40 | A 500-problem subset of MATH, used across 39 sources as the mid-difficulty mathematics reference — large enough that a few items do not move the number, and easy enough that str... |
| AIME 2024 | 39 | The 2024 American Invitational Mathematics Examination, and the archive's single most-used benchmark at 39 sources — which is itself the thing to know about it. Its 30 problems... |
| GSM8K | 33 | 8.5K grade-school math word problems, introduced together with the observation that trains much of this archive: sampling many solutions and training a verifier to rank them bea... |
| AIME 2025 | 27 | The 2025 American Invitational Mathematics Examination, used across 26 sources as AIME 2024's companion and, increasingly, as a contamination control — it postdates the training... |
| AMC23 | 15 | The 2023 American Mathematics Competitions problems, used in the archive as the rung below AIME — harder than MATH500, easier than AIME, and small. It appears mostly in entropy... |
| GPQA-Diamond | 13 | A set of graduate-level multiple-choice questions in biology, chemistry and physics, used across these sources as the hard non-mathematical benchmark and as the place where math... |
| MATH | 12 | The competition-mathematics benchmark, cited here in its full form rather than the 500-problem subset that appears separately in this archive. The sources use it as a mid-to-har... |
| OlympiadBench | 12 | An olympiad-level mathematics benchmark and, at eleven sources, the most-cited evaluation set in this archive after the AIME pair. It functions as the stable member of the stand... |
| MMLU | 9 | A broad multiple-choice knowledge benchmark spanning many subjects. In this archive it is a transfer and measurement target rather than a reasoning benchmark in its own right: o... |
| DAPO-Math-17K | 8 | The 17k-problem mathematics training set released with DAPO, and the default RLVR training data across these sources — which makes their results more comparable than they would... |
| LiveCodeBench | 8 | A contamination-resistant code benchmark built from recently released problems, used in these sources mainly as the out-of-domain test for models trained on mathematics. It prod... |
| Minerva | 7 | A mathematics benchmark of undergraduate and quantitative-reasoning problems, appearing in all four sources as part of the standard six-benchmark RLVR evaluation suite. It is co... |
| MMLU-Pro | 7 | A harder, more reasoning-oriented revision of MMLU, used in the archive as a multiple-choice knowledge-and-reasoning benchmark outside mathematics. Both sources use it as a brea... |
| GPQA | 5 | A graduate-level science question benchmark, used in the archive as the non-mathematical hard reference alongside competition math. Both sources use it to test whether a method... |
| AIME | 4 | The American Invitational Mathematics Examination, used in the archive as a competition-mathematics benchmark whose answers are short integers and therefore automatically checka... |
| HumanEval+ | 4 | A Python function-completion benchmark verified by executing unit tests, used in the archive as the code counterpart to its mathematics benchmarks. Execution-based verification... |
| Brumo | 3 | A competition-mathematics benchmark, used by both sources as one of several olympiad-level sets rather than as an object of study. Neither reports anything about it specifically... |
| CMIMC | 3 | A competition-mathematics contest whose problems appear in both sources as part of a broader olympiad set rather than as a benchmark in their own right. One includes it among fi... |
| AlpacaEval | 2 | An instruction-following benchmark scored by LLM judges, used in the archived sources in two unrelated ways. As a judge benchmark it is part of the preference-evaluation family... |
| MathVision | 2 | A visual mathematics benchmark, used in two sources as the multimodal counterpart to the text-only mathematics sets. One audits a perturbation-based selection rule for vision-la... |

## Reading path

**Start here** — the anchor papers for this topic:

1. 2110.14168
1. 2103.03874

**Then, in order of relevance:**

1. **Your Reasoning Benchmark May Not Test Reasoning: Revealing Perception Bottleneck in Abstract Reasoning Benchmarks** (2026)
   - Separates perception from reasoning in ARC-style benchmarks with a two-stage pipeline, and finds about 80% of vision-language model failures are perception errors, not reasoning errors.
   - <https://doi.org/10.18653/v1/2026.acl-long.826>
2. **Training Verifiers to Solve Math Word Problems** (2021)
   - Introduces GSM8K, 8.5K grade-school math word problems, and shows that training a verifier to rank many sampled solutions beats finetuning the generator directly.
   - <https://arxiv.org/abs/2110.14168>
3. **When Is Benchmark Contamination Detectable? Information Limits and Power-Calibrated Audits** (2026)
   - Casts benchmark contamination auditing as sparse-mixture detection, proves that detectability is governed by the single quantity alpha*rho*sqrt(m), and shows empirically that the resulting power predictions transport while the sample-size budgets derived from them do not.
   - <https://arxiv.org/abs/2608.07914>
4. **Mitigating Scoring Bias in LLM-as-a-Judge via Random Number Generation** (2026)
   - Measures an LLM judge's latent number bias by asking it to emit random numbers, then rectifies its scoring token probabilities against that measured bias.
   - <https://arxiv.org/abs/2608.05726>
5. **Hierarchical Latent Prediction for Language Models** (2026)
   - Adds a higher-level abstract latent as an auxiliary pretraining target to reduce compounding error in latent-space rollouts, aiming at longer-horizon coherence than multi-token or next-latent prediction.
   - <https://arxiv.org/abs/2608.05806>
6. **DASH: Divergence-Adaptive Supervision Horizons for On-Policy Self-Distillation of Reasoning Models** (2026)
   - Weights on-policy self-distillation supervision by how each local teacher-student divergence compares to the sequence mean, gating backward multi-step aggregation on that comparison.
   - <https://arxiv.org/abs/2608.06243>
7. **RP-OPSD: Reasoning-Pivot-Guided On-Policy Self-Distillation for Multilingual Reasoning Transfer** (2026)
   - Concentrates privileged self-distillation on reasoning pivots identified by the teacher's distributional shift when an English reference solution is added or removed, for multilingual reasoning transfer.
   - <https://arxiv.org/abs/2608.06347>
8. **SMART: Evaluating LLMs&apos; Mathematical Reasoning via a Human Cognitive Process-Inspired Benchmark** (2026)
   - Decomposes mathematical problem-solving into four cognitive dimensions after Polya and tests each separately, finding wide capability gaps that final-answer accuracy hides.
   - <https://doi.org/10.18653/v1/2026.acl-long.1638>
9. **VisAidMath: Benchmarking Visual-Aided Mathematical Reasoning** (2026)
   - Benchmarks whether multimodal models can construct visual aids for geometry problems, and finds high answer accuracy conceals near-total failure at producing or reasoning from those aids.
   - <https://doi.org/10.18653/v1/2026.acl-long.1719>
10. **Revisiting a Pain in the Neck: A Semantic Reasoning Benchmark for Language Models** (2026)
   - Consolidates multiword-expression resources into one evaluation suite covering idioms, noun compounds and verbal constructions across extraction, classification and interpretation tasks.
   - <https://doi.org/10.18653/v1/2026.acl-long.210>

## Open problems

Drawn from the limitations each paper states about itself, so this is what the field admits it cannot do yet.

- **When Is Benchmark Contamination Detectable? Information Limits and Power-Calibrated Audits** — The paper's own limitations section is unusually complete and should be read as part of the result. The mixture channel is an auditable modelling assumption rather than a law of training: contaminated examples can affect unexposed ones and post-training can alter both the clean and seen channels, and the stability diagnostics can reveal large violations but cannot prove transportability. The lower bound is pointwise in a chosen behavioural access channel and says nothing about direct corpus search, cryptographic provenance or watermarking. The matching optimality is local and assumes finite chi-square divergence. The certificate needs independent matched controls and a score learned on separate data, which an external auditor of a closed model generally cannot construct, so neither efficacy nor the exposed fraction is identified without extra assumptions. Six named gaps are open and unexecuted, including the locked external validation on the 25-model release that motivates the paper. A reader should add that the causal exposure claim rests on one base checkpoint (pythia-160m), one benchmark (SQuAD), one copy count and one protocol; that 'Pile-trained' does not certify the base never saw SQuAD, so only the incremental effect of the paired continuations is claimed; that the mechanism arms are not dose-matched, so the ordering is descriptive rather than a causal comparison; and that the three adjacent mechanism differences are significant per seed by sign-test but not after Holm correction.
- **Mitigating Scoring Bias in LLM-as-a-Judge via Random Number Generation** — No numeric margins in the abstract, and the models are not named. The method assumes a uniform distribution is the correct reference for a random-number request, which is a modelling choice rather than a fact about the intended judge behaviour. Rectification needs access to token generation probabilities, so it does not apply to judges behind APIs that do not expose logprobs. Bias varying by score range means a single measured distribution may not correct the tails.
- **Hierarchical Latent Prediction for Language Models** — No quantitative results, no named benchmarks, and no model scales in the abstract; the description of the abstract latent's construction and supervision is not given at this level of detail. Claims about belief-state coherence are asserted without a stated measurement. Being a pretraining-objective change, cost and any comparison at matched compute are unreported, which is the central question for a pretraining auxiliary loss.
- **DASH: Divergence-Adaptive Supervision Horizons for On-Policy Self-Distillation of Reasoning Models** — No effect sizes, benchmark names or model scales in the abstract, so the improvement is directional only. The baseline is the authors' own matched OPSD reruns, which is the right comparison but leaves the absolute standing against other dense-supervision methods unstated. Requires a privileged teacher. The sequence-level mean as the reference point makes each token's weight depend on the whole rollout, so weights are not available online during generation.
- **RP-OPSD: Reasoning-Pivot-Guided On-Policy Self-Distillation for Multilingual Reasoning Transfer** — No effect sizes, benchmark names or model scales in the abstract. The pivot proxy is defined by sensitivity to an English reference, so it presupposes English as the anchor and identifies pivots relative to that anchor rather than intrinsically. Restricted to mathematical reasoning. The claim that the method separates reasoning-control tokens from surface-realization tokens is an analysis of its own weights, not an independent validation.
- **Reasoning Errors Have a Region and a Direction in the Residual-Stream Trajectory of LLMs** — Improvements are stated as 'up to', so the typical gain is lower than 12%/21%. Benchmarks and models are not named in the abstract. Transfer to factual tasks supports a correctness signal but leaves open whether the signal is correctness or a correlate such as fluency or confidence. The detector needs white-box access to multi-layer activations, so it cannot monitor an API model.
- **Constraint-First Reasoning: A Training-Free Protocol for Exploiting Answer-Space Constraints in Mathematical Problem Solving** — Effect sizes are not given in the abstract. The benefit is explicitly conditional on the problem having recoverable constraints and on Stage 1 extracting them correctly, so it does not generalize to problems whose answer space is unconstrained. The router is a text-only regex, which bounds how well restrictive cues can be detected. Backbones are not named.
- **Self-Improving Large Language Models via Progressive Experience Evolution** — The conclusion's stated limitation is really future work — extending to domains with sparser or less reliable feedback. What a reader should weigh instead: the margin over GRPO is 0.75 to 1.92 average points with no seeds, variance or repeated runs reported anywhere, on five benchmarks two of which (AIME24/25 at 1.7B, at 5.21 and 7.71) are small enough that the average is carried by GSM8K and MATH500. The efficiency claim counts training trajectories and steps but not the extra forward passes spent extracting items, running the evolution operator, and scoring marginal utility on a probe set — so 28% fewer trajectories is not 28% less compute, and no wall-clock or FLOP accounting is given for Stage I. The main experiments use a single evolution round while the iteration study shows sampling accuracy still climbing at four, so the reported configuration is explicitly not the converged one. The extractor is the model being trained, which bounds experience quality by the current policy; the paper calls the items provisional hypotheses and filters them by utility, but never measures how often a wrong or misleading item survives the filter, nor what the acceptance threshold rejects. Everything is mathematics on one base-model family.
- **Beyond the Mean: Multi-Moment Policy Optimization for LLM Reasoning** — The paper states none. What a reader should weigh: the margins are 0.8 and 2.6 average points from single runs with no seeds or variance anywhere, and the reported figure is the best average across checkpoints evaluated every twenty steps — applied equally to all methods, but still a best-checkpoint protocol selected on the evaluation benchmarks rather than a held-out criterion. The truncation order T = 4 is likewise chosen by an ablation on the same model and benchmarks the headline table reports. The main results use the plug-in advantage estimator, which the authors say is generally biased; the unbiased leave-one-out estimator is derived in full and then not what produced the numbers. Scale is small — two base checkpoints under 4B, one training set, mathematics only, two GPUs — and the Schur-convexity result is a value judgement made explicit rather than a free improvement: the objective is designed to prefer evenly distributed success, and the bound on reweighting limits but does not eliminate the risk that buying tail coverage costs first-attempt accuracy, which is visible in the AIME columns at 1.7B.
- **Reinforcement Learning with Evolving Rubrics as Rewards for Audio Reasoning** — The paper has no limitations section. What a reader should weigh: the headline is a rubric method whose ablation attributes most of the movement to ordinary RL — 10.00 of 12.80 points on MMAU — with the entire rubric apparatus, static plus evolving plus length penalty, worth 2.80. The method also hinges on a strong proprietary generator and judge, and the paper shows it falling below plain GRPO when that is weakened, which makes the result conditional on a component the authors do not control and cannot release. Nothing accounts for the cost of that dependency: a judge call is issued per rubric per rollout per group per step, and no compute or wall-clock comparison against the GRPO baseline appears. Both reward weights are selected by sweeps on the same benchmarks the headline table reports. There is one policy backbone, one training corpus, greedy decoding only, and no seeds or variance anywhere. Finally, the claim that the rubrics make reasoning grounded in the audio is supported by accuracy on a perception split rather than by any direct check that the traces cite acoustic evidence — the mechanism is plausible and the measurement is still downstream accuracy.
- **Cloud-ScPO: Hidden-State Geometry for Semi-Supervised Preference Optimization in LLM Reasoning** — The paper has no limitations section. What a reader should weigh: the topological claim is validated qualitatively on Level 3 and Level 4 subsets of MATH with 200 points per cloud, and the appendix states directly that it should not be read as establishing the same pattern for every difficulty level or model configuration. The H1 (loop) signal is reported as exploratory and is not used in scoring at all, and the paper says it weakens after pooling and normalization. The mean-token versus last-token comparison in Table 5 uses different retention ratios, beta and learning rates, so it compares two whole pipelines rather than isolating the representation, which the paper acknowledges. The reference-bank ablation does not identify a single best configuration — M=100 with R=10 gives the best AUC at 67.02 while R=20 gives better extreme rankings — so the setting used for the main results is not the one that maximizes discrimination. Only one labeled-set size is tried (600 problems), only two datasets, and no cost accounting is given for the filtration and multi-bank scoring against a reward-model forward pass.
- **Your Reasoning Benchmark May Not Test Reasoning: Revealing Perception Bottleneck in Abstract Reasoning Benchmarks** — Three ARC-style datasets, so the conclusion is about this benchmark family. The perception stage's output is a natural-language description, so reasoning is evaluated over a lossy re-encoding — an upper bound on reasoning given perfect description is not the same as reasoning over the image. The 80% figure comes from manual inspection whose protocol, sample size and agreement are not given in the abstract. Models are not named.

## References

1. Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian et al.. *Training Verifiers to Solve Math Word Problems*. cs.LG. 2021 <https://arxiv.org/abs/2110.14168>
2. Guan Zhe Hong, Nishanth Dikkala, Enming Luo et al.. *A Implies B: Circuit Analysis in LLMs for Propositional Logical Reasoning*. NeurIPS 2025. 2025
3. Yang Yue, Zhiqi Chen, Rui Lu et al.. *Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?*. preprint. 2025
4. Chenxu Yang, Qingyi Si, Yongjie Duan et al.. *Dynamic Early Exit in Reasoning Models*. preprint. 2025
5. Yanxi Chen, Xuchen Pan, Yaliang Li et al.. *Provable Scaling Laws for the Test-Time Compute of Large Language Models*. NeurIPS. 2025
6. Xumeng Wen, Zihan Liu, Shun Zheng et al.. *Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs*. preprint. 2025
7. *Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking*. ICLR 2025. 2025
8. Jiayi Yuan, Hao Li, Xinheng Ding et al.. *Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference*. NeurIPS 2025. 2025
9. Luke Guerdan, Solon Barocas, Kenneth Holstein et al.. *Validating LLM-as-a-Judge Systems under Rating Indeterminacy*. NeurIPS 2025. 2025
10. Lisa Alazraki, Lihu Chen, Ana Brassard et al.. *AgentCoMa: A Compositional Benchmark Mixing Commonsense and Mathematical Reasoning in Real-World Scenarios*. ACL. 2026 <https://doi.org/10.18653/v1/2026.acl-long.380>
11. Xinyan Jiang, Ninghao Liu, Di Wang et al.. *Beyond Scalars: Evaluating and Understanding LLM Reasoning via Geometric Progress and Stability*. ICML. 2026
12. Jun Gao, Yun Peng, Qian Qiao et al.. *CoRE: A Fine-Grained Code Reasoning Benchmark Beyond Output Prediction*. ACL. 2026 <https://doi.org/10.18653/v1/2026.findings-acl.460>
13. Yuxuan Jiang, Dawei Li 0008, Francis Ferraro. *DRP: Distilled Reasoning Pruning with Mathematical Skill-aware Step Decomposition for Efficient Large Reasoning Models*. ACL. 2026 <https://doi.org/10.18653/v1/2026.findings-acl.196>
14. Yibo Yan, Shen Wang 0005, Jiahao Huo et al.. *ErrorRadar: Benchmarking Complex Mathematical Reasoning of Multimodal Large Language Models Via Error Detection*. ACL. 2026 <https://doi.org/10.18653/v1/2026.findings-acl.1217>
15. Lihao Sun, Hang Dong, Bo Qiao et al.. *LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals*. preprint. 2026
16. Yehua Lin, Liping Zheng, Yin Chen. *MAC-Reasoner: A Multi-Agent Collaborative Framework for Enhancing Logical Reasoning in Large Language Models*. ACL. 2026 <https://doi.org/10.18653/v1/2026.findings-acl.233>
17. Xiaoyuan Li 0001, Keqin Bao, Yubo Ma et al.. *MTR-Bench: A Comprehensive Benchmark for Multi-Turn Reasoning Evaluation*. ACL. 2026 <https://doi.org/10.18653/v1/2026.acl-long.984>
18. Yuandong Wang 0002, Yao Cui, Yuxin Zhao et al.. *MathSight: A Benchmark Exploring Have Vision-Language Models Really Seen in University-Level Mathematical Reasoning?*. ACL. 2026 <https://doi.org/10.18653/v1/2026.acl-long.2198>
19. *On The Fragility of Benchmark Contamination Detection in Reasoning Models*. ICLR 2026. 2026
20. Atharva Naik, Prakam, Yash Mathur et al.. *PBEBench: A Multi-Step Programming by Examples Reasoning Benchmark inspired by Historical Linguistics*. ACL. 2026 <https://doi.org/10.18653/v1/2026.findings-acl.432>
21. Subbarao Kambhampati, Karthik Valmeekam, Siddhant Bhambri et al.. *Position: Stop Anthropomorphizing Intermediate Tokens as Reasoning/Thinking Traces!*. ICML. 2026
22. Justin D. Norman, Michael U. Rivera, D. Alex Hughes. *Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias*. preprint. 2026
23. Yang Liu, Hongming Li, Melissa Xiaohui Qin et al.. *Revisiting a Pain in the Neck: A Semantic Reasoning Benchmark for Language Models*. ACL. 2026 <https://doi.org/10.18653/v1/2026.acl-long.210>
24. Yujie Hou, Mei Wang, Yaoyao Zhong et al.. *SMART: Evaluating LLMs&apos; Mathematical Reasoning via a Human Cognitive Process-Inspired Benchmark*. ACL. 2026 <https://doi.org/10.18653/v1/2026.acl-long.1638>
25. Longteng Guo, Xuanxu Lin, Dongze Hao et al.. *SciVQR: A Multidisciplinary Multimodal Benchmark for Advanced Scientific Reasoning Evaluation*. ACL. 2026 <https://doi.org/10.18653/v1/2026.findings-acl.28>
26. Yansi Li, Gongshen Liu, Zhuosheng Zhang 0001. *The Confidence Paradox: Unveiling the Latent Discriminative Power of Diffusion Large Language Models in Mathematical Reasoning*. ACL. 2026 <https://doi.org/10.18653/v1/2026.findings-acl.2142>
27. Huimin Xu, Shuai Zhao, Xiaobao Wu et al.. *Understanding and Preventing Entropy Collapse in RLVR with On-Policy Entropy Flow Optimization*. preprint. 2026
28. Jian Yao, Bowen Zheng, Ran Cheng et al.. *VAR-MATH: Probing True Mathematical Reasoning in LLMs via Symbolic Multi-Instance Benchmarks*. preprint. 2026
29. Jingkun Ma, Runzhe Zhan, Yang Li et al.. *VisAidMath: Benchmarking Visual-Aided Mathematical Reasoning*. ACL. 2026 <https://doi.org/10.18653/v1/2026.acl-long.1719>
30. Yingzhi Mao, Chunkang Zhang, Junxiang Wang et al.. *When Models Outthink Their Safety: Unveiling and Mitigating Self-Jailbreak in Large Reasoning Models*. ACL. 2026 <https://doi.org/10.18653/v1/2026.findings-acl.1118>
31. Xinhe Wang 0001, Jin Huang, Xingjian Zhang 0002 et al.. *Your Reasoning Benchmark May Not Test Reasoning: Revealing Perception Bottleneck in Abstract Reasoning Benchmarks*. ACL. 2026 <https://doi.org/10.18653/v1/2026.acl-long.826>
32. Yuzhou Liu, Xiyang Hu. *Cloud-ScPO: Hidden-State Geometry for Semi-Supervised Preference Optimization in LLM Reasoning*. cs.CL. 2026 <https://arxiv.org/abs/2608.01014>
33. Yijun Zhang, Yule Xie, Jiaxin Ding et al.. *Beyond the Mean: Multi-Moment Policy Optimization for LLM Reasoning*. cs.AI. 2026 <https://arxiv.org/abs/2608.02149>
34. Fangxu Yu, Tao Feng, Dehai Min et al.. *Reinforcement Learning with Evolving Rubrics as Rewards for Audio Reasoning*. cs.SD. 2026 <https://arxiv.org/abs/2608.02831>
35. Shijie Ren, Xiting Wang, Meng Li et al.. *Self-Improving Large Language Models via Progressive Experience Evolution*. cs.CL. 2026 <https://arxiv.org/abs/2608.02139>
36. Hongbo Ma, Bangji Yang, Yunqian Selina Cheng et al.. *Constraint-First Reasoning: A Training-Free Protocol for Exploiting Answer-Space Constraints in Mathematical Problem Solving*. cs.CL. 2026 <https://arxiv.org/abs/2608.05254>
37. ZhiYan Hou, Xinyu Tang, Hongyan An et al.. *DASH: Divergence-Adaptive Supervision Horizons for On-Policy Self-Distillation of Reasoning Models*. cs.AI. 2026 <https://arxiv.org/abs/2608.06243>
38. Chang Shi, Tim Pearce, Manan Tomar et al.. *Hierarchical Latent Prediction for Language Models*. cs.CL. 2026 <https://arxiv.org/abs/2608.05806>
39. Yuma Asato, Kiyoaki Shirai, Natthawut Kertkeidkachorn. *Mitigating Scoring Bias in LLM-as-a-Judge via Random Number Generation*. cs.CL. 2026 <https://arxiv.org/abs/2608.05726>
40. Yijiang Li, Bingyang Wang, Yijun Liang et al.. *On-Policy Self-Distillation without Any Supervision*. cs.LG. 2026 <https://arxiv.org/abs/2608.06296>
41. Xinye Wang, Junxiao Liu, Shujian Huang. *RP-OPSD: Reasoning-Pivot-Guided On-Policy Self-Distillation for Multilingual Reasoning Transfer*. cs.CL. 2026 <https://arxiv.org/abs/2608.06347>
42. Hamed Damirchi, Ignacio Meza De la Jara, Damith Ranasinghe et al.. *Reasoning Errors Have a Region and a Direction in the Residual-Stream Trajectory of LLMs*. cs.LG. 2026 <https://arxiv.org/abs/2608.05660>
43. Ruijie Hou, Yueyang Jiao, Zhao Wang et al.. *Zero Gap Is Not Restoration: Stratified Per-Question Probability Evaluation and Step-wise Mitigation of Benchmark Contamination*. cs.CL. 2026 <https://arxiv.org/abs/2608.07341>
44. Abhishek Panwar, Maheep Singh, Saksham Bansal. *Think Deep, Speak Once: Relit, A Recursive Latent Implicit Transformer Framework*. cs.AI. 2026 <https://arxiv.org/abs/2608.08113>
45. Rui Wang, Yeteng Wu, Xianling Zhang et al.. *VTO: Visual Tool Orchestration for Video Anomaly Detection*. cs.CV. 2026 <https://arxiv.org/abs/2608.08219>
46. Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma. *When Is Benchmark Contamination Detectable? Information Limits and Power-Calibrated Audits*. cs.AI. 2026 <https://arxiv.org/abs/2608.07914>
47. Rahma Simin Ali, Jawad Hossain. *MathShikkha: A Controlled Study of Answer-Only and Chain-of-Thought Supervision for Bangla Mathematical Reasoning in Small Language Models*. cs.AI. 2026 <https://arxiv.org/abs/2608.08503>
48. Haotian Wang, Lian Yan, Xingzhi Yao et al.. *MedCalc-R1: Knowledge-Guided Reward Framework for Medical Mathematical Reasoning*. cs.AI. 2026 <https://arxiv.org/abs/2608.08623>
49. Yangyang Feng, Zhuoyan Feng, Junlan Chen. *PAST: Privileged Adaptation from Complete Student Trajectories for On-Policy Self-Distillation*. cs.LG. 2026 <https://arxiv.org/abs/2608.08726>
50. Ting Zhou, Zhenqing Ling, Daoyuan Chen et al.. *Beyond Solvability: Task Learnability as a Static Prior for LLM RL Post-Training*. cs.LG. 2026 <https://arxiv.org/abs/2608.09217>
51. Zichao Yu, Chengzhi Yu, Shengze Xu et al.. *Mismatch Matters: On-Policy Distillation Beyond Token Agreement*. cs.AI. 2026 <https://arxiv.org/abs/2608.09836>
52. Di Wu, Xiaohui Zhu. *Post-Hoc Sparse Coding of Latent Communication Between Vision-Language Model Agents*. cs.AI. 2026 <https://arxiv.org/abs/2608.10198>
53. Yuanchi Zhu, Kang An, Tengyue Wang et al.. *SafeSceneReason: A Multimodal Reasoning Benchmark Connecting Industrial Hazards with Accident Knowledge*. cs.AI. 2026 <https://arxiv.org/abs/2608.09230>
54. Zhen Yang, Mengqi Wang, Gengda Zhao et al.. *Calibrating Post-Training Feature Shifts for LLM Data Contamination Detection*. cs.CL. 2026 <https://arxiv.org/abs/2608.10462>
55. Alicia Larsen, Victoire Laurent, Aulia Kharis Rakhamsari et al.. *V-FiLLM: Verified Financial LLM Reasoning Benchmark*. cs.AI. 2026 <https://arxiv.org/abs/2608.11047>
56. Zhixin Zhang, Xinke Jiang, Zhibang Yang et al.. *LoongReflect: Boosting Long-Horizon Reflection in Search Agents via Global Perspective Distillation*. cs.LG. 2026 <https://arxiv.org/abs/2608.11967>
