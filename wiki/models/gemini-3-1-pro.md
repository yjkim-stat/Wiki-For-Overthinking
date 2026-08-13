# Gemini-3.1-Pro

<!-- auto:begin -->

A frontier proprietary model, appearing in both sources as the capable outside system a pipeline depends on rather than as a subject. One uses it as both rubric generator and judge for an RL training loop and reports the dependency as load-bearing: substituting a weaker audio model drops performance on all three benchmarks, in the paper's own words below the vanilla GRPO baseline. The other evaluates it in a large-scale study of judge reliability. Read together they mark a hazard the archive should track — a method whose signal comes from a model the authors neither control nor release is only reproducible while that model is available and unchanged.

- **Kind**: model
- **Also called**: Gemini 3.1 Pro
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [abstention](../concepts/abstention.md), [advantage estimation](../concepts/advantage-estimation.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Claude-3.7-Sonnet](claude-3-7-sonnet.md), [construct validity](../concepts/construct-validity.md), [counterfactual intervention](../methods/counterfactual-intervention.md), [Gemini-1.5-Pro](gemini-1-5-pro.md), [Gemini-2.5-Flash](gemini-2-5-flash.md), [GPT-4o](gpt-4o.md), [GPT-5.5](gpt-5-5.md), [grounding](../concepts/grounding.md), [GRPO](../methods/grpo.md), [Kimi-K2.5](kimi-k2-5.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [meta-evaluation](../concepts/meta-evaluation.md), [MT-Bench](../datasets/mt-bench.md), [multi-hop reasoning](../concepts/multi-hop-reasoning.md), [outcome reward](../concepts/outcome-reward.md), [overthinking](../concepts/overthinking.md), [process reward](../concepts/process-reward.md), [Qwen3-8B](qwen3-8b.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [reward hacking](../concepts/reward-hacking.md), [RLVR](../methods/rlvr.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [synthetic data generation](../methods/synthetic-data-generation.md), [traceability](../concepts/traceability.md)

## Appears in

- [Reinforcement Learning with Evolving Rubrics as Rewards for Audio Reasoning](../../archive/papers/2026/arxiv-2608-02831/summary.md) — Supervises audio reasoning with per-question rubrics generated from the raw waveform, and keeps the signal alive as the policy improves by regenerating the rubrics from the model's own rollouts each step and pruning any criterion that every rollout satisfies or none does.
- [DocTrace: Towards Traceable Long Document VQA via Hierarchical Evidence Graph Reasoning](../../archive/papers/2026/arxiv-2608-03292/summary.md) — Recasts long-document visual question answering as building an explicit evidence graph whose nodes are grounded document blocks and whose edges are reasoning dependencies, and verifies the graph causally — masking the evidence it cites flips 82.8% of correct answers while masking uncited evidence changes 9.6%.
- [Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias](../../archive/papers/2026/local-504cc53656b06ab4/summary.md) — Evaluates 21 LLM judges across three benchmarks and three protocols over ~541,000 judgments, and shows the field's standard validation metric — exact-match agreement — overstates chance-corrected discrimination by 34-41 points universally, while high test-retest reliability can coexist with severe position bias.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
