# compute-optimal scaling

<!-- auto:begin -->

Three of the four sources use this in the pretraining or training sense — allocating a fixed training-compute budget across the axes a trainer controls — and one uses it at inference, so the entry is not a single idea. The training-sense work covers reconciling the Kaplan and Chinchilla laws (attributing the disagreement to last-layer compute accounting, warmup duration and scale-dependent optimizer tuning), a compute-optimal recipe for contrastively converting decoder-only LMs into embedding models by jointly choosing model size, data quantity and fine-tuning method, and a split between model capacity and update-to-data ratio in online value-based deep RL where a TD-overfitting effect makes the best batch size depend on model size. Only AgentTTS uses the phrase at test time, searching for the compute-optimal model and inference budget per subtask of a multi-stage task. A reader should treat the label as a shared phrase across separate literatures rather than evidence that the archive holds one coherent result.

- **Kind**: concept
- **Also called**: Compute-Optimal Scaling, Compute-optimal scaling, compute-optimal recipe
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [compute-optimal allocation](compute-optimal-allocation.md), [Compute-optimal inference](compute-optimal-inference.md)

## Appears in

- [Repurposing Language Models into Embedding Models: Finding the Compute-Optimal Recipe](../../archive/papers/2024/title-8f5c26cc033aae9f/summary.md) — Derives a compute-optimal recipe for contrastively converting pretrained decoder-only language models into text embedding models, jointly choosing model size, data quantity and fine-tuning method for a given training budget.
- [Resolving Discrepancies in Compute-Optimal Scaling of Language Models](../../archive/papers/2024/title-d494aac6d49ec910/summary.md) — Reproduces the Kaplan et al. compute-optimal scaling law and shows that three methodological differences — last-layer compute accounting, warmup duration, and scale-dependent optimizer tuning — account for its disagreement with the Chinchilla law.
- [Compute-Optimal Scaling for Value-Based Deep RL](../../archive/papers/2025/title-d5d62f18a483fc4a/summary.md) — An empirical study of how to split a fixed training-compute budget between model capacity and update-to-data ratio in online value-based deep RL, identifying a TD-overfitting effect that makes the best batch size depend on model size.
- [AgentTTS: Large Language Model Agent for Test-time Compute-optimal Scaling Strategy in Complex Tasks](../../archive/papers/2025/title-f3f44348f8094543/summary.md) — Proposes an LLM-agent framework, AgentTTS, that searches for the compute-optimal choice of model and inference budget per subtask in multi-stage complex tasks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
