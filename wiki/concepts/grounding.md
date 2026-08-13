# grounding

<!-- auto:begin -->

Tying a claim or a reasoning step to the specific evidence that supports it, and in both sources something a method is built to enforce rather than to measure. One generates per-question criteria directly from the raw waveform rather than from a transcript, so each criterion is anchored to acoustic evidence actually present in the clip, and prunes any criterion whose verdict does not vary across a rollout group. The other constructs an explicit graph whose nodes are document blocks and whose edges are reasoning dependencies, then tests the grounding causally: masking the evidence the graph cites flips 82.8% of originally correct answers while masking uncited evidence changes 9.6%. That counterfactual pairing is the stronger of the two demonstrations and is the form the archive should ask for — a grounding claim that is not checked by masking is a claim about annotation rather than about dependence.

- **Kind**: concept
- **Also called**: evidence grounding
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [abstention](abstention.md), [advantage estimation](advantage-estimation.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Claude-3.7-Sonnet](../models/claude-3-7-sonnet.md), [counterfactual intervention](../methods/counterfactual-intervention.md), [Gemini-1.5-Pro](../models/gemini-1-5-pro.md), [Gemini-3.1-Pro](../models/gemini-3-1-pro.md), [GPT-4o](../models/gpt-4o.md), [GPT-5.5](../models/gpt-5-5.md), [GRPO](../methods/grpo.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [multi-hop reasoning](multi-hop-reasoning.md), [outcome reward](outcome-reward.md), [overthinking](overthinking.md), [process reward](process-reward.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [reward hacking](reward-hacking.md), [RLVR](../methods/rlvr.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [synthetic data generation](../methods/synthetic-data-generation.md), [traceability](traceability.md)

## Appears in

- [Reinforcement Learning with Evolving Rubrics as Rewards for Audio Reasoning](../../archive/papers/2026/arxiv-2608-02831/summary.md) — Supervises audio reasoning with per-question rubrics generated from the raw waveform, and keeps the signal alive as the policy improves by regenerating the rubrics from the model's own rollouts each step and pruning any criterion that every rollout satisfies or none does.
- [DocTrace: Towards Traceable Long Document VQA via Hierarchical Evidence Graph Reasoning](../../archive/papers/2026/arxiv-2608-03292/summary.md) — Recasts long-document visual question answering as building an explicit evidence graph whose nodes are grounded document blocks and whose edges are reasoning dependencies, and verifies the graph causally — masking the evidence it cites flips 82.8% of correct answers while masking uncited evidence changes 9.6%.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
