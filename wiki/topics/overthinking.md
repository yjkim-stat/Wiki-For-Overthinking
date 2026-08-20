# Overthinking

<!-- auto:begin -->

When and why large reasoning models think more than a problem needs (or less than it needs) — the accuracy/efficiency tradeoff of reasoning length, test-time compute scaling, and methods to make a model stop, or keep going, at the right point.

- **Slug**: `overthinking`
- **Papers**: 154
- **Seminars**: 0
- **Tracked keywords**: `overthinking`, `underthinking`, `over-thinking`, `under-thinking`, `reasoning length`, `test-time compute`, `test time scaling`, `inverse scaling`, `chain-of-thought length`, `thinking budget`, `reasoning-action dilemma`, `large reasoning model`, `adaptive compression`, `accuracy-efficiency tradeoff`

## Most recent papers

- [SMTrap: Cost-Effective DoS Attacks Against Large Reasoning Models via SMT Conflict Guidance](../../archive/papers/2026/arxiv-2608-18921/summary.md) (2026-08-19)
  - SMTrap uses SMT solver conflict counts as a free, model-feedback-free proxy to synthesize Sudoku and zebra-puzzle queries that induce excessive backtracking-driven reasoning in large reasoning models, mounting a state-of-the-art denial-of-service attack that a bounded-solver defense can neutralize.
- [Test-Time Scaling in the Wild: Why Exploitation, Not Exploration, Is the Bottleneck](../../archive/papers/2026/arxiv-2608-18931/summary.md) (2026-08-19)
  - A compute-normalised, five-benchmark comparison of test-time scaling methods on open-ended generation finds that the candidate pool improves steadily with compute, but exploitation - selecting or synthesising the final answer from that pool - is the bottleneck, with reward-model-based selection near random (verifier correlation ~0.12) and even the best method (Fusion) recovering only ~40% of available quality.
- [Funnel of Thoughts: Efficient Test-Time Scaling via Early Voting and Rollout Pruning](../../archive/papers/2026/arxiv-2608-15065/summary.md) (2026-08-15)
  - Funnel of Thoughts detects and discards the subset of parallel reasoning rollouts that are spiraling into unproductive self-correction (flagged by a rising density of hesitation words like 'Wait' and 'perhaps'), matching self-consistency's accuracy while cutting attention FLOPs by up to 56% and wall time by 37.6%.
- [Divergent-Convergent Reasoning: Scaling Test-Time Compute through Structured Solution Synthesis](../../archive/papers/2026/arxiv-2608-15303/summary.md) (2026-08-15)
  - Divergent-Convergent Reasoning generates diverse candidate solutions and then uses reviewer-style reconciliation calls (optionally run recursively with a verifier-free unanimous-consent stopping rule) to recover correct answers even when they start out as a minority, reaching 93.3% on AIME 2024 and 92.0% on AIME 2025 while using about 27% less compute than a fixed single-round baseline.
- [Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling](../../archive/papers/2026/arxiv-2608-11829/summary.md) (2026-08-12)
  - Using pass@K/avg@K analysis, the paper shows on-policy distillation improves a student model's sampling efficiency at small K but does not expand its reasoning capability boundary at large K, and even causes it to forget some previously solvable problems.
- [Claim-Level Reliability Assessment for Efficient Test-Time Reasoning](../../archive/papers/2026/arxiv-2608-11994/summary.md) (2026-08-12)
  - CLR reallocates part of the test-time compute budget from generating more solution samples to falsifying a small set of decision-critical claims extracted from each trace, improving accuracy over self-consistency while using fewer tokens on some models.
- [ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling](../../archive/papers/2026/arxiv-2608-10928/summary.md) (2026-08-11)
  - ThinkRetrieve augments each step of a reasoning model's chain of thought with a dynamically retrieved, fully worked solved example (rather than just facts), consistently beating standard sequential test-time scaling on math and QA benchmarks.
- [Test-Time Scaling for CAD Generation via Verifier-Free Consensus Selection](../../archive/papers/2026/arxiv-2608-09706/summary.md) (2026-08-10)
  - Introduces verifier-free 'consensus selection' for text-to-CAD generation, picking among N compiled 3D CAD candidates the one that geometrically or topologically agrees most with the rest of the pool.
- [Consilience for Verifier-Free Test-Time Scaling](../../archive/papers/2026/arxiv-2608-09898/summary.md) (2026-08-10)
  - Introduces consilience, a verifier-free test-time-scaling selection metric that picks the sampled reasoning rollout whose confidence starts low (exploratory) and ends high (convergent), fixing a failure mode where naive confidence maximization favors confidently wrong answers on hard problems.
- [Efficient Test-Time Scaling for LLM-based Time Series Forecasting](../../archive/papers/2026/arxiv-2608-08675/summary.md) (2026-08-09)
  - Proposes SCALER, a coarse-to-fine LLM-based time-series forecaster that first predicts a lightweight global shape and then uses it to guide cheaper, fixed-step test-time refinement of the full-resolution forecast.
- [Thinking Hard, Not Smart: Reasoning Models Fail to Ration Test-Time Compute Across Questions](../../archive/papers/2026/arxiv-2608-07968/summary.md) (2026-08-08)
  - Introduces an exam-style evaluation where reasoning models must divide one shared token budget across multiple questions of different difficulty and value, and finds they allocate it by presentation order rather than by difficulty or value.
