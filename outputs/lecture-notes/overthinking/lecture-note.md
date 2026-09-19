# Overthinking

_Lecture note assembled from the research archive_

> Generated on 2026-09-20 from 460 archived source(s).
> Regenerated on every render — put your own material in a separate file.

## Scope

When and why large reasoning models think more than a problem needs (or less than it needs) — the accuracy/efficiency tradeoff of reasoning length, test-time compute scaling, and methods to make a model stop, or keep going, at the right point.

Built from 460 paper(s) and 0 recording(s) spanning 2024-01-01 to 2026-09-17. 458 of the papers have been read in full.

Tracked terms: `overthinking`, `underthinking`, `over-thinking`, `under-thinking`, `reasoning length`, `test-time compute`, `test time scaling`, `inverse scaling`, `chain-of-thought length`, `thinking budget`, `reasoning-action dilemma`, `large reasoning model`, `adaptive compression`, `accuracy-efficiency tradeoff`, `reasoning effort`, `thinking effort`, `reasoning budget`, `token budget`, `reasoning token`, `shared budget`, `resource-rational`, `compute-optimal`, `cost-bounded`, `early stopping`, `early exit`, `efficient reasoning`, `reasoning efficiency`, `parallel reasoning`, `test-time depth`, `token pricing`, `concise reasoning`, `adaptive reasoning`, `adaptive thinking`, `thinking model`, `reasoning trace`, `activation steering`, `steering vector`, `representation engineering`, `representation steering`, `inference-time intervention`, `test-time intervention`, `latent steering`, `logit bias`, `contrastive decoding`, `sparse autoencoder`, `attention temperature`, `linear probe`, `decoding intervention`, `reasoning control`, `controllable reasoning`.

## Where the field stands

### undated

- **$R^3$-Bench: LLMs Struggle with Resource-Rational Reasoning under Shared Budgets** — A benchmark that puts six problems of mixed difficulty under one shared computation budget and measures the gap between what a model solves problem-by-problem and what it solves when it must decide how to divide the budget.

### 2026

- **OBC-Prune: Outcome-Based Calibration for Large Reasoning Model Pruning** _(not yet summarized)_
- **Disentangling Steering Vectors** _(not yet summarized)_
- **Thinking effort aligns between humans and reasoning models in abductive reasoning** — Measures whether reasoning models spend tokens on the same items humans spend time on, using a forced-choice abductive task where item difficulty cannot be read off formal structure, and finds a significant per-item correlation in all eight models tested.
- **Evaluating the Semantic Specificity of Representation Steering in Language Models** — Applying a late-layer steering vector to model families where a language model is already competent (Cross-Rule Transfer) reveals that a steering intervention which appears to perfectly fix contradiction blindness is functionally equivalent to a constant logit bias toward the target label, collapsing entailment accuracy from 99.6% to 40.4% rather than repairing a reasoning circuit.
- **SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing** — SABER is a training-free early-exit method that, at each "Wait" token, branches the reasoning prefix into a neutral and an adversarial probe, and stops when the two branches agree in answer and in confidence.
- **Prefix Sliding for efficient test-time scaling** — Prefix Sliding discards reasoning tokens outside a prefix (system instructions/prompt) plus a sliding window of the most recent tokens, giving constant per-token generation cost that lets language models reason for arbitrarily long horizons -- 3x faster than full attention without training, and enabling RL rollouts beyond 100,000 tokens with better reward than full-attention training at equal memory.
- **Adaptive Regularization for Random Features: A Neighboring Early-Stopping Rule with Oracle-Rate Guarantees** — Proposes NESR-KRR-RF, a neighboring early-stopping rule that adaptively selects the regularization parameter for kernel ridge regression with random features by comparing only adjacent estimators on a uniform grid, proving it attains the oracle polynomial learning rate up to log factors at lower computational cost than classical Lepskii-type all-pairs comparison.
- **Reflection Steering: Disentangling Reflection from Reasoning in Activation Space for Token-Efficient Inference** — Reflection Steering is a training-free activation-space intervention that isolates reflection-associated computation from general reasoning via PCA-purified, orthogonalized steering directions calibrated per layer, cutting thinking tokens by 16.9% on average across six model-benchmark settings with accuracy statistically equivalent to the raw model.
- **GRIP: Granular Reward-Guided Parameter Interpolation for Efficient Reasoning** — GRIP fuses a reasoning model and an instruction (non-thinking) model of identical architecture by learning a separate sigmoid-controlled interpolation ratio per module (attention, FFN, embedding/LM-head), trained with an RL reward that favors correct and concise responses while keeping both source models frozen, cutting Qwen3-4B-Thinking's average generation length 27.0% while slightly improving average accuracy.
- **Routed Graph Handoff: Adaptive Format Selection for Multi-Agent LLM Delegation** — Routed Graph Handoff (RGH) uses a lightweight LLM router to pick, per delegation, between a typed dependency-graph message and natural-language prose for multi-agent LLM handoffs, matching or beating NL-only on every one of four benchmarks while cutting token cost 2-3x.
- **$R^3$: Training Robots to Reason in Natural Language via Reinforcement Learning** — R3 is a two-stage post-training recipe (SFT mid-training on expert reasoning traces, then rubric-based single-step RL on offline instruction-only data) that trains a vision-language model to produce free-form natural-language reasoning steering a frozen low-level robot policy, and shows this test-time reasoning causally improves generalization beyond what training-time reasoning supervision alone provides.
- **TRACE: An Evidence-Grounded Benchmark for Safety Evaluation of Large Reasoning Models** — TRACE is a benchmark that extends LLM-safety evaluation from prompts and final responses to the reasoning traces of large reasoning models, with evidence-grounded annotations for each safety label.
- _...and 342 more._

### 2025

- **Between Underthinking and Overthinking: An Empirical Study of Reasoning Length and correctness in LLMs** — An empirical study showing reasoning LLMs overthink easy questions and underthink hard ones, and that preferring shorter outputs via SimPO can cut generation length 30-60% with little accuracy loss.
- **ARM: Adaptive Reasoning Model** — ARM trains a model to pick among four reasoning formats (Direct Answer, Short CoT, Code, Long CoT) per task using Ada-GRPO, cutting average tokens by about 30% at roughly unchanged accuracy.
- **How Far Are We from Optimal Reasoning Efficiency?** — Defines an empirical accuracy-vs-token-budget frontier for a fixed base reasoning model, measures how far existing efficiency methods fall short of it with a single metric (REG), and proposes REO-RL, an RL objective that targets a handful of token budgets to close most of that gap.
- **Inverse Scaling in Test-Time Compute** — Constructs evaluation tasks across four categories (distractor counting, spurious-feature regression, constraint-tracking deduction, and AI-risk model-written evaluations) where letting large reasoning models reason longer at test time makes their accuracy or alignment worse, not better.
- **Mitigating Overthinking in Large Reasoning Models via Manifold Steering** — A training-free residual-stream steering method that mitigates overthinking by projecting a difference-in-means 'overthinking direction' onto a low-dimensional PCA manifold of the model's activations before ablating it, removing the accuracy-degrading interference noise that limits naive single-direction steering.
- **The Danger of Overthinking: Examining the Reasoning-Action Dilemma in Agentic Tasks** — Defines and measures 'overthinking' in Large Reasoning Models on real software-engineering agent tasks, showing that favoring internal reasoning over environment interaction correlates with lower SWE-bench issue-resolution rates and can be mitigated at lower cost.
- **Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL** — AutoThink uses a three-stage RL curriculum with stage-wise reward shaping to teach R1-style distilled models to decide per problem whether to emit an explicit reasoning chain at all.
- **On Reasoning Strength Planning in Large Reasoning Models** — Finds that large reasoning models pre-plan how many reasoning tokens a question will need, encoded as a single pre-allocated direction vector in their activations whose magnitude can be read out to predict reasoning length or added/subtracted to causally control it.
- **Let LRMs Break Free from Overthinking via Self-Braking Tuning** — Introduces Self-Braking Tuning, which trains a large reasoning model to detect and stop its own redundant reasoning steps, cutting token usage by up to 60% with comparable accuracy on math benchmarks.
- **Does Thinking More Always Help? Mirage of Test-Time Scaling in Reasoning Models** — Shows that extending a reasoning model's thinking trace improves accuracy only up to a point and then declines from overthinking, and proposes sampling multiple independent short traces (parallel thinking) with majority vote as a more effective use of the same compute budget.
- **S-GRPO: Early Exit via Reinforcement Learning in Reasoning Models** — S-GRPO trains a reasoning model to stop its chain of thought early by sampling one reasoning path, forcing answers at several truncation points along it, and paying correct answers a reward that decays with how late the exit was.
- **A*-Thought: Efficient Reasoning via Bidirectional Compression for Low-Resource Settings** — A*-Thought treats a long reasoning trace as a search tree over reasoning spans and uses A* search with a bidirectional importance score to select a short, high-information subset of it as supervised fine-tuning data for compressed reasoning.
- _...and 87 more._

### 2024

- **Scaling Laws and Compute-Optimal Training Beyond Fixed Training Durations** — Shows that a constant-learning-rate-with-cooldown schedule scales as predictably and reliably as the standard cosine schedule for LLM pretraining, letting scaling-law experiments reuse partial training runs across durations and cut required compute.
- **Repurposing Language Models into Embedding Models: Finding the Compute-Optimal Recipe** — Derives a compute-optimal recipe for contrastively fine-tuning pretrained decoder-only LLMs into text-embedding models, finding full fine-tuning is optimal at lower compute budgets and LoRA fine-tuning at higher ones.
- **TinyTTA: Efficient Test-time Adaptation via Early-exit Ensembles on Edge Devices** — TinyTTA enables test-time adaptation on memory-constrained microcontroller units via a self-ensemble, batch-agnostic early-exit strategy, improving TTA accuracy by up to 57.6% and cutting memory use up to 6x versus prior methods.
- **Resolving Discrepancies in Compute-Optimal Scaling of Language Models** — Explains the discrepancy between the Kaplan and Chinchilla compute-optimal scaling laws by identifying and correcting three confounds (last-layer compute cost, warmup duration, scale-dependent optimizer tuning), after which the Kaplan-style reproduction matches the Chinchilla law.
- **DARG: Dynamic Evaluation of Large Language Models via Adaptive Reasoning Graph** — A benchmark-construction framework that extracts the reasoning graph behind each item in an existing benchmark and perturbs it to generate new test items at controlled complexity levels, then measures how 15 LLMs degrade as complexity rises.
- **4+3 Phases of Compute-Optimal Neural Scaling Laws** — Analyzes a solvable three-parameter neural scaling model (data complexity, target complexity, model-parameter-count) to derive the compute-optimal model size in the compute-limited, infinite-data regime, identifying 4 phases (+3 subphases) with proven scaling-law exponents in each.

## Core ideas

### Overthinking

A large reasoning model spending more reasoning tokens or steps on a problem than the problem needs, in a way that wastes compute for no accuracy gain, actively lowers accuracy, or degrades safety- or fairness-relevant behavior (e.g. more stereotype-aligned answers under sustained self-doubt, worse AI-risk judgments) as reasoning length grows. It is measured and explained several ways across the archive: an accuracy-vs-token-length curve that peaks and then falls (inverted-U); a model abandoning a previously correct intermediate answer ('flip events') or reasoning itself out of a right answer; excessive, unproductive self-verification and backtracking; information-theoretic divergence from an ideal reasoning path; a low-dimensional direction in activation space; and, on agentic tasks (software engineering, robotic action planning), favoring internal reasoning over acting in the environment. It is mitigated by length-penalized preference optimization, self-braking or self-training, decoupled token-level rewards with curriculum scheduling, activation steering, verifier-based trimming, decoding-tree early termination, parallel short-sample voting, and budget-aware query decomposition -- most reporting 30-70% token reductions at little or no accuracy cost, though a 33-model unified benchmark (OptimalThinkingBench) finds no evaluated model yet balances over- and under-thinking well.

Seen in: EvoThink: Evolving Thinking in Large Reasoning Models via Self-Pruning and Aha-Moment Preference Optimization; BLADE: Boundary-Expanded and Layer-Adaptive Dynamic Exit for Efficient LLM Reasoning; Translation with Thought: Difficulty-Adaptive Reasoning via Reinforcement Learning for Multi-Domain Machine Translation; Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning.

### Test-Time Scaling

Letting a model use more inference-time computation -- longer chains of thought, more parallel samples, search -- in the hope of higher accuracy. This is the umbrella term the largest number of the archive's collected papers use, spanning genuine reasoning-length work (speculative decoding for reasoning models, budget-aware tree search) and many off-topic applications the topic's keyword filter also caught (GUI agents, diffusion-model image generation, protein design) where 'test-time scaling' means something unrelated to LLM reasoning length. Note: the archive's wiki tracks this same underlying idea under at least three overlapping entries (test-time scaling, test-time compute, test-time compute scaling) that were never merged -- this is the largest and most heavily overloaded of the three, and readers should treat individual sources under it on a paper-by-paper basis rather than assuming uniform relevance.

Seen in: SLPO: Scaling Latent Reasoning via a Surrogate Policy; Interpretable Adaptive Sampling for LLM Test-Time Scaling; Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility; Disagree to Explore, Agree to Commit: Routing-Guided Test-Time Scaling for Software Agents.

### Test-Time Compute Scaling

Letting a language model use more inference-time computation — a longer chain of thought, more reasoning tokens, more parallel samples, tree search, or self-refinement passes — in the hope of higher accuracy; the archive's sources treat it as non-monotonic and mechanism-dependent rather than as a reliable lever. Its two identified mechanisms are verifier-search and proposal-revision: allocating compute per prompt difficulty beats any fixed strategy and can beat scaling parameters, scaling by verification or RL beats scaling by imitation of successful traces with the gap growing as sqrt(token budget), and on the sampling side self-consistency error decays as a power law in the sample count, so the same budget reallocated across questions matches vanilla self-consistency with 4.8x fewer samples. Where the extra compute pays is sharply uneven, and the newer sources sharpen that rather than soften it: a budget-forcing sweep has GSM8K and MATH-500 accuracy saturating at 256 thinking tokens while AIME generations split bimodally into ones that terminate and ones that loop to the 10,000-token ceiling; measured against an empirical accuracy-versus-token-budget frontier, current efficiency methods leave a quantified gap (REO-RL reaches 62.9% at 5,966 tokens against vanilla RL's 64.4% at 11,283 — 1.5 points for 55.9% fewer tokens); and past a point the returns go negative, with constructed tasks where longer reasoning worsens accuracy and alignment-relevant behaviour, agentic software tasks where favouring internal reasoning over environment interaction lowers issue-resolution rates, basic-arithmetic benchmarks where reasoning-tuned models spend far more tokens for equal or worse accuracy, and no model among 33 evaluated balancing over- and underthinking. Two framing corrections arrive with the newer sources: spent tokens are not the same as effort — the fraction of tokens still being revised in the network's late layers tracks accuracy better than raw length (mean Pearson 0.683 against 0.605 for self-certainty) — and the budget is not the model's to choose alone, since priced as a service the provider's optimal default reasoning budget sits above what the user would pick, with the user's own optimum measured at zero extra reasoning on GPQA Diamond and HMMT 2025.

Seen in: Token Budget Saturation and Mechanistic Early Detection of Reasoning Non-Convergence in Chain-of-Thought Models; Penelope: Localized Latent Recurrence for Efficient Structured Reasoning; Keep, Customize, or Exit: Default Design and Token Pricing in LLM Reasoning Services; Inverse Scaling in Test-Time Compute.

### accuracy-efficiency tradeoff

