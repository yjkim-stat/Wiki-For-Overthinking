# entropy trajectory

<!-- auto:begin -->

The ordered sequence of per-step entropies over a single generation, treated as a signal in its own right rather than collapsed into a mean. Both sources argue that this temporal structure carries information that aggregate statistics discard, and both find that correct and incorrect reasoning have different trajectory shapes — but they characterize the shape differently and at different granularity. One works at the token level and identifies instability as the signature of error: incorrect solutions show 1.7-3.6x more entropy fluctuation, with burst spikes of sustained growth and peak-valley spikes where confidence is reached and then lost. The other works at the reasoning-step level and identifies a regime shift instead: a high-entropy Uncertainty Region that transitions abruptly into a low-entropy Confidence Region, with the location of that transition, not its raggedness, predicting correctness. The two are compatible readings of the same object at different scales, but neither source tests the other's characterization.

- **Kind**: concept
- **Also called**: entropy dynamics
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC23](../datasets/amc23.md), [answer stabilization](answer-stabilization.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER](../methods/deer.md), [Dynasor](../methods/dynasor.md), [early exit](../methods/early-exit.md), [entropy collapse](entropy-collapse.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [majority voting](../methods/majority-voting.md), [MATH](../datasets/math.md), [overthinking](overthinking.md), [process supervision](process-supervision.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-14B](../models/qwen3-14b.md), [reasoning redundancy](reasoning-redundancy.md), [self-certainty](../methods/self-certainty.md), [self-consistency](../methods/self-consistency.md), [token-level entropy](token-level-entropy.md)

## Appears in

- [Unveiling the Entropy Dynamics of Chain-of-Thought Reasoning](../../archive/papers/2026/local-379c0b6966148b4a/summary.md) — Shows that CoT entropy follows a two-phase structure — a high-entropy exploration region that shifts abruptly into a low-entropy convergence region — and detects that shift online with the CUSUM change-point algorithm to drive early exit and trajectory-weighted voting.
- [EDIS: Diagnosing LLM Reasoning via Entropy Dynamics](../../archive/papers/2026/local-e64d3a8c4788daf7/summary.md) — Introduces EDIS, a trajectory-level score that measures how unstably token entropy evolves during generation, and uses it to select better reasoning rollouts at inference and to curate training samples in RL.

<!-- auto:end -->

## Notes

### Two scales, verified never compared

The archive holds two characterizations of trajectory shape:

| | *EDIS* | *Unveiling the Entropy Dynamics* |
| --- | --- | --- |
| Unit | token | reasoning step |
| Signature of error | instability — spikes, 1.7-3.6× more fluctuation | timing — a late regime shift |
| Statistic | spike counts × variance | CUSUM log-likelihood ratio |
| Guarantee | none | minimax detection delay, false-alarm bound |

**Checked, not assumed:** the later paper (CUSUM, June 2026) contains zero
mentions of EDIS or of an instability score, despite EDIS predating it by four
months and both using the phrase "entropy dynamics" in their titles. They are
unaware of each other.

They are not obviously in conflict — a ragged token-level trace and an abrupt
step-level regime change can coexist — but they imply different interventions
(rerank completed trajectories vs stop one in flight), and neither reports the
other's statistic. Computing both on the same rollouts is cheap and would settle
whether one subsumes the other.

### The word-cloud collision

This is the sharpest unresolved tension in the archive, and it is lexical rather
than thematic.

- **MI Peaks** decodes the representations at mutual-information peaks and finds
  they are "So", "Hmm", "Wait", "Therefore" — and shows that suppressing exactly
  these degrades accuracy while suppressing equally many other tokens does not.
- **Commitment Boundary** builds a word cloud of the *post*-commitment tail —
  the region its truncation experiments show does not change the answer — and
  finds "so", "but", "thus", "let's check", "answer", "maybe", "final".

**These are nearly the same word cloud.** One paper says these tokens are
information peaks that reasoning depends on; the other says they populate the
tail that demonstrably does not matter. Both are well-controlled.

**The reconciliation is almost forced: position.** The same marker does
different work before and after commitment. And note the Commitment Boundary
paper supplies half the evidence for this itself — it establishes that hedging
language is *disproportionately concentrated* after the boundary, which is a
positional claim about frequency. What is missing is the causal half: the weight
of reflective tokens as a function of position relative to `i*`.

**Why it has not been done, precisely.** The two papers share benchmark
(MATH-500) but **no model**: MI Peaks uses the DeepSeek-R1-Distill series and
QwQ-32B, Commitment Boundary uses gpt-oss-20b, Qwen3-14B and gemma-4-26B-A4B-it.
The decisive experiment needs one shared model, then: compute `i*` per trace,
compute MI peaks per trace, and cross-tabulate. Both methods are described in
enough detail to reimplement.

### Why the CUSUM framing is worth the group's attention

It imports a solved problem. Sequential change-point detection has a century of
theory, and the paper uses it properly: an explicit optimization objective
(minimize worst-case detection delay subject to a false-alarm bound), a proof
that the log-likelihood ratio drifts in opposite directions across the two
regimes, and a single interpretable threshold `h = log(γ)`.

The gap to watch: CUSUM's optimality assumes i.i.d. observations within each
regime. Entropy sequences are dependent. The paper cites a sub-quadratic
partial-sum variance condition and asserts it holds rather than testing it. For
a statistics group this is the obvious place to contribute — verify the
condition empirically on real trajectories, or replace CUSUM with a detector
built for dependent observations.

### Open question

Both papers detect *that* a trajectory has gone wrong. Neither identifies
*where* the error entered. If entropy dynamics could localize the faulty step
rather than score the whole trajectory, it would bootstrap process reward models
without step labels — see [[process-supervision]].
