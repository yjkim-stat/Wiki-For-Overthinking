<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# A Implies B: Circuit Analysis in LLMs for Propositional Logical Reasoning

- **Authors**: Guan Zhe Hong, Nishanth Dikkala, Enming Luo, Cyrus Rashtchian, Xin Wang, Rina Panigrahy
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: local
- **Topics**: reasoning-evaluation, reasoning-faithfulness, reasoning-interpretability
- **Relevance score**: reasoning-evaluation 0.50

## In one line

Uses causal mediation analysis on a minimal propositional logic task to recover a sparse reasoning circuit in Mistral-7B and Gemma-2 up to 27B, and decomposes it into four families of attention heads that execute rule locating, rule moving, fact processing and decision making as sequential steps.

## Problem

Circuit analysis is the main tool for understanding how transformers use their internal components, but studies of reasoning have been limited to partial evidence or to small models — three-layer transformers and GPT-2-scale networks. That leaves the basic questions about frontier-scale reasoning unanswered: is reasoning for a given problem localized to particular parts of the network, and do models decompose a reasoning problem into modular components executed as sequential steps with depth, or do they perform one opaque computation?

## Contributions

- A circuit-level account of a canonical propositional reasoning problem in models up to 27B parameters, going well beyond the GPT-2-scale precedent for this kind of analysis.
- Identification of four distinct families of attention heads with specialized roles — queried-rule locating, queried-rule mover, fact-processing and decision heads — present in all three models studied, with roles verified individually by patching after targeted counterfactual prompts.
- The finding that the models execute these steps sequentially rather than merging them, which is evidence for genuinely modular rather than entangled computation.
- A 'lazy reasoning' observation: the core circuit does not pre-process the rules and facts as they are read, but activates primarily after the question and the query variable appear.
- Evidence complicating the claim that circuits are consistent across scale: the 27B model contains logical-operator heads absent or non-causal in the 9B, and its circuit is more parallel where the 9B's is more sequential, even though the core algorithm is shared.
- A contrast with three-layer models trained directly on the task, which reach near-perfect accuracy through intermingled, non-modular reasoning.

## Method

The task is a minimal propositional logic problem requiring several facts to be combined — rules, facts, and a question naming a query variable — chosen because the correct computation is fully specified so a recovered circuit can be checked against it. Causal mediation analysis supplies the indirect effect of each component: activations are patched from counterfactual runs and the change in output measured, identifying which attention heads carry information relevant to the answer. The recovered circuit is validated by running it against counterfactuals and confirming the output does not change substantially. To determine what each component does rather than only that it matters, key-value-query interventions are applied separately to each head — for instance testing whether a head uses the query token to locate the relevant rule — and the four head families are distinguished by patching after different classes of counterfactual prompt, such as swapping the positions of rules or flipping the values of facts. Models are Mistral-7B-v0.1, Gemma-2-9B and Gemma-2-27B, with the 27B analysis partial for computational reasons; three-layer transformers trained from scratch on the same task serve as a small-model comparison.

## Results

All three models contain the same four families of attention heads, applied step by step: heads that locate the rule matching the query, heads that move that rule forward, heads that process the facts, and decision heads that produce the answer. That the steps are separable rather than merged is the paper's own stated surprise, since nothing forces a transformer to keep them distinct. The circuit is sparse — a small set of heads accounts for the computation — and sub-circuits are reused across different parts of an argument where the structure permits, verified for Gemma-2-9B and Mistral-7B. Reasoning is lazy in the sense that the circuit does not activate as rules and facts are read; it engages after the question and the query variable arrive, so the model does not speculatively pre-process the context. Across scale the picture is shared but not identical: Gemma-2-27B contains logical-operator heads that either do not exist in the 9B or lack strong causal roles there, and its circuit is somewhat more parallel where the 9B's is more sequential, which the authors present as adding nuance to prior claims that circuits stay consistent as models scale — the core algorithm persists while mechanical details and extra functional components differ, and those extras likely contribute to the larger model's higher proof accuracy. The small three-layer models trained directly on the task achieve near-perfect accuracy but do so with intermingled reasoning, linking attention blocks and residual streams in ways that do not decompose into the modular families the pretrained models show.

