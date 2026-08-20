# Reasoning Faithfulness

_Lecture note assembled from the research archive_

> Generated on 2026-08-20 from 32 archived source(s).
> Regenerated on every render — put your own material in a separate file.

## Scope

The gap between a model's stated chain of thought and the computation that produced its answer: unfaithful or post-hoc rationalization, reasoning that is latent rather than written, encoded or steganographic traces, and what a monitor reading the trace can and cannot catch. The question the archive answers is when a visible reasoning trace is evidence about the model, and when it is only text.

Built from 32 paper(s) and 0 recording(s) spanning 2023-05-07 to 2026-08-11. 29 of the papers have been read in full.

Tracked terms: `chain of thought faithfulness`, `faithful reasoning`, `unfaithful`, `faithfulness of chain of thought`, `chain of thought monitoring`, `monitorability`, `encoded reasoning`, `steganography`, `latent reasoning`, `implicit reasoning`, `post-hoc rationalization`, `reasoning trace`, `introspection`, `sandbagging`.

## Where the field stands

### 2026

- **INSIDE the Student's Mind: Jointly Modeling Latent Reasoning and Action in LLM Student Simulators** _(not yet summarized)_
- **ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling** — Injects a retrieved solved problem, with its full worked solution, into the middle of a reasoning model's own thinking trace at each step boundary, using the model's current intermediate answer as the retrieval query.
- **Stealing Reasoning Traces from Proprietary LLM APIs** _(not yet summarized)_
- **BDH-CQ: In-Context Learning with Recurrent Latent Reasoning** _(not yet summarized)_
- **Think Deep, Speak Once: Relit, A Recursive Latent Implicit Transformer Framework** — Bolts a small trainable recurrent block between a frozen 1.1B language model's body and its output head, so reasoning happens as repeated refinement of two latent vectors rather than as generated tokens.
- **Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings** — The first benchmark comparing CoT monitorability under explicit versus implicit influence, finding detection falls 41-46 points when the prompt never instructs the model to hide anything.
- **Does Out-of-Sight Equal Out-of-Mind in CoT Monitorability?** — Asks whether latent CoT destroys monitorability, and finds monitorability depends more on the task and on access to internals than on whether reasoning is explicit or latent.
- **LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipulation** — Builds a 0.5B world-action model for robot manipulation whose future-state prediction and action generation share one compact latent in a single token stream, specifies the task as a direction in visual feature space instead of language, and shows a frozen self-supervised vision encoder beating a four-times-larger pretrained vision-language backbone at the same training budget.
- **LatentGuard: Efficient and Inspectable Latent Reasoning for LLM Safeguards** — Compresses a safety guard's textual rationales into continuous latent states by a staged curriculum, cutting 268 reasoning tokens to 1.60 and latency 8.9-fold, and adds an on-demand decoder that reconstructs a human-readable audit artifact — whose own ablation shows the artifact is anchored far more by the source text than by the latent states it is supposed to inspect.
- **Perception Before Reasoning: Dynamic Latent Reasoning for Video Understanding and Question Answering** — Splits a video model's latent computation into perception latents that always ground the question in visual evidence and reasoning latents allocated only when the question needs inference, and shows that reasoning latents without rationale supervision are worse than no reasoning latents at all.
- **Evading Chain-of-Thought Monitoring Through Model Poisoning** — Shows that supervised fine-tuning can install a triggered backdoor whose visible reasoning stays clean, correct and topically benign while the final answer is attacker-chosen — leaving CoT-only monitors at chance (AUC 0.44-0.55) and recovering detection only when the monitor is shown the answer alongside the trace (0.76-1.00).
- **Latent Thought Credit: Multi-Answer Credit Assignment for Latent Reasoning** — Estimates what a continuous latent thought is worth by freezing the context after it and averaging the rewards of several answers sampled from that fixed context, then credits latent positions with the resulting thought-level advantage and answer positions with the ordinary group-relative one.
- _...and 11 more._

### 2025

