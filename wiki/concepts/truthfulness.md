# truthfulness

<!-- auto:begin -->

Saying what is true, treated by both sources as separable from reasoning well. One makes it one of three trustworthiness dimensions alongside safety and efficiency, evaluated over 30 reasoning tasks and 26 models, and finds reasoning models generally more fragile than plain LLMs when facing reasoning-induced risks. The other supplies a mechanism for why capable reasoners can still be untruthful: a reasoning-answer hit gap in which the model identifies the correct facts during reasoning and fails to carry them into the response, which it addresses by reweighting reasoning segments rather than by checking outputs. Together they locate untruthfulness after the reasoning rather than in it.

- **Kind**: concept
- **Also called**: factuality, veracity
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [chain of thought](../methods/chain-of-thought.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [credit assignment](credit-assignment.md), [meta-reasoning](../methods/meta-reasoning.md), [monitorability](monitorability.md), [overthinking](overthinking.md), [process supervision](process-supervision.md)

## Appears in

- [Red Teaming Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1034/summary.md) — A trustworthiness benchmark for reasoning models over truthfulness, safety and efficiency, using training paradigm as an analytical axis, and finding reasoning models more fragile than plain LLMs to reasoning-induced risks.
- [MR-ALIGN: Meta-Reasoning Informed Factuality Alignment for Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-204/summary.md) — Improves factuality by reweighting reasoning segments according to state-transition probabilities along the thinking process, targeting a gap where correct facts appear in reasoning but not in the answer.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
