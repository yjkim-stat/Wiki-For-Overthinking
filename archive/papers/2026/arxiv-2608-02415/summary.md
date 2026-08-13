<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Training-Free versus Training-Based Intent Classification in LLMs: Accuracy, Robustness, and Failure Modes

- **Authors**: Nan Chen, Zhouhao Yang, Soufiane Hayou
- **Venue**: cs.CL
- **Published**: 2026-08-03
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.02415>
- **PDF**: <https://arxiv.org/pdf/2608.02415v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.40

## In one line

Compares two training-free intent classifiers built from summary statistics of prefill-time activations against trained heads on the same features, and finds the trade-off is not accuracy but where each fails — trained heads win fine-grained distinctions, statistical ones give better uncertainty on mixed prompts and survive adversarial rephrasing that collapses the trained heads to zero.

## Problem

Routing architectures put an intent classifier in front of specialized models, so the classifier decides what everything downstream sees. The available options trade off badly: a direct LLM call is flexible but expensive and hard to calibrate, and a dedicated supervised classifier needs labelled data and retraining whenever the label space changes. What was missing was a systematic comparison of lightweight alternatives that says not which is more accurate but which fails where — since a router's failures are what determine whether the system is safe to deploy.

## Contributions

- Two training-free classifiers computed from activations already produced during prefill: one keeping coordinate-wise first and second moments, the other compressing each token to its norm and keeping only the mean and variance of that scalar
- A theorem separating when each is sufficient — when classes differ only in the direction of their means, any norm-only rule is at chance while a coordinate-aware one has exponentially small error; when they share a mean and differ in isotropic scale, radial information is sufficient and the norm-only rule is Bayes-optimal
- A calibration-cost theorem showing the radial statistic converges dimension-free while the coordinate-wise one carries a dimension-dependent rate, so the cheaper method needs a factor of d fewer calibration samples
- A mixed-intent dataset at five known mixture ratios in both orderings, scoring methods by how well their predicted probability tracks the true mixture rather than by accuracy
- An adversarial set that disguises mathematics problems as bug reports at three levels of camouflage, with frontier LLM calls used to verify the difficulty stratification is real

## Method

Both training-free methods read the output features of linear modules during the prefill pass and compare their summary statistics to per-class baselines precomputed on calibration data, assigning the class with the highest similarity; scoring is the closed-form KL divergence between Gaussian surrogates fitted to those statistics, with a cosine variant for the coordinate-wise method. The paper is explicit that the Gaussian surrogate is a computationally cheap scoring rule based on first and second moments, not a claim that activations are Gaussian. Training-based baselines are a two-layer MLP and a linear probe on mean-pooled or last-token prefill features from the final block, trained on the same calibration data, plus an end-to-end fine-tuned RoBERTa and direct zero- and three-shot LLM calls. Four tasks span two granularities: coarse domain classification (general text, mathematics, code), programming-language identification, natural-language identification, and fine-grained mathematical subfield classification. Seven models from Qwen3 and Llama families at 1B to 32B are evaluated at three seeds, with results reported as balanced accuracy.

## Results

Coarse-grained classification saturates: almost every method reaches 99 to 100 percent on domain and natural-language identification, so that comparison carries little information. The one exception is diagnostic and matches the theory — on programming-language identification the norm-only method falls to 56.39 and 57.02 on Qwen3-8B and 32B while the coordinate-wise method and the trained heads stay above 99, because programming languages share the code domain and differ directionally rather than radially. On fine-grained mathematical subfields the trained heads win consistently (Qwen3-8B: 73.94 on Algebra and 89.36 on Precalculus for the MLP against 31.01 and 51.98 for the norm-only method), though no single method is best on every subfield. Two stress tests reverse the ordering. On mixed-intent prompts the coordinate-wise statistic gives the lowest calibration RMSE in both prompt orderings (0.1216 and 0.0858 against 0.2451 and 0.1764 for the MLP), while the last-token MLP is both worst overall and most sensitive to which intent appears first. On adversarially rephrased mathematics the trained heads collapse — on Qwen3-32B the mean-pooled MLP falls to 11.73, 0.40 and 0.00 across easy, medium and hard camouflage — while training-free methods retain 92.33 and 80.67 on the first two tiers. The hard tier defeats every lightweight method equally, at or near zero, against 64 percent for a frontier LLM call, which the paper reports rather than smooths over. Two practical findings fall out of the ablations: both methods are competitive using only the first 12 of 28 layers, so no full forward pass is needed, and the calibration convergence rates match the theorem, with the radial statistic attaining much lower absolute error.