- **Measuring Chain-of-Thought Monitorability Through Faithfulness and Verbosity** — Argues that faithfulness alone is insufficient for CoT monitoring and adds verbosity — whether the trace lists every factor needed to solve the task — combining the two into a monitorability score, then shows models can look faithful while omitting key factors.
- **Arithmetic Without Algorithms: Language Models Solve Math With a Bag of Heuristics** — Reverse-engineers the arithmetic circuit down to individual neurons and finds it is neither a learned algorithm nor memorization, but an unordered collection of sparse heuristic neurons that each fire on a numerical input pattern and vote for corresponding answers.
- **Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks in LLM Reasoning** — Tracks mutual information between each reasoning step's representation and the correct answer, finds it spikes at sparse 'MI peaks' that decode to reflective tokens like 'Wait' and 'Hmm', and shows suppressing exactly those tokens degrades reasoning while suppressing equally many others does not.
- **On Reasoning Strength Planning in Large Reasoning Models** — Shows that a reasoning model decides how long to think before emitting a single reasoning token — the eventual token count is linearly decodable from the question's activations at Spearman 0.84 — and that this plan is carried by one shared direction vector whose magnitude encodes strength and which acts by shifting the logits of the end-of-thinking token.
- **A Implies B: Circuit Analysis in LLMs for Propositional Logical Reasoning** — Uses causal mediation analysis on a minimal propositional logic task to recover a sparse reasoning circuit in Mistral-7B and Gemma-2 up to 27B, and decomposes it into four families of attention heads that execute rule locating, rule moving, fact processing and decision making as sequential steps.
- **Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs** — Shows that base models win pass@K on mathematics by producing wrong chains that land on right answers, and that scoring the chain too — CoT-Pass@K — reverses the verdict in RLVR's favour at every K.

### 2024

- **Grokked Transformers are Implicit Reasoners: A Mechanistic Journey to the Edge of Generalization** — Shows that transformers can learn implicit multi-step reasoning over stored knowledge, but only through grokking — extended training far past overfitting — and that whether the resulting circuit generalizes out of distribution depends on the reasoning type, succeeding for comparison and failing for composition.

### 2023

- **Measuring Faithfulness in Chain-of-Thought Reasoning** — Measures how much a model's answer actually depends on its stated chain of thought by intervening on the trace — adding mistakes, paraphrasing, truncating — and finds the dependence varies by task and decreases as models get larger.
- **Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting** — Shows that chain-of-thought explanations systematically misrepresent the real reason for a model's answer, by biasing inputs in ways the model never mentions and watching it rationalize the biased answer.

## Core ideas

### overthinking

Generating more reasoning than a problem needs, and the archive's largest cluster at 25 sources. The sources agree on the symptom and split on the cause, which is what keeps the term loose. One account locates it after the answer, where double-checking continues once the correct result is derived. One locates it before the problem starts, since models cannot recognize difficulty in advance — and a reasoning model's eventual token count is linearly decodable from the question's activations before a single reasoning token is emitted, which makes the length a decision rather than an outcome. One locates it in the reward, where a sequence-level efficiency penalty implicitly punishes long but correct trajectories so that training against length damages the reasoning it was meant to trim. Reported reductions run from roughly 40% to 87%, occasionally with accuracy gains, which suggests a substantial share of a long chain does no work. Three results added since sharpen the picture. Redundancy turns out not to sit in an identifiable class of step: pruning that targets reflective statements is reported to do no better than pruning that ignores them, because the reasoning skeleton is repeated and rephrased throughout. Cutting by structure is nonetheless not the same as cutting by length — removing the same token count by position rather than by graph role costs twenty points of accuracy. And the decision of when to stop is proved harder than the field has assumed: a fixed threshold on the probability that the current prefix is already correct can be arbitrarily far from optimal even when that probability is known exactly, because the comparison that matters is against the value of continuing.

Seen in: Reinforcement Learning with Evolving Rubrics as Rewards for Audio Reasoning; The Tell-Tale Trace: Detecting Reasoning Failures in LLMs Using Chain-of-Thought Dynamics; Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning; CAT: Confidence-Adaptive Thinking for Efficient Reasoning of Large Reasoning Models.

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

### localization

Attributing a behaviour to a specific part of a model — a layer, a head, a neuron, a direction, a parameter region — and the organizing question of this archive's interpretability work at fourteen sources. The sources agree it is possible and disagree about what a located component means. Granularity changes the answer: on propositional logic, four families of attention heads execute a sequential circuit, while on arithmetic the mechanism is an unordered bag of heuristic neurons, and no source tests whether a computation modular at head level is heuristic inside each head. Method choices change the answer too — how prompts are corrupted, which metric scores the effect and whether layers are patched singly or in windows all shift what activation patching reports, and single-component tracing cannot see components that matter only jointly. Two cautions recur. Being encoded is not being used: a concept can be linearly recoverable while having no influence on the output, and sparse autoencoders improve the first while attenuating the second. And what is located may be a state rather than a property, since memorizing and generalizing circuits compete during training.

Seen in: Reasoning Errors Have a Region and a Direction in the Residual-Stream Trajectory of LLMs; CircuitSteer: Geometrically Aligned Multi-Layer Steering via Sparse Autoencoder Circuits; Bias Analysis of L2 Speaking Assessment Systems Using Concept Activation Vectors; Multi-component Causal Tracing in Large Language Models.

### monitorability

_Definition pending; a task is queued._

Seen in: How Much Does a Reasoning Summary Reveal? An Observability Ladder for Large Language Models; Evading Chain-of-Thought Monitoring Through Model Poisoning; The Tell-Tale Trace: Detecting Reasoning Failures in LLMs Using Chain-of-Thought Dynamics; Risky Business: Measuring The Faithfulness-Safety Tension.

