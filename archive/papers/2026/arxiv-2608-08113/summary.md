<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Think Deep, Speak Once: Relit, A Recursive Latent Implicit Transformer Framework

- **Authors**: Abhishek Panwar, Maheep Singh, Saksham Bansal
- **Venue**: cs.AI
- **Published**: 2026-08-08
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.08113>
- **PDF**: <https://arxiv.org/pdf/2608.08113v1>
- **Topics**: reasoning-evaluation, reasoning-faithfulness, reasoning-training
- **Relevance score**: reasoning-evaluation 0.40, reasoning-faithfulness 0.40, reasoning-training 0.40, test-time-scaling 0.25

## In one line

Bolts a small trainable recurrent block between a frozen 1.1B language model's body and its output head, so reasoning happens as repeated refinement of two latent vectors rather than as generated tokens.

## Problem

Chain-of-thought forces every atomic reasoning step through discrete tokens, which is expensive and arguably lossy -- a high-dimensional internal state is collapsed into low-bandwidth text, and compute is spent on syntax. Latent reasoning keeps the steps in continuous space instead, but the small recursive models that do this well are trained from scratch on symbolic tasks and cannot handle natural language, while training a recursive language reasoner from scratch is prohibitively expensive. The gap is an architecture that has both.

## Contributions

- A tripartite state -- a frozen semantic anchor, an answer state and a latent scratchpad -- so the anchor cannot drift however deep the recursion goes
- Residual state refinement: each step computes a delta added to the existing state rather than regenerating it, which is the stated departure from the recursive models it borrows from
- A recall-then-learn protocol that runs the recursion gradient-free and takes one gradient step on the settled state, bounding memory independently of depth
- Adaptive halting, with the reported halting depth rising with task complexity

## Method

A prompt passes once through a frozen TinyLlama-1.1B; the last-layer representation becomes a static semantic anchor that is held constant for the whole recursion, so the reasoning block can work on logic alone without losing the prompt. Two states evolve: an answer state initialized as a copy of the anchor, and a latent scratchpad initialized from a learnable Gaussian and free to hold intermediate logic that need not map to any valid output. Each step concatenates the anchor with both states, passes them through a small pre-normalized transformer block with RMSNorm and a SwiGLU feed-forward, and adds the result back -- so the block is a differential engine that sculpts the answer rather than regenerating it, which the paper argues keeps gradients flowing and stops semantic information vanishing over long thinking cycles. Depth is decoupled from memory by a two-phase protocol: the recursion runs with gradients disabled until the state settles, then a single gradient-enabled update is taken on the matured state with the previous one detached, which is truncated backpropagation through time. Deep supervision applies cross-entropy to the answer state at every macro-step so intermediate states stay aligned with the target, and an adaptive-computation-time head predicts a halting probability that masks and scales the loss for samples that have converged. The final answer state is projected back to vocabulary through the frozen output head, which the paper frames as anchoring the block's reasoning to the base model's semantic map; a trainable decoder is offered as an alternative at higher cost. Only the recursive block is trained. Evaluation is on five GLoRE datasets spanning propositional logic, counterfactual reasoning and multi-hop path planning, with training-set sizes from 200 to 5,000.

## Results

The split by task type is stark and the paper does not dwell on it. On the two theorem-finding sets ReLIT reaches 97.60 on RuleTaker and 98.60 on ProofWriter, far above every model in the comparison -- the best reasoning LLM listed manages 78.10 and 82.40. On the three natural-language-inference sets it is the weakest or near-weakest entry: 53.43 on HELP, 56.30 on TaxiNLI and 55.20 on NaN-NLI, against 63.69/81.41/71.55 for the strongest listed reasoning model and 90.02 on NaN-NLI for a fine-tuned RoBERTa. The reported average of 72.23 therefore sits just below the reasoning LLMs at 73.23 to 75.92, and is composed of two saturated wins and three losses. Halting depth rises with task difficulty as claimed: 3.6 steps on ProofWriter, 5.2 on RuleTaker, 6.8 on HELP and 7.8 on the 200-sample NaN-NLI, which the paper reads as the model allocating more internal recursion when the linguistic signal is thin. The qualitative figure traces the answer state moving through intermediate logical predicates before settling on the verdict, presented as evidence that the latent trajectory performs the deduction geometrically.

## Limitations

