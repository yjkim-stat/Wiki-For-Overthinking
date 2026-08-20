# importance sampling

<!-- auto:begin -->

Reweighting by the ratio of a new policy's probability to an old one's, the mechanism that lets a policy-gradient method reuse rollouts across several updates. Across 3 sources its consequences here are mostly indirect. It is identified, together with clipping, as the cause of post-training concealing benchmark contamination -- which makes the concealment a property of a broad class of reinforcement-learning methods rather than of any one algorithm. It appears in a convergence analysis of softmax policy gradient under linear function approximation. And the archive's related material shows its ratio being multiplied into a shaping term as a magnitude, so that a local signal reweights rather than overrides the trajectory-level advantage.

- **Kind**: method
- **Also called**: importance ratio, importance sampling ratio
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [activation patching](activation-patching.md), [activation steering](activation-steering.md), [AIME 2024](../datasets/aime-2024.md), [ARC-Easy](../datasets/arc-easy.md), [benchmark contamination](../concepts/benchmark-contamination.md), [circuit analysis](circuit-analysis.md), [construct validity](../concepts/construct-validity.md), [detection versus control](../concepts/detection-versus-control.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-2](../models/gpt-2.md), [GPT-2 XL](../models/gpt-2-xl.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [KL divergence](kl-divergence.md), [knowledge distillation](knowledge-distillation.md), [linear function approximation](linear-function-approximation.md), [linear probe](linear-probe.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.3-70B](../models/llama-3-3-70b.md), [log-linear policy](../concepts/log-linear-policy.md), [logit lens](logit-lens.md), [LoRA](lora.md), [low-rank approximation](low-rank-approximation.md), [MATH500](../datasets/math500.md), [membership inference](../concepts/membership-inference.md), [memorization](../concepts/memorization.md), [natural policy gradient](natural-policy-gradient.md), [policy gradient](policy-gradient.md), [PPO](ppo.md), [REINFORCE](reinforce.md), [residual stream](../concepts/residual-stream.md), [RLVR](rlvr.md), [SciQ](../datasets/sciq.md), [softmax policy](../concepts/softmax-policy.md), [sparse autoencoder](sparse-autoencoder.md), [supervised fine-tuning](supervised-fine-tuning.md), [tabular softmax parameterization](../concepts/tabular-softmax-parameterization.md), [the Pile](../datasets/the-pile.md), [tuned lens](tuned-lens.md), [WikiText-2](../datasets/wikitext-2.md)

## Appears in

- [Interpreting Language Model Hidden States at Scale](../../archive/papers/2026/arxiv-2608-10260/summary.md) — Makes trained lenses cheap enough to attach densely across a whole model — every layer, and residual, attention and MLP alike — and then uses that coverage to show that where a behaviour is most visible is not where intervening on it works best.
- [On The Fragility of Benchmark Contamination Detection in Reasoning Models](../../archive/papers/2026/local-4cf1061e50d8b3c3/summary.md) — Shows that benchmark contamination in reasoning models is alarmingly easy to hide: a brief round of GRPO erases the signals contamination detectors rely on, and PPO-style importance sampling and clipping are identified as the cause — implying a broad class of RL methods conceals contamination inherently.
- [Rethinking the Global Convergence of Softmax Policy Gradient with Linear Function Approximation](../../archive/papers/2025/local-8458ce24c9e6b3b5/summary.md) — Shows by two four-armed bandits with nearly identical approximation error, one of which converges and one of which does not, that approximation error cannot characterize whether softmax policy gradient reaches the optimum, and replaces it with a condition on whether the features preserve the ordering of the rewards.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
