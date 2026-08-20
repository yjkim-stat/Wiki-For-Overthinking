# tool learning

<!-- auto:begin -->

Training a model to invoke external tools and use what they return, and across 3 sources a capability with a syntactic precondition easy to mistake for the capability itself. The ablation that makes the separation categorical: a policy trained by reinforcement learning alone cannot reliably emit parsable tool calls at all, at 50.6 percent format compliance against 100 for the full pipeline, while supervised fine-tuning alone reaches 99.8 percent and comes within a few points of the full system -- so imitation installs the invocation format and reinforcement learning adds judgement about where to search and when to stop. A second source reaches the same two-stage arrangement and shows what the reinforcement stage is for, with a policy that selects the right tool at every step and never terminates. A third names a failure invisible to standard metrics: the right tool called with semantically correct arguments in the wrong language, which is operationally invalid and which no function-calling metric catches. The decomposition the three support is that emitting parsable calls, choosing which call to make, and knowing when to stop fail separately.

- **Kind**: concept
- **Also called**: tool use
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [advantage estimation](advantage-estimation.md), [catastrophic forgetting](catastrophic-forgetting.md), [component ablation](../methods/component-ablation.md), [credit assignment](credit-assignment.md), [cross-lingual transfer](cross-lingual-transfer.md), [error compounding](error-compounding.md), [exploration](exploration.md), [format compliance](format-compliance.md), [Gemini-1.5-Pro](../models/gemini-1-5-pro.md), [GPT-4o](../models/gpt-4o.md), [GRPO](../methods/grpo.md), [KL regularization](../methods/kl-regularization.md), [Llama-3-8B](../models/llama-3-8b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [outcome reward](outcome-reward.md), [PPO](../methods/ppo.md), [premature convergence](premature-convergence.md), [process reward](process-reward.md), [process supervision](process-supervision.md), [Qwen2.5-14B-Instruct](../models/qwen2-5-14b-instruct.md), [Qwen2.5-32B-Instruct](../models/qwen2-5-32b-instruct.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen2.5-VL](../models/qwen2-5-vl.md), [Qwen3-VL](../models/qwen3-vl.md), [Qwen3-VL-8B](../models/qwen3-vl-8b.md), [ReAct](../methods/react.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [reward shaping](../methods/reward-shaping.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [tool orchestration](tool-orchestration.md), [Vicuna-7B](../models/vicuna-7b.md), [Video-MME](../datasets/video-mme.md)

## Appears in

- [SCOUT: Self-Checking and Recovery-Aware Tool-Thought Agents for Ultra-Long Egocentric Video Reasoning](../../archive/papers/2026/arxiv-2608-07959/summary.md) — Replaces the monotonic zoom-in that tool-using video agents follow once they pick a region with a policy that self-checks each tool observation and can switch regions, and trains it with turn-level credit applied multiplicatively -- reweighting the trajectory advantage's magnitude while preserving its sign -- rather than additively.
- [VTO: Visual Tool Orchestration for Video Anomaly Detection](../../archive/papers/2026/arxiv-2608-08219/summary.md) — Trains a multimodal agent to orchestrate twelve video-analysis tools for anomaly detection with GRPO under a dual reward that combines exact-match rule checks with an LLM judge scoring logicality, relevance and completeness, and releases the benchmark it is evaluated on.
- [When the API Speaks the Wrong Language: Revisiting Post-Training for Multilingual Tool Use](../../archive/papers/2026/arxiv-2608-11715/summary.md) — Names and measures a multilingual tool-calling failure in which the model picks the right API but writes argument values in the wrong language, then compares supervised fine-tuning against PPO and GRPO under matched budgets and finds that a well-selected supervised checkpoint matches or beats reinforcement learning on the task while costing more elsewhere.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
