# Test-Time Scaling

_Lecture note assembled from the research archive_

> Generated on 2026-08-20 from 90 archived source(s).
> Regenerated on every render — put your own material in a separate file.

## Scope

What a model gains by thinking longer at inference: sampling and verification, search over reasoning steps, self-correction, and the length of the chain itself as a compute knob. The question the archive answers is how accuracy trades against tokens spent, and where that curve flattens.

Built from 90 paper(s) and 0 recording(s) spanning 2023-01-01 to 2026-08-12. 72 of the papers have been read in full.

Tracked terms: `chain of thought`, `chain of thought prompting`, `test-time compute`, `test-time scaling`, `inference-time scaling`, `inference-time compute`, `best of n`, `self-consistency`, `tree of thoughts`, `monte carlo tree search`, `self-refine`, `self-correction`, `self-verification`, `budget forcing`, `thinking budget`, `reasoning budget`, `extended thinking`, `overthinking`.

## Where the field stands

### 2026

- **Reinforcing Step-level Reasoning for Effective Self-Correction in LLMs** _(not yet summarized)_
- **Chain-of-Thought Shows the Path to a Tree: Realizing Branching Complexity** _(not yet summarized)_
- **Diagnosis Before Recovery: Turning Agent Failures into Selective Self-Correction** _(not yet summarized)_
- **Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling** _(not yet summarized)_
- **Claim-Level Reliability Assessment for Efficient Test-Time Reasoning** — Reallocates half of a test-time sampling budget from generating more solutions to asking the same model to refute a handful of decision-critical claims extracted from each trace, then weights the consensus vote by how many claims survive.
- **SCOUT: Unlocking Enhanced Spatial Reasoning via Structured Chain-of-Thought and Multi-Objective Process Reward** _(not yet summarized)_
- **ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling** — Injects a retrieved solved problem, with its full worked solution, into the middle of a reasoning model's own thinking trace at each step boundary, using the model's current intermediate answer as the retrieval query.
- **When Self-Consistency Backfires: Majority Vote Hurts the Majority of Hard Science Problems for Small LLMs** _(not yet summarized)_
- **Social Chain of Thought: A Multi-Agent Architecture Grounded in Medical Differential Diagnosis Methodology** _(not yet summarized)_
- **FaithformBench: Benchmarking Faithfulness of Mathematical Chain-of-Thought Autoformalisation** _(not yet summarized)_
- **XCoT-VLA: Executable Chain-of-Thought for Vision-Language-Action Driving** _(not yet summarized)_
- **Test-Time Augmentation for LLMs: When Input Diversity Beats Output Diversity at Matched Compute** — Asks whether a fixed inference budget buys more accuracy spent on varying the input than on varying the reasoning path, and finds paraphrase aggregation beats self-consistency on five of six benchmarks at matched compute.
- _...and 55 more._

### 2025

- **s1: Simple test-time scaling** — Reaches test-time scaling with two simple ingredients: supervised finetuning on 1,000 curated reasoning traces, and 'budget forcing', which controls thinking length by cutting generation off or appending 'Wait' to extend it.
- **DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning** — Shows that reasoning ability can be incentivized in an LLM by pure reinforcement learning on verifiable tasks, with no human-annotated reasoning trajectories, and that the resulting reasoning patterns can be transferred to smaller models.
- **Measuring Chain-of-Thought Monitorability Through Faithfulness and Verbosity** — Argues that faithfulness alone is insufficient for CoT monitoring and adds verbosity — whether the trace lists every factor needed to solve the task — combining the two into a monitorability score, then shows models can look faithful while omitting key factors.
- **Optimizing Test-Time Compute via Meta Reinforcement Fine-Tuning** — Formalizes 'spend test-time compute well' as a meta-reinforcement-learning problem — treating one long output stream as a sequence of episodes and scoring it by cumulative regret over tokens — and trains against a dense progress bonus that outcome-only reward cannot express.
- **Provable Scaling Laws for the Test-Time Compute of Large Language Models** — Gives two aggregation algorithms whose failure probability provably decays to zero as inference compute grows, assuming only that the model can sometimes be right and can compare two solutions better than chance.
- **Optimal Stopping vs Best-Of-N for Inference Time Optimization** — Casts each generation as opening a costly box in Weitzman's Pandora's Box problem and learns the optimal stopping threshold online, matching best-of-N quality with 15-35% fewer generations.
- **Transformers Provably Learn Chain-of-Thought Reasoning with Length Generalization** — Gives the first optimization guarantee that gradient descent trains constant-depth transformers to solve NC1-complete problems with chain of thought, and shows the algebraic structure of the task decides how far the learned reasoning extrapolates.
- **Efficiently Scaling LLM Reasoning with Certaindex** — Defines certaindex, an algorithm-agnostic measure of how much a reasoning algorithm's answer has stopped changing, and builds it into a serving system that reallocates or terminates compute per query — saving up to 50% of tokens in batch inference and tripling online throughput.
- **Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks in LLM Reasoning** — Tracks mutual information between each reasoning step's representation and the correct answer, finds it spikes at sparse 'MI peaks' that decode to reflective tokens like 'Wait' and 'Hmm', and shows suppressing exactly those tokens degrades reasoning while suppressing equally many others does not.
- **The Overthinker's DIET: Cutting Token Calories with DIfficulty-AwarE Training** — Trains reasoning models to be concise in proportion to difficulty by modulating the token penalty and the target length per problem, and fixes a distortion that naive reward weighting introduces into group-normalized RL.
- **On Reasoning Strength Planning in Large Reasoning Models** — Shows that a reasoning model decides how long to think before emitting a single reasoning token — the eventual token count is linearly decodable from the question's activations at Spearman 0.84 — and that this plan is carried by one shared direction vector whose magnitude encodes strength and which acts by shifting the logits of the end-of-thinking token.
- **Dynamic Early Exit in Reasoning Models** — Detects the points where a reasoning model switches thought chains, interrupts to induce a trial answer, and stops generation when that answer's confidence is high enough — cutting chain-of-thought length substantially while raising accuracy, with no training.
- _...and 3 more._

### 2024

- **Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters** — Studies how far a fixed model improves when given more inference compute, and shows that allocating that compute adaptively per prompt by difficulty beats a uniform best-of-N budget by more than 4x.
- **The Expressive Power of Transformers with Chain of Thought** — Characterizes exactly how much computational power a chain of thought buys as a function of its length, sandwiching the class of languages a decoder recognizes with t(n) decoding steps between two standard complexity classes.
- **Chain of Thought Empowers Transformers to Solve Inherently Serial Problems** — Proves a tighter no-CoT upper bound of AC^0 for constant-precision transformers, and shows T steps of chain of thought let a constant-depth model compute anything a size-T boolean circuit can.
- **Free Process Rewards without Process Labels** — Proves that parameterizing an outcome reward as the log-likelihood ratio between a policy and a reference model makes the per-step Q value fall out of the same model for free, so a process reward model can be obtained by training an outcome reward model on response-level labels alone.