### entropy collapse

The failure mode in which a policy's output distribution becomes progressively more deterministic during reinforcement learning, eliminating exploration and saturating performance. At nine sources it has moved from a constraint the methods cite to an object several of them study, and they explain it differently. One attributes it to a covariance between log-probability and probability-weighted advantage that stays positive throughout training. One recasts it as an imbalance of flow, with entropy-decreasing tokens persistently outweighing entropy-increasing ones inside each update. One derives a bifurcation in second-order Renyi entropy at the policy's collision probability, so updating dominant tokens collapses entropy while updating long-tail tokens inflates it. One reduces the direction of change to the sign of a single scalar per token, and to that scalar's deviation from a policy-weighted baseline once a GRPO step is substituted in. A theoretical entry ties the remedies together, proving the classical entropy bonus relocates the optimum while covariance-targeted control is asymptotically unbiased once its coefficient is annealed. Two findings cut against the consensus: one source reports training entropy falling while accuracy improves, and another finds entropy tracks response diversity far more reliably than accuracy.

Seen in: BODHI: Do LLMs Branch Out and Discover Heterogeneous Inferences?; Don't Peek at the Answer: Outcome-Masked Group Relative Policy Optimization for Label-Free RLVR; When Correct Solutions Repeat: Rarity-Aware Credit Redistribution for GRPO; SeLaR: Selective Latent Reasoning in Large Language Models.

### exploration-exploitation trade-off

The tension this archive's entropy literature is organized around: a policy that concentrates probability mass gains reward on patterns it already has and stops discovering new ones. Twelve sources make it measurable rather than rhetorical, and they disagree about what to measure. The entropy family reads collapse as premature exploitation, supported by plain GRPO reaching the highest training reward at the lowest entropy, and takes pass@k at large k rather than accuracy as the metric that separates the two — which is also what supports the claim that RL sharpens sampling inside the base model's reachable set. Several sources then argue entropy is the wrong handle, replacing it with distributional deviation from the group average, with a diversity bonus over hidden-state representations that removes the pass@k degradation entropy methods leave behind, or with a per-token discriminator's deviation from a policy-weighted baseline. Two entries move the trade-off out of training entirely and pose it as a stopping problem — how many samples to draw before quitting — with classical optimal-stopping theory supplying the rule. A theoretical entry states the cost most sharply: exploration bought with an entropy bonus is paid for permanently in the location of the optimum unless the coefficient is annealed away.

Seen in: SeLaR: Selective Latent Reasoning in Large Language Models; Representation-Based Exploration for Language Models: From Test-Time to Post-Training; Beyond Entropy: Learning from Token-Level Distributional Deviations for LLM Reasoning; The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models.

## Methods

| Method | Sources | Summary |
| --- | ---: | --- |
| GRPO | 36 | _pending_ |
| LLM-as-a-judge | 30 | _pending_ |
| supervised fine-tuning | 29 | Training on input-output pairs, and in these sources specifically on reasoning traces. What 27 sources collectively show is how little of it is needed and how much depends on wh... |
| linear probe | 24 | A linear classifier or regressor fitted to a model's internal activations to test whether some property is linearly decodable from them — used across these 22 sources both as a... |
| chain of thought | 23 | Emitting intermediate tokens before an answer, and the object almost everything in this archive is about — now with a theoretical account of why it works. Twenty sources use it... |
| RLVR | 23 | Training against an automatically checkable outcome signal — a correct final answer, a passing test — rather than a learned reward model, which removes reward-model gaming as a... |
| self-consistency | 19 | _pending_ |
| test-time scaling | 18 | _pending_ |
| activation patching | 17 | _pending_ |
| chain-of-thought prompting | 15 | _pending_ |
| pass@k | 15 | _pending_ |
| activation steering | 14 | _pending_ |
| best-of-n | 14 | Generating N candidates and keeping the one a verifier scores highest, the archive's standard selection baseline — and one with a known failure direction. With an imperfect veri... |
| causal intervention | 11 | _pending_ |
| sparse autoencoder | 10 | An autoencoder trained to reconstruct a model's internal activations through a wider hidden layer under a sparsity penalty, so its rows form an overcomplete dictionary and any a... |
| process reward model | 9 | _pending_ |
| circuit analysis | 8 | Identifying a subset of model components — attention heads, neurons — and the information flow between them that accounts for a behaviour. The archived sources use it at three s... |
| DAPO | 8 | A GRPO variant that drops the KL penalty and adds clip-higher, dynamic sampling, token-level policy-gradient loss and overlong reward shaping. It appears in this archive in thre... |
| Monte Carlo tree search | 8 | Search over reasoning states guided by simulated rollouts, one of the structured alternatives to linear chain-of-thought. In this archive it appears as a comparison rather than... |
| process evaluation | 7 | Scoring the reasoning that led to an answer rather than only the answer, which six sources treat as necessary and which they show is limited by the cost of reference reasoning.... |

