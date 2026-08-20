# ReAct

<!-- auto:begin -->

An agent format interleaving a written thought, a chosen action, its input and the returned observation, repeated until an answer. In these sources it is infrastructure rather than a contribution -- the format that supervised trajectories are written in, that policies are fine-tuned to emit parsably, and that tool-augmented systems are built on. Two of the sources use it while establishing something about what that format does not guarantee. The tool-orchestration work fine-tunes a policy on ReAct-formatted trajectories and then shows that behaviour cloning on them plateaus, and that removing a global completion reward leaves per-step decision and tool-selection accuracy at 100 percent while whole-response accuracy falls to 29.92 percent -- correct steps in the correct format, never terminating. The agent-contamination work uses ReAct-style systems as the setting in which implicit state persists across sessions through name binding and event triggering, invisible to logging that records only the tool calls the format makes explicit. The archive's reading is that ReAct makes the reasoning and the action legible in the transcript without making the state that drives them legible.

- **Kind**: method
- **Also called**: Reason+Act
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [activation patching](activation-patching.md), [advantage estimation](../concepts/advantage-estimation.md), [calibration](calibration.md), [credit assignment](../concepts/credit-assignment.md), [DeepSeek-V3.2](../models/deepseek-v3-2.md), [detection versus control](../concepts/detection-versus-control.md), [factorial ablation](factorial-ablation.md), [Gemini-2.0-flash](../models/gemini-2-0-flash.md), [GPT-4o](../models/gpt-4o.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [GRPO](grpo.md), [hallucination](../concepts/hallucination.md), [KL regularization](kl-regularization.md), [linear probe](linear-probe.md), [linear separability](../concepts/linear-separability.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.3-70B](../models/llama-3-3-70b.md), [Llama-3-8B](../models/llama-3-8b.md), [LLM-as-a-judge](llm-as-a-judge.md), [LoRA](lora.md), [multi-agent pipeline](../concepts/multi-agent-pipeline.md), [outcome reward](../concepts/outcome-reward.md), [persistent semantic entity](../concepts/persistent-semantic-entity.md), [predictive entropy](../concepts/predictive-entropy.md), [process reward](../concepts/process-reward.md), [process supervision](../concepts/process-supervision.md), [prompt injection](../concepts/prompt-injection.md), [Qwen2.5-coder-7B](../models/qwen2-5-coder-7b.md), [Qwen2.5-VL](../models/qwen2-5-vl.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-VL-235B](../models/qwen3-vl-235b.md), [residual stream](../concepts/residual-stream.md), [reward shaping](../concepts/reward-shaping.md), [self-verification](../concepts/self-verification.md), [semantic entropy](semantic-entropy.md), [supervised fine-tuning](supervised-fine-tuning.md), [uncertainty quantification](../concepts/uncertainty-quantification.md), [Wilson confidence interval](wilson-confidence-interval.md)

## Appears in

- [Persistent Semantic Entities in Tool-Augmented LLM Systems](../../archive/papers/2026/arxiv-2608-07952/summary.md) — Formalises implicit agent state that survives session boundaries as Persistent Semantic Entities defined by name binding, event triggering and propagation, and measures across 24 models that whether injected contamination decays depends on what kind of contamination it is rather than on model scale or deployment.
- [VTO: Visual Tool Orchestration for Video Anomaly Detection](../../archive/papers/2026/arxiv-2608-08219/summary.md) — Trains a multimodal agent to orchestrate twelve video-analysis tools for anomaly detection with GRPO under a dual reward that combines exact-match rule checks with an LLM judge scoring logicality, relevance and completeness, and releases the benchmark it is evaluated on.
- [Actionable Hallucination Detection: Translating Latent Uncertainty into Agentic Critique](../../archive/papers/2026/arxiv-2608-10430/summary.md) — Detects the class of hallucination where a model confidently fabricates a parameter the user never gave, by running a LoRA adapter alongside the frozen model that restructures the residual stream and then names the offending parameter in words the agent can act on.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