### 2023

- **Measuring Faithfulness in Chain-of-Thought Reasoning** — Measures how much a model's answer actually depends on its stated chain of thought by intervening on the trace — adding mistakes, paraphrasing, truncating — and finds the dependence varies by task and decreases as models get larger.
- **Tree of Thoughts: Deliberate Problem Solving with Large Language Models** — Generalizes chain-of-thought into a search over a tree of intermediate 'thoughts', letting a model self-evaluate branches, look ahead and backtrack instead of committing to one left-to-right path.
- **Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting** — Shows that chain-of-thought explanations systematically misrepresent the real reason for a model's answer, by biasing inputs in ways the model never mentions and watching it rationalize the biased answer.
- **Towards Revealing the Mystery behind Chain of Thought: A Theoretical Perspective** — Proves via circuit complexity that bounded-depth Transformers cannot directly solve basic arithmetic, linear equations or general dynamic programming unless their size grows super-polynomially, while constant-size autoregressive Transformers can solve all of them by generating chain-of-thought derivations.

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

_Definition pending; a task is queued._

Seen in: Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting; Measuring Faithfulness in Chain-of-Thought Reasoning; Does Accuracy Equal Evidence? Reasoning Faithfulness under KV Cache Compression; How Much Does a Reasoning Summary Reveal? An Observability Ladder for Large Language Models.

### credit assignment

_Definition pending; a task is queued._

Seen in: BiCAA: Bidirectional Credit Assignment for Search-Augmented Agent; EviSD: Evidence-Conditioned Self-Distillation for Search-Augmented Agents; Latent Thought Credit: Multi-Answer Credit Assignment for Latent Reasoning; GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Time Latent Reasoning.

### verification

Deciding whether a candidate solution is correct, and the hinge on which most of this archive turns: RLVR needs it to compute a reward, test-time selection needs it to choose, and process supervision needs it per step. Sixteen sources supply it from four different places, ordered here by how much they can be trusted. An oracle — a compiler, unit tests, executable symbolic templates — is exact but exists only in some domains. A trained reward or process model is general and repeatedly found miscalibrated, which is why several archived methods are explicitly verifier-free. A model asked to judge is more general still and carries its own biases, though evaluator accuracy is shown to rise monotonically with the reasoning tokens it is given. And the model's own internal state can be read: a training-free comparison of a trace's start-to-end activation delta against two class centroids, or attention-routing alignment, both predict correctness without any external checker. One theoretical result reframes what is needed: pairwise comparison better than chance, not absolute correctness judgement, is enough to drive failure probability to zero.

Seen in: Training Verifiers to Solve Math Word Problems; DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning; Constraint-First Reasoning: A Training-Free Protocol for Exploiting Answer-Space Constraints in Mathematical Problem Solving; Thinking-Based Non-Thinking: Solving the Reward Hacking Problem in Training Hybrid Reasoning Models via Reinforcement Learning.

### adaptive compute allocation

_Definition pending; a task is queued._

Seen in: Test-Time Scaling for Safe Text-Guided Image Generation via Intermediate Clean Estimates; LatentGuard: Efficient and Inspectable Latent Reasoning for LLM Safeguards; Interpretable Adaptive Sampling for LLM Test-Time Scaling; Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility.

### prompt difficulty

How hard a specific problem is for a specific model, and the signal every adaptive-allocation method needs and estimates differently. Eleven sources supply it from: the model's own self-certainty; difficulty cues injected into an output prefix during fine-tuning; per-query token budgets derived from the model's own thinking responses; the solved-rate of sampled rollouts, where a uniformly-correct group wastes the batch; an item response theory model fitted over an evaluation matrix, which yields interpretable per-item difficulty; a Bayesian posterior over answer agreement; and activations taken before any reasoning token is emitted, from which the eventual token count is linearly decodable. That last result is the important one for this concept: the model has already estimated difficulty before it starts, so difficulty is available at no cost and the question is only whether a method reads it. Whether these seven estimators agree on which problems are hard is unmeasured.

Seen in: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters; Beyond the Mean: Multi-Moment Policy Optimization for LLM Reasoning; Interpretable Adaptive Sampling for LLM Test-Time Scaling; Beyond Solvability: Task Learnability as a Static Prior for LLM RL Post-Training.

### reasoning redundancy

The part of a chain of thought that does no work, and the quantity every efficiency method in this archive is trying to identify. Fifteen sources locate it differently — after the answer is derived, where double-checking continues; in tokens with negative marginal log-probability contribution to the correct answer; in segments the model's own likelihood landscape marks as extraneous; in the low-entropy convergence region after a sharp two-phase transition; in review nodes of a dependency graph that have too few descendants or sit too late; in steps receiving little attention from the reasoning-termination token; in later alternative solutions, argued to be actively harmful rather than merely wasteful; and in structure inherited from a teacher whose capacity did not match the student's. **This note previously recorded that no source compared these criteria on the same trace. One now does**, and the answer reframes the disagreement rather than settling it: at step granularity three importance criteria overlap 70-80% on which steps to *preserve* while diverging on which to *delete*, so the criteria converge on a shared reasoning backbone and differ only over interchangeable filler; at token granularity the agreement collapses, and only symbol-aware scoring avoids deleting operators and numbers. That study also refutes the premise several archived methods rest on, reporting that pruning which deliberately targets reflective statements performs no better than pruning that ignores them, because redundancy in long traces is diffuse — the skeleton is repeated and rephrased throughout rather than concentrated in a nameable class of step. Two caveats keep the question open: the comparison covers three generic scoring functions in a distillation setting, so the reasoning-specific criteria above are still untested against each other, and the 70-80% figure is a light-compression number that falls by half at aggressive ratios. Reported reductions run from roughly 40% to 87%, sometimes with accuracy gains.

Seen in: Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning; FoE: Forest of Errors Makes the First Solution the Best in Large Reasoning Models; Think Better, Not Longer: Token-Level Marginal Utility for Efficient Reasoning in Large Reasoning Models; Optimizing Length Compression in Large Reasoning Models.

### monitorability

_Definition pending; a task is queued._

Seen in: How Much Does a Reasoning Summary Reveal? An Observability Ladder for Large Language Models; Evading Chain-of-Thought Monitoring Through Model Poisoning; The Tell-Tale Trace: Detecting Reasoning Failures in LLMs Using Chain-of-Thought Dynamics; Risky Business: Measuring The Faithfulness-Safety Tension.

### entropy collapse

