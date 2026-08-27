# Mistral 7B

<!-- auto:begin -->

An open-weight LLM used across sources as an evaluation subject: as one of the base models fine-tuned with TISER's temporal self-reflection pipeline, and (per another archived source) as a comparison point in a study of when extra test-time iterations help versus harm a recurrent-depth reasoner, based on a measurable dynamical property (settling, marginal, or drifting) of the model's trained update map.

- **Kind**: model
- **Also called**: Mistral-7B
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [GPT-4o](gpt-4o.md), [LoRA fine-tuning](../methods/lora-fine-tuning.md), [Qwen2.5 7B](qwen2-5-7b.md)

## Appears in

- [Think Shallow, Solve Deep: Controlling Recurrent Dynamics for Reliable Test-Time Depth](../../archive/papers/2026/arxiv-2608-18222/summary.md) — Shows that whether a recurrent-depth reasoner is helped or harmed by extra test-time iterations is predicted by a measurable dynamical property of its trained update map (settling, marginal, or drifting), proves a sufficient condition for the decoded answer to be frozen under further iteration, and demonstrates that a single terminal fixed-point loss term moves the regime and the depth behaviour together in both directions.
- [Learning to Reason Over Time: Timeline Self-Reflection for Improved Temporal Reasoning in Language Models](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-1358/summary.md) — TISER (Temporal Self-Reflective Prompting) extends chain-of-thought into a four-stage test-time-scaling pipeline -- reasoning, explicit timeline construction, iterative self-reflection, then answer generation -- for temporal reasoning, and fine-tuning smaller open models (Mistral-7B, Qwen2.5-7B) on TISER-formatted synthetic traces lets them match or beat GPT-4o on in-domain and out-of-distribution temporal reasoning benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
