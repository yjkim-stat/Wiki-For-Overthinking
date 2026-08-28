# QwQ

<!-- auto:begin -->

QwQ is a reasoning model cited in this archive's revisiting-test-time-scaling study, which finds o1-like models including QwQ do not possess consistent sequential test-time scaling -- correct solutions are on average shorter than incorrect ones, and self-revision often fails to fix wrong answers or even breaks correct ones -- motivating Shortest Majority Vote as a parallel-scaling alternative, and by SafeChain's 13-model safety evaluation. Note: distinct entry from 'QwQ-32B' recorded elsewhere in the archive, possibly the same model cited without its size suffix; not merged here.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [Claude-3.7-Sonnet](claude-3-7-sonnet.md), [GSM8K](../datasets/gsm8k.md), [HumanEval](../datasets/humaneval.md), [LiveCodeBench (v5)](../datasets/livecodebench-v5.md), [MATH500](../datasets/math500.md), [MBPP](../datasets/mbpp.md), [sequential vs. parallel test-time scaling](../concepts/sequential-vs-parallel-test-time-scaling.md), [Sky-T1](sky-t1.md), [StrongReject](../datasets/strongreject.md), [WildJailbreak](../datasets/wildjailbreak.md), [XSTest](../datasets/xstest.md)

## Appears in

- [Revisiting the Test-Time Scaling of o1-like Models: Do they Truly Possess Test-Time Scaling Capabilities?](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-232/summary.md) — Systematically shows that o1-like models (QwQ, R1, LIMO, and R1-Distill variants) do not actually possess consistent sequential test-time scaling: correct solutions are on average shorter than incorrect ones on the same questions, accuracy does not consistently improve (and sometimes inverse-scales) with solution length, and this traces to a failure of self-revision (models rarely fix wrong answers and sometimes break correct ones) -- leading to Shortest Majority Vote, a parallel-scaling method weighting majority-vote clusters by inverse-log solution length, which significantly outperforms both plain Majority Vote and a shortest-solution-only heuristic.
- [SafeChain: Safety of Language Models with Long Chain-of-Thought Reasoning Capabilities](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-1197/summary.md) — SafeChain systematically evaluates 13 large reasoning models' safety on StrongReject/WildJailbreak, finding no model is safe on both, that unsafe responses are consistently longer than safe ones, that safety improves within a model family as it scales but long-CoT fine-tuning itself does not inherently improve safety over the base instruction-tuned model, and that training-free decoding strategies controlling thought length (ZeroThink most effectively) improve safety without training -- motivating a new CoT-style safety training dataset that preserves reasoning performance while improving safety.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