The failure mode in which a policy's output distribution becomes progressively more deterministic during reinforcement learning, eliminating exploration and saturating performance. At nine sources it has moved from a constraint the methods cite to an object several of them study, and they explain it differently. One attributes it to a covariance between log-probability and probability-weighted advantage that stays positive throughout training. One recasts it as an imbalance of flow, with entropy-decreasing tokens persistently outweighing entropy-increasing ones inside each update. One derives a bifurcation in second-order Renyi entropy at the policy's collision probability, so updating dominant tokens collapses entropy while updating long-tail tokens inflates it. One reduces the direction of change to the sign of a single scalar per token, and to that scalar's deviation from a policy-weighted baseline once a GRPO step is substituted in. A theoretical entry ties the remedies together, proving the classical entropy bonus relocates the optimum while covariance-targeted control is asymptotically unbiased once its coefficient is annealed. Two findings cut against the consensus: one source reports training entropy falling while accuracy improves, and another finds entropy tracks response diversity far more reliably than accuracy.

Seen in: BODHI: Do LLMs Branch Out and Discover Heterogeneous Inferences?; Don't Peek at the Answer: Outcome-Masked Group Relative Policy Optimization for Label-Free RLVR; When Correct Solutions Repeat: Rarity-Aware Credit Redistribution for GRPO; SeLaR: Selective Latent Reasoning in Large Language Models.

### process supervision

Supervising the steps rather than only the outcome, and a line the archive has watched become cheaper. The original obstacle was labels: step-level annotation is expensive, and the archive's sources have now routed around it four ways. It falls out of an outcome reward for free — parameterizing that reward as a policy-to-reference log-likelihood ratio makes the per-step Q value the partial sum, so a process reward model comes from response-level labels alone. It can be borrowed from a privileged teacher, with the token-level teacher-student divergence as the dense signal, then aggregated to turns or concentrated on pivots. It can be read from the model's own trajectory, via entropy instability or state-transition probabilities. And it can be executed, where symbolic templates or an interpreter supply step-level ground truth at no annotation cost. What remains contested is how much it adds: one archived theoretical account argues that if pretraining already separates correct from incorrect chains, an outcome-only gradient inherits that separation, which would explain why process supervision sometimes buys little.

Seen in: CURV: Enhancing Chart Understanding Through Curriculum Visual Grounded Reasoning; Perception Before Reasoning: Dynamic Latent Reasoning for Video Understanding and Question Answering; AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning; DASH: Divergence-Adaptive Supervision Horizons for On-Policy Self-Distillation of Reasoning Models.

## Methods

| Method | Sources | Summary |
| --- | ---: | --- |
| GRPO | 40 | _pending_ |
| LLM-as-a-judge | 33 | _pending_ |
| supervised fine-tuning | 33 | Training on input-output pairs, and in these sources specifically on reasoning traces. What 27 sources collectively show is how little of it is needed and how much depends on wh... |
| linear probe | 25 | A linear classifier or regressor fitted to a model's internal activations to test whether some property is linearly decodable from them — used across these 22 sources both as a... |
| RLVR | 24 | Training against an automatically checkable outcome signal — a correct final answer, a passing test — rather than a learned reward model, which removes reward-model gaming as a... |
| chain of thought | 23 | Emitting intermediate tokens before an answer, and the object almost everything in this archive is about — now with a theoretical account of why it works. Twenty sources use it... |
| self-consistency | 20 | _pending_ |
| test-time scaling | 19 | _pending_ |
| chain-of-thought prompting | 18 | _pending_ |
| activation patching | 17 | A three-pass causal test: run a clean prompt with a known answer and cache the activations of chosen components, run a corrupted or contrasting prompt, then restore one cached a... |
| pass@k | 16 | _pending_ |
| activation steering | 15 | Adding a signed multiple of a fixed direction to the residual stream at inference so behaviour changes without retraining; the direction is usually a mean difference between act... |
| best-of-n | 14 | Generating N candidates and keeping the one a verifier scores highest, the archive's standard selection baseline — and one with a known failure direction. With an imperfect veri... |
| majority voting | 13 | Returning the most frequent answer among sampled trajectories, counting every trajectory equally. The sources treat it as the aggregation floor and report it is hard to beat out... |
| calibration | 11 | Whether a model's stated confidence matches its actual accuracy, and a property the archive has learned to split in two. The distinction comes from a diffusion language model me... |
| PPO | 11 | The clipped-surrogate policy-gradient algorithm the RLVR methods here descend from. It is rarely run directly in these sources; what carries over is its clipping mechanism, whic... |
| LoRA | 10 | Fine-tuning by learning low-rank updates to frozen weights instead of all parameters. Neither source studies it; both use it as the cheap adaptation that makes their comparison... |
| sparse autoencoder | 10 | An autoencoder trained to reconstruct a model's internal activations through a wider hidden layer under a sparsity penalty, so its rows form an overcomplete dictionary and any a... |
| process reward model | 9 | _pending_ |
| circuit analysis | 8 | Identifying a subset of model components — attention heads, neurons — and the information flow between them that accounts for a behaviour. The archived sources use it at three s... |

## Benchmarks and datasets

| Dataset / benchmark | Sources | Summary |
| --- | ---: | --- |
| MATH500 | 43 | A 500-problem subset of MATH, used across 39 sources as the mid-difficulty mathematics reference — large enough that a few items do not move the number, and easy enough that str... |
| AIME 2024 | 42 | The 2024 American Invitational Mathematics Examination, and the archive's single most-used benchmark at 39 sources — which is itself the thing to know about it. Its 30 problems... |
| GSM8K | 35 | _pending_ |
| AIME 2025 | 30 | The 2025 American Invitational Mathematics Examination, used across 26 sources as AIME 2024's companion and, increasingly, as a contamination control — it postdates the training... |
| AMC23 | 16 | The 2023 American Mathematics Competitions problems, used in the archive as the rung below AIME — harder than MATH500, easier than AIME, and small. It appears mostly in entropy... |
| GPQA-Diamond | 14 | A set of graduate-level multiple-choice questions in biology, chemistry and physics, used across these sources as the hard non-mathematical benchmark and as the place where math... |
| OlympiadBench | 13 | An olympiad-level mathematics benchmark and, at eleven sources, the most-cited evaluation set in this archive after the AIME pair. It functions as the stable member of the stand... |
| MATH | 12 | The competition-mathematics benchmark, cited here in its full form rather than the 500-problem subset that appears separately in this archive. The sources use it as a mid-to-har... |
| DAPO-Math-17K | 9 | The 17k-problem mathematics training set released with DAPO, and the default RLVR training data across these sources — which makes their results more comparable than they would... |
| LiveCodeBench | 9 | A contamination-resistant code benchmark built from recently released problems, used in these sources mainly as the out-of-domain test for models trained on mathematics. It prod... |
| MMLU | 9 | A broad multiple-choice knowledge benchmark spanning many subjects. In this archive it is a transfer and measurement target rather than a reasoning benchmark in its own right: o... |
| Minerva | 8 | A mathematics benchmark of undergraduate and quantitative-reasoning problems, appearing in all four sources as part of the standard six-benchmark RLVR evaluation suite. It is co... |
| MMLU-Pro | 7 | A harder, more reasoning-oriented revision of MMLU, used in the archive as a multiple-choice knowledge-and-reasoning benchmark outside mathematics. Both sources use it as a brea... |
| GPQA | 5 | A graduate-level science question benchmark, used in the archive as the non-mathematical hard reference alongside competition math. Both sources use it to test whether a method... |
| Omni-MATH | 5 | A competition-level mathematics benchmark, reported by both sources only as one of the held-out evaluation sets in reinforcement learning experiments on verifiable mathematics.... |
| BBH | 4 | A multi-task reasoning benchmark that the sources use as the legible, non-frontier end of an evaluation suite rather than as a hard test. One finds dataset difficulty inversely... |
| HMMT | 4 | A competition-mathematics contest whose problem sets both sources use as evaluation alongside AIME. One includes it among five mathematics benchmarks on which a categorical-crit... |
| HumanEval+ | 4 | A Python function-completion benchmark verified by executing unit tests, used in the archive as the code counterpart to its mathematics benchmarks. Execution-based verification... |
| AIME 2026 | 3 | The 2026 edition of the competition-mathematics examination, and in both sources the newest set — the one whose value comes from postdating the training of the models being eval... |
| AMC | 3 | A competition mathematics benchmark, used by both sources purely as an evaluation set reported alongside AIME and MATH500. Neither describes its contents, size or construction,... |

