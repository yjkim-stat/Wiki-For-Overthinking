# AIME 24

<!-- auto:begin -->

The 2024 American Invitational Mathematics Examination problems, used as a small, hard, automatically checkable math benchmark. The sources use it for selection and token-attribution experiments rather than to characterize the benchmark: one reports accuracy rising from 56.7% under majority@64 to 70.0% under a hidden-state verifier at top-maj@16, the other restricts RLVR gradient updates to the highest-entropy 20% of tokens. Its size is the caveat the archive attaches to it — 30 problems means a single item is worth over three percentage points, and one archived source shows AIME'24 accuracy shifting by up to 9 percentage points from GPU type, GPU count or batch size alone.

- **Kind**: dataset
- **Also called**: AIME 2024, AIME'24
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [activation probing](../methods/activation-probing.md), [AIME 25](aime-25.md), [answer stabilization](../concepts/answer-stabilization.md), [best-of-n](../methods/best-of-n.md), [calibration](../methods/calibration.md), [clip-higher](../methods/clip-higher.md), [credit assignment](../concepts/credit-assignment.md), [DAPO](../methods/dapo.md), [DAPO-Math-17K](dapo-math-17k.md), [entropy bonus](../concepts/entropy-bonus.md), [GPQA](gpqa.md), [GRPO](../methods/grpo.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [majority voting](../methods/majority-voting.md), [MATH500](math500.md), [Minerva](minerva.md), [OlympiadBench](olympiadbench.md), [pass-k](../methods/pass-k.md), [policy gradient masking](../methods/policy-gradient-masking.md), [PPO](../methods/ppo.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [residual stream](../concepts/residual-stream.md), [RLVR](../methods/rlvr.md), [token-level entropy](../concepts/token-level-entropy.md), [verification](../concepts/verification.md), [VeRL](../methods/verl.md)

## Appears in

- [Your Reasoning Model is Secretly a Reward Model - Optimization-Free Verification from Experience](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-788/summary.md) — Verifies correctness without training by comparing a reasoning trace's start-to-end hidden-state delta against two class centroids built from labelled experience.
- [Beyond the 80/20 Rule: High-Entropy Minority Tokens Drive Effective Reinforcement Learning for LLM Reasoning](../../archive/papers/2025/local-7d5e3edea2d46b92/summary.md) — Shows that the roughly 20% of CoT tokens with the highest entropy act as decision forks, and that restricting RLVR policy-gradient updates to only those tokens matches or beats full-gradient training, with the advantage growing with model size.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