## Limitations

The paper's own: the circuit analysis operates mostly at the level of attention patterns, and the authors say it would be better strengthened by embedding-level analysis; problem complexity is not varied, so whether the same components remain integral for longer logical chains is unverified and is named as the check that would most strengthen the claims; and how model size and family shape the type of circuit remains open, with the Mistral-versus-Gemma comparison offering only partial evidence. Computational constraints also make the 27B analysis partial. A reader should add that the task is a synthetic propositional logic problem solved in a single forward pass with no generated chain of thought, so the paper describes the mechanism of implicit reasoning rather than of the multi-step generated reasoning that dominates this archive — and that the small-model contrast, while striking, cuts against the intuition that clean circuits reflect competence, since the non-modular small models are the more accurate ones on this task.

## Why it matters here

- **reasoning-faithfulness**: The paper that closes this archive's most explicitly named gap: causal intervention applied to reasoning in real language models at scale, not to a synthetic one-bit state and not to language modelling in general. It matters for this topic in a way worth stating carefully, because it does not study traces at all — the task is solved in a single forward pass with no chain of thought. That is precisely its value here. This topic's question is when a visible trace is evidence about the computation, and answering it requires knowing what the computation looks like when there is no trace to read. What this paper finds is that the internal computation is modular and sequential — rule location, then rule movement, then fact processing, then decision — which is the strongest evidence in this archive that step-structured reasoning is a real property of the network rather than an artefact of generating step-structured text. It also supplies two cautions. The lazy-reasoning result means the circuit engages only once the question is known, so a trace produced before the query is fixed cannot be reporting this computation. And the scale comparison undermines a convenient assumption: circuits are not stable across model size even when the algorithm is, so a faithfulness or monitoring result established on one model should not be assumed to transfer. Finally, the finding that three-layer models trained on the task are more accurate while being less modular is a direct warning against reading circuit legibility as evidence of correct reasoning.

## Entities

- **Concepts**: circuit analysis, causal mediation analysis, activation patching, attention head specialization, [modularity](../../../../wiki/concepts/modularity.md), lazy reasoning, sub-circuit reuse, propositional logic, [implicit reasoning](../../../../wiki/concepts/implicit-reasoning.md), [localization](../../../../wiki/concepts/localization.md), indirect effect
- **Methods**: [causal mediation analysis](../../../../wiki/methods/causal-mediation-analysis.md), [activation patching](../../../../wiki/methods/activation-patching.md), key-value-query intervention, counterfactual prompting, [circuit discovery](../../../../wiki/methods/circuit-discovery.md)
- **Datasets**: synthetic propositional logic task

Tags: `mechanistic interpretability`, `circuit analysis`, `causal mediation`, `logical reasoning`, `attention heads`, `modularity`

## Abstract

Due to the size and complexity of modern large language models (LLMs), it has proven challenging to uncover the underlying mechanisms that models use to solve reasoning problems. For instance, is their reasoning for a specific problem localized to certain parts of the network? Do they break down the reasoning problem into modular components that are then executed as sequential steps as we go deeper in the model? To better understand the reasoning capability of LLMs, we study a minimal propositional logic problem that requires combining multiple facts to arrive at a solution. By studying this problem on Mistral and Gemma models, up to 27B parameters, we illuminate the core components the models use to solve such logic problems. From a mechanistic interpretability point of view, we use causal mediation analysis to uncover the pathways and components of the LLMs' reasoning processes. Then, we offer fine-grained insights into the functions of attention heads in different layers. We not only find a sparse circuit that computes the answer, but we decompose it into sub-circuits that have four distinct and modular uses. Finally, we reveal that three distinct models -- Mistral-7B, Gemma-2-9B and Gemma-2-27B -- contain analogous but not identical mechanisms.

---

Record id: `local:99a25b62fd9ad86c`
