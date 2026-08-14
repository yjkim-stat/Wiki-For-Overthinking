# predictive entropy

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [activation patching](../methods/activation-patching.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [answer stabilization](answer-stabilization.md), [budget forcing](../methods/budget-forcing.md), [calibration](../methods/calibration.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER](../methods/deer.md), [dense retrieval](../methods/dense-retrieval.md), [detection versus control](detection-versus-control.md), [Dynasor](../methods/dynasor.md), [early exit](../methods/early-exit.md), [entropy trajectory](entropy-trajectory.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [hallucination](hallucination.md), [in-context learning](in-context-learning.md), [linear probe](../methods/linear-probe.md), [linear separability](linear-separability.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [MATH500](../datasets/math500.md), [overthinking](overthinking.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [Qwen3-8B](../models/qwen3-8b.md), [reasoning drift](reasoning-drift.md), [reasoning redundancy](reasoning-redundancy.md), [residual stream](residual-stream.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [SciQ](../datasets/sciq.md), [self-consistency](../methods/self-consistency.md), [self-reflection](../methods/self-reflection.md), [semantic entropy](../methods/semantic-entropy.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time scaling](../methods/test-time-scaling.md), [uncertainty quantification](uncertainty-quantification.md)

## Appears in

- [Actionable Hallucination Detection: Translating Latent Uncertainty into Agentic Critique](../../archive/papers/2026/arxiv-2608-10430/summary.md) — Detects the class of hallucination where a model confidently fabricates a parameter the user never gave, by running a LoRA adapter alongside the frozen model that restructures the residual stream and then names the offending parameter in words the agent can act on.
- [ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling](../../archive/papers/2026/arxiv-2608-10928/summary.md) — Injects a retrieved solved problem, with its full worked solution, into the middle of a reasoning model's own thinking trace at each step boundary, using the model's current intermediate answer as the retrieval query.
- [Unveiling the Entropy Dynamics of Chain-of-Thought Reasoning](../../archive/papers/2026/local-379c0b6966148b4a/summary.md) — Shows that CoT entropy follows a two-phase structure — a high-entropy exploration region that shifts abruptly into a low-entropy convergence region — and detects that shift online with the CUSUM change-point algorithm to drive early exit and trajectory-weighted voting.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
