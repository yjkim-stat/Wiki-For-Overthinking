<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Interpretable Adaptive Sampling for LLM Test-Time Scaling

- **Authors**: Mobina Kashaniyan, Ali Jannesari
- **Venue**: cs.AI
- **Published**: 2026-08-04
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.03961>
- **PDF**: <https://arxiv.org/pdf/2608.03961v1>
- **Topics**: test-time-scaling
- **Relevance score**: reasoning-evaluation 0.25, test-time-scaling 0.57

## In one line

Allocates test-time samples per prompt with a fuzzy controller over human-readable difficulty and confidence signals, and — under a selector-matched protocol that isolates the budget policy from the answer selector — reports the result honestly as an accuracy-compute tradeoff rather than an accuracy gain.

## Problem

Test-time scaling pipelines mostly spend a fixed number of samples on every prompt, wasting compute on easy instances while underserving hard ones. Learned allocation policies can do better but their decisions are hard to audit, which matters for debugging, safety review and deployment under a compute budget: a fixed budget at least explains itself trivially, whereas a learned policy explains nothing about why a given prompt received the compute it did. A second problem is methodological — a method that changes both the budget and the answer selector cannot say which of the two produced its result.

## Contributions

- A budget controller whose inputs, rules and outputs are inspectable per prompt: fuzzy membership over prompt complexity, model confidence, entropy, prompt type, expected answer length and cached history, with a second stage whose interval width is itself a reported uncertainty
- A fair-alignment protocol that fixes decoding across methods, disables the draft pass and lets the controller change only the number of samples — deliberately stricter than the full system, to answer whether adaptive allocation helps when selection and decoding are held constant
- A selector-matched control at the same maximum budget, so the effect of allocation is separated from the effect of the answer selector
- Reporting the outcome as a tradeoff rather than a win, including the two of four settings where adaptive is slightly less accurate
- A component ablation reported with its inconvenient results intact — removing some signals improves accuracy

## Method

Prompt-side signals are computed before generation: a surface complexity score from normalized length with bonuses for punctuation, digits and multiple sentences, and an NLP complexity score combining vocabulary richness, sentence count, mathematical-symbol density, semantic ambiguity, linguistic complexity and reasoning depth, blended into one difficulty value. Model-side signals come from a short draft — a confidence score from the geometric mean of token probabilities and a normalized entropy — plus a slow-moving cache of prior performance on similar prompts. A two-stage fuzzy controller maps difficulty and confidence to a coarse budget through triangular and trapezoidal membership functions, then refines it with the remaining signals as Type-2 intervals whose width narrows when the refinements agree and widens when they conflict; defuzzification gives a scale and an uncertainty, and the scale is nudged upward in proportion to that uncertainty before being mapped to an integer sample count, with a floor for clearly hard prompts. Candidates are scored by self-certainty and aggregated by Borda count over extracted answers. Two small instruction-tuned models are evaluated on grade-school arithmetic, a competition mathematics subset and a short factual science set, against best-of-N at several fixed budgets, a compute-optimal allocation rule, self-certainty selection at the full budget, and the selector-matched fixed full budget.

## Results

Under the selector-matched comparison the method is not more accurate, and the paper says so. On competition mathematics it loses 0.007 and 0.018 accuracy while using 10.8% and 14.5% fewer samples on the two models; on grade-school arithmetic it loses 0.002 on one and gains 0.005 on the other, at 1.4% and 3.9% fewer samples. The claim being made is therefore that an interpretable controller can stay close to full-budget accuracy while spending less, and the budget histograms explain where the saving comes from — more prompts fall below the full budget on the harder mathematics set, while the arithmetic set concentrates near the cap, so the controller is conservative exactly where near-full aggregation still helps. Against the broader baselines it does better: on the factual set it reaches 0.192 and 0.376 accuracy against 0.154 and 0.360 for self-certainty selection at the full budget, using about seven samples on average. The most interesting number in the paper is a baseline failure rather than a method success — best-of-3 scores 0.093 against best-of-1's 0.153 on one model, so three samples are worse than one, which the authors read correctly: if the selector does not exploit the candidate set, extra samples add plausible wrong answers. The fixed-budget controls confirm the shape: budgets of one to three are far worse, five is closer, and the adaptive setting lands within 0.001 and 0.004 of the full budget at 7.86 and 7.07 average samples. The component ablation is reported with its awkward results intact — removing the entropy signal improves mathematics accuracy, and neutralizing confidence also improves it while forcing the average budget to the maximum — and the authors draw the correct conclusion, that the controller should be read as a transparent allocation policy rather than an optimized one.

