# MATH-500

<!-- auto:begin -->

A 500-problem subset of the MATH benchmark, and the archive's most common mid-difficulty mathematics reference — easy enough that strong base models solve most of it with sufficient attempts, which is exactly what makes it informative. One source uses it to validate provable test-time scaling; another reports that RLVR's effect on it is muted precisely because the base model already reaches the answers given enough samples, so the benchmark cannot show an extended boundary. That saturation is the thing to know before quoting a MATH-500 number.

- **Kind**: dataset
- **Also called**: MATH-500 subset, MATH500
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AMC23](amc23.md), [benchmark contamination](../concepts/benchmark-contamination.md), [best-of-n](../methods/best-of-n.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [DAPO](../methods/dapo.md), [DAPO-Qwen-32B](../models/dapo-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [GPQA](gpqa.md), [GPT-4o](../models/gpt-4o.md), [GRPO](../methods/grpo.md), [judge reliability](../concepts/judge-reliability.md), [LiveCodeBench](livecodebench.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [majority voting](../methods/majority-voting.md), [Minerva](minerva.md), [MMLU-PRO](mmlu-pro.md), [pass-k](../methods/pass-k.md), [process evaluation](../methods/process-evaluation.md), [Qwen2.5](../models/qwen2-5.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [QwQ-32B](../models/qwq-32b.md), [reasoning boundary](../concepts/reasoning-boundary.md), [reward hacking](../concepts/reward-hacking.md), [RLVR](../methods/rlvr.md), [self-consistency](../methods/self-consistency.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](../methods/test-time-scaling.md), [training dynamics](../concepts/training-dynamics.md), [verification](../concepts/verification.md)

## Appears in

- [Provable Scaling Laws for the Test-Time Compute of Large Language Models](../../archive/papers/2025/local-e5ae26db2daac1d7/summary.md) — Gives two aggregation algorithms whose failure probability provably decays to zero as inference compute grows, assuming only that the model can sometimes be right and can compare two solutions better than chance.
- [Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs](../../archive/papers/2025/local-fb100130d8c7c2bd/summary.md) — Shows that base models win pass@K on mathematics by producing wrong chains that land on right answers, and that scoring the chain too — CoT-Pass@K — reverses the verdict in RLVR's favour at every K.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