Across the eleven archived papers this is the background premise of the whole efficient-reasoning literature rather than a defined quantity: that shortening or skipping a model's reasoning saves tokens, latency or FLOPs, and that past some point the saving costs accuracy. The sources disagree about where the tradeoff actually binds. Several report it is largely avoidable at current operating points -- ARM cuts average tokens about 30% at roughly unchanged accuracy via Ada-GRPO over four reasoning formats, and CoSMo, ConPress, Retrieval-of-Thought and REAM each shorten traces without retraining accuracy away -- while WS-GRPO reports far shorter reasoning at some accuracy cost, and DRPO shows the tradeoff can be an artifact of the optimiser rather than of the model, since a naive length penalty inside GRPO turns correct-but-long rollouts negative. Two sources make it measurable instead of rhetorical: the inference-scaling-laws study plots accuracy against FLOPs across decoding strategies and model sizes, and 'How Far Are We from Optimal Reasoning Efficiency?' defines an empirical accuracy-versus-token-budget frontier for a fixed base model and scores how far existing methods fall short of it with a single metric, REG. Note: the archive tracks this idea under several near-duplicate entries that were never merged -- 'Accuracy-Length Tradeoff', 'Accuracy-Efficiency Pareto Frontier', 'Accuracy-token Pareto frontier', 'accuracy-efficiency tradeoff curve' and 'accuracy-efficiency tradeoff of reasoning length' -- which describe substantially the same idea.

Seen in: Penelope: Localized Latent Recurrence for Efficient Structured Reasoning; Towards Efficient Reasoning in LLM-Based Recommender Systems via Model Merging; Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL; Short Chains, Deep Thoughts: Balancing Reasoning Efficiency and Intra-Segment Capability via Split-Merge Optimization.

### Chain-of-Thought Compression

In these eight sources 'chain-of-thought compression' is an umbrella for making a reasoning trace shorter while keeping the answer, and it covers at least three operations that share no mechanism. One is selecting a subset of an existing trace -- A*-Thought runs A* search with a bidirectional importance score over reasoning spans and fine-tunes on the survivors. A second replaces the trace with non-textual tokens: Heima emits one learned thinking token per reasoning stage in latent space with a separate decoder that expands them back, while ImgCoT trains an autoencoder to reconstruct an image of the rendered CoT rather than its text. A third stops the trace early -- S-GRPO rewards correct answers with a decay in how late the exit was, DEER terminates at a thought-chain switch once a trial answer's token confidence clears a threshold, and ShorterBetter targets the shortest correct response in a sampled group, cutting output length by 50%-80% on DeepSeek-Distill-Qwen-1.5B/7B; one source is negative, showing that entropy-based selection never beats random pruning once a random baseline is included and that the apparent maths exception is caused by numeric tokens rather than entropy.

Seen in: Demystifying Entropy-based Selection for Chain-of-Thought Compression in Large Reasoning Models; Don't Overthink It: A Survey of Efficient R1-style Large Reasoning Models; ImgCoT: Compressing Long Chain of Thought into Compact Visual Tokens for Efficient Reasoning of Large Language Model; S-GRPO: Early Exit via Reinforcement Learning in Reasoning Models.

### supervised fine-tuning

Supervised fine-tuning appears across these six sources mainly as the stage that instills a target reasoning behaviour before or alongside RL. CoSMo trains on reasoning chains restructured by merging redundant segments and splitting logical gaps, budgeted by segment count rather than tokens; ARM and 'How Far Are We from Optimal Reasoning Efficiency?' use SFT-then-RL recipes (Ada-GRPO, REO-RL) to reach a chosen point on the accuracy-vs-token-budget frontier; 'Smaller, Weaker, Yet Better' shows that under a fixed sampling-compute budget, SFT data sampled many times from a smaller weaker model trains stronger reasoners than fewer samples from a larger one; 'From Reasoning Traces to Reusable Modules' argues the SFT-then-RL recipe works because RL decomposes the SFT-trained compound traces into reusable atomic modules; Dualformer instead trains one model with parts of its SFT traces randomly dropped, so it can run in fast, slow or auto mode from a single checkpoint.

Seen in: ChainPrune: Evaluating and Reducing Redundancy in Long Chain-of-Thought Reasoning; Select2Reason: Efficient Instruction-Tuning Data Selection for Long-CoT Reasoning; Follow the Path: Reasoning over Knowledge Graph Paths to Improve Large Language Model Factuality; Short Chains, Deep Thoughts: Balancing Reasoning Efficiency and Intra-Segment Capability via Split-Merge Optimization.

### underthinking

The complement failure mode to overthinking: a model reasons too little on a problem that genuinely requires deliberate, multi-step reasoning. The archive's 6 sources give it several concrete mechanisms: taking the first plausible answer without exploring alternatives or verifying it (OptimalThinkingBench), failing to extend a chain of thought far enough on hard questions while overthinking easy ones (Between Underthinking and Overthinking), and frequent premature switching between partial reasoning 'thoughts' before any is followed to completion, which prevents deep exploration of a promising line of reasoning ('Thoughts Are All Over the Place', which introduces a decoding-time penalty, TIP, to discourage the switching). TrimR and Plan-and-Budget both note it as the failure mode their overthinking-trimming methods must avoid falling into.

Seen in: OptimalThinkingBench: Evaluating Over and Underthinking in LLMs; Between Underthinking and Overthinking: An Empirical Study of Reasoning Length and correctness in LLMs; Thoughts Are All Over the Place: On the Underthinking of Long Reasoning Models; Efficient Reasoning with Balanced Thinking.

### adaptive reasoning

In these sources 'adaptive reasoning' names the property that a model's reasoning effort should follow the actual difficulty of the instance rather than a fixed global setting, and it is used loosely across at least three different knobs. Ada-R1 merges a long-CoT and a short-CoT model and applies bi-level preference training so the model first picks a reasoning style per problem and then prefers the shorter correct trace within it, cutting average reasoning length by about 51% on five maths datasets; ARES scales exploration effort with difficulty using sliding-window token entropy; AdaReasoner instead adapts the prompt instruction format, decoding temperature and number of reasoning steps as a model-agnostic RL-trained plugin. A fourth source makes the failure mode explicit by training (SFT on simple problems phrased both concisely and verbosely, then GRPO with a custom reward) so that the choice between explicit reasoning and a direct answer tracks real difficulty rather than how wordy the question is, and the efficiency survey files all of this under single-model optimization for avoiding overthinking.

Seen in: Don't Overthink It: A Survey of Efficient R1-style Large Reasoning Models; ARES: Multimodal Adaptive Reasoning via Difficulty-Aware Token-Level Entropy Shaping; When Simple Problems Wear Complex Costumes: Improving Efficiency in LRM's Adaptive Reasoning; Ada-R1: Hybrid-CoT via Bi-Level Adaptive Reasoning Optimization.

### Latent reasoning

Carrying the intermediate steps of reasoning in continuous hidden states rather than emitting them as chain-of-thought tokens, so that test-time compute is spent on internal iterations instead of on generated text. The archived sources instantiate this in four ways: a recurrent-depth architecture that iterates a latent block to arbitrary depth in place of longer chains; Penelope, which confines the recurrence to a five-layer slice of the decoder and refines a fixed-size boundary memory K times rather than re-running the whole model; Heima, which replaces each stage of a multimodal chain of thought with one learned thinking token and trains a separate decoder to expand those tokens back into readable reasoning; and AVA-VLA, which trains latent reasoning variables in a vision-language-action policy by RL denoising. The recurring open problem across them is not whether to reason latently but how deep to go: AVA-VLA adds a confidence-gated early exit that cuts mean reasoning depth from 5.0 to 2.3 steps and latency from 312 ms to 145 ms at essentially unchanged LIBERO success, and SLPO trains a stopping head that turns a fixed latent thinking budget into a learned per-instance horizon, scoring latent transitions with a Gaussian surrogate density from MC-dropout forwards. Because the steps are no longer text, they are not directly inspectable, which is why Heima trains a decoder to recover them.

Seen in: SLPO: Scaling Latent Reasoning via a Surrogate Policy; Penelope: Localized Latent Recurrence for Efficient Structured Reasoning; Large Reasoning Models Are (Not Yet) Multilingual Latent Reasoners; Efficient Reasoning with Hidden Thinking.

### MMMU

A multimodal knowledge and reasoning benchmark that reaches this archive only as an evaluation subject, never as a topic in its own right. In Amplified Does Not Mean Predictive it is one of the places the thinking-model advantage disappears: post-failure recovery rates are 32.9% for thinking models against 33.8% for instruct models, comparable rather than the 2-3x gap seen on VisualPuzzles, MATH-500 and MMLU-Pro. ARM2 uses it as an out-of-domain benchmark where enabling code execution raises accuracy from 49.8% to 50.2%, evidence that substituting code for long chain-of-thought is not merely a stylistic change; RECAP includes it among the benchmarks where RLVR paired with general-domain replay achieves best-or-near-best performance without the forgetting that reasoning-only fine-tuning causes; and ARISE uses it alongside MathVista and CharXiv-Reasoning to test its scaling metric on multimodal tasks, where GPT-5 and Claude Opus 4.1 score highest. ARES lists it among ten multimodal benchmarks but reports its largest gains on the harder MMMU-Pro (54.8 versus 41.2 for the Vision-G1 baseline) rather than on MMMU itself.

Seen in: Amplified Does Not Mean Predictive: Reasoning Behaviors in Thinking Models; ARM2: Adaptive Reasoning Model with Vision Understanding and Executable Code; Beyond Reasoning Gains: Mitigating General-Capability Forgetting in Large Reasoning Models; ARISE: An Adaptive Resolution-Aware Metric for Test-Time Scaling Evaluation in Large Reasoning Models.

### answer convergence

Answer convergence is the observation, shared by all three sources here, that a reasoning model settles on the answer it will finally give well before it stops generating, so the remainder of the trace changes the outcome little. The sources agree on the phenomenon and disagree on where to look for it: one defines an Answer Convergence Ratio by repeatedly truncating the trace, forcing an answer, and finding the earliest chunk after which that answer no longer changes — reporting ratios near 0.0 on NaturalQuestions, about 0.8 on GSM8K and MATH-500 and about 0.9 on GPQA and AIME'24; a second locates it in the confidence of probed intermediate answers, and adds that trajectories which never converge are the expensive ones, averaging over 25K tokens against about 12K for correct ones on Qwen3-4B; a third looks at reasoning-level semantic redundancy instead of the answer at all, and reports that 41-52% of reasoning tokens are generated after the model has already reached its final answer. All three treat convergence as a stopping signal rather than a correctness signal, and the first states plainly that convergence does not guarantee correctness.

Seen in: SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing; Early Stopping for Large Reasoning Models via Confidence Dynamics; Answer Convergence as a Signal for Early Stopping in Reasoning; Stop When Reasoning Converges: Semantic-Preserving Early Exit for Reasoning Models.

### early stopping

The five archived sources use 'early stopping' in three unrelated senses, and the archive should not be read as holding one idea here. Two halt a large reasoning model at inference: CaTS stops drawing further samples for a query once its self-distilled confidence is high enough, and 'Statistical Early Stopping for Reasoning Models' applies sequential stopping rules to the arrival of uncertainty keywords inside a trace, halting on ill-posed or ambiguous queries, with a finite-sample bound on the probability of halting too early on a well-posed one. Two use the classical training sense of stopping an optimizer short of convergence: Instance-dependent Early Stopping drops a training example from backpropagation once the second-order difference of its loss stays near zero, and a theoretical paper shows that in well-specified high-dimensional logistic regression gradient descent stopped early is consistent with polynomially many samples while gradient descent run to convergence is not. The fifth is neither, calibrating a termination threshold for a mixed-integer solver by conformal prediction on a learned estimate of the optimality gap; and none of the five is about leaving a network's layer stack at an intermediate head, which is early exit.

Seen in: A Data-dependent Early Stopping Rule using Rademacher Complexity with L1-norm; CaTS: Calibrated Test-Time Scaling for Efficient LLM Reasoning; Statistical Early Stopping for Reasoning Models; Conformal Prediction for Early Stopping in Mixed Integer Optimization.

## Methods

| Method | Sources | Summary |
| --- | ---: | --- |
| GRPO | 42 | The reinforcement-learning algorithm almost every training-side method in this archive is built on: it samples a group of G completions per prompt and replaces PPO's value netwo... |
| Self-Consistency | 12 | Sampling several independent reasoning traces for one problem and returning the answer the most of them agree on. In this archive it is the baseline every parallel test-time-sca... |
| Best-of-N sampling | 8 | A test-time-compute strategy that samples N candidate solutions independently and selects one (by a verifier, reward model, or majority vote), trading inference compute for accu... |
| Early Exit | 8 | Stopping a computation before its natural end once a signal indicates that continuing will not change the answer. In the sense this archive tracks, that computation is a reasoni... |
| process reward model | 8 | A model that scores the intermediate steps of a reasoning trace rather than only its final answer, used in this archive to guide search and to decide where compute should go. It... |
| SFT (baseline) | 8 | SFT (Supervised Fine-Tuning) is used across sources both as a standard training-pipeline stage (e.g. the pre-RL stage in SFT-then-RL pipelines) and as a comparison baseline for... |
| best-of-N | 7 | Best-of-N is a parallel test-time-compute strategy that samples N candidate solutions independently and selects one, trading inference compute for accuracy. Across the sources h... |
| Budget Forcing | 7 | Controlling how long a reasoning model thinks by imposing a token budget directly, rather than by reading any signal from the generation: the model is made to stop when the budg... |
| DEER | 7 | DEER is a training-free decoding method that ends a large reasoning model's chain of thought early: it treats the points where the model switches thoughts (marked in practice by... |
| O1-Pruner (baseline) | 7 | O1-Pruner is a fine-tuning method that compresses chain-of-thought length, and it appears in this archive only as a comparison baseline — no source here presents it as its own c... |
| DPO (baseline) | 6 | DPO appears in this archive as a baseline and as a component rather than as a subject: it is the preference-tuning route that length-control and efficient-reasoning methods are... |
| LoRA fine-tuning | 6 | A parameter-efficient fine-tuning method, present in these sources as the mechanism by which their training stages are implemented rather than as anything they study. None of th... |
| majority voting | 6 | Sampling several independent answers to one problem and returning the most frequent one -- the cheapest parallel test-time-compute strategy, needing no verifier and no reward mo... |
| NoThinking (baseline) | 6 | NoThinking (bypassing explicit chain-of-thought and answering directly) is used across these sources as a training-free lower-bound/comparison baseline for reasoning-efficiency... |
| activation steering | 5 | Controlling how long or how a reasoning model thinks by modifying its internal activations at inference time, rather than by prompting or retraining it. Sources here use it on t... |
| CoT-Valve (baseline) | 5 | CoT-Valve is cited here only as a length-control baseline that other adaptive-length methods (e.g. AdaMix) compare against and outperform on an accuracy-efficiency score; the so... |
| DEER (baseline) | 5 | DEER is used in these sources as a training-free early-exit/dynamic-stopping baseline that newer methods compare against: ThinkBrake and NEAT both report accuracy-length trade-o... |
| RLVR | 5 | Reinforcement learning in which the reward is a programmatic check of the final answer rather than a learned preference model, and the dominant post-training recipe among the re... |
| AdaptThink | 4 | A length-based reward-shaping reinforcement-learning method for controlling reasoning length. OptimalThinkingBench tests it as one of five overthinking mitigations, where it cut... |
| AdaptThink (baseline) | 4 | AdaptThink is used in these sources as a representative adaptive-reasoning (think/no-think gating) RL baseline that newer efficient-reasoning methods compare against: RPO report... |

## Benchmarks and datasets

