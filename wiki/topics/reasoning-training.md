# Reasoning Training

<!-- auto:begin -->

How a language model acquires long-form reasoning: reinforcement learning against verifiable rewards, process versus outcome supervision, distillation of reasoning traces, and self-training. The question the archive answers is which training signal produces reasoning that generalizes, and what each one costs.

- **Slug**: `reasoning-training`
- **Papers**: 120
- **Seminars**: 0
- **Tracked keywords**: `large reasoning model`, `reasoning model`, `reasoning capability`, `reasoning ability`, `chain of thought`, `verifiable reward`, `RLVR`, `process reward model`, `outcome reward`, `process supervision`, `reasoning distillation`, `chain of thought distillation`, `GRPO`, `long chain of thought`, `self-taught reasoner`

## Most recent papers

- [DASH: Divergence-Adaptive Supervision Horizons for On-Policy Self-Distillation of Reasoning Models](../../archive/papers/2026/arxiv-2608-06243/summary.md) (2026-08-06)
  - Weights on-policy self-distillation supervision by how each local teacher-student divergence compares to the sequence mean, gating backward multi-step aggregation on that comparison.
- [LC-GRPO: Bridging Train-Inference Gap for Flow-Based GRPO with Langevin Correction](../../archive/papers/2026/arxiv-2608-05600/summary.md) (2026-08-06)
  - A GRPO variant for flow-based generative models that replaces SDE training rollouts with an ODE step plus a Langevin correction, aligning training samples with the deterministic sampler used at test time.
- [AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning](../../archive/papers/2026/arxiv-2608-05987/summary.md) (2026-08-06)
  - Turns token-level teacher-student log-probability gaps into turn-level credit for agentic RL by recursively updating a Bayesian belief in log-odds space, identifying pivotal turns without a critic.
- [RP-OPSD: Reasoning-Pivot-Guided On-Policy Self-Distillation for Multilingual Reasoning Transfer](../../archive/papers/2026/arxiv-2608-06347/summary.md) (2026-08-06)
  - Concentrates privileged self-distillation on reasoning pivots identified by the teacher's distributional shift when an English reference solution is added or removed, for multilingual reasoning transfer.
- [Evaluating Theory of Mind in Reasoning Models: Robustness over Reasoning](../../archive/papers/2026/arxiv-2608-04646/summary.md) (2026-08-05)
  - Tests reasoning models on Theory of Mind tasks and argues their gains are increased robustness to prompt and task perturbation rather than a new ToM-specific ability.
- [Easy to Complete, Hard to Choose: Investigating LLM Performance on the ProverbIT Benchmark](../../archive/papers/2026/arxiv-2608-04670/summary.md) (2026-08-05)
  - An Italian proverb benchmark on which models complete proverbs successfully but fail multiple-choice selection when no correct option is present, with CoT analysis showing they name the right ending while failing to notice its absence.
- [Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning](../../archive/papers/2026/arxiv-2608-04771/summary.md) (2026-08-05)
  - Couples KV-cache compression and generation-length control under a single process-reward signal, compressing harder at high-reward reasoning steps and stopping early when confidence is high.
- [Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings](../../archive/papers/2026/arxiv-2608-04735/summary.md) (2026-08-05)
  - The first benchmark comparing CoT monitorability under explicit versus implicit influence, finding detection falls 41-46 points when the prompt never instructs the model to hide anything.
- [Trident : How to Break Deep Reinforcement Learning Cyber Defenses (Agentic)](../../archive/papers/2026/arxiv-2608-04317/summary.md) (2026-08-05)
  - An agentic RLVR red-teaming framework that trains an LLM planner to attack deep-RL cyber-defence agents, showing those defences were only ever evaluated against static attackers.
- [ODRA: Synthesizing Cognitive Behavioral Therapy Sessions with Structured Chain-Of-Thought and Dynamic Patient Resistance](../../archive/papers/2026/arxiv-2608-04524/summary.md) (2026-08-05)
  - Synthesizes Cognitive Behavioral Therapy dialogues using a CoT strategy grounded in CBT guidelines plus a resistance orchestrator that steers simulated patients away from sycophantic compliance.
- [Teaching MLLMs to Say No: Generalized Referring Expression Comprehension via Refusal Calibrated GRPO](../../archive/papers/2026/arxiv-2608-04698/summary.md) (2026-08-05)
  - A GRPO variant that teaches multimodal models to refuse when a referred object is absent, without losing localization accuracy on cases where it is present.
- [SpecRoll: Fast-Slow Verifier-Feedback Adaptation for Speculative Reinforcement Learning Rollouts](../../archive/papers/2026/arxiv-2608-04962/summary.md) (2026-08-05)
  - A speculative-decoding rollout engine for RL post-training that keeps the target sampling distribution exact while adapting the drafter at two timescales.
- [Don't Peek at the Answer: Outcome-Masked Group Relative Policy Optimization for Label-Free RLVR](../../archive/papers/2026/arxiv-2608-03119/summary.md) (2026-08-04)
- [When Correct Solutions Repeat: Rarity-Aware Credit Redistribution for GRPO](../../archive/papers/2026/arxiv-2608-03467/summary.md) (2026-08-04)
- [PAMT: Process-Aligned Reinforcement Learning for Multi-Domain Machine Translation](../../archive/papers/2026/arxiv-2608-03077/summary.md) (2026-08-04)
- [The Tell-Tale Trace: Detecting Reasoning Failures in LLMs Using Chain-of-Thought Dynamics](../../archive/papers/2026/arxiv-2608-03291/summary.md) (2026-08-04)
- [Risky Business: Measuring The Faithfulness-Safety Tension](../../archive/papers/2026/arxiv-2608-03745/summary.md) (2026-08-04)
- [TQLite: Multi-LLM Jury Guided Distillation for Real-time MQM Translation Quality Evaluation](../../archive/papers/2026/arxiv-2608-02975/summary.md) (2026-08-04)
- [DocTrace: Towards Traceable Long Document VQA via Hierarchical Evidence Graph Reasoning](../../archive/papers/2026/arxiv-2608-03292/summary.md) (2026-08-04)
- [Soft Guidance Starts to Outperform CoT Prompting as LLMs Improve](../../archive/papers/2026/arxiv-2608-03550/summary.md) (2026-08-04)
- [Evading Chain-of-Thought Monitoring Through Model Poisoning](../../archive/papers/2026/arxiv-2608-02820/summary.md) (2026-08-03)
- [BODHI: Do LLMs Branch Out and Discover Heterogeneous Inferences?](../../archive/papers/2026/arxiv-2608-02867/summary.md) (2026-08-03)
- [Does Accuracy Equal Evidence? Reasoning Faithfulness under KV Cache Compression](../../archive/papers/2026/arxiv-2608-01631/summary.md) (2026-08-03)
  - Replays one fixed reasoning trace through eleven KV cache compression methods and finds that the ones preserving final-answer accuracy are largely the ones destroying the reasoning that supports it — on AIME the accuracy ranking of compressors correlates with their chain-validity ranking at Spearman -0.95.
- [Start Classifying: Categorical Critics for LLM Reinforcement Learning](../../archive/papers/2026/arxiv-2608-02181/summary.md) (2026-08-03)
- [CURV: Enhancing Chart Understanding Through Curriculum Visual Grounded Reasoning](../../archive/papers/2026/arxiv-2608-02833/summary.md) (2026-08-03)

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