## Benchmarks and datasets

| Dataset / benchmark | Sources | Summary |
| --- | ---: | --- |
| MATH500 | 43 | A 500-problem subset of MATH, used across 39 sources as the mid-difficulty mathematics reference — large enough that a few items do not move the number, and easy enough that str... |
| AIME 2024 | 41 | The 2024 American Invitational Mathematics Examination, and the archive's single most-used benchmark at 39 sources — which is itself the thing to know about it. Its 30 problems... |
| GSM8K | 35 | _pending_ |
| AIME 2025 | 29 | The 2025 American Invitational Mathematics Examination, used across 26 sources as AIME 2024's companion and, increasingly, as a contamination control — it postdates the training... |
| AMC23 | 16 | The 2023 American Mathematics Competitions problems, used in the archive as the rung below AIME — harder than MATH500, easier than AIME, and small. It appears mostly in entropy... |
| GPQA-Diamond | 14 | A set of graduate-level multiple-choice questions in biology, chemistry and physics, used across these sources as the hard non-mathematical benchmark and as the place where math... |
| OlympiadBench | 13 | An olympiad-level mathematics benchmark and, at eleven sources, the most-cited evaluation set in this archive after the AIME pair. It functions as the stable member of the stand... |
| MATH | 12 | The competition-mathematics benchmark, cited here in its full form rather than the 500-problem subset that appears separately in this archive. The sources use it as a mid-to-har... |
| LiveCodeBench | 9 | A contamination-resistant code benchmark built from recently released problems, used in these sources mainly as the out-of-domain test for models trained on mathematics. It prod... |
| MMLU | 9 | A broad multiple-choice knowledge benchmark spanning many subjects. In this archive it is a transfer and measurement target rather than a reasoning benchmark in its own right: o... |
| Minerva | 8 | A mathematics benchmark of undergraduate and quantitative-reasoning problems, appearing in all four sources as part of the standard six-benchmark RLVR evaluation suite. It is co... |
| MMLU-Pro | 7 | A harder, more reasoning-oriented revision of MMLU, used in the archive as a multiple-choice knowledge-and-reasoning benchmark outside mathematics. Both sources use it as a brea... |
| Omni-MATH | 5 | A competition-level mathematics benchmark, reported by both sources only as one of the held-out evaluation sets in reinforcement learning experiments on verifiable mathematics.... |
| BBH | 4 | A multi-task reasoning benchmark that the sources use as the legible, non-frontier end of an evaluation suite rather than as a hard test. One finds dataset difficulty inversely... |
| SciQ | 3 | A science question-answering set that appears in three archived papers as a supporting evaluation set, with none of them describing its construction or reporting a headline attr... |
| AlpacaEval | 2 | An instruction-following benchmark scored by LLM judges, used in the archived sources in two unrelated ways. As a judge benchmark it is part of the preference-evaluation family... |
| BeaverTails | 2 | A safety dataset of prompts paired with responses annotated for harmfulness, used by both sources as the substrate for a harmful-content task rather than as an object of study.... |
| HarmBench | 2 | A benchmark of harmful behaviour prompts used for red-teaming, appearing in both sources as the adversarial half of a safety evaluation. One includes it among the nine moderatio... |
| MMLU-STEM | 2 | The science, technology, engineering and mathematics subset of a broad multiple-choice knowledge benchmark, used by both sources as the transfer check in a suite otherwise built... |
| OpenCodeInstruct | 2 | A large instruction-tuning corpus of programming problems, used by both sources as the coding half of a training or calibration mixture rather than as an evaluation set. One dra... |

## Reading path

**Start here** — the anchor papers for this topic:

1. 2305.04388
1. 2307.13702

**Then, in order of relevance:**

1. **Reasoning Traces Shape Outputs but Models Won&apos;t Say So** (2026)
   - Injects synthetic reasoning into a model's trace, shows the injection changes the answer, then shows the model refuses to admit it and fabricates an unrelated explanation instead.
   - <https://doi.org/10.18653/v1/2026.acl-long.1986>
2. **Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings** (2026)
   - The first benchmark comparing CoT monitorability under explicit versus implicit influence, finding detection falls 41-46 points when the prompt never instructs the model to hide anything.
   - <https://arxiv.org/abs/2608.04735>
3. **Does Out-of-Sight Equal Out-of-Mind in CoT Monitorability?** (2026)
   - Asks whether latent CoT destroys monitorability, and finds monitorability depends more on the task and on access to internals than on whether reasoning is explicit or latent.
   - <https://arxiv.org/abs/2608.04928>