## Reading path

**Start here** — the anchor papers for this topic:

1. 2408.03314
1. 2501.19393
1. 2305.10601

**Then, in order of relevance:**

1. **Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting** (2023)
   - Shows that chain-of-thought explanations systematically misrepresent the real reason for a model's answer, by biasing inputs in ways the model never mentions and watching it rationalize the biased answer.
   - <https://arxiv.org/abs/2305.04388>
2. **ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling** (2026)
   - Injects a retrieved solved problem, with its full worked solution, into the middle of a reasoning model's own thinking trace at each step boundary, using the model's current intermediate answer as the retrieval query.
   - <https://arxiv.org/abs/2608.10928>
3. **Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning** (2026)
   - Spends test-time compute on iteratively refining each sampled rollout rather than on drawing more of them, then majority-votes the refined answers, with no verifier.
   - <https://arxiv.org/abs/2608.05643>
4. **It's the Decoding Format, Not the Perturbation: Auditing Consistency-Based Selection for Vision-Language Test-Time Scaling** (2026)
   - Shows that a perturbation-based selection rule's apparent 31.8-point gain over majority voting in vision-language test-time scaling is a decoding-format effect, by adding a control that spends the same short-answer budget on the unperturbed image and finds it matches or beats the perturbation rule everywhere.
   - <https://arxiv.org/abs/2608.01207>
5. **s1: Simple test-time scaling** (2025)
   - Reaches test-time scaling with two simple ingredients: supervised finetuning on 1,000 curated reasoning traces, and 'budget forcing', which controls thinking length by cutting generation off or appending 'Wait' to extend it.
   - <https://arxiv.org/abs/2501.19393>
6. **Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters** (2024)
   - Studies how far a fixed model improves when given more inference compute, and shows that allocating that compute adaptively per prompt by difficulty beats a uniform best-of-N budget by more than 4x.
   - <https://arxiv.org/abs/2408.03314>
7. **Tree of Thoughts: Deliberate Problem Solving with Large Language Models** (2023)
   - Generalizes chain-of-thought into a search over a tree of intermediate 'thoughts', letting a model self-evaluate branches, look ahead and backtrack instead of committing to one left-to-right path.
   - <https://arxiv.org/abs/2305.10601>
8. **Test-Time Augmentation for LLMs: When Input Diversity Beats Output Diversity at Matched Compute** (2026)
   - Asks whether a fixed inference budget buys more accuracy spent on varying the input than on varying the reasoning path, and finds paraphrase aggregation beats self-consistency on five of six benchmarks at matched compute.
   - <https://arxiv.org/abs/2608.09351>
9. **Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings** (2026)
   - The first benchmark comparing CoT monitorability under explicit versus implicit influence, finding detection falls 41-46 points when the prompt never instructs the model to hide anything.
   - <https://arxiv.org/abs/2608.04735>
10. **Interpretable Adaptive Sampling for LLM Test-Time Scaling** (2026)
   - Allocates test-time samples per prompt with a fuzzy controller over human-readable difficulty and confidence signals, and — under a selector-matched protocol that isolates the budget policy from the answer selector — reports the result honestly as an accuracy-compute tradeoff rather than an accuracy gain.
   - <https://arxiv.org/abs/2608.03961>

## Open problems

Drawn from the limitations each paper states about itself, so this is what the field admits it cannot do yet.

