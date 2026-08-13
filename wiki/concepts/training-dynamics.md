# training dynamics

<!-- auto:begin -->

How a model's behaviour changes over the course of training, as distinct from what it ends up being able to do. One source makes it one of three organizing dimensions for mechanistic findings about reasoning models, alongside reasoning mechanisms and unintended behaviours. The other uses dynamics operationally rather than descriptively, reweighting training objectives online from short-horizon signals of convergence and instability so that focus shifts away from saturated objectives toward underperforming or volatile ones. The second shows why the first matters: if the mixture should adapt to observed dynamics, then dynamics are a control input and not only an object of study.

- **Kind**: concept
- **Also called**: learning dynamics, optimization dynamics
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [attention analysis](../methods/attention-analysis.md), [benchmark contamination](benchmark-contamination.md), [catastrophic forgetting](catastrophic-forgetting.md), [chain of thought](../methods/chain-of-thought.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [circuit complexity](circuit-complexity.md), [DAPO](../methods/dapo.md), [DAPO-Qwen-32B](../models/dapo-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [emergent behaviour](emergent-behaviour.md), [expressivity-learnability gap](expressivity-learnability-gap.md), [gradient descent analysis](../methods/gradient-descent-analysis.md), [GRPO](../methods/grpo.md), [judge reliability](judge-reliability.md), [KL regularization](../methods/kl-regularization.md), [length generalization](length-generalization.md), [literature survey](../methods/literature-survey.md), [LiveCodeBench](../datasets/livecodebench.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH-500](../datasets/math-500.md), [mechanistic interpretability](mechanistic-interpretability.md), [Minerva](../datasets/minerva.md), [pass-k](../methods/pass-k.md), [process evaluation](../methods/process-evaluation.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [reasoning boundary](reasoning-boundary.md), [RLVR](../methods/rlvr.md), [self-training](self-training.md), [state tracking](state-tracking.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [verification](verification.md)

## Appears in

- [Towards a Mechanistic Understanding of Large Reasoning Models: A Survey of Training, Inference, and Failures](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-889/summary.md) — A survey organizing mechanistic findings about reasoning models into training dynamics, reasoning mechanisms and unintended behaviours, and arguing the field needs a unified theoretical framework.
- [Beyond Reasoning Gains: Mitigating General-Capability Forgetting in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1717/summary.md) — Confirms that prolonged RLVR makes models forget foundational skills, and counters it with experience replay whose objective weights adapt online to convergence and instability signals.
- [Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs](../../archive/papers/2025/local-fb100130d8c7c2bd/summary.md) — Shows that base models win pass@K on mathematics by producing wrong chains that land on right answers, and that scoring the chain too — CoT-Pass@K — reverses the verdict in RLVR's favour at every K.
- [Transformers Provably Learn Chain-of-Thought Reasoning with Length Generalization](../../archive/papers/2025/local-fe69869b0e362891/summary.md) — Gives the first optimization guarantee that gradient descent trains constant-depth transformers to solve NC1-complete problems with chain of thought, and shows the algebraic structure of the task decides how far the learned reasoning extrapolates.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
