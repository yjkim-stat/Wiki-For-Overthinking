# semantic entropy

<!-- auto:begin -->

An uncertainty estimate that clusters several sampled generations by meaning and takes the entropy over those clusters rather than over tokens, so that paraphrases of one answer do not count as disagreement. The archive's two sources place it at opposite ends of usefulness. In the reasoning-serving system it is one of the signals behind an algorithm-agnostic measure of how far a reasoning algorithm's answer has stopped changing, used to reallocate or terminate compute per query and reported as saving up to half the tokens in batch inference. In the hallucination-detection work it fails outright, and the diagnosis is specific rather than dismissive: on the failure mode where a model confidently fabricates a parameter the user never supplied, the entropy family reaches AUROC 0.674 for token entropy, 0.639 for semantic entropy and 0.548 for a semantic-entropy probe against 0.966 for an adapter reading internal state, and once AUPRC is adjusted for base prevalence the entropy methods sit exactly at the trivial always-positive decision floor. The reason is structural -- because the model is confident and the fabrication is plausible, the samples agree, so semantic entropy collapses into a single cluster. The two sources together bound it: it measures disagreement among samples, which tracks difficulty and convergence well and tracks confident wrongness not at all.

- **Kind**: method
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation patching](activation-patching.md), [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [AIME 2024](../datasets/aime-2024.md), [AMC23](../datasets/amc23.md), [answer stabilization](../concepts/answer-stabilization.md), [calibration](../concepts/calibration.md), [chain of thought](chain-of-thought.md), [DeepSeek-R1](../models/deepseek-r1.md), [detection versus control](../concepts/detection-versus-control.md), [Dynasor](dynasor.md), [early exit](early-exit.md), [GSM8K](../datasets/gsm8k.md), [hallucination](../concepts/hallucination.md), [linear probe](linear-probe.md), [linear separability](../concepts/linear-separability.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-70B](../models/llama-3-1-70b.md), [LLM-as-a-judge](llm-as-a-judge.md), [LoRA](lora.md), [MATH500](../datasets/math500.md), [Monte Carlo tree search](monte-carlo-tree-search.md), [overthinking](../concepts/overthinking.md), [predictive entropy](../concepts/predictive-entropy.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen3-4B](../models/qwen3-4b.md), [QwQ-32B](../models/qwq-32b.md), [ReAct](react.md), [residual stream](../concepts/residual-stream.md), [self-consistency](self-consistency.md), [supervised fine-tuning](supervised-fine-tuning.md), [test-time compute](../concepts/test-time-compute.md), [uncertainty quantification](../concepts/uncertainty-quantification.md)

## Appears in

- [Actionable Hallucination Detection: Translating Latent Uncertainty into Agentic Critique](../../archive/papers/2026/arxiv-2608-10430/summary.md) — Detects the class of hallucination where a model confidently fabricates a parameter the user never gave, by running a LoRA adapter alongside the frozen model that restructures the residual stream and then names the offending parameter in words the agent can act on.
- [Efficiently Scaling LLM Reasoning with Certaindex](../../archive/papers/2025/local-0c24c3c0e4729108/summary.md) — Defines certaindex, an algorithm-agnostic measure of how much a reasoning algorithm's answer has stopped changing, and builds it into a serving system that reallocates or terminates compute per query — saving up to 50% of tokens in batch inference and tripling online throughput.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
