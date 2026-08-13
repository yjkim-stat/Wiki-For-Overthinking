# self-verification

<!-- auto:begin -->

A model checking its own work, which the sources place at three different points and which the archive elsewhere finds weak. One makes it explicit and structured, extracting a problem's constraints first and then checking intermediate and final results against that summary — with the reported bottleneck being the extraction step, not the checking. One trains it as a meta-ability on automatically generated self-verifiable tasks rather than waiting for it to emerge. One reads it internally, interpreting the reasoning process at step level with a sparse autoencoder. Set against the archive's finding that the content margin of self-revision is near zero at small-to-mid scale, and that prompting models to self-reflect on named proof failure modes does not fix them, these sources describe an ability that is easier to invoke than to make effective.

- **Kind**: concept
- **Also called**: self-check, self-critique, self-reflection
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [activation patching](../methods/activation-patching.md), [aha moment](aha-moment.md), [AIME](../datasets/aime.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [Brumo](../datasets/brumo.md), [chain of thought](../methods/chain-of-thought.md), [emergent behaviour](emergent-behaviour.md), [GSM8K](../datasets/gsm8k.md), [information bottleneck](information-bottleneck.md), [linear probing](../methods/linear-probing.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH500](../datasets/math500.md), [model merging](../methods/model-merging.md), [monosemanticity](monosemanticity.md), [OlympiadBench](../datasets/olympiadbench.md), [OpenCodeInstruct](../datasets/opencodeinstruct.md), [performance ceiling](performance-ceiling.md), [Qwen2.5-0.5B](../models/qwen2-5-0-5b.md), [routing](routing.md), [self-consistency](../methods/self-consistency.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [superposition](superposition.md), [verification](verification.md)

## Appears in

- [Constraint-First Reasoning: A Training-Free Protocol for Exploiting Answer-Space Constraints in Mathematical Problem Solving](../../archive/papers/2026/arxiv-2608-05254/summary.md) — A training-free two-stage prompting protocol that extracts a problem's answer-space constraints first and then checks its own intermediate and final results against them, routed on by a regex detector.
- [Beyond &apos;Aha!&apos;: Toward Systematic Meta-Abilities Alignment in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1981/summary.md) — Replaces reliance on unpredictable emergent 'aha moments' by explicitly aligning models to deduction, induction and abduction on self-verifiable tasks before domain RL.
- [Step-Level Sparse Autoencoder for Reasoning Process Interpretation](../../archive/papers/2026/local-d9699040f5220b4c/summary.md) — Trains a sparse autoencoder over whole reasoning steps rather than tokens, conditioning both encoder and decoder on the preceding trajectory so the sparse code carries only what the step adds, and shows that step correctness, logicality, length and first token are all linearly decodable from that code.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
