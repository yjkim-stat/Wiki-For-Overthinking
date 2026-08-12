# MMLU-PRO

<!-- auto:begin -->

A harder, more reasoning-oriented revision of MMLU, used in the archive as a multiple-choice knowledge-and-reasoning benchmark outside mathematics. Both sources use it as a breadth check rather than studying it: one as a testbed for knockout and league aggregation with provable scaling guarantees, the other for local causal attribution of chain-of-thought reasoning. Its presence marks one of the archive's few non-mathematical evaluation surfaces.

- **Kind**: dataset
- **Also called**: MMLU Pro, MMLU-Pro
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [activation steering](../methods/activation-steering.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AIME24](aime24.md), [AMC23](amc23.md), [BBH](bbh.md), [best-of-n](../methods/best-of-n.md), [chain-of-thought compression](../methods/chain-of-thought-compression.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [Gemini-2.5-Flash](../models/gemini-2-5-flash.md), [generative rewriting](../methods/generative-rewriting.md), [GPQA](gpqa.md), [GPQA-Diamond](gpqa-diamond.md), [GPT-4o](../models/gpt-4o.md), [GSM8K](gsm8k.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [majority voting](../methods/majority-voting.md), [MATH-500](math-500.md), [MATH500](math500.md), [overthinking](../concepts/overthinking.md), [pass-k](../methods/pass-k.md), [Qwen2.5](../models/qwen2-5.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [QwQ-32B](../models/qwq-32b.md), [reasoning distillation](../methods/reasoning-distillation.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [reasoning skeleton](../concepts/reasoning-skeleton.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [restructuring level](../concepts/restructuring-level.md), [reward hacking](../concepts/reward-hacking.md), [self-consistency](../methods/self-consistency.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [supervised finetuning](../methods/supervised-finetuning.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](../methods/test-time-scaling.md), [verification](../concepts/verification.md), [ZebraLogic](zebralogic.md)

## Appears in

- [When Compression Helps and When It Hurts: Condition-Aware Analysis of Chain-of-Thought Distillation](../../archive/papers/2026/local-4acfffb647c2e41f/summary.md) — Runs the head-to-head this literature had been missing, comparing three importance criteria on the same traces at matched compression ratios, and finds step-level criteria agree on what to keep while disagreeing on what to cut — because redundancy is diffuse rather than located in any identifiable class of step.
- [Local Causal Attribution of Chain-of-Thought Reasoning](../../archive/papers/2026/local-6db01f05462cef8e/summary.md) — Fits a structural causal model over the units of a single chain-of-thought trace using leave-one-out interventions and linear regression, producing a pairwise influence matrix between every pair of steps at a cost linear in the number of units.
- [Provable Scaling Laws for the Test-Time Compute of Large Language Models](../../archive/papers/2025/local-e5ae26db2daac1d7/summary.md) — Gives two aggregation algorithms whose failure probability provably decays to zero as inference compute grows, assuming only that the model can sometimes be right and can compare two solutions better than chance.
- [The Tell-Tale Norm: L2 Magnitude as a Signal for Reasoning Dynamics in Large Language Models](../../archive/papers/2026/local-f92e5f936a3c7422/summary.md) — Argues that the L2 norm of a hidden state is a training-free proxy for how hard a model is reasoning at that layer and token, proves it bounds the activation of SAE-identified reasoning features, and uses norm peaks to decide where to recurse a layer, where to steer, and which sampled response to keep.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
