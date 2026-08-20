<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Grokked Transformers are Implicit Reasoners: A Mechanistic Journey to the Edge of Generalization

- **Authors**: _unknown_
- **Venue**: NeurIPS 2024
- **Published**: 2024-01-01
- **Source**: local
- **Topics**: reasoning-faithfulness, reasoning-training

## In one line

Shows that transformers can learn implicit multi-step reasoning over stored knowledge, but only through grokking — extended training far past overfitting — and that whether the resulting circuit generalizes out of distribution depends on the reasoning type, succeeding for comparison and failing for composition.

## Problem

Language models are deficient at implicit reasoning with their parametric memory: they cannot robustly compose internalized facts, and even strong models fail to compare entities' attributes reliably. Whether this is a fundamental limitation of transformers or an artefact of how they are trained was unknown, and the internal mechanism by which such reasoning would be acquired had not been characterized.

## Contributions

- Evidence that transformers can learn implicit reasoning over parametric knowledge for both composition and comparison, but only via grokking — training continued far beyond the point of overfitting.
- The finding that generalization level depends on reasoning type: on out-of-distribution examples, models fail to systematically generalize for composition while succeeding for comparison.
- A mechanistic account of grokking here — the formation of a generalizing circuit, and the role of the relative efficiency of the generalizing versus the memorizing circuit in determining which one training settles on.
- A link between systematicity and the configuration of the generalizing circuit, explaining why composition and comparison differ.
- Practical guidance on data and training setup to induce implicit reasoning, and an architectural suggestion — encouraging cross-layer knowledge sharing.
- A demonstration that a fully grokked transformer reaches near-perfect accuracy on a challenging large-search-space reasoning task where GPT-4-Turbo and Gemini-1.5-Pro fail badly regardless of prompting style or retrieval augmentation.

## Method

Two representative implicit reasoning types are studied — composition (chaining stored facts) and comparison (relating attributes of stored entities) — on controlled synthetic knowledge bases where the required inferences are exactly specified and in-distribution versus out-of-distribution splits can be constructed. Transformers are trained far past the point where training accuracy saturates, and generalization is tracked throughout, so grokking is observed rather than assumed. Model internals are examined across training with analytical experiments that identify the circuit implementing the generalizing solution and contrast it with the circuit that merely memorizes, and the relative efficiency of the two is used to explain when training transitions from one to the other. The configuration of the generalizing circuit — how its components are distributed across layers — is then related to whether the model generalizes systematically. A final comparison pits a fully grokked transformer relying on parametric memory against frontier models relying on non-parametric memory, across prompting styles and with retrieval augmentation, on a task with a large search space.

## Results

Transformers do acquire implicit reasoning for both types, but only through grokking, so the capability is invisible at the point where standard training would stop. Generalization is type-dependent: on out-of-distribution examples, models generalize systematically for comparison and fail to for composition, which the analysis ties to how the generalizing circuit is configured across layers rather than to task difficulty. The mechanism behind the grokking transition is the relative efficiency of the generalizing and memorizing circuits — the model first fits by memorization and later reorganizes into a circuit that computes, once continued training makes the generalizing solution the more efficient one. The headline capability comparison is stark: on a challenging reasoning task with a large search space, GPT-4-Turbo and Gemini-1.5-Pro fail badly regardless of prompting style or retrieval augmentation, while a fully grokked transformer achieves near-perfect accuracy — evidence that parametric memory supports complex reasoning that non-parametric retrieval does not.

## Limitations

No standalone limitations section is present in the material read. Points a reader should weigh: the setting is a controlled synthetic knowledge base, which is what makes the circuit analysis and the in/out-of-distribution split possible, but leaves open whether grokking of this kind occurs during realistic pretraining, where data is not repeated to the same degree; the comparison against GPT-4-Turbo and Gemini-1.5-Pro is not like-for-like, since the grokked transformer was trained on exactly this knowledge base while the frontier models were not, so it establishes that parametric memory can support the task rather than that those models could not learn it; and the architectural suggestion of cross-layer knowledge sharing follows from the circuit analysis as a hypothesis rather than being tested.