No limitations section, and the central comparison does not support the claim it is used for. ReLIT is **trained on each dataset's training split** -- 5,000 ProofWriter examples, 5,000 RuleTaker, 800 HELP, 2,000 TaxiNLI -- while every LLM number in the same table is taken from GLoRE under few-shot prompting. The paper says as much when introducing the setup and then tabulates the two side by side, so 'matching or outperforming significantly larger models' is a comparison between a task-specific trained head and models that saw no training data. On the two tasks where the training set is large and the label space is a verdict, ReLIT reaches 97-99 percent; on the three where it is small or the task is linguistic, it does not. Second, the repeated inference that stability implies correctness is not supported: 'the outputs remain consistent after this stabilization phase' and 'high confidence in the final supervision loops proves that the model is not hallucinating' conflate convergence with being right, and this archive holds a direct counter-case in work showing intermediate answers stabilize regardless of whether the answer is ultimately correct. Third, one backbone, one scale, no seeds or variance anywhere, and no ablation separating the residual-refinement novelty from deep supervision, adaptive halting or the frozen head. Finally, the efficiency argument is asserted rather than measured -- no latency, token or FLOP comparison against chain-of-thought appears, though avoiding token generation is the paper's motivation.

## Why it matters here

- **reasoning-evaluation**: A case where the benchmark table is the finding. The average that carries the abstract's claim is built from two near-saturated logic sets and three NLI sets on which the method is the weakest entry, and the rows being compared were produced under different supervision regimes -- trained-on-task against few-shot. This archive already holds that an evaluation apparatus inherited from prior work is an experimental variable rather than a fixed point; here the apparatus is inherited from a benchmark paper and the new row is not commensurable with it.
- **reasoning-faithfulness**: The claim that latent-state stabilization proves the model is not guessing is the strongest version of an inference this archive has repeatedly found unsupported. Answer stability is a property of the model's convergence, not of its correctness, and the archive's own certainty-based serving work states outright that intermediate answers stabilize whether or not the final answer is right. Worth keeping as the clearest recent example of the confusion.
- **reasoning-training**: An intermediate case for the archive's latent-reasoning dispute. The from-scratch models in the superposition study do exhibit genuine parallel latent computation while fine-tuned latent reasoners on a pretrained backbone do not; ReLIT is neither -- a from-scratch recurrent block on a frozen pretrained anchor -- and its results split exactly along that seam, excelling where the task is symbolic and failing where it is linguistic.

## Entities

- **Concepts**: [latent reasoning](../../../../wiki/concepts/latent-reasoning.md), recurrent depth, implicit chain of thought, semantic drift, adaptive computation time, deep supervision, [answer stabilization](../../../../wiki/concepts/answer-stabilization.md), residual refinement, parameter efficiency
- **Methods**: truncated backpropagation through time, [Coconut](../../../../wiki/methods/coconut.md), [chain-of-thought prompting](../../../../wiki/methods/chain-of-thought-prompting.md), RMSNorm, SwiGLU, adaptive halting
- **Datasets**: GLoRE, ProofWriter, RuleTaker, HELP, NaN-NLI, TaxiNLI

Tags: `latent-reasoning`, `recurrence`, `efficiency`, `logical-reasoning`, `small-models`

## Abstract

Chain-of-Thought (CoT) prompting has become the dominant paradigm for eliciting reasoning in Large Language Models (LLMs), yet it creates substantial computational overhead by forcing models to externalize intermediate reasoning steps as discrete tokens. Recent latent reasoning approaches attempt to internalize this process within continuous hidden states. One of the latest advancements in the field of latent reasoning, Tiny Recursive Models (TRMs) excel at symbolic reasoning but struggle to preserve semantic coherence in natural language settings. To bridge this gap, we introduce ReLIT (Recursive Latent Implicit Transformer), a hybrid framework that grounds deep recursive reasoning within the rich semantic representations of a foundational model. ReLIT augments a frozen LLM backbone (TinyLlama-1.1B) with a lightweight, trainable recursive block that iteratively refines its latent thinking (z) before committing to a final output, structurally solving linguistic intuition from algorithmic processing and enabling "deep thinking" via gradient-isolated recurrent loops without the latency of explicit token generation. Empirically, ReLIT achieves high parameter efficiency on the GLoRE logical reasoning benchmark, matching or outperforming significantly larger models on challenging tasks such as ProofWriter and RuleTaker despite minimal supervision. These results demonstrate that reasoning capability can be scaled efficiently through recurrent depth rather than parameter width, offering a principled framework for semantically grounded implicit reasoning.

---

Record id: `arxiv:2608.08113`
