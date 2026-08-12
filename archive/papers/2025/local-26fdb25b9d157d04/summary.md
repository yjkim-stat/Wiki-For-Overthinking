<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Arithmetic Without Algorithms: Language Models Solve Math With a Bag of Heuristics

- **Authors**: Yaniv Nikankin, Anja Reusch, Aaron Mueller, Yonatan Belinkov
- **Venue**: ICLR 2025
- **Published**: 2025-01-01
- **Source**: local
- **Topics**: reasoning-faithfulness, reasoning-interpretability

## In one line

Reverse-engineers the arithmetic circuit down to individual neurons and finds it is neither a learned algorithm nor memorization, but an unordered collection of sparse heuristic neurons that each fire on a numerical input pattern and vote for corresponding answers.

## Problem

Whether LLMs implement robust reusable algorithms or memorize the training distribution is a central question, because memorization suffices for a limited problem set while algorithmic competence is what generalizes. Arithmetic is a good lens because all three routes are available — learn a known algorithm, invent one, or memorize input-output pairs. Prior work had identified an arithmetic circuit and characterized information flow within it, but stopped short of saying what mechanism the circuit implements, which is exactly what is needed to place a model on the generalization-memorization axis. Other work found Fourier-space features for addition, but in models fine-tuned on arithmetic data and, the authors argue, capturing only part of the mechanism.

## Contributions

- A causal identification of the circuit responsible for basic arithmetic, followed by analysis at the level of individual neurons within it rather than stopping at components and information flow.
- The discovery that a sparse set of neurons — about 1% — implements simple heuristics, each recognizing a numerical input pattern and promoting the answers associated with it.
- A taxonomy of heuristic types, such as neurons that activate when an operand falls in a particular range, with the finding that the *unordered* combination of these types explains most of the model's arithmetic accuracy.
- Evidence that this mechanism is not a late artefact: it is already the main source of arithmetic accuracy early in training.
- A negative conclusion supported across several LLMs — the mechanism is neither a robust algorithm nor memorization, but a 'bag of heuristics'.

## Method

Arithmetic prompts over basic operations serve as the task. Causal analysis first isolates a circuit — a subset of model components — that accounts for most of the model's behaviour on these prompts, verified by the usual intervention criterion that ablating outside the circuit leaves behaviour largely intact. The analysis then zooms in to individual neurons within that circuit, examining which inputs make each fire and which output tokens it promotes. Neurons are categorized into heuristic types according to the input pattern they respond to, and the causal contribution of each type is measured by intervening on the neurons implementing it. The decisive test is whether the combination of heuristic types, taken without any ordering or sequential structure, accounts for the model's accuracy — distinguishing a bag-of-heuristics mechanism from an algorithm, which would require the components to compose in a particular order. A training-trajectory analysis then checks when this mechanism emerges. Results are replicated across several LLMs.

## Results

A sparse set of neurons — roughly 1% — carries the arithmetic computation, and each of them implements a recognizable heuristic rather than a step of a general procedure: a neuron may activate when an operand lies in a certain range, or when the operands match some other numerical pattern, and promote the answers consistent with that pattern. The combination of these heuristic types, unordered, explains most of the model's accuracy on arithmetic prompts, which is the paper's central evidence that no algorithm is being executed. The mechanism is also not memorization, since the heuristics generalize across inputs sharing a pattern rather than storing individual input-output pairs. Finally, the same mechanism is already the dominant source of arithmetic accuracy early in training, so it is the model's original strategy rather than something that replaces an earlier algorithmic one. The pattern holds across several models.

## Limitations

No limitations section appears in the material read. Points a reader should weigh: the task is basic arithmetic on small operands, which is the setting most favourable to pattern-matching and least likely to require an algorithm, so the negative conclusion may be specific to problems where heuristics suffice rather than general to reasoning; 'explains most of the accuracy' is a quantitative claim whose threshold matters, since a residual not covered by the heuristic combination could contain the algorithmic part; the heuristic taxonomy is constructed by the authors from observed activation patterns, so the categories are a description of the neurons rather than an independently derived basis; and the study inherits the sensitivity of circuit identification documented elsewhere in this archive, where corruption method and evaluation metric each change which components appear important.

## Why it matters here

- **reasoning-faithfulness**: Sits in direct tension with the other circuit-level result in this archive, and holding both is more informative than choosing. The propositional-logic study finds four families of attention heads executing rule location, rule movement, fact processing and decision *sequentially*, and reads that as evidence of genuinely modular, algorithm-like computation. This study finds an *unordered* combination of heuristic neurons and concludes explicitly that no algorithm is being executed. Three reconciliations are available and the archive can distinguish them. First, task: propositional logic presents rules and facts as explicit structure in the prompt, so attention must route between them, whereas arithmetic has no such structure to route. Second, granularity — and this is the interesting one — the logic study analyses attention heads while this one analyses neurons inside the circuit, so a computation can look modular at the head level and be a bag of heuristics inside each module; nothing rules that out and neither paper tests it. Third, the logic study's own caveat cuts the same way: three-layer models trained directly on its task are *more* accurate while being *less* modular, which is what one expects if modularity is not what produces correctness. For this topic the consequence is concrete. Both papers study computation that produces no chain of thought, and they disagree about whether that computation is step-structured. So the archive's evidence that reasoning traces mirror an internally step-structured process is weaker than the logic paper alone suggests, and a faithfulness claim built on 'the model really does reason in steps' should specify at which level of granularity and on which kind of task.

## Entities

- **Concepts**: bag of heuristics, circuit analysis, [memorization](../../../../wiki/concepts/memorization.md), [generalization](../../../../wiki/concepts/generalization.md), heuristic neurons, causal analysis, [localization](../../../../wiki/concepts/localization.md), arithmetic reasoning, [modularity](../../../../wiki/concepts/modularity.md), neuron interpretability
- **Methods**: [causal analysis](../../../../wiki/methods/causal-analysis.md), [activation patching](../../../../wiki/methods/activation-patching.md), [circuit discovery](../../../../wiki/methods/circuit-discovery.md), neuron ablation, logit attribution
- **Datasets**: synthetic arithmetic prompts

Tags: `mechanistic interpretability`, `arithmetic`, `heuristics`, `memorization`, `generalization`, `circuits`, `neurons`

## Abstract

Do large language models (LLMs) solve reasoning tasks by learning robust generalizable algorithms, or do they memorize training data? To investigate this question, we use arithmetic reasoning as a representative task. Using causal analysis, we identify a subset of the model (a circuit) that explains most of the model's behavior for basic arithmetic logic and examine its functionality. By zooming in on the level of individual circuit neurons, we discover a sparse set of important neurons that implement simple heuristics. Each heuristic identifies a numerical input pattern and outputs corresponding answers. We hypothesize that the combination of these heuristic neurons is the mechanism used to produce correct arithmetic answers. To test this, we categorize each neuron into several heuristic types—such as neurons that activate when an operand falls within a certain range—and find that the unordered combination of these heuristic types is the mechanism that explains most of the model's accuracy on arithmetic prompts. Finally, we demonstrate that this mechanism appears as the main source of arithmetic accuracy early in training. Overall, our experimental results across several LLMs show that LLMs perform arithmetic using neither robust algorithms nor memorization; rather, they rely on a "bag of heuristics".

---

Record id: `local:26fdb25b9d157d04`