4. **Evading Chain-of-Thought Monitoring Through Model Poisoning** (2026)
   - Shows that supervised fine-tuning can install a triggered backdoor whose visible reasoning stays clean, correct and topically benign while the final answer is attacker-chosen — leaving CoT-only monitors at chance (AUC 0.44-0.55) and recovering detection only when the monitor is shown the answer alongside the trace (0.76-1.00).
   - <https://arxiv.org/abs/2608.02820>
5. **ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling** (2026)
   - Injects a retrieved solved problem, with its full worked solution, into the middle of a reasoning model's own thinking trace at each step boundary, using the model's current intermediate answer as the retrieval query.
   - <https://arxiv.org/abs/2608.10928>
6. **LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipulation** (2026)
   - Builds a 0.5B world-action model for robot manipulation whose future-state prediction and action generation share one compact latent in a single token stream, specifies the task as a direction in visual feature space instead of language, and shows a frozen self-supervised vision encoder beating a four-times-larger pretrained vision-language backbone at the same training budget.
   - <https://arxiv.org/abs/2608.03701>
7. **LatentGuard: Efficient and Inspectable Latent Reasoning for LLM Safeguards** (2026)
   - Compresses a safety guard's textual rationales into continuous latent states by a staged curriculum, cutting 268 reasoning tokens to 1.60 and latency 8.9-fold, and adds an on-demand decoder that reconstructs a human-readable audit artifact — whose own ablation shows the artifact is anchored far more by the source text than by the latent states it is supposed to inspect.
   - <https://arxiv.org/abs/2608.03838>
8. **Perception Before Reasoning: Dynamic Latent Reasoning for Video Understanding and Question Answering** (2026)
   - Splits a video model's latent computation into perception latents that always ground the question in visual evidence and reasoning latents allocated only when the question needs inference, and shows that reasoning latents without rationale supervision are worse than no reasoning latents at all.
   - <https://arxiv.org/abs/2608.04124>
9. **Latent Thought Credit: Multi-Answer Credit Assignment for Latent Reasoning** (2026)
   - Estimates what a continuous latent thought is worth by freezing the context after it and averaging the rewards of several answers sampled from that fixed context, then credits latent positions with the resulting thought-level advantage and answer positions with the ordinary group-relative one.
   - <https://arxiv.org/abs/2608.01593>
10. **GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Time Latent Reasoning** (2026)
   - Inserts optimizable latent states at an intermediate Transformer layer rather than at the output, so self-attention makes every continuation token's log-probability differentiable with respect to every latent and reward-weighted gradients reach them from the whole continuation instead of only through their own decoded token.
   - <https://arxiv.org/abs/2608.02585>

## Open problems

Drawn from the limitations each paper states about itself, so this is what the field admits it cannot do yet.

