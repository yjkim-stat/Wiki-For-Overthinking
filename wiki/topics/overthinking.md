# Overthinking

<!-- auto:begin -->

When and why large reasoning models think more than a problem needs (or less than it needs) — the accuracy/efficiency tradeoff of reasoning length, test-time compute scaling, and methods to make a model stop, or keep going, at the right point.

- **Slug**: `overthinking`
- **Papers**: 278
- **Seminars**: 0
- **Tracked keywords**: `overthinking`, `underthinking`, `over-thinking`, `under-thinking`, `reasoning length`, `test-time compute`, `test time scaling`, `inverse scaling`, `chain-of-thought length`, `thinking budget`, `reasoning-action dilemma`, `large reasoning model`, `adaptive compression`, `accuracy-efficiency tradeoff`, `reasoning effort`, `thinking effort`, `reasoning budget`, `token budget`, `reasoning token`, `reasoning-token`, `shared budget`, `resource-rational`, `compute-optimal`, `cost-bounded`, `early stopping`, `early exit`, `efficient reasoning`, `reasoning efficiency`, `parallel reasoning`, `test-time depth`, `token pricing`, `concise reasoning`, `adaptive reasoning`, `adaptive thinking`, `thinking model`, `reasoning trace`

## Most recent papers

- [Training-Free Inference-Time Self-Reflection and Cost-Bounded Early Stopping for Large Language Models](../../archive/papers/2026/arxiv-2608-18884/summary.md) (2026-08-19)
  - A training-free generate-critique-revise loop over a frozen backbone that stops when the critique emits a CONFIRMED sentinel or a depth cap is hit, measured across nine experiments to show the sentinel halts 82-88% of items at about 2.1 generations, with accuracy flat on BBH and significantly higher on GSM8K and MATH.
- [Can a Lightweight Multimodal Model Estimate LLM Reasoning Performance? A Study for Compute-Optimal Document Inference](../../archive/papers/2026/arxiv-2608-18591/summary.md) (2026-08-19)
  - Trains a ~1B-parameter multimodal model to predict, before any API call, which of seven performance bins a frontier LLM will land in for a given (document, prompt, model, reasoning budget) tuple, and uses those predictions to pick a per-sample reasoning budget for document tasks.
- [SMTrap: Cost-Effective DoS Attacks Against Large Reasoning Models via SMT Conflict Guidance](../../archive/papers/2026/arxiv-2608-18921/summary.md) (2026-08-19)
  - SMTrap uses SMT solver conflict counts as a free, model-feedback-free proxy to synthesize Sudoku and zebra-puzzle queries that induce excessive backtracking-driven reasoning in large reasoning models, mounting a state-of-the-art denial-of-service attack that a bounded-solver defense can neutralize.
- [Test-Time Scaling in the Wild: Why Exploitation, Not Exploration, Is the Bottleneck](../../archive/papers/2026/arxiv-2608-18931/summary.md) (2026-08-19)
  - A compute-normalised, five-benchmark comparison of test-time scaling methods on open-ended generation finds that the candidate pool improves steadily with compute, but exploitation - selecting or synthesising the final answer from that pool - is the bottleneck, with reward-model-based selection near random (verifier correlation ~0.12) and even the best method (Fusion) recovering only ~40% of available quality.
- [Think Shallow, Solve Deep: Controlling Recurrent Dynamics for Reliable Test-Time Depth](../../archive/papers/2026/arxiv-2608-18222/summary.md) (2026-08-18)
  - Shows that whether a recurrent-depth reasoner is helped or harmed by extra test-time iterations is predicted by a measurable dynamical property of its trained update map (settling, marginal, or drifting), proves a sufficient condition for the decoded answer to be frozen under further iteration, and demonstrates that a single terminal fixed-point loss term moves the regime and the depth behaviour together in both directions.
- [ParaTempo: Efficient Parallel Reasoning via Temporal Confidence](../../archive/papers/2026/arxiv-2608-16425/summary.md) (2026-08-17)
  - A training-free controller for parallel reasoning that probes each branch every 500 tokens for a tentative answer distribution, averages recent probes into a 'temporal confidence' score, and uses that one signal to prune, retire, fork and globally stop branches.
