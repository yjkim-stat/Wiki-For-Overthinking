# Reasoning Training

<!-- auto:begin -->

How a language model acquires long-form reasoning: reinforcement learning against verifiable rewards, process versus outcome supervision, distillation of reasoning traces, and self-training. The question the archive answers is which training signal produces reasoning that generalizes, and what each one costs.

- **Slug**: `reasoning-training`
- **Papers**: 152
- **Seminars**: 0
- **Tracked keywords**: `large reasoning model`, `reasoning model`, `reasoning capability`, `reasoning ability`, `chain of thought`, `verifiable reward`, `RLVR`, `process reward model`, `outcome reward`, `process supervision`, `reasoning distillation`, `chain of thought distillation`, `GRPO`, `long chain of thought`, `self-taught reasoner`

## Most recent papers

- [Chain-of-Thought Shows the Path to a Tree: Realizing Branching Complexity](../../archive/papers/2026/arxiv-2608-11716/summary.md) (2026-08-12)
- [GRPO for Financial Advice Generation: Outperforming Commercial LLMs under CATE Evaluation](../../archive/papers/2026/arxiv-2608-11787/summary.md) (2026-08-12)
  - Trains an open-weight model with GRPO against a safety-gated LLM-as-a-judge rubric for financial advice, then audits the result with a judge-independent causal estimator on logged outcomes -- and finds the two evaluations rank the other systems differently, with the untrained base model last on the rubric and second on the audit.
- [SCOUT: Unlocking Enhanced Spatial Reasoning via Structured Chain-of-Thought and Multi-Objective Process Reward](../../archive/papers/2026/arxiv-2608-12220/summary.md) (2026-08-12)
  - Splits a spatial-reasoning chain of thought into explicitly typed segments -- perception, including depth, and reasoning -- and gives each its own process reward and its own advantage term, so that the two do not compete for credit under a single outcome signal.
- [LEMUR: Latent Entropy-aware Multimodal Unlearning via Visual-anchored Reasoning Redirection](../../archive/papers/2026/arxiv-2608-11691/summary.md) (2026-08-12)
  - Finds that a fact successfully unlearned from a multimodal model's final answer can still be reproduced in its reasoning trace, far more in natively RL-trained models than in their base versions, and uses the token-level entropy signature RL leaves behind as a training-free control signal for redirecting the trace at decoding time.
- [When the API Speaks the Wrong Language: Revisiting Post-Training for Multilingual Tool Use](../../archive/papers/2026/arxiv-2608-11715/summary.md) (2026-08-12)
- [PAIR: Pairwise-Aware Inclusion Reweighting for Adaptive Rollout Allocation in RLVR](../../archive/papers/2026/arxiv-2608-11368/summary.md) (2026-08-11)
- [FaithformBench: Benchmarking Faithfulness of Mathematical Chain-of-Thought Autoformalisation](../../archive/papers/2026/arxiv-2608-10916/summary.md) (2026-08-11)
  - Tests whether systems that translate natural-language reasoning steps into Lean preserve invalidity as well as validity, by automatically perturbing steps to make them wrong, and finds pervasive silent correction -- with the systems best at preserving valid inputs the most likely to repair invalid ones.
- [ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling](../../archive/papers/2026/arxiv-2608-10928/summary.md) (2026-08-11)
  - Injects a retrieved solved problem, with its full worked solution, into the middle of a reasoning model's own thinking trace at each step boundary, using the model's current intermediate answer as the retrieval query.
- [XCoT-VLA: Executable Chain-of-Thought for Vision-Language-Action Driving](../../archive/papers/2026/arxiv-2608-10976/summary.md) (2026-08-11)
- [Social Chain of Thought: A Multi-Agent Architecture Grounded in Medical Differential Diagnosis Methodology](../../archive/papers/2026/arxiv-2608-11420/summary.md) (2026-08-11)
  - Structures multi-agent medical differential diagnosis as rounds of persona-conditioned specialist deliberation, and shows the recall advantage is not reproduced by best-of-n sampling from the same model, concentrates entirely in the cases where monolithic inference fails, and reverses on the easiest quartile.
