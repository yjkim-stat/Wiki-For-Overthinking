# Overthinking

_Lecture note assembled from the research archive_

> Generated on 2026-08-20 from 154 archived source(s).
> Regenerated on every render — put your own material in a separate file.

## Scope

When and why large reasoning models think more than a problem needs (or less than it needs) — the accuracy/efficiency tradeoff of reasoning length, test-time compute scaling, and methods to make a model stop, or keep going, at the right point.

Built from 154 paper(s) and 0 recording(s) spanning 2025-01-01 to 2026-08-19. 154 of the papers have been read in full.

Tracked terms: `overthinking`, `underthinking`, `over-thinking`, `under-thinking`, `reasoning length`, `test-time compute`, `test time scaling`, `inverse scaling`, `chain-of-thought length`, `thinking budget`, `reasoning-action dilemma`, `large reasoning model`, `adaptive compression`, `accuracy-efficiency tradeoff`.

## Where the field stands

### 2026

- **SMTrap: Cost-Effective DoS Attacks Against Large Reasoning Models via SMT Conflict Guidance** — SMTrap uses SMT solver conflict counts as a free, model-feedback-free proxy to synthesize Sudoku and zebra-puzzle queries that induce excessive backtracking-driven reasoning in large reasoning models, mounting a state-of-the-art denial-of-service attack that a bounded-solver defense can neutralize.
- **Test-Time Scaling in the Wild: Why Exploitation, Not Exploration, Is the Bottleneck** — A compute-normalised, five-benchmark comparison of test-time scaling methods on open-ended generation finds that the candidate pool improves steadily with compute, but exploitation - selecting or synthesising the final answer from that pool - is the bottleneck, with reward-model-based selection near random (verifier correlation ~0.12) and even the best method (Fusion) recovering only ~40% of available quality.
- **Funnel of Thoughts: Efficient Test-Time Scaling via Early Voting and Rollout Pruning** — Funnel of Thoughts detects and discards the subset of parallel reasoning rollouts that are spiraling into unproductive self-correction (flagged by a rising density of hesitation words like 'Wait' and 'perhaps'), matching self-consistency's accuracy while cutting attention FLOPs by up to 56% and wall time by 37.6%.
- **Divergent-Convergent Reasoning: Scaling Test-Time Compute through Structured Solution Synthesis** — Divergent-Convergent Reasoning generates diverse candidate solutions and then uses reviewer-style reconciliation calls (optionally run recursively with a verifier-free unanimous-consent stopping rule) to recover correct answers even when they start out as a minority, reaching 93.3% on AIME 2024 and 92.0% on AIME 2025 while using about 27% less compute than a fixed single-round baseline.
- **Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling** — Using pass@K/avg@K analysis, the paper shows on-policy distillation improves a student model's sampling efficiency at small K but does not expand its reasoning capability boundary at large K, and even causes it to forget some previously solvable problems.
- **Claim-Level Reliability Assessment for Efficient Test-Time Reasoning** — CLR reallocates part of the test-time compute budget from generating more solution samples to falsifying a small set of decision-critical claims extracted from each trace, improving accuracy over self-consistency while using fewer tokens on some models.
- **ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling** — ThinkRetrieve augments each step of a reasoning model's chain of thought with a dynamically retrieved, fully worked solved example (rather than just facts), consistently beating standard sequential test-time scaling on math and QA benchmarks.
- **Test-Time Scaling for CAD Generation via Verifier-Free Consensus Selection** — Introduces verifier-free 'consensus selection' for text-to-CAD generation, picking among N compiled 3D CAD candidates the one that geometrically or topologically agrees most with the rest of the pool.
- **Consilience for Verifier-Free Test-Time Scaling** — Introduces consilience, a verifier-free test-time-scaling selection metric that picks the sampled reasoning rollout whose confidence starts low (exploratory) and ends high (convergent), fixing a failure mode where naive confidence maximization favors confidently wrong answers on hard problems.
- **Efficient Test-Time Scaling for LLM-based Time Series Forecasting** — Proposes SCALER, a coarse-to-fine LLM-based time-series forecaster that first predicts a lightweight global shape and then uses it to guide cheaper, fixed-step test-time refinement of the full-resolution forecast.
- **Thinking Hard, Not Smart: Reasoning Models Fail to Ration Test-Time Compute Across Questions** — Introduces an exam-style evaluation where reasoning models must divide one shared token budget across multiple questions of different difficulty and value, and finds they allocate it by presentation order rather than by difficulty or value.
- **Thought-Level Beam Search for Reasoning** — Introduces Gambit, an inference algorithm that formulates test-time reasoning as thought-level beam search, periodically pruning weak reasoning traces and branching new ones from high-quality prefixes to concentrate a fixed hardware budget on the most promising partial reasoning.
- _...and 91 more._

### 2025

- **Between Underthinking and Overthinking: An Empirical Study of Reasoning Length and correctness in LLMs** — An empirical study showing reasoning LLMs overthink easy questions and underthink hard ones, and that preferring shorter outputs via SimPO can cut generation length 30-60% with little accuracy loss.
- **Inverse Scaling in Test-Time Compute** — Constructs evaluation tasks across four categories (distractor counting, spurious-feature regression, constraint-tracking deduction, and AI-risk model-written evaluations) where letting large reasoning models reason longer at test time makes their accuracy or alignment worse, not better.
- **The Danger of Overthinking: Examining the Reasoning-Action Dilemma in Agentic Tasks** — Defines and measures 'overthinking' in Large Reasoning Models on real software-engineering agent tasks, showing that favoring internal reasoning over environment interaction correlates with lower SWE-bench issue-resolution rates and can be mitigated at lower cost.
- **Mitigating Overthinking in Large Reasoning Models via Manifold Steering** — Identifies that overthinking in large reasoning models corresponds to a low-dimensional manifold in activation space and proposes projecting steering interventions onto that manifold to cut output tokens by up to 71% without hurting accuracy.
- **On Reasoning Strength Planning in Large Reasoning Models** — Finds that large reasoning models pre-plan how much to reason via a directional vector in their activations, whose magnitude causally sets reasoning length.
- **Let LRMs Break Free from Overthinking via Self-Braking Tuning** — Introduces Self-Braking Tuning, which trains a large reasoning model to detect and stop its own redundant reasoning steps, cutting token usage by up to 60% with comparable accuracy on math benchmarks.
- **Does Thinking More Always Help? Mirage of Test-Time Scaling in Reasoning Models** — Shows that extending a reasoning model's thinking trace improves accuracy only up to a point and then declines from overthinking, and proposes sampling multiple independent short traces (parallel thinking) with majority vote as a more effective use of the same compute budget.
- **Thoughts Are All Over the Place: On the Underthinking of Long Reasoning Models** — Identifies 'underthinking' in long reasoning models, where frequent switching between reasoning thoughts prevents sufficient exploration and hurts accuracy, and proposes a decoding-time penalty to fix it.
- **Think or Not? Exploring Thinking Efficiency in Large Reasoning Models via an Information-Theoretic Lens** — Uses information-theoretic metrics (InfoBias, InfoGain) to show that longer reasoning chains in LRMs grow less informative and more divergent from an ideal path, and introduces an entropy-based stopping rule that cuts token usage while preserving accuracy.
- **Towards Thinking-Optimal Scaling of Test-Time Compute for LLM Reasoning** — Shows that scaling chain-of-thought length can hurt math reasoning past a domain-dependent optimum, and proposes a self-improvement method that teaches a model to pick the shortest correct response under varying reasoning efforts.
- **One Token Embedding Is Enough to Deadlock Your Large Reasoning Model** — The Deadlock Attack trains a backdoored adversarial token embedding that forces large reasoning models into perpetual chain-of-thought loops, achieving a 100% attack success rate across four LRMs and three math benchmarks.
- **Noise Hypernetworks: Amortizing Test-Time Compute in Diffusion Models** — Trains a hypernetwork to modulate initial noise in distilled diffusion models so that test-time-scaling quality gains are baked into a single forward pass instead of requiring explicit inference-time reward optimization.
- _...and 39 more._