- [The Price of Thinking: Reasoning Effort as a Model-Specific API Contract](../../archive/papers/2026/arxiv-2608-16956/summary.md) (2026-08-16)
  - A preregistered, paired 360-call measurement on 30 AIME 2026 items of what a buyer gets by setting a reasoning-effort parameter explicitly versus omitting it on the same model, pricing every paid attempt including wrong and no-answer ones.
- [Funnel of Thoughts: Efficient Test-Time Scaling via Early Voting and Rollout Pruning](../../archive/papers/2026/arxiv-2608-15065/summary.md) (2026-08-15)
  - Funnel of Thoughts detects and discards the subset of parallel reasoning rollouts that are spiraling into unproductive self-correction (flagged by a rising density of hesitation words like 'Wait' and 'perhaps'), matching self-consistency's accuracy while cutting attention FLOPs by up to 56% and wall time by 37.6%.
- [Divergent-Convergent Reasoning: Scaling Test-Time Compute through Structured Solution Synthesis](../../archive/papers/2026/arxiv-2608-15303/summary.md) (2026-08-15)
  - Divergent-Convergent Reasoning generates diverse candidate solutions and then uses reviewer-style reconciliation calls (optionally run recursively with a verifier-free unanimous-consent stopping rule) to recover correct answers even when they start out as a minority, reaching 93.3% on AIME 2024 and 92.0% on AIME 2025 while using about 27% less compute than a fixed single-round baseline.
- [BiasTrace: Linking Reasoning Behaviours to Biased Outputs in LLMs](../../archive/papers/2026/arxiv-2608-14161/summary.md) (2026-08-14)
  - Introduces BiasTrace, a six-label annotation scheme for reasoning behaviours in bias-sensitive traces, and finds that overthinking (repeated second-guessing or revisiting the same options more than three times) is the strongest behavioural predictor of stereotype-aligned answers on BBQ, then uses the scheme to filter samples at inference time.
- [Keep, Customize, or Exit: Default Design and Token Pricing in LLM Reasoning Services](../../archive/papers/2026/arxiv-2608-13315/summary.md) (2026-08-13)
  - Models an LLM reasoning service as a Stackelberg game in which the provider sets a per-token price and a default reasoning-token budget while the user may keep the default, customize it, or exit, and shows the provider's optimal default sits above the budget the user would choose.
- [Amplified Does Not Mean Predictive: Reasoning Behaviors in Thinking Models](../../archive/papers/2026/arxiv-2608-13760/summary.md) (2026-08-13)
  - Annotates 15,282 reasoning traces from 15 models on 6 benchmarks with a nine-behavior taxonomy and shows that the behaviors reasoning-oriented training amplifies most (self-correction, hypothesis testing, uncertainty acknowledgment) are not the behaviors most associated with getting the answer right (confidence calibration, knowledge alignment, self-awareness).
- [Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling](../../archive/papers/2026/arxiv-2608-11829/summary.md) (2026-08-12)
  - Using pass@K/avg@K analysis, the paper shows on-policy distillation improves a student model's sampling efficiency at small K but does not expand its reasoning capability boundary at large K, and even causes it to forget some previously solvable problems.
- [Reasoning Jury: Multi-Model Consensus for Evaluating Reasoning Traces](../../archive/papers/2026/arxiv-2608-12585/summary.md) (2026-08-12)
  - Replaces the single LLM judge of a long reasoning trace with a panel of jurors that first judge independently and then reach consensus through a blind moderator's deliberation or a consolidation pass, letting cheap open-weight models beat frontier single judges at step-level defect localization for a fraction of the dollar cost.
- [LEMUR: Latent Entropy-aware Multimodal Unlearning via Visual-anchored Reasoning Redirection](../../archive/papers/2026/arxiv-2608-11691/summary.md) (2026-08-12)
  - A training-free, inference-time unlearning method for RL-trained multimodal reasoning models that detects memorized private attributes from a token-level entropy signature and replaces the committed tokens with image-grounded sanitized embeddings.
