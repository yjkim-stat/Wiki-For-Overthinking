# Qwen3-VL-8B

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: model
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [annotation incompleteness](../concepts/annotation-incompleteness.md), [component ablation](../methods/component-ablation.md), [credit assignment](../concepts/credit-assignment.md), [distribution shift](../concepts/distribution-shift.md), [format compliance](../concepts/format-compliance.md), [GRPO](../methods/grpo.md), [hard negative mining](../methods/hard-negative-mining.md), [KL regularization](../methods/kl-regularization.md), [Llama-3-8B](llama-3-8b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [MathVista](../datasets/mathvista.md), [MMMU](../datasets/mmmu.md), [MMMU-Pro](../datasets/mmmu-pro.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [outcome reward](../concepts/outcome-reward.md), [pass@k](../concepts/pass-k.md), [process reward](../concepts/process-reward.md), [process reward model](../concepts/process-reward-model.md), [process supervision](../concepts/process-supervision.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen2.5-VL](qwen2-5-vl.md), [Qwen2.5-VL-7B](qwen2-5-vl-7b.md), [Qwen3-VL-2B](qwen3-vl-2b.md), [ReAct](../methods/react.md), [reward hacking](../concepts/reward-hacking.md), [reward shaping](../concepts/reward-shaping.md), [RLVR](../methods/rlvr.md), [self-correction](../concepts/self-correction.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [Vicuna-7B](vicuna-7b.md)

## Appears in

- [VTO: Visual Tool Orchestration for Video Anomaly Detection](../../archive/papers/2026/arxiv-2608-08219/summary.md) — Trains a multimodal agent to orchestrate twelve video-analysis tools for anomaly detection with GRPO under a dual reward that combines exact-match rule checks with an LLM judge scoring logicality, relevance and completeness, and releases the benchmark it is evaluated on.
- [StructReward: Efficient Structured Process Rewards for Self-Correcting Multimodal Reasoning](../../archive/papers/2026/arxiv-2608-08326/summary.md) — Builds a dense process reward without a learned verifier or an online judge, by aligning generated reasoning steps to the process-labelled reference steps that existing datasets already contain using numerical, symbolic and lexical matching rules, gated so a partial reference match cannot override a wrong final answer.
- [Improving Generalization Robustness of Multimodal RLVR](../../archive/papers/2026/arxiv-2608-08802/summary.md) — Traces the brittleness of multimodal RLVR gains under paraphrase and template change to two properties of the standard objective -- a binary verifier that cannot distinguish a wrong answer from a misformatted one, and a training distribution covering a thin slice of the prompts a deployed model meets -- and fixes both with a trinary reward and an invariance penalty across semantically equivalent prompts.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