## Limitations

The paper is candid about most of this in the text. The accuracy differences are within overlapping marginal confidence intervals, and the authors note that a paired test would require matched per-prompt correctness logs which they do not report — so the small negative deltas are not established as real losses any more than the small positive one is a real gain. The component ablation shows individual signals are not validated: some removals help, which means the interpretability claim is about the controller's structure being auditable, not about its signals being the right ones. The fair-alignment protocol disables the draft pass and fixes decoding, so the evaluated configuration is deliberately weaker than the full system and the reported savings are a lower bound on what the full method would do and an upper bound on how cleanly it can be attributed. Scale is two small instruction-tuned models with a maximum budget of eight and a 256-token output cap, which bounds both the difficulty of the problems and the room for allocation to matter. The factual-QA numbers are acknowledged to be depressed by strict exact-match scoring. Nothing is reported about the controller's own compute cost against the samples it saves.

## Why it matters here

- **test-time-scaling**: Two things here are worth more than the method. The first is the selector-matched control: adaptive allocation and fixed full budget run through the same self-certainty-plus-Borda selector, so the comparison isolates the budget policy — which is precisely the discipline the archive's baseline-validity finding asks for, and which the archive's own vision-language audit showed can be worth 31.8 points when neglected. The second is the non-monotonicity: best-of-3 scoring below best-of-1 on one model is a clean demonstration that more samples are not safe by default, and it joins the label-free RLVR result where 64 rollouts underperformed 16. The shared mechanism is the same in both — more samples strengthen whatever the aggregation rule already does, including when it is wrong — and it is the counterweight this archive needs against the assumption that sampling more is a free improvement. The paper's own honesty is also a data point for how to read this literature: it reports a tradeoff where a less careful version would have reported a win, and reports an ablation in which removing its own signals sometimes helps.

## Entities

- **Concepts**: test-time scaling, [adaptive compute allocation](../../../../wiki/concepts/adaptive-compute-allocation.md), self-consistency, best-of-N, [prompt difficulty](../../../../wiki/concepts/prompt-difficulty.md), interpretability, [uncertainty quantification](../../../../wiki/concepts/uncertainty-quantification.md), [selection signal](../../../../wiki/concepts/selection-signal.md), [matched-budget comparison](../../../../wiki/concepts/matched-budget-comparison.md)
- **Methods**: fuzzy control, [best-of-N](../../../../wiki/methods/best-of-n.md), [Borda count](../../../../wiki/methods/borda-count.md), [self-certainty](../../../../wiki/methods/self-certainty.md), compute-optimal allocation, [majority voting](../../../../wiki/methods/majority-voting.md)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH](../../../../wiki/datasets/math.md), SciQ

Tags: `test-time scaling`, `adaptive allocation`, `interpretability`, `sampling`, `compute budget`

## Abstract

Test-time scaling improves LLM reasoning by generating and aggregating multiple candidate answers, yet many pipelines use fixed per-query budgets that spend the same compute on easy and difficult prompts. These fixed budgets are also difficult to inspect because they do not explain why a given prompt receives a particular number of samples. We propose adaptive} test-time scaling with a lightweight fuzzy controller that maps interpretable signals, including estimated prompt complexity and model confidence, to a per-query sampling budget. The controller assigns fewer samples to easier or more confident prompts and more samples to harder or less certain prompts, making inference-time compute inspectable rather than fixed or opaque. We evaluate under a fair-alignment protocol with matched decoding settings and controlled answer selection, and compare against best-of-$N$, compute-aware scaling, and self-certainty-based baselines on question-answering and mathematical reasoning tasks. Across models and datasets, adaptive fuzzy control improves over several standard baselines and remains close to a selector-matched full-budget control while reducing the average number of samples. These findings suggest that interpretable adaptive sampling is a practical direction for more efficient test-time reasoning in large language models.

---

Record id: `arxiv:2608.03961`