| Dataset / benchmark | Sources | Summary |
| --- | ---: | --- |
| MATH500 | 144 | MATH500 is a 500-problem subset of the MATH competition-mathematics benchmark (Hendrycks et al.), used throughout this archive as a standard evaluation set for reasoning accurac... |
| AIME 2024 | 127 | AIME 2024 is the 2024 American Invitational Mathematics Examination, a competition-math problem set used throughout this archive as a hard reasoning-accuracy benchmark -- its pr... |
| AIME 2025 | 111 | AIME 2025 is the 2025 American Invitational Mathematics Examination, used identically to AIME 2024 across this archive as a hard, less-saturated competition-math benchmark for t... |
| GSM8K | 97 | GSM8K is a grade-school math word-problem benchmark, used throughout this archive as the 'easy' end of the math-reasoning difficulty spectrum -- its problems are short and large... |
| GPQA-Diamond | 83 | GPQA-Diamond is a graduate-level, expert-written multiple-choice science-question benchmark (the hardest subset of GPQA), used throughout this archive alongside AIME as a hard r... |
| AMC23 | 59 | AMC23 is the 2023 American Mathematics Competition problem set, used throughout this archive as a mid-difficulty competition-math benchmark -- harder than GSM8K/MATH500 but gene... |
| OlympiadBench | 37 | OlympiadBench is a challenging olympiad-level math/science benchmark used throughout this archive as a hard reasoning-accuracy test, comparable in difficulty to AIME -- used e.g... |
| LiveCodeBench | 31 | LiveCodeBench is a contamination-resistant, continuously-updated code-generation benchmark used throughout this archive as the primary code-reasoning accuracy test -- frequently... |
| GPQA | 30 | GPQA is a graduate-level, expert-written multiple-choice science-question benchmark, used throughout this archive as a hard, non-math reasoning-accuracy test -- its Diamond subs... |
| MATH | 26 | The 12,500-problem competition-mathematics dataset of Hendrycks et al., used in this archive far more often as a training corpus and a probe set than as a test set -- reinforcem... |
| MMLU-Pro | 19 | A harder, more reasoning-intensive successor to MMLU spanning broad academic and professional knowledge domains with ten answer choices per question instead of four, used across... |
| MMLU | 18 | A multiple-choice knowledge benchmark that the archive's papers use mainly as the short-answer, low-difficulty end of a reasoning suite, and as a capability-preservation check r... |
| Minerva | 16 | A quantitative-reasoning maths benchmark used in this archive almost exclusively as an out-of-domain evaluation: papers train on MATH500, AMC or AIME data and report Minerva alo... |
| AIME | 13 | AIME (American Invitational Mathematics Examination) is a competition-math benchmark cited across many efficient-reasoning papers in this archive -- Self-Braking Tuning, DRPO, S... |
| AMC | 13 | The American Mathematics Competitions, used in this archive as a source of competition problems sitting between GSM8K and AIME in difficulty. Sources cite it in two ways that sh... |
| HumanEval | 13 | A code-generation benchmark of hand-written Python programming problems checked by unit tests, used across this archive's sources as one standard task (alongside math benchmarks... |
| CommonsenseQA | 10 | A multiple-choice commonsense question-answering set, used across the archive as the easy, non-mathematical end of the benchmark suite - the place where adaptive-length methods... |
| HMMT25 | 8 | A sitting of the Harvard-MIT Mathematics Tournament used in this archive as a hard competition-maths benchmark alongside AIME, on the order of 30 problems. It appears mainly in... |
| MathVista | 8 | A multimodal mathematical reasoning benchmark. None of the eight sources defines it, and it functions here as the shared evaluation on which work about vision-language reasoning... |
| MBPP | 8 | A Python program-synthesis benchmark, used across these sources as the code-generation member of an evaluation suite rather than as a subject in its own right; none of the eight... |

## Reading path

**Then, in order of relevance:**

1. **CAT: Confidence-Adaptive Thinking for Efficient Reasoning of Large Reasoning Models**
   - CAT (Confidence-Adaptive Thinking) uses self-certainty -- the KL divergence of a reasoning trajectory's per-token predictive distribution from uniform, an intrinsic model signal requiring no external labels -- to build preference pairs and a confidence-weighted preference-optimization loss (CWPO) that compresses reasoning on problems the model is confident about while preserving deliberation on uncertain ones, beating three efficient-reasoning baselines (OverThink, DAST, ConCISE) on accuracy-at-compression across three LRMs and three benchmarks.
   - <https://aclanthology.org/2026.acl-industry.152/>
2. **Between Underthinking and Overthinking: An Empirical Study of Reasoning Length and correctness in LLMs** (2025)
   - An empirical study showing reasoning LLMs overthink easy questions and underthink hard ones, and that preferring shorter outputs via SimPO can cut generation length 30-60% with little accuracy loss.
3. **When Is Thinking Enough? Early Exit via Sufficiency Assessment for Efficient Reasoning**
   - DTSR (Dynamic Thought Sufficiency in Reasoning) is a training-free early-exit framework where the model itself, at each reflection signal ('Wait', 'Alternatively', etc.), evaluates from a third-person perspective whether its own chain-of-thought so far is sufficient to answer, exiting once a self-assessed sufficiency score crosses a threshold, cutting reasoning length 28.9-34.9% with near-zero accuracy loss across Qwen3-8B/14B/32B and five benchmarks, outperforming NoThinking, NOWAIT, and DEER while also cutting inference latency 25-40% (unlike DEER, which reduces length but increases latency).
   - <https://aclanthology.org/2026.acl-long.1080/>
4. **Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation** (2026)
   - Trains a 1.5B reasoning model to emit one of three mode tokens (NoThink, Short, Long) as the very first token of its response and to reason under that mode's budget, learned end-to-end inside GRPO with no separate router.
   - <https://arxiv.org/abs/2608.20256>
5. **ARM: Adaptive Reasoning Model** (2025)
   - ARM trains a model to pick among four reasoning formats (Direct Answer, Short CoT, Code, Long CoT) per task using Ada-GRPO, cutting average tokens by about 30% at roughly unchanged accuracy.
   - <https://neurips.cc/virtual/2025/poster/115075>
6. **Think Better, Not Longer: Token-Level Marginal Utility for Efficient Reasoning in Large Reasoning Models**
   - Introduces token-level marginal utility -- the per-token log-probability gain toward the ground-truth answer -- and MUTO, a training framework that penalizes trajectories and individual tokens that reduce this probability, cutting DeepSeek-R1-Distill-Qwen token usage by 87.1% (1.5B) / 80.2% (7B) with comparable or better accuracy.
   - <https://aclanthology.org/2026.acl-long.1386/>
7. **Step-GRPO: Internalizing Dynamic Early Exit for Efficient Reasoning**
   - Step-GRPO internalizes dynamic early-exit into a reasoning model's own weights via a Dynamic Truncated Rollout exposing the model to short-yet-correct trajectories during RL training and a Step-Aware Relative Reward that penalizes redundant semantic steps relative to the group's own correct-completion baseline, cutting Qwen3-8B token usage 32.0% with no accuracy loss and zero inference-time overhead.
   - <https://aclanthology.org/2026.acl-long.990/>
8. **Translation with Thought: Difficulty-Adaptive Reasoning via Reinforcement Learning for Multi-Domain Machine Translation** (2026)
   - TwT trains a translation model to spend reasoning tokens in proportion to input difficulty, by cold-starting on 7K difficulty-rewritten CoT traces and then running GRPO with a BLEU+COMET quality reward and an n-gram repetition penalty.
   - <https://aclanthology.org/2026.acl-long.1400/>
9. **How Far Are We from Optimal Reasoning Efficiency?** (2025)
   - Defines an empirical accuracy-vs-token-budget frontier for a fixed base reasoning model, measures how far existing efficiency methods fall short of it with a single metric (REG), and proposes REO-RL, an RL objective that targets a handful of token budgets to close most of that gap.
   - <https://neurips.cc/virtual/2025/poster/118341>
10. **LEASH: Adaptive Length Penalty and Reward Shaping for Efficient Large Reasoning Model**
   - LEASH formulates reasoning-length control as a constrained RL optimization (maximize task reward subject to an expected-length constraint) solved via a Lagrangian primal-dual method with a one-sided length penalty, letting the penalty coefficient lambda self-tighten or self-relax based on real-time constraint violation rather than requiring manual tuning, and reduces average reasoning length by up to 62.7% (1.5B model) or 26.2% (4B model) while maintaining or improving accuracy on in-domain math and out-of-domain (GPQA, MMLU-Pro) benchmarks, outperforming fixed-penalty and prior length-control baselines.
   - <https://aclanthology.org/2026.acl-long.129/>

## Open problems

Drawn from the limitations each paper states about itself, so this is what the field admits it cannot do yet.

