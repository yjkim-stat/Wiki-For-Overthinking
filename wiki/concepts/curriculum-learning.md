# curriculum learning

<!-- auto:begin -->

Ordering training so that a target is approached in stages, which both sources find is not an optimization convenience but a requirement. One proves curriculum is necessary rather than merely helpful for training latent reasoners: removing it collapses the model to at or below the no-CoT baseline on two of three benchmarks. The other designs the schedule to match the target's structure, deleting thinking tokens in geometric chunks aligned to the parity tree's levels rather than one at a time, which cuts the number of training stages from linear in chain length to logarithmic. The shared lesson is that the schedule should follow the shape of the computation being internalized, not the length of the text.

- **Kind**: concept
- **Also called**: curriculum, progressive training, staged training
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [activation patching](../methods/activation-patching.md), [causal intervention](causal-intervention.md), [chain of thought](../methods/chain-of-thought.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [Coconut](../methods/coconut.md), [compounding error](compounding-error.md), [effective depth](effective-depth.md), [Gemma-4-12B](../models/gemma-4-12b.md), [GPT-2](../models/gpt-2.md), [GPT-4o](../models/gpt-4o.md), [gradient descent analysis](../methods/gradient-descent-analysis.md), [GSM8K](../datasets/gsm8k.md), [implicit reasoning](implicit-reasoning.md), [information bottleneck](information-bottleneck.md), [KL regularization](../methods/kl-regularization.md), [latent chain of thought](../methods/latent-chain-of-thought.md), [latent reasoning](latent-reasoning.md), [linear probe](../methods/linear-probe.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [monitorability](monitorability.md), [parity](../datasets/parity.md), [ProntoQA](../datasets/prontoqa.md), [ProsQA](../datasets/prosqa.md), [Qwen3.6-35B-A3B](../models/qwen3-6-35b-a3b.md), [sample complexity](sample-complexity.md), [self-consistency](../methods/self-consistency.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time compute](test-time-compute.md)

## Appears in

- [Evading Chain-of-Thought Monitoring Through Model Poisoning](../../archive/papers/2026/arxiv-2608-02820/summary.md) — Shows that supervised fine-tuning can install a triggered backdoor whose visible reasoning stays clean, correct and topically benign while the final answer is attacker-chosen — leaving CoT-only monitors at chance (AUC 0.44-0.55) and recovering detection only when the monitor is shown the answer alongside the trace (0.76-1.00).
- [Capabilities and Fundamental Limits of Latent Chain-of-Thought](../../archive/papers/2026/local-6b66615b7bf3ef86/summary.md) — Explains why latent chain-of-thought excels at exploration but fails at computation by identifying decisional certainty as the governing variable, formalizing it as the Symbolic Index, and proving that curriculum learning is not merely helpful but necessary for training latent reasoners.
- [Transformers Provably Learn to Internalize Chain-of-Thought](../../archive/papers/2026/local-ee30f023d9f2d8fb/summary.md) — Proves that reasoning can be moved from emitted tokens into hidden states without losing sample efficiency, using a curriculum that deletes thinking tokens in geometric chunks and so needs only logarithmically many training stages.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
