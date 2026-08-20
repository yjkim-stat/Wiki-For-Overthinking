# Jensen-Shannon divergence

<!-- auto:begin -->

A symmetric, bounded divergence between two distributions, measuring each against their mixture. The two sources here use it for opposite purposes and reach opposite verdicts, which is the whole of what the archive knows about it. As a distillation objective it fails: the unsupervised self-distillation work sweeps divergences under pseudo-labels and finds symmetric JSD costing 13.8 percent and landing level with the untrained model, against forward KL's 57.10 average -- symmetry buying nothing where the teacher is the thing being trusted. As a token-selection criterion it works: the distributional-deviation work argues Shannon entropy is the wrong signal for choosing which tokens to train on in verifiable-reward RL, and selects instead the top ten percent of tokens by the JSD of their logit distribution from the group average, so what is trained is where a rollout departs from its siblings rather than where the model is merely uncertain. The distinction worth carrying is between using a divergence as a loss and using it as a measurement.

- **Kind**: method
- **Also called**: JSD
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [consensus](../concepts/consensus.md), [degenerate generation](../concepts/degenerate-generation.md), [entropy collapse](../concepts/entropy-collapse.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [format compliance](../concepts/format-compliance.md), [forward KL divergence](forward-kl-divergence.md), [GPQA](../datasets/gpqa.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [HMMT 2025](../datasets/hmmt-2025.md), [knowledge distillation](knowledge-distillation.md), [majority voting](majority-voting.md), [MATH500](../datasets/math500.md), [MMLU-STEM](../datasets/mmlu-stem.md), [on-policy distillation](on-policy-distillation.md), [pass@k](../concepts/pass-k.md), [privileged information](../concepts/privileged-information.md), [Qwen2.5-0.5B](../models/qwen2-5-0-5b.md), [Qwen2.5-1.5B](../models/qwen2-5-1-5b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-4B-Instruct-2507](../models/qwen3-4b-instruct-2507.md), [Qwen3-8B](../models/qwen3-8b.md), [reverse KL divergence](reverse-kl-divergence.md), [RLVR](rlvr.md), [self-consistency](self-consistency.md), [supervised fine-tuning](supervised-fine-tuning.md), [teacher-student gap](../concepts/teacher-student-gap.md), [token-level entropy](../concepts/token-level-entropy.md), [top-k truncation](top-k-truncation.md), [VeRL](verl.md)

## Appears in

- [On-Policy Self-Distillation without Any Supervision](../../archive/papers/2026/arxiv-2608-06296/summary.md) — Removes external supervision from on-policy self-distillation by building a pseudo-solution from the model's own majority vote and using it as privileged teacher context rather than as a scalar reward, then distilling only on the completions that disagree with it.
- [Beyond Entropy: Learning from Token-Level Distributional Deviations for LLM Reasoning](../../archive/papers/2026/local-2175408b166d313f/summary.md) — Argues that Shannon entropy is the wrong criterion for picking which tokens to train on in RLVR, and selects tokens instead by the Jensen-Shannon divergence of their logit distribution from the group average, updating only the top 10% of these 'unique' tokens.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
