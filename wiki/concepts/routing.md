# routing

<!-- auto:begin -->

Deciding per input which of several processing paths to take, rather than applying one procedure uniformly. One source routes on a text-only regex detector of restrictive cues, activating a two-stage constraint-extraction protocol only where constraints exist to exploit and falling back to direct chain-of-thought otherwise. The other routes at every generation step among a fast path, a slow perception path and a slow reasoning path, with the router trained by multi-objective RL on roughly 790k samples of teacher-attributed perception-versus-reasoning failures. The pair spans the design range: a hand-written detector applied once per problem, and a learned controller applied at each step.

- **Kind**: concept
- **Also called**: dispatch, gating, path selection
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [adversarial robustness](adversarial-robustness.md), [AIME](../datasets/aime.md), [Brumo](../datasets/brumo.md), [calibration](../methods/calibration.md), [chain of thought](../methods/chain-of-thought.md), [CMIMC](../datasets/cmimc.md), [cosine similarity](../methods/cosine-similarity.md), [GPT-4o](../models/gpt-4o.md), [GPT-5](../models/gpt-5.md), [GSM8K](../datasets/gsm8k.md), [hidden-state geometry](hidden-state-geometry.md), [HumanEval+](../datasets/humaneval.md), [linear probe](../methods/linear-probe.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH500](../datasets/math500.md), [meta-reasoning](../methods/meta-reasoning.md), [MMLU](../datasets/mmlu.md), [OlympiadBench](../datasets/olympiadbench.md), [out-of-distribution generalization](out-of-distribution-generalization.md), [overthinking](overthinking.md), [perception bottleneck](perception-bottleneck.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [sample complexity](sample-complexity.md), [self-correction](self-correction.md), [self-verification](self-verification.md), [superposition](superposition.md), [test-time compute](test-time-compute.md), [uncertainty quantification](uncertainty-quantification.md), [verification](verification.md)

## Appears in

- [Training-Free versus Training-Based Intent Classification in LLMs: Accuracy, Robustness, and Failure Modes](../../archive/papers/2026/arxiv-2608-02415/summary.md) — Compares two training-free intent classifiers built from summary statistics of prefill-time activations against trained heads on the same features, and finds the trade-off is not accuracy but where each fails — trained heads win fine-grained distinctions, statistical ones give better uncertainty on mixed prompts and survive adversarial rephrasing that collapses the trained heads to zero.
- [Constraint-First Reasoning: A Training-Free Protocol for Exploiting Answer-Space Constraints in Mathematical Problem Solving](../../archive/papers/2026/arxiv-2608-05254/summary.md) — A training-free two-stage prompting protocol that extracts a problem's answer-space constraints first and then checks its own intermediate and final results against them, routed on by a regex detector.
- [Addressing Overthinking in Large Vision-Language Models via Gated Perception-Reasoning Optimization](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-215/summary.md) — Routes each generation step among a fast path, a perception re-examination path and a self-reflection path, trained on 790k samples of teacher-attributed perception-versus-reasoning failures.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
