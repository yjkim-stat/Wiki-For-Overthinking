<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Measuring Faithfulness in Chain-of-Thought Reasoning

- **Authors**: Tamera Lanham, Anna Chen, Ansh Radhakrishnan, Benoit Steiner, Carson Denison, Danny Hernandez, Dustin Li, Esin Durmus, Evan Hubinger, Jackson Kernion, Kamilė Lukošiūtė, Karina Nguyen, Newton Cheng, Nicholas Joseph, Nicholas Schiefer, Oliver Rausch, Robin Larson, Sam McCandlish, Sandipan Kundu, Saurav Kadavath, Shannon Yang, Thomas Henighan, Timothy Maxwell, Timothy Telleen-Lawton, Tristan Hume, Zac Hatfield-Dodds, Jared Kaplan, Jan Brauner, Samuel R. Bowman, Ethan Perez
- **Venue**: cs.AI
- **Published**: 2023-07-17
- **Source**: seed
- **Link**: <https://arxiv.org/abs/2307.13702>
- **PDF**: <https://arxiv.org/pdf/2307.13702v1>
- **Topics**: reasoning-faithfulness, reasoning-training, test-time-scaling
- **Relevance score**: reasoning-faithfulness 0.40, reasoning-training 0.50, test-time-scaling 0.57

## In one line

Measures how much a model's answer actually depends on its stated chain of thought by intervening on the trace — adding mistakes, paraphrasing, truncating — and finds the dependence varies by task and decreases as models get larger.

## Problem

Models answer better after producing step-by-step reasoning, but whether that stated reasoning is a faithful account of the process producing the answer was unclear. Establishing it requires distinguishing several competing explanations for CoT's benefit: real conditioning on the stated steps, extra test-time computation regardless of content, or information smuggled in by particular phrasing.

## Contributions

- An intervention-based measurement of faithfulness: perturb the CoT and observe how far the prediction moves, rather than inspecting the text.
- The finding that conditioning on the CoT varies widely across tasks, from heavy reliance to near-complete disregard.
- Evidence against two alternative explanations of CoT's benefit — that it comes from added test-time compute alone, or from information encoded in the CoT's particular phrasing.
- An inverse-scaling observation: larger, more capable models produce less faithful reasoning on most tasks studied.

## Method

The chain of thought is intervened on directly — for example by introducing mistakes into it or by paraphrasing it — and the change in the model's answer is measured. Strong movement indicates the answer was conditioned on the stated reasoning; little movement indicates it was not. Comparing perturbation types separates content-dependence from mere length or phrasing effects. The abstract does not name the tasks or models.

## Results

Faithfulness varies substantially across tasks, with models sometimes relying heavily on the CoT and sometimes largely ignoring it. The performance boost is attributed neither to added test-time compute alone nor to phrasing-encoded information. Faithfulness decreases with model size and capability on most tasks studied. The abstract reports no numeric values. Summarized from the abstract alone, so the figures below are only those the abstract states; the paper's full evaluation is not represented here.

## Limitations

Not discussed in the abstract, which also omits the task list and model sizes, so the scope of the inverse-scaling claim cannot be judged from the material supplied. The framing offered — that CoT can be faithful if model size and task are chosen carefully — is a conditional worth treating as the paper's actual conclusion rather than a general endorsement.

## Why it matters here

- **reasoning-faithfulness**: The methodological complement to the biasing-based test in this archive: instead of adding a cue to the input and watching the explanation omit it, this intervenes on the trace itself and watches the answer fail to move. That makes faithfulness a measurable quantity per task rather than a binary property, and the finding that it varies from heavy reliance to near-disregard is the reason this topic asks 'when is the trace evidence' rather than 'is the trace evidence'. The inverse-scaling result is the most consequential claim for the group: if faithfulness degrades as capability grows, monitoring approaches that depend on readable traces get weaker exactly where they matter most. It also directly rules out the deflationary explanation that CoT works purely as extra computation, which matters for the test-time-scaling literature next door.
- **reasoning-training**: A thin match. The paper measures a property of trained models and proposes no training method. Its bearing is that faithfulness appears to be shaped by scale and task rather than deliberately trained for, which is the gap a later archived paper fills by showing 800 SFT examples can install or destroy the habit of externalizing uncertainty.
- **test-time-scaling**: Relevant through one specific negative result rather than through a method: CoT's benefit is not explained by added test-time compute alone. That is a constraint on how this topic should interpret its own gains — the content of the extra tokens matters, so a scaling curve is not simply a compute curve.

## Entities

- **Concepts**: [chain of thought faithfulness](../../../../wiki/concepts/chain-of-thought-faithfulness.md), intervention on reasoning, conditioning on the trace, [inverse scaling](../../../../wiki/concepts/inverse-scaling.md), [post-hoc rationalization](../../../../wiki/concepts/post-hoc-rationalization.md), [test-time compute](../../../../wiki/concepts/test-time-compute.md)
- **Methods**: CoT perturbation, mistake injection, paraphrasing intervention, [chain-of-thought prompting](../../../../wiki/methods/chain-of-thought-prompting.md)
- **Datasets**: _none recorded_

Tags: `faithfulness`, `chain of thought`, `intervention`, `inverse scaling`, `measurement`

## Abstract

Large language models (LLMs) perform better when they produce step-by-step, "Chain-of-Thought" (CoT) reasoning before answering a question, but it is unclear if the stated reasoning is a faithful explanation of the model's actual reasoning (i.e., its process for answering the question). We investigate hypotheses for how CoT reasoning may be unfaithful, by examining how the model predictions change when we intervene on the CoT (e.g., by adding mistakes or paraphrasing it). Models show large variation across tasks in how strongly they condition on the CoT when predicting their answer, sometimes relying heavily on the CoT and other times primarily ignoring it. CoT's performance boost does not seem to come from CoT's added test-time compute alone or from information encoded via the particular phrasing of the CoT. As models become larger and more capable, they produce less faithful reasoning on most tasks we study. Overall, our results suggest that CoT can be faithful if the circumstances such as the model size and task are carefully chosen.

---

Record id: `arxiv:2307.13702`
