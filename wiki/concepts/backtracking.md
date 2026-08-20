# backtracking

<!-- auto:begin -->

Returning from a state where progress is impossible to an earlier one and taking a different path. The two sources approach it from opposite ends of the same question. One builds it into an inference-time search procedure, making lookahead and backtracking explicit operations over a tree of partial solutions rather than something a model does inside a linear trace. The other measures whether reinforcement learning teaches it: at sampled dead-end maze states the probability of the reversing move rises from 0.0068 to 0.1537 and from 0.0647 to 0.1687 after RLVR, absolute failures fall, and on mathematics recovery from an injected distractor improves by 4.18 to 29.09 points. Together they mark a shift in where the capability is thought to live — from a scaffold placed around the model to a property the training instils — and the second supplies the archive's clearest evidence that RLVR buys something real with the trajectory diversity it spends.

- **Kind**: concept
- **Also called**: backtrack
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [AIME](../datasets/aime.md), [chain of thought](../methods/chain-of-thought.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [DAPO](../methods/dapo.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DAPO-Qwen-32B](../models/dapo-qwen-32b.md), [entropy collapse](entropy-collapse.md), [exploration](exploration.md), [foresight](foresight.md), [Game of 24](../datasets/game-of-24.md), [GPT-4](../models/gpt-4.md), [gpt-5.6-luna](../models/gpt-5-6-luna.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [Llama-3-8B](../models/llama-3-8b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [long chain-of-thought distillation](../methods/long-chain-of-thought-distillation.md), [monitorability](monitorability.md), [overthinking](overthinking.md), [paired bootstrap confidence intervals](../methods/paired-bootstrap-confidence-intervals.md), [pass@k](pass-k.md), [policy entropy](policy-entropy.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-8B](../models/qwen3-8b.md), [Qwen3-8B-Base](../models/qwen3-8b-base.md), [reasoning boundary](reasoning-boundary.md), [RLVR](../methods/rlvr.md), [self-correction](self-correction.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [trajectory diversity](trajectory-diversity.md), [Tree of Thoughts](../methods/tree-of-thoughts.md)

## What we have settled

- **Established** — RLVR narrows the set of semantically distinct solution paths a model will produce while widening the set of errors it can recover from; the two effects are separable, both real, and a single pass@k number cannot show either.
  - Measuring a model's preference between two specific verifier-equivalent continuations at a shared branch point, RLVR-trained policies show lower branch entropy than distilled counterparts on 95.5-100% of sampled branches across four model families, and the collapse is significantly stronger in the semantic contrast than in the syntactic one — so the pruning is of inferences, not of phrasing. The same work shows the compensating gain: backtracking probability at dead ends rises from 0.0068 to 0.1537 and from 0.0647 to 0.1687 on two maze models, and recovery from an injected distractor improves by 4.18 to 29.09 points on mathematics. Masking illegal continuations makes the trade explicit — with invalid options removed the flatter distilled policy outperforms the RL one by about 60 percent. This reconciles the archive's standing disagreement rather than picking a side: under plain pass@k the base model overtakes at large k because valid-but-different paths were pruned, while under CoT-Pass@K the RLVR model leads at every k because invalid paths were pruned harder.

## Appears in

- [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](../../archive/papers/2023/arxiv-2305-10601/summary.md) — Generalizes chain-of-thought into a search over a tree of intermediate 'thoughts', letting a model self-evaluate branches, look ahead and backtrack instead of committing to one left-to-right path.
- [BODHI: Do LLMs Branch Out and Discover Heterogeneous Inferences?](../../archive/papers/2026/arxiv-2608-02867/summary.md) — Builds prefix trees of semantically equivalent reasoning statements and measures how RLVR changes a model's preference between branches, finding the entropy collapse is not stylistic — the collapse is stronger for semantically distinct continuations than for syntactic variants of the same statement.
- [The Tell-Tale Trace: Detecting Reasoning Failures in LLMs Using Chain-of-Thought Dynamics](../../archive/papers/2026/arxiv-2608-03291/summary.md) — Tags every sentence of a reasoning trace by its function and studies the sequence rather than the content, finding that failing SAT traces collapse into repetitive verification and commit early, that failing UNSAT traces run the wrong procedure entirely, and that a prompt naming the missing procedure recovers 84.6% of them.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
