# judge reliability

<!-- auto:begin -->

Whether a model judge gives the same verdict twice, and across 3 sources a property the archive keeps separate from whether the verdict is right. The instances that matter: test-retest reliability as high as 0.992 coexisting with the most severe position bias in a cohort and the third-lowest agreement with human judgements, so consistency and validity come apart and a reliable judge can be reliably wrong; a scoring bias in which judges produce characteristic scores regardless of the text, addressed in one source by random-number-based debiasing; and spending more compute on judging as a way to improve it. The archive's related material adds the reason reliability alone is insufficient -- a judge drawn from the same family as a system it scores is not independent, and validating a judge against annotators using its own criteria does not establish that it is.

- **Kind**: concept
- **Also called**: evaluator reliability, judge bias, judge consistency, scoring bias
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [annotation agreement](annotation-agreement.md), [benchmark contamination](benchmark-contamination.md), [best-of-n](../methods/best-of-n.md), [calibration](calibration.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [compute allocation](compute-allocation.md), [DAPO](../methods/dapo.md), [DAPO-Qwen-32B](../models/dapo-qwen-32b.md), [DeepSeek-R1-0528-Qwen3-8B](../models/deepseek-r1-0528-qwen3-8b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [GRPO](../methods/grpo.md), [LiveCodeBench](../datasets/livecodebench.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH500](../datasets/math500.md), [meta-evaluation](meta-evaluation.md), [Minerva](../datasets/minerva.md), [pass@k](pass-k.md), [position bias](position-bias.md), [process evaluation](process-evaluation.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [reasoning boundary](reasoning-boundary.md), [reranking](../methods/reranking.md), [RLVR](../methods/rlvr.md), [Skywork-OR1](../models/skywork-or1.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time compute](test-time-compute.md), [test-time scaling](test-time-scaling.md), [training dynamics](training-dynamics.md), [verification](verification.md)

## Appears in

- [Mitigating Scoring Bias in LLM-as-a-Judge via Random Number Generation](../../archive/papers/2026/arxiv-2608-05726/summary.md) — Measures an LLM judge's latent number bias by asking it to emit random numbers, then rectifies its scoring token probabilities against that measured bias.
- [Scaling Evaluation-Time Compute with Reasoning Models as Evaluators](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2102/summary.md) — Shows evaluator accuracy improves monotonically with reasoning tokens spent, and that buying compute at evaluation time can substitute for buying it at generation time.
- [Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs](../../archive/papers/2025/local-fb100130d8c7c2bd/summary.md) — Shows that base models win pass@K on mathematics by producing wrong chains that land on right answers, and that scoring the chain too — CoT-Pass@K — reverses the verdict in RLVR's favour at every K.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
