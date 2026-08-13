# teacher forcing

<!-- auto:begin -->

Training a model on ground-truth prefixes rather than on its own generations. The sources treat it from opposite ends. One prices it: selecting a predictor consistent with the entire chain of thought on the training data learns with sample complexity logarithmic in the combined input and reasoning length, with a matching lower bound, so no other rule using chain data does fundamentally better. The other names it as the thing to move away from, arguing that the teacher-forced objective underlying next-token prediction is ill-suited to long-horizon reasoning and planning and proposing latent auxiliary targets instead. Statistically cheap and, by the second account, structurally limited.

- **Kind**: method
- **Also called**: teacher-forced training
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [belief state](../concepts/belief-state.md), [chain of thought](chain-of-thought.md), [compounding error](../concepts/compounding-error.md), [credit assignment](../concepts/credit-assignment.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-V3](../models/deepseek-v3.md), [expressivity-learnability gap](../concepts/expressivity-learnability-gap.md), [GEMBA-MQM](gemba-mqm.md), [Gemini-2.0-flash](../models/gemini-2-0-flash.md), [generalization](../concepts/generalization.md), [GPT-4o](../models/gpt-4o.md), [GPT-5](../models/gpt-5.md), [GRPO](grpo.md), [implicit reasoning](../concepts/implicit-reasoning.md), [KL regularization](kl-regularization.md), [latent reasoning](../concepts/latent-reasoning.md), [long chain-of-thought distillation](long-chain-of-thought-distillation.md), [outcome reward](../concepts/outcome-reward.md), [process reward](../concepts/process-reward.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [reasoning drift](../concepts/reasoning-drift.md), [reward shaping](../concepts/reward-shaping.md), [sample complexity](../concepts/sample-complexity.md), [speculative decoding](speculative-decoding.md), [supervised fine-tuning](supervised-fine-tuning.md), [WMT22](../datasets/wmt22.md)

## Appears in

- [PAMT: Process-Aligned Reinforcement Learning for Multi-Domain Machine Translation](../../archive/papers/2026/arxiv-2608-03077/summary.md) — Scores each reasoning step of a translation by how much appending it raises a frozen reference model's teacher-forced likelihood of the gold translation, and adds that as a dense per-step reward on top of sequence-level quality — after first establishing that explicit reasoning helps long and hard inputs while drifting on terminology and style.
- [Hierarchical Latent Prediction for Language Models](../../archive/papers/2026/arxiv-2608-05806/summary.md) — Adds a higher-level abstract latent as an auxiliary pretraining target to reduce compounding error in latent-space rollouts, aiming at longer-horizon coherence than multi-token or next-latent prediction.
- [Tight Sample Complexity of Transformers](../../archive/papers/2026/local-209065fd89f43691/summary.md) — Pins down the VC dimension of transformers as depth times parameters times a logarithm, and shows chain-of-thought learning by teacher forcing costs only logarithmically more as the number of reasoning steps grows.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
