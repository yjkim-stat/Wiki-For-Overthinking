# Overthinking

<!-- auto:begin -->

A large reasoning model spending more reasoning tokens or steps on a problem than the problem needs, in a way that wastes compute for no accuracy gain, actively lowers accuracy, or degrades safety- or fairness-relevant behavior (e.g. more stereotype-aligned answers under sustained self-doubt, worse AI-risk judgments) as reasoning length grows. It is measured and explained several ways across the archive: an accuracy-vs-token-length curve that peaks and then falls (inverted-U); a model abandoning a previously correct intermediate answer ('flip events') or reasoning itself out of a right answer; excessive, unproductive self-verification and backtracking; information-theoretic divergence from an ideal reasoning path; a low-dimensional direction in activation space; and, on agentic tasks (software engineering, robotic action planning), favoring internal reasoning over acting in the environment. It is mitigated by length-penalized preference optimization, self-braking or self-training, decoupled token-level rewards with curriculum scheduling, activation steering, verifier-based trimming, decoding-tree early termination, parallel short-sample voting, and budget-aware query decomposition -- most reporting 30-70% token reductions at little or no accuracy cost, though a 33-model unified benchmark (OptimalThinkingBench) finds no evaluated model yet balances over- and under-thinking well.

- **Kind**: concept
- **Also called**: Overthinking, overthinking
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 51

