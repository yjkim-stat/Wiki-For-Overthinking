<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# RAEE: A Robust Retrieval-Augmented Early Exit Framework for Efficient Inference

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10010491>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

RAEE decides which transformer layer to exit at by retrieving the exit behaviour of similar training examples from a pre-built database, instead of training internal classifiers or using heuristics.

## Problem

Layer-wise early exit reduces LLM inference cost by stopping the forward pass at an intermediate layer, but existing exit policies either train internal classifiers (large training overhead) or use heuristics (accuracy loss). The paper frames choosing an exit layer as an open problem of predicting, for a given input, the distribution over which layer would already give the correct prediction.

## Contributions

- Formulates the early-exit decision as predicting a distribution over exit layers, and argues that distribution can be approximated from the exit information of similar data
- A procedure for collecting exit information of correct predictions and building a retrieval database and index from it
- RAEE, which uses retrieved exit information both to pick the exit layer and to correct the prediction at that intermediate layer, without training internal classifiers
- Zero-shot evaluation over eight downstream tasks and four backbones, with database build cost under 2 minutes on one RTX 4090

## Method

The paper models early exit as a distribution prediction problem: for an input, predict the distribution over exit layers that yield a correct answer. It approximates that distribution using exit information from similar data. Offline, the authors run the backbone over a corpus, record for each example the layers at which the prediction was correct, embed the examples, and build a retrieval database plus a similarity index. At inference, the input is embedded, its nearest neighbours are retrieved, and their recorded exit information both selects the exit layer and supplies corrective exit information used at the intermediate layer to adjust the backbone's prediction. No internal classifiers are trained.

## Results

Evaluated on eight classification tasks (SST-2, SST-5, MR, CR, MPQA, SUBJ, TREC, CoLA) with four backbones. With RoBERTa-Large, RAEE reports average accuracy 63.41 against baselines in the 35.75-54.05 range; with Llama-3-8B, 57.39 against baselines in the 36.06-41.80 range. For the billion-parameter backbones (Llama-3-8B, Gemma-7B) the paper reports inference latency reduced by roughly half; for the smaller (million-parameter) backbones the speedup is described as modest because baseline inference was already fast. Building the retrieval database takes under 2 minutes on a single RTX 4090; database and index storage average 3.4MB and 2.1MB per task.

## Limitations

The paper states no explicit limitations section. Points a reader should notice: the gains are measured on eight sentence-level classification tasks in a zero-shot setting, not on open-ended generation or multi-step reasoning; the accuracy comparison is against other early-exit policies on the same backbone rather than against the full-depth model at every layer budget, so how much of the 63.41 vs 54.05 gap is exit-policy quality and how much is the corrective retrieved information is not separated in the headline number; the method requires a labelled corpus to record correct-prediction exit layers, so it presumes per-task offline preparation; and the retrieval step itself adds latency that the near-halved latency figure must be read as already including.

## Why it matters here

- **overthinking**: Tangential: the archive matched on the keyword 'early exit', but here that means exiting the transformer's layer stack partway through a single forward pass on sentence classification tasks, not stopping a reasoning chain. There is no reasoning trace, no test-time compute scaling, and no notion of a model thinking longer than a problem needs. The only shared idea is per-instance allocation of compute according to how easy the input looks, and RAEE's version of it is depth rather than length. Nothing here transfers to reasoning-length control without re-deriving the method for generation.

## Entities

- **Concepts**: Early Exit, Retrieval-Augmented Inference, Adaptive Inference Depth, Exit Layer Distribution Prediction, Inference Efficiency
- **Methods**: RAEE, [early exit](../../../../wiki/methods/early-exit.md), retrieval-augmented inference, k-nearest-neighbour retrieval, RoBERTa-Large, [T5-Large](../../../../wiki/methods/t5-large.md), [Llama-3-8B](../../../../wiki/methods/llama-3-8b.md), Gemma-7B
- **Datasets**: [SST-2](../../../../wiki/datasets/sst-2.md), SST-5, MR, CR, MPQA, SUBJ, TREC, CoLA

Tags: `early-exit`, `inference-efficiency`, `retrieval`, `adaptive-computation`, `classification`

---

Record id: `title:5e9b243e4d404cc8`
