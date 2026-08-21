# compute-optimal scaling

<!-- auto:begin -->

Three of the four sources use this in the pretraining or training sense — allocating a fixed training-compute budget across the axes a trainer controls — and one uses it at inference, so the entry is not a single idea. The training-sense work covers reconciling the Kaplan and Chinchilla laws (attributing the disagreement to last-layer compute accounting, warmup duration and scale-dependent optimizer tuning), a compute-optimal recipe for contrastively converting decoder-only LMs into embedding models by jointly choosing model size, data quantity and fine-tuning method, and a split between model capacity and update-to-data ratio in online value-based deep RL where a TD-overfitting effect makes the best batch size depend on model size. Only AgentTTS uses the phrase at test time, searching for the compute-optimal model and inference budget per subtask of a multi-stage task. A reader should treat the label as a shared phrase across separate literatures rather than evidence that the archive holds one coherent result.

- **Kind**: concept
- **Also called**: Compute-Optimal Scaling, Compute-optimal scaling, compute-optimal recipe, compute-optimal scaling
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [compute-optimal allocation](compute-optimal-allocation.md), [Compute-optimal inference](compute-optimal-inference.md)

## Appears in

- [AgentTTS: Large Language Model Agent for Test-time Compute-optimal Scaling Strategy in Complex Tasks](../../archive/papers/2025/title-f3f44348f8094543/summary.md) — Proposes an LLM-agent framework, AgentTTS, that searches for the compute-optimal choice of model and inference budget per subtask in multi-stage complex tasks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
