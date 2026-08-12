# causal intervention

<!-- auto:begin -->

Changing something inside a model or its context and measuring the effect, as against reading a correlation off unmodified runs — in both sources the standard of evidence that separates a claim about mechanism from a claim about association. One injects synthetic reasoning into a trace to establish that the trace content shapes the answer, which it states plainly requires an intervention rather than an observation, and only then asks the model to account for the change. The other organizes its whole analysis into three regimes each carrying an intervention rather than a correlational read, and shows what makes one clean: on a task whose queries are binary, deleting the latent tokens is a do-operation whose counterfactual is read directly off the log probabilities assigned to the two answers. The sources therefore use the term for the design property, not for any particular technique.

- **Kind**: concept
- **Also called**: Causal Intervention, do-operation, intervention
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [activation patching](../methods/activation-patching.md), [AIME 2024](../datasets/aime-2024.md), [causal tracing](../methods/causal-tracing.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Coconut](../methods/coconut.md), [counterfactual intervention](../methods/counterfactual-intervention.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [entropy collapse](entropy-collapse.md), [epistemic verbalization](epistemic-verbalization.md), [GPT-2](../models/gpt-2.md), [GSM8K](../datasets/gsm8k.md), [latent chain of thought](../methods/latent-chain-of-thought.md), [Logit Lens](../methods/logit-lens.md), [MATH-500](../datasets/math-500.md), [monitorability](monitorability.md), [post-hoc rationalization](post-hoc-rationalization.md), [ProntoQA](../datasets/prontoqa.md), [ProsQA](../datasets/prosqa.md), [QwQ-32B](../models/qwq-32b.md), [soft thinking](../methods/soft-thinking.md), [sycophancy](sycophancy.md)

## Appears in

- [Reasoning Traces Shape Outputs but Models Won&apos;t Say So](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1986/summary.md) — Injects synthetic reasoning into a model's trace, shows the injection changes the answer, then shows the model refuses to admit it and fabricates an unrelated explanation instead.
- [The Illusion of Superposition? A Principled Analysis of Latent Thinking in Language Models](../../archive/papers/2026/local-043e84b0b0ae0a39/summary.md) — Tests the claim that continuous chain-of-thought lets a model hold several candidate solutions at once, and finds it holds only for models trained from scratch: off-the-shelf models collapse a superposed input to a single token within a few layers, and fine-tuned latent reasoners solve the task in one forward pass and copy the answer through the latent slots.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