- [CARE: Confidence-Aware Reasoning for Reliable Medical VQA](../../archive/papers/2026/arxiv-2608-10964/summary.md) (2026-08-11)
- [ConRub-Med: Reinforcement Learning with Consensus Rubrics for Open-Ended Medical Question Answering](../../archive/papers/2026/arxiv-2608-10996/summary.md) (2026-08-11)
- [Scheduling Mixed RL Rollouts Beyond Prefix Locality](../../archive/papers/2026/arxiv-2608-11152/summary.md) (2026-08-11)
- [Parameter Exploration for RLVR via Variational Learning](../../archive/papers/2026/arxiv-2608-09805/summary.md) (2026-08-10)
  - Explores in weight space rather than token space during RLVR by sampling policies from a variational posterior at rollout time, and introduces a training-time exploration metric -- how often a method produces a correct rollout on a prompt where GRPO produced none -- because entropy and pass@k cannot tell exploration from degeneration.
- [REATS: LLM Reasoning-based Ensemble Learning for Adaptive Time Series Forecasting](../../archive/papers/2026/arxiv-2608-10149/summary.md) (2026-08-10)
- [SoftmaxGRPO: Learning to Reason using Softmax Advantage Group Estimation](../../archive/papers/2026/arxiv-2608-09271/summary.md) (2026-08-10)
- [Dual-Adversarial Safety Alignment: Cultivating Intrinsic Threat Comprehension in LRMs](../../archive/papers/2026/arxiv-2608-09542/summary.md) (2026-08-10)
- [Distill Skills into Weights, Not Prompts: Abstract Skills as Privileged Signals for On-Policy Self-Distillation](../../archive/papers/2026/arxiv-2608-09826/summary.md) (2026-08-10)
- [Improving Generalization Robustness of Multimodal RLVR](../../archive/papers/2026/arxiv-2608-08802/summary.md) (2026-08-09)
- [MathShikkha: A Controlled Study of Answer-Only and Chain-of-Thought Supervision for Bangla Mathematical Reasoning in Small Language Models](../../archive/papers/2026/arxiv-2608-08503/summary.md) (2026-08-09)
  - Compares chain-of-thought against answer-only supervision under a protocol where the two conditions differ in nothing but the training target, and finds the rationales buy nothing in-domain for strong backbones while buying 20 to 28 points out of domain -- with a human study attributing the measurable effect to language adherence and inspectability rather than to better reasoning.
- [LLM Reasoning for Subjective Tasks: Failure Modes, Mitigation, and Dynamic Reasoning Routing](../../archive/papers/2026/arxiv-2608-08889/summary.md) (2026-08-09)
  - Shows on four internal Netflix verification tasks that explicit reasoning usually degrades subjective judgement, that applying RLVR to fix it makes the policy abandon deliberation for short heuristic guessing, and that a length bonus gated on answer correctness is what stops the collapse.
- [MedCalc-R1: Knowledge-Guided Reward Framework for Medical Mathematical Reasoning](../../archive/papers/2026/arxiv-2608-08623/summary.md) (2026-08-09)
- [SkillReason: Reasoning-Enhanced Agent Skill Retrieval for Implicit User Requests](../../archive/papers/2026/arxiv-2608-08640/summary.md) (2026-08-09)
  - Uses chain-of-thought about required capabilities as training-time supervision for a skill retriever -- distilled from a teacher in stage one and refined by retrieval-rewarded GRPO in stage two -- so that at inference the model encodes the bare query with no generation at all.
- [StructReward: Efficient Structured Process Rewards for Self-Correcting Multimodal Reasoning](../../archive/papers/2026/arxiv-2608-08326/summary.md) (2026-08-08)
  - Builds a dense process reward without a learned verifier or an online judge, by aligning generated reasoning steps to the process-labelled reference steps that existing datasets already contain using numerical, symbolic and lexical matching rules, gated so a partial reference match cannot override a wrong final answer.
- [REIN: Bridging the Gap between Reasoning and Reliability via Reflection and Abstention Alignment](../../archive/papers/2026/arxiv-2608-07931/summary.md) (2026-08-08)

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