- **Thinking effort aligns between humans and reasoning models in abductive reasoning** — Stated by the author: effort increased correctness only on the hardest tercile of problems; all main analyses used each model's default reasoning-effort setting, a choice fixed a priori and analogous to telling a human in advance to expect easy, medium or hard items, so alignment might be stronger on a difficulty-calibrated dataset; only one form of abduction is tested (inference to the best explanation), leaving hypothesis generation uncovered; LLM outputs are prompt-sensitive and a different instruction wording could change the results; and although the shared error pattern argues against simple memorisation, ART items may have appeared in pretraining. Noticeable to the reader: the alignment is correlational and per-item, so it constrains what makes a problem expensive but says nothing about whether either system spends the right amount; the single non-reasoning control is one model, which is what leaves the reasoning-versus-non-reasoning comparison underpowered; and the stochastic-decoding gain is obtained by averaging many runs per item, so it describes an aggregate rather than the cost of any single generation the way a deployed model would produce it.
- **Evaluating the Semantic Specificity of Representation Steering in Language Models** — Stated by the authors: (1) Asymmetricity-2.0 is built from Wikidata, which carries geographic/cultural/historical biases and gaps the authors cannot control; (2) the study is English-only, so culture- or language-specific reasoning artifacts in the templates or in English-pretrained models cannot be ruled out; (3) the downstream benchmarks (CLUTRR, SpartQA, ProntoQA) are stylized, structured reasoning tasks and do not capture open-ended conversational reasoning or free-form dialogue where label-token boundaries are less well defined; (4) parameter-level mechanistic validation (e.g. cosine similarity of the steering vector with the unembedding label-direction difference, layerwise logit-lens attribution) is not performed on closed/API-only models and is left as future work -- CRT is explicitly a behavioral, not a weight-level, audit. Additional caveats the reader should note: the steering-strength sweep (Table 7) shows the collapse is threshold-dependent -- at alpha<=1.0 the intervention is too weak to fix contradiction recall at all, and there is no intermediate alpha at which contradiction recall is restored without also destroying entailment competence, so the failure mode is not an artifact of picking alpha=1.5 specifically. Qwen-3.5-9B-Instruct is included only as a directional sanity check, not a valid CRT subject, because its own native competence on the entailment rules (45.2%) falls below the paper's own >=95% competence threshold. The 'zero side effects' headline for LRS holds only under oracle task-level gating (injecting the vector exclusively on contradiction-labeled inputs, which requires a task classifier that does not exist at deployment); under the realistic unconditional/ungated setting the same vector produces the catastrophic collapse. Token-position ablations show the vector's effect is entirely at the final label-decision token (final-token-only injection gives 100% of the effect; injecting only during the preceding chain-of-thought tokens gives 0% effect), meaning the intervention overrides the output commitment rather than altering the internal reasoning trajectory.
- **SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing** — Stated by the authors (Limitations section): experiments cover only text-based reasoning benchmarks on models of 4B to 8B parameters, with no larger scales, and no evaluation in multimodal or agent settings where intermediate representations and confidence dynamics may behave differently. Noticeable to the reader: the paper does not state whether the Tok and CR columns of Table 1 include the probe tokens, and the totals in Table 3 do not match Table 1's Overall column, so the reported compression cannot be reconciled with the separately reported 3.8% probe overhead from the paper alone - this matters because the method's cost is precisely the extra generation it performs at every "Wait". The exit threshold tau is set per model family rather than derived, and the best alpha differs between easy and hard benchmarks, so two of the method's constants are tuned against the evaluation suite. The scoring-function ablation reports that SC * CS and a branch-uncertainty difference are both competitive, which the authors read as evidence that the two-branch probing framework rather than the RSS form carries the gains; that also means RSS itself is not shown to be necessary. Accuracy gains over vanilla are within about one point on every model, so the claim supported by the tables is preserved accuracy at lower cost rather than improved accuracy.
- **Prefix Sliding for efficient test-time scaling** — On LiveCodeBench, a window smaller than 16,384 tokens fails to match full attention -- inspecting samples shows the model sometimes reasons about code via long comment blocks before writing the implementation, so with a small window the start of the code implementation can move outside the window by the time it resumes coding; the paper suggests RL training with Prefix Sliding would likely adapt this commenting behavior. Benefit is limited for short generations, since the sliding-window 'warm-up phase' (before the window has filled) still behaves like full attention -- demonstrated on HealthBench, where average generations (~2086 tokens) rarely trigger sliding with a 2048-token window, yielding little speedup. Agentic/multi-turn use raises unresolved issues: reading large external content (e.g. a webpage) that exceeds the window risks losing information, and how to handle future user turns relative to prefix/window boundaries is left open. Comparisons are restricted to methods that (1) work on existing pretrained transformers out of the box and (2) have bounded cost per new token, excluding alternative subquadratic architectures (RNNs, SSMs) that would require training from scratch to compare fairly. Experiments scale up to hundreds of thousands of tokens and 7B-parameter models; further scaling is left to future work.
- **Adaptive Regularization for Random Features: A Neighboring Early-Stopping Rule with Oracle-Rate Guarantees** — The number of random features M is treated as a prespecified computational budget rather than adaptively selected -- adaptive selection of M is explicitly stated as not considered in this work. Theorem 2's feature-budget lower bound depends on the unknown exponents r, alpha, gamma (a uniform sufficient bound is given in Corollary 1, but it is conservative). Theoretical guarantees require 2r+gamma>1; one of the four simulated settings ((r,gamma)=(0.4,0.1), violating this) is included only as an empirical check outside the proven regime. All empirical validation is on synthetic periodic-spline-kernel data and one real-data experiment; no application to deep-learning or LLM settings is attempted or claimed.
- **Reflection Steering: Disentangling Reflection from Reasoning in Activation Space for Token-Efficient Inference** — Evaluated only on the Qwen family (Qwen3-30B-A3B, Qwen3-8B, QwQ-32B) due to needing internal activation access; transfer beyond this model family is untested. On GPQA-Diamond, the accuracy-equivalence test does not pass at the +-1-point margin (a -1.5pp change), so the strongest accuracy-preserving evidence is specific to mathematical reasoning. Calibration selects layers and the operating point (alpha) per model, and the paper notes the selected layers and best alpha remain model-dependent rather than universal. The method requires white-box access to residual-stream activations, so it cannot be applied to closed-weight APIs.
- **GRIP: Granular Reward-Guided Parameter Interpolation for Efficient Reasoning** — Evaluated only at the 4B parameter scale due to compute constraints; whether the accuracy-efficiency trade-off and per-layer differentiation patterns transfer to substantially larger reasoning models (30B+) is left open. All experiments use dense Transformer backbones; the method is not validated on Mixture-of-Experts architectures, where router and expert weights introduce structure the current per-module parameterization does not address. GRIP requires the reasoning and instruction models to share an identical architecture (same depth, width, head count), restricting it to within-family pairs (e.g. Qwen3-Thinking with Qwen3-Instruct); cross-family fusion is not directly supported and is not evaluated.
- **Routed Graph Handoff: Adaptive Format Selection for Multi-Agent LLM Delegation** — The router performs per-task-type (not fine-grained per-instance) routing and is blind to benchmark identity, so decisions cluster coarsely (100% graph on dependency-chain benchmarks, 89% NL on AppWorld); the 8.6pp oracle headroom would require execution-time signals and is left to future work. The typed schema was designed on 47 tau-bench trajectories disjoint from all evaluation data; the paper notes the schema may not generalize to domains with fundamentally different coordination patterns (e.g. open-ended creative tasks), and automating schema generation beyond hand-design is left as future work. Main results use one orchestrator backbone (Claude Sonnet 4.5) with only partial cross-vendor/cross-model replication reported. The graph-aware executor prompt is a required complement to the schema -- omitting it yields no gain -- so adoption requires updating the receiving agent, not just the message format.
- **$R^3$: Training Robots to Reason in Natural Language via Reinforcement Learning** — Evaluated only in two simulated testbeds (Language Table block arrangement, bimanual grocery packing) with a single VLM backbone (Qwen3.5-4B) and a fixed low-level policy; generalization to real robots and other model scales/architectures is not demonstrated. The RL stage uses a single-step formulation to sidestep long-horizon credit assignment rather than full multi-turn RL with real environment rollouts, so gains are bounded by how well single-step reward (semantic match to an expert's next instruction) approximates eventual task success. The reward function requires either a VLM-as-judge (validated only against 100 human-labeled prompt-response pairs) or exact-match parsing (grocery packing), both of which could introduce judge-specific biases not explored beyond the reported inter-annotator agreement check.
- **TRACE: An Evidence-Grounded Benchmark for Safety Evaluation of Large Reasoning Models** — TRACE covers only English and Chinese, so cross-lingual generality beyond these two is untested. Safety labels rely on 3 annotator LRMs plus human review of unresolved cases rather than full human annotation, so some label noise may remain. The paper does not report how reasoning-trace length or verbosity relates to safety, so it says nothing about whether longer traces are more or less likely to contain unsafe content.
- **Recursive Agentic Reasoning** — BRANCH's selection is an unweighted majority vote; the paper records but does not use a per-item agreement ratio, and notes verifier- or confidence-weighted selection is strictly more expressive and the largest gap versus the state of the art. No significance tests are reported; a single 200-item cell's accuracy carries a roughly ±7-point 95% interval, so small effects in the BBEH and Omni-MATH cells are called provisional. The HLE grader (letter/string extraction) is a stated lower bound relative to an LLM judge. Omni-MATH was not run on Qwen3.6-plus. A 50-item pilot that preceded the full runs showed a task-dependent pattern of operator effectiveness that motivated the routing hypothesis and did not survive contact with the full-scale data, illustrating that small-n pilots at this cost regime can support a conclusion the full data contradicts.
- **Beyond Confidence: Test-Time Scaling for Multi-Turn Search Agents via Retrieval Grounding** — RGV inherits retrieval quality -- it can be no better than what retrieval actually returned, and under outright corpus mismatch it is the only rule that stays above single-rollout average but its own margin is thin. Grounded is not correct: RGV measures retrieval success, not truth, so a wrong rollout that retrieves the right topic but draws the wrong conclusion still scores well (4.2% of questions). The prose-side normalization weakens the signal when the answer is forced to be very short, degrading toward simple answer-containment. All experiments are in English, and the method assumes retrieval-heavy agents; agents relying on non-retrieval tools (e.g. code interpreters) would need a different grounding signal, and gains shrink on reasoning-intensive tasks with less retrieval. RGV trusts the retrieval log, so an adversarially poisoned corpus could raise the vote weight of rollouts that copy from it -- a vulnerability shared by any method reading that log, and left open.

## References

1. Peisong Wang, Zhiwei Ma, Bowen Liu et al.. *$R^3$-Bench: LLMs Struggle with Resource-Rational Reasoning under Shared Budgets*. cs.CL <https://arxiv.org/abs/2608.16033>
2. Jaeeun Jang, Hansle Lee, Sangmin Kim. *A Few Bad Apples Spoil the Bunch: Preventing Global Entropy Collapse Driven by a Small Set of Tokens in LLM Reasoning*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.641/>
3. Yang Yao, Xuan Tong, Ruofan Wang et al.. *A Mousetrap: Fooling Large Reasoning Models for Jailbreak with Chain of Iterative Chaos*. ACL. 2025 <https://aclanthology.org/2025.findings-acl.408/>
4. Yingqian Cui, Zhenwei Dai, Pengfei He et al.. *A Reward-Guided Dual-Phase Framework for Adaptive Inference-Time Reasoning*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.511/>
5. Tingyun li, Zishang Jiang, Jinyi Han et al.. *ADaPT: Token-Level Decoupling for Efficient Large Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.165/>
6. Junlin Liu, Shengnan An, Shuang Zhou et al.. *AMO-Bench: Large Language Models Still Struggle in High School Math Competitions*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.101/>
7. Zhangyue Yin, Qiushi Sun, Zhiyuan Zeng et al.. *ARISE: An Adaptive Resolution-Aware Metric for Test-Time Scaling Evaluation in Large Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.289/>
8. Jian Xie, Zhendong Chu, Aoxiao Zhong et al.. *ARM2: Adaptive Reasoning Model with Vision Understanding and Executable Code*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1365/>
9. Yize Zhang, Tianshu Wang, Sirui Chen et al.. *ARise: Towards Knowledge-Augmented Reasoning via Risk-Adaptive Search*. ACL. 2025 <https://aclanthology.org/2025.acl-long.538/>
10. Seyedarmin Azizi, Erfan Baghaei Potraghloo, Souvik Kundu et al.. *Activation Steering for Chain-of-Thought Compression*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1828/>
11. Hao Luo, Xiao Yan, Xinyan Li et al.. *AdaMix: Adaptive Mixing for Short and Long Reasoning Adapters*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1864/>
12. Wenyue Xu, Xu Wan, Wei Wang et al.. *AdapThink: Adaptive Thinking Preferences for Reasoning Language Models*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.477/>
13. Tianle Chen, Pengyu Cheng, Qiyuan Zhu et al.. *Adaptive Spatial and Temporal Redundancy Optimization for Efficient Reasoning in Large Language Models*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1130/>
14. Bowen Zuo, Dongruo Zhou, Yinglun Zhu. *Adaptive Test-Time Compute Allocation with Evolving In-Context Demonstrations*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1754/>
15. Xingjian Diao, Zheyuan Liu, Chunhui Zhang et al.. *Addressing Overthinking in Large Vision-Language Models via Gated Perception-Reasoning Optimization*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.215/>
16. Henan Sun, Kaichi Yu, Yuyao Wang et al.. *AlgBench: To What Extent Do Large Reasoning Models Understand Algorithms?*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1885/>
17. Fan Li, Jianxing Yu, Jielong Tang et al.. *Answering Complex Geographic Questions by Adaptive Reasoning with Visual Context and External Commonsense Knowledge*. ACL. 2025 <https://aclanthology.org/2025.acl-long.1239/>
18. Abinitha Gourabathina, Inkit Padhi, Manish Nagireddy et al.. *Answering the Wrong Question: Reasoning Trace Inversion for Abstention in LLMs*. ACL. 2026 <https://aclanthology.org/2026.acl-long.608/>
19. Wei Wu, Liyi Chen, Congxi Xiao et al.. *Anti-Length Shift: Dynamic Outlier Truncation for Training Efficient Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1047/>
20. Shuaiyi Nie, Dingsiyu, Wenyuan Zhang et al.. *AttnPO: Attention-Guided Process Supervision for Efficient Reasoning*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1845/>
21. Feng Luo, Yu-Neng Chuang, Guanchu Wang et al.. *AutoL2S: Auto Long-Short Reasoning for Efficient Large Language Models*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.831/>
22. Jiacheng Liang, Tanqiu Jiang, Yuhui Wang et al.. *AutoRAN: Automated Hijacking of Safety Reasoning in Large Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1988/>
23. Ivan Rodkin, Daniil Orel, Konstantin Smirnov et al.. *Beyond Memorization: Extending Reasoning Depth with Recurrence, Memory and Test-Time Compute Scaling*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.2103/>
24. Hoang Phan, Xianjun Yang, Yuanshun Yao et al.. *Beyond Reasoning Gains: Mitigating General-Capability Forgetting in Large Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1717/>
25. Canhui Wu, Qiong Cao, Chang Li et al.. *Beyond Token Length: Step Pruner for Efficient and Accurate Reasoning in Large Language Models*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.94/>
26. Zhiyuan Hu, Yibo Wang, Hanze Dong et al.. *Beyond ’Aha!’: Toward Systematic Meta-Abilities Alignment in Large Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1981/>
27. Zhiyi Duan, Lei Gao, Jiangshan Guan et al.. *BloomEval: A Bloom’s Cognitive Taxonomy-Based Benchmark for Evaluating LRMs via Cognitive Hierarchy Trace*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1262/>
28. Litu Ou, Kuan Li, Huifeng Yin et al.. *BrowseConf: Confidence-Guided Test-Time Scaling for Web Agents*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.21/>
29. Xuanming Zhang, Shwan Ashrafi, Aziza Mirsaidova et al.. *Budget-Aware Anytime Reasoning with LLM-Synthesized Preference Data*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.417/>
30. Qizhi Jiang, Shuo Wang, Pei Ke et al.. *CAT: Confidence-Adaptive Thinking for Efficient Reasoning of Large Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.acl-industry.152/>
31. Oded Schlesinger, Young Kyung Kim, J. Matias Di Martino et al.. *CLARO: Controlled Attribute-Driven Reasoning Optimization for Efficient Chain-of-Thought*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1335/>
32. Kai Zhang, Jiayi Liao, Chengpeng Li et al.. *Chronos: Learning Temporal Dynamics of Reasoning Chains for Test-Time Scaling*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1376/>
33. Junyi Li, Yongqiang Chen, Ningning Ding. *CiPO: Counterfactual Unlearning for Large Reasoning Models through Iterative Preference Optimization*. ACL. 2026 <https://aclanthology.org/2026.acl-long.143/>
34. Siyi Li, Jiajun Shi, Shiwen Ni et al.. *CoTJudger: A Graph-Driven Framework for Automatic Evaluation of Chain-of-Thought Efficiency and Redundancy in LRMs*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.2077/>
35. Nicholas Roberts, Niladri S. Chatterji, Sharan Narang et al.. *Compute Optimal Scaling of Skills: Knowledge vs Reasoning*. ACL. 2025 <https://aclanthology.org/2025.findings-acl.688/>
36. Yifan Wu, Jingze Shi, Bingheng Wu et al.. *Concise Math Reasoning via Difficulty-Aware Distillation*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.2155/>
37. Honghao Liu, Chengjin Xu, Xuhui Jiang et al.. *Conflicts Make Large Reasoning Models Vulnerable to Attacks*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.463/>
38. Nathanaël Carraz Rakotonirina, Ren Pang, Neha Anna John et al.. *Correct, Concise and Complete: Multi-stage Training For Adaptive Reasoning*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.622/>
39. Jiaxi Bi, Tongxu Luo, Wenyu Du et al.. *Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning*. ACL. 2026 <https://aclanthology.org/2026.acl-long.876/>
40. Yuxuan Jiang, Dawei Li, Francis Ferraro. *DRP: Distilled Reasoning Pruning with Mathematical Skill-aware Step Decomposition for Efficient Large Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.196/>
41. Shangqing Tu, Yaxuan Li, Yushi Bai et al.. *DeepPrune: Parallel Scaling without Inter-trace Redundancy*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.656/>
42. Ziang Ye, Zhenru Zhang, Yang Zhang et al.. *Disentangling Reasoning Tokens and Boilerplate Tokens For Language Model Fine-tuning*. ACL. 2025 <https://aclanthology.org/2025.findings-acl.1078/>
43. Taewon Yun, Jisu Shin, Jeonghwan Choi et al.. *Distilling Long-CoT Reasoning through Collaborative Step-wise Multi-Teacher Decoding*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1867/>
44. Wei-Rui Chen, Vignesh Kothapalli, Ata Fatahibaarzi et al.. *Distilling the Essence: Efficient Reasoning Distillation via Sequence Truncation*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.587/>
45. Janvijay Singh, Dilek Hakkani-Tür. *Do LLMs Encode Functional Importance of Reasoning Tokens ?*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1419/>
46. Xinliang Frederick Zhang, Anhad Mohananey, Alexandra Chronopoulou et al.. *Do LLMs Really Need 10+ Thoughts for “Find the Time 1000 Days Later”? Towards Structural Understanding of LLM Overthinking*. ACL. 2026 <https://aclanthology.org/2026.acl-long.773/>
47. Kun Huang, Rui Qiu, Xiaoming Li et al.. *Do Not Guess, Verify: Logic-Guided Adaptive Reasoning for Multimodal Misinformation Detection*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.238/>
48. Zhuowen Han, Lei Yang, Renren Jin et al.. *ERRV: Eliciting Efficient Reasoning through Reasoning Vectors for Policy Optimization in Large Language Models*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1425/>
49. Xuan Xiong, Huan Liu, Li Gu et al.. *ETR: Entropy Trend Reward for Efficient Chain-of-Thought Reasoning*. ACL. 2026 <https://aclanthology.org/2026.acl-long.799/>
50. Mukai Li, Linfeng Song, Zhenwen Liang et al.. *EconProver: Towards More Economical Test-Time Scaling for Automated Theorem Proving*. ACL. 2026 <https://aclanthology.org/2026.acl-long.2121/>
51. Jikai Wang, Juntao Li, Jianye Hou et al.. *Efficient Reasoning for LLMs through Speculative Chain-of-Thought*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.76/>
52. Jiakun Li, Xingwei He, Kefan Li et al.. *Efficient Test-Time Scaling via Temporal Reasoning Aggregation*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.651/>
53. Taehyeon Kim, Hyunsoo Lee, Youngsoo Jang et al.. *Efficiently Learning To Reason or Not to Reason: Root-token Policy Optimization for Adaptive Thinking*. ACL. 2026 <https://aclanthology.org/2026.acl-long.816/>
54. Jinu Lee, Kyoung-Woon On, Sophia Simeng Han et al.. *Evaluating Legal Reasoning Traces with Legal Issue Tree Rubrics*. ACL. 2026 <https://aclanthology.org/2026.acl-long.150/>
55. Yufeng Shi, Weilin Luo, Yuxiang Zhang et al.. *Exploration-Exploitation Reshaping towards Efficient Reasoning for Large Language Models*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1520/>
56. Hossam Amer, Maryam Dialameh, Hossein Rajabzadeh et al.. *FLOP-Efficient Training: Early Stopping Based on Test-Time Compute Awareness*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1766/>
57. Divya Jyoti Bajpai, Manjesh Kumar Hanawal. *FREE: Fast and Robust Vision Language Models with Early Exits*. ACL. 2025 <https://aclanthology.org/2025.findings-acl.1209/>
58. Chiwei Zhu, Benfeng Xu, Mingxuan Du et al.. *FS-Researcher: Test-Time Scaling for Long-Horizon Research Tasks with File-System-Based Agents*. ACL. 2026 <https://aclanthology.org/2026.acl-long.288/>
59. Chak Tou Leong, Dingwei Chen, Heming Xia et al.. *Finding RELIEF: Shaping Reasoning Behavior without Reasoning Supervision via Belief Engineering*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.218/>
60. Kehan Jiang, Haonan Dong, Zhaolu Kang et al.. *FoE: Forest of Errors Makes the First Solution the Best in Large Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1128/>
61. Mike Zhang, Johannes Bjerva, Russa Biswas. *Follow the Path: Reasoning over Knowledge Graph Paths to Improve Large Language Model Factuality*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.561/>
62. Rui Ha, Rui Pu, Chaozhuo Li et al.. *From "Aha Moments" to Controllable Thinking: Toward Meta-Cognitive Reasoning in LRMs via Decoupled Reasoning and Control*. ACL. 2026 <https://aclanthology.org/2026.acl-long.304/>
63. Zhaohan Zhang, Ziquan Liu, Ioannis Patras. *GrACE: A Generative Approach to Better Confidence Elicitation and Efficient Test-Time Scaling in Large Language Models*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1069/>
64. Hongyuan Yuan, Xinran He, Run Shao et al.. *Graph-Based Chain-of-Thought Pruning for Reducing Redundant Reflections in Reasoning LLMs*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.281/>
65. Amirhosein Ghasemabadi, Keith G. Mills, Baochun Li et al.. *Guided by Gut: Efficient Test-Time Scaling with Reinforced Intrinsic Confidence*. ACL. 2026 <https://aclanthology.org/2026.acl-long.739/>
66. Zhixiang Liang, Beichen Huang, Zheng Wang et al.. *Hidden States as Early Signals: Step-level Trace Evaluation and Pruning for Efficient Test-Time Scaling*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1336/>
67. Haoyang Chen, Yi Liu, Jianzhi Shao et al.. *How Do Answer Tokens Read Reasoning Traces? Self-Reading Patterns in Thinking LLMs for Quantitative Reasoning*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1507/>
68. Zhexin Zhang, Xian Qi Loye, Victor Shea-Jay Huang et al.. *How Should We Enhance the Safety of Large Reasoning Models: An Empirical Study*. ACL. 2026 <https://aclanthology.org/2026.acl-long.936/>
69. Peiqi Wang, ShengYun Peng, Xuewen Zhang et al.. *Inference Compute-Optimal Video Vision Language Models*. ACL. 2025 <https://aclanthology.org/2025.acl-long.117/>
70. William Jurayj, Jeffrey Cheng, Benjamin Van Durme. *Is That Your Final Answer? Test-Time Scaling Improves Selective Question Answering*. ACL. 2025 <https://aclanthology.org/2025.acl-short.50/>
71. Yanhao Li, Lu Ma, Jiaran Zhang et al.. *LEASH: Adaptive Length Penalty and Reward Shaping for Efficient Large Reasoning Model*. ACL. 2026 <https://aclanthology.org/2026.acl-long.129/>
72. Yihong Liu, Raoyuan Zhao, Hinrich Schuetze et al.. *Large Reasoning Models Are (Not Yet) Multilingual Latent Reasoners*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1121/>
73. Hao Wang, Hao Gu, Hongming Piao et al.. *Learning While Staying Curious: Entropy-Preserving Supervised Fine-Tuning via Adaptive Self-Distillation for Large Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.acl-long.617/>
74. Adrián Bazaga, Rexhina Blloshmi, Bill Byrne et al.. *Learning to Reason Over Time: Timeline Self-Reflection for Improved Temporal Reasoning in Language Models*. ACL. 2025 <https://aclanthology.org/2025.acl-long.1358/>
75. Qibin Wang, Pu Zhao, Shaohan Huang et al.. *Learning to Refine: Self-Refinement of Parallel Reasoning in LLMs*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1291/>
76. Guijin Son, Jiwoo Hong, Hyunwoo Ko et al.. *Linguistic Generalizability of Test-Time Scaling in Mathematical Reasoning*. ACL. 2025 <https://aclanthology.org/2025.acl-long.699/>
77. Bingxuan Li, Yiwei Wang, Jiuxiang Gu et al.. *METAL: A Multi-Agent Framework for Chart Generation with Test-Time Scaling*. ACL. 2025 <https://aclanthology.org/2025.acl-long.1452/>
78. Xinming Wang, Jian Xu, Bin Yu et al.. *MR-ALIGN: Meta-Reasoning Informed Factuality Alignment for Large Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.204/>
79. Hang Yan, Fangzhi Xu, Rongman Xu et al.. *MUR: Momentum Uncertainty guided Reasoning for Large Language Models*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1058/>
80. Huifeng Yin, Yu Zhao, Minghao Wu et al.. *Marco-o1 v2: Towards Widening The Distillation Bottleneck for Reasoning Models*. ACL. 2025 <https://aclanthology.org/2025.acl-long.1145/>
81. Dadi Guo, Jiayu Liu, Zhiyuan Fan et al.. *Mathematical Proof as a Litmus Test: Revealing Failure Modes of Advanced Large Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.acl-long.582/>
82. Weijie Xu, Brian Dillon, Richard Futrell. *Memory efficiency and resource-rational encoding in sentence processing*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1550/>
83. Heming Xia, Cunxiao Du, Rui Li et al.. *Merlin’s Whisper: Enabling Efficient Reasoning in Large Language Models via Black-box Persuasive Prompting*. ACL. 2026 <https://aclanthology.org/2026.acl-long.917/>
84. Qin Liu, Wenxuan Zhou, Nan Xu et al.. *MetaScale: Test-Time Scaling with Evolving Meta-Thoughts*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.574/>
85. Shuyang Jiang, Yuhao Wang, Ya Zhang et al.. *Miner: Mining Intrinsic Mastery for Data-Efficient RL in Large Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.acl-long.237/>
86. Florian Valentin Wunderlich, Lars Benedikt Kaesberg, Jan Philip Wahle et al.. *Multi-Agent Reasoning Improves Compute Efficiency: Pareto-Optimal Test-Time Scaling*. ACL. 2026 <https://aclanthology.org/2026.acl-srw.1/>
87. Kang Liu, YongKang Liu, Xiaocui Yang et al.. *NEAT: Neuron-Based Early Exit for Large Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1231/>
88. Haonan Dong, Kehan Jiang, Haoran Ye et al.. *NeuReasoner: Towards Explainable, Controllable, and Unified Reasoning via Mixture-of-Neurons*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1033/>
89. Haotian Luo, Haiying He, Yibo Wang et al.. *O1-Pruner: Length-Harmonizing Fine-Tuning for O1-Like Reasoning Pruning*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.697/>
90. Minh Duc Bui, Kyung Eun Park, Goran Glavaš et al.. *On Generalization across Measurement Systems: LLMs Entail More Test-Time Compute for Underrepresented Cultures*. ACL. 2025 <https://aclanthology.org/2025.acl-long.1032/>
91. Hyungjoo Chae, Dongjin Kang, Jihyuk Kim et al.. *One Missing Piece for Open-Source Reasoning Models: A Dataset to Mitigate Cold-Starting Short CoT LLMs in RL*. ACL. 2025 <https://aclanthology.org/2025.acl-industry.85/>
92. Zhengxiang Cheng, Dongping Chen, Mingyang Fu et al.. *Optimizing Length Compression in Large Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.acl-long.146/>
93. Ruixiang Feng, Yuntao Wen, Silin Zhou et al.. *PACE: Prefix-Protected and Difficulty-Aware Compression for Efficient Reasoning*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1545/>
94. Zhihao Xu, Fuzhen Yang, Liang Lin et al.. *PAM: Enhancing General Alignment of Large Reasoning Models through Priority-Aware Metacognition*. ACL. 2026 <https://aclanthology.org/2026.acl-long.432/>
95. Jingcheng Hu, Yinmin Zhang, Shijie Shang et al.. *PaCoRe: Learning to Scale Test-Time Compute with Parallel Coordinated Reasoning*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1253/>
96. Runyang You, Yongqi Li, Meng Liu et al.. *Parallel Test-Time Scaling for Latent Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.acl-long.2069/>
97. Derrick Goh Xin Deik, Quanyu Long, Zhengyuan Liu et al.. *Programming over Thinking: Efficient and Robust Multi-Constraint Planning*. ACL. 2026 <https://aclanthology.org/2026.acl-long.2028/>
98. Sanket Badhe, Deep Shah. *Prompt-Level Distillation: A Non-Parametric Alternative to Model Fine-Tuning for Efficient Reasoning*. ACL. 2026 <https://aclanthology.org/2026.acl-industry.142/>
99. Sondos Mahmoud Bsharat, Zhiqiang Shen. *Prompting Test-Time Scaling Is A Strong LLM Reasoning Data Augmentation*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.474/>
100. Han Liu, Shuotian Ma, Hui Li et al.. *Pru-CoT: Towards Efficient Reasoning Distillation via Pruning Chain-of-Thought*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1684/>
101. Yangyi Li, Chenxu Zhao, Mengdi Huai. *Quantifying and Understanding Uncertainty in Large Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1511/>
102. Zhuoshi Pan, Qizhi Pei, Yu Li et al.. *REST: Stress Testing Large Reasoning Models by Asking Multiple Problems at Once*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1296/>
103. Zihang Liu, Fang Zhouhua, Hui Liu et al.. *RFS-Guard: Detecting Reasoning Hallucinations via Cross-Phase Routing Focus in Large Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.acl-long.885/>
104. Mohsen Hariri, Michael Hinczewski, Jing Ma et al.. *Ranking Reasoning LLMs under Test-Time Scaling*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1544/>
105. Zhizhang Fu, Yuancheng Gu, Chenkai Hu et al.. *ReEfBench: Quantifying the Reasoning Efficiency of LLMs*. ACL. 2026 <https://aclanthology.org/2026.acl-long.931/>
106. Jingwei Ni, Ekaterina Fadeeva, Tianyi Wu et al.. *ReProbe: Efficient Test-Time Scaling of Multi-Step Reasoning by Probing Internal States of Large Language Models*. ACL. 2026 <https://aclanthology.org/2026.acl-long.536/>
107. Francesco Maria Molfese, Luca Moroni, Ciro Porcaro et al.. *ReTraceQA: Evaluating Reasoning Traces of Small Language Models in Commonsense Question Answering*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1798/>
108. Peizhuo Lv, Ruihua Zhou, Yunpeng Li et al.. *ReasMark: A Robust Watermark for Attributing LLM Reasoning Under Knowledge Distillation Attacks*. ACL. 2026 <https://aclanthology.org/2026.acl-long.2185/>
109. Yongchan Kwon, Shang Zhu, Federico Bianchi et al.. *ReasonIF: Large Reasoning Models Fail to Follow Instructions During Reasoning*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1456/>
110. Xiaoyu Xu, Yulan Pan, Xiaosong Yuan et al.. *Reasoning Fails Where Step Flow Breaks*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1212/>
111. Yijie Hao, Lingjie Chen, Ali Emami et al.. *Reasoning Traces Shape Outputs but Models Won’t Say So*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1986/>
112. Yuquan Wang, Mi Zhang, Yining Wang et al.. *ReasoningGuard: Safeguarding Large Reasoning Models with Inference-time Safety Aha Moments*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1453/>
113. Jiawei Chen, Yang Yang, Chao Yu et al.. *Red Teaming Large Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1034/>
114. Ziqi Zhao, Zhaochun Ren, Jiahong Zou et al.. *Reinforced Efficient Reasoning via Semantically Diverse Exploration*. ACL. 2026 <https://aclanthology.org/2026.acl-long.2216/>
115. Sahel Sharifymoghaddam, Jimmy Lin. *Rerank Before You Reason: Analyzing Reranking Tradeoffs through Effective Token Cost in Deep Search Agents*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1289/>
116. Yexiang Liu, Zekun Li, Zhi Fang et al.. *Rethinking the Role of Prompting Strategies in LLM Test-Time Scaling: A Perspective of Probability Theory*. ACL. 2025 <https://aclanthology.org/2025.acl-long.1356/>
117. Renren Jin, Pengzhi Gao, Yuqi Ren et al.. *Revisiting Entropy in Reinforcement Learning for Large Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1266/>
118. Taiqiang Wu, Runming Yang, Tao Liu et al.. *Revisiting Model Interpolation for Efficient Reasoning*. ACL. 2026 <https://aclanthology.org/2026.acl-long.389/>
119. Zhiyuan Zeng, Qinyuan Cheng, Zhangyue Yin et al.. *Revisiting the Test-Time Scaling of o1-like Models: Do they Truly Possess Test-Time Scaling Capabilities?*. ACL. 2025 <https://aclanthology.org/2025.acl-long.232/>
120. Ziyuan Nan, Qi Yi, Di Huang et al.. *Rhombus: Incentivizing Coordination in Parallel Thinking through Reinforcement Learning*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1956/>
121. Yu Zhang, Songwei Liu, Chenqian Yan et al.. *S2O: Early Stopping for Sparse Attention via Online Permutation*. ACL. 2026 <https://aclanthology.org/2026.acl-long.351/>
122. Weiyang Huang, Xuefeng Bai, Kehai Chen et al.. *SAT: Balancing Reasoning Accuracy and Efficiency with Stepwise Adaptive Thinking*. ACL. 2026 <https://aclanthology.org/2026.acl-long.2009/>
123. Fengqing Jiang, Zhangchen Xu, Yuetai Li et al.. *SafeChain: Safety of Language Models with Long Chain-of-Thought Reasoning Capabilities*. ACL. 2025 <https://aclanthology.org/2025.findings-acl.1197/>
124. Seungone Kim, Ian Wu, Jinu Lee et al.. *Scaling Evaluation-Time Compute with Reasoning Models as Evaluators*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.2102/>
125. Tingchen Fu, Yafu Li, Jiawei Gu et al.. *Scaling Reasoning, Losing Control: Evaluating Instruction Following in Large Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1878/>
126. Mehrzad Samadi, Aleksander Ficek, Sean Narenthiran et al.. *Scaling Test-Time Compute to Achieve IOI Gold Medal with Open-Weight Models*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1532/>
127. Shiyu Ji, Yixuan Wang, Yijun Liu et al.. *Seer Self-Consistency: Advance Budget Estimation for Adaptive Test-Time Scaling*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.2120/>
128. Cehao Yang, Xueyuan Lin, Xiaojun Wu et al.. *Select2Reason: Efficient Instruction-Tuning Data Selection for Long-CoT Reasoning*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.331/>
129. Shijia Xu, Zhou Wu, Xiaolong Jia et al.. *Self-Correcting RAG: Enhancing Faithfulness via MMKP Context Selection and NLI-Guided MCTS*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1052/>
130. Qiang Huang, Wei Zhai, Feng Huang et al.. *Self-Reflection Improves Safety of Large Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.678/>
131. Tergel Munkhbat, Namgyu Ho, Seo Hyun Kim et al.. *Self-Training Elicits Concise Reasoning in Large Language Models*. ACL. 2025 <https://aclanthology.org/2025.findings-acl.1289/>
132. Zheng Li, Qingxiu Dong, Jingyuan Ma et al.. *SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1063/>
133. Lechen Zhang, Yunxiang Zhang, Wei Hu et al.. *Skill-Aware Data Selection and Fine-Tuning for Data-Efficient Reasoning Distillation*. ACL. 2026 <https://aclanthology.org/2026.acl-short.49/>
134. Yige Xu, Xu Guo, Zhiwei Zeng et al.. *SoftCoT: Soft Chain-of-Thought for Efficient Reasoning with LLMs*. ACL. 2025 <https://aclanthology.org/2025.acl-long.1137/>
135. Shengmin Piao, Sanghyun Park. *SpiralThinker: Latent Reasoning through an Iterative Process with Text–Latent Interleaving*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1605/>
136. Han Wang, Xiaodong Yu, Jialian Wu et al.. *Stabilizing Efficient Reasoning with Step-Level Advantage Selection*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1333/>
137. Junyan Li, Wenshuo Zhao, Yang Zhang et al.. *Steering LLM Thinking with Budget Guidance*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1866/>
138. Benteng Chen, Weida Wang, Shufei Zhang et al.. *Step-GRPO: Internalizing Dynamic Early Exit for Efficient Reasoning*. ACL. 2026 <https://aclanthology.org/2026.acl-long.990/>
139. Renliang Sun, Wei Cheng, Dawei Li et al.. *Stop When Enough: Adaptive Early-Stopping for Chain-of-Thought Reasoning*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1256/>
140. Zichuan Fu, Xian Wu, Guojing Li et al.. *Tandem: Riding Together with Large and Small Language Models for Efficient Reasoning*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.2098/>
141. Cong Wan, Ying He, Zhongzhan Huang et al.. *Test-Time Scaling in Multimodal Foundation Models: A Comprehensive Survey of Generation and Reasoning*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.383/>
142. Huixue Zhou, Hengrui Gu, Zaifu Zhan et al.. *The Efficiency vs. Accuracy Trade-off: Optimizing RAG-Enhanced LLM Recommender Systems Using Multi-Head Early Exit*. ACL. 2025 <https://aclanthology.org/2025.acl-long.1283/>
143. Pratham Singla, Shivank Garg, Ayush Singh et al.. *The Inner Monologue of Language Models: When Reasoning Traces Reveal More Than They Hide*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.2078/>
144. Byung-Doh Oh, Hongao Zhu, William Schuler. *The Inverse Scaling Effect of Pre-Trained Language Model Surprisal Is Not Due to Data Leakage*. ACL. 2025 <https://aclanthology.org/2025.findings-acl.91/>
145. Zhiyuan Yu, Shijian Xiao, Cam-Tu Nguyen et al.. *Thermometer of Thoughts: Enhancing LLM’s Exploration via Attention Temperature Modulation*. ACL. 2026 <https://aclanthology.org/2026.acl-long.200/>
146. George Kour, Itay Nakash, Michal Shmueli-Scheuer et al.. *Think Again! The Effect of Test-Time Compute on Preferences, Opinions, and Beliefs of Large Language Models*. ACL. 2025 <https://aclanthology.org/2025.acl-industry.45/>
147. Jiawei Li, Yang Gao, Huashan Sun et al.. *Think Better, Not Longer: Token-Level Marginal Utility for Efficient Reasoning in Large Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1386/>
148. Ling-I Wu, Minyu Chen, Jingyang Li et al.. *Think Earlier, Not Longer: Prompt Optimization via Reducing Unhealthy Exploration*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.817/>
149. Yongjiang Liu, Haoxi Li, Xiaosong Ma et al.. *Think How to Think: Mitigating Overthinking with Autonomous Difficulty Cognition in Large Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1766/>
150. Yi Sui, Chaozhuo Li, Dawei Song. *Think Less, Know More: State-Aware Reasoning Compression with Knowledge Guidance for Efficient Reasoning*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1128/>
151. Zhichao Sheng, Shilin Zhou, Chen Gong et al.. *Think Smart, Not Hard: Difficulty Adaptive Reasoning for Large Audio Language Models*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1640/>
152. Vladislav Smirnov, Quang-Chieu Nguyen, Sergey Senichev et al.. *ThinkBooster: A Unified Framework for Seamless Test-Time Scaling of LLM Reasoning*. ACL. 2026 <https://aclanthology.org/2026.acl-demo.70/>
153. Sangjun Song, Minjae Oh, Seungkyu Lee et al.. *ThinkBrake: Efficient Reasoning via Log-Probability Margin Guided Decoding*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1095/>
154. Guangxiang Zhao, Qilong Shi, Xusen Xiao et al.. *Thinking with Reasoning Skills: Fewer Tokens, More Accuracy*. ACL. 2026 <https://aclanthology.org/2026.acl-industry.154/>
155. Siyuan Gan, Jiaheng Liu, Boyan Wang et al.. *Thinking-Based Non-Thinking: Solving the Reward Hacking Problem in Training Hybrid Reasoning Models via Reinforcement Learning*. ACL. 2026 <https://aclanthology.org/2026.acl-long.2122/>
156. Zhixiao Qi, Feng Huang, Yunqi Zhang et al.. *Thought-Action Graph Reasoning: Faithful and Efficient Reasoning of Large Language Models via Reusing Past Experience*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1572/>
157. Nguyen Viet Anh, Shiqian Zhao, Gia Dao et al.. *Three Minds, One Legend: Jailbreak Large Reasoning Model with Adaptive Stacked Ciphers*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.355/>
158. Yichuan Ma, Linyang Li, Yongkang Chen et al.. *Timely Machine: Awareness of Time Makes Test-Time Scaling Agentic*. ACL. 2026 <https://aclanthology.org/2026.acl-long.211/>
159. Tingxu Han, Zhenting Wang, Chunrong Fang et al.. *Token-Budget-Aware LLM Reasoning*. ACL. 2025 <https://aclanthology.org/2025.findings-acl.1274/>
160. Yi Zhao, Yajuan Peng, Cam-Tu Nguyen et al.. *TrigReason: Trigger-Based Collaboration between Small and Large Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.333/>
161. Haohan Yuan, Haopeng Zhang. *Understanding LLM Reasoning for Abstractive Summarization*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.859/>
162. James Petullo, Sonny George, Dylan Cashman et al.. *VecCISC: Improving Confidence-Informed Self-Consistency with Reasoning Trace Clustering and Candidate Answer Selection*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1305/>
163. Sangkwon Park, Donghun Kang, Jisoo Mok et al.. *Verbal-R3: Verbal Reranker as the Missing Bridge between Retrieval and Reasoning*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1712/>
164. Mourad Heddaya, Manley Roberts, Rohan Wadhawan et al.. *When Internalization Fails: Finding Better Targets for Reasoning Compression*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.734/>
165. Yang Xiang, Yixin Ji, Ruotao Xu et al.. *When Is Thinking Enough? Early Exit via Sufficiency Assessment for Efficient Reasoning*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1080/>
166. Yingzhi Mao, Chunkang Zhang, Junxiang Wang et al.. *When Models Outthink Their Safety: Unveiling and Mitigating Self-Jailbreak in Large Reasoning Models*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1118/>
167. Sitong Fang, Wenjing Cao, Jiahao Li et al.. *When Slower Isn’t Truer: Inverse Scaling Law of Truthfulness in Multimodal Reasoning*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.63/>
168. Zi-Ao Ma, Xian-Ling Mao, Tian Lan et al.. *Your Reasoning Model Knows What Counts: Self-Guided Chain-of-Thought Pruning for Efficient Reasoning*. ACL. 2026 <https://aclanthology.org/2026.acl-long.25/>
169. David H. Yang, Yuxuan Zhu, Mohammad Mohammadi Amiri et al.. *ZoomR: Memory Efficient Reasoning through Multi-Granularity Key Value Retrieval*. ACL. 2026 <https://aclanthology.org/2026.acl-long.76/>
170. Lingrui Mei, Shenghua Liu, Yiwei Wang et al.. *a1: Steep Test-time Scaling Law via Environment Augmented Generation*. ACL. 2026 <https://aclanthology.org/2026.findings-acl.1240/>
171. *4+3 Phases of Compute-Optimal Neural Scaling Laws*. NeurIPS 2024. 2024 <https://neurips.cc/virtual/2024/poster/94549>
172. *DARG: Dynamic Evaluation of Large Language Models via Adaptive Reasoning Graph*. NeurIPS 2024. 2024 <https://neurips.cc/virtual/2024/poster/96593>
173. *Repurposing Language Models into Embedding Models: Finding the Compute-Optimal Recipe*. NeurIPS 2024. 2024 <https://neurips.cc/virtual/2024/poster/93887>
174. *Resolving Discrepancies in Compute-Optimal Scaling of Language Models*. NeurIPS 2024. 2024 <https://neurips.cc/virtual/2024/poster/96646>
175. *Scaling Laws and Compute-Optimal Training Beyond Fixed Training Durations*. NeurIPS 2024. 2024 <https://neurips.cc/virtual/2024/poster/94731>
176. *TinyTTA: Efficient Test-time Adaptation via Early-exit Ensembles on Edge Devices*. NeurIPS 2024. 2024 <https://neurips.cc/virtual/2024/poster/94778>
177. *A*-Thought: Efficient Reasoning via Bidirectional Compression for Low-Resource Settings*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/115454>
178. *ARM: Adaptive Reasoning Model*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/115075>
179. *Ada-R1: Hybrid-CoT via Bi-Level Adaptive Reasoning Optimization*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/117295>
180. *AdaReasoner: Adaptive Reasoning Enables More Flexible Thinking*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/117660>
181. *AgentTTS: Large Language Model Agent for Test-time Compute-optimal Scaling Strategy in Complex Tasks*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/119334>
182. Xin Liu, Lu Wang. *Answer Convergence as a Signal for Early Stopping in Reasoning*. arXiv. 2025
183. *Are Large Reasoning Models Good Translation Evaluators? Analysis and Performance Boost*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/117120>
184. *Atom of Thoughts for Markov LLM Test-Time Scaling*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/115860>
185. *BEEM: Boosting Performance of Early Exit DNNs using Multi-Exit Classifiers as Experts*. ICLR 2025. 2025 <https://iclr.cc/virtual/2025/poster/30371>
186. *Benefits of Early Stopping in Gradient Descent for Overparameterized Logistic Regression*. ICML 2025. 2025 <https://icml.cc/virtual/2025/poster/44193>
187. Jinyan Su, Jennifer Healey, Preslav Nakov et al.. *Between Underthinking and Overthinking: An Empirical Study of Reasoning Length and correctness in LLMs*. preprint. 2025
188. *Beyond Greedy Exits: Improved Early Exit Decisions for Risk Control and Reliability*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/118222>
189. *Compute Optimal Inference and Provable Amortisation Gap in Sparse Autoencoders*. ICML 2025. 2025 <https://icml.cc/virtual/2025/poster/46270>
190. *Compute-Optimal LLMs Provably Generalize Better with Scale*. ICLR 2025. 2025 <https://iclr.cc/virtual/2025/poster/29945>
191. *Compute-Optimal Scaling for Value-Based Deep RL*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/119555>
192. *Decoder-Hybrid-Decoder Architecture for Efficient Reasoning with Long Generation*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/115542>
193. Zhongxiang Sun, Qipeng Wang, Haoyu Wang et al.. *Detection and Mitigation of Hallucination in Large Reasoning Models: A Mechanistic Perspective*. preprint. 2025
194. *DisCO: Reinforcing Large Reasoning Models with Discriminative Constrained Optimization*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/114995>
195. Gaurav Srivastava, Aafiya Hussain, Sriram Srinivasan et al.. *Do LLMs Overthink Basic Math Reasoning? Benchmarking the Accuracy-Efficiency Tradeoff in Language Models*. preprint. 2025 <https://aclanthology.org/2026.findings-acl.1285/>
196. *Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models*. ICML 2025. 2025 <https://icml.cc/virtual/2025/poster/45540>
197. *Does Thinking More Always Help? Mirage of Test-Time Scaling in Reasoning Models*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/115605>
198. Linan Yue, Yichao Du, Yizhi Wang et al.. *Don't Overthink It: A Survey of Efficient R1-style Large Reasoning Models*. preprint. 2025
199. *Don’t Think Longer, Think Wisely: Optimizing Thinking Dynamics for Large Reasoning Models*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/116095>
200. *Dualformer: Controllable Fast and Slow Thinking by Learning with Randomized Reasoning Traces*. ICLR 2025. 2025 <https://iclr.cc/virtual/2025/poster/29093>
201. *Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/116060>
202. *Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Time Scaling Evaluators*. ICML 2025. 2025 <https://icml.cc/virtual/2025/poster/46046>
203. *Every Rollout Counts: Optimal Resource Allocation for Efficient Test-Time Scaling*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/115239>
204. *Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning*. ICML 2025. 2025 <https://icml.cc/virtual/2025/poster/46117>
205. *FreqExit: Enabling Early-Exit Inference for Visual Autoregressive Models via Frequency-Aware Guidance*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/119216>
206. *From Judgment to Interference: Early Stopping LLM Harmful Outputs via Streaming Content Monitoring*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/116186>
207. *How Far Are We from Optimal Reasoning Efficiency?*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/118341>
208. Ayeong Lee, Ethan Che, Tianyi Peng. *How Well do LLMs Compress Their Own Chain-of-Thought? A Token Complexity Approach*. preprint. 2025
209. *Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving*. ICLR 2025. 2025 <https://iclr.cc/virtual/2025/poster/29417>
210. *Instance-dependent Early Stopping*. ICLR 2025. 2025 <https://iclr.cc/virtual/2025/poster/29782>
211. Aryo Pradipta Gema, Alexander Hägele, Runjin Chen et al.. *Inverse Scaling in Test-Time Compute*. Transactions on Machine Learning Research (TMLR). 2025 <https://iclr.cc/virtual/2026/poster/10014059>
212. *Inverse Scaling: When Bigger Isn't Better*. ICLR 2025. 2025 <https://iclr.cc/virtual/2025/poster/31511>
213. *Kinetics: Rethinking Test-Time Scaling Law*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/115931>
214. *LIMOPro: Reasoning Refinement for Efficient and Effective Test-time Scaling*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/117621>
215. *Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/118864>
216. *Let LRMs Break Free from Overthinking via Self-Braking Tuning*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/115532>
217. *LongVU: Spatiotemporal Adaptive Compression for Long Video-Language Understanding*. ICML 2025. 2025 <https://icml.cc/virtual/2025/poster/44939>
218. *MIND over Body: Adaptive Thinking using Dynamic Computation*. ICLR 2025. 2025 <https://iclr.cc/virtual/2025/poster/30390>
219. *Measuring the Faithfulness of Thinking Drafts in Large Reasoning Models*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/120231>
220. *MindJourney: Test-Time Scaling with World Models for Spatial Reasoning*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/118581>
221. Yao Huang, Huanran Chen, Shouwei Ruan et al.. *Mitigating Overthinking in Large Reasoning Models via Manifold Steering*. 39th Conference on Neural Information Processing Systems (NeurIPS 2025). 2025 <https://neurips.cc/virtual/2025/poster/119969>
222. *No Loss, No Gain: Gated Refinement and Adaptive Compression for Prompt Optimization*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/118743>
223. Leheng Sheng, An Zhang, Zijian Wu et al.. *On Reasoning Strength Planning in Large Reasoning Models*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/118916>
224. Mohan Zhang, Yihua Zhang, Jinghan Jia et al.. *One Token Embedding Is Enough to Deadlock Your Large Reasoning Model*. 39th Conference on Neural Information Processing Systems (NeurIPS 2025). 2025 <https://neurips.cc/virtual/2025/poster/116766>
225. Pranjal Aggarwal, Seungone Kim, Jack Lanchantin et al.. *OptimalThinkingBench: Evaluating Over and Underthinking in LLMs*. ICLR 2026. 2025 <https://iclr.cc/virtual/2026/poster/10009890>
226. *Optimizing Test-Time Compute via Meta Reinforcement Finetuning*. ICML 2025. 2025 <https://icml.cc/virtual/2025/poster/45154>
227. *Provable Scaling Laws for the Test-Time Compute of Large Language Models*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/118984>
228. *QFFT, Question-Free Fine-Tuning for Adaptive Reasoning*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/119264>
229. *QUTE: Quantifying Uncertainty in TinyML models with Early-exit-assisted ensembles for model-monitoring*. ICML 2025. 2025 <https://icml.cc/virtual/2025/poster/45956>
230. *Reasoning Models Hallucinate More: Factuality-Aware Reinforcement Learning for Large Reasoning Models*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/118780>
231. *Reinforcement Learning Teachers of Test Time Scaling*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/115573>
232. *Rethinking Fine-Tuning when Scaling Test-Time Compute: Limiting Confidence Improves Mathematical Reasoning*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/116423>
233. *Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/117041>
234. Keqin Peng, Liang Ding, Yuanxin Ouyang et al.. *Revisiting Overthinking in Long Chain-of-Thought from the Perspective of Self-Doubt*. preprint. 2025
235. *S-GRPO: Early Exit via Reinforcement Learning in Reasoning Models*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/115333>
236. *Sampling-Efficient Test-Time Scaling: Self-Estimating the Best-of-N Sampling in Early Decoding*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/119365>
237. *Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning*. ICLR 2025. 2025 <https://iclr.cc/virtual/2025/poster/31024>
238. *Scaling Test-Time Compute Without Verification or RL is Suboptimal*. ICML 2025. 2025 <https://icml.cc/virtual/2025/poster/44733>
239. *Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/117966>
240. *ShorterBetter: Guiding Reasoning Models to Find Optimal Inference Length for Efficient Reasoning*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/118481>
241. *Smaller, Weaker, Yet Better: Training LLM Reasoners via Compute-Optimal Sampling*. ICLR 2025. 2025 <https://iclr.cc/virtual/2025/poster/31080>
242. *SolverLLM: Leveraging Test-Time Scaling for Optimization Problem via LLM-Guided Search*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/116215>
243. Xiao Pu, Michael Saxon, Wenyue Hua et al.. *THOUGHTTERMINATOR: Benchmarking, Calibrating, and Mitigating Overthinking in Reasoning Models*. preprint. 2025
244. Alejandro Cuadron, Dacheng Li, Wenjie Ma et al.. *The Danger of Overthinking: Examining the Reasoning-Action Dilemma in Agentic Tasks*. International Conference on Machine Learning (ICML) 2025. 2025
245. Joykirat Singh, Justin Chih-Yao Chen, Archiki Prasad et al.. *Think Right: Learning to Mitigate Under-Over Thinking via Adaptive, Attentive Compression*. preprint. 2025
246. *Think Smarter not Harder: Adaptive Reasoning with Inference Aware Optimization*. ICML 2025. 2025 <https://icml.cc/virtual/2025/poster/46693>
247. *Think or Not? Exploring Thinking Efficiency in Large Reasoning Models via an Information-Theoretic Lens*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/119190>
248. *Thoughts Are All Over the Place: On the Underthinking of Long Reasoning Models*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/117581>
249. *Topology of Reasoning: Understanding Large Reasoning Models through Reasoning Graph Properties*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/116088>
250. *Towards Thinking-Optimal Scaling of Test-Time Compute for LLM Reasoning*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/119802>
251. *VideoChat-R1.5: Visual Test-Time Scaling to Reinforce Multimodal Reasoning by Iterative Perception*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/116032>
252. *WebThinker: Empowering Large Reasoning Models with Deep Research Capability*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/119715>
253. *A Simple "Motivation" Can Enhance Reinforcement Finetuning of Large Reasoning Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011610>
254. *ARES: Multimodal Adaptive Reasoning via Difficulty-Aware Token-Level Entropy Shaping*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011711>
255. *ATTS: Asynchronous Test-Time Scaling via Conformal Prediction*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10008898>
256. *AdaNav: Adaptive Reasoning with Uncertainty for Vision-Language Navigation*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/61535>
257. *Adaptive Thinking: Large Language Models Know When to Think in Latent Space*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011708>
258. *AdvChain: Adversarial Chain-of-Thought Tuning for Robust Safety Alignment of Large Reasoning Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10007590>
259. *Aligning Tree-Search Policies with Fixed Token Budgets in Test-Time Scaling of LLMs*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/63795>
260. *Anytime Safe PAC Efficient Reasoning*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/62243>
261. *Are Large Reasoning Models Interruptible?*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/61807>
262. *Asymptotic Universal Alignment: A New Alignment Framework via Test-Time Scaling*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/66584>
263. *AsyncSpade: Efficient Test-Time Scaling with Asynchronous Sparse Decoding*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/63012>
264. *Base Models Know How to Reason, Thinking Models Learn When*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/66610>
265. *BeaconKV: Key-Value Cache Compression Guided by Beacon Queries for Efficient Large Reasoning Model Inference*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/62942>
266. *Better, Faster: Harnessing Self-Improvement in Large Reasoning Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/64514>
267. *CaTS: Calibrated Test-Time Scaling for Efficient LLM Reasoning*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10007848>
268. *Cache Coherent Resampling for Efficient Test Time Scaling in LLM Reasoning via Adaptive Sequential Monte Carlo*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/64829>
269. *Causal Dependency-Aware Unsupervised Routing for Large Reasoning Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/64247>
270. *Certain Head, Uncertain Tail: Expert-Sample for Test-Time Scaling in Fine-Grained MoE*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/62643>
271. *CodeChemist: Test-Time Scaling for Low-Resource Code Generation via Functional Knowledge Transfer*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/63512>
272. *Compute-Optimal Quantization-Aware Training*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10009552>
273. *ConPress: Learning Efficient Reasoning from Multi-Question Contextual Pressure*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/61485>
274. *Conditional Advantage Estimation for Reinforcement Learning in Large Reasoning Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10010855>
275. *Conformal Prediction for Early Stopping in Mixed Integer Optimization*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/61715>
276. *ContextPRM: Leveraging Contextual Coherence for multi-domain Test-Time Scaling*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011128>
277. Yi Fang, Wenjie Wang, Mingfeng Xue et al.. *Controllable LLM Reasoning via Sparse Autoencoder-Based Steering*. Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers). 2026
278. Dongkyu Cho, Amy B. Z. Zhang, Bilel Fehri et al.. *Correct Reasoning Paths Visit Shared Decision Pivots*. preprint. 2026
279. *D-CORE: Incentivizing Task Decomposition in Large Reasoning Models for Complex Tool Use*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/61056>
280. *DR$^2$Seg: Decomposed Two-Stage Rollouts for Efficient Reasoning Segmentation in Multimodal Large Language Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/62304>
281. *DRPO: Efficient Reasoning via Decoupled Reward Policy Optimization*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10010492>
282. Zicheng Xu, Xiuyi Lou, Guanchu Wang et al.. *DTS: Enhancing Large Reasoning Models via Decoding Tree Sketching*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/61328>
283. Xiang Liu, Xuming Hu, Xiaowen Chu et al.. *DiffAdapt: Difficulty-Adaptive Reasoning for Token-Efficient LLM Inference*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011403>
284. *Distilled Pretraining: A modern lens of Data, In-Context Learning and Test-Time Scaling*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10009683>
285. *Diversity Matters: Revisiting Test-Time Compute in Vision-Language Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/63569>
286. *Don't Overthink with Pixels: Efficient Reasoning for Segmentation*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/61221>
287. *Doxing via the Lens: Revealing Location-related Privacy Leakage on Multi-modal Large Reasoning Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10006914>
288. *Dynamic Early Exit in Reasoning Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10009830>
289. *Dynamic Thinking-Token Selection for Efficient Reasoning in Large Reasoning Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/61200>
290. *Dynamics-Predictive Sampling for Active RL Finetuning of Large Reasoning Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10006780>
291. *ETS: Energy-Guided Test-Time Scaling for Training-Free RL Alignment*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/61604>
292. Parsa Hosseini, Sumit Nawathe, Mahdi Salmani et al.. *Early Stopping for Large Reasoning Models via Confidence Dynamics*. COLM 2026 Workshop on Efficient Reasoning. 2026
293. Jiameng Huang, Baijiong Lin, Guhao Feng et al.. *Efficient Reasoning for Large Reasoning Language Models via Certainty-Guided Reflection Suppression*. AAAI. 2026
294. *Efficient Reasoning with Balanced Thinking*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10008522>
295. *Efficient Reasoning with Hidden Thinking*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/65014>
296. *Efficient Test-Time Scaling for Small Vision-Language Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10007164>
297. *Efficient Test-Time Scaling via Hierarchical Search and Self-Verification for Discrete Diffusion Language Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/64102>
298. *Exposing Weaknesses of Large Reasoning Models through Graph Algorithm Problems*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10010419>
299. *Expressive Power of Implicit Models: Rich Equilibria and Test-Time Scaling*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10009635>
300. *FROST: Filtering Reasoning Outliers with Attention for Efficient Reasoning*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10008733>
301. *From Reasoning Traces to Reusable Modules: Understanding Compositional Generalization in Language Model Reasoning*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/61216>
302. *GTA1: GUI Test-time Scaling Agent*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011639>
303. *HardcoreLogic: Challenging Large Reasoning Models with Long-tail Logic Puzzle Games*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011195>
304. *HiDrop: Hierarchical Vision Token Reduction in MLLMs via Late Injection, Concave Pyramid Pruning, and Early Exit*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011723>
305. *IAPO: Information-Aware Policy Optimization for Token-Efficient Reasoning*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/63983>
306. *ImgCoT: Compressing Long Chain of Thought into Compact Visual Tokens for Efficient Reasoning of Large Language Model*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/63716>
307. *Internalizing Safety Understanding in Large Reasoning Models via Verification*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/63605>
308. *Is it Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10010463>
309. *KLAS: Using Similarity to Stitch Neural Networks for Improved Accuracy-Efficiency Tradeoffs*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10007961>
310. *Knowing When to Quit: Probabilistic Early Exits for Speech Separation Networks*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10009506>
311. *Learning Generalized Trackers with Elastic Token Budgets*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/63126>
312. *Less Diverse, Less Safe: The Indirect But Pervasive Risk of Test-Time Scaling in Large Language Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/64671>
313. Zhen Yang, Mingyang Zhang, Feng Chen et al.. *Less is More: Improving LLM Reasoning with Minimal Test-Time Intervention*. Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers). 2026
314. *Mechanistic Detection and Mitigation of Hallucination in Large Reasoning Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10008968>
315. *Mind the Budget: Accelerating Deep Reinforcement Learning using Constrained Early Exit Neural Networks*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/61963>
316. *Mixture-of-Visual-Thoughts: Exploring Context-Adaptive Reasoning Mode Selection for General Visual Reasoning*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011171>
317. *Mode-conditioning unlocks superior test-time compute scaling*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10010159>
318. *Modeling Hierarchical Thinking in Large Reasoning Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/64487>
319. *On the Limits of Test-Time Compute: Sequential Reward Filtering for Better Inference*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/64598>
320. *OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10006973>
321. *Optimal Aggregation of LLM and PRM Signals for Efficient Test-Time Scaling*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10006667>
322. *Optimal Self-Consistency for Efficient Reasoning with Large Language Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/61225>
323. *Overthinking Reduction with Decoupled Rewards and Curriculum Data Scheduling*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10007765>
324. *Overthinking: Amplifying Reasoning Weights to Extract Learned Secrets*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/63085>
325. *PEAR: Phase Entropy Aware Reward for Efficient Reasoning*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10010398>
326. *ParoQuant: Pairwise Rotation Quantization for Efficient Reasoning LLM Inference*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011824>
327. *Plan and Budget: Effective and Efficient Test-Time Scaling on Reasoning Large Language Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10008460>
328. *Pruning Long Chain-of-Thought of Large Reasoning Models via Small-Scale Preference Optimization*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011162>
329. *Pushing Test-Time Scaling Limits of Deep Search with Asymmetric Verification*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10008007>
330. *QuRL: Low-Precision Reinforcement Learning for Efficient Reasoning*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10008335>
331. *R-Horizon: How Far Can Your Large Reasoning Model Really Go in Breadth and Depth?*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10007149>
332. *RAEE: A Robust Retrieval-Augmented Early Exit Framework for Efficient Inference*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10010491>
333. *RAIN-Merging: A Gradient-Free Method to Enhance Instruction Following in Large Reasoning Models with Preserved Thinking Format*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10009681>
334. *REA-RL: Reflection-Aware Online Reinforcement Learning for Efficient Reasoning*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10010716>
335. *RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011763>
336. *ROC-n-reroll: How verifier imperfection affects test-time scaling*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011656>
337. *Real-Time Monitoring and Calibration of Chain-of-Thought Sycophancy in Large Reasoning Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/61298>
338. *Real-Time Visual Attribution Streaming in Thinking Model*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/62671>
339. *Reasoning or Retrieval? A Study of Answer Attribution on Large Reasoning Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10010758>
340. Wenhui Tan, Fiorenzo Parascandolo, Enver Sanginetto et al.. *Restoring Exploration after Post-Training: Latent Exploration Decoding for Large Reasoning Models*. Proceedings of the 43rd International Conference on Machine Learning (ICML), PMLR 306. 2026 <https://icml.cc/virtual/2026/poster/66546>
341. *Rethinking Calibration for Early-Exit Neural Networks*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/62138>
342. *Retrieval-of-Thought: Efficient Reasoning via Reusing Thoughts*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10009010>
343. *SPARC: Separating Perception And Reasoning Circuits for Test-time Scaling of VLMs*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/62906>
344. *Sample Complexity and Representation Ability of Test-time Scaling Paradigms*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10009511>
345. *Sample More to Think Less: Group Filtered Policy Optimization for Concise Reasoning*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10009238>
346. *Scaling Up, Speeding Up: A Benchmark of Speculative Decoding for Efficient LLM Test-Time Scaling*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10010752>
347. Siyuan Wang, Yanchen Liu, Xiang Ren. *Segment-Level Attribution for Selective Learning of Long Reasoning Traces*. arXiv.org. 2026 <https://www.semanticscholar.org/paper/004113a0556d9524d1015c51c08267a98eb2aa31>
348. *Short Chains, Deep Thoughts: Balancing Reasoning Efficiency and Intra-Segment Capability via Split-Merge Optimization*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/64198>
349. *Small Generalizable Prompt Predictive Models Can Steer Efficient RL Post-Training of Large Reasoning Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/60937>
350. *SmartThinker: Progressive Chain-of-Thought Length Calibration for Efficient Large Language Model Reasoning*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/64022>
351. *SpecExit: Accelerating Large Reasoning Model via Speculative Exit*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/66249>
352. *Statistical Early Stopping for Reasoning Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/63833>
353. *Stop Unnecessary Reflection: Training LRMs for Efficient Reasoning with Adaptive Reflection and Length Coordinated Penalty*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10008702>
354. Dehai Min, Giovanni Vaccarino, Huiyi Chen et al.. *Stop When Reasoning Converges: Semantic-Preserving Early Exit for Reasoning Models*. preprint. 2026
355. *Strategic Scaling of Test-Time Compute: A Bandit Learning Approach*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011899>
356. *SuCo: Sufficiency-guided Continuous Adaptive Reasoning*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/63630>
357. *SwiftPFN: Revisiting Row-Wise Attention–Only Tabular Foundation Models with Adaptive Early Exit*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/61560>
358. *T1: Tool-integrated Verification for Test-time Compute Scaling in Small Language Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10007001>
359. *TEST-TIME SCALING IN DIFFUSION LLMS VIA HIDDEN SEMI-AUTOREGRESSIVE EXPERTS*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10010063>
360. *TUMIX: Multi-Agent Test-Time Scaling with Tool-Use Mixture*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10010417>
361. *TaTToo: Tool-Grounded Thinking PRM for Test-Time Scaling in Tabular Reasoning*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10006442>
362. *Test-Time Scaling with Reflective Generative Model*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10006997>
363. Zihao Wei, Liang Pang, Jiahao Liu et al.. *The Evolution of Thought: Tracking LLM Overthinking via Reasoning Dynamics Analysis*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1239/>
364. Renfei Dang, Zhening Li, Shujian Huang et al.. *The First Impression Problem: Internal Bias Triggers Overthinking in Reasoning Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011746>
365. *The Quest for Efficient Reasoning: A Data-Centric Benchmark to CoT Distillation*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10010734>
366. *Theoretical Guarantees for One-Shot Magnitude Pruning and Compute-Adaptive Early Exit*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/63550>
367. *ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10009980>
368. *Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/64256>
369. *Think Less, Act Early: Reinforced Latent Reasoning with Early Exit in Vision-Language-Action Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/61571>
370. Bo Cheng, Qiaolin Lu, Yi Chang et al.. *Thinking vs. NoThinking: Towards Interpreting Reasoning Mechanisms of Large Language Models via Sparse Autoencoders*. preprint. 2026
371. *ThreadWeaver: Adaptive Threading for Efficient Parallel Reasoning in Language Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/65330>
372. *Towards Safe Reasoning in Large Reasoning Models via Corrective Intervention*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011693>
373. Yi Hu, Jiaqi Gu, Ruxin Wang et al.. *Towards a Mechanistic Understanding of Large Reasoning Models: A Survey of Training, Inference, and Failures*. preprint. 2026 <https://aclanthology.org/2026.acl-long.889/>
374. *Training Large Reasoning Models Efficiently via Progressive Thought Encoding*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10007286>
375. *TrimR: Verifier-based Training-Free Thinking Trimming for Efficient Test-Time Scaling*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10007390>
376. *UnMaskFork: Test-Time Scaling for Masked Diffusion via Deterministic Action Branching*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/66823>
377. *Understanding the Role of Training Data in Test-Time Scaling*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10008915>
378. *UniScale: Adaptive Unified Inference Scaling via Online Joint Optimization of Model Routing and Test-Time Scaling*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/60578>
379. *VLA-ATTC: Adaptive Test-Time Compute for VLA Models with Relative Action Critic Model*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/61157>
380. *WAVE: Window-Aware Vocabulary-Efficient Early-Exit for Training-Free LLM Acceleration*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/62373>
381. *WS-GRPO: Weakly-Supervised Group-Relative Policy Optimization for Rollout-Efficient Reasoning*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/64686>
382. *Wait, Do We Need to Wait? Revisiting Budget Forcing for Sequential Test-Time Scaling*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10012115>
383. *What If We Allocate Test-Time Compute Adaptively?*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/60797>
384. Shu Zhou, Rui Ling, Junan Chen et al.. *When More Thinking Hurts: Overthinking in LLM Test-Time Compute Scaling*. preprint. 2026 <https://aclanthology.org/2026.findings-acl.1199/>
385. *When More is Less: Understanding Chain-of-Thought Length in LLMs*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011380>
386. *When Reasoning Meets Compression: Understanding the Effects of LLMs Compression on Large Reasoning Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011689>
387. *When Simple Problems Wear Complex Costumes: Improving Efficiency in LRM's Adaptive Reasoning*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/62755>
388. *Your Models Have Thought Enough: Training Large Reasoning Models to Stop Overthinking*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011695>
389. *Zero-Overhead Introspection for Adaptive Test-Time Compute*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10010457>
390. *e3: Learning to Explore Enables Extrapolation of Test-Time Compute for LLMs*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10008718>
391. Tianyang Zhou, Somesh Jha, Mihai Christodorescu et al.. *Verifier-Guided Code Translation via Meta-Step Decoding*. arXiv.org. 2026 <https://www.semanticscholar.org/paper/0033708ee454d5ea4c7b6ed0f9424e63baf9b395>
392. Kaishen Wang, Tong Zheng, Xuehao Cui et al.. *Mitigating Factual Hallucination in Large Reasoning Models via Mixed-Mode Advantage Regularization*. arXiv. 2026 <https://www.semanticscholar.org/paper/0294e3ee8794087f78b1cd58a21c3b4ab12f7f56>
393. Xinbang Dai, Zheyu Xin, Huikang Hu et al.. *EvoThink: Evolving Thinking in Large Reasoning Models via Self-Pruning and Aha-Moment Preference Optimization*. cs.AI. 2026 <https://arxiv.org/abs/2607.19962>
394. Runyang You, Zhiyuan Liu, Yongqi Li et al.. *SLPO: Scaling Latent Reasoning via a Surrogate Policy*. cs.CL. 2026 <https://arxiv.org/abs/2607.19691>
395. Siwei Chen, Siqi Chen, Xupeng Miao et al.. *QLPO: Quadrant-weighted Sampling for Length-aware Policy Optimization*. cs.AI. 2026 <https://arxiv.org/abs/2607.21793>
396. Renuka Oladri, Niveda Jawahar, Abdirisak Mohamed. *Token Budget Saturation and Mechanistic Early Detection of Reasoning Non-Convergence in Chain-of-Thought Models*. cs.CL. 2026 <https://arxiv.org/abs/2607.21433>
397. Junlin Fang, Do Nguyen-Thanh, Xiaogang Xu et al.. *Reasoning Denoiser: Denoising Reasoning Traces for Hallucination Detection in Large Reasoning Models*. cs.AI. 2026 <https://arxiv.org/abs/2607.22098>
398. Jiarun Fu, Lizhong Ding, Sida Chen et al.. *CHILL-Harness: Counterfactual Harness Learning for Efficient Reasoning in Long-Horizon Agents*. arXiv. 2026 <https://www.semanticscholar.org/paper/00a392559287f448c41d331f0e43694389177348>
399. Yutong Chen, Shouqian Shi, Xinran Liu et al.. *Penelope: Localized Latent Recurrence for Efficient Structured Reasoning*. cs.AI. 2026 <https://arxiv.org/abs/2607.25915>
400. Chia-Ming Lee, Shao-Kai Liu, Ming-Ching Chang et al.. *Commit Locally, Exit Globally: Coordinating Adaptive Sampling and Early Exit in Diffusion Language Models*. cs.CL. 2026 <https://arxiv.org/abs/2607.28166>
401. Sara Candussio, Daniel Scalena, Luca Bortolussi et al.. *Demystifying Entropy-based Selection for Chain-of-Thought Compression in Large Reasoning Models*. cs.CL. 2026 <https://arxiv.org/abs/2607.28707>
402. Keshu Fu, Keqin Peng, Jun Bai et al.. *BLADE: Boundary-Expanded and Layer-Adaptive Dynamic Exit for Efficient LLM Reasoning*. cs.CL. 2026 <https://arxiv.org/abs/2607.28966>
403. Yongshi Ye, Biao Fu, Chongxuan Huang et al.. *Translation with Thought: Difficulty-Adaptive Reasoning via Reinforcement Learning for Multi-Domain Machine Translation*. ACL. 2026 <https://aclanthology.org/2026.acl-long.1400/>
404. Faizan Faisal, Prem Devanbu, Toufique Ahmed. *Distilling Reasoning Traces into Advisory Prompts for Software Engineering Tasks*. cs.SE. 2026 <https://arxiv.org/abs/2608.00437>
405. Jingqi Tian, Haoji Zhang, Lin Chen et al.. *AdaThinkV: Adaptive Thinking for Token-Efficient Video Reasoning*. cs.CV. 2026 <https://arxiv.org/abs/2608.01980>
406. Mengting Ai, Jingrui He, Yue Guo. *Does Accuracy Equal Evidence? Reasoning Faithfulness under KV Cache Compression*. cs.CL. 2026 <https://arxiv.org/abs/2608.01631>
407. Xiaocheng Lu, Hualei Zhang, Shuhan Guo et al.. *OPTD: On-Policy Transition Distillation with Consistency-Guided Adaptive Compression for Few-Step Diffusion Language Models*. cs.CL. 2026 <https://arxiv.org/abs/2608.02942>
408. Mobina Kashaniyan, Ali Jannesari. *Interpretable Adaptive Sampling for LLM Test-Time Scaling*. cs.AI. 2026 <https://arxiv.org/abs/2608.03961>
409. Dominik Meier, Luca Joshua Francis, Marco Bernhard Kaiser et al.. *Risky Business: Measuring The Faithfulness-Safety Tension*. cs.AI. 2026 <https://arxiv.org/abs/2608.03745>
410. Mohsen Hariri, Weicong Chen, Nahal Shahini et al.. *Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility*. cs.LG. 2026 <https://arxiv.org/abs/2608.04001>
411. Qiyuan Zhu, Dezhi Li, Pengyu Cheng et al.. *Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning*. cs.AI. 2026 <https://arxiv.org/abs/2608.04771>
412. Ahsan Bilal, Muhammad Ahmed Mohsin, Muhammad Umer et al.. *Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning*. cs.AI. 2026 <https://arxiv.org/abs/2608.05643>
413. Yan Zhou, Yue Ouyang, Kaiyang Zheng et al.. *CoBa: Cost-Effective Test-Time Scaling via Compute-Balanced Routing*. cs.AI. 2026 <https://arxiv.org/abs/2608.07424>
414. Agamdeep Singh, Srishti Gautam, Priyanshu Gupta et al.. *Reason Wide, Not Deep: Amortizing the Reasoning Premium into Distilled Skills*. cs.AI. 2026 <https://arxiv.org/abs/2608.07885>
415. Chenrui Fan, Yize Cheng, Ming Li et al.. *Thinking Hard, Not Smart: Reasoning Models Fail to Ration Test-Time Compute Across Questions*. cs.CL. 2026 <https://arxiv.org/abs/2608.07968>
416. Lijie Yang, Hongyin Luo, Jiawei Zhao et al.. *Thought-Level Beam Search for Reasoning*. cs.AI. 2026 <https://arxiv.org/abs/2608.08020>
417. Juncheng Dong, Ding Tong, Ishan Gupta et al.. *LLM Reasoning for Subjective Tasks: Failure Modes, Mitigation, and Dynamic Reasoning Routing*. cs.AI. 2026 <https://arxiv.org/abs/2608.08889>
418. Lecheng Kong, Like Hui, Haitao Mao et al.. *Consilience for Verifier-Free Test-Time Scaling*. cs.CL. 2026 <https://arxiv.org/abs/2608.09898>
419. Alexander Panfilov, David Schmotz, Ilia Shumailov et al.. *Stealing Reasoning Traces from Proprietary LLM APIs*. cs.CR. 2026 <https://arxiv.org/abs/2608.09867>
420. Vaibhav Singh, Soumya Suvra Ghosal, Sarvesh Gharat et al.. *ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling*. cs.AI. 2026 <https://arxiv.org/abs/2608.10928>
421. Linh Dieu Le, Tong Chen, Shazia Sadiq et al.. *Towards Efficient Reasoning in LLM-Based Recommender Systems via Model Merging*. cs.IR. 2026 <https://arxiv.org/abs/2608.10447>
422. Sen Xu, Wei Wang, Shixi Liu et al.. *Claim-Level Reliability Assessment for Efficient Test-Time Reasoning*. cs.AI. 2026 <https://arxiv.org/abs/2608.11994>
423. Congchao Wang, Diwakar Singh, Qiaozi Gao et al.. *Reasoning Jury: Multi-Model Consensus for Evaluating Reasoning Traces*. cs.AI. 2026 <https://arxiv.org/abs/2608.12585>
424. Xinmu Ge, Zizhuo Zhang, Yu Huang et al.. *Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling*. cs.LG. 2026 <https://arxiv.org/abs/2608.11829>
425. Jean de Dieu Nyandwi, Leena Mathur, Yonatan Bisk et al.. *Amplified Does Not Mean Predictive: Reasoning Behaviors in Thinking Models*. cs.CL. 2026 <https://arxiv.org/abs/2608.13760>
426. Ahmet Bugra Gundogan, Yigit Turkmen, Melih Bastopcu. *Keep, Customize, or Exit: Default Design and Token Pricing in LLM Reasoning Services*. cs.GT. 2026 <https://arxiv.org/abs/2608.13315>
427. Varsha Ramineni, Hossein A. Rahmani, Jerome Ramos et al.. *BiasTrace: Linking Reasoning Behaviours to Biased Outputs in LLMs*. cs.AI. 2026 <https://arxiv.org/abs/2608.14161>
428. Bo Wen, Yuhao Chen, Erhan Bilal et al.. *Divergent-Convergent Reasoning: Scaling Test-Time Compute through Structured Solution Synthesis*. cs.AI. 2026 <https://arxiv.org/abs/2608.15303>
429. Chanhee Park, Sungbin Han, Jeongho Yoon et al.. *Funnel of Thoughts: Efficient Test-Time Scaling via Early Voting and Rollout Pruning*. cs.AI. 2026 <https://arxiv.org/abs/2608.15065>
430. Yeabin Moon. *The Price of Thinking: Reasoning Effort as a Model-Specific API Contract*. cs.AI. 2026 <https://arxiv.org/abs/2608.16956>
431. Xuteng Zhang, Wenhao Zeng, Xiaodong Gu et al.. *ParaTempo: Efficient Parallel Reasoning via Temporal Confidence*. cs.AI. 2026 <https://arxiv.org/abs/2608.16425>
432. Ivan Viakhirev, Kirill Borodin, Amirah Almutairi et al.. *Think Shallow, Solve Deep: Controlling Recurrent Dynamics for Reliable Test-Time Depth*. cs.LG. 2026 <https://arxiv.org/abs/2608.18222>
433. Zishan Ahmad, Vishal Vaddina. *Can a Lightweight Multimodal Model Estimate LLM Reasoning Performance? A Study for Compute-Optimal Document Inference*. cs.AI. 2026 <https://arxiv.org/abs/2608.18591>
434. Jian Yang, Zhenqi Feng, Zhaoyang Yu et al.. *SMTrap: Cost-Effective DoS Attacks Against Large Reasoning Models via SMT Conflict Guidance*. cs.CL. 2026 <https://arxiv.org/abs/2608.18921>
435. Davide Romano, Kanak Raj, Jerrod Parker et al.. *Test-Time Scaling in the Wild: Why Exploitation, Not Exploration, Is the Bottleneck*. cs.CL. 2026 <https://arxiv.org/abs/2608.18931>
436. Wei Yu, Suxing Liu, Minjie Yu et al.. *Training-Free Inference-Time Self-Reflection and Cost-Bounded Early Stopping for Large Language Models*. cs.AI. 2026 <https://arxiv.org/abs/2608.18884>
437. Yiting Qu, Ziqing Yang, Chi Cui et al.. *EchoCoT: Extracting Hidden Chain-of-Thought from Large Reasoning Models*. cs.CR. 2026 <https://arxiv.org/abs/2608.20055>
438. Gijs Kassenaar, Zhao Yang, Vincent François-Lavet. *Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation*. cs.AI. 2026 <https://arxiv.org/abs/2608.20256>
439. Weihang Pan, Zhengxu Yu, Yuxiang Zhang et al.. *ChainPrune: Evaluating and Reducing Redundancy in Long Chain-of-Thought Reasoning*. cs.LG. 2026 <https://arxiv.org/abs/2608.21860>
440. Chandresh Pandey. *More Experts, Worse Dynamics: Inverse Scaling and Spectral Bias in Mixture-of-Experts State-Space Models*. cs.LG. 2026 <https://arxiv.org/abs/2608.21840>
441. Kang Chen, Junjie Nian, Yixin Cao et al.. *Disagree to Explore, Agree to Commit: Routing-Guided Test-Time Scaling for Software Agents*. cs.AI. 2026 <https://arxiv.org/abs/2608.22191>
442. Maria-Eleni Zoumpoulidi, Georgios Paraskevopoulos, Alexandros Potamianos. *Cognitive Profiling of LRMs' Reasoning Traces Using Bloom's Taxonomy*. cs.AI. 2026 <https://arxiv.org/abs/2608.23205>
443. Sujoy Nath, Aswini Kumar, Tanmoy Chakraborty. *Counter with Evidence! A Multi-Agent Memory Efficient Reasoning Framework for Hate Category Informed Counterspeech Generation*. cs.CL. 2026 <https://arxiv.org/abs/2608.23152>
444. Min Chen, Shengjun Zhang, Yuxin Li et al.. *ParallelWorld: Test-Time Scaling for Embodied Reasoning*. cs.AI. 2026 <https://arxiv.org/abs/2608.22971>
445. Duy Hoang, Bastien Berret, Olivier Bruneau et al.. *A Data-dependent Early Stopping Rule using Rademacher Complexity with L1-norm*. cs.LG. 2026 <https://arxiv.org/abs/2608.24210>
446. Hyunho Kook, Junhyuk So, Tianyu Fu et al.. *Beyond Confidence: Test-Time Scaling for Multi-Turn Search Agents via Retrieval Grounding*. cs.AI. 2026 <https://arxiv.org/abs/2608.24024>
447. Zhengyang Zhang, Zijian Zhang, Jiaxuan Gao et al.. *Parason: Revealing Subtask and Trial Parallelism in LLM Reasoning*. cs.AI. 2026 <https://arxiv.org/abs/2608.24658>
448. Shengxin Zhang, Xiaomin Wu, Xiyang Wu et al.. *Recursive Agentic Reasoning*. cs.AI. 2026 <https://arxiv.org/abs/2608.23956>
449. Zhenyu Wu, Siyuan Chen, Changchun Yang et al.. *TRACE: An Evidence-Grounded Benchmark for Safety Evaluation of Large Reasoning Models*. cs.AI. 2026 <https://arxiv.org/abs/2608.24232>
450. Lehong Wu, Yuxiao Qu, Zheyuan Hu et al.. *$R^3$: Training Robots to Reason in Natural Language via Reinforcement Learning*. cs.RO. 2026 <https://arxiv.org/abs/2608.26053>
451. Caixing Wang, Zhibo Chen, Yue Wang. *Adaptive Regularization for Random Features: A Neighboring Early-Stopping Rule with Oracle-Rate Guarantees*. stat.ML. 2026 <https://arxiv.org/abs/2608.25513>
452. Lam So, Canhui Wu, Han Lin. *GRIP: Granular Reward-Guided Parameter Interpolation for Efficient Reasoning*. cs.CL. 2026 <https://arxiv.org/abs/2608.25583>
453. Niklas Muennighoff, Zhengyang Wang, Zeyi Chen et al.. *Prefix Sliding for efficient test-time scaling*. cs.CL. 2026 <https://arxiv.org/abs/2608.26070>
454. Jiarui Hu, Zhiyuan Wen, Xiaoyun Liu et al.. *Reflection Steering: Disentangling Reflection from Reasoning in Activation Space for Token-Efficient Inference*. cs.LG. 2026 <https://arxiv.org/abs/2608.25542>
455. Pratyay Banerjee, Ankit Chadha. *Routed Graph Handoff: Adaptive Format Selection for Multi-Agent LLM Delegation*. cs.CL. 2026 <https://arxiv.org/abs/2608.25277>
456. Wanli Cheng, Haiya Xiang, Juntao Li et al.. *SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing*. cs.AI. 2026 <https://arxiv.org/abs/2608.27963>
457. Zhangdie Yuan, Andreas Vlachos. *Evaluating the Semantic Specificity of Representation Steering in Language Models*. cs.CL. 2026 <https://arxiv.org/abs/2608.29431>
458. Henry Arthur. *Thinking effort aligns between humans and reasoning models in abductive reasoning*. cs.CL. 2026 <https://arxiv.org/abs/2609.01867>
459. Takeru Hiramatsu, Kyohei Atarashi, Koh Takeuchi et al.. *Disentangling Steering Vectors*. cs.LG. 2026 <https://arxiv.org/abs/2609.07037>
460. Ha Lan Nguyen, Huy Hoang Tran, Trac-Duy Tran et al.. *OBC-Prune: Outcome-Based Calibration for Large Reasoning Model Pruning*. cs.AI. 2026 <https://arxiv.org/abs/2609.17890>
