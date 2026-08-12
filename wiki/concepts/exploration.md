# exploration

<!-- auto:begin -->

Deliberately injected stochasticity that lets policy optimization sample outside what the current policy would produce deterministically. Neither source treats it as free, and both make the form and placement of the noise the design problem rather than its amount. One injects Gumbel noise into the logits that form a continuous latent thought, so exploration is the mechanism by which two latent thoughts for the same prompt differ at all, and reports that removing it costs 2.12 points on GSM8K and 1.70 on MATH. The other observes that a flow model is sampled by a deterministic ODE at deployment while online RL needs stochastic rollouts, so the usual remedy of swapping in an SDE during training makes the optimized samples diverge from the ones the deployed sampler produces — and blur further as the exploration noise rises. Exploration in these sources is therefore something bought at the cost of agreement between training and inference.

- **Kind**: concept
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [advantage estimation](advantage-estimation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [credit assignment](credit-assignment.md), [DAPO-Math-17k](../datasets/dapo-math-17k.md), [data efficiency](data-efficiency.md), [entropy collapse](entropy-collapse.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [latent reasoning](latent-reasoning.md), [MATH](../datasets/math.md), [MATH-500](../datasets/math-500.md), [MMLU-STEM](../datasets/mmlu-stem.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [policy entropy](policy-entropy.md), [post-hoc rationalization](post-hoc-rationalization.md), [privileged information](privileged-information.md), [REINFORCE](../methods/reinforce.md), [reward sparsity](reward-sparsity.md), [soft thinking](../methods/soft-thinking.md), [train-inference gap](train-inference-gap.md)

## Appears in

- [Latent Thought Credit: Multi-Answer Credit Assignment for Latent Reasoning](../../archive/papers/2026/arxiv-2608-01593/summary.md) — Estimates what a continuous latent thought is worth by freezing the context after it and averaging the rewards of several answers sampled from that fixed context, then credits latent positions with the resulting thought-level advantage and answer positions with the ordinary group-relative one.
- [Self-Improving Large Language Models via Progressive Experience Evolution](../../archive/papers/2026/arxiv-2608-02139/summary.md) — Inserts a stage before RL in which the model extracts textual lessons from its own successful and failed rollouts, filters them by measured marginal utility on a held-out probe set, and distills the surviving pool into its own weights — so that GRPO starts from a policy that fails all-eight-samples less often.
- [LC-GRPO: Bridging Train-Inference Gap for Flow-Based GRPO with Langevin Correction](../../archive/papers/2026/arxiv-2608-05600/summary.md) — A GRPO variant for flow-based generative models that replaces SDE training rollouts with an ODE step plus a Langevin correction, aligning training samples with the deterministic sampler used at test time.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
