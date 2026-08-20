# annotation incompleteness

<!-- auto:begin -->

A reference annotation covering less than the space of correct answers, so a system is penalised for being different rather than wrong. Across 3 sources it is the standing limitation of reusing existing labels as supervision: a process reward computed as agreement with one validated derivation penalises a rollout that reaches the verified answer through intermediate quantities absent from that reference, and a retrieval benchmark whose targets are model-selected treats an unlisted but adequate skill as a miss. One source states the coverage consequence explicitly -- the method is available only where such annotations already exist, which is the resource its own premise says others pay to create. The archive's practical note is that where annotation incompleteness is suspected, the useful control is an answer-distinct or alternative-derivation check rather than a looser threshold.

- **Kind**: concept
- **Also called**: sparse annotation, under-annotation
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [ablation](../methods/ablation.md), [activation steering](../methods/activation-steering.md), [advantage estimation](advantage-estimation.md), [annotation agreement](annotation-agreement.md), [benchmark design](benchmark-design.md), [causal intervention](../methods/causal-intervention.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Claude Haiku 4.5](../models/claude-haiku-4-5.md), [component ablation](../methods/component-ablation.md), [credit assignment](credit-assignment.md), [DeepSeek-R1](../models/deepseek-r1.md), [dense retrieval](../methods/dense-retrieval.md), [detection versus control](detection-versus-control.md), [gpt-5.6-luna](../models/gpt-5-6-luna.md), [GRPO](../methods/grpo.md), [hard negative mining](../methods/hard-negative-mining.md), [knowledge distillation](../methods/knowledge-distillation.md), [latent reasoning](latent-reasoning.md), [linear probe](../methods/linear-probe.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MathVista](../datasets/mathvista.md), [MMMU](../datasets/mmmu.md), [MMMU-Pro](../datasets/mmmu-pro.md), [outcome reward](outcome-reward.md), [privileged information](privileged-information.md), [process reward](process-reward.md), [process reward model](process-reward-model.md), [Qwen3-235B-A22B](../models/qwen3-235b-a22b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-VL-2B](../models/qwen3-vl-2b.md), [Qwen3-VL-8B](../models/qwen3-vl-8b.md), [representation versus readout](representation-versus-readout.md), [reranking](../methods/reranking.md), [residual stream](residual-stream.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [reward shaping](../methods/reward-shaping.md), [RLVR](../methods/rlvr.md), [selectivity control](../methods/selectivity-control.md), [self-correction](self-correction.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [sparse dictionary learning](../methods/sparse-dictionary-learning.md), [steering vector](../methods/steering-vector.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md)

## Appears in

- [StructReward: Efficient Structured Process Rewards for Self-Correcting Multimodal Reasoning](../../archive/papers/2026/arxiv-2608-08326/summary.md) — Builds a dense process reward without a learned verifier or an online judge, by aligning generated reasoning steps to the process-labelled reference steps that existing datasets already contain using numerical, symbolic and lexical matching rules, gated so a partial reference match cannot override a wrong final answer.
- [SkillReason: Reasoning-Enhanced Agent Skill Retrieval for Implicit User Requests](../../archive/papers/2026/arxiv-2608-08640/summary.md) — Uses chain-of-thought about required capabilities as training-time supervision for a skill retriever -- distilled from a teacher in stage one and refined by retrieval-rewarded GRPO in stage two -- so that at inference the model encodes the bare query with no generation at all.
- [Probing and steering biology across Boltz-1s trunk-diffusion boundary](../../archive/papers/2026/arxiv-2608-11475/summary.md) — Probes and steers across the trunk-to-diffusion boundary of an AlphaFold3-class structure predictor, finding that geometry survives the crossing while sequence chemistry is attenuated, and that a strand direction predictive at F1 0.82 steers nothing at all -- with an architectural explanation for why.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
