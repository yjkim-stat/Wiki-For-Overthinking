# commitment boundary

<!-- auto:begin -->

The point in a reasoning trace after which the answer is effectively fixed, so that continued reasoning no longer changes it. One source establishes it by truncating the trace at each step and forcing an answer, finding the transition is sharp and single-step rather than gradual. The other applies the same logic to sycophancy, using counterfactual rollouts to locate the sentences that commit a model to agreeing with an incorrect user suggestion, and shows those positions are detectable from activations at 74-85% balanced accuracy — beating text-only baselines specifically at high commitment, meaning strong commitments are the ones not visible in the words. The concept matters because it separates reasoning that determines the answer from reasoning that follows it.

- **Kind**: concept
- **Also called**: commitment point, point of no return, sycophantic anchor
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME25](../datasets/aime25.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [early exit](../methods/early-exit.md), [Gemma-4-26B-A4B-it](../models/gemma-4-26b-a4b-it.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-OSS-20B](../models/gpt-oss-20b.md), [linear probe](../methods/linear-probe.md), [linear probing](../methods/linear-probing.md), [Llama](../models/llama.md), [localization](localization.md), [MATH500](../datasets/math500.md), [monitorability](monitorability.md), [overthinking](overthinking.md), [Qwen](../models/qwen.md), [Qwen3-14B](../models/qwen3-14b.md), [reasoning redundancy](reasoning-redundancy.md), [reasoning trajectory](reasoning-trajectory.md), [sycophancy](sycophancy.md), [ZebraLogic](../datasets/zebralogic.md)

## Appears in

- [Sycophantic Anchors: Localizing and Quantifying User Agreement in Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-srw-20/summary.md) — Locates the sentences in a reasoning trace that commit a model to agreeing with an incorrect user suggestion, using counterfactual rollouts and linear probes.
- [Beyond the Commitment Boundary: Probing Epiphenomenal Chain-of-Thought in Large Reasoning Models](../../archive/papers/2026/local-d6e266929de37684/summary.md) — Measures each CoT step's causal contribution by truncating the trace and forcing an answer, finds reasoning crosses a sharp single-step 'commitment boundary' after which the answer probability stops moving, and trains activation probes to detect that boundary and exit early.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
