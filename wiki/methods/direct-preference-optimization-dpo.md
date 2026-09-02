# Direct Preference Optimization (DPO)

<!-- auto:begin -->

Direct Preference Optimization (DPO) is used across these sources as the training objective for turning selected pairs of reasoning traces (e.g. a Pareto-dominant short path vs. a longer one, or a self-pruned trace vs. its original) into a fine-tuning signal that biases a model toward the preferred trace. ChainPrune builds DPO preference data from tree-merged reasoning paths plus an added NLL term; EconProver uses DPO-trained dynamic CoT-mode switching; SGP-CoT applies preference optimization to self-pruned traces identified via the model's own likelihood signals.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Claude-3.7-Sonnet](../models/claude-3-7-sonnet.md), [DAST](dast.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-o1](../models/gpt-o1.md), [GSM8K](../datasets/gsm8k.md), [LC-R1 (baseline)](lc-r1-baseline.md), [LLM-as-a-Judge](llm-as-a-judge.md), [LogiQA](../datasets/logiqa.md), [MATH500](../datasets/math500.md), [MedQA](../datasets/medqa.md), [Overthinking](../concepts/overthinking.md), [Redundant Reasoning Steps](../concepts/redundant-reasoning-steps.md), [SimPO](simpo.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md)

## Appears in

- [ChainPrune: Evaluating and Reducing Redundancy in Long Chain-of-Thought Reasoning](../../archive/papers/2026/arxiv-2608-21860/summary.md) — ChainPrune merges semantically equivalent steps from 16 sampled reasoning paths into a tree, picks Pareto-dominant short paths as DPO preference data, and fine-tunes with an added NLL term, cutting tokens 28.1% and reasoning steps 26.8% on two R1-distilled models without losing accuracy.
- [EconProver: Towards More Economical Test-Time Scaling for Automated Theorem Proving](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2121/summary.md) — EconRL identifies substantial token-level inefficiency in state-of-the-art automated theorem provers' test-time scaling (sequential reflective CoT vs. parallel sampling) and fixes it with two combined RL techniques -- DPO-trained dynamic CoT-mode switching and difficulty-partitioned diverse-prefix parallel scaling -- so EconProver-GD matches Goedel-Prover-V2-8B's full-CoT accuracy on miniF2F using only 12% of the sampling cost.
- [Your Reasoning Model Knows What Counts: Self-Guided Chain-of-Thought Pruning for Efficient Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-25/summary.md) — SGP-CoT identifies which reasoning units a model can safely drop using only its own intrinsic likelihood signals (counterfactual answer-impact and coherence-impact scores, no external verifier or curated data), then trains the model via preference optimization on self-pruned traces, cutting reasoning length 15-50% across five model families while preserving or improving accuracy -- and shows pruning by a different model consistently degrades accuracy more than self-pruning.
- [Correct Reasoning Paths Visit Shared Decision Pivots](../../archive/papers/2026/local-f8a4b161736737f2/summary.md) — Proposes that correct chain-of-thought paths for a given question converge on a small shared set of verifiable 'decision pivots', and builds a self-training pipeline that intersects multiple sampled correct paths into a compact pivot-focused reasoning trace used as the preferred completion for DPO, improving accuracy on LogiQA, MedQA and MATH500 over prior self-training baselines while also shortening generated reasoning as a side effect.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