- **ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling** — No limitations section in the material read. What a reader should weigh first is the retrieval encoder: the related-work section cites a result that structurally faithful retrieval over mathematics is hard with off-the-shelf encoders, and the method then uses an off-the-shelf E5-Large, with the encoder choice relegated to an ablation. Second, decontamination is by cosine similarity at 0.90 and the audit reports maximum retained similarities of 0.898 and 0.891 -- immediately below the cut, with mean retained similarities of 0.866 and 0.845, which the paper attributes to the structural density of synthetic math corpora rather than leakage, and defends with an answer-distinct retrieval control rather than with a lower threshold. Third, the headline gains sit on AIME 2025, which is 30 problems, so +13.4 is four problems even at three seeds. Fourth, three of the four benchmarks share the same NuminaMath bank and the fourth uses its own training split, so 'adapts to different example banks' rests on one swap, and nothing here tests a domain where a bank of solved problems does not exist. Finally, the entropy reduction is offered as the explanation of the gain but is measured alongside it rather than manipulated, so it is a correlate of the improvement and not shown to cause it.
- **Think Deep, Speak Once: Relit, A Recursive Latent Implicit Transformer Framework** — No limitations section, and the central comparison does not support the claim it is used for. ReLIT is **trained on each dataset's training split** -- 5,000 ProofWriter examples, 5,000 RuleTaker, 800 HELP, 2,000 TaxiNLI -- while every LLM number in the same table is taken from GLoRE under few-shot prompting. The paper says as much when introducing the setup and then tabulates the two side by side, so 'matching or outperforming significantly larger models' is a comparison between a task-specific trained head and models that saw no training data. On the two tasks where the training set is large and the label space is a verdict, ReLIT reaches 97-99 percent; on the three where it is small or the task is linguistic, it does not. Second, the repeated inference that stability implies correctness is not supported: 'the outputs remain consistent after this stabilization phase' and 'high confidence in the final supervision loops proves that the model is not hallucinating' conflate convergence with being right, and this archive holds a direct counter-case in work showing intermediate answers stabilize regardless of whether the answer is ultimately correct. Third, one backbone, one scale, no seeds or variance anywhere, and no ablation separating the residual-refinement novelty from deep supervision, adaptive halting or the frozen head. Finally, the efficiency argument is asserted rather than measured -- no latency, token or FLOP comparison against chain-of-thought appears, though avoiding token generation is the paper's motivation.
- **Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings** — The 41-46 point drop is reported for two of four settings, so the effect is not uniform across task formats and the other two are not characterized in the abstract. Nudges are constructed, and their strength relative to real deployment biases is unknown. Detection depends on the monitor used, so the numbers bound this monitor rather than monitorability in general.
- **Does Out-of-Sight Equal Out-of-Mind in CoT Monitorability?** — No quantitative results in the abstract. Hint-reliance is one proxy target, and a negative result about reasoning mode on this target need not transfer to other monitored behaviours. Models and probe architectures are not named. The finding is comparative and does not establish an absolute level of monitorability for any mode.
- **LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipulation** — No limitations section appears in the main text. What a reader should weigh: the headline comparison is close enough that the ordering depends on which column is read — the method leads on clean success and trails on randomized against the strongest similar-size baseline — and no seeds or variance are reported anywhere, on any table. The task token is computed offline from that task's own demonstrations, so specifying a genuinely new task requires demonstrations of it, which is a weaker form of instruction-following than the language conditioning it replaces and is not framed as a trade-off in the text. The ablations run on a 10-task subset while the headline uses 50, and the backbone comparison substitutes both the encoder and the task-conditioning at once, so the 9-point gap is not attributable to the backbone alone. The causal probe reads similarity through the training-time decoder rather than through anything used at inference, and the real-robot evaluation is not quantified in the portion of the paper reporting simulation results.
- **LatentGuard: Efficient and Inspectable Latent Reasoning for LLM Safeguards** — The paper has no limitations section, and one of its own framings should be read as the central caveat: the auxiliary decoder is explicitly not intended to recover the guard's internal reasoning process, only to produce artifacts that make decisions easier to review. Given that the ablation attributes most of the artifact's utility to source-text conditioning, a reader should treat the audit output as a plausible post-hoc account conditioned on the same input a human could read, not as a window into the latent computation — and nothing here tests whether the artifact and the verdict can disagree, which is the check that would distinguish the two. Further: the audit-utility metric is scored by a model judge, validated against human annotation on 386 samples by an annotator using the same criteria as that judge, so the two are not independent. All models are initialized from one reasoning-guard family and trained on one corpus, so the improvement is measured against the checkpoint the method starts from rather than against independently trained baselines. And the latency advantage holds against reasoning guards while two classification guards remain faster, so the efficiency claim is relative to the family being replaced.
- **Perception Before Reasoning: Dynamic Latent Reasoning for Video Understanding and Question Answering** — The paper has no limitations section. What a reader should weigh: the latent budgets are fixed at inference, so 'adaptive' means whether to reason rather than how much, and the routing is the only quantity the reinforcement stage adjusts. The training supervision — evidence boxes and rationales alike — is generated by one large model and filtered by another, so both the grounding targets and the distillation teacher are model outputs rather than human annotation, and the paper's own quality control is a human audit deferred to an appendix. No seeds or variance are reported for any table. And the interpretability claim rests on attention heatmaps concentrating on diagnostic cues, which the paper offers as a complementary non-textual form of explanation — a weak substitute, since attention concentration shows where the model looked and not that the answer depended on it.
- **Evading Chain-of-Thought Monitoring Through Model Poisoning** — The paper states its bounds directly: three open-weight reasoning models between 3.8B and 12B parameters, with every backdoor installed through supervised fine-tuning, so whether the same behaviour and mechanism arise at larger scale or through reinforcement learning and preference optimization is open. It also names the cost of its own recommendation — consistency monitoring requires recovering the conclusion implied by a trace, which is difficult in open-ended agentic settings where there may be no parseable conclusion to compare against. Two things a reader should add. The threat model grants the adversary full control of fine-tuning, which is the strongest position available and makes this an upper bound on the attack rather than a claim about likelihood; the authors note the poisoned models also stand in for the weaker case of a model inadvertently learning misaligned behaviour during training. And the one defence tested, a KL penalty toward the base distribution, reduces attack success from 94.0% to 79.3% — which the paper correctly describes as a cost to the attacker rather than a defence, leaving the defensive side essentially unexplored.
- **Latent Thought Credit: Multi-Answer Credit Assignment for Latent Reasoning** — The paper states its scope in the conclusion rather than a limitations section: two Qwen2.5-Instruct sizes, mathematics and STEM multiple choice with verifiable or easily normalized rewards, and fixed K and M, with noisier open-ended rewards, other model families, and the interpretability of the continuous thoughts left as future work. Two things a reader should add. First, the diagnostics undercut the mechanism more than the paper says: after training, thought-level utilities are so close together that ordering them is barely better than chance, which means the thought-level advantage — the paper's central signal — is estimating differences that have largely collapsed. The paper reads the small regret as reassurance, but the honest statement is that the credit signal survives because choosing wrong costs little, not because it chooses well. Second, the tuning surface is broad and task-dependent: the matching strength, the top-k support size (non-monotonic, with the highest-peak setting finishing a full point below the best final one) and the K-M split each have a different optimum per dataset, and all of them are read off the evaluation benchmarks. Gains over HRPO are around 0.9 to 1.2 average points with no seeds or variance reported.
- **GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Time Latent Reasoning** — The paper has no limitations section. What a reader should weigh: the random-walk result is presented as robustness and is also the sharpest bound on the claim, since a reward-free random direction in this latent space (60.6) nearly matches a reward-guided output-side method (60.3), and reward guidance accounts for only 2.4 of the roughly 6.1-point ablation span. That leaves open how much of the improvement is reasoning being refined as against a well-placed perturbation being selected. The method consumes an instance-level reward signal at inference, and the main text does not say what supplies it — the paper reports only that its optimization-iteration count is lower than the sample counts used by the sampling baselines, which is a compute argument rather than an information one. The interpretability claim rests on the L2 norm of gradients aggregated over rule-based token categories, which is a first-order sensitivity measure rather than a causal test, and no intervention confirms that perturbing connector tokens changes the outcome. Backbones are five instruction-tuned models at 3B to 14B on three benchmarks, and apart from the learning-rate sweep no seeds or variance are reported for any table.
- **How Much Does a Reasoning Summary Reveal? An Observability Ladder for Large Language Models** — The paper names four. The summaries are a controlled proxy — the same model, one instruction, no content filter and no incentive to evade a monitor — so the estimates describe this summary method rather than deployed provider summaries or adversarial ones. The claims are reader-relative: most estimates use simple linear readers, the stronger-reader test covers one judge on one model and benchmark, and monitors fitted in one setting transfer imperfectly. The ladder measures final-answer correctness only, and the authors state plainly that nothing here shows a trace or summary is a causal account of the model's computation, so extending the design to faithfulness or misbehaviour needs labels defined independently of correctness. And length is entangled with the linear readers' signal in a way the adjustments show but do not disentangle — the paper says the unadjusted and adjusted results should be read together, with neither isolating a length-independent semantic effect. Two further bounds a reader should note: the repeated-run analysis runs on MMLU-Pro alone, on an unusually difficult discordant subset whose primary-run accuracy is 23 to 30 points below the held-out pool with traces 2.5 to 3 times longer, and the GPT-5-mini comparison mixes monitoring with task solving, since that model can attempt the question itself.
- **Reasoning Traces Shape Outputs but Models Won&apos;t Say So** — Three models, unnamed in the abstract. Injected snippets are synthetic, so the influence is not one the model generated itself and non-disclosure of an external insertion may differ from non-disclosure of its own bias. The sycophancy and deception directions are pre-identified constructs, and their activation is correlational evidence about what the fabrication resembles rather than proof of a deceptive mechanism. 'Extreme hints' marks the strongest condition, so over 90% is not the rate across all conditions.

