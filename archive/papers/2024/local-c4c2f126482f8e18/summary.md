<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Chain of Thought Empowers Transformers to Solve Inherently Serial Problems

- **Authors**: Zhiyuan Li, Hong Liu, Denny Zhou, Tengyu Ma
- **Venue**: preprint
- **Published**: 2024-01-01
- **Source**: local
- **Topics**: reasoning-training, test-time-scaling
- **Relevance score**: reasoning-training 0.50, test-time-scaling 0.50

## In one line

Proves a tighter no-CoT upper bound of AC^0 for constant-precision transformers, and shows T steps of chain of thought let a constant-depth model compute anything a size-T boolean circuit can.

## Problem

Chain of thought works and the mechanism is unclear. The paper's hypothesis is that a transformer's serial computation is bounded by its depth, which is fixed by the architecture, so problems that are inherently serial are out of reach however wide the model is — and that intermediate tokens lift that bound because each one is another serial step.

## Contributions

- A tighter upper bound: constant-depth transformers with constant-bit precision solve only AC^0, a proper subset of the previously established TC^0
- A precision model that handles floating-point rounding rather than assuming infinite or fixed-point arithmetic
- The result that T steps of CoT plus O(log n) embedding size express any size-T boolean circuit, hence P/poly with polynomial steps
- The consequence that linear steps compute all regular languages, including composition of the non-solvable group S_5
- A proof that logarithmic CoT steps do not exceed AC^0
- Empirical confirmation on modular addition, permutation composition, iterated squaring and the circuit value problem, separating parallel-friendly from inherently serial tasks

## Method

Expressivity is analysed in circuit complexity. Crucially the precision model is constant-bit floating point following IEEE 754, with correct rounding and summation defined as a chain of rounded binary additions in fixed order — chosen because 16- or 32-bit arithmetic is what is deployed and because prior bounds assumed infinite or log precision and only really covered fixed-point addition. The problem class solvable with a given CoT length and embedding size is defined as CoT[T(n), d(n)], and results are stated as inclusions between those classes and standard circuit classes. Four tasks are then learned from synthetic data with and without CoT, and with a hint but no CoT, at varying depth.

## Results

Without CoT, constant-depth constant-precision transformers solve only AC^0, a proper subset of the TC^0 bound established by prior work under weaker precision assumptions. With T steps of CoT, constant-depth constant-precision transformers with O(log n) embedding size express anything computable by a boolean circuit of size T; polynomially many steps therefore reach P/poly, a superclass of P, and linearly many steps compute all regular languages including composition of the non-solvable group S_5, which is not in AC^0 and is conjectured outside TC^0. Logarithmically many CoT steps do not permit computing beyond AC^0. Empirically, on modular addition — which lies in TC^0 and is parallel-friendly — depth 1 suffices without CoT, while on permutation composition, iterated squaring and the circuit value problem the vanilla transformer needs very large depth or fails outright, and CoT solves them once depth exceeds a small threshold.

## Limitations

The lower-bound constructions say what a transformer can represent, not what gradient descent finds; the empirical section trains on large synthetic datasets and does not address whether such solutions are learnable at realistic data scales. Embedding size enters the theorems, so the headline result requires O(log n) width rather than being width-free. Summation is modelled as a fixed-order chain of rounded additions and the paper leaves tree-order summation to future work. The separations rest on standard conjectures — that AC^0, TC^0 and NC^1 do not collapse. Layer normalization is omitted from the analysed architecture and its treatment deferred to an appendix.

## Why it matters here

- **reasoning-training**: Its precision model is the contribution this topic should note: moving from log-precision to constant-bit floating point tightens the no-CoT bound from TC^0 to AC^0, which means the deployed arithmetic is a real part of the limit rather than an idealization detail. That connects to the archive's evidence that hardware and precision shift measured reasoning accuracy by up to 9 percentage points — the same variable appears in the theory and in the measurement noise, from opposite directions.
- **test-time-scaling**: Converges independently with Merrill and Sabharwal's characterization, which the archive now holds alongside it: both find logarithmic steps buy nothing and linear steps buy the qualitative jump. That two groups reach the same regime boundaries through different precision models is stronger evidence than either alone. This paper adds the practically pointed part — the tasks CoT rescues are exactly the ones that are hard to parallelize, and on a task that parallelizes (modular addition) depth 1 already suffices and CoT is unnecessary. That is a usable predictor of when spending inference compute will pay.

## Entities

- **Concepts**: [expressivity](../../../../wiki/concepts/expressivity.md), [circuit complexity](../../../../wiki/concepts/circuit-complexity.md), serial computation, [effective depth](../../../../wiki/concepts/effective-depth.md), chain of thought, [finite precision](../../../../wiki/concepts/finite-precision.md), parallel versus serial, non-solvable group
- **Methods**: circuit complexity analysis, [chain of thought](../../../../wiki/methods/chain-of-thought.md), constant-precision floating point modelling, synthetic task training
- **Datasets**: modular addition, permutation composition, iterated squaring, circuit value problem

Tags: `expressivity`, `circuit complexity`, `serial computation`, `theory`, `chain of thought`

## Abstract

Instructing the model to generate a sequence of intermediate steps, a.k.a., a chain of thought (CoT), is a highly effective method to improve the accuracy of large language models (LLMs) on arithmetics and symbolic reasoning tasks. However, the mechanism behind CoT remains unclear. This work provides a theoretical understanding of the power of CoT for decoder-only transformers through the lens of expressiveness. Conceptually, CoT empowers the model with the ability to perform inherently serial computation, which is otherwise lacking in transformers, especially when depth is low. Given input length n, previous works have shown that constant-depth transformers with finite precision poly(n) embedding size can only solve problems in TC0 without CoT. We first show an even tighter expressiveness upper bound for constant-depth transformers with constant-bit precision, which can only solve problems in AC0, a proper subset of TC0. However, with T steps of CoT, constant-depth transformers using constant-bit precision and O(log n) embedding size can solve any problem solvable by boolean circuits of size T. Empirically, enabling CoT dramatically improves the accuracy for tasks that are hard for parallel computation, including the composition of permutation groups, iterated squaring, and circuit value problems, especially for low-depth transformers.

---

Record id: `local:c4c2f126482f8e18`
