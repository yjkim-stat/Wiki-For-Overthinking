# Coconut

<!-- auto:begin -->

The curriculum that trains latent chain-of-thought by progressively replacing prefix reasoning tokens with continuous latent states, and in these sources the standard instantiation of latent CoT rather than one method among several. Both find its behaviour is governed by the curriculum rather than by the latent representation: one recasts the per-stage objective by Lagrangian duality as a Conditional Information Bottleneck and shows that removing the curriculum drops GSM8K from 34.1% to 14.4% and ProntoQA from 99.8% to 52.4%, at or below the no-CoT baseline. The other finds that in the fine-tuned regime the latent tokens it produces can be deleted outright with accuracy changing by at most 1.0 point on ProsQA across GPT-2 and three SmolLM2 sizes, with entity probing showing the final target entity already dominating the representation. Taken together the sources describe a method whose latent slots carry an answer that has already been reached rather than a computation in progress.

- **Kind**: method
- **Also called**: COCONUT, Coconut curriculum
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [AIME 2024](../datasets/aime-2024.md), [auditability](../concepts/auditability.md), [BeaverTails](../datasets/beavertails.md), [causal intervention](../concepts/causal-intervention.md), [chain of thought](chain-of-thought.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [compounding error](../concepts/compounding-error.md), [curriculum learning](../concepts/curriculum-learning.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [effective depth](../concepts/effective-depth.md), [entropy collapse](../concepts/entropy-collapse.md), [GPT-2](../models/gpt-2.md), [GSM8K](../datasets/gsm8k.md), [HarmBench](../datasets/harmbench.md), [information bottleneck](../concepts/information-bottleneck.md), [latent chain of thought](latent-chain-of-thought.md), [latent reasoning](../concepts/latent-reasoning.md), [LLM-as-a-judge](llm-as-a-judge.md), [logit lens](logit-lens.md), [MATH-500](../datasets/math-500.md), [monitorability](../concepts/monitorability.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [ProntoQA](../datasets/prontoqa.md), [ProsQA](../datasets/prosqa.md), [QwQ-32B](../models/qwq-32b.md), [representation versus readout](../concepts/representation-versus-readout.md), [safety alignment](../concepts/safety-alignment.md), [self-consistency](self-consistency.md), [soft thinking](soft-thinking.md), [supervised fine-tuning](supervised-fine-tuning.md)

## Appears in

- [LatentGuard: Efficient and Inspectable Latent Reasoning for LLM Safeguards](../../archive/papers/2026/arxiv-2608-03838/summary.md) — Compresses a safety guard's textual rationales into continuous latent states by a staged curriculum, cutting 268 reasoning tokens to 1.60 and latency 8.9-fold, and adds an on-demand decoder that reconstructs a human-readable audit artifact — whose own ablation shows the artifact is anchored far more by the source text than by the latent states it is supposed to inspect.
- [The Illusion of Superposition? A Principled Analysis of Latent Thinking in Language Models](../../archive/papers/2026/local-043e84b0b0ae0a39/summary.md) — Tests the claim that continuous chain-of-thought lets a model hold several candidate solutions at once, and finds it holds only for models trained from scratch: off-the-shelf models collapse a superposed input to a single token within a few layers, and fine-tuned latent reasoners solve the task in one forward pass and copy the answer through the latent slots.
- [Capabilities and Fundamental Limits of Latent Chain-of-Thought](../../archive/papers/2026/local-6b66615b7bf3ef86/summary.md) — Explains why latent chain-of-thought excels at exploration but fails at computation by identifying decisional certainty as the governing variable, formalizing it as the Symbolic Index, and proving that curriculum learning is not merely helpful but necessary for training latent reasoners.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
