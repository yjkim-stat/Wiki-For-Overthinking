# Vicuna-7B

<!-- auto:begin -->

An early open instruction-tuned Llama derivative, appearing in this archive twice as the weak end of a comparison. In the video tool-orchestration benchmark it scores 0 percent whole-response accuracy on the interrelated-tool split under both zero-shot and few-shot prompting, which is that paper's starkest illustration that chaining interdependent tools is a different capability from invoking one. In the reproduction study it is the model evaluated through an independent re-implementation, reported separately and explicitly marked as not on the same scale as the other three because it was run on different hardware and library versions, with only the direction of its degradation treated as comparable. Neither source describes the model; its role here is as a floor and as a reminder that a separately re-implemented evaluation is not a fourth data point on the same axis.

- **Kind**: model
- **Also called**: Vicuna-7b
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [activation steering](../methods/activation-steering.md), [advantage estimation](../concepts/advantage-estimation.md), [bootstrap confidence intervals](../methods/bootstrap-confidence-intervals.md), [calibration](../concepts/calibration.md), [contrastive activation addition](../methods/contrastive-activation-addition.md), [credit assignment](../concepts/credit-assignment.md), [detection versus control](../concepts/detection-versus-control.md), [distribution mismatch](../concepts/distribution-mismatch.md), [expected calibration error](../concepts/expected-calibration-error.md), [GPT-4](gpt-4.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [interpretability illusion](../concepts/interpretability-illusion.md), [KL regularization](../methods/kl-regularization.md), [linear probe](../methods/linear-probe.md), [Llama-3-8B](llama-3-8b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [Mistral-7B](mistral-7b.md), [outcome reward](../concepts/outcome-reward.md), [process reward](../concepts/process-reward.md), [process supervision](../concepts/process-supervision.md), [Qwen2.5-VL](qwen2-5-vl.md), [Qwen3-8B](qwen3-8b.md), [Qwen3-VL-8B](qwen3-vl-8b.md), [ReAct](../methods/react.md), [representation editing](../methods/representation-editing.md), [reproducibility](../concepts/reproducibility.md), [reward shaping](../methods/reward-shaping.md), [selectivity control](../methods/selectivity-control.md), [self-consistency](../methods/self-consistency.md), [steering vector](../methods/steering-vector.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [tool learning](../concepts/tool-learning.md), [tool orchestration](../concepts/tool-orchestration.md)

## Appears in

- [VTO: Visual Tool Orchestration for Video Anomaly Detection](../../archive/papers/2026/arxiv-2608-08219/summary.md) — Trains a multimodal agent to orchestrate twelve video-analysis tools for anomaly detection with GRPO under a dual reward that combines exact-match rule checks with an LLM judge scoring logicality, relevance and completeness, and releases the benchmark it is evaluated on.
- [Reproducing and Stress-Testing Two Approaches to LLM Reasoning Reliability: Test-Time Probability Aggregation and Logic-Representation Editing](../../archive/papers/2026/arxiv-2608-08514/summary.md) — Independently reproduces two published reliability methods and stress-tests them across models and domains their authors never tried, finding one reproduces exactly but loses significance everywhere new, and the other rests on a decodable logic direction that a same-norm random direction matches exactly under steering.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
