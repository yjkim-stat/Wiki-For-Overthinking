# deepseek-v4-flash

<!-- auto:begin -->

A DeepSeek reasoning model used in this archive as an API-accessed backbone whose chain of thought is reachable. It is the frozen backbone of a self-reflection protocol study -- nine experiments over three tool-free benchmarks, where its self-reported numeric confidence proved useless (at or above 0.6 on 100% of first generations) while its discrete CONFIRMED sentinel early-stopped 82-88% of items -- and it is the most extractable of three open-CoT targets in a CoT-extraction study, where an attack reaches 66.4% near-verbatim success against near-zero for prior methods. Both uses treat it as a representative current reasoning model rather than as a subject in itself.

- **Kind**: model
- **Also called**: DeepSeek-V4-Flash, deepseek-v4-flash
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [deepseek-v4-pro](deepseek-v4-pro.md), [Direct Prompting](../methods/direct-prompting.md), [GAIA](../datasets/gaia.md), [GLM-5.2](glm-5-2.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md), [o4-mini](o4-mini.md), [OpenThoughts](../datasets/openthoughts.md), [Qwen3.5-Plus](qwen3-5-plus.md), [Self-verification](../methods/self-verification.md), [SWE-bench Verified](../datasets/swe-bench-verified.md)

## Appears in

- [CHILL-Harness: Counterfactual Harness Learning for Efficient Reasoning in Long-Horizon Agents](../../archive/papers/2026/arxiv-2607-25825/summary.md) — Treats an agent harness's orchestration decisions as causal interventions on the current workflow, learns which ones would improve it, and executes only those whose estimated advantage clears a margin -- so deliberation is spent where it changes the plan rather than at every step.
- [Training-Free Inference-Time Self-Reflection and Cost-Bounded Early Stopping for Large Language Models](../../archive/papers/2026/arxiv-2608-18884/summary.md) — A training-free generate-critique-revise loop over a frozen backbone that stops when the critique emits a CONFIRMED sentinel or a depth cap is hit, measured across nine experiments to show the sentinel halts 82-88% of items at about 2.1 generations, with accuracy flat on BBH and significantly higher on GSM8K and MATH.
- [EchoCoT: Extracting Hidden Chain-of-Thought from Large Reasoning Models](../../archive/papers/2026/arxiv-2608-20055/summary.md) — A security study showing that the hidden chain-of-thought of a black-box reasoning model can be recovered near-verbatim through ordinary API tool-calling, because reasoning state must be retained across tool calls within a turn.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