- **Claim-Level Reliability Assessment for Efficient Test-Time Reasoning** — The paper's own scope limits are stated in the method rather than a section. CLR only reweights already-parsed candidates, so it cannot recover a correct answer absent from the Stage-1 samples -- it converts candidate coverage into better selection and nothing more. Request parity does not imply token parity, and on the model where accuracy gains are largest the token cost rises by up to 47.8 percent, so 'matched budget' means matched calls. The exponent M in the score is a heuristic monotone transform, not a joint correctness probability, and does not assume claim independence. The M ablation jointly varies claim count, score resolution and penalty sharpness, because M is both the number of claims and the exponent, so it does not isolate claim count. What a reader should add: this is a workshop paper, and every benchmark is competition mathematics with a parseable short answer, so the equivalence-group construction that the aggregation depends on is doing easy work here. The headline framing rests on GPT-OSS-20B/CMIMC25 while the same model regresses on HMMT25 and the near-saturated Qwen3.5-27B gains almost nothing, so the benefit is conditional on the base consensus being unreliable -- which the paper says, but the abstract does not. Ties, including the all-zero-score case where every trace has a refuted claim, fall back to the earliest equivalence group in sampling order, and how often that fires is not reported.
- **ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling** — No limitations section in the material read. What a reader should weigh first is the retrieval encoder: the related-work section cites a result that structurally faithful retrieval over mathematics is hard with off-the-shelf encoders, and the method then uses an off-the-shelf E5-Large, with the encoder choice relegated to an ablation. Second, decontamination is by cosine similarity at 0.90 and the audit reports maximum retained similarities of 0.898 and 0.891 -- immediately below the cut, with mean retained similarities of 0.866 and 0.845, which the paper attributes to the structural density of synthetic math corpora rather than leakage, and defends with an answer-distinct retrieval control rather than with a lower threshold. Third, the headline gains sit on AIME 2025, which is 30 problems, so +13.4 is four problems even at three seeds. Fourth, three of the four benchmarks share the same NuminaMath bank and the fourth uses its own training split, so 'adapts to different example banks' rests on one swap, and nothing here tests a domain where a bank of solved problems does not exist. Finally, the entropy reduction is offered as the explanation of the gain but is measured alongside it rather than manipulated, so it is a correlate of the improvement and not shown to cause it.
- **Test-Time Augmentation for LLMs: When Input Diversity Beats Output Diversity at Matched Compute** — The paper is unusually direct about scope: it states that gains of 1-2 pp may not justify a 2-6x cost increase, and that TTA is most valuable when baseline accuracy is moderate (40-80%). Two of its six benchmarks fall outside that band and show it -- IMDB at 94.5% where all three methods return an identical +1.00, and HLE at 3.0% where a +0.75 pp gain on 400 examples is three questions. What a reader should add: the main results use one base model, so 'input diversity beats output diversity' is established for Claude 4.5 Haiku and the model-scale section is an ablation rather than a replication. The 1.8x cost-effectiveness figure in the abstract is not either of the two ratios the figure reports -- accuracy per dollar is 1.45x and per LLM call is 1.93x -- so the headline number should be traced to the intended denominator before quoting. k is chosen per dataset and method by grid search, which is the right protocol but means the reported k differs across arms of the comparison. And the crossing at k = 10 on Math500 undercuts the framing more than the paper says: if self-consistency catches up given enough samples, input diversity is buying convergence speed rather than a higher ceiling, which is a different claim from the one in the title.
- **Persistent Semantic Entities in Tool-Augmented LLM Systems** — Stated: the panel mixes inference backends (local, vendor APIs, OpenRouter), so rates are per-condition characterisations rather than vendor leaderboards, and cross-provider testing covers Llama-3.1-8B only. Persistence is measured only to turn 10, at temperature 0, on one model, and the authors claim neither unbounded persistence nor cross-family generality. Scenarios are synthetic by design in order to isolate (N,T,P), and the AutoGPT case study is a mechanism-level reconstruction from documented behaviour rather than an observed incident -- the authors state they have not executed the chain against a deployed instance and that their citation supports only that plugins can run arbitrary code and register handlers. The LLM judge (Gemini-2.0-Flash-Lite) is not independent of a panel that includes Google models, so the authors ask that rates be read as relative comparisons rather than absolute estimates. Several results are withdrawn rather than defended: an earlier factorial on uncontaminated settings is stated qualitatively because its run-level artifact was not released, and the utility and half-life columns plus three remediation operators carried in earlier versions are withdrawn as unrecoverable from released artifacts, with no Pareto-dominance claim made. Not stated but worth noticing: sample sizes are small where the strongest claims sit -- the temporal persistence table rests on n=10 seeds per cell, and the defence panel on n=20 -- so several headline percentages carry confidence intervals wide enough to overlap; the remediation operator comparison rests on 9 trials each; and the paper's own framing that name binding is 'dominant' is in tension with its admission that the ablation makes N necessary partly by construction.
- **Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning** — The reported gains are concentrated on small open-weight models, and the headline example is a 1.5B model; whether refinement still beats resampling when the base model is strong enough to have little to repair is not established here. Compute is not obviously matched — refining each of N rollouts costs more than generating N, so a compute-matched comparison against a larger N is the control the abstract does not report. It also depends on self-critique being informative, which arxiv:2608.04355 argues is largely a format effect at small-to-mid scale.
- **Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings** — The 41-46 point drop is reported for two of four settings, so the effect is not uniform across task formats and the other two are not characterized in the abstract. Nudges are constructed, and their strength relative to real deployment biases is unknown. Detection depends on the monitor used, so the numbers bound this monitor rather than monitorability in general.
- **The Calibration Floor: Format Repair Can Masquerade as Self-Correction at Small-to-Mid Scale** — The frontier arm is stated to be lower-powered. Two large-effect cells retain an unexplained residual after grammar-constrained decoding. The calibration-floor argument identifies a squeeze rather than a remedy: floor-scale models have headroom but not enough signal, capable-scale models have signal but little headroom, so the design space where self-correction could be measured cleanly is nearly empty. Scope is answer-extractable tasks; the decomposition does not apply where there is no parseable answer field.
- **ODRA: Synthesizing Cognitive Behavioral Therapy Sessions with Structured Chain-Of-Thought and Dynamic Patient Resistance** — No numeric margins are given for the automated evaluations; the headline evidence is a preference count over 13 metrics. Expert preference is not reported with inter-rater agreement or the number of psychologists. Downstream validation is against simulated patients, not human ones, so the claim that explicit resistance modelling transfers to clinical robustness is established only within simulation.
- **Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning** — 'Largely preserving accuracy' is not quantified in the abstract, so the accuracy cost of the 37-65% token reduction is unstated. Models and benchmarks are not named. The process-reward estimator is an additional component whose own cost and calibration are not reported, and the claim that deleting tokens at high-reward steps is safer rests on that estimator being right about which steps are high-reward.
- **Interpretable Adaptive Sampling for LLM Test-Time Scaling** — The paper is candid about most of this in the text. The accuracy differences are within overlapping marginal confidence intervals, and the authors note that a paired test would require matched per-prompt correctness logs which they do not report — so the small negative deltas are not established as real losses any more than the small positive one is a real gain. The component ablation shows individual signals are not validated: some removals help, which means the interpretability claim is about the controller's structure being auditable, not about its signals being the right ones. The fair-alignment protocol disables the draft pass and fixes decoding, so the evaluated configuration is deliberately weaker than the full system and the reported savings are a lower bound on what the full method would do and an upper bound on how cleanly it can be attributed. Scale is two small instruction-tuned models with a maximum budget of eight and a 256-token output cap, which bounds both the difficulty of the problems and the room for allocation to matter. The factual-QA numbers are acknowledged to be depressed by strict exact-match scoring. Nothing is reported about the controller's own compute cost against the samples it saves.
- **Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility** — The paper is a formalization and a resource rather than a claim about which method is best, and it says so throughout — the empirical numbers are described as descriptive properties of the specific configurations measured, not as general small-sample guarantees. What a reader should hold: the taxonomy's regimes are explicitly not mutually exclusive, since most practical systems are hybrids of prefix search followed by a leaf-level reducer, so classifying a real system still requires judgement. The repeated-sampling diagnostics have their independent-attempt interpretation only when the bank comes from independent draws of a declared fixed proposal; for banks produced by adaptive search or dependent procedures they remain descriptive summaries of what was returned, which the paper states and which most papers reporting pass@k do not. The released banks are large but fixed, so any reducer evaluated on them inherits whatever the generating protocols produced. And the prescriptions — protocol-consistent uncertainty propagated through the aggregation rule, declaration of budget, temperature, evidence map, stopping and extraction rules before outcomes are inspected — are normative requirements the paper argues for rather than empirical findings, and it does not measure how often current work violates them.
- **Test-Time Scaling for Safe Text-Guided Image Generation via Intermediate Clean Estimates** — The paper states them: the method inherits whatever ambiguity its vision-language safety encoder has, and it updates the conditioning from the safety signal at the detected timestep without directly optimizing preservation of the original prompt or the quality of the final image — so it can under-suppress indirect attacks, or over-suppress benign attributes and reduce semantic fidelity when the update is stronger. A reader should add that the multi-concept degradation is measured and not solved, and that safety is evaluated by an automatic detector and a model judge rather than by human review, so the reported detection rates inherit those instruments' errors. Two backbones, both from one family, and no seeds or variance are reported.