## Core ideas

### overthinking

A large reasoning model spending more reasoning tokens or steps on a problem than the problem needs, in a way that either wastes compute for no accuracy gain or actively lowers accuracy (or, in one source, safety-relevant behavior) as reasoning length grows. Across the archive's 22 sources it is measured and explained several ways: an accuracy-vs-token-length curve that peaks and then falls (inverted-U); tracking a model abandoning a previously correct intermediate answer ('flip events') or reaching the right answer early and reasoning itself out of it; excessive, unproductive self-verification/backtracking loops; a low-dimensional direction in activation space; and, on agentic software-engineering tasks, favoring internal reasoning over environment interaction. It is mitigated by a wide range of methods in the corpus -- length-penalized preference optimization, self-braking/self-training, decoupled token-level rewards with curriculum scheduling, activation steering, verifier-based trimming, decoding-tree early termination, and budget-aware query decomposition -- most reporting 30-70% token reductions at little or no accuracy cost.

Seen in: Inverse Scaling in Test-Time Compute; When More Thinking Hurts: Overthinking in LLM Test-Time Compute Scaling; Towards a Mechanistic Understanding of Large Reasoning Models: A Survey of Training, Inference, and Failures; OptimalThinkingBench: Evaluating Over and Underthinking in LLMs.

### test-time scaling

Letting a model use more inference-time computation -- longer chains of thought, more parallel samples, search -- in the hope of higher accuracy. This is the umbrella term the largest number of the archive's collected papers use, spanning genuine reasoning-length work (speculative decoding for reasoning models, budget-aware tree search) and many off-topic applications the topic's keyword filter also caught (GUI agents, diffusion-model image generation, protein design) where 'test-time scaling' means something unrelated to LLM reasoning length. Note: the archive's wiki tracks this same underlying idea under at least three overlapping entries (test-time scaling, test-time compute, test-time compute scaling) that were never merged -- this is the largest and most heavily overloaded of the three, and readers should treat individual sources under it on a paper-by-paper basis rather than assuming uniform relevance.

Seen in: Scaling Up, Speeding Up: A Benchmark of Speculative Decoding for Efficient LLM Test-Time Scaling; Aligning Tree-Search Policies with Fixed Token Budgets in Test-Time Scaling of LLMs; GTA1: GUI Test-time Scaling Agent; UniScale: Adaptive Unified Inference Scaling via Online Joint Optimization of Model Routing and Test-Time Scaling.

### test-time compute scaling

Letting a language model use more inference-time computation -- a longer chain of thought, more reasoning tokens, more parallel samples, or self-refinement passes -- in the hope of higher accuracy. The archive's 9 sources treat it as non-monotonic and mechanism-dependent rather than a reliable lever: on constructed tasks, letting large reasoning models reason longer makes accuracy or alignment-relevant behavior worse, not better ('inverse scaling'); verifier-search and proposal-revision are identified as its two primary underlying mechanisms, with verification/RL-guided scaling proven to beat imitation-based scaling as the token budget grows; and its payoff is domain- and difficulty-dependent -- e.g. small parameter-efficient models gain from self-refinement, tool-integrated verification lets small models match larger ones, and 'The Danger of Overthinking' shows spending it on agentic software tasks can directly lower task-resolution rates.

Seen in: Reasoning models, test-time compute, self refinement; Inverse Scaling in Test-Time Compute; OptimalThinkingBench: Evaluating Over and Underthinking in LLMs; The Danger of Overthinking: Examining the Reasoning-Action Dilemma in Agentic Tasks.

### underthinking

The complement failure mode to overthinking: a model reasons too little on a problem that genuinely requires deliberate, multi-step reasoning. The archive's 6 sources give it several concrete mechanisms: taking the first plausible answer without exploring alternatives or verifying it (OptimalThinkingBench), failing to extend a chain of thought far enough on hard questions while overthinking easy ones (Between Underthinking and Overthinking), and frequent premature switching between partial reasoning 'thoughts' before any is followed to completion, which prevents deep exploration of a promising line of reasoning ('Thoughts Are All Over the Place', which introduces a decoding-time penalty, TIP, to discourage the switching). TrimR and Plan-and-Budget both note it as the failure mode their overthinking-trimming methods must avoid falling into.

Seen in: OptimalThinkingBench: Evaluating Over and Underthinking in LLMs; Between Underthinking and Overthinking: An Empirical Study of Reasoning Length and correctness in LLMs; Thoughts Are All Over the Place: On the Underthinking of Long Reasoning Models; OptimalThinkingBench: Evaluating Over and Underthinking in LLMs.

### process reward model

A reward model that scores the intermediate steps of a reasoning trace, used to guide test-time search rather than only rank finished answers. MetaStone-S1 shares one backbone between its policy and process-reward model; TaTToo trains a domain-specific PRM for tabular reasoning; JETTS benchmarks how well LLM-as-judge models substitute for a trained PRM in guiding test-time scaling, finding judges match outcome reward models but lag PRMs. Note: same concept as the archive's separately-tracked 'process reward model (PRM)' entry -- not merged.

Seen in: Test-Time Scaling with Reflective Generative Model; TaTToo: Tool-Grounded Thinking PRM for Test-Time Scaling in Tabular Reasoning; Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Time Scaling Evaluators; ContextPRM: Leveraging Contextual Coherence for multi-domain Test-Time Scaling.

### distillation

Training a model (or a stage of pretraining) to imitate a stronger teacher's outputs or reasoning traces, rather than learning purely from raw data or reward. The archived sources give it mixed effects on reasoning-length behavior: 'Distilled Pretraining' finds it improves test-time-scaling generalization but impairs in-context learning; 'When Reasoning Meets Compression' finds it (along with quantization and pruning) degrades reasoning ability differently than memorization ability; 'Reinforcement Learning Teachers of Test Time Scaling' trains an RL teacher specifically to produce distillation explanations that help a student learn.

Seen in: Reinforcement Learning Teachers of Test Time Scaling; Distilled Pretraining: A modern lens of Data, In-Context Learning and Test-Time Scaling; When Reasoning Meets Compression: Understanding the Effects of LLMs Compression on Large Reasoning Models.

### accuracy-efficiency tradeoff of reasoning length

The core tension the archive's sources study: a reasoning model's accuracy as a function of how many tokens it spends thinking is not monotonic — spending more improves accuracy up to a point and then wastes compute or actively hurts it (overthinking), while spending too few tokens leaves genuinely hard problems unsolved (underthinking). OptimalThinkingBench frames this as a single benchmark (OverthinkingBench + UnderthinkingBench) precisely because no evaluated model balances both sides of the tradeoff at once.

Seen in: OptimalThinkingBench: Evaluating Over and Underthinking in LLMs; OptimalThinkingBench: Evaluating Over and Underthinking in LLMs.

### AUC_OAA

