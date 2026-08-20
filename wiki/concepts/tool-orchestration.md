# tool orchestration

<!-- auto:begin -->

Sequencing several tools whose outputs feed each other, as distinct from selecting one tool for one query. Both sources build benchmarks around the distinction and find it is where systems break. The video-anomaly work separates single-tool from interrelated-tool responses and reports the gap starkly: one baseline scores 0 percent whole-response accuracy on the interrelated split, another 4.52, and a model roughly nine times larger than the trained system reaches only 67.40 -- while performing acceptably on isolated tools. The long-horizon video agent identifies the complementary failure in sequencing over time, where prior systems follow a monotonic zoom-in and cannot revise, and shows that results on a 41-minute benchmark do not predict results on multi-hour ones, with one agent leading the first and losing 35 points on the second. The archive's reading is that orchestration is a separate capability from tool use rather than more of it, and that a benchmark not separating the two will report a system as competent that cannot chain.

- **Kind**: concept
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [advantage estimation](advantage-estimation.md), [ALFWorld](../datasets/alfworld.md), [component ablation](../methods/component-ablation.md), [compute allocation](compute-allocation.md), [credit assignment](credit-assignment.md), [DeepSeek-V4-Flash](../models/deepseek-v4-flash.md), [error compounding](error-compounding.md), [exploration](exploration.md), [format compliance](format-compliance.md), [Gemini-1.5-Pro](../models/gemini-1-5-pro.md), [GPT-4o](../models/gpt-4o.md), [GRPO](../methods/grpo.md), [in-context learning](in-context-learning.md), [KL regularization](../methods/kl-regularization.md), [Llama-3-8B](../models/llama-3-8b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [long-horizon agency](long-horizon-agency.md), [LoRA](../methods/lora.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [outcome reward](outcome-reward.md), [premature convergence](premature-convergence.md), [process reward](process-reward.md), [process supervision](process-supervision.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen2.5-VL](../models/qwen2-5-vl.md), [Qwen3.5-27B](../models/qwen3-5-27b.md), [Qwen3.6-27B](../models/qwen3-6-27b.md), [Qwen3-8B](../models/qwen3-8b.md), [Qwen3-VL](../models/qwen3-vl.md), [Qwen3-VL-8B](../models/qwen3-vl-8b.md), [ReAct](../methods/react.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [reward shaping](reward-shaping.md), [selective prediction](selective-prediction.md), [self-correction](self-correction.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [tool learning](tool-learning.md), [Vicuna-7B](../models/vicuna-7b.md), [Video-MME](../datasets/video-mme.md)

## Appears in

- [SCOUT: Self-Checking and Recovery-Aware Tool-Thought Agents for Ultra-Long Egocentric Video Reasoning](../../archive/papers/2026/arxiv-2608-07959/summary.md) — Replaces the monotonic zoom-in that tool-using video agents follow once they pick a region with a policy that self-checks each tool observation and can switch regions, and trains it with turn-level credit applied multiplicatively -- reweighting the trajectory advantage's magnitude while preserving its sign -- rather than additively.
- [VTO: Visual Tool Orchestration for Video Anomaly Detection](../../archive/papers/2026/arxiv-2608-08219/summary.md) — Trains a multimodal agent to orchestrate twelve video-analysis tools for anomaly detection with GRPO under a dual reward that combines exact-match rule checks with an LLM judge scoring logicality, relevance and completeness, and releases the benchmark it is evaluated on.
- [Diagnosis Before Recovery: Turning Agent Failures into Selective Self-Correction](../../archive/papers/2026/arxiv-2608-11772/summary.md) — Profiles the dominant failure mode of an agent task family on development data, then freezes a policy that permits only the recovery interventions matched to that failure -- so a failure decides which repair is admissible and how much evidence to spend, rather than triggering more context indiscriminately.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
