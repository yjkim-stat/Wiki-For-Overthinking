# Llama-3-8B

<!-- auto:begin -->

Meta's 8B-parameter Llama 3 checkpoint, used in this archive as a mid-scale general backbone rather than as a reasoning model: it appears in scaling sweeps alongside Pythia, Mistral-7B and the Llemma pair, in fast/slow-thinking comparisons, and as the largest generator in an edge RAG study where it accounts for roughly 90% of per-query latency and 91% of GPU energy. Sources treat it as the point where generation cost dominates everything else in a pipeline, which is what makes prompt-shortening worth its own overhead there and not at 1B.

- **Kind**: model
- **Also called**: LLaMA3-8B, Llama-3.1-8B, Llama3-8B
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Early Exit](../methods/early-exit.md), [GRPO](../methods/grpo.md), [Llama-3.1-8B](llama-3-1-8b.md), [Llama-3.2-1B](llama-3-2-1b.md), [Mistral 7B](mistral-7b.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5 7B](qwen2-5-7b.md), [reasoning effort](../concepts/reasoning-effort.md), [RLOO](../methods/rloo.md), [SST-2](../datasets/sst-2.md), [T5-Large](../methods/t5-large.md)

## Appears in

- [Disentangling Reasoning Tokens and Boilerplate Tokens For Language Model Fine-tuning](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-1078/summary.md) — SHAD automatically separates a training sample's tokens into 'reasoning' (sample-specific, hard to predict) versus 'boilerplate' (repetitive, format/template) tokens by fine-tuning on a small shuffled-input-output subset and comparing per-token loss before/after, and the resulting Reasoning-highlighted Fine-Tuning (RFT) -- which adaptively up-weights reasoning tokens during agent SFT -- outperforms SFT, regex-based weighting, and two other token-differentiation baselines on held-in and held-out agent benchmarks.
- [Is it Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort](../../archive/papers/2026/title-49c61dced5ecc63a/summary.md) — TRACE detects implicit reward hacking by truncating a model's chain of thought at increasing fractions, forcing an answer at each cut, and scoring the area under the resulting reward-versus-CoT-length curve — a hacking model reaches high reward with little of its reasoning consumed.
- [RAEE: A Robust Retrieval-Augmented Early Exit Framework for Efficient Inference](../../archive/papers/2026/title-5e9b243e4d404cc8/summary.md) — RAEE decides which transformer layer to exit at by retrieving the exit behaviour of similar training examples from a pre-built database, instead of training internal classifiers or using heuristics.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
