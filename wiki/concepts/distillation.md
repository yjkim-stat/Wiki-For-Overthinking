# distillation

<!-- auto:begin -->

Training a model (or a stage of pretraining) to imitate a stronger teacher's outputs or reasoning traces, rather than learning purely from raw data or reward. The archived sources give it mixed effects on reasoning-length behavior: 'Distilled Pretraining' finds it improves test-time-scaling generalization but impairs in-context learning; 'When Reasoning Meets Compression' finds it (along with quantization and pruning) degrades reasoning ability differently than memorization ability; 'Reinforcement Learning Teachers of Test Time Scaling' trains an RL teacher specifically to produce distillation explanations that help a student learn.

- **Kind**: concept
- **Also called**: knowledge distillation
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [test-time compute scaling](test-time-compute-scaling.md), [test-time scaling](test-time-scaling.md)

## Appears in

- [Reinforcement Learning Teachers of Test Time Scaling](../../archive/papers/2025/title-21d46f88974ff7dd/summary.md) — Trains a reinforcement-learned teacher model that is given the solution and rewarded for producing explanations that help a student model understand it, outperforming distillation pipelines built from much larger models.
- [Distilled Pretraining: A modern lens of Data, In-Context Learning and Test-Time Scaling](../../archive/papers/2026/title-5d210749910cf061/summary.md) — Studies how distillation during LLM pretraining improves test-time scaling but impairs in-context learning (via induction heads), explained through a bigram-model sandbox.
- [When Reasoning Meets Compression: Understanding the Effects of LLMs Compression on Large Reasoning Models](../../archive/papers/2026/title-c593d75efe2e5d8c/summary.md) — Analyzes how quantization, distillation, and pruning affect the reasoning versus memorization abilities of large reasoning models such as DeepSeek-R1, and proposes protecting a small subset of weights to recover accuracy under quantization.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
