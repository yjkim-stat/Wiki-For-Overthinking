# MathVista

<!-- auto:begin -->

A vision-language mathematics benchmark, and the one multimodal set in this archive on which reasoning length is actually measured rather than only accuracy. Heima, which replaces each reasoning stage with a single latent token, emits 13.8 tokens per MathVista answer against 216.3 for its LLaVA-CoT baseline - about 6% - at a cost of 3.1 accuracy points on its six-benchmark average, which the archive reads as an honest price for the extreme of compression. ARES shortens MathVista traces by about 19% against its own cold-start model, next to about 22% on GSM8K and about 38% longer on AIME25, so the easy-set pattern holds here too; Mixture-of-Visual-Thoughts reports accuracy only (AdaVaR-3B 69.8% against 62.3% for Qwen2.5-VL-3B) and vStream uses it as one of three maths-category sets for measuring visual-attribution faithfulness, not reasoning cost. Three of its four sources reached the archive through vocabulary shared with the topic rather than through its subject; MathVista is the entity where that overlap still yielded usable length evidence.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [Ada-GRPO](../methods/ada-grpo.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AI2D](ai2d.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [ARES](../methods/ares.md), [BBEH](bbeh.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [Difficulty-aware compute allocation](../concepts/difficulty-aware-compute-allocation.md), [GPQA](gpqa.md), [GQA](gqa.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [Latent reasoning](../concepts/latent-reasoning.md), [LLaMA-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [LLaVA-CoT](../models/llava-cot.md), [MATH500](math500.md), [MathVerse](mathverse.md), [MathVision](mathvision.md), [MMLU-Pro](mmlu-pro.md), [MMMU](mmmu.md), [MMStar](mmstar.md), [OlympiadBench](olympiadbench.md), [Overthinking](../concepts/overthinking.md), [POPE](pope.md), [Qwen2.5-VL](../methods/qwen2-5-vl.md), [Reasoning Trace Length](../concepts/reasoning-trace-length.md), [RLVR](../methods/rlvr.md), [ScienceQA](scienceqa.md), [Token-Level Entropy](../concepts/token-level-entropy.md), [WeMath](wemath.md)

## Appears in

- [Mixture-of-Visual-Thoughts: Exploring Context-Adaptive Reasoning Mode Selection for General Visual Reasoning](../../archive/papers/2026/title-4321f3ae06d02a2e/summary.md) — Unifies text-based and visually-grounded reasoning in one vision-language model and uses RL with a mode-relative advantage to make the model pick which mode to use per input, raising average accuracy over eight benchmarks by about 5 points.
- [Real-Time Visual Attribution Streaming in Thinking Model](../../archive/papers/2026/title-503ded235751878b/summary.md) — vStream trains a lightweight linear estimator to predict counterfactual ablation effects of image regions from cached attention features, so a multimodal reasoning model's visual grounding can be displayed while it reasons rather than recomputed afterwards, at 0.024 s per 10 tokens against 1.9-2.8 s for causal baselines.
- [ARES: Multimodal Adaptive Reasoning via Difficulty-Aware Token-Level Entropy Shaping](../../archive/papers/2026/title-544eea46a2eb68c1/summary.md) — ARES trains multimodal reasoning models to spend exploration effort in proportion to problem difficulty, using sliding-window token entropy as the signal for when and how much to explore.
- [Efficient Reasoning with Hidden Thinking](../../archive/papers/2026/title-725397e20ebf1509/summary.md) — Heima replaces each stage of a multimodal model's textual chain of thought with a single learned 'thinking token' generated in latent space, and trains a separate decoder that can expand those tokens back into readable reasoning.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
