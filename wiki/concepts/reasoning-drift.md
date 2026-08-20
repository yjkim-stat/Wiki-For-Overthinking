# reasoning drift

<!-- auto:begin -->

The name both sources give to a long chain of thought moving away from what it should be tracking as it lengthens, and neither defines it operationally or measures it directly. PAMT addresses it by giving each reasoning step a potential -- the teacher-forced log-likelihood of the reference translation under a frozen reference policy, conditioned on the prompt plus the first k steps -- so a step whose potential falls is one that has drifted, with the per-step gain taken as the difference of consecutive potentials. ThinkRetrieve pairs it with error compounding as the failure that in-trace retrieval of complete solved exemplars at every step is meant to arrest, and offers as evidence that in-trace exemplars lower the predictive entropy of the generated answer relative to sequential scaling. The term is used loosely in both: it names the failure a mechanism is aimed at rather than a quantity either paper reports.

- **Kind**: concept
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [advantage estimation](advantage-estimation.md), [AIME 2025](../datasets/aime-2025.md), [budget forcing](../methods/budget-forcing.md), [credit assignment](credit-assignment.md), [decontamination](../methods/decontamination.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-V3](../models/deepseek-v3.md), [dense retrieval](../methods/dense-retrieval.md), [error compounding](error-compounding.md), [GEMBA-MQM](../methods/gemba-mqm.md), [Gemini-2.0-flash](../models/gemini-2-0-flash.md), [GPT-4o](../models/gpt-4o.md), [GPT-5](../models/gpt-5.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [in-context learning](in-context-learning.md), [KL regularization](../methods/kl-regularization.md), [long chain-of-thought distillation](../methods/long-chain-of-thought-distillation.md), [MATH500](../datasets/math500.md), [outcome reward](outcome-reward.md), [predictive entropy](predictive-entropy.md), [process reward](process-reward.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3.5-2B](../models/qwen3-5-2b.md), [Qwen3-8B](../models/qwen3-8b.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [reward shaping](../methods/reward-shaping.md), [SciQ](../datasets/sciq.md), [self-reflection](../methods/self-reflection.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [teacher forcing](../methods/teacher-forcing.md), [test-time scaling](test-time-scaling.md), [WMT22](../datasets/wmt22.md)

## Appears in

- [PAMT: Process-Aligned Reinforcement Learning for Multi-Domain Machine Translation](../../archive/papers/2026/arxiv-2608-03077/summary.md) — Scores each reasoning step of a translation by how much appending it raises a frozen reference model's teacher-forced likelihood of the gold translation, and adds that as a dense per-step reward on top of sequence-level quality — after first establishing that explicit reasoning helps long and hard inputs while drifting on terminology and style.
- [ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling](../../archive/papers/2026/arxiv-2608-10928/summary.md) — Injects a retrieved solved problem, with its full worked solution, into the middle of a reasoning model's own thinking trace at each step boundary, using the model's current intermediate answer as the retrieval query.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
