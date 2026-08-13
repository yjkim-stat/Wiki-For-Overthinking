# reward shaping

<!-- auto:begin -->

Designing the reward's structure — what it attaches to, and when — rather than only its target, which all four sources treat as where efficiency methods succeed or fail. One confines an efficiency reward to a single mode-selection token after diagnosing that a sequence-level efficiency signal implicitly penalizes long but correct trajectories. One pairs a length reward with a compress reward aimed specifically at double-checking that occurs after the answer is already derived. One forces 'None' rollouts so negative samples produce a valid advantage, and penalizes over-refusal on positives. One scales the reward by problem difficulty. The shared lesson is that a reward correct in aggregate can be wrong per token or per group.

- **Kind**: concept
- **Also called**: reward design, reward engineering
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 5

**Related**: [abstention](abstention.md), [adaptive compute allocation](adaptive-compute-allocation.md), [advantage estimation](advantage-estimation.md), [AIME 2024](../datasets/aime-2024.md), [answer stabilization](answer-stabilization.md), [credit assignment](credit-assignment.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-V3](../models/deepseek-v3.md), [GEMBA-MQM](../methods/gemba-mqm.md), [Gemini-2.0-flash](../models/gemini-2-0-flash.md), [GPT-4o](../models/gpt-4o.md), [GPT-5](../models/gpt-5.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [hallucination](hallucination.md), [KL regularization](../methods/kl-regularization.md), [length control](../methods/length-control.md), [long chain-of-thought distillation](../methods/long-chain-of-thought-distillation.md), [majority voting](../methods/majority-voting.md), [MATH500](../datasets/math500.md), [OlympiadBench](../datasets/olympiadbench.md), [outcome reward](outcome-reward.md), [overthinking](overthinking.md), [Pareto frontier](pareto-frontier.md), [process reward](process-reward.md), [prompt difficulty](prompt-difficulty.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [reasoning drift](reasoning-drift.md), [reasoning redundancy](reasoning-redundancy.md), [reinforcement learning post-training](../methods/reinforcement-learning-post-training.md), [RLVR](../methods/rlvr.md), [self-correction](self-correction.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [teacher forcing](../methods/teacher-forcing.md), [WMT22](../datasets/wmt22.md)

## What we have settled

- **Established** — Dense process reward works only as a modifier on an outcome signal, never as a replacement: across every paper measuring it, removing the terminal reward is the largest single ablation loss, and pushing the process weight too high drives performance below the baseline it was meant to improve.
  - Three independent instances in three domains. In search-agent training, removing the terminal outcome reward costs 6.3 F1 — larger than removing either dense per-step signal — and is the only ablation that degrades every benchmark; the process weight sweep peaks at 0.25 and collapses to 44.8 at 1.00, below several baselines. In multi-domain translation, removing the sequence-level quality reward is likewise the largest degradation (in-domain BLEU 29.83 to 22.94), well ahead of removing the process reward or its token-level distribution. In audio reasoning, accuracy declines past a rubric weight of 0.5 because the policy optimizes for satisfying criteria rather than for being right, and a length penalty had to be added because more criteria are satisfied by longer traces. A fourth design makes the constraint explicit rather than empirical: bounding a privileged-teacher correction by the magnitude of the outcome advantage means it can never flip a sign or create an update where the outcome reward is silent. The practical reading is that a process signal refines the distribution of credit along a trajectory and cannot supply its direction.

## Appears in

- [PAMT: Process-Aligned Reinforcement Learning for Multi-Domain Machine Translation](../../archive/papers/2026/arxiv-2608-03077/summary.md) — Scores each reasoning step of a translation by how much appending it raises a frozen reference model's teacher-forced likelihood of the gold translation, and adds that as a dense per-step reward on top of sequence-level quality — after first establishing that explicit reasoning helps long and hard inputs while drifting on terminology and style.
- [Teaching MLLMs to Say No: Generalized Referring Expression Comprehension via Refusal Calibrated GRPO](../../archive/papers/2026/arxiv-2608-04698/summary.md) — A GRPO variant that teaches multimodal models to refuse when a referred object is absent, without losing localization accuracy on cases where it is present.
- [Optimizing Length Compression in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-146/summary.md) — Identifies double-checking after the correct answer is already derived as 'invalid thinking', and trains a GRPO variant with a compress reward that targets exactly that portion.
- [ADaPT: Token-Level Decoupling for Efficient Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-165/summary.md) — Attributes efficiency-training damage to sequence-level coupling between efficiency and correctness rewards, and decouples them by applying the efficiency reward only to a single mode-selection token.
- [The Overthinker's DIET: Cutting Token Calories with DIfficulty-AwarE Training](../../archive/papers/2025/local-5feb5d3d92da16e0/summary.md) — Trains reasoning models to be concise in proportion to difficulty by modulating the token penalty and the target length per problem, and fixes a distortion that naive reward weighting introduces into group-normalized RL.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