## Limitations

The paper states none beyond its conclusion that there is no one-size-fits-all method. What a reader should weigh: the headline robustness claim holds on the easy and medium adversarial tiers only, and which training-free method is more robust swaps between backbones — the norm-only rule leads on the 32B model and the cosine variant on the 8B — so the ranking is not stable even within the claim. The hard tier is a shared collapse that no lightweight method survives, which bounds the practical reading of 'more robust' considerably. The level-1 comparison is saturated at 99 to 100 percent, so most of the accuracy table cannot distinguish methods; the informative content is concentrated in the one task where the norm-only rule fails and in the level-2 gap. The two theoretical regimes are limiting cases the paper says real activations mix, and the intermediate analysis is a symmetric-mixture proxy rather than a result about activations. The mixed-intent calibration numbers in the main text come from one 1.7B model, and the adversarial set was produced by rewriting MATH500 with a frontier model, so its difficulty is defined by what that rewriter produced.

## Why it matters here

- **reasoning-interpretability**: It is an interpretability result arriving from the routing literature: the claim that prefill activations separate prompts by domain well enough that first- and second-order statistics suffice, with a theorem saying exactly when the radial part is enough and when direction is required. That is a sharper version of the linear-probe question this archive tracks — not whether a property is decodable, but which statistic of the representation carries it, and at what calibration cost. The failure structure is the more transferable half. A trained head and a statistical summary of the same activations agree on clean inputs and diverge under distribution shift, with the trained head collapsing to zero under adversarial rephrasing while the summary holds — so agreement on a benchmark says nothing about whether two readers of the same representation are reading the same thing. That is the same lesson the archive's monitorability work reaches from the other direction, where the reader determines what a display reveals. It also supplies a caution about probe-based interpretability generally: the fine-tuned encoder here is competitive in-distribution and falls to 42.33 out of it, while the same features read statistically stay above 90.

## Entities

- **Concepts**: intent classification, linear probe, [hidden-state geometry](../../../../wiki/concepts/hidden-state-geometry.md), calibration, [sample complexity](../../../../wiki/concepts/sample-complexity.md), [out-of-distribution generalization](../../../../wiki/concepts/out-of-distribution-generalization.md), [adversarial robustness](../../../../wiki/concepts/adversarial-robustness.md), [uncertainty quantification](../../../../wiki/concepts/uncertainty-quantification.md), [routing](../../../../wiki/concepts/routing.md), [superposition](../../../../wiki/concepts/superposition.md)
- **Methods**: VecStat, NormStat, [linear probe](../../../../wiki/methods/linear-probe.md), multilayer perceptron classifier, KL divergence scoring, [cosine similarity](../../../../wiki/methods/cosine-similarity.md), [LLM-as-a-judge](../../../../wiki/methods/llm-as-a-judge.md)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH-500](../../../../wiki/datasets/math-500.md), [HumanEval](../../../../wiki/datasets/humaneval.md), Magicoder, [MMLU](../../../../wiki/datasets/mmlu.md), Aya, Competition Math, Adv_MATH500

Tags: `intent classification`, `routing`, `probing`, `calibration`, `adversarial robustness`

## Abstract

Intent classification in Large Language Models (LLMs) involves categorizing user prompts into predefined classes. For instance, given a user prompt, the system must determine whether it primarily concerns mathematics, coding, or general text processing. Such classification enables routing prompts to specialized models optimized for specific domains, improving both accuracy and computational efficiency. In this work, we conduct a systematic study comparing training-free vs training-based approaches for intent classification. For this purpose, we consider two lightweight, training-free methods based on statistics of internal representations and compare them against MLP classifiers and linear probes. Our comprehensive empirical evaluation reveals that 1) Both training-free and training-based methods saturate easy benchmarks (mathematics vs. coding vs. natural language), 2) Training-based classifiers have an advantage on harder classification tasks (e.g. Java vs Python), and 3) Training-free methods are generally more robust to mixed-intent and adversarial prompts.

---

Record id: `arxiv:2608.02415`