## References

1. Guhao Feng, Bohang Zhang, Yuntian Gu et al.. *Towards Revealing the Mystery behind Chain of Thought: A Theoretical Perspective*. NeurIPS 2023. 2023
2. Miles Turpin, Julian Michael, Ethan Perez et al.. *Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting*. cs.CL. 2023 <https://arxiv.org/abs/2305.04388>
3. Shunyu Yao, Dian Yu, Jeffrey Zhao et al.. *Tree of Thoughts: Deliberate Problem Solving with Large Language Models*. cs.CL. 2023 <https://arxiv.org/abs/2305.10601>
4. Tamera Lanham, Anna Chen, Ansh Radhakrishnan et al.. *Measuring Faithfulness in Chain-of-Thought Reasoning*. cs.AI. 2023 <https://arxiv.org/abs/2307.13702>
5. Zhiyuan Li, Hong Liu, Denny Zhou et al.. *Chain of Thought Empowers Transformers to Solve Inherently Serial Problems*. preprint. 2024
6. Lifan Yuan, Wendi Li, Huayu Chen et al.. *Free Process Rewards without Process Labels*. preprint. 2024
7. William Merrill, Ashish Sabharwal. *The Expressive Power of Transformers with Chain of Thought*. ICLR. 2024
8. Charlie Snell, Jaehoon Lee, Kelvin Xu et al.. *Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters*. cs.LG. 2024 <https://arxiv.org/abs/2408.03314>
9. Junnan Liu, Hongwei Liu, Linchen Xiao et al.. *Deciphering Trajectory-Aided LLM Reasoning: An Optimization Perspective*. preprint. 2025
10. Chen Qian, Dongrui Liu, Haochen Wen et al.. *Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks in LLM Reasoning*. preprint. 2025
11. Yang Yue, Zhiqi Chen, Rui Lu et al.. *Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?*. preprint. 2025
12. Chenxu Yang, Qingyi Si, Yongjie Duan et al.. *Dynamic Early Exit in Reasoning Models*. preprint. 2025
13. Yichao Fu, Junda Chen, Siqi Zhu et al.. *Efficiently Scaling LLM Reasoning with Certaindex*. preprint. 2025
14. Austin Meek, Eitan Sprejer, Iván Arcuschin et al.. *Measuring Chain-of-Thought Monitorability Through Faithfulness and Verbosity*. preprint. 2025
15. Leheng Sheng, An Zhang, Zijian Wu et al.. *On Reasoning Strength Planning in Large Reasoning Models*. NeurIPS 2025. 2025
16. Yusuf Kalayci, Vinod Raman, Shaddin Dughmi. *Optimal Stopping vs Best-Of-N for Inference Time Optimization*. preprint. 2025
17. Yuxiao Qu, Matthew Y. R. Yang, Amrith Setlur et al.. *Optimizing Test-Time Compute via Meta Reinforcement Fine-Tuning*. ICML 2025. 2025
18. Yanxi Chen, Xuchen Pan, Yaliang Li et al.. *Provable Scaling Laws for the Test-Time Compute of Large Language Models*. NeurIPS. 2025
19. *The Overthinker's DIET: Cutting Token Calories with DIfficulty-AwarE Training*. NeurIPS 2025. 2025
20. Yu Huang, Zixin Wen, Aarti Singh et al.. *Transformers Provably Learn Chain-of-Thought Reasoning with Length Generalization*. NeurIPS. 2025
21. Jiayi Yuan, Hao Li, Xinheng Ding et al.. *Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference*. NeurIPS 2025. 2025
22. DeepSeek-AI, Daya Guo, Dejian Yang et al.. *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning*. Nature volume 645, pages 633-638 (2025). 2025 <https://arxiv.org/abs/2501.12948>
23. Niklas Muennighoff, Zitong Yang, Weijia Shi et al.. *s1: Simple test-time scaling*. cs.CL. 2025 <https://arxiv.org/abs/2501.19393>
24. Xingjian Diao, Zheyuan Liu 0010, Chunhui Zhang et al.. *Addressing Overthinking in Large Vision-Language Models via Gated Perception-Reasoning Optimization*. ACL. 2026 <https://doi.org/10.18653/v1/2026.findings-acl.215>
25. Zhiyuan Hu, Yibo Wang, Hanze Dong et al.. *Beyond &apos;Aha!&apos;: Toward Systematic Meta-Abilities Alignment in Large Reasoning Models*. ACL. 2026 <https://doi.org/10.18653/v1/2026.findings-acl.1981>
26. Xinyan Jiang, Ninghao Liu, Di Wang et al.. *Beyond Scalars: Evaluating and Understanding LLM Reasoning via Geometric Progress and Stability*. ICML. 2026
27. Daniel Scalena, Sara Candussio, Luca Bortolussi et al.. *Beyond the Commitment Boundary: Probing Epiphenomenal Chain-of-Thought in Large Reasoning Models*. preprint. 2026
28. Qizhi Jiang, Shuo Wang, Pei Ke et al.. *CAT: Confidence-Adaptive Thinking for Efficient Reasoning of Large Reasoning Models*. ACL. 2026 <https://doi.org/10.18653/v1/2026.acl-industry.152>
29. Yangsong Lan, Hongliang Dai, Piji Li. *CRISP: Compressing Redundancy in Chain-of-Thought via Intrinsic Saliency Pruning*. ACL 2026 Findings. 2026
30. Jiaxuan Zou, Yaozhong Xiong, Yong Liu. *Capabilities and Fundamental Limits of Latent Chain-of-Thought*. preprint. 2026
31. Chenghua Zhu, Siyan Wu, Xiangkang Zeng et al.. *EDIS: Diagnosing LLM Reasoning via Entropy Dynamics*. preprint. 2026
32. Zhuohan Xie, Daniil Orel, Rushil Thareja et al.. *FinChain: A Symbolic Benchmark for Verifiable Chain-of-Thought Financial Reasoning*. ACL. 2026 <https://doi.org/10.18653/v1/2026.acl-long.662>
33. Hongyuan Yuan, Xinran He, Run Shao et al.. *Graph-Based Chain-of-Thought Pruning for Reducing Redundant Reflections in Reasoning LLMs*. ACL 2026 Findings. 2026
34. Lihao Sun, Hang Dong, Bo Qiao et al.. *LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals*. preprint. 2026
35. Zhanke Zhou, Zhaocheng Zhu, Xuan Li et al.. *Landscape of Thoughts: Visualizing the Reasoning Process of Large Language Models*. ICLR 2026. 2026
36. Dennis Wei, Yannis Belkhiter, Erik Miehling et al.. *Local Causal Attribution of Chain-of-Thought Reasoning*. Mechanistic Interpretability Workshop at ICML 2026. 2026
37. Guoming Ling, Zhongzhan Huang, Yupei Lin et al.. *Neural Chain-of-Thought Search: Searching the Optimal Reasoning Path to Enhance Large Language Models*. ACL. 2026 <https://doi.org/10.18653/v1/2026.findings-acl.1149>
38. Mohammed Ehab, Aymane El Gadarri, Vivek Farias et al.. *OS-Pruner: Pruning Chains-of-Thought of Reasoning Models via Optimal Stopping*. preprint. 2026
39. Jingkai Huang, Will Ma, Zhengyuan Zhou. *Optimal Bayesian Stopping for Efficient Inference of Consistent LLM Answers*. ICML. 2026
40. Atharva Naik, Prakam, Yash Mathur et al.. *PBEBench: A Multi-Step Programming by Examples Reasoning Benchmark inspired by Historical Linguistics*. ACL. 2026 <https://doi.org/10.18653/v1/2026.findings-acl.432>
41. Subbarao Kambhampati, Karthik Valmeekam, Siddhant Bhambri et al.. *Position: Stop Anthropomorphizing Intermediate Tokens as Reasoning/Thinking Traces!*. ICML. 2026
42. *RADAR: Reasoning-Ability and Difficulty-Aware Routing for Reasoning LLMs*. ICLR 2026. 2026
43. Jens Tuyls, Dylan J. Foster, Akshay Krishnamurthy et al.. *Representation-Based Exploration for Language Models: From Test-Time to Post-Training*. ICLR 2026. 2026
44. Seungone Kim, Ian Wu, Jinu Lee 0001 et al.. *Scaling Evaluation-Time Compute with Reasoning Models as Evaluators*. ACL. 2026 <https://doi.org/10.18653/v1/2026.findings-acl.2102>
45. Xuan Yang, Jiayu Liu, Yuhang Lai et al.. *Step-Level Sparse Autoencoder for Reasoning Process Interpretation*. ICML 2026 (Proceedings of the 43rd International Conference on Machine Learning, PMLR 306). 2026
46. Jinyang Zhang, Hongxin Ding, Yue Fang et al.. *The Tell-Tale Norm: L2 Magnitude as a Signal for Reasoning Dynamics in Large Language Models*. preprint. 2026
47. Jiawei Li 0020, Yang Gao 0016, Huashan Sun et al.. *Think Better, Not Longer: Token-Level Marginal Utility for Efficient Reasoning in Large Reasoning Models*. ACL. 2026 <https://doi.org/10.18653/v1/2026.acl-long.1386>
48. Yongjiang Liu, Haoxi Li, Xiaosong Ma et al.. *Think How to Think: Mitigating Overthinking with Autonomous Difficulty Cognition in Large Reasoning Models*. ACL. 2026 <https://doi.org/10.18653/v1/2026.acl-long.1766>
49. Siyuan Gan, Jiaheng Liu, Boyan Wang et al.. *Thinking-Based Non-Thinking: Solving the Reward Hacking Problem in Training Hybrid Reasoning Models via Reinforcement Learning*. ACL. 2026 <https://doi.org/10.18653/v1/2026.acl-long.2122>
50. Yixiao Huang, Hanlin Zhu, Zixuan Wang et al.. *Transformers Provably Learn to Internalize Chain-of-Thought*. preprint. 2026
51. Ting Xu, Xu He, Yupu Lu et al.. *Unveiling the Entropy Dynamics of Chain-of-Thought Reasoning*. ICML 2026 (Proceedings of the 43rd International Conference on Machine Learning, PMLR 306). 2026
52. Ahsan Bilal, Muhammad Ahmed Mohsin, Muhammad Umer et al.. *What If We Allocate Test-Time Compute Adaptively?*. ICML 2026 (Proceedings of the 43rd International Conference on Machine Learning, PMLR 306). 2026
53. Siyang Lyu, Zhijing Sun, Xinghao Chen et al.. *When Compression Helps and When It Hurts: Condition-Aware Analysis of Chain-of-Thought Distillation*. preprint. 2026
54. Zi-Ao Ma, Xian-Ling Mao, Tian Lan 0003 et al.. *Your Reasoning Model Knows What Counts: Self-Guided Chain-of-Thought Pruning for Efficient Reasoning*. ACL. 2026 <https://doi.org/10.18653/v1/2026.acl-long.25>
55. Puzhuo Zheng, Hasan Kurban. *It's the Decoding Format, Not the Perturbation: Auditing Consistency-Based Selection for Vision-Language Test-Time Scaling*. cs.CV. 2026 <https://arxiv.org/abs/2608.01207>
56. Xuehang Guo, Pingyue Zhang, Ruiyi Zhang et al.. *CURV: Enhancing Chart Understanding Through Curriculum Visual Grounded Reasoning*. cs.CV. 2026 <https://arxiv.org/abs/2608.02833>
57. Giorgio Severi, Shujaat Mirza, Blake Bullwinkel et al.. *Evading Chain-of-Thought Monitoring Through Model Poisoning*. cs.CR. 2026 <https://arxiv.org/abs/2608.02820>
58. Zhaoxin Yu, Qi Shen, Hengli Li et al.. *GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Time Latent Reasoning*. cs.LG. 2026 <https://arxiv.org/abs/2608.02585>
59. Mobina Kashaniyan, Ali Jannesari. *Interpretable Adaptive Sampling for LLM Test-Time Scaling*. cs.AI. 2026 <https://arxiv.org/abs/2608.03961>
60. Teng Lin, Zhiyang Zhang, Yuyu Luo et al.. *Monte Carlo Tree Search for Table-to-Multimodal Report Generation*. cs.AI. 2026 <https://arxiv.org/abs/2608.04071>
61. Jinya Sakurai, Shueicheng Yan, Xun Xu. *Test-Time Scaling for Safe Text-Guided Image Generation via Intermediate Clean Estimates*. cs.CV. 2026 <https://arxiv.org/abs/2608.03284>
62. Mohsen Hariri, Weicong Chen, Nahal Shahini et al.. *Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility*. cs.LG. 2026 <https://arxiv.org/abs/2608.04001>
63. Shashwat Sourav, Aishwarya Balwani. *The Tell-Tale Trace: Detecting Reasoning Failures in LLMs Using Chain-of-Thought Dynamics*. cs.LG. 2026 <https://arxiv.org/abs/2608.03291>
64. Agatha Duzan, Asa Cooper Stickland. *Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings*. cs.AI. 2026 <https://arxiv.org/abs/2608.04735>
65. Qiyuan Zhu, Dezhi Li, Pengyu Cheng et al.. *Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning*. cs.AI. 2026 <https://arxiv.org/abs/2608.04771>
66. Javier Rodriguez-Juan, Hiba Arnaout, Jose Garcia-Rodriguez et al.. *ODRA: Synthesizing Cognitive Behavioral Therapy Sessions with Structured Chain-Of-Thought and Dynamic Patient Resistance*. cs.CL. 2026 <https://arxiv.org/abs/2608.04524>
67. Mingguang Chen, Bo Qu, Licheng Wang. *The Calibration Floor: Format Repair Can Masquerade as Self-Correction at Small-to-Mid Scale*. cs.CL. 2026 <https://arxiv.org/abs/2608.04355>
68. Ahsan Bilal, Muhammad Ahmed Mohsin, Muhammad Umer et al.. *Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning*. cs.AI. 2026 <https://arxiv.org/abs/2608.05643>
69. Yan Zhou, Yue Ouyang, Kaiyang Zheng et al.. *CoBa: Cost-Effective Test-Time Scaling via Compute-Balanced Routing*. cs.AI. 2026 <https://arxiv.org/abs/2608.07424>
70. Zhaohui Wang. *Persistent Semantic Entities in Tool-Augmented LLM Systems*. cs.LG. 2026 <https://arxiv.org/abs/2608.07952>
71. Yifan Li, Ruxin Sun, Tongzhou Zhao. *StructReward: Efficient Structured Process Rewards for Self-Correcting Multimodal Reasoning*. cs.AI. 2026 <https://arxiv.org/abs/2608.08326>
72. Xuan-May Le, Minh-Tuan Tran, Ling Luo et al.. *Efficient Test-Time Scaling for LLM-based Time Series Forecasting*. cs.LG. 2026 <https://arxiv.org/abs/2608.08675>
73. Rahma Simin Ali, Jawad Hossain. *MathShikkha: A Controlled Study of Answer-Only and Chain-of-Thought Supervision for Bangla Mathematical Reasoning in Small Language Models*. cs.AI. 2026 <https://arxiv.org/abs/2608.08503>
74. Subinay Adhikary, Upal Bhattacharya, Vivek Kumar Singh et al.. *PROSLEX: A Novel Dataset for Expert-Annotated Legal Statute Prediction for Indian Judiciary*. cs.AI. 2026 <https://arxiv.org/abs/2608.08830>
75. Youssef A. Elhagrasy, Ian Hill, André Ivanov. *Adaptive Sequential Test Planning for Multi-Mechanism Reliability Qualification via Bayesian Monte Carlo Tree Search*. cs.AI. 2026 <https://arxiv.org/abs/2608.09622>
76. Rohan Bhagra, Mahantesh Halapannavar, Uddhav Bhattarai. *Agentic Harnesses: LLM-Driven Verification Layers for Robot Autonomy*. cs.RO. 2026 <https://arxiv.org/abs/2608.09857>
77. Lecheng Kong, Like Hui, Haitao Mao et al.. *Consilience for Verifier-Free Test-Time Scaling*. cs.CL. 2026 <https://arxiv.org/abs/2608.09898>
78. Nikita Kozodoi, Zainab Afolabi, Jack Butler. *Test-Time Augmentation for LLMs: When Input Diversity Beats Output Diversity at Matched Compute*. cs.LG. 2026 <https://arxiv.org/abs/2608.09351>
79. Aaron Haag, Altay Kaçan, Bertram Fuchs et al.. *Test-Time Scaling for CAD Generation via Verifier-Free Consensus Selection*. cs.CE. 2026 <https://arxiv.org/abs/2608.09706>
80. Rob Cornish, Iacopo Ghinassi, Po-Hung Yeh et al.. *FaithformBench: Benchmarking Faithfulness of Mathematical Chain-of-Thought Autoformalisation*. cs.CL. 2026 <https://arxiv.org/abs/2608.10916>
81. Del Coburn, Scott Sanner, Dan Silver. *Social Chain of Thought: A Multi-Agent Architecture Grounded in Medical Differential Diagnosis Methodology*. cs.AI. 2026 <https://arxiv.org/abs/2608.11420>
82. Vaibhav Singh, Soumya Suvra Ghosal, Sarvesh Gharat et al.. *ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling*. cs.AI. 2026 <https://arxiv.org/abs/2608.10928>
83. Utkarsh Bahuguna. *When Self-Consistency Backfires: Majority Vote Hurts the Majority of Hard Science Problems for Small LLMs*. cs.AI. 2026 <https://arxiv.org/abs/2608.11403>
84. Foundation Model Team, XPeng Inc. *XCoT-VLA: Executable Chain-of-Thought for Vision-Language-Action Driving*. cs.AI. 2026 <https://arxiv.org/abs/2608.10976>
85. Debanjan Dutta, Anish Chakrabarty, Swagatam Das. *Chain-of-Thought Shows the Path to a Tree: Realizing Branching Complexity*. cs.LG. 2026 <https://arxiv.org/abs/2608.11716>
86. Sen Xu, Wei Wang, Shixi Liu et al.. *Claim-Level Reliability Assessment for Efficient Test-Time Reasoning*. cs.AI. 2026 <https://arxiv.org/abs/2608.11994>
87. Pan Wang, Yihao Hu, Hang Wang et al.. *Diagnosis Before Recovery: Turning Agent Failures into Selective Self-Correction*. cs.CL. 2026 <https://arxiv.org/abs/2608.11772>
88. Vu Duc Anh, Nhat M. Hoang, Do Xuan Long et al.. *Reinforcing Step-level Reasoning for Effective Self-Correction in LLMs*. cs.CL. 2026 <https://arxiv.org/abs/2608.11573>
89. Zile Zhou, Huining Yuan, Weichen Zhang et al.. *SCOUT: Unlocking Enhanced Spatial Reasoning via Structured Chain-of-Thought and Multi-Objective Process Reward*. cs.CV. 2026 <https://arxiv.org/abs/2608.12220>
90. Xinmu Ge, Zizhuo Zhang, Yu Huang et al.. *Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling*. cs.LG. 2026 <https://arxiv.org/abs/2608.11829>
