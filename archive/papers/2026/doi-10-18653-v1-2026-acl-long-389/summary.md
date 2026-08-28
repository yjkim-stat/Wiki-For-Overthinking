<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Revisiting Model Interpolation for Efficient Reasoning

- **Authors**: Taiqiang Wu, Runming Yang, Tao Liu, Jiahao Wang, Ngai Wong
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.389/>
- **PDF**: <https://aclanthology.org/2026.acl-long.389.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.389
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

Reveals that linear interpolation between an Instruct model's and a Thinking model's weights does not trade off performance and reasoning verbosity smoothly, but follows a predictable three-stage transition (Instruct-dominated -> abrupt thinking-pattern emergence -> converging to Thinking with diminishing/overthinking returns), and shows a strategically chosen interpolation point beats sophisticated model-merging baselines (task arithmetic, TIES) on both efficiency and accuracy.

## Problem

Model merging between a long-CoT 'Thinking' model and a short-CoT 'Instruct' model is a popular way to build efficient hybrid reasoners, but the simplest merging method -- direct linear weight interpolation -- had not been systematically analyzed to understand how performance and reasoning verbosity actually evolve as the interpolation coefficient sweeps from 0 to 1, leaving practitioners without principled guidance for navigating the performance-cost trade-off.

## Contributions

- a systematic revisiting of linear model interpolation between Instruct and Thinking models, showing performance and verbosity follow a predictable three-stage paradigm rather than evolving linearly
- identification of the abrupt phase-transition stage as a favorable performance-cost sweet spot, and the final convergence stage as an explicit, controllable demonstration of overthinking
- empirical evidence that a strategically interpolated model surpasses more sophisticated merging baselines (Task Arithmetic, TIES-Merging, DARE, SLERP) on accuracy, token efficiency and controllability simultaneously
- layer- and module-level ablations localizing long-CoT reasoning: FFN sublayers in the later two-thirds of the network drive the thinking pattern's emergence, while MHA sublayers govern reasoning correctness

## Method

Defines model interpolation (MI) as Theta_merge = lambda*Theta_Thinking + (1-lambda)*Theta_Instruct, and shows algebraically this is equivalent to task arithmetic with scaling factors lambda and (1-lambda) applied to the Thinking and Instruct task vectors relative to any base model. Sweeps lambda from 0 to 1 on Qwen3-4B and Qwen3-30B-A3B, evaluating Pass@k, Mean@k, Vote@k, token count and Thinking Ratio (fraction of responses containing a think token) across AIME'25, IFEval and GPQA-Diamond. Compares against Task Arithmetic, TIES-Merging, DARE and SLERP baselines, and conducts layer-wise and module-wise (MHA vs. FFN) ablations to localize where the thinking pattern is stored.

## Results

MI follows a consistent three-stage evolution rather than a linear one: Stage 1 (lambda approx 0-0.4) is Instruct-dominated, Think Ratio near 0 but token count and Pass@k grow gradually with no explicit reasoning. Stage 2 (lambda approx 0.4-0.6) is a sharp phase transition -- Think Ratio abruptly rises from near 0 to 1, Mean@k jumps sharply (AIME'25 Mean@64 55.8->71.0) while Pass@k grows only gently and token count briefly decreases, marking an efficiency/effectiveness sweet spot; the merged model at lambda=0.8 can even outperform the pure Thinking model. Stage 3 (lambda approx 0.6-1.0) converges toward the pure Thinking model with continuously increasing token count but only marginal or plateauing Mean@k/Pass@k gains -- explicit evidence of overthinking. MI-0.8 achieves state-of-the-art results versus TA/TIES baselines on all three benchmarks (AIME'25 Mean@64 80.5, 10.9 points above the best TA baseline) and needs only 1556 tokens on IFEval versus 2810 for the best TA baseline at comparable or better accuracy. Layer-wise ablation shows interpolating only the last two-thirds of the model's 36 layers reproduces near-full performance while any one-third alone fails to induce thinking behavior. Module-wise ablation shows skipping FFN sublayers collapses Think Ratio from 99.95% to 0.68% (FFN drives long-CoT pattern emergence), while skipping MHA leaves Think Ratio nearly unchanged but drops Mean@64 from 80.47 to 71.46 (MHA is needed for reasoning quality, not the pattern itself). Substituting the Instruct backbone with the pretrained base model collapses AIME'25 Mean@64 from 80.5 to 67.7 despite similar Pass@64, indicating instruction-following alignment in the non-thinking backbone matters for merged-reasoning quality.

## Limitations

Empirical validation is centered on the Qwen3 family (4B and 30B-A3B, plus a confirmatory Llama-3.1-8B check); whether the three-stage dynamic generalizes to other model families (e.g. Mistral) is left as future work. The study interpolates only two models (Instruct and Thinking); extending to three or more specialist models is an open direction not explored.

## Why it matters here

- **overthinking**: Central to the topic: gives a mechanistic, quantitative account of overthinking-like diminishing returns in model merging -- as the interpolation coefficient pushes a hybrid model toward the pure Thinking model, token count keeps rising while Mean@k/Pass@k plateau, explicitly identified by the paper as overthinking. Its finding that an intermediate interpolation point can outperform the pure Thinking model, and its layer/module localization of the thinking pattern to specific FFN sublayers, offer both a practical training-free efficiency lever and mechanistic grounding for why blending in non-thinking behavior can regularize away some overthinking.

## Entities

- **Concepts**: model interpolation (linear weight merging), three-stage evolutionary paradigm, Thinking Ratio (Think #R), layer- and module-localized reasoning capability
- **Methods**: Model Interpolation (MI), Task Arithmetic (TA, baseline), TIES-Merging (baseline), DARE (baseline), SLERP (baseline)
- **Datasets**: [AIME'25](../../../../wiki/datasets/aime-2025.md), [IFEval](../../../../wiki/datasets/ifeval.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md)

Tags: `overthinking`, `model-merging`, `efficient-reasoning`, `controllable-reasoning-length`, `mechanistic-interpretability`

## Abstract

Model merging, typically on Instruct and Thinking models, has shown remarkable performance for efficient reasoning. In this paper, we systematically revisit the simplest merging method that interpolates two weights directly. Particularly, we observe that model interpolation follows a three-stage evolutionary paradigm with distinct behaviors on the reasoning trajectory. These dynamics provide a principled guide for navigating the performance-cost trade-off. Empirical results demonstrate that a strategically interpolated model surprisingly surpasses sophisticated model merging baselines on both efficiency and effectiveness. We further validate our findings with extensive ablation studies on model layers, modules, and decoding strategies. Ultimately, this work demystifies model interpolation and offers a practical framework for crafting models with precisely targeted reasoning capabilities.

---

Record id: `doi:10.18653/v1/2026.acl-long.389`
