# ProsQA

<!-- auto:begin -->

A synthetic graph-traversal question-answering task with binary queries, used by both sources as the case where latent chain-of-thought looks best and, on closer reading, as the case that explains why. One reports latent reasoning at 97.0% against 77.5% for explicit chain of thought while using 14.2 tokens against 49.4, and attributes the advantage to sustained uncertainty: its Symbolic Index stays below 0.6, in the 0.2 to 0.5 band, so a distribution over several latent paths is maintained rather than collapsed. The other exploits the binary answer space as an experimental affordance — with two possible answers, deleting every latent token is a clean do-operation whose counterfactual is read straight off two log probabilities — and finds accuracy changes by at most 1.0 point when they are removed. Read together, the benchmark is where latent reasoning wins and where the win is shown not to depend on the latent tokens carrying the computation.

- **Kind**: dataset
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME 2024](aime-2024.md), [causal intervention](../concepts/causal-intervention.md), [chain of thought](../concepts/chain-of-thought.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Coconut](../methods/coconut.md), [compounding error](../concepts/compounding-error.md), [curriculum learning](../methods/curriculum-learning.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [effective depth](../concepts/effective-depth.md), [entropy collapse](../concepts/entropy-collapse.md), [GPT-2](../models/gpt-2.md), [GSM8K](gsm8k.md), [information bottleneck](../concepts/information-bottleneck.md), [latent chain of thought](../methods/latent-chain-of-thought.md), [logit lens](../methods/logit-lens.md), [MATH500](math500.md), [ProntoQA](prontoqa.md), [QwQ-32B](../models/qwq-32b.md), [self-consistency](../methods/self-consistency.md), [soft thinking](../methods/soft-thinking.md)

## Appears in

- [The Illusion of Superposition? A Principled Analysis of Latent Thinking in Language Models](../../archive/papers/2026/local-043e84b0b0ae0a39/summary.md) — Tests the claim that continuous chain-of-thought lets a model hold several candidate solutions at once, and finds it holds only for models trained from scratch: off-the-shelf models collapse a superposed input to a single token within a few layers, and fine-tuned latent reasoners solve the task in one forward pass and copy the answer through the latent slots.
- [Capabilities and Fundamental Limits of Latent Chain-of-Thought](../../archive/papers/2026/local-6b66615b7bf3ef86/summary.md) — Explains why latent chain-of-thought excels at exploration but fails at computation by identifying decisional certainty as the governing variable, formalizing it as the Symbolic Index, and proving that curriculum learning is not merely helpful but necessary for training latent reasoners.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