## Why it matters here

- **reasoning-faithfulness**: The third and decisive data point in a dispute this archive had left at two. One archived paper finds propositional-logic reasoning implemented by four attention-head families executing sequentially and reads it as modular, algorithm-like computation; another finds arithmetic implemented by an unordered bag of heuristic neurons and concludes no algorithm is executed. This paper explains how both can be true of transformers: a memorizing circuit and a generalizing circuit compete, the memorizing one is found first, and the model reorganizes into the generalizing one only under extended training. Modularity is therefore not a fixed property of the architecture or the task but a state a model may or may not have reached — which is exactly what one would expect if a heuristic bag and a clean circuit are the two ends of the same trajectory. It also refines the caution the archive already recorded, that three-layer models trained on a logic task are more accurate while less modular: accuracy and modularity dissociate because a memorizing circuit can be highly accurate in distribution. For this topic the consequence is that a claim about whether a model 'really reasons in steps' is underdetermined without knowing where on that trajectory the model sits, and that out-of-distribution systematicity, not in-distribution accuracy, is the discriminating measurement.
- **reasoning-training**: Places a boundary condition on this topic's central question. The archive's training papers all study post-training — which tokens receive gradient, how entropy is managed, what the reward signal should be — on models whose reasoning ability is assumed to be already present and in need of eliciting or sharpening. This paper studies where such ability comes from in the first place, and the answer is uncomfortable: it emerges only after training continues far past overfitting, via a reorganization from memorization to computation that standard stopping criteria would never reach. That gives the archive's recurring 'RL elicits rather than creates' finding a mechanistic complement — if the generalizing circuit forms only under grokking conditions that pretraining may or may not supply, then what RL has to work with is determined long before RL begins. The data and training-setup guidance is the actionable part, and the type-dependence is the caution: composition and comparison, superficially similar, differ in whether the acquired circuit generalizes at all.

## Entities

- **Concepts**: grokking, [implicit reasoning](../../../../wiki/concepts/implicit-reasoning.md), parametric memory, generalizing circuit, memorizing circuit, systematicity, [compositionality](../../../../wiki/concepts/compositionality.md), [out-of-distribution generalization](../../../../wiki/concepts/out-of-distribution-generalization.md), circuit analysis, [memorization](../../../../wiki/concepts/memorization.md)
- **Methods**: grokking, [circuit analysis](../../../../wiki/methods/circuit-analysis.md), [causal analysis](../../../../wiki/methods/causal-analysis.md), [retrieval-augmented generation](../../../../wiki/methods/retrieval-augmented-generation.md), [chain-of-thought prompting](../../../../wiki/methods/chain-of-thought-prompting.md)
- **Datasets**: synthetic knowledge base (composition), synthetic knowledge base (comparison)

Tags: `grokking`, `implicit reasoning`, `circuits`, `generalization`, `parametric memory`, `mechanistic interpretability`

## Abstract

We study whether transformers can learn to implicitly reason over parametric knowledge, a skill that even the most capable language models struggle with. Focusing on two representative reasoning types, composition and comparison, we consistently find that transformers can learn implicit reasoning, but only through grokking, i.e., extended training far beyond overfitting. The levels of generalization also vary across reasoning types: when faced with out-of-distribution examples, transformers fail to systematically generalize for composition but succeed for comparison. We delve into the model's internals throughout training, conducting analytical experiments that reveal: 1) the mechanism behind grokking, such as the formation of the generalizing circuit and its relation to the relative efficiency of generalizing and memorizing circuits, and 2) the connection between systematicity and the configuration of the generalizing circuit. Our findings guide data and training setup to better induce implicit reasoning and suggest potential improvements to the transformer architecture, such as encouraging cross-layer knowledge sharing. Furthermore, we demonstrate that for a challenging reasoning task with a large search space, GPT-4-Turbo and Gemini-1.5-Pro based on non-parametric memory fail badly regardless of prompting styles or retrieval augmentation, while a fully grokked transformer can achieve near-perfect accuracy, showcasing the power of parametric memory for complex reasoning.

---

Record id: `local:6252abed1b134f57`