A metric from OptimalThinkingBench for scoring overthinking: Overthinking-Adjusted Accuracy (OAA_t) counts a response correct only if it also stays under a thinking-token threshold t, and AUC_OAA is the area under the OAA_t curve as t sweeps up to 1000 tokens. A model that reaches the right answer but keeps generating unnecessary tokens scores lower on AUC_OAA than one that stops promptly, even at equal raw accuracy.

Seen in: OptimalThinkingBench: Evaluating Over and Underthinking in LLMs; OptimalThinkingBench: Evaluating Over and Underthinking in LLMs.

### Bayesian inference

A statistical framework for updating a belief (e.g. a prediction of prompt difficulty, or of how useful a training example will be) from prior assumptions plus observed evidence. In the archived sources it appears as the tool behind two training-efficiency methods: predicting which RL training prompts are informative from partial reward history, and a small, prompt-generic Bayesian predictor of prompt difficulty learned from shared optimization history, used to select prompts for efficient RL post-training of reasoning models.

Seen in: Dynamics-Predictive Sampling for Active RL Finetuning of Large Reasoning Models; Small Generalizable Prompt Predictive Models Can Steer Efficient RL Post-Training of Large Reasoning Models.

### contextual bandits

An online-learning framework for repeatedly choosing an action (e.g. which model to route a query to, or how much test-time compute to spend) based on context, using observed rewards to improve the choice over time. UniScale uses a bandit controller (LinUCB) to jointly decide model routing and test-time-compute allocation per query; the diffusion-model noise-trajectory-search paper casts its epsilon-greedy noise search the same way -- though that application is unrelated to LLM reasoning length.

Seen in: UniScale: Adaptive Unified Inference Scaling via Online Joint Optimization of Model Routing and Test-Time Scaling; Test-Time Scaling of Diffusion Models via Noise Trajectory Search.

### difficulty-based routing between reasoning modes

Deciding per-query whether a model should think (spend extra reasoning tokens) or answer directly, based on estimated problem difficulty, instead of a single fixed mode. OptimalThinkingBench tests this as one of its five overthinking/underthinking mitigation strategies: a trained difficulty-based router improves its combined F1^otb metric by 20.4% on average over the best single mode, but still trails an oracle router by roughly 15 points.

Seen in: OptimalThinkingBench: Evaluating Over and Underthinking in LLMs; OptimalThinkingBench: Evaluating Over and Underthinking in LLMs.

### F1^otb combined metric

OptimalThinkingBench's headline metric: the harmonic mean of AUC_OAA (the overthinking-penalized accuracy score) and UnderthinkingBench accuracy, so a model must score well on both sub-benchmarks to score high overall. No evaluated model optimally balances both: o3 scores best overall (71.1%), GPT-OSS-120B best among open-weight models (68.3%).

Seen in: OptimalThinkingBench: Evaluating Over and Underthinking in LLMs; OptimalThinkingBench: Evaluating Over and Underthinking in LLMs.

## Methods

