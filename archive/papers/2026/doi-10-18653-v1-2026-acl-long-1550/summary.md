<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Memory efficiency and resource-rational encoding in sentence processing

- **Authors**: Weijie Xu, Brian Dillon, Richard Futrell
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1550/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1550.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1550
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Models human working-memory (WM) constraints in a GPT-2-small language model by injecting Gaussian noise into self-attention value vectors (with precision decaying exponentially by query-key distance) and training with a hybrid objective that trades off next-word prediction against total encoding precision, finding this explicit WM constraint improves alignment with human reading times and reshapes next-word predictions into a more compressed, categorical representational space.

## Problem

Language models used as cognitive models of human sentence processing need to be constrained in their use of memory for context, analogous to human working memory, but the exact representational nature of WM constraints -- what information is lost, and how -- remained theoretically underspecified and had mostly been implemented ad hoc (reduced model/training-data size, locally biased attention) rather than derived from a principled resource-rational account.

## Contributions

- a computational-level formalization of working-memory constraint as representational uncertainty (Gaussian noise with distance-decaying precision) injected into Transformer self-attention, trained via a hybrid next-word-prediction / encoding-precision-penalty objective
- evidence that explicit, resource-rational WM constraint improves alignment between model surprisal estimates and human reading times on at least some corpora/measures, without requiring ad hoc architectural restrictions
- evidence that stronger WM constraint reshapes the model's next-word-prediction representational space to be more compressed and, for some linguistic features (temporal/spatial prepositions), more categorically clustered
- a documented dissociation between locally biased attention (retrieval) and encoding precision (representational quality) under WM constraint, suggesting locality bias in retrieval alone does not fully characterize WM processes

## Method

Injects Gaussian noise into Transformer self-attention value vectors, so the noisy value at key position k for query q is sampled from a distribution whose precision (inverse variance) decays exponentially with query-key distance at a learnable rate theta per attention head and layer -- implementing representational uncertainty rather than a binary forget/retain decision. Trains five GPT-2-small-architecture language models on WikiText-103 with a hybrid loss combining next-word cross-entropy with an explicit penalty (weighted by lambda in {0, 0.001, 0.01, 0.1, 1}) on total encoding precision (a proxy for WM resource cost), so stronger lambda forces more aggressive resource-rational compression. Evaluates (1) the learned precision-decay pattern across layers/heads, (2) the models' surprisal estimates' predictive power (delta log-likelihood over a no-surprisal baseline) for human reading times on three English corpora (Provo eye-tracking, SPR Natural Stories, A-Maze Natural Stories), and (3) via PCA on next-word log-probability distributions, whether stronger WM constraint produces a more compressed and more categorically clustered representational space (using an animacy manipulation and a temporal-vs-spatial preposition manipulation as test features).

## Results

With no WM constraint (lambda=0), all attention heads learn a precision-decay rate near 0 (using the full context). As WM constraint strengthens, precision decay first emerges asymmetrically in lower-layer attention heads (processing local morphosyntactic features) before diffusing to higher-layer heads (processing longer-range discourse) at stronger constraint levels. Explicit WM constraint improves psychometric predictive power on human reading times, most clearly on the SPR Natural Stories corpus (a moderate constraint of lambda=0.01 outperforms the unconstrained baseline GPT-2) and mildly for Provo's first-fixation durations, though this improvement is not observed for Provo total reading time or the A-Maze corpus, and does not increase monotonically with lambda -- consistent with a hypothesized 'Goldilocks' effect where human WM is constrained but not infinitely so. Stronger memory constraint yields less extreme surprisal estimates (fewer very-low-surprisal predictions, more mass at moderate surprisal 5-15) and higher model perplexity on the RT corpora, tracking prior findings that overly confident/accurate next-word prediction can align worse with human reading behavior. All noisy models show more locally biased attention than the unconstrained baseline, but this locality bias does not increase monotonically with lambda and weakens again at higher constraint levels -- evidence the paper reads as a dissociation between WM retrieval bias (locality in attention) and the underlying representational encoding (precision), since the representational compression continues to increase with lambda even where the locality-bias effect plateaus or reverses. In the representational-space experiment, the PCA-reduced space of next-word predictions becomes increasingly compressed (lower pairwise item-to-item distance) as lambda grows, and a categorical cluster structure emerges for temporal-vs-spatial prepositions (higher silhouette score) at lambda >= 0.01, though the same categorical emergence is not observed for the animacy feature on the manipulated subject noun.

## Limitations

The model is built on GPT-2 small's parallel (non-incremental) Transformer computation, which does not truly resemble the word-by-word incremental updating of human sentence processing, though the paper notes recent State Space Model advances could address this in future work. The model assumes linear query-key distance is the primitive dimension of memory decay, insensitive to the hierarchical constituent structure of language that a substantial body of work argues is central to how proximate tokens are actually represented mentally. There is no established linking hypothesis between the model's lambda parameter and an actual quantitative level of human WM constraint, making it difficult to predict a priori which lambda value should best align with human behavior -- observed empirically post hoc instead. The study is based on a single, relatively small English-only model (GPT-2 small) trained on WikiText-103; cross-linguistic generalization and larger/different architectures are left to future work.

## Why it matters here

- **overthinking**: Not relevant to the topic: this is a psycholinguistic/cognitive-modeling study of human working-memory constraints during sentence comprehension, using a small GPT-2 model as a scientific instrument rather than studying large reasoning models, test-time compute, or reasoning-trace length at all. It appears to have matched the topic's collection keywords only via generic terms like 'resource-rational' or 'memory efficiency.'

## Entities

- **Concepts**: resource-rational working memory constraint, representational uncertainty (Gaussian noise injection), precision-decay rate (theta), categorical vs. fine-grained encoding under memory constraint
- **Methods**: Gaussian noise injection into self-attention value vectors, resource-rational hybrid training objective (cross-entropy + encoding-precision penalty), surprisal-based psychometric predictive power (delta log-likelihood), PCA-based representational-space analysis
- **Datasets**: WikiText-103 (training), Provo Corpus, SPR Natural Stories Corpus, A-Maze Natural Stories Corpus (MazeNSC)

Tags: `working-memory`, `psycholinguistics`, `cognitive-modeling`, `sentence-processing`, `resource-rationality`

## Abstract

There is a growing consensus that, in order to serve as models of human language processing, language models (LMs) need to be constrained in their use of memory for context, the analogue to human working memory (WM). Here we take a novel yet simple approach to constraining WM in language models, in a way that reflects models of human cognition where memory is treated as a limited resource and deployed strategically. In order to capture this constraint on memory encoding, we inject noise into the hidden representations of Transformer-based LMs at tunable rates. Then we train the models with a hybrid objective, such that they learn to maximize the performance of next-word prediction subject to explicit constraints on the total encoding precision. We find that explicit WM constraints improve the model’s alignment with human reading times. More importantly, we find that the need to manage encoding precision reshapes the nature of the models’ context representations, making them more compressed and categorical. Our results show how resource-rational models of WM allocation can be implemented in neural models simply and successfully, and point to a dissociation between WM retrieval mechanisms and the underlying memory representations in models of human sentence processing.

---

Record id: `doi:10.18653/v1/2026.acl-long.1550`
