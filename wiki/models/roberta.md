# RoBERTa

<!-- auto:begin -->

An encoder-only pretrained language model that appears in this archive as the fine-tuned baseline newer methods are measured against, and which they do not always beat. In ReLIT's comparison a fine-tuned RoBERTa scores 90.02 on NaN-NLI, the strongest entry in that table, against 55.20 for ReLIT itself and 71.55 for the strongest listed reasoning model -- so on that natural-language-inference set a task-specific encoder remains ahead of both recursive latent reasoning and large reasoning LLMs. The intent-classification study uses an end-to-end fine-tuned RoBERTa as one of its training-based baselines, against training-free classifiers computed from activations already produced during prefill. Neither source studies the model itself; both use it to mark what task-specific supervised training already achieves.

- **Kind**: model
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [adversarial robustness](../concepts/adversarial-robustness.md), [annotation agreement](../concepts/annotation-agreement.md), [answer stabilization](../concepts/answer-stabilization.md), [calibration](../methods/calibration.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Claude-Sonnet-4](claude-sonnet-4.md), [Coconut](../methods/coconut.md), [cosine similarity](../methods/cosine-similarity.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [few-shot prompting](../methods/few-shot-prompting.md), [GPT-4](gpt-4.md), [GPT-4o](gpt-4o.md), [GPT-5](gpt-5.md), [GSM8K](../datasets/gsm8k.md), [hidden-state geometry](../concepts/hidden-state-geometry.md), [human evaluation](../methods/human-evaluation.md), [HumanEval+](../datasets/humaneval.md), [implicit chain of thought](../concepts/implicit-chain-of-thought.md), [in-context learning](../concepts/in-context-learning.md), [latent reasoning](../concepts/latent-reasoning.md), [linear probe](../methods/linear-probe.md), [Llama-3.1-70B](llama-3-1-70b.md), [Llama-3.2-1B](llama-3-2-1b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [o1-mini](o1-mini.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [ProofWriter](../datasets/proofwriter.md), [Qwen3-1.7B](qwen3-1-7b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-8B](qwen3-8b.md), [QwQ-32B](qwq-32b.md), [recurrent depth](../concepts/recurrent-depth.md), [routing](../concepts/routing.md), [sample complexity](../concepts/sample-complexity.md), [superposition](../concepts/superposition.md), [Tree of Thoughts](../methods/tree-of-thoughts.md), [uncertainty quantification](../concepts/uncertainty-quantification.md), [zero-shot prompting](../methods/zero-shot-prompting.md)

## Appears in

- [Training-Free versus Training-Based Intent Classification in LLMs: Accuracy, Robustness, and Failure Modes](../../archive/papers/2026/arxiv-2608-02415/summary.md) — Compares two training-free intent classifiers built from summary statistics of prefill-time activations against trained heads on the same features, and finds the trade-off is not accuracy but where each fails — trained heads win fine-grained distinctions, statistical ones give better uncertainty on mixed prompts and survive adversarial rephrasing that collapses the trained heads to zero.
- [Think Deep, Speak Once: Relit, A Recursive Latent Implicit Transformer Framework](../../archive/papers/2026/arxiv-2608-08113/summary.md) — Bolts a small trainable recurrent block between a frozen 1.1B language model's body and its output head, so reasoning happens as repeated refinement of two latent vectors rather than as generated tokens.
- [PROSLEX: A Novel Dataset for Expert-Annotated Legal Statute Prediction for Indian Judiciary](../../archive/papers/2026/arxiv-2608-08830/summary.md) — Builds an expert-annotated Indian Supreme Court dataset in which each applicable statute is paired with the specific text span a legal expert says establishes it, and uses it to show that predicting the right statute and giving the right reason are separable abilities.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
