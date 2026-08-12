# modularity

<!-- auto:begin -->

Whether a computation decomposes into components with separable roles that compose in a definite order. The archived sources disagree, and the disagreement is the useful part. On propositional logic, four families of attention heads execute rule location, rule movement, fact processing and decision *sequentially* — presented by its authors as surprising, since nothing forces a transformer to keep the steps distinct. On arithmetic, the mechanism is an *unordered* combination of heuristic neurons, and the authors conclude no algorithm is executed. The two analyses work at different granularities (attention heads versus neurons), so a computation could be modular at one level and a bag of heuristics inside each module; neither paper tests this. A third source warns against reading modularity as competence at all: three-layer models trained directly on the logic task are more accurate while being less modular.

- **Kind**: concept
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 4

**Related**: [activation patching](../methods/activation-patching.md), [attention head](attention-head.md), [catastrophic forgetting](catastrophic-forgetting.md), [causal analysis](../methods/causal-analysis.md), [causal mediation analysis](../methods/causal-mediation-analysis.md), [causal tracing](../methods/causal-tracing.md), [circuit analysis](../methods/circuit-analysis.md), [circuit discovery](../methods/circuit-discovery.md), [generalization](generalization.md), [GPT-J 6B](../models/gpt-j-6b.md), [implicit reasoning](implicit-reasoning.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [localization](localization.md), [memorization](memorization.md), [Mistral-7B](../models/mistral-7b.md), [model merging](../methods/model-merging.md), [Pythia-410M](../models/pythia-410m.md), [superposition](superposition.md)

## Appears in

- [Multi-component Causal Tracing in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-154/summary.md) — Generalizes causal tracing from one component or layer at a time to selecting subsets of components jointly, by relaxing the combinatorial search into a continuous one over soft interventions.
- [ReasonAny: Incorporating Reasoning Capability to Any Model via Simple and Effective Model Merging](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2201/summary.md) — Merges a reasoning model into a domain-specialized one after finding that reasoning ability resides in low-gradient-sensitivity parameter regions rather than high-magnitude ones.
- [Arithmetic Without Algorithms: Language Models Solve Math With a Bag of Heuristics](../../archive/papers/2025/local-26fdb25b9d157d04/summary.md) — Reverse-engineers the arithmetic circuit down to individual neurons and finds it is neither a learned algorithm nor memorization, but an unordered collection of sparse heuristic neurons that each fire on a numerical input pattern and vote for corresponding answers.
- [A Implies B: Circuit Analysis in LLMs for Propositional Logical Reasoning](../../archive/papers/2025/local-99a25b62fd9ad86c/summary.md) — Uses causal mediation analysis on a minimal propositional logic task to recover a sparse reasoning circuit in Mistral-7B and Gemma-2 up to 27B, and decomposes it into four families of attention heads that execute rule locating, rule moving, fact processing and decision making as sequential steps.

<!-- auto:end -->

## Notes

### Three results, and the one that reconciles them

The archive holds three circuit-level accounts of reasoning that appear to
conflict:

| Source | Task | Finding |
| --- | --- | --- |
| A Implies B | propositional logic, 7B-27B pretrained | **modular, sequential**: four head families executing rule-locate → rule-move → fact-process → decide |
| Bag of Heuristics | arithmetic, pretrained | **unordered**: ~1% of neurons, each firing on a numerical pattern; explicitly "no algorithm" |
| Grokked Transformers | synthetic composition/comparison, trained from scratch | **both, sequentially in time**: a memorizing circuit forms first, a generalizing circuit replaces it only under extended training |

**The third explains the first two.** Memorizing and generalizing circuits
compete; the memorizing one is cheaper and is found first; reorganization into
the generalizing circuit happens only when continued training makes it the more
efficient solution. So modularity is **a state a model may or may not have
reached**, not a property of the architecture or of the task. A bag of
heuristics and a clean sequential circuit are plausibly the two ends of one
trajectory.

### What this costs the archive

Two cautions follow, and both weaken conclusions recorded earlier here.

**Modularity is not competence.** Three-layer models trained directly on the
logic task are *more accurate* while being *less* modular — exactly what one
expects if a memorizing circuit can be highly accurate in distribution. So
"we found a clean circuit" is not evidence the model reasons well, and
"we found a heuristic bag" is not evidence it reasons badly.

**In-distribution accuracy cannot discriminate.** The grokking work finds
systematic out-of-distribution generalization for *comparison* and failure for
*composition* despite similar in-distribution performance. The discriminating
measurement is OOD systematicity, which neither of the two pretrained-model
studies performs.

### The untested reconciliation

The two pretrained studies work at **different granularities** — attention heads
versus individual neurons. A computation could be modular at the head level and
a bag of heuristics inside each head's contribution. Nothing rules this out and
neither paper tests it. Combined with the grokking account, the honest position
is that the archive has **no established answer** to whether reasoning in
pretrained models is step-structured, and that a faithfulness claim resting on
"the model really does reason in steps" must specify granularity, task, and
where on the memorize→generalize trajectory the model sits.
