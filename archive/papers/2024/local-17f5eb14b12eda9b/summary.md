<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# The Expressive Power of Transformers with Chain of Thought

- **Authors**: William Merrill, Ashish Sabharwal
- **Venue**: ICLR
- **Published**: 2024-01-01
- **Source**: local
- **Topics**: reasoning-training, test-time-scaling
- **Relevance score**: reasoning-training 0.50, test-time-scaling 0.50

## In one line

Characterizes exactly how much computational power a chain of thought buys as a function of its length, sandwiching the class of languages a decoder recognizes with t(n) decoding steps between two standard complexity classes.

## Problem

Standard transformers that answer immediately after reading their input provably cannot solve simple sequential problems — simulating finite automata, deciding graph connectivity, solving linear equalities — because they lack recurrence. Chain of thought helps in practice, but there was no general characterization of what it makes solvable, nor of how many intermediate steps are needed to gain what.

## Contributions

- The sandwich TIME(t(n)) subset CoT(t(n)) subset SPACE(t(n)+log n) intersect TIME~(t(n)^2+n^2), relating decoding steps to standard time and space classes
- The layer-norm hash, a construction enabling cross-column retrieval by query-key matching of numerical values under uniform attention
- A proof that a linear number of steps suffices to recognize all regular languages, separating such decoders from step-free transformers under TC^0 != NC^1
- An exact characterization: polynomially many steps with strict causal attention and projected pre-norm recognize exactly P
- The negative observation that logarithmic steps expand the bound only from TC^0 to L and admit no known concrete gain

## Method

A decoder-only transformer is allowed t(n) intermediate decoding steps before answering, and CoT(t(n)) denotes the languages recognized that way. The bound is proved in both directions. The lower bound constructs a transformer that simulates a Turing machine step per decoding step; its enabling device is the layer-norm hash, a module that makes exact-match retrieval work across columns whose values were produced by uniform attention and therefore carry different denominators — phi(x/i, 1/i) is shown to be scale-invariant, so an inner product of two such encodings tests equality of the underlying scalars regardless of the positions they were computed at. The upper bounds simulate the transformer on a multitape Turing machine. Assumptions for the lower bounds: log-precision, saturated attention, strict causal masking, and projected pre-norm (layer-norm applied to a linear projection of a sublayer's input rather than the whole input).

## Results

The central sandwich is TIME(t(n)) subset of CoT(t(n)) subset of SPACE(t(n) + log n) intersected with TIME~(t(n)^2 + n^2). Three regimes follow. Logarithmic steps expand the upper bound only from TC^0 to L, so such transformers still cannot solve NL-complete problems like directed graph connectivity or P-complete problems like linear equalities. Linear steps suffice to recognize all regular languages, which is impossible without intermediate steps unless TC^0 = NC^1, and keep the decoder within context-sensitive languages. Polynomial steps with projected pre-norm and strict causal attention make transformer decoders equivalent to exactly P — the paper states this is the first exact equivalence between a class of transformers and a standard complexity class. Quadratic steps suffice for directed graph connectivity. The authors note they identified no concrete reasoning problem where a logarithmic number of steps helps.

## Limitations

The lower bounds need saturated attention, strict causal masking and projected pre-norm; projected and multi-pre-norm are generalizations of standard pre-norm rather than what is deployed, and the paper itself suggests investigating whether to adopt them in practice. Results are about expressivity only — what a transformer can represent, not what training finds, and there is no generalization or learnability claim. The characterization is asymptotic in the number of steps, so it says nothing about the constants that decide whether a construction is usable. Polynomial steps make transformers strong reasoners in principle while the paper notes running polynomially many forward passes of a large transformer is likely intractable.

## Why it matters here

- **reasoning-training**: A limit on what any training signal can produce, which is a different kind of claim from the rest of this topic. If a task lies outside CoT(t(n)) for the step budget a model is trained to use, no reward shaping or curriculum reaches it — the ceiling is architectural. It also gives the archive's effective-depth thread its formal footing: the reason emitted tokens raise usable depth is that each one is another Turing machine step, and the paper constructs the simulation explicitly rather than arguing by analogy.
- **test-time-scaling**: The strongest statement in the archive about what inference compute buys, and it is a statement about kind rather than degree: the number of decoding steps is a computational resource akin to time, and the classes it unlocks are named exactly. Two results bear directly on practice here. Logarithmic steps buy essentially nothing, so a scaling curve that flattens early is expected rather than anomalous. And the jump that matters is at linear steps, where recurrence becomes simulable — which is the formal version of the archive's recurring empirical finding that a trace must be long enough to carry state, not merely long. It also bounds every stopping-signal method tracked here from below: truncating a trace to a sublinear fraction of the input length cannot preserve capabilities that need linear steps.

## Entities

- **Concepts**: [expressivity](../../../../wiki/concepts/expressivity.md), [circuit complexity](../../../../wiki/concepts/circuit-complexity.md), [effective depth](../../../../wiki/concepts/effective-depth.md), chain of thought, latent reasoning, regular language, context-sensitive language, log-precision, saturated attention, recurrence
- **Methods**: layer-norm hash, Turing machine simulation, automaton simulation, projected pre-norm, [chain of thought](../../../../wiki/methods/chain-of-thought.md)
- **Datasets**: _none recorded_

Tags: `expressivity`, `circuit complexity`, `chain of thought`, `theory`, `complexity classes`

## Abstract

Recent theoretical work has identified surprisingly simple reasoning problems, such as checking if two nodes in a graph are connected or simulating finite-state machines, that are provably unsolvable by standard transformers that answer immediately after reading their input. However, in practice, transformers' reasoning can be improved by allowing them to use a "chain of thought" or "scratchpad", i.e., generate and condition on a sequence of intermediate tokens before answering. Motivated by this, we ask: Does such intermediate generation fundamentally extend the computational power of a decoder-only transformer? We show that the answer is yes, but the amount of increase depends crucially on the amount of intermediate generation. For instance, we find that transformer decoders with a logarithmic number of decoding steps (w.r.t. the input length) push the limits of standard transformers only slightly, while a linear number of decoding steps, assuming projected pre-norm (a slight generalization of standard pre-norm), adds a clear new ability (under standard complexity conjectures): recognizing all regular languages. Our results also imply that linear steps keep transformer decoders within context-sensitive languages, and polynomial steps with generalized pre-norm make them recognize exactly the class of polynomial-time solvable problems—the first exact characterization of a type of transformers in terms of standard complexity classes. Together, this provides a nuanced framework for understanding how the length of a transformer's chain of thought or scratchpad impacts its reasoning power.

---

Record id: `local:17f5eb14b12eda9b`
