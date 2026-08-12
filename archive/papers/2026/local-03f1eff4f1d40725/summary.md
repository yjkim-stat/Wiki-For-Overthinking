<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# A Sharper Picture of Generalization in Transformers

- **Authors**: Paul Lintilhac, Sair Shaikh
- **Venue**: preprint
- **Published**: 2026-01-01
- **Source**: local
- **Topics**: reasoning-training, reasoning-interpretability

## In one line

Derives a non-vacuous PAC-Bayes generalization bound for transformers on boolean functions in terms of Fourier sparsity and degree, and uses it to show chain of thought turns an exponential dependence on reasoning length into a linear one for Parity.

## Problem

Expressivity results say what a transformer can represent; they do not say what can be learned from finite data, and the gap between the two is unexplained. Prior transformer generalization bounds come from Rademacher complexity and capacity arguments grounded in parameter norms. The paper asks whether PAC-Bayes, grounded in flat minima, gives a sharper picture, and whether it can explain why functions a transformer provably expresses are nonetheless hard to learn.

## Contributions

- A constructive PAC-Bayes methodology for transformer generalization bounds that needs no knowledge of the learned parameters, only that the learner's solution is dominated in norm and sharpness by an explicit construction
- A non-vacuous generalization bound scaling as O(omega D_f^2) in Fourier sparsity and degree
- A concrete bridge across the expressivity-learnability gap, explaining why high-degree expressible functions resist learning
- A sharpness-based learning bound showing chain of thought makes the Parity bound linear rather than exponential in reasoning length
- Efficient estimation of the bound's complexity parameters via property testing
- A mechanistic interpretability study supporting the realism of the theoretical construction

## Method

Target functions on the boolean cube are decomposed in the Fourier basis, characterized by degree D_f and spectral sparsity omega. The methodology is constructive PAC-Bayes and it inverts the usual requirement: rather than needing to know the learned parameters to compute a KL divergence, the authors explicitly build a transformer implementing the target with bounded norm and sharpness, then assume only that the learner finds some interpolator dominated in both quantities. That is strictly less information than knowing the minimum found, at the cost of assuming a dominating construction exists — which they validate empirically. The learner is idealized as minimizing training loss plus a parameter-norm term plus the trace of the Hessian, sharpness being balanced against norm because sharpness alone is parameterization-dependent and can be traded away by rescaling. A 1.5-layer single-head transformer is constructed for low-degree sparse functions. Complexity parameters are estimated by property testing, and a mechanistic interpretability study checks that real trained transformers resemble the construction.

## Results

The generalization gap scales as O(omega * D_f^2) in Fourier sparsity and degree, giving a complexity-theoretic account of why an expressible function may not be learnable. For Parity — the special case of sparsity 1 and degree T — the sharpness-based bound with chain of thought grows only linearly in T, against exponentially without it. Conditions under which the bound is non-vacuous are stated, including lower bounds on the number of training points needed per complexity class.

## Limitations

The learner is idealized: it minimizes loss, norm and Hessian trace directly rather than being SGD, so the result abstracts away training dynamics. The construction assumes all Fourier components share the same degree and positive coefficients, with the general mixed-degree signed case said to follow by adding heads but not carried out. The dominating-construction assumption is validated empirically rather than proved. Scope is boolean domains and sparsity no greater than the context length. The mechanistic study supports realism of the construction rather than establishing that trained transformers implement it.

## Why it matters here

- **reasoning-interpretability**: Unusual for a theory paper in running a mechanistic study to check that its construction resembles what real transformers do, rather than leaving the construction as an existence proof. That is the direction the archive's interpretability thread rarely gets — theory proposing a specific mechanism and then looking for it — and it is the same move the counting paper makes from the opposite side. The flat-minima framing also connects sharpness, a training-dynamics quantity, to what the archive reads off activations.
- **reasoning-training**: Fills the gap the archive's expressivity papers name in their own limitations sections — that they cover what a transformer can represent and say nothing about generalization. This is the missing half, and its headline is the learnability analogue of theirs: for Parity, chain of thought converts an exponential dependence on length into a linear one, so CoT helps not only by adding serial steps but by making the target learnable from feasible data. The bound's shape is the transferable part: generalization degrades with the degree of the target function squared, which predicts that reasoning tasks requiring high-order interactions between inputs need disproportionately more data — a statement about which reasoning problems are hard that does not depend on any particular training recipe.

## Entities

- **Concepts**: [generalization](../../../../wiki/concepts/generalization.md), PAC-Bayes, flat minima, sharpness, Fourier spectrum, [expressivity-learnability gap](../../../../wiki/concepts/expressivity-learnability-gap.md), [sample complexity](../../../../wiki/concepts/sample-complexity.md), parity, low-degree bias, chain of thought
- **Methods**: PAC-Bayes bound, constructive PAC-Bayes, sharpness minimization, property testing, Fourier analysis, mechanistic interpretability
- **Datasets**: [Parity](../../../../wiki/datasets/parity.md)

Tags: `generalization`, `pac-bayes`, `fourier`, `learnability`, `parity`, `theory`

## Abstract

We study transformers' generalization behavior on boolean domains from the perspective of the Fourier spectra of their target functions. In contrast to prior work [11, 25], which derived generalization bounds from Rademacher complexity, we investigate the feasibility of obtaining generalization bounds via PAC-Bayes theory. We show that sparse spectra concentrated on low-degree components enable low-sharpness constructions with good generalization properties. Our idea is to show the existence of flat minima implementing any boolean function of sparsity no greater than the context length, and then apply a PAC-Bayes bound to an idealized low-sharpness learner, resulting in a non-vacuous generalization bound. We use this to give a formal account of why chain-of-thought improves generalization for high-degree target functions, and show that the complexity parameters in our bound can be efficiently estimated via property testing. We make predictions empirically and conduct a mechanistic interpretability study to support the realism of our theoretical construction in real transformers.

---

Record id: `local:03f1eff4f1d40725`
