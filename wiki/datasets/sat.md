# SAT

<!-- auto:begin -->

SAT is referenced as a benchmark/task in ReCo (which uses a 30M process-reward estimator to set per-step KV-cache retention and generation controls for efficient reasoning) and RECAP (mitigating general-capability forgetting caused by RLVR-based reasoning fine-tuning in vision-language models).

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AI2D](ai2d.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [ChartQA](chartqa.md), [Confidence-based early stopping](../methods/confidence-based-early-stopping.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [Dynasor](../methods/dynasor.md), [GPQA](gpqa.md), [GSM8K](gsm8k.md), [KV-cache compression](../methods/kv-cache-compression.md), [LISA](lisa.md), [MATH500](math500.md), [MathVerse](mathverse.md), [MathVision](mathvision.md), [MathVista](mathvista.md), [MMMU](mmmu.md), [MMMU-Pro](mmmu-pro.md), [Overthinking](../concepts/overthinking.md), [process reward model](../methods/process-reward-model.md), [Qwen2.5-VL-3B](../models/qwen2-5-vl-3b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [Qwen3-8B](../models/qwen3-8b.md), [R-KV](../methods/r-kv.md), [ScienceQA](scienceqa.md), [Uniform sampling baseline](../methods/uniform-sampling-baseline.md), [VizWiz](vizwiz.md)

## Appears in

- [Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning](../../archive/papers/2026/arxiv-2608-04771/summary.md) — ReCo uses a 30M process-reward estimator to set, per reasoning step, both the KV-cache retention ratio and generation-side controls (a reflection-token logit penalty and confidence-based early stopping), cutting generated tokens by 37-65% and end-to-end latency by 2.08-2.35x versus full-cache CoT.
- [Beyond Reasoning Gains: Mitigating General-Capability Forgetting in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1717/summary.md) — RECAP mitigates the general-capability forgetting (perception, grounding, safety) that RLVR-based reasoning fine-tuning causes in vision-language models, by replaying general-domain data alongside the reasoning objective and dynamically reweighting each objective's loss based on its recent convergence rate and instability -- an entropy-regularized priority allocation that provably reduces to a closed-form softmax -- preserving or improving general capabilities while matching or exceeding reasoning-only fine-tuning's math/reasoning performance, and, as a side effect, producing shorter, more concise reasoning rationales without compromising reasoning ability.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
