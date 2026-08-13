# Game of 24

<!-- auto:begin -->

A puzzle requiring four numbers to be combined with arithmetic operations to reach 24, used as the search-shaped task in this archive. It is where tree search shows its most dramatic result — 4% for chain-of-thought against 74% for Tree of Thoughts with GPT-4 — and where representation-based diversity selection shows its largest gain, a 3x improvement in verifier efficiency on the hardest questions. Both are cases where the benefit comes from covering a solution space rather than from computing more carefully, which is what makes the task useful as a contrast to mathematics benchmarks.

- **Kind**: dataset
- **Also called**: Game of 24, Game-of-24
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME24](aime24.md), [AIME25](aime25.md), [backtracking](../concepts/backtracking.md), [best-of-n](../methods/best-of-n.md), [chain of thought](../methods/chain-of-thought.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [GPT-4](../models/gpt-4.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [MATH](math.md), [MBPP+](mbpp.md), [Mistral-7B](../models/mistral-7b.md), [pass@k](../methods/pass-k.md), [Phi-4](../models/phi-4.md), [policy entropy](../concepts/policy-entropy.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [RLVR](../methods/rlvr.md), [Tree of Thoughts](../methods/tree-of-thoughts.md)

## Appears in

- [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](../../archive/papers/2023/arxiv-2305-10601/summary.md) — Generalizes chain-of-thought into a search over a tree of intermediate 'thoughts', letting a model self-evaluate branches, look ahead and backtrack instead of committing to one left-to-right path.
- [Representation-Based Exploration for Language Models: From Test-Time to Post-Training](../../archive/papers/2026/local-1fadd9f07b138261/summary.md) — Uses elliptical bonuses over a language model's own hidden-state representations as a diversity signal, validates it in a clean inference-time selection setting, then transfers the same signal into RL post-training — where it eliminates the diversity collapse that degrades pass@k at large k.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
