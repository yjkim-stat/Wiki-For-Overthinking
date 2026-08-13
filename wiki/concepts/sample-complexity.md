# sample complexity

<!-- auto:begin -->

How many training examples suffice to learn a target to a given accuracy, and the archive's measure of what reasoning supervision costs statistically. The sources agree the news is good and arrive at it differently. One bounds it parametrically through the VC dimension of transformers, finding chain-of-thought learning by teacher forcing costs O(LW log((T+T')W)) — so input length and the number of reasoning steps enter only inside a logarithm, and only through their sum. One bounds it by the target's Fourier structure via PAC-Bayes, where CoT turns Parity's dependence from exponential to linear in reasoning length. One shows the efficiency survives internalization, with implicit CoT learning k-parity from polynomially many samples. The common conclusion is that long reasoning chains are not statistically expensive; whatever they cost is compute or annotation.

- **Kind**: concept
- **Also called**: example complexity, statistical complexity
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [adversarial robustness](adversarial-robustness.md), [calibration](../methods/calibration.md), [chain of thought](../methods/chain-of-thought.md), [cosine similarity](../methods/cosine-similarity.md), [curriculum learning](curriculum-learning.md), [effective depth](effective-depth.md), [expressivity-learnability gap](expressivity-learnability-gap.md), [generalization](generalization.md), [GPT-4o](../models/gpt-4o.md), [GPT-5](../models/gpt-5.md), [gradient descent analysis](../methods/gradient-descent-analysis.md), [GSM8K](../datasets/gsm8k.md), [hidden-state geometry](hidden-state-geometry.md), [HumanEval+](../datasets/humaneval.md), [implicit chain of thought](implicit-chain-of-thought.md), [implicit reasoning](implicit-reasoning.md), [latent reasoning](latent-reasoning.md), [linear probe](../methods/linear-probe.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH500](../datasets/math500.md), [mechanistic interpretability](mechanistic-interpretability.md), [MMLU](../datasets/mmlu.md), [out-of-distribution generalization](out-of-distribution-generalization.md), [parity](../datasets/parity.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [RoBERTa](../models/roberta.md), [routing](routing.md), [superposition](superposition.md), [teacher forcing](../methods/teacher-forcing.md), [test-time compute](test-time-compute.md), [uncertainty quantification](uncertainty-quantification.md)

## Appears in

- [Training-Free versus Training-Based Intent Classification in LLMs: Accuracy, Robustness, and Failure Modes](../../archive/papers/2026/arxiv-2608-02415/summary.md) — Compares two training-free intent classifiers built from summary statistics of prefill-time activations against trained heads on the same features, and finds the trade-off is not accuracy but where each fails — trained heads win fine-grained distinctions, statistical ones give better uncertainty on mixed prompts and survive adversarial rephrasing that collapses the trained heads to zero.
- [A Sharper Picture of Generalization in Transformers](../../archive/papers/2026/local-03f1eff4f1d40725/summary.md) — Derives a non-vacuous PAC-Bayes generalization bound for transformers on boolean functions in terms of Fourier sparsity and degree, and uses it to show chain of thought turns an exponential dependence on reasoning length into a linear one for Parity.
- [Tight Sample Complexity of Transformers](../../archive/papers/2026/local-209065fd89f43691/summary.md) — Pins down the VC dimension of transformers as depth times parameters times a logarithm, and shows chain-of-thought learning by teacher forcing costs only logarithmically more as the number of reasoning steps grows.
- [Transformers Provably Learn to Internalize Chain-of-Thought](../../archive/papers/2026/local-ee30f023d9f2d8fb/summary.md) — Proves that reasoning can be moved from emitted tokens into hidden states without losing sample efficiency, using a curriculum that deletes thinking tokens in geometric chunks and so needs only logarithmically many training stages.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
