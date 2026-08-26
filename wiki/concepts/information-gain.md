# Information Gain

<!-- auto:begin -->

Information gain names how much a further step of computation adds to what is already known, and the archive's two sources use it at very different levels of rigour. Think or Not? defines it as an information-theoretic quantity, InfoGain, paired with InfoBias, and uses it to show that longer reasoning chains grow progressively less informative and diverge from an ideal path, then derives an entropy-based stopping rule that cuts tokens while preserving accuracy. ParallelWorld uses the phrase loosely for what its verifier agent is asked to prefer when pruning branches -- the paths judged most informative about the task -- with no formal quantity computed and the judgement left to a prompted model. A reader should treat the first as a metric and the second as a description of an objective.

- **Kind**: concept
- **Also called**: InfoGain, information gain
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Confidence-Based Stopping](../methods/confidence-based-stopping.md), [GPT-5.5](../models/gpt-5-5.md), [Overthinking](overthinking.md), [Test-Time Scaling](test-time-scaling.md)

## Appears in

- [ParallelWorld: Test-Time Scaling for Embodied Reasoning](../../archive/papers/2026/arxiv-2608-22971/summary.md) — ParallelWorld is a verifier-guided tree search over simulated future observations for embodied reasoning: from a restorable simulator state it expands several candidate camera and physical actions in parallel, prunes branches with a verifier agent under a branch-width schedule, and answers from the top-ranked root-to-leaf route.
- [Think or Not? Exploring Thinking Efficiency in Large Reasoning Models via an Information-Theoretic Lens](../../archive/papers/2025/title-640d466d159a19d8/summary.md) — Uses information-theoretic metrics (InfoBias, InfoGain) to show that longer reasoning chains in LRMs grow less informative and more divergent from an ideal path, and introduces an entropy-based stopping rule that cuts token usage while preserving accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