- [Thought-Level Beam Search for Reasoning](../../archive/papers/2026/arxiv-2608-08020/summary.md) (2026-08-08)
  - Introduces Gambit, an inference algorithm that formulates test-time reasoning as thought-level beam search, periodically pruning weak reasoning traces and branching new ones from high-quality prefixes to concentrate a fixed hardware budget on the most promising partial reasoning.
- [From Test-Time Scaling to Reusable Memory: Measuring Crystallization in Text-to-SQL](../../archive/papers/2026/arxiv-2608-07213/summary.md) (2026-08-07)
  - This paper measures how much of the value of test-time repair episodes in text-to-SQL survives when they are stored as a per-database memory bank and reused on new questions, isolating replay, cross-question retention, and held-out transfer, and finding that verified, database-specific memory captures 44.4% of the on-demand repair headroom on BIRD.
- [CoBa: Cost-Effective Test-Time Scaling via Compute-Balanced Routing](../../archive/papers/2026/arxiv-2608-07424/summary.md) (2026-08-07)
  - CoBa treats test-time scaling as a compute-allocation problem and routes cheap answer-agreement evidence versus a small number of strong-verifier calls, reaching majority-voting/self-evaluation-level accuracy on math and symbolic reasoning benchmarks while using roughly half the parameter-weighted tokens.
- [Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning](../../archive/papers/2026/arxiv-2608-05643/summary.md) (2026-08-06)
  - A training-free, verifier-free test-time scaling method that refines each of N sampled reasoning rollouts through D rounds of self-critique and self-correction before majority-voting the answers, instead of only sampling more candidates or relying on an external verifier.
- [Mitigating Factual Hallucination in Large Reasoning Models via Mixed-Mode Advantage Regularization](../../archive/papers/2026/arxiv-2607-05861/summary.md) (2026-07-07)
  - This paper shows that explicit reasoning traces can overturn otherwise-correct direct answers in factual QA (thinking-induced hallucination), and proposes an RL method (MARGO) that uses the model's own non-thinking answers as a reference to suppress harmful thinking while keeping useful thinking.
- [Reasoning models, test-time compute, self refinement](../../archive/papers/2026/doi-10-1109-cando-epe71091-2026-11569472/summary.md) (2026-05-26)
  - A short empirical study applying self-refinement test-time compute scaling to a small parameter-efficient reasoning model (Qwen 0.6B) to examine gains in mathematical-logical performance.
- [TravelReasoner: Leveraging Large Reasoning Models to Address Mobility Data Gap](../../archive/papers/2026/doi-10-1145-3774904-3793054/summary.md) (2026-04-13)
  - TravelReasoner post-trains large reasoning models on a reasoning-aligned Chain-of-Trips dataset derived from NHTS to synthesize interpretable, behaviorally consistent travel/mobility survey data, improving location consistency by 6.8% and time consistency by 4.1% over baselines.
- [GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models](../../archive/papers/2026/arxiv-2601-18197/summary.md) (2026-01-26)
  - GAIA trains an iteratively self-improving critic model that filters GUI agent actions by predicted success probability, used as a test-time scaling mechanism for GUI agents.
- [When More Thinking Hurts: Overthinking in LLM Test-Time Compute Scaling](../../archive/papers/2026/local-32a56cfa1105c39e/summary.md) (2026-01-01)
  - The paper shows that extended chain-of-thought reasoning in LLMs has diminishing and eventually negative marginal utility, quantifies this 'overthinking' via answer-flip tracking, and proposes cost-aware, indicator-based early-stopping strategies that cut compute substantially with little accuracy loss.
- [Your Models Have Thought Enough: Training Large Reasoning Models to Stop Overthinking](../../archive/papers/2026/title-92690cf46de29df1/summary.md) (2026-01-01)
  - Trains large reasoning models via RL to proactively stop reasoning once they have accumulated enough evidence, cutting output length by 46.3% while improving accuracy by 4.6% on the Olympiad benchmark.
- [TrimR: Verifier-based Training-Free Thinking Trimming for Efficient Test-Time Scaling](../../archive/papers/2026/title-b987d2649d32f1f3/summary.md) (2026-01-01)
  - TrimR is a training-free, verifier-based system that trims redundant chain-of-thought reasoning in deployed large reasoning models to speed up test-time scaling with little accuracy loss.
- [Plan and Budget: Effective and Efficient Test-Time Scaling on Reasoning Large Language Models](../../archive/papers/2026/title-f0073c841a41fca9/summary.md) (2026-01-01)
  - Plan-and-Budget decomposes queries into sub-questions and allocates test-time token budgets by estimated complexity, using a theoretical model of reasoning as sequential sub-questions to reduce both overthinking and underthinking.
- [Pruning Long Chain-of-Thought of Large Reasoning Models via Small-Scale Preference Optimization](../../archive/papers/2026/title-0694f0010d7ac51f/summary.md) (2026-01-01)
  - Proposes Length Controlled Preference Optimization (LCPO), a small-scale preference-tuning method that cuts large reasoning models' average output length by over 50% while preserving reasoning performance.
- [When More is Less: Understanding Chain-of-Thought Length in LLMs](../../archive/papers/2026/title-221551a348e7dac5/summary.md) (2026-01-01)
  - Shows chain-of-thought accuracy follows an inverted U-shape in reasoning length, derives how the optimal CoT length scales with task difficulty and model capability, and uses this to explain and mitigate overthinking via RL-based length calibration and length-aware filtering.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
