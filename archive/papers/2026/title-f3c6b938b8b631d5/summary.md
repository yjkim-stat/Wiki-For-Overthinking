<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Scaling Atomistic Protein Binder Design with Generative Pretraining and Test-Time Compute

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10007211>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Proteina-Complexa combines generative pretraining on a new synthetic dataset with inference-time optimization to design atomistic protein binders, reporting higher in-silico success rates than prior generative approaches.

## Problem

Protein binder design for drug discovery has relied on either conditional generative modeling or structure-predictor-based optimization ('hallucination') as separate approaches, each with its own tradeoffs in success rate and compute cost.

## Contributions

- Proteina-Complexa, a fully atomistic binder generation method unifying conditional generative modeling and structure-predictor-based (hallucination) optimization
- Teddymer, a large-scale synthetic binder-target pair dataset for pretraining, combined with experimental multimer data
- Demonstrated applications to hydrogen bond optimization, fold-guided generation, small molecule targeting, and enzyme design

## Method

Proteina-Complexa extends a flow-based latent protein generative architecture, pretrained on the Teddymer dataset of synthetic binder-target pairs and fine-tuned on experimental multimer structures. At inference time, it applies test-time optimization that leverages the learned generative prior, combining the strengths of conditional generative modeling and structure-predictor-based (hallucination) design.

## Results

Proteina-Complexa reports markedly higher in-silico success rates than existing generative approaches on computational binder design benchmarks and outperforms prior methods under constrained compute budgets.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Tangential. The paper shares only the generic keyword 'test-time compute' with the tracked topic: here it denotes inference-time structure optimization for protein binder generation, not reasoning-length control in language models. It contains no treatment of chain-of-thought length, accuracy/efficiency tradeoffs in reasoning traces, or stopping criteria for LLM reasoning, and belongs to protein/structural-biology design rather than LLM reasoning.

## Entities

- **Concepts**: atomistic protein binder design, flow-based generative modeling, generative pretraining for proteins, inference-time optimization
- **Methods**: Proteina-Complexa, flow-based latent protein generation
- **Datasets**: Teddymer (synthetic binder-target pairs), experimental protein multimers

Tags: `protein-design`, `drug-discovery`, `generative-model`, `off-topic`

## Abstract

Abstract Protein interaction modeling is central to protein design, which has been transformed by machine learning with applications in drug discovery and beyond. In this landscape, structure-based de novo binder design is cast as either conditional generative modeling or sequence optimization via structure predictors (``hallucination''). We argue that this is a false dichotomy and propose Proteina-Complexa, a novel fully atomistic binder generation method unifying both paradigms. We extend recent flow-based latent protein generation architectures and leverage the domain-domain interactions of monomeric computationally predicted protein structures to construct Teddymer, a new large-scale dataset of synthetic binder-target pairs for pretraining. Combined with high-quality experimental multimers, this enables training a strong base model. We then perform inference-time optimization with this generative prior, unifying the strengths of previously distinct generative and hallucination methods. Proteina-Complexa sets a new state of the art in computational binder design benchmarks: it delivers markedly higher in-silico success rates than existing generative approaches, and our novel test-time optimization strategies greatly outperform previous hallucination methods under normalized compute budgets. We also demonstrate interface hydrogen bond optimization, fold class-guided binder generation, and extensions to small molecule targets and enzyme design tasks, again surpassing prior methods. Code, models and new data will be publicly released.

---

Record id: `title:f3c6b938b8b631d5`
