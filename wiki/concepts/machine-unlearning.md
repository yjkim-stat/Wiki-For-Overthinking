# machine unlearning

<!-- auto:begin -->

Removing a designated subject's information from a trained model on request, without retraining from scratch. Both sources here make the same argument, that for a reasoning model the target is the trace and not only the answer, and both intervene there rather than on the output. One shows why: a fact successfully unlearned from the final answer is still reproduced in the reasoning trace, and an answer-oriented baseline cuts forget-split classification accuracy from 59.2 to 42.2 percent while subject-level reasoning leakage moves only from 61.6 to 58.3 -- so answer-level and reasoning-level forgetting are separate achievements, and the gap is substantially larger in natively RL-trained models than in their base versions. Its own method is training-free and inference-time, redirecting the trajectory through sanitised image-grounded latent injection. The other reframes unlearning as an intervention on the chain of thought directly, having the model generate logically valid counterfactual traces and iteratively preference-tuning toward them. Both sources also record the failure mode of the gradient-based alternatives: parameter updates aimed at the forget set spill onto retained knowledge, degrading utility and generation quality even on data the model was never asked to forget.

- **Kind**: concept
- **Also called**: unlearning
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [chain of thought](../methods/chain-of-thought.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [component ablation](../methods/component-ablation.md), [degenerate generation](degenerate-generation.md), [entropy collapse](entropy-collapse.md), [Gemini-2.5-pro](../models/gemini-2-5-pro.md), [latent reasoning](latent-reasoning.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [memorization](memorization.md), [monitorability](monitorability.md), [preference optimization](../methods/preference-optimization.md), [Qwen2.5-VL](../models/qwen2-5-vl.md)

## What we have settled

- **Established** — The reasoning trace and the answer are separate information channels: content present in one can be absent from the other in both directions, so nothing about an answer bounds what its trace contains, and no intervention at the answer level has touched the trace until measured there.
  - Three independent sources, in three settings, and the divergence runs both ways. Measured on production traffic: decoding 315,320 reasoning blocks from 6,708 publicly posted agent sessions recovers 704 sensitive artifacts from genuine user sessions, of which 64 appear nowhere in the visible chat history — and the recurring trigger is benign, since asking an agent to anonymise a session makes it re-read the history in hidden reasoning and restate there exactly the values it was asked to remove. Measured under intervention: a multimodal fact successfully unlearned from the final answer is still reproduced in the reasoning trace, and an answer-oriented unlearning baseline cuts forget-split classification accuracy from 59.2% to 42.2% while subject-level reasoning leakage moves only from 61.6% to 58.3% — seventeen points of answer suppression buying three points of trace suppression. The same paper finds the gap substantially larger in natively RL-trained reasoning models than in their non-reasoning base models, so RL post-training widens it. And in the opposite direction: a factuality-alignment paper targets precisely the gap where correct facts appear in the reasoning and fail to reach the answer. Two consequences follow. First, an answer-level edit, filter or unlearning procedure should be assumed not to have reached the trace until leakage is measured there separately, which is a different metric and not a stricter threshold on the same one. Second, sanitising what is visible can populate what is not — so a trace is not a compression, a summary or a subset of the output it accompanies, and reasoning about one from the other is unsound in either direction.

## Appears in

- [LEMUR: Latent Entropy-aware Multimodal Unlearning via Visual-anchored Reasoning Redirection](../../archive/papers/2026/arxiv-2608-11691/summary.md) — Finds that a fact successfully unlearned from a multimodal model's final answer can still be reproduced in its reasoning trace, far more in natively RL-trained models than in their base versions, and uses the token-level entropy signature RL leaves behind as a training-free control signal for redirecting the trace at decoding time.
- [CiPO: Counterfactual Unlearning for Large Reasoning Models through Iterative Preference Optimization](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-143/summary.md) — Reframes unlearning in reasoning models as an intervention on the CoT itself, having the model generate logically valid counterfactual traces and iteratively preference-tuning toward them.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
