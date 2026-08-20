# structured chain of thought

<!-- auto:begin -->

Constraining a chain of thought to a fixed sequence of typed segments rather than leaving it free-form, so that each segment can be separately supervised, rewarded or checked. The spatial-reasoning work makes the case most concretely: perception, including depth estimation and grounding, becomes a stage the model must explicitly produce before any inference, and each segment then receives its own process reward and its own advantage term. Its ablation shows why the structure alone is not the contribution -- with the perception advantage removed the model still emits the perception segment and the grounding and depth rewards simply never improve over training, so the structure is present and inert. The therapy-dialogue work uses the same idea to encode domain procedure, grounding the segment sequence in clinical guidelines and adding a separate orchestrator to keep simulated patients from collapsing into sycophantic compliance. Between them the sources make one point the archive should carry: imposing structure creates addressable slots, and a slot supervised only through the final answer is not filled with anything useful -- which is the same result the latent-reasoning entries reach from the other direction.

- **Kind**: method
- **Also called**: structured CoT, structured chain-of-thought
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [activation steering](activation-steering.md), [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [advantage estimation](../concepts/advantage-estimation.md), [chain of thought](chain-of-thought.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [component ablation](component-ablation.md), [compression](../concepts/compression.md), [credit assignment](../concepts/credit-assignment.md), [flow matching](flow-matching.md), [GPT-4o](../models/gpt-4o.md), [GRPO](grpo.md), [latent reasoning](../concepts/latent-reasoning.md), [LLM-as-a-judge](llm-as-a-judge.md), [out-of-domain generalization](../concepts/out-of-domain-generalization.md), [outcome reward](../concepts/outcome-reward.md), [process reward](../concepts/process-reward.md), [Qwen2.5-VL-3B](../models/qwen2-5-vl-3b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [reward shaping](../concepts/reward-shaping.md), [supervised fine-tuning](supervised-fine-tuning.md), [sycophancy](../concepts/sycophancy.md), [synthetic data generation](synthetic-data-generation.md), [visual grounding](../concepts/visual-grounding.md)

## Appears in

- [ODRA: Synthesizing Cognitive Behavioral Therapy Sessions with Structured Chain-Of-Thought and Dynamic Patient Resistance](../../archive/papers/2026/arxiv-2608-04524/summary.md) — Synthesizes Cognitive Behavioral Therapy dialogues using a CoT strategy grounded in CBT guidelines plus a resistance orchestrator that steers simulated patients away from sycophantic compliance.
- [XCoT-VLA: Executable Chain-of-Thought for Vision-Language-Action Driving](../../archive/papers/2026/arxiv-2608-10976/summary.md) — Replaces a verbose natural-language rationale with two to six executable action tokens drawn from a fixed vocabulary, supervised automatically by pairing logged trajectories with scene context, so that driving-oriented reasoning fits inside a real-time control budget that verbose chain-of-thought exceeds by three to four times.
- [SCOUT: Unlocking Enhanced Spatial Reasoning via Structured Chain-of-Thought and Multi-Objective Process Reward](../../archive/papers/2026/arxiv-2608-12220/summary.md) — Splits a spatial-reasoning chain of thought into explicitly typed segments -- perception, including depth, and reasoning -- and gives each its own process reward and its own advantage term, so that the two do not compete for credit under a single outcome signal.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
