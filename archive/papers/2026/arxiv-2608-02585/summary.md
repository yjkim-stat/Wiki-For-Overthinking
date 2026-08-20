<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Time Latent Reasoning

- **Authors**: Zhaoxin Yu, Qi Shen, Hengli Li, Zhaowei Zhang, Song-Chun Zhu, Chi Zhang, Zilong Zheng
- **Venue**: cs.LG
- **Published**: 2026-08-03
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.02585>
- **PDF**: <https://arxiv.org/pdf/2608.02585v1>
- **Topics**: reasoning-faithfulness, test-time-scaling
- **Relevance score**: reasoning-evaluation 0.25, reasoning-faithfulness 0.50, reasoning-training 0.25, test-time-scaling 0.50

## In one line

Inserts optimizable latent states at an intermediate Transformer layer rather than at the output, so self-attention makes every continuation token's log-probability differentiable with respect to every latent and reward-weighted gradients reach them from the whole continuation instead of only through their own decoded token.

## Problem

Test-time latent optimization improves outputs by tuning instance-specific continuous states while the model stays frozen, but existing methods place those latents at the transformer's output and decode them into the first tokens of the continuation. Optimization then has to reach the latents by backpropagating through the decoding step, which is an information bottleneck: each latent's update is tied to the log-probability of its own decoded prefix token, so how a latent contributes to later reasoning and to the final answer cannot be attributed. The credit-assignment problem is therefore the same one dense-reward work faces in training, moved to inference.

## Contributions

- Placing the latents inside the network — concatenated with the prompt's and continuation's hidden states at a chosen layer — so the pre-trained self-attention serves as both the forward computation path and the backward gradient path
- A resulting factorization in which every generated token attends to every latent, so the reward-weighted gradient for each latent aggregates contributions from all continuation positions rather than one
- An ablation that decomposes the gain into three separable parts: inserting a fixed prefix, optimizing it in the selected latent space at all, and using reward-derived rather than random directions
- A token-level gradient attribution showing where latent influence lands, using rule-based categories for continuation tokens
- A layer sweep locating the effective optimization space at 25 to 50 percent of network depth

## Method

For an M-layer decoder, the prompt and the already-generated tokens are passed through the first l layers, and a small set of optimizable latent vectors is inserted between the two resulting hidden-state blocks. The concatenation runs through the remaining layers and the language-model head to give the next-token distribution, so the latents participate in self-attention alongside token representations. The latents are then updated by a policy-gradient step whose gradient sums, over all T continuation positions, the reward times the gradient of that token's log-probability with respect to the latent — the base model's parameters are never touched. Evaluation covers five instruction-tuned backbones, three benchmarks and two answer formats for 30 settings, against chain-of-thought prompting, a one-pass self-reflection baseline, self-consistency, self-scored best-of-N, and LatentSeek as the output-side latent method. Robustness is probed two ways: scaling each method's base learning rate by factors from 0.4 to 1.6, and replacing the reward-derived gradient with Gaussian random directions to give a random-walk variant with no reward guidance.

## Results

Averaged over all 30 settings the method reaches 64.5 percent, 6.6 points above chain-of-thought prompting and 2.4 above the strongest competing method, and is best in 23 of 30. Against the output-side latent baseline it wins every benchmark-format aggregate, by 2.2 and 2.0 points on GPQA-Diamond, 2.5 and 3.8 on GSM8K, and 2.8 and 8.9 on MATH-500. The robustness results are the more interesting half. Across seven learning-rate settings its accuracy moves only from 51.4 to 53.8 percent against 47.6 to 51.8 for the baseline, with standard deviation 0.82 against 1.53. And the random-walk variant — reward guidance removed entirely — averages 60.6 percent against 60.3 for the reward-guided baseline, which the paper reads as evidence that the latent space itself is the robust part and the reward only decides how well it is explored. The ablation separates three contributions cleanly: inserting a fixed prefix moves the average from 60.5 to 62.0 percent but degrades six of fifteen settings, random optimization of that prefix beats the fixed version in 14 of 15, and reward-derived directions add a further 2.4 points to reach 66.6. Gradient attribution puts latent influence on reasoning connectors — tokens like 'because', 'therefore' and 'then' — at 0.308, 0.303 and 0.256 gradient strength across the three benchmarks, well above answer markers, answer content, formatting and content explanation, with answer content lowest on two of three. The layer sweep favours intermediate depth: 25 to 50 percent of the network beats the embedding level on all three benchmarks and 75 percent is worse than either, most visibly on GPQA-Diamond.

## Limitations

