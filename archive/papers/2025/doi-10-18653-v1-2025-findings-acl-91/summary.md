<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# The Inverse Scaling Effect of Pre-Trained Language Model Surprisal Is Not Due to Data Leakage

- **Authors**: Byung-Doh Oh, Hongao Zhu, William Schuler
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2025.findings-acl.91/>
- **PDF**: <https://aclanthology.org/2025.findings-acl.91.pdf>
- **DOI**: 10.18653/v1/2025.findings-acl.91
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Shows that the well-known inverse-scaling effect -- larger pre-trained language models' word-surprisal predicting human reading times worse than smaller models' -- is not an artifact of training-data leakage: overlap between five naturalistic reading-time corpora and two pre-training corpora is minimal, and models trained from scratch on leakage-free data still replicate the negative size-vs-fit relationship.

## Problem

A negative relationship between LM size and how well the model's word-surprisal predicts human reading times has been observed and speculated to be caused by data leakage (larger models having 'memorized' the exact reading-time stimulus texts during pretraining, artificially lowering their surprisal on them), which would undermine the validity of using pre-trained LMs as psycholinguistic models of human sentence processing.

## Contributions

- a large-scale audit (via CDAWG-based longest-overlap querying) of data leakage between five widely-used naturalistic reading-time corpora and two major LM pre-training corpora (Pile, OpenWebText), finding minimal leakage
- a causal replication showing LMs trained from scratch on leakage-free data still exhibit the negative model-size-vs-reading-time-fit relationship, ruling out leakage as the explanation
- a controlled demonstration that artificially inducing severe leakage (via fine-tuning on the evaluation corpora) would inflate, not create, the negative size-fit relationship -- clarifying what kind of leakage would and would not be a confound

## Method

Study 1 builds Compacted Directed Acyclic Word Graphs (CDAWGs) over two pre-training corpora (the Pile subset used for Pythia, and OpenWebText used for GPT-2) to efficiently query, for every passage in five naturalistic reading-time corpora (Dundee, Brown, GECO, Provo, Natural Stories), the length and frequency of the longest overlapping token n-gram, plus its chance-probability of occurring at that length via a 5-gram KenLM. Study 2 causally tests the leakage hypothesis: identifies leakage-free Pile training chunks (no more than 11 continuous overlapping tokens with any reading-time passage), trains three Pythia-style Transformer LMs (Small/Medium/Large: 28M/70M/162M params) from scratch on this leakage-free data, then artificially reintroduces leakage by fine-tuning each model on the reading-time corpora themselves for 5 and 10 steps, measuring at each stage how well each model's surprisal predicts reading times via linear mixed-effects regression (Delta log-likelihood over a baseline model without LM surprisal) and reporting corpus-level perplexity.

## Results

Except for the Provo corpus, no passage in any reading-time corpus is observed in its entirety in either pre-training corpus, and most highly-overlapping Provo passages occur under 10 times in either pre-training corpus (longer overlaps exceeding 100 tokens occur at most twice) -- interpreted as the reading-time corpora suffering little from data leakage overall. LMs trained on strictly leakage-free data still show a negative relationship between model size and fit to reading times (Delta log-likelihood) across all five datasets before any fine-tuning, replicating the previously reported inverse-scaling pattern and indicating it is not driven by leakage. When leakage is artificially introduced via fine-tuning directly on the reading-time corpora, both perplexity and Delta log-likelihood decrease more for larger models at the same number of fine-tuning updates than for smaller ones -- meaning severe, deliberately-induced leakage would cause an overestimation of the negative size-fit relationship, so genuine (mild, naturally-occurring) leakage is not the explanation, but severe leakage could bias such studies if it existed.

## Limitations

Leakage is evaluated only for English corpora, English-trained LMs, and reading-time data from native English speakers, so replication is needed to assess leakage in other languages. Leakage detection relies mainly on token n-gram overlap, which is insensitive to minor surface-form variations such as paraphrases, so leakage via paraphrased or reformatted text would not be detected. Since OpenWebText is an open-source replication of GPT-2's undisclosed training data, its corpus statistics may differ from GPT-2's actual (proprietary) training data. The work is concerned specifically with using language models as cognitive models of human sentence processing, and does not relate to their use in natural language processing applications.

## Why it matters here

- **overthinking**: Not relevant beyond the shared keyword 'inverse scaling': this is a psycholinguistic-modeling study of whether larger LMs' word-by-word surprisal predicts human reading times worse than smaller LMs', and whether that pattern is a data-leakage artifact, unconnected to LLM reasoning-trace length, test-time compute, or the accuracy/efficiency tradeoff of reasoning that the topic tracks.

## Entities

- **Concepts**: inverse scaling (LM size vs. surprisal-reading-time fit), data leakage (pretraining-corpus overlap with evaluation stimuli), Compacted Directed Acyclic Word Graph (CDAWG) overlap querying, leakage-free training data
- **Methods**: Compacted Directed Acyclic Word Graph (CDAWG) sequence indexing, linear mixed-effects regression (surprisal fit to reading times), leakage-free data filtering, artificial leakage induction via fine-tuning
- **Datasets**: Dundee Corpus, Brown Corpus (Smith and Levy), GECO, [Provo Corpus](../../../../wiki/datasets/provo-corpus.md), Natural Stories, The Pile (Pythia training subset), OpenWebText Corpus (GPT-2 replication)

Tags: `inverse-scaling`, `psycholinguistics`, `data-leakage`, `reading-times`, `surprisal`

## Abstract

In psycholinguistic modeling, surprisal from larger pre-trained language models has been shown to be a poorer predictor of naturalistic human reading times. However, it has been speculated that this may be due to data leakage that caused language models to see the text stimuli during training. This paper presents two studies to address this concern at scale. The first study reveals relatively little leakage of five naturalistic reading time corpora in two pre-training datasets in terms of length and frequency of token n-gram overlap. The second study replicates the negative relationship between language model size and the fit of surprisal to reading times using models trained on ‘leakage-free’ data that overlaps only minimally with the reading time corpora. Taken together, this suggests that previous results using language models trained on these corpora are not driven by the effects of data leakage.

---

Record id: `doi:10.18653/v1/2025.findings-acl.91`