- [Claim-Level Reliability Assessment for Efficient Test-Time Reasoning](../../archive/papers/2026/arxiv-2608-11994/summary.md) (2026-08-12)
  - CLR reallocates part of the test-time compute budget from generating more solution samples to falsifying a small set of decision-critical claims extracted from each trace, improving accuracy over self-consistency while using fewer tokens on some models.
- [Towards Efficient Reasoning in LLM-Based Recommender Systems via Model Merging](../../archive/papers/2026/arxiv-2608-10447/summary.md) (2026-08-11)
  - REAM merges a slow-thinking recommender with a fast-thinking one at the granularity of individual attention heads, assigning each head a merge coefficient from its reasoning importance and its parameter sensitivity, to shorten reasoning traces without retraining.
- [ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling](../../archive/papers/2026/arxiv-2608-10928/summary.md) (2026-08-11)
  - ThinkRetrieve augments each step of a reasoning model's chain of thought with a dynamically retrieved, fully worked solved example (rather than just facts), consistently beating standard sequential test-time scaling on math and QA benchmarks.
- [Test-Time Scaling for CAD Generation via Verifier-Free Consensus Selection](../../archive/papers/2026/arxiv-2608-09706/summary.md) (2026-08-10)
  - Introduces verifier-free 'consensus selection' for text-to-CAD generation, picking among N compiled 3D CAD candidates the one that geometrically or topologically agrees most with the rest of the pool.
- [Stealing Reasoning Traces from Proprietary LLM APIs](../../archive/papers/2026/arxiv-2608-09867/summary.md) (2026-08-10)
  - Shows that the encrypted chain-of-thought blocks returned by Anthropic, OpenAI and Google APIs are interchangeable across sessions, users and models within a provider, and uses a weaker sibling model as a decryption oracle to recover hidden reasoning traces verbatim.
- [Consilience for Verifier-Free Test-Time Scaling](../../archive/papers/2026/arxiv-2608-09898/summary.md) (2026-08-10)
  - Introduces consilience, a verifier-free test-time-scaling selection metric that picks the sampled reasoning rollout whose confidence starts low (exploratory) and ends high (convergent), fixing a failure mode where naive confidence maximization favors confidently wrong answers on hard problems.
- [Efficient Test-Time Scaling for LLM-based Time Series Forecasting](../../archive/papers/2026/arxiv-2608-08675/summary.md) (2026-08-09)
  - Proposes SCALER, a coarse-to-fine LLM-based time-series forecaster that first predicts a lightweight global shape and then uses it to guide cheaper, fixed-step test-time refinement of the full-resolution forecast.
- [LLM Reasoning for Subjective Tasks: Failure Modes, Mitigation, and Dynamic Reasoning Routing](../../archive/papers/2026/arxiv-2608-08889/summary.md) (2026-08-09)
  - An empirical study of LLM verifiers on four subjective verification tasks from a production recommender platform, showing that explicit reasoning often degrades accuracy and that standard RLVR drives reasoning length to near zero ('reasoning collapse'), plus a conditional length-penalized reward that restores it.
- [Reason Wide, Not Deep: Amortizing the Reasoning Premium into Distilled Skills](../../archive/papers/2026/arxiv-2608-07885/summary.md) (2026-08-08)
  - Distills a short natural-language 'skill' from an existing corpus of agent trajectories with a coding agent, injects it into a non-reasoning model's system prompt, and measures how much of the think/no-think gap it recovers at a fraction of the output tokens.
- [Thinking Hard, Not Smart: Reasoning Models Fail to Ration Test-Time Compute Across Questions](../../archive/papers/2026/arxiv-2608-07968/summary.md) (2026-08-08)
  - Introduces an exam-style evaluation where reasoning models must divide one shared token budget across multiple questions of different difficulty and value, and finds they allocate it by presentation order rather than by difficulty or value.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