The paper has no limitations section. What a reader should weigh: the random-walk result is presented as robustness and is also the sharpest bound on the claim, since a reward-free random direction in this latent space (60.6) nearly matches a reward-guided output-side method (60.3), and reward guidance accounts for only 2.4 of the roughly 6.1-point ablation span. That leaves open how much of the improvement is reasoning being refined as against a well-placed perturbation being selected. The method consumes an instance-level reward signal at inference, and the main text does not say what supplies it — the paper reports only that its optimization-iteration count is lower than the sample counts used by the sampling baselines, which is a compute argument rather than an information one. The interpretability claim rests on the L2 norm of gradients aggregated over rule-based token categories, which is a first-order sensitivity measure rather than a causal test, and no intervention confirms that perturbing connector tokens changes the outcome. Backbones are five instruction-tuned models at 3B to 14B on three benchmarks, and apart from the learning-rate sweep no seeds or variance are reported for any table.

## Why it matters here

- **reasoning-faithfulness**: The gradient attribution is the part that bears on faithfulness, and it points the same way as this archive's other latent-reasoning evidence. Optimizing a latent state changes reasoning connectors far more than answer content — 0.303 against 0.018 on GSM8K — so what the intervention moves is the shape of the trace rather than the conclusion it reports. Read alongside the archive's finding that trace content is often not what produces the answer, that is a second route to the same place: the connective tissue of a chain is what an internal intervention has purchase on, which is exactly the part a reader would take as evidence of reasoning. The case study points the other way and is worth keeping for it: the output-side method visibly corrupts the decoded text while getting the answer wrong, whereas this one corrects the answer without altering the token sequence — a reminder that an unchanged-looking trace is not evidence that nothing was intervened on.
- **test-time-scaling**: It is a test-time method whose ablation is more informative than its benchmark table. Three effects are separated at fixed inference budget — inserting a prefix, optimizing it, and optimizing it with reward — and only the last is what the method claims to be about, worth 2.4 of the points. The random-direction control is the piece other test-time-scaling work in this archive rarely runs: it establishes that most of the gain is available without the guidance signal, which is the same shape as the archive's finding that a perturbation-based selection rule was beaten by a format-matched control. The layer sweep also gives a concrete design fact — the usable optimization space is at 25 to 50 percent of depth, with the embedding level and the last quarter both worse — and the iteration counts are below the sample counts of self-consistency and best-of-N, so the comparison is at least argued on budget rather than assumed.

## Entities

- **Concepts**: latent reasoning, [credit assignment](../../../../wiki/concepts/credit-assignment.md), [test-time compute](../../../../wiki/concepts/test-time-compute.md), [test-time scaling](../../../../wiki/concepts/test-time-scaling.md), policy gradient, self-attention, circuit analysis, gradient attribution, reasoning connector
- **Methods**: GradCuit, LatentSeek, [self-consistency](../../../../wiki/methods/self-consistency.md), [best-of-N](../../../../wiki/methods/best-of-n.md), [self-reflection](../../../../wiki/methods/self-reflection.md), [chain-of-thought prompting](../../../../wiki/methods/chain-of-thought-prompting.md), prefix tuning
- **Datasets**: [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH-500](../../../../wiki/datasets/math500.md)

Tags: `latent reasoning`, `test-time optimization`, `credit assignment`, `interpretability`, `attention`

## Abstract

Optimization-based latent reasoning improves large language model outputs by optimizing instance-specific continuous states at test time while keeping model parameters frozen. Existing methods, however, typically connect these states to the reasoning trajectory through decoded tokens, making sequence-level credit assignment indirect and obscuring how latent updates shape subsequent reasoning. We introduce GradCuit (gradient through circuit), which inserts optimizable latent states at a selected Transformer layer between the hidden representations of the prompt and the generated continuation. Causal self-attention provides every continuation-token log-probability with a differentiable path to every preceding latent state through the remaining Transformer blocks, enabling reward-weighted gradients from the entire continuation to be assigned directly to the latents. Across five instruction-tuned backbones, three reasoning benchmarks, and two answer formats, GradCuit achieves an average accuracy of 64.5%, outperforming chain-of-thought prompting by 6.6 percentage points and the strongest competing method by 2.4 points. GradCuit also demonstrates greater robustness: across seven learning-rate settings, it consistently outperforms LatentSeek while reducing the standard deviation of accuracy from 1.53 to 0.82, and even its random-walk variant remains competitive with LatentSeek. For interpretability, token-level gradient attribution reveals that latent influence concentrates on reasoning-connector tokens, while layer analysis identifies early-to-middle Transformer layers as the most effective optimization space. By directly optimizing internal reasoning from outcome feedback, GradCuit opens a new axis of robust and interpretable test-time scaling, where LLMs adapt how they reason rather than merely regenerate, sample, or rerank outputs.

---

Record id: `arxiv:2608.02585`