| Method | Sources | Summary |
| --- | ---: | --- |
| best-of-N sampling | 7 | A test-time-compute strategy that samples N candidate solutions independently and selects one (by a verifier, reward model, or majority vote), trading inference compute for accu... |
| AdaptThink | 3 | A length-based reward-shaping reinforcement-learning method for controlling reasoning length. OptimalThinkingBench tests it as one of five overthinking mitigations, where it cut... |
| Best-of-N | 3 | A test-time-compute strategy that samples N candidate solutions independently and selects one, trading inference compute for accuracy. In the sources tagged separately under thi... |
| budget forcing | 3 | Controlling a reasoning model's chain-of-thought length by inserting a keyword at inference time -- most commonly 'Wait' to force it to keep thinking past what it would have gen... |
| counterfactual intervention | 3 | A causal-analysis technique that alters part of a reasoning trace (e.g. an intermediate thinking-draft step, or a model's implicit first guess) and observes whether the final an... |
| Model Merging | 3 | Combining the parameters of two or more trained models into one, without further gradient-based training, to transfer a capability from one into the other. OptimalThinkingBench... |
| Monte Carlo Tree Search | 3 | A search algorithm that builds a tree of candidate reasoning/solution steps, using simulated rollouts to decide which branches to explore further, applied at inference time to s... |
| preference optimization | 3 | Training a model on pairs of preferred-vs-dispreferred outputs to shift its behavior, without a separate reward model. In the archive it is repeatedly used to shorten reasoning:... |
| self-consistency | 3 | Sampling multiple reasoning traces and taking the most common final answer, the simplest form of parallel test-time compute. A theoretical paper derives that its sample complexi... |
| speculative decoding | 3 | An inference-acceleration technique where a small draft model proposes tokens that a larger target model verifies in parallel, cutting wall-clock generation time without changin... |
| VeriThinker | 3 | An auxiliary-verification-training method for reducing overthinking, listed in the 'Don't Overthink It' survey's taxonomy and tested as one of five mitigation strategies in Opti... |
| activation steering | 2 | Controlling how long or how a reasoning model thinks by directly modifying its internal activations at inference time, rather than by prompting or retraining it. The archived so... |
| Best-of-N (BoN) sampling | 2 | A test-time-compute strategy that samples N candidate solutions independently and selects one by a verifier or reward model, trading inference compute for accuracy. Under this s... |
| confidence-based early stopping | 2 | Stopping a model's sampling or reasoning process once its own confidence signal (e.g. self-distilled calibration, or cross-agent consensus) indicates further compute is unlikely... |
| early exit | 2 | Stopping a reasoning model's generation before it reaches a natural end, once an internal or external signal indicates the answer is already settled, to avoid spending tokens on... |
| L1 length-controlled reinforcement learning | 2 | A reinforcement-learning method that adds a length-based reward term to directly control how many tokens a reasoning model generates. OptimalThinkingBench tests it as one of fiv... |
| LC-R1 | 2 | A chain-level chain-of-thought compression method, categorized under 'CoT Compression' in the 'Don't Overthink It' survey's taxonomy, that trains a reasoning model to produce sh... |
| linear probing | 2 | Training a simple linear classifier or regressor on a model's internal activations to test what information they encode, without modifying the model itself. Used in the archive... |
| majority voting | 2 | Sampling multiple independent answers and taking the most common one, a simple parallel test-time-compute strategy that needs no verifier or reward model. 'Diversity Matters' fi... |
| Manifold Steering | 2 | An overthinking-mitigation technique that identifies overthinking as movement along a low-dimensional manifold in a reasoning model's activation space, then steers activations a... |

## Benchmarks and datasets

| Dataset / benchmark | Sources | Summary |
| --- | ---: | --- |
| AIME 2025 | 17 | The 2025 sitting of the American Invitational Mathematics Examination, the archive's single most-used hard-math benchmark (17 sources): compute-balanced routing (CoBa), beam sea... |
| MATH-500 | 16 | A 500-problem curated subset of the MATH benchmark, one of the archive's most-used evaluation sets (16 sources) for reasoning-length and test-time-compute methods -- compute-bal... |
| AIME 2024 | 15 | The 2024 sitting of the American Invitational Mathematics Examination, the single most-used hard-math benchmark across the archive's 15 sources for evaluating test-time-compute... |
| GPQA-Diamond | 9 | A hard multiple-choice science-question benchmark used across the archive's 9 sources as a standard hard-reasoning evaluation set for test-time-compute and overthinking-mitigati... |
| GSM8K | 9 | A grade-school math word-problem benchmark used in the archive's 9 sources as an 'easier' reasoning testbed, in contrast to harder benchmarks like AIME or GPQA Diamond. It shows... |
| AIME | 5 | The American Invitational Mathematics Examination, used throughout the archive's sources (unspecified year in this entry) as a standard hard competition-math benchmark. Under th... |
| HMMT 2025 | 5 | The 2025 Harvard-MIT Mathematics Tournament, used as a hard competition-math benchmark alongside AIME. In the archive's 5 sources it appears in Gambit's thought-level beam searc... |
| MATH | 5 | The MATH competition-mathematics dataset, used in the archive both directly (e.g. 'Between Underthinking and Overthinking' evaluates on MATH and GSM8K to show reasoning models o... |
| AMC23 | 4 | The 2023 sitting of the American Mathematics Competitions, used as a hard competition-math evaluation benchmark alongside AIME in CoBa's compute-balanced routing, the on-policy-... |
| AMC | 3 | A competition-math benchmark used alongside AIME and MATH-500 in the archive's 3 sources as a standard hard-reasoning evaluation set: verifier-free self-correction (Refining Ove... |
| GPQA | 3 | A graduate-level multiple-choice science-question benchmark used across the archive as a hard-reasoning evaluation set, referenced by the foundational overthinking paper ('Do NO... |
| AIME 2026 | 2 | Referenced in the archive's sources as a sitting of the American Invitational Mathematics Examination named alongside AIME 2024/2025 evaluation results in Gambit's thought-level... |
| BBH (Big Bench Hard) | 2 | A benchmark of hard multi-step reasoning tasks used in the archive's sources as one of several standard evaluation sets for test-time-compute efficiency methods, alongside AIME/... |
| GAIA | 2 | A benchmark of multi-step, tool-using agent tasks used in the archive to evaluate deep-search / web-research LLM agents: the asymmetric-verification deep-search paper and WebThi... |
| LiveCodeBench | 2 | A code-generation benchmark used in the archive alongside math benchmarks to evaluate test-time-compute methods across domains: the bandit-learning compute-allocation paper and... |
| OverthinkingBench | 2 | The overthinking half of OptimalThinkingBench: 1327 general-domain plus 133 math questions, built via constrained synthetic generation and filtered by requiring 8/8 agreement ac... |
| SuperGPQA | 2 | A large, broad-domain multiple-choice science-question dataset used as a source pool in the archive: TRAAC references it as part of its evaluation suite, and OptimalThinkingBenc... |
| SWE-bench Verified | 2 | A curated, human-verified subset of SWE-bench (real GitHub issue-resolution tasks) used to evaluate agentic coding performance under a fixed compute/cost budget. 'The Danger of... |
| UnderthinkingBench | 2 | The underthinking half of OptimalThinkingBench: 11 Reasoning Gym task types plus AIME'25/HMMT'25 math, keeping only tasks where a small thinking model (Qwen3-1.7B) outperforms a... |
| 12 unnamed datasets (count stated, individual names not given in material reviewed) | 1 | _pending_ |

## Reading path

**Then, in order of relevance:**

1. **Between Underthinking and Overthinking: An Empirical Study of Reasoning Length and correctness in LLMs** (2025)
   - An empirical study showing reasoning LLMs overthink easy questions and underthink hard ones, and that preferring shorter outputs via SimPO can cut generation length 30-60% with little accuracy loss.
2. **When More Thinking Hurts: Overthinking in LLM Test-Time Compute Scaling** (2026)
   - The paper shows that extended chain-of-thought reasoning in LLMs has diminishing and eventually negative marginal utility, quantifies this 'overthinking' via answer-flip tracking, and proposes cost-aware, indicator-based early-stopping strategies that cut compute substantially with little accuracy loss.
3. **Your Models Have Thought Enough: Training Large Reasoning Models to Stop Overthinking** (2026)
   - Trains large reasoning models via RL to proactively stop reasoning once they have accumulated enough evidence, cutting output length by 46.3% while improving accuracy by 4.6% on the Olympiad benchmark.
   - <https://iclr.cc/virtual/2026/poster/10011695>
4. **TrimR: Verifier-based Training-Free Thinking Trimming for Efficient Test-Time Scaling** (2026)
   - TrimR is a training-free, verifier-based system that trims redundant chain-of-thought reasoning in deployed large reasoning models to speed up test-time scaling with little accuracy loss.
   - <https://iclr.cc/virtual/2026/poster/10007390>
5. **Inverse Scaling in Test-Time Compute** (2025)
   - Constructs evaluation tasks across four categories (distractor counting, spurious-feature regression, constraint-tracking deduction, and AI-risk model-written evaluations) where letting large reasoning models reason longer at test time makes their accuracy or alignment worse, not better.
   - <https://iclr.cc/virtual/2026/poster/10014059>
6. **The Danger of Overthinking: Examining the Reasoning-Action Dilemma in Agentic Tasks** (2025)
   - Defines and measures 'overthinking' in Large Reasoning Models on real software-engineering agent tasks, showing that favoring internal reasoning over environment interaction correlates with lower SWE-bench issue-resolution rates and can be mitigated at lower cost.
7. **Mitigating Overthinking in Large Reasoning Models via Manifold Steering** (2025)
   - Identifies that overthinking in large reasoning models corresponds to a low-dimensional manifold in activation space and proposes projecting steering interventions onto that manifold to cut output tokens by up to 71% without hurting accuracy.
   - <https://neurips.cc/virtual/2025/poster/119969>
8. **Plan and Budget: Effective and Efficient Test-Time Scaling on Reasoning Large Language Models** (2026)
   - Plan-and-Budget decomposes queries into sub-questions and allocates test-time token budgets by estimated complexity, using a theoretical model of reasoning as sequential sub-questions to reduce both overthinking and underthinking.
   - <https://iclr.cc/virtual/2026/poster/10008460>
9. **On Reasoning Strength Planning in Large Reasoning Models** (2025)
   - Finds that large reasoning models pre-plan how much to reason via a directional vector in their activations, whose magnitude causally sets reasoning length.
   - <https://neurips.cc/virtual/2025/poster/118916>
10. **Let LRMs Break Free from Overthinking via Self-Braking Tuning** (2025)
   - Introduces Self-Braking Tuning, which trains a large reasoning model to detect and stop its own redundant reasoning steps, cutting token usage by up to 60% with comparable accuracy on math benchmarks.
   - <https://neurips.cc/virtual/2025/poster/115532>

## Open problems

Drawn from the limitations each paper states about itself, so this is what the field admits it cannot do yet.

- **SMTrap: Cost-Effective DoS Attacks Against Large Reasoning Models via SMT Conflict Guidance** — The paper's own scope statement: the mitigation targets only the failure mode of unrestricted natural-language search on structured CSP-style tasks, not all possible LRM-DoS attacks. Main experiments are limited to Sudoku and Zebra-Game as CSP testbeds; generalisation to graph coloring is reported only as a preliminary, single-family test (low-conflict 20,127 vs high-conflict 35,712 output tokens on GPT-5.5). Stealthiness evaluation used a single external classifier (GPT-4o via OpenRouter) and found 10 of 30 Zebra queries still flagged as malicious. Kimi-K2.6 was excluded from the reasoning-time average because its batch API does not report per-case reasoning time.
- **Test-Time Scaling in the Wild: Why Exploitation, Not Exploration, Is the Bottleneck** — Conclusions rest on two generator model families (Qwen3.5 and OLMo3) and a single unified LLM judge (Qwen3.5-397B-A17B), not the benchmarks' native judges, though judge agreement was validated against native judges on 5-15% stratified samples (e.g. HealthBench Macro F1 0.679, PRBench criterion-level kappa 0.679, WildBench QWK 0.564, WritingBench per-pair agreement 0.408). The oracle estimator assumes i.i.d. candidates, which is exact for BoN but only approximate for Refinement, Fusion, and Particle Filtering; the authors expect it to slightly underestimate the true oracle for the first two and slightly overestimate it for Particle Filtering. Sequential Refinement's apparent gain on WritingBench is confounded by the benchmark's judge having a stronger length-score correlation (rho=+0.33 for SR vs +0.20 for BoN) than other benchmarks, i.e. a verbosity bias in that specific benchmark's evaluation design. Results do not cover all open-ended use cases and the authors note deploying TTS in high-stakes domains without human oversight remains inadvisable.
- **Funnel of Thoughts: Efficient Test-Time Scaling via Early Voting and Rollout Pruning** — Stated in Section 6: evaluation is centered on tasks with extractable final answers (boxed numbers, multiple-choice, or executable code); open-ended generation, multi-turn interaction, and tasks where correctness cannot be reduced to answer extraction are outside the study's scope. The calibration pool is unbalanced (MATH500 supplies 3,000 of 3,600 model-problem pairs), so pooled statistics are weighted toward easy problems where pruning has little to remove or risk; the paper reports the hard split separately for this reason. Early voting relies on a commitment detector (the \boxed{} convention in math), and the vote bank's reliability is bounded by that detector's accuracy in other domains. The method uses a fixed checkpoint schedule and an English hesitation-marker kernel; models reasoning in other languages or with substantially different deliberation styles may need a revalidated marker set. FLOP accounting assumes standard full attention; under efficient-attention mechanisms the saving shrinks toward a token-reduction floor (48.7% down to 23.0% in the linear limit, per Appendix D.2). Pool-size sweeps show pruning is mildly harmful when the sampling pool k is small (k=8), becomes neutral around k=16, and only turns clearly positive beyond that -- so FoT is intended as a large-pool replacement for self-consistency, not a general small-k method. Slim-SC (a competing baseline) over-prunes on hard samples (drops AIME25 accuracy from 69.4 to 61.7 while saving 67.1% FLOPs), illustrating that similarity-based pruning approaches can discard useful diversity, a failure mode FoT is designed to avoid via a different (hesitation-density, within-pool relative) signal.
- **Divergent-Convergent Reasoning: Scaling Test-Time Compute through Structured Solution Synthesis** — Discussion section (6) and Future Work (7) state several limits: (1) Upfront cost of estimation -- computing dispersion as a gating signal requires generating N proposals (N=25 in experiments) before assessing difficulty, which may be prohibitive in latency-sensitive production settings; adaptive probing or hybrid human-triage strategies are left to future work. (2) Bias in low-dispersion regimes -- low dispersion signals high model confidence but not correctness; a model can be consistently and confidently wrong ('confident hallucination'), and DCR is less effective there; addressing this would need heterogeneous ensembles rather than single-model resampling. (3) The recursive system's unanimous-consent stopping rule is strict and may be overly conservative; the paper suggests future work on 'soft consensus' or probabilistic stopping rules. (4) The dispersion metric currently uses only final-answer embeddings; the authors note additional signals (reasoning-path dispersion, confidence dispersion, token-level entropy) are not yet incorporated. (5) A distinct failure mode is observed in mixed-proposal (DCR-Mix) settings: weaker models' incorrect proposals can 'pollute' a stronger reviewer's judgment, causing it to hallucinate or drift from a correct path, so mixing is only reliably helpful when it lifts weaker models toward a strong consensus rather than diluting strong experts with weak noise.
- **Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling** — The paper does not state an explicit limitations section in the pages read; the framing itself notes open questions it leaves unresolved: it studies three specific student-teacher OPD settings (Qwen3, Skywork, JustRL) and a handful of OPD variants (EOPD, ExOPD, Direct-OPD, forward-KL) rather than an exhaustive survey of distillation methods, and the perplexity/case-study analyses are conducted on a small sample (16 problems x 32 trajectories per source model in Appendix D).
- **Claim-Level Reliability Assessment for Efficient Test-Time Reasoning** — The paper notes the falsification asymmetry (refuting is easier than constructing a correct solution) is treated as an inductive bias, not a guaranteed property -- 'we treat this asymmetry as an inductive bias rather than a guarantee that falsification is uniformly easier than generation.' The nonlinear reliability score (trace score = mean claim survival raised to the Mth power) is described as 'a heuristic, not a joint correctness probability' and does not assume claim independence. Results are model- and regime-dependent: on Gemma-4-12B-it, CLR improves accuracy by 7.12-12.08 points but costs 22.2-47.8% more tokens; on the already near-saturated Qwen3.5-27B (Cons@64 already >90% on three benchmarks), CLR's gains are small (up to +2.60pp) and its largest token reduction is 14.5%; the accuracy-token curves versus self-consistency can cross at intermediate budgets, so CLR is 'not uniformly dominant at every operating point.' It is published as a COLM 2026 workshop paper.
- **ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling** — Stated in Section 7: (1) retrieval quality depends on corpus coverage - for problems distributionally distant from the corpus, retrieved exemplars can be irrelevant or actively misleading and degrade performance below the no-retrieval baseline; a structurally analogous but load-bearing-different exemplar can anchor the model on a confident wrong answer because of the method's low-entropy property. (2) QA-QA contamination filtering (cosine similarity <=0.90) cannot exhaustively rule out latent structural similarities where two problems share an identical solution procedure despite different surface forms. (3) Additional per-step latency from retrieval calls and expanding context; wall-clock inference time is higher than sequential TTS even though token-budget-matched comparisons hold (Table 5, Appendix B). (4) The SciQ train/test splits (as released by the dataset authors) contain substantial paraphrase-level overlap that was not filtered in this work. (5) Every benchmark is paired with a domain-matched corpus (NuminaMath for math, SciQ's own training split for SciQ); whether the method remains beneficial where building a high-coverage exemplar corpus is harder (e.g. code generation, open-ended logical reasoning) is left to future work.
- **Test-Time Scaling for CAD Generation via Verifier-Free Consensus Selection** — Consensus selection cannot help when all sampled candidates are identical, and it fails when the same error appears in most candidates, since that shared error becomes part of the consensus. It favors candidates near the center of the pool and may miss a high-quality outlier, which the authors identify as the main source of the remaining gap to an oracle upper bound (which keeps improving with more samples while consensus and random selection saturate by about N=9). Geometric consensus normalizes and ICP-aligns models before comparison, so it cannot detect absolute-dimension mismatches even when dimensions are specified in the prompt, and a global (whole-model) distance may fail to distinguish small local features. No statistically significant difference was found between topological consensus and the verifier baseline on topology correctness. Whether consensus generalizes to sequential refinements of a single program (rather than parallel independent candidates) is left open.
- **Consilience for Verifier-Free Test-Time Scaling** — The suggested frozen hyperparameters (alpha=3, window k=20%) capture only 72-78% of the per-dataset grid-search optimum under 5-fold cross-validation, so some gain is left on the table without per-task tuning; performance degrades if the penalty multiplier alpha is set too large, over-penalizing early exploration. Applying consilience with n=32 samples at every step of an agentic workflow incurs roughly 32x the compute of a single rollout; in the authors' implementation this took about 18 hours versus 8 hours for the plain agent on their hardware, though only a subset of high-value steps were targeted. The method requires access to top-K token log-probabilities (K=5 used), so it needs at least partial logit access and is not purely black-box. On easy problems (near-ceiling Pass@1), consilience is neutral since all candidates already show similarly high initial confidence, leaving no discriminative signal to exploit.
- **Efficient Test-Time Scaling for LLM-based Time Series Forecasting** — Ablations show that using the lightweight global forecaster to predict full-resolution future tokens (instead of only a downscaled coarse shape) is more expensive and does not improve accuracy, attributed to the forecaster's fine-grained predictions being unreliable and potentially misleading the LLM during refinement. Varying the global forecaster's depth from 1 to 4 layers gives only marginal, inconsistent gains beyond the default depth of 1, suggesting limited headroom from that component. No dedicated 'Limitations' section was found in the read portion of the paper; scope is restricted to LLM-based multivariate time series forecasting.
- **Thinking Hard, Not Smart: Reasoning Models Fail to Ration Test-Time Compute Across Questions** — The full factorial design (varying length, order, and point values) is run only on Omni-MATH; CRUXEval-O experiments cover just two exam lengths, four models and two scoring schemes, with no native difficulty axis and no ordering/repricing manipulations, so absolute score rates and effect magnitudes should not be compared across the two domains. Per-question token attribution is recovered from Q1/Q2 marker segmentation, which the authors call reliable for the large majority of traces but only an approximation; a fully rigorous notion of effort (detecting where a question is actually being solved, not merely referenced) remains open.
- **Thought-Level Beam Search for Reasoning** — No dedicated limitations section is stated; the empirical evaluation is confined to a single hardware setup (one 275GB NVIDIA B300 GPU) via vLLM and three open-weight architectures (Qwen3-4B-Thinking, DeepSeek-R1-8B, Phi-4-reasoning-plus-14B). The main comparison isolates the search-topology contribution by reusing the identical off-the-shelf 2-layer MLP scorer from prior work (STEP), so results depend on that scorer's reliability. The paper notes that its large total-token savings do not translate proportionally into latency reductions, because branching increases the frequency of long-running traces (a rightward shift in the total sequence-length distribution) rather than shortening individual traces.

## References

1. *AgentTTS: Large Language Model Agent for Test-time Compute-optimal Scaling Strategy in Complex Tasks*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/119334>
2. *Are Large Reasoning Models Good Translation Evaluators? Analysis and Performance Boost*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/117120>
3. *Atom of Thoughts for Markov LLM Test-Time Scaling*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/115860>
4. Jinyan Su, Jennifer Healey, Preslav Nakov et al.. *Between Underthinking and Overthinking: An Empirical Study of Reasoning Length and correctness in LLMs*. preprint. 2025
5. *DisCO: Reinforcing Large Reasoning Models with Discriminative Constrained Optimization*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/114995>
6. Gaurav Srivastava, Aafiya Hussain, Sriram Srinivasan et al.. *Do LLMs Overthink Basic Math Reasoning? Benchmarking the Accuracy-Efficiency Tradeoff in Language Models*. preprint. 2025
7. *Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models*. ICML 2025. 2025 <https://icml.cc/virtual/2025/poster/45540>
8. *Does Thinking More Always Help? Mirage of Test-Time Scaling in Reasoning Models*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/115605>
9. Linan Yue, Yichao Du, Yizhi Wang et al.. *Don't Overthink It: A Survey of Efficient R1-style Large Reasoning Models*. preprint. 2025
10. *Don’t Think Longer, Think Wisely: Optimizing Thinking Dynamics for Large Reasoning Models*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/116095>
11. *Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/116060>
12. *Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Time Scaling Evaluators*. ICML 2025. 2025 <https://icml.cc/virtual/2025/poster/46046>
13. *Every Rollout Counts: Optimal Resource Allocation for Efficient Test-Time Scaling*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/115239>
14. *Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning*. ICML 2025. 2025 <https://icml.cc/virtual/2025/poster/46117>
15. *Generation as Search Operator for Test-Time Scaling of Diffusion-based Combinatorial Optimization*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/119551>
16. Aryo Pradipta Gema, Alexander Hägele, Runjin Chen et al.. *Inverse Scaling in Test-Time Compute*. Transactions on Machine Learning Research (TMLR). 2025 <https://iclr.cc/virtual/2026/poster/10014059>
17. *Inverse Scaling: When Bigger Isn't Better*. ICLR 2025. 2025 <https://iclr.cc/virtual/2025/poster/31511>
18. *Kinetics: Rethinking Test-Time Scaling Law*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/115931>
19. *LIMOPro: Reasoning Refinement for Efficient and Effective Test-time Scaling*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/117621>
20. *Let LRMs Break Free from Overthinking via Self-Braking Tuning*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/115532>
21. *LongVU: Spatiotemporal Adaptive Compression for Long Video-Language Understanding*. ICML 2025. 2025 <https://icml.cc/virtual/2025/poster/44939>
22. *Measuring the Faithfulness of Thinking Drafts in Large Reasoning Models*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/120231>
23. *MindJourney: Test-Time Scaling with World Models for Spatial Reasoning*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/118581>
24. *Mitigating Overthinking in Large Reasoning Models via Manifold Steering*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/119969>
25. *No Loss, No Gain: Gated Refinement and Adaptive Compression for Prompt Optimization*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/118743>
26. *Noise Hypernetworks: Amortizing Test-Time Compute in Diffusion Models*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/119207>
27. *On Reasoning Strength Planning in Large Reasoning Models*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/118916>
28. *One Token Embedding Is Enough to Deadlock Your Large Reasoning Model*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/116766>
29. Pranjal Aggarwal, Seungone Kim, Jack Lanchantin et al.. *OptimalThinkingBench: Evaluating Over and Underthinking in LLMs*. preprint. 2025
30. *Optimizing Test-Time Compute via Meta Reinforcement Finetuning*. ICML 2025. 2025 <https://icml.cc/virtual/2025/poster/45154>
31. *Provable Scaling Laws for the Test-Time Compute of Large Language Models*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/118984>
32. *Reasoning Models Hallucinate More: Factuality-Aware Reinforcement Learning for Large Reasoning Models*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/118780>
33. *Reinforcement Learning Teachers of Test Time Scaling*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/115573>
34. *Rethinking Fine-Tuning when Scaling Test-Time Compute: Limiting Confidence Improves Mathematical Reasoning*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/116423>
35. *Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/117041>
36. *Sampling-Efficient Test-Time Scaling: Self-Estimating the Best-of-N Sampling in Early Decoding*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/119365>
37. *Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning*. ICLR 2025. 2025 <https://iclr.cc/virtual/2025/poster/31024>
38. *Scaling Test-Time Compute Without Verification or RL is Suboptimal*. ICML 2025. 2025 <https://icml.cc/virtual/2025/poster/44733>
39. *Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/117966>
40. *SolverLLM: Leveraging Test-Time Scaling for Optimization Problem via LLM-Guided Search*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/116215>
41. *TTS-VAR: A Test-Time Scaling Framework for Visual Auto-Regressive Generation*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/115886>
42. *Test Time Scaling for Neural Processes*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/119684>
43. *Test-Time Scaling of Diffusion Models via Noise Trajectory Search*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/116804>
44. Alejandro Cuadron, Dacheng Li, Wenjie Ma et al.. *The Danger of Overthinking: Examining the Reasoning-Action Dilemma in Agentic Tasks*. International Conference on Machine Learning (ICML) 2025. 2025
45. Joykirat Singh, Justin Chih-Yao Chen, Archiki Prasad et al.. *Think Right: Learning to Mitigate Under-Over Thinking via Adaptive, Attentive Compression*. preprint. 2025
46. *Think or Not? Exploring Thinking Efficiency in Large Reasoning Models via an Information-Theoretic Lens*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/119190>
47. *Thoughts Are All Over the Place: On the Underthinking of Long Reasoning Models*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/117581>
48. *Topology of Reasoning: Understanding Large Reasoning Models through Reasoning Graph Properties*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/116088>
49. *Towards Thinking-Optimal Scaling of Test-Time Compute for LLM Reasoning*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/119802>
50. *VideoChat-R1.5: Visual Test-Time Scaling to Reinforce Multimodal Reasoning by Iterative Perception*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/116032>
51. *WebThinker: Empowering Large Reasoning Models with Deep Research Capability*. NeurIPS 2025. 2025 <https://neurips.cc/virtual/2025/poster/119715>
52. *A Simple "Motivation" Can Enhance Reinforcement Finetuning of Large Reasoning Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011610>
53. *ATTS: Asynchronous Test-Time Scaling via Conformal Prediction*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10008898>
54. *AdvChain: Adversarial Chain-of-Thought Tuning for Robust Safety Alignment of Large Reasoning Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10007590>
55. *Aligning Tree-Search Policies with Fixed Token Budgets in Test-Time Scaling of LLMs*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/63795>
56. *Are Large Reasoning Models Interruptible?*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/61807>
57. *Asymptotic Universal Alignment: A New Alignment Framework via Test-Time Scaling*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/66584>
58. *AsyncSpade: Efficient Test-Time Scaling with Asynchronous Sparse Decoding*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/63012>
59. *BeaconKV: Key-Value Cache Compression Guided by Beacon Queries for Efficient Large Reasoning Model Inference*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/62942>
60. *Better, Faster: Harnessing Self-Improvement in Large Reasoning Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/64514>
61. *CaTS: Calibrated Test-Time Scaling for Efficient LLM Reasoning*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10007848>
62. *Cache Coherent Resampling for Efficient Test Time Scaling in LLM Reasoning via Adaptive Sequential Monte Carlo*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/64829>
63. *Causal Dependency-Aware Unsupervised Routing for Large Reasoning Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/64247>
64. *Certain Head, Uncertain Tail: Expert-Sample for Test-Time Scaling in Fine-Grained MoE*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/62643>
65. *CodeChemist: Test-Time Scaling for Low-Resource Code Generation via Functional Knowledge Transfer*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/63512>
66. *Conditional Advantage Estimation for Reinforcement Learning in Large Reasoning Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10010855>
67. *ContextPRM: Leveraging Contextual Coherence for multi-domain Test-Time Scaling*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011128>
68. *D-CORE: Incentivizing Task Decomposition in Large Reasoning Models for Complex Tool Use*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/61056>
69. *DTS: Enhancing Large Reasoning Models via Decoding Tree Sketching*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/61328>
70. *Distilled Pretraining: A modern lens of Data, In-Context Learning and Test-Time Scaling*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10009683>
71. *Diversity Matters: Revisiting Test-Time Compute in Vision-Language Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/63569>
72. *Doxing via the Lens: Revealing Location-related Privacy Leakage on Multi-modal Large Reasoning Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10006914>
73. *Dynamic Thinking-Token Selection for Efficient Reasoning in Large Reasoning Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/61200>
74. *Dynamics-Predictive Sampling for Active RL Finetuning of Large Reasoning Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10006780>
75. *ETS: Energy-Guided Test-Time Scaling for Training-Free RL Alignment*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/61604>
76. *Efficient Test-Time Scaling for Small Vision-Language Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10007164>
77. *Efficient Test-Time Scaling via Hierarchical Search and Self-Verification for Discrete Diffusion Language Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/64102>
78. *Exposing Weaknesses of Large Reasoning Models through Graph Algorithm Problems*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10010419>
79. *Expressive Power of Implicit Models: Rich Equilibria and Test-Time Scaling*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10009635>
80. *GTA1: GUI Test-time Scaling Agent*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011639>
81. *HardcoreLogic: Challenging Large Reasoning Models with Long-tail Logic Puzzle Games*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011195>
82. *Internalizing Safety Understanding in Large Reasoning Models via Verification*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/63605>
83. *KLAS: Using Similarity to Stitch Neural Networks for Improved Accuracy-Efficiency Tradeoffs*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10007961>
84. *Less Diverse, Less Safe: The Indirect But Pervasive Risk of Test-Time Scaling in Large Language Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/64671>
85. *Lookahead Sample Reward Guidance for Test-Time Scaling of Diffusion Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/64926>
86. *Mechanistic Detection and Mitigation of Hallucination in Large Reasoning Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10008968>
87. *Mode-conditioning unlocks superior test-time compute scaling*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10010159>
88. *Modeling Hierarchical Thinking in Large Reasoning Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/64487>
89. *Multi-Objective Protein Design via Memory-Aware Test-Time Scaling in Diffusion Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/65578>
90. *On the Limits of Test-Time Compute: Sequential Reward Filtering for Better Inference*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/64598>
91. *Optimal Aggregation of LLM and PRM Signals for Efficient Test-Time Scaling*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10006667>
92. *OptimalThinkingBench: Evaluating Over and Underthinking in LLMs*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10009890>
93. *Overthinking Reduction with Decoupled Rewards and Curriculum Data Scheduling*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10007765>
94. *Overthinking: Amplifying Reasoning Weights to Extract Learned Secrets*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/63085>
95. *Plan and Budget: Effective and Efficient Test-Time Scaling on Reasoning Large Language Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10008460>
96. *Pruning Long Chain-of-Thought of Large Reasoning Models via Small-Scale Preference Optimization*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011162>
97. *Pushing Test-Time Scaling Limits of Deep Search with Asymmetric Verification*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10008007>
98. *R-Horizon: How Far Can Your Large Reasoning Model Really Go in Breadth and Depth?*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10007149>
99. *RAIN-Merging: A Gradient-Free Method to Enhance Instruction Following in Large Reasoning Models with Preserved Thinking Format*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10009681>
100. *RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011763>
101. *ROC-n-reroll: How verifier imperfection affects test-time scaling*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011656>
102. *Real-Time Monitoring and Calibration of Chain-of-Thought Sycophancy in Large Reasoning Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/61298>
103. *Reasoning or Retrieval? A Study of Answer Attribution on Large Reasoning Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10010758>
104. *Restoring Exploration after Post-Training: Latent Exploration Decoding for Large Reasoning Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/66546>
105. *Robust Federated Learning Against Adaptive Compression*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/61991>
106. *SPARC: Separating Perception And Reasoning Circuits for Test-time Scaling of VLMs*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/62906>
107. *Sample Complexity and Representation Ability of Test-time Scaling Paradigms*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10009511>
108. *Scaling Atomistic Protein Binder Design with Generative Pretraining and Test-Time Compute*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10007211>
109. *Scaling Up, Speeding Up: A Benchmark of Speculative Decoding for Efficient LLM Test-Time Scaling*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10010752>
110. *Small Generalizable Prompt Predictive Models Can Steer Efficient RL Post-Training of Large Reasoning Models*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/60937>
111. *SmartThinker: Progressive Chain-of-Thought Length Calibration for Efficient Large Language Model Reasoning*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/64022>
112. *SpecExit: Accelerating Large Reasoning Model via Speculative Exit*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/66249>
113. *Strategic Scaling of Test-Time Compute: A Bandit Learning Approach*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011899>
114. *T1: Tool-integrated Verification for Test-time Compute Scaling in Small Language Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10007001>
115. *TEST-TIME SCALING IN DIFFUSION LLMS VIA HIDDEN SEMI-AUTOREGRESSIVE EXPERTS*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10010063>
116. *TUMIX: Multi-Agent Test-Time Scaling with Tool-Use Mixture*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10010417>
117. *TaTToo: Tool-Grounded Thinking PRM for Test-Time Scaling in Tabular Reasoning*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10006442>
118. *Test-Time Scaling with Reflective Generative Model*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10006997>
119. *The First Impression Problem: Internal Bias Triggers Overthinking in Reasoning Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011746>
120. *Towards Safe Reasoning in Large Reasoning Models via Corrective Intervention*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011693>
121. Yi Hu, Jiaqi Gu, Ruxin Wang et al.. *Towards a Mechanistic Understanding of Large Reasoning Models: A Survey of Training, Inference, and Failures*. preprint. 2026
122. *Training Large Reasoning Models Efficiently via Progressive Thought Encoding*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10007286>
123. *TrimR: Verifier-based Training-Free Thinking Trimming for Efficient Test-Time Scaling*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10007390>
124. *UnMaskFork: Test-Time Scaling for Masked Diffusion via Deterministic Action Branching*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/66823>
125. *Understanding the Role of Training Data in Test-Time Scaling*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10008915>
126. *UniScale: Adaptive Unified Inference Scaling via Online Joint Optimization of Model Routing and Test-Time Scaling*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/60578>
127. *VLA-ATTC: Adaptive Test-Time Compute for VLA Models with Relative Action Critic Model*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/61157>
128. *Wait, Do We Need to Wait? Revisiting Budget Forcing for Sequential Test-Time Scaling*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10012115>
129. *What If We Allocate Test-Time Compute Adaptively?*. ICML 2026. 2026 <https://icml.cc/virtual/2026/poster/60797>
130. Shu Zhou, Rui Ling, Junan Chen et al.. *When More Thinking Hurts: Overthinking in LLM Test-Time Compute Scaling*. preprint. 2026
131. *When More is Less: Understanding Chain-of-Thought Length in LLMs*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011380>
132. *When Reasoning Meets Compression: Understanding the Effects of LLMs Compression on Large Reasoning Models*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011689>
133. *Your Models Have Thought Enough: Training Large Reasoning Models to Stop Overthinking*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10011695>
134. *Zero-Overhead Introspection for Adaptive Test-Time Compute*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10010457>
135. *e3: Learning to Explore Enables Extrapolation of Test-Time Compute for LLMs*. ICLR 2026. 2026 <https://iclr.cc/virtual/2026/poster/10008718>
136. Shaokang Wang, Pei Fu, Ruoceng Zhang et al.. *GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models*. arXiv.org. 2026 <https://www.semanticscholar.org/paper/024b8e6fbfc20171bb77a15a3c2116a29f69f4f6>
137. Peijie Liu, Fengli Xu, Yong Li. *TravelReasoner: Leveraging Large Reasoning Models to Address Mobility Data Gap*. The Web Conference. 2026 <https://www.semanticscholar.org/paper/01c84bcd6e681633bf47bc34a73afb7423695452>
138. Juhász Levente Zsolt. *Reasoning models, test-time compute, self refinement*. 2026 IEEE 8th International Conference and Workshop Óbuda on Electrical and Power Engineering (CANDO-EPE). 2026 <https://www.semanticscholar.org/paper/0249f6192c6a7cb170fd1b45c5d3e5607f5b9f92>
139. Kaishen Wang, Tong Zheng, Xuehao Cui et al.. *Mitigating Factual Hallucination in Large Reasoning Models via Mixed-Mode Advantage Regularization*. arXiv. 2026 <https://www.semanticscholar.org/paper/0294e3ee8794087f78b1cd58a21c3b4ab12f7f56>
140. Ahsan Bilal, Muhammad Ahmed Mohsin, Muhammad Umer et al.. *Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning*. cs.AI. 2026 <https://arxiv.org/abs/2608.05643>
141. Yan Zhou, Yue Ouyang, Kaiyang Zheng et al.. *CoBa: Cost-Effective Test-Time Scaling via Compute-Balanced Routing*. cs.AI. 2026 <https://arxiv.org/abs/2608.07424>
142. Jiaqian Wang, Yutao Qi, Wenjin Hou et al.. *From Test-Time Scaling to Reusable Memory: Measuring Crystallization in Text-to-SQL*. cs.CL. 2026 <https://arxiv.org/abs/2608.07213>
143. Chenrui Fan, Yize Cheng, Ming Li et al.. *Thinking Hard, Not Smart: Reasoning Models Fail to Ration Test-Time Compute Across Questions*. cs.CL. 2026 <https://arxiv.org/abs/2608.07968>
144. Lijie Yang, Hongyin Luo, Jiawei Zhao et al.. *Thought-Level Beam Search for Reasoning*. cs.AI. 2026 <https://arxiv.org/abs/2608.08020>
145. Xuan-May Le, Minh-Tuan Tran, Ling Luo et al.. *Efficient Test-Time Scaling for LLM-based Time Series Forecasting*. cs.LG. 2026 <https://arxiv.org/abs/2608.08675>
146. Lecheng Kong, Like Hui, Haitao Mao et al.. *Consilience for Verifier-Free Test-Time Scaling*. cs.CL. 2026 <https://arxiv.org/abs/2608.09898>
147. Aaron Haag, Altay Kacan, Bertram Fuchs et al.. *Test-Time Scaling for CAD Generation via Verifier-Free Consensus Selection*. cs.CE. 2026 <https://arxiv.org/abs/2608.09706>
148. Vaibhav Singh, Soumya Suvra Ghosal, Sarvesh Gharat et al.. *ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling*. cs.AI. 2026 <https://arxiv.org/abs/2608.10928>
149. Sen Xu, Wei Wang, Shixi Liu et al.. *Claim-Level Reliability Assessment for Efficient Test-Time Reasoning*. cs.AI. 2026 <https://arxiv.org/abs/2608.11994>
150. Xinmu Ge, Zizhuo Zhang, Yu Huang et al.. *Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling*. cs.LG. 2026 <https://arxiv.org/abs/2608.11829>
151. Bo Wen, Yuhao Chen, Erhan Bilal et al.. *Divergent-Convergent Reasoning: Scaling Test-Time Compute through Structured Solution Synthesis*. cs.AI. 2026 <https://arxiv.org/abs/2608.15303>
152. Chanhee Park, Sungbin Han, Jeongho Yoon et al.. *Funnel of Thoughts: Efficient Test-Time Scaling via Early Voting and Rollout Pruning*. cs.AI. 2026 <https://arxiv.org/abs/2608.15065>
153. Jian Yang, Zhenqi Feng, Zhaoyang Yu et al.. *SMTrap: Cost-Effective DoS Attacks Against Large Reasoning Models via SMT Conflict Guidance*. cs.CL. 2026 <https://arxiv.org/abs/2608.18921>
154. Davide Romano, Kanak Raj, Jerrod Parker et al.. *Test-Time Scaling in the Wild: Why Exploitation, Not Exploration, Is the Bottleneck*. cs.CL. 2026 <https://arxiv.org/abs/2608.18931>
