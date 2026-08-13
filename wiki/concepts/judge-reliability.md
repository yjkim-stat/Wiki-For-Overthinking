# judge reliability

<!-- auto:begin -->

Whether a model used to score other models' output can be trusted, which matters because judges are how reasoning work gets evaluated once the answer is not a checkable string. One source isolates a content-independent component of judge behaviour by asking the model to emit random numbers, treating deviation from uniform as its latent bias, and rectifies scoring probabilities against it — finding bias varies across models, tasks and score ranges. The other shows judging improves monotonically with reasoning tokens spent, so evaluation compute buys accuracy the way generation compute does, at a comparable exchange rate. A third archived source finds judge preference scores track style rather than substance.

- **Kind**: concept
- **Also called**: evaluator reliability, judge bias, scoring bias
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [benchmark contamination](benchmark-contamination.md), [best-of-n](../methods/best-of-n.md), [calibration](../methods/calibration.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [DAPO](../methods/dapo.md), [DAPO-Qwen-32B](../models/dapo-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [GRPO](../methods/grpo.md), [LiveCodeBench](../datasets/livecodebench.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH-500](../datasets/math-500.md), [meta-evaluation](meta-evaluation.md), [Minerva](../datasets/minerva.md), [pass@k](../methods/pass-k.md), [process evaluation](../methods/process-evaluation.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [reasoning boundary](reasoning-boundary.md), [RLVR](../methods/rlvr.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time compute](test-time-compute.md), [test-time scaling](../methods/test-time-scaling.md), [training dynamics](training-dynamics.md), [verification](verification.md)

## Appears in

- [Mitigating Scoring Bias in LLM-as-a-Judge via Random Number Generation](../../archive/papers/2026/arxiv-2608-05726/summary.md) — Measures an LLM judge's latent number bias by asking it to emit random numbers, then rectifies its scoring token probabilities against that measured bias.
- [Scaling Evaluation-Time Compute with Reasoning Models as Evaluators](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2102/summary.md) — Shows evaluator accuracy improves monotonically with reasoning tokens spent, and that buying compute at evaluation time can substitute for buying it at generation time.
- [Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs](../../archive/papers/2025/local-fb100130d8c7c2bd/summary.md) — Shows that base models win pass@K on mathematics by producing wrong chains that land on right answers, and that scoring the chain too — CoT-Pass@K — reverses the verdict in RLVR's favour at every K.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