**Related**: [A*-Thought](../methods/a-thought.md), [Accuracy-Efficiency Score (AES)](accuracy-efficiency-score-aes.md), [accuracy-efficiency tradeoff](accuracy-efficiency-tradeoff.md), [accuracy-efficiency tradeoff of reasoning length](accuracy-efficiency-tradeoff-of-reasoning-length.md), [Accuracy-Length Tradeoff](accuracy-length-tradeoff.md), [activation steering](../methods/activation-steering.md), [Ada-GRPO](../methods/ada-grpo.md), [Ada-R1](../methods/ada-r1.md), [adaptive reasoning](adaptive-reasoning.md), [adaptive reasoning length](adaptive-reasoning-length.md), [AdaptThink](../methods/adaptthink.md), [Aha Moment](aha-moment.md), [AIME](../datasets/aime.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [ARES](../methods/ares.md), [AUC_OAA](auc-oaa.md), [AutoThink](../methods/autothink.md), [BBH](../datasets/bbh.md), [Best-of-N sampling](../methods/best-of-n-sampling.md), [Budget Forcing](../methods/budget-forcing.md), [Chain-of-Draft](../methods/chain-of-draft.md), [Chain-of-Thought Compression](chain-of-thought-compression.md), [Chain-of-Thought Distillation](../methods/chain-of-thought-distillation.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [CommonsenseQA](../datasets/commonsenseqa.md), [Confidence-based early stopping](../methods/confidence-based-early-stopping.md), [Conformal Prediction](../methods/conformal-prediction.md), [DAPO](../methods/dapo.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DeepScaleR](../datasets/deepscaler.md), [DeepSeek-R1-Distill-Llama-8B](../methods/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../methods/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../methods/deepseek-r1-distill-qwen-7b.md), [DEER](../methods/deer.md), [Difficulty-aware compute allocation](difficulty-aware-compute-allocation.md), [difficulty-based routing between reasoning modes](difficulty-based-routing-between-reasoning-modes.md), [DPO_Shortest](../methods/dpo-shortest.md), [Dr. GRPO](../methods/dr-grpo.md), [DRP](../methods/drp.md), [Dynamic Early Exit](../methods/dynamic-early-exit.md), [Dynasor](../methods/dynasor.md), [Early Exit](../methods/early-exit.md), [early stopping](early-stopping.md), [Efficient Reasoning](efficient-reasoning.md), [F1^otb combined metric](f1-otb-combined-metric.md), [GFPO](../methods/gfpo.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [Group-Relative Advantage](group-relative-advantage.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [Hidden-State Probing](hidden-state-probing.md), [HLE](../datasets/hle.md), [HMMT 2025](../datasets/hmmt-2025.md), [HMMT25](../datasets/hmmt25.md), [HotpotQA](../datasets/hotpotqa.md), [HumanEval](../datasets/humaneval.md), [hybrid thinking/non-thinking models](hybrid-thinking-non-thinking-models.md), [inverse scaling](inverse-scaling.md), [KV-cache compression](../methods/kv-cache-compression.md), [L1 length-controlled reinforcement learning](../methods/l1-length-controlled-reinforcement-learning.md), [Laser](../methods/laser.md), [LC-R1](../methods/lc-r1.md), [Length Penalty](length-penalty.md), [Length reward](length-reward.md), [linear probe](../methods/linear-probe.md), [LiveCodeBench](../datasets/livecodebench.md), [LiveCodeBench-v6](../datasets/livecodebench-v6.md), [Llama-3-8B](../models/llama-3-8b.md), [LLM-as-a-Judge](../methods/llm-as-a-judge.md), [Majority Voting](../methods/majority-voting.md), [Manifold Steering](../methods/manifold-steering.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MathQA](../datasets/mathqa.md), [MathVerse](../datasets/mathverse.md), [MathVision](../datasets/mathvision.md), [MathVista](../datasets/mathvista.md), [MBPP](../datasets/mbpp.md), [mechanistic interpretability](mechanistic-interpretability.md), [Minerva](../datasets/minerva.md), [MMLU](../datasets/mmlu.md), [MMLU-Pro](../datasets/mmlu-pro.md), [MMLU-STEM](../datasets/mmlu-stem.md), [MMMU](../datasets/mmmu.md), [MMStar](../datasets/mmstar.md), [Model Merging](../methods/model-merging.md), [Natural Questions](../datasets/natural-questions.md), [NoThinking](../methods/nothinking.md), [NOWAIT](../methods/nowait.md), [O1-Pruner](../methods/o1-pruner.md), [OlympiadBench](../datasets/olympiadbench.md), [Omni-MATH](../datasets/omni-math.md), [Overthinking-Adjusted Accuracy (OAA)](overthinking-adjusted-accuracy-oaa.md), [OverthinkingBench](../datasets/overthinkingbench.md), [pass@K](pass-k.md), [PLAN-AND-BUDGET](../methods/plan-and-budget.md), [Preference Optimization](../methods/preference-optimization.md), [process reward model](../methods/process-reward-model.md), [Qwen2.5-Instruct](../methods/qwen2-5-instruct.md), [Qwen2.5-VL](../methods/qwen2-5-vl.md), [Qwen3-8B](../methods/qwen3-8b.md), [QwQ-32B](../methods/qwq-32b.md), [R-KV](../methods/r-kv.md), [Reasoning Collapse](reasoning-collapse.md), [reasoning effort](reasoning-effort.md), [Reasoning Segmentation](reasoning-segmentation.md), [Reasoning Trace Length](reasoning-trace-length.md), [ReasonSeg](../datasets/reasonseg.md), [Redundant Self-Verification](redundant-self-verification.md), [RefCOCO](../datasets/refcoco.md), [RefCOCOg](../datasets/refcocog.md), [Resource-Rational Reasoning](resource-rational-reasoning.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [retrieval-augmented reasoning](retrieval-augmented-reasoning.md), [Reward Hacking](reward-hacking.md), [Reward Shaping](reward-shaping.md), [RLOO](../methods/rloo.md), [RLVR](../methods/rlvr.md), [S-GRPO](../methods/s-grpo.md), [s1K-1.1](../datasets/s1k-1-1.md), [SEAL](../methods/seal.md), [Seg-Zero (baseline)](../methods/seg-zero-baseline.md), [Self-Certainty](self-certainty.md), [Self-Consistency](../methods/self-consistency.md), [Self-Distillation](self-distillation.md), [Self-verification](../methods/self-verification.md), [SelfBudgeter](../methods/selfbudgeter.md), [Sequential revision](sequential-revision.md), [SFT_Shortest](../methods/sft-shortest.md), [SPIRIT](../methods/spirit.md), [Still](../datasets/still.md), [StrategyQA](../datasets/strategyqa.md), [supervised fine-tuning](supervised-fine-tuning.md), [SVAMP](../datasets/svamp.md), [SWE-bench Verified](../datasets/swe-bench-verified.md), [Task Decomposition](task-decomposition.md), [Test-Time Compute](test-time-compute.md), [Test-Time Compute Scaling](test-time-compute-scaling.md), [Test-Time Scaling](test-time-scaling.md), [thinking-token budget](thinking-token-budget.md), [Thinkless](../methods/thinkless.md), [ThinkPrune](../methods/thinkprune.md), [Token Budget](token-budget.md), [Token-Level Entropy](token-level-entropy.md), [TokenSkip](../methods/tokenskip.md), [trained difficulty-based router / oracle router](trained-difficulty-based-router-oracle-router.md), [TrimR](../methods/trimr.md), [Uncertainty Quantification](uncertainty-quantification.md), [underthinking](underthinking.md), [UnderthinkingBench](../datasets/underthinkingbench.md), [VeriThinker](../methods/verithinker.md), [veRL](../methods/verl.md), [WeMath](../datasets/wemath.md)

## What we have settled

- **Established** — Reasoning-trace length is not a measure of overthinking: it correlates negatively with accuracy, so a longer trace is evidence about the problem rather than about waste.
  - Three archive records establish this from different directions. Think Deep, Not Just Long ranks eight inference-time signals by mean Pearson correlation with accuracy and finds token length at -0.594, below every internal-state signal it tests (DTR +0.683, self-certainty +0.605, negative entropy +0.571, log-probability +0.527, negative perplexity +0.219) -- so the field's default proxy points the wrong way. LLMThinkBench shows the same thing on a matched pair that isolates training as the cause: Phi-4 scores 78.92 percent at 378.6 tokens per response while Phi-4-reasoning, the same base model under CoT supervision, scores 72.23 percent at 6,066.2 tokens, losing 6.69 accuracy points for roughly 16 times the tokens; its composite Overthinking Score reads 0.863 against 0.352. Do NOT Think That Much for 2+3=? gives the conceptual reason by splitting the quantity in two, outcome efficiency (whether extra compute changes the answer) and process efficiency (what fraction of the chain is redundant), which are independent: how much was emitted and how much was wasted are different questions. The consequence for this archive is that a token count is a cost, not a diagnosis, and any claim that one model overthinks more than another because it emits more tokens is unsupported.

## Appears in

- [EvoThink: Evolving Thinking in Large Reasoning Models via Self-Pruning and Aha-Moment Preference Optimization](../../archive/papers/2026/arxiv-2607-19962/summary.md) — EvoThink cuts overthinking in two separable stages: Self-Pruning Training deletes reasoning steps whose local conclusion repeats the previous step's and self-trains on the shortened traces, while Aha-Moment Preference Optimization builds from-wrong-to-right preference pairs out of the model's most diverse failed attempts and applies DPO to them.
- [BLADE: Boundary-Expanded and Layer-Adaptive Dynamic Exit for Efficient LLM Reasoning](../../archive/papers/2026/arxiv-2607-28966/summary.md) — BLADE trains a lightweight hidden-state probe to decide, at sentence and self-doubt boundaries, whether a reasoning prefix already supports the correct answer, and stops generation when it does.
- [Translation with Thought: Difficulty-Adaptive Reasoning via Reinforcement Learning for Multi-Domain Machine Translation](../../archive/papers/2026/arxiv-2607-29287/summary.md) — TwT trains a translation model to spend reasoning tokens in proportion to input difficulty, by cold-starting on 7K difficulty-rewritten CoT traces and then running GRPO with a BLEU+COMET quality reward and an n-gram repetition penalty.
- [Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning](../../archive/papers/2026/arxiv-2608-04771/summary.md) — ReCo uses a 30M process-reward estimator to set, per reasoning step, both the KV-cache retention ratio and generation-side controls (a reflection-token logit penalty and confidence-based early stopping), cutting generated tokens by 37-65% and end-to-end latency by 2.08-2.35x versus full-cache CoT.
- [BiasTrace: Linking Reasoning Behaviours to Biased Outputs in LLMs](../../archive/papers/2026/arxiv-2608-14161/summary.md) — Introduces BiasTrace, a six-label annotation scheme for reasoning behaviours in bias-sensitive traces, and finds that overthinking (repeated second-guessing or revisiting the same options more than three times) is the strongest behavioural predictor of stereotype-aligned answers on BBQ, then uses the scheme to filter samples at inference time.
- [Inverse Scaling in Test-Time Compute](../../archive/papers/2025/local-018eb3ee241c1a69/summary.md) — Constructs evaluation tasks across four categories (distractor counting, spurious-feature regression, constraint-tracking deduction, and AI-risk model-written evaluations) where letting large reasoning models reason longer at test time makes their accuracy or alignment worse, not better.
- [When More Thinking Hurts: Overthinking in LLM Test-Time Compute Scaling](../../archive/papers/2026/local-32a56cfa1105c39e/summary.md) — The paper shows that extended chain-of-thought reasoning in LLMs has diminishing and eventually negative marginal utility, quantifies this 'overthinking' via answer-flip tracking, and proposes cost-aware, indicator-based early-stopping strategies that cut compute substantially with little accuracy loss.
- [Towards a Mechanistic Understanding of Large Reasoning Models: A Survey of Training, Inference, and Failures](../../archive/papers/2026/local-34cecfd6f28ba72b/summary.md) — A survey that organizes existing mechanistic-interpretability research on large reasoning models into three areas -- reasoning-oriented training dynamics, reasoning mechanisms, and unintended behaviors (hallucination, CoT unfaithfulness, overthinking, unsafety) -- and proposes directions for future mechanistic work.
- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2025/local-49199e3b0f694ee1/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.
- [Between Underthinking and Overthinking: An Empirical Study of Reasoning Length and correctness in LLMs](../../archive/papers/2025/local-6afb006d68240134/summary.md) — An empirical study showing reasoning LLMs overthink easy questions and underthink hard ones, and that preferring shorter outputs via SimPO can cut generation length 30-60% with little accuracy loss.
- [Don't Overthink It: A Survey of Efficient R1-style Large Reasoning Models](../../archive/papers/2025/local-6c80b6fd388d671e/summary.md) — A survey that organizes methods for making R1-style large reasoning models reason efficiently (i.e., avoid overthinking) into two axes: single-model optimization and multi-model collaboration.
- [The Danger of Overthinking: Examining the Reasoning-Action Dilemma in Agentic Tasks](../../archive/papers/2025/local-9f60265e5ada34cb/summary.md) — Defines and measures 'overthinking' in Large Reasoning Models on real software-engineering agent tasks, showing that favoring internal reasoning over environment interaction correlates with lower SWE-bench issue-resolution rates and can be mitigated at lower cost.
- [Exposing Weaknesses of Large Reasoning Models through Graph Algorithm Problems](../../archive/papers/2026/title-00481a9889909bb4/summary.md) — Introduces GrAlgoBench, a graph-algorithm-problem benchmark that exposes two weaknesses of large reasoning models: accuracy collapse on long-context inputs and unproductive overthinking via excessive self-verification.
- [Pruning Long Chain-of-Thought of Large Reasoning Models via Small-Scale Preference Optimization](../../archive/papers/2026/title-0694f0010d7ac51f/summary.md) — Proposes Length Controlled Preference Optimization (LCPO), a small-scale preference-tuning method that cuts large reasoning models' average output length by over 50% while preserving reasoning performance.
- [Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL](../../archive/papers/2025/title-0bc5d9b198744bed/summary.md) — AutoThink uses a three-stage RL curriculum with stage-wise reward shaping to teach R1-style distilled models to decide per problem whether to emit an explicit reasoning chain at all.
- [Short Chains, Deep Thoughts: Balancing Reasoning Efficiency and Intra-Segment Capability via Split-Merge Optimization](../../archive/papers/2026/title-0bf980e6919c2982/summary.md) — CoSMo restructures reasoning chains by merging redundant segments and splitting logical gaps, then trains with RL against a segment-count budget rather than a token budget.
- [ConPress: Learning Efficient Reasoning from Multi-Question Contextual Pressure](../../archive/papers/2026/title-11f96b3e58a44cf5/summary.md) — ConPress observes that a reasoning model shortens its traces when several independent questions share one prompt, and harvests those shortened traces as self-supervised fine-tuning data for the single-question setting.
- [ARM: Adaptive Reasoning Model](../../archive/papers/2025/title-21d562149c3adad6/summary.md) — ARM trains a model to pick among four reasoning formats (Direct Answer, Short CoT, Code, Long CoT) per task using Ada-GRPO, cutting average tokens by about 30% at roughly unchanged accuracy.
- [How Far Are We from Optimal Reasoning Efficiency?](../../archive/papers/2025/title-279ee92c27a8bb8d/summary.md) — Defines an empirical accuracy-vs-token-budget frontier for a fixed base reasoning model, measures how far existing efficiency methods fall short of it with a single metric (REG), and proposes REO-RL, an RL objective that targets a handful of token budgets to close most of that gap.
- [Let LRMs Break Free from Overthinking via Self-Braking Tuning](../../archive/papers/2025/title-2b17dd2ef08b6fa4/summary.md) — Introduces Self-Braking Tuning, which trains a large reasoning model to detect and stop its own redundant reasoning steps, cutting token usage by up to 60% with comparable accuracy on math benchmarks.
- [Retrieval-of-Thought: Efficient Reasoning via Reusing Thoughts](../../archive/papers/2026/title-2c8dfbd1f24680a2/summary.md) — Retrieval-of-Thought stores prior reasoning as a graph of composable thought steps and, at inference, retrieves and traverses it to assemble a problem-specific template that shortens the model's generated reasoning without retraining.
- [WS-GRPO: Weakly-Supervised Group-Relative Policy Optimization for Rollout-Efficient Reasoning](../../archive/papers/2026/title-39bbcb4cded34ec7/summary.md) — WS-GRPO trains a preference model from outcome-only correctness labels to score partial reasoning trajectories, turning terminal reward into prefix-level signal about whether continuing is worthwhile, and reports far shorter reasoning at some accuracy cost.
- [REA-RL: Reflection-Aware Online Reinforcement Learning for Efficient Reasoning](../../archive/papers/2026/title-474d6c4d88a30199/summary.md) — REA-RL trains a large reasoning model online with a distilled 7B reflection model that supplies both parallel samples and truncated sequential revisions, plus a reflection-density reward, cutting response length about 36% on math benchmarks without losing accuracy.
- [Is it Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort](../../archive/papers/2026/title-49c61dced5ecc63a/summary.md) — TRACE detects implicit reward hacking by truncating a model's chain of thought at increasing fractions, forcing an answer at each cut, and scoring the area under the resulting reward-versus-CoT-length curve — a hacking model reaches high reward with little of its reasoning consumed.
- [IAPO: Information-Aware Policy Optimization for Token-Efficient Reasoning](../../archive/papers/2026/title-4bd9ad89663d1e26/summary.md) — IAPO shapes token-level RL advantages by each reasoning token's conditional mutual information with the final answer, so uninformative exploration is suppressed rather than length being penalized in aggregate, reporting up to 36% shorter reasoning at equal or better accuracy on math benchmarks.
- [SmartThinker: Progressive Chain-of-Thought Length Calibration for Efficient Large Language Model Reasoning](../../archive/papers/2026/title-535dc7d9e1ccc5d5/summary.md) — A GRPO-based training method that dynamically calibrates the target chain-of-thought length per problem to cut redundant reasoning without penalizing correct long answers.
- [ARES: Multimodal Adaptive Reasoning via Difficulty-Aware Token-Level Entropy Shaping](../../archive/papers/2026/title-544eea46a2eb68c1/summary.md) — ARES trains multimodal reasoning models to spend exploration effort in proportion to problem difficulty, using sliding-window token entropy as the signal for when and how much to explore.
- [DR$^2$Seg: Decomposed Two-Stage Rollouts for Efficient Reasoning Segmentation in Multimodal Large Language Models](../../archive/papers/2026/title-56bdffcf992c5e91/summary.md) — DR2Seg splits reasoning segmentation into a description stage and a referring-segmentation stage and rewards the model when a shorter self-contained description still yields the right mask, cutting reasoning length while raising gIoU.
- [Statistical Early Stopping for Reasoning Models](../../archive/papers/2026/title-594984624acaa60d/summary.md) — Two statistical stopping rules monitor uncertainty-keyword arrivals inside a reasoning trace and halt generation on ill-posed or ambiguous queries, one with a finite-sample bound on the probability of halting too early on a well-posed query.
- [Does Thinking More Always Help? Mirage of Test-Time Scaling in Reasoning Models](../../archive/papers/2025/title-5d66fe9a10241ce8/summary.md) — Shows that extending a reasoning model's thinking trace improves accuracy only up to a point and then declines from overthinking, and proposes sampling multiple independent short traces (parallel thinking) with majority vote as a more effective use of the same compute budget.
- [Think or Not? Exploring Thinking Efficiency in Large Reasoning Models via an Information-Theoretic Lens](../../archive/papers/2025/title-640d466d159a19d8/summary.md) — Uses information-theoretic metrics (InfoBias, InfoGain) to show that longer reasoning chains in LRMs grow less informative and more divergent from an ideal path, and introduces an entropy-based stopping rule that cuts token usage while preserving accuracy.
- [DRPO: Efficient Reasoning via Decoupled Reward Policy Optimization](../../archive/papers/2026/title-68327bf6b9e4e869/summary.md) — Diagnoses why adding a length penalty to GRPO degrades accuracy — the group-relative advantage can turn correct-but-long rollouts negative — and fixes it by normalising the reward of correct rollouts only against other correct rollouts.
- [S-GRPO: Early Exit via Reinforcement Learning in Reasoning Models](../../archive/papers/2025/title-69eddf96377a8095/summary.md) — S-GRPO trains a reasoning model to stop its chain of thought early by sampling one reasoning path, forcing answers at several truncation points along it, and paying correct answers a reward that decays with how late the exit was.
- [A*-Thought: Efficient Reasoning via Bidirectional Compression for Low-Resource Settings](../../archive/papers/2025/title-6ac5c2757444abad/summary.md) — A*-Thought treats a long reasoning trace as a search tree over reasoning spans and uses A* search with a bidirectional importance score to select a short, high-information subset of it as supervised fine-tuning data for compressed reasoning.
- [When Simple Problems Wear Complex Costumes: Improving Efficiency in LRM's Adaptive Reasoning](../../archive/papers/2026/title-75760913d4d6cfa4/summary.md) — Trains an adaptive reasoning model in two stages -- SFT on simple problems presented in both concise and verbose phrasings, then GRPO with a custom reward -- so that its choice between explicit reasoning and a direct answer tracks actual task difficulty rather than how wordy the question is.
- [Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](../../archive/papers/2025/title-7805f8ec24eadc13/summary.md) — The first systematic study of overthinking in o1-like reasoning models, introducing outcome/process efficiency metrics and a self-training method that trims redundant reasoning on easy problems without hurting accuracy.
- [Efficient Reasoning with Balanced Thinking](../../archive/papers/2026/title-7a3e08192f168bcb/summary.md) — ReBalance is a training-free inference-time steering method that reads a reasoning model's token confidence to detect overthinking or underthinking and applies a hidden-state steering vector to shorten or extend the chain of thought accordingly.
- [Stop Unnecessary Reflection: Training LRMs for Efficient Reasoning with Adaptive Reflection and Length Coordinated Penalty](../../archive/papers/2026/title-833de99e9b3ea69d/summary.md) — ARLCP is a reinforcement-learning fine-tuning recipe that adds two coupled reward penalties -- one on reflective steps, one on response length scaled by estimated problem complexity -- to shorten chains of thought in distilled reasoning models without losing accuracy.
- [Overthinking Reduction with Decoupled Rewards and Curriculum Data Scheduling](../../archive/papers/2026/title-a0cc8089e70a3eb9/summary.md) — Introduces DECS, a decoupled token-level reward plus curriculum batch scheduling method that cuts reasoning-token length by over 50% while maintaining or improving accuracy in RLVR-trained reasoning models.
- [SuCo: Sufficiency-guided Continuous Adaptive Reasoning](../../archive/papers/2026/title-b37859867120f044/summary.md) — Defines the Minimal Sufficient CoT — the shortest reasoning prefix at which the model's confidence in the ground-truth answer crosses a difficulty-adaptive threshold — and trains on it via supervised fine-tuning plus a GRPO stage whose reward penalises both over- and under-thinking, so reasoning length is calibrated continuously rather than by discrete modes.
- [Mitigating Overthinking in Large Reasoning Models via Manifold Steering](../../archive/papers/2025/title-b4ba27743c499d8d/summary.md) — Identifies that overthinking in large reasoning models corresponds to a low-dimensional manifold in activation space and proposes projecting steering interventions onto that manifold to cut output tokens by up to 71% without hurting accuracy.
- [TrimR: Verifier-based Training-Free Thinking Trimming for Efficient Test-Time Scaling](../../archive/papers/2026/title-b987d2649d32f1f3/summary.md) — TrimR is a training-free, verifier-based system that trims redundant chain-of-thought reasoning in deployed large reasoning models to speed up test-time scaling with little accuracy loss.
- [Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens](../../archive/papers/2026/title-bcd9cf99a0e84a2d/summary.md) — Measures a reasoning model's inference-time effort not by how many tokens it emits but by what fraction of them are still being revised in the network's late layers, and uses that fraction to pick which of many sampled generations to keep.
- [DTS: Enhancing Large Reasoning Models via Decoding Tree Sketching](../../archive/papers/2026/title-c614f5d4c1a5c21d/summary.md) — A decoding-time framework that sketches a reasoning tree via selective branching and terminates long, low-accuracy reasoning trajectories early, using an observed length-accuracy anti-correlation.
- [ShorterBetter: Guiding Reasoning Models to Find Optimal Inference Length for Efficient Reasoning](../../archive/papers/2025/title-d40396527f776f1d/summary.md) — ShorterBetter takes the length of the shortest correct response in a sampled group as a per-problem target and rewards the model for matching it, cutting output length by 50%-80% on DeepSeek-Distill-Qwen-1.5B/7B.
- [Don't Overthink with Pixels: Efficient Reasoning for Segmentation](../../archive/papers/2026/title-d94f940ea2e159b8/summary.md) — PixelThink regulates the length of a multimodal LLM's reasoning chain in reasoning segmentation by conditioning a GRPO reward on an externally estimated task difficulty and the model's own uncertainty, cutting reasoning tokens roughly in half while slightly improving mask accuracy.
- [Don’t Think Longer, Think Wisely: Optimizing Thinking Dynamics for Large Reasoning Models](../../archive/papers/2025/title-edaac274df1e07a6/summary.md) — Segments reasoning traces into thinking patterns, prunes detrimental ones, and uses the resulting optimal-vs-suboptimal pairs for preference optimization to cut reasoning length while improving accuracy.
- [Plan and Budget: Effective and Efficient Test-Time Scaling on Reasoning Large Language Models](../../archive/papers/2026/title-f0073c841a41fca9/summary.md) — Plan-and-Budget decomposes queries into sub-questions and allocates test-time token budgets by estimated complexity, using a theoretical model of reasoning as sequential sub-questions to reduce both overthinking and underthinking.
- [LIMOPro: Reasoning Refinement for Efficient and Effective Test-time Scaling](../../archive/papers/2025/title-f14f82d5eba9e811/summary.md) — PIR scores reasoning steps by their effect on answer confidence and prunes only low-importance verification/error-correction steps from distilled chain-of-thought data, producing models that reason more concisely without losing accuracy.
- [Dynamic Early Exit in Reasoning Models](../../archive/papers/2026/title-f508a5b012a33fd1/summary.md) — DEER is a training-free decoding method that watches for the points where a reasoning model switches thought chains, prompts it for a trial answer there, and terminates the chain of thought when the trial answer's token confidence exceeds a threshold.
- [QFFT, Question-Free Fine-Tuning for Adaptive Reasoning](../../archive/papers/2025/title-ff37e37c3f1ab9b2/summary.md) — QFFT fine-tunes a short-CoT instruct model on Long CoT responses with the question deleted from every training example, so the model keeps its default concise reasoning and switches to reflective Long CoT only when it hits uncertainty or an error, cutting average tokens by roughly 50% at accuracy comparable to ordinary SFT.

<!-- auto:end -->

## Notes

# Making a qualitative failure countable: six families, and no common unit

Assembled 2026-08-22 from the archive. Where a record is abstract-only, that
is said. No `analysis-sources` marker: that counter is checked against this
note's own evidence, and several records below file their concepts under other
names and are not attached here — LLMThinkBench (`local:c1f4e56014fb43fb`),
R³-Bench (`arxiv:2608.16033`), Token Budget Saturation (`arxiv:2607.21433`),
Funnel of Thoughts (`arxiv:2608.15065`), Think Shallow (`arxiv:2608.18222`).

## The measurement problem

Overthinking is a claim about a counterfactual: *this answer would have been
as good, or better, with less thinking*. Nothing in a single trace contains
that counterfactual. **How each family obtains one is what separates them**,
and it is a sharper axis than what they call the quantity.

| Family | Where the counterfactual comes from | Cost |
| --- | --- | --- |
| 1. Benchmark design | Questions filtered until *any* length is excessive | Only measures the easy end |
| 2. Budget sweep | Re-run the same problem at every budget | 32 runs per problem, post hoc |
| 3. Trace-internal counting | Assumed: a repeated conclusion is redundant | No ground truth at all |
| 4. Internal state | None — a correlate, validated against something else | Inherits that something's error |
| 5. LLM judge | The judge's own opinion | Not a reproducible computation |
| 6. Allocation across problems | Other problems that went unsolved | Needs a shared budget to exist |

## 1. Design the benchmark so any length is too much

**LLMThinkBench** (document) defines the **Overthinking Score** as the
harmonic mean of accuracy `A` and normalised token efficiency
`E_t = 1 − (T_i − T_min)/(T_max − T_min)`, and proves five properties: bounded
in `[0,1]`, symmetric, strictly increasing in both arguments, **sublinear
(`O ≤ min(A, E)`)**, and — compared formally against the arithmetic and
geometric means — **maximal penalty for imbalance among symmetric homogeneous
means**. This is the only metric here whose choice of aggregator is argued
rather than assumed.

> Phi-4 **0.863** (78.92% at 378.6 tokens) against Phi-4-reasoning **0.352**
> (72.23% at 6,066.2 tokens). Same base model, CoT supervision the only
> difference: **6.69 accuracy points lost for 16× the tokens.**

**OptimalThinkingBench** (document) builds two sub-benchmarks and refuses to
report either alone:

```
OAA_t    = accuracy counted only for responses under t thinking tokens
AUC_OAA  = area under the OAA_t curve, t_max = 1000
F1^otb   = harmonic mean(AUC_OAA, UnderthinkingBench accuracy)
```

o3 leads at **71.1%**; best open-weight GPT-OSS-120B at 68.3%. **The benchmark
construction is half the metric**: OverthinkingBench keeps only questions
where 8 independently sampled responses agree 8/8, so "easy" is operationally
defined as model consensus. Token use there tracks surface cues, not
difficulty — **+42 thinking tokens per added irrelevant MCQ distractor,
R²=0.94**, and Qwen3 goes 750 → 950 tokens from 1.7B to 235B with accuracy
flat at 86.1–86.8%.

## 2. Sweep the budget — the only family that builds the counterfactual

**When More Thinking Hurts** (document) forces budgets from 500 to 16,000 in
500-token steps, 32 points per problem, temperature 0:

```
MU(t)      = Acc(t+500) − Acc(t)
flip event = predicted answer changes between consecutive budgets
flip ratio = negative flips / positive flips      > 1 ⇒ thinking harms more than it helps
```

Marginal utility falls **+3.2%** (0.5–2K) to **−0.3%** (12–16K) on AIME with
R1-32B. The flip ratio crosses 1.0 at **~7K tokens** (1.09, 95% CI
[1.01, 1.18], p=0.038) and reaches **7.55** at 16K (CI [6.12, 9.24],
p<0.001); s1-32B crosses at ~5K. Optimal budget varies **7.5×** with
difficulty on MATH-500 (Level 1 at 1.0K, Level 5 at 7.5K).

**And the flips were checked by hand.** Of 80 negative-flip cases on AIME,
**67.5% were genuine overthinking** (explicit reconsideration abandoning a
correct answer), 20.0% exploration divergence, 12.5% degradation artifacts.
That is the closest thing in the archive to a validated instance-level label.

**Token Budget Saturation** (document) reduces the curve to one number:
`B*` = the smallest budget reaching **≥95%** of uncapped accuracy. GSM8K and
MATH-500 saturate at **256 tokens**. AIME does not saturate — it splits, and
**43.5% of generations never emit `</think>` within 10,000 tokens**, scoring
11.5% against 96.5% for those that do.

**How Far Are We from Optimal Reasoning Efficiency** (abstract) fits an
empirical accuracy-vs-budget frontier for a fixed base model and reports
**REG**, the gap from it. REO-RL: 62.9% at 5,966 tokens against vanilla RL's
64.4% at 11,282.6 — **55.9% REG reduction**, where fixed-4K RL manages 27.5%.

## 3. Count structure inside the trace

**Do NOT Think That Much for 2+3=?** (abstract) was the first to split the
quantity in two, and the split has held:

| | measures |
| --- | --- |
| **outcome efficiency** | whether extra compute changes the final answer |
| **process efficiency** | what fraction of the emitted chain is redundant |

They are independent — a verification pass changes nothing and may still not
be redundant.

The operational definitions get simpler from there, and simpler is not worse:

- **answer oscillation** (When More Thinking Hurts): count of intermediate-
  conclusion changes. Predicts negative flips at `r=0.78` alone, `r=0.82`
  combined with hesitation markers and confidence trajectory, at **76.3%
  precision / 80% recall**.
- **hesitation-marker density** (Funnel of Thoughts, document): markers per
  1,000 characters, over a 21-word lexicon chosen by benchmark-weighted
  point-biserial correlation on a 115,200-rollout profiling pool.
- **repeated local conclusion** (EvoThink, document): delete unit `u⁽ᵗ⁾` when
  its local conclusion equals `u⁽ᵗ⁻¹⁾`'s. Needs no gold answer.
- **revisiting the same options more than three times** (BiasTrace, document).
  The bluntest definition here, and the strongest behavioural predictor of
  stereotype-aligned answers on BBQ.
- **InfoBias / InfoGain** (Think or Not, abstract): divergence from an ideal
  path and diminishing information, worsening with length **especially when
  the answer is wrong**.

## 4. Read it off internal state — and the finding that matters most

**Think Deep, Not Just Long** (abstract) defines **DTR**, the fraction of
emitted tokens still being revised in the network's late layers, and ranks
signals by mean Pearson correlation with accuracy:

```
DTR              +0.683
self-certainty   +0.605
neg-entropy      +0.571
logprob          +0.527
neg-perplexity   +0.219
token length     −0.594      ← the field's default proxy
```

**Length is not a measure of overthinking.** It is the most-used stand-in in
this literature and it correlates *negatively* with accuracy. LLMThinkBench's
Phi-4 pair is the same result from the other direction, and *Do NOT Think That
Much*'s outcome/process split is a third: how much was emitted and how much
was wasted are different questions.

**ReBalance** (abstract) separates the two signs with one statistic: **high
variance in per-step confidence is the overthinking signature, consistently
high confidence the underthinking one.**

**Manifold Steering** (abstract) locates overthinking as a low-dimensional
manifold in activation space, cutting output tokens up to 71% by projecting
interventions onto it.

## 5. Ask a judge

**The Danger of Overthinking** (document, ICML 2025) scores traces 0–10 by
LLM judgement and regresses against SWE-bench resolution:

```
β1 = −7.894    R² = 0.892    p = 0.000     (reasoning models)
reasoning 3.505 ± 1.774   vs   non-reasoning 2.228 ± 0.751
function calling: score 2.43 → 1.05, o1 29.1% → 47.7%
```

R²=0.892 is among the strongest relations in the archive. **The weakness is
that the judge is the instrument** — unlike every other family here, the
number is not a reproducible computation over the trace.

## 6. Make it an allocation problem

**R³-Bench** (document) defines the **Gap Ratio**: what a model solves
problem-by-problem minus what it solves when one budget must be divided among
six. Range **0.00%–82.47%**. Oracle allocation is at least the model's own in
all 72 cells and **strictly better in 71**; at ρ=0.8, **equal allocation beats
the model's own for 4 of 6 models**.

**Think Shallow, Solve Deep** (document) reports `overthink` as a quantity
separate from accuracy — worst over difficulty tiers of (best EM − EM at
hc=128), from 0 for settling operators to 0.91 for drifting ones.

**TRACE** (abstract) truncates a chain at 10%, 20%, …, 100%, forces an answer
at each cut, and takes the **area under the reward-vs-CoT-fraction curve**.
Built to detect reward hacking — but it is the only procedure here that
produces a per-instance curve of *what the answer would have been by now*.

## What has been quantified, and what has not

**Quantified:** the cost (tokens, dollars, latency), the loss (flip ratio, EM
lost to depth, Gap Ratio), and the waste (redundant-unit fraction, hesitation
density).

**Not quantified: per-instance ground truth for how many tokens were
unnecessary in *this* response.** The budget sweep produces it — and needs 32
runs after the fact. Every real-time signal (DTR, confidence variance,
hesitation density) is validated against a different proxy, so none of them is
calibrated against the same target.

**And there is no common unit.** These are the scales in play:

| Metric | Unit | Range |
| --- | --- | --- |
| Overthinking Score | harmonic mean | [0, 1] |
| AUC_OAA / F1^otb | area, harmonic mean | [0, 100] |
| flip ratio | ratio | [0, ∞) |
| REG | area difference | unbounded |
| overthink (depth) | EM difference | [0, 1] |
| Gap Ratio | percent | 0–82.47 observed |
| DTR | fraction of tokens | [0, 1] |
| judge score | ordinal | 0–10 |

A model can rank differently under any two of these and **nothing in the
archive has checked whether it does.** OptimalThinkingBench evaluated 33
models and LLMThinkBench 53; neither reports the other's metric, and the two
model sets overlap. That is a cheap experiment nobody has run, and it is filed
as a synthesis question rather than asserted here.

## What is missing

1. **No cross-metric agreement study.** See above. Until one exists, "model X
   overthinks more than Y" is a statement about a metric, not about a model.
2. **Only one instance-level label set exists** — the 80 hand-reviewed
   negative flips in *When More Thinking Hurts*, 67.5% of them genuine. Every
   detector in family 3 and 4 should be scored against something like it and
   none is.
3. **Nothing measures the easy and hard ends on one scale.** `F1^otb` combines
   two sub-benchmarks by harmonic mean, which is a composition, not a common
   scale: an easy question's excess tokens and a hard question's missing ones
   are still counted in different units.