## References

1. Miles Turpin, Julian Michael, Ethan Perez et al.. *Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting*. cs.CL. 2023 <https://arxiv.org/abs/2305.04388>
2. Tamera Lanham, Anna Chen, Ansh Radhakrishnan et al.. *Measuring Faithfulness in Chain-of-Thought Reasoning*. cs.AI. 2023 <https://arxiv.org/abs/2307.13702>
3. *Grokked Transformers are Implicit Reasoners: A Mechanistic Journey to the Edge of Generalization*. NeurIPS 2024. 2024
4. Guan Zhe Hong, Nishanth Dikkala, Enming Luo et al.. *A Implies B: Circuit Analysis in LLMs for Propositional Logical Reasoning*. NeurIPS 2025. 2025
5. Yaniv Nikankin, Anja Reusch, Aaron Mueller et al.. *Arithmetic Without Algorithms: Language Models Solve Math With a Bag of Heuristics*. ICLR 2025. 2025
6. Chen Qian, Dongrui Liu, Haochen Wen et al.. *Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks in LLM Reasoning*. preprint. 2025
7. Austin Meek, Eitan Sprejer, Iván Arcuschin et al.. *Measuring Chain-of-Thought Monitorability Through Faithfulness and Verbosity*. preprint. 2025
8. Leheng Sheng, An Zhang, Zijian Wu et al.. *On Reasoning Strength Planning in Large Reasoning Models*. NeurIPS 2025. 2025
9. Xumeng Wen, Zihan Liu, Shun Zheng et al.. *Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs*. preprint. 2025
10. Daniel Scalena, Sara Candussio, Luca Bortolussi et al.. *Beyond the Commitment Boundary: Probing Epiphenomenal Chain-of-Thought in Large Reasoning Models*. preprint. 2026
11. Benjamin Shih, John Winnicki, Eric Darve. *Do Models Read What They Write? Causal Registers in Scratchpad Reasoning*. preprint. 2026
12. Dennis Wei, Yannis Belkhiter, Erik Miehling et al.. *Local Causal Attribution of Chain-of-Thought Reasoning*. Mechanistic Interpretability Workshop at ICML 2026. 2026
13. Subbarao Kambhampati, Karthik Valmeekam, Siddhant Bhambri et al.. *Position: Stop Anthropomorphizing Intermediate Tokens as Reasoning/Thinking Traces!*. ICML. 2026
14. Yijie Hao, Lingjie Chen, Ali Emami et al.. *Reasoning Traces Shape Outputs but Models Won&apos;t Say So*. ACL. 2026 <https://doi.org/10.18653/v1/2026.acl-long.1986>
15. Renyu Fu, Guibo Luo. *SeLaR: Selective Latent Reasoning in Large Language Models*. ACL. 2026 <https://doi.org/10.18653/v1/2026.acl-long.320>
16. Xuan Yang, Jiayu Liu, Yuhang Lai et al.. *Step-Level Sparse Autoencoder for Reasoning Process Interpretation*. ICML 2026 (Proceedings of the 43rd International Conference on Machine Learning, PMLR 306). 2026
17. Michael Rizvi-Martel, Guillaume Rabusseau, Marius Mosbach. *The Illusion of Superposition? A Principled Analysis of Latent Thinking in Language Models*. COLM. 2026
18. Jeonghye Kim, Xufang Luo, Minbeom Kim et al.. *Understanding Reasoning in LLMs through Strategic Information Allocation under Uncertainty*. preprint. 2026
19. Giorgio Severi, Shujaat Mirza, Blake Bullwinkel et al.. *Evading Chain-of-Thought Monitoring Through Model Poisoning*. cs.CR. 2026 <https://arxiv.org/abs/2608.02820>
20. Zhaoxin Yu, Qi Shen, Hengli Li et al.. *GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Time Latent Reasoning*. cs.LG. 2026 <https://arxiv.org/abs/2608.02585>
21. Andres Algaba, Francesca Carlon, Lynn Delcon et al.. *How Much Does a Reasoning Summary Reveal? An Observability Ladder for Large Language Models*. cs.LG. 2026 <https://arxiv.org/abs/2608.02089>
22. Xuyang Zhao, Liting Zhang, Zichen Xu et al.. *Latent Thought Credit: Multi-Answer Credit Assignment for Latent Reasoning*. cs.AI. 2026 <https://arxiv.org/abs/2608.01593>
23. Zhinan Liu, Jie Li, Mingyu Kang et al.. *LatentGuard: Efficient and Inspectable Latent Reasoning for LLM Safeguards*. cs.AI. 2026 <https://arxiv.org/abs/2608.03838>
24. Fan Yang, Yuting Su, Xiaobo Wang et al.. *LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipulation*. cs.RO. 2026 <https://arxiv.org/abs/2608.03701>
25. Haotian Xia, Zilin Xiao, Junbo Zou et al.. *Perception Before Reasoning: Dynamic Latent Reasoning for Video Understanding and Question Answering*. cs.CV. 2026 <https://arxiv.org/abs/2608.04124>
26. Agatha Duzan, Asa Cooper Stickland. *Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings*. cs.AI. 2026 <https://arxiv.org/abs/2608.04735>
27. Pedro Ferreira, Wilker Aziz, Ivan Titov. *Does Out-of-Sight Equal Out-of-Mind in CoT Monitorability?*. cs.CL. 2026 <https://arxiv.org/abs/2608.04928>
28. Abhishek Panwar, Maheep Singh, Saksham Bansal. *Think Deep, Speak Once: Relit, A Recursive Latent Implicit Transformer Framework*. cs.AI. 2026 <https://arxiv.org/abs/2608.08113>
29. Björn Engdahl, Adrian Kosowski, Jan Chorowski et al.. *BDH-CQ: In-Context Learning with Recurrent Latent Reasoning*. cs.NE. 2026 <https://arxiv.org/abs/2608.09888>
30. Alexander Panfilov, David Schmotz, Ilia Shumailov et al.. *Stealing Reasoning Traces from Proprietary LLM APIs*. cs.CR. 2026 <https://arxiv.org/abs/2608.09867>
31. Rose Niousha, Minwoo Kang, Narges Norouzi. *INSIDE the Student's Mind: Jointly Modeling Latent Reasoning and Action in LLM Student Simulators*. cs.AI. 2026 <https://arxiv.org/abs/2608.10492>
32. Vaibhav Singh, Soumya Suvra Ghosal, Sarvesh Gharat et al.. *ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling*. cs.AI. 2026 <https://arxiv.org/abs/2608.10928>
