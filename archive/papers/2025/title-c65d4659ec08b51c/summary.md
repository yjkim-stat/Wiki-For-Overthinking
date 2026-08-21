<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Beyond Greedy Exits: Improved Early Exit Decisions for Risk Control and Reliability

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/118222>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

UAT replaces the static confidence threshold in early-exit deep networks with a multi-armed bandit that adapts the threshold online and unsupervised, reporting 1.70-2.10x speedup at under 2% performance drop.

## Problem

Early-exit networks emit a prediction at an intermediate layer when confidence in the class prediction passes a threshold fixed on a static validation set. The threshold is set once and never revisited, so the model can exit on a class it is overconfident and wrong about, and the calibration does not survive the distribution shifts encountered in deployment.

## Contributions

- UAT, a multi-armed bandit formulation of the exit-threshold decision in early-exit networks, adjusted online without labels
- A reward function combining predictive certainty with a learned reliability estimate and a penalty on unnecessarily late exits
- Stated risk guarantees for the exit policy
- Evaluation across text classification, QA, summarization, translation and vision-language tasks with three backbones

## Method

Each candidate threshold is an arm of a multi-armed bandit; the algorithm keeps UCB indices over arms, balancing empirical mean reward against an exploration bonus, and picks the threshold for each incoming sample. The reward is r(tau) = C_tau^i * (1 - C_g^i) - psi(i): the exit's predictive certainty weighted by a learned reliability (confidence) function, minus a penalty psi(i) that grows with the layer index so that exiting later than necessary is charged for. No labels are needed at deployment, so the adjustment is unsupervised and online. The paper states risk guarantees for the resulting exit policy. The threshold is global across exits rather than per-layer.

## Results

Speedup of 1.70-2.10x with under 2% drop against full-model performance, across GLUE text classification (SST-2, MNLI, RTE, QNLI, QQP), SQuAD 2.0 question answering, summarization (SamSum, CNN/DailyMail, MultiNews, BigPatent), IWSLT translation, and vision-language tasks (image captioning, VQA, visual dialogue). Backbones are BERT-large, T5-large and BLIP-2-ViT-FlanT5-xl. Metrics are accuracy, ROUGE-L, F1, and BLEU/CIDEr/SPICE respectively. Per-task breakdowns are in the paper's Tables 1-5; the abstract reports only the aggregate range.

## Limitations

The authors state the method relies on the quality of the learned confidence function g, and that a single global threshold across all exits could be improved by layer-specific thresholds. A reader should also notice that a bandit adapting online needs a stream of samples to converge, so the guarantees are asymptotic rather than per-sample, and the reported 'minimal performance drop' is an aggregate ceiling of 2% rather than a per-task figure. Nothing in the evaluation involves generated reasoning traces: the notion of 'exit' here is depth in the network, not stopping a chain of thought.

## Why it matters here

- **overthinking**: Tangential. The paper matched on the keyword 'early exit', but its subject is layer-wise early exit in classifiers and encoder-decoder models — the sample leaves the network at an intermediate layer — not the length of a reasoning trace a language model generates. Nothing here is evaluated on reasoning tasks or measures thinking tokens; the backbones are BERT-large, T5-large and BLIP-2, and the tasks are classification, QA, summarization, translation and captioning. The one transferable idea is structural: a stopping threshold fitted once on a validation set is stale under shift and can be adapted online from an unsupervised reward that charges for both wrong-and-early and unnecessarily-late stopping. If the group ever wants a stop-thinking controller that is calibrated at deployment rather than at training, this is a precedent for the mechanism, but it is not evidence about reasoning length.

## Entities

- **Concepts**: Early exit, Adaptive inference, Confidence thresholding, Overconfidence on wrong predictions, Distribution shift at deployment, Multi-armed bandit, [Risk control](../../../../wiki/concepts/risk-control.md)
- **Methods**: UAT, Multi-Armed Bandit, Upper Confidence Bound (UCB), Early-Exit Deep Neural Networks, BERT-large, [T5-large](../../../../wiki/methods/t5-large.md), BLIP-2-ViT-FlanT5-xl
- **Datasets**: [SST-2](../../../../wiki/datasets/sst-2.md), MNLI, RTE, QNLI, QQP, SQuAD 2.0, SamSum, CNN/DailyMail, MultiNews, BigPatent, IWSLT

Tags: `early-exit`, `adaptive-inference`, `multi-armed-bandit`, `confidence-calibration`, `risk-control`, `distribution-shift`, `inference-efficiency`

## Abstract

Abstract Early-Exit Deep Neural Networks enable adaptive inference by allowing prediction at intermediary layers, significantly reducing computational costs and latency. Most of the early exit strategies greedily exit a sample at an intermediary layer if the confidence in class prediction exceeds a predefined threshold that is set using a static validation set. This is problematic as the model might be overconfident in a wrong class. Also, they are not robust to distribution shifts encountered in deployment, which can undermine model trustworthiness and accuracy. To address these challenges, we propose UAT that adapts the threshold for exit decisions using a Multi-Armed Bandit framework, enabling online, unsupervised adjustment of exit decisions. UAT makes decisions based on a new reward function that assesses predictive certainty and its reliability to balance computational efficiency and prediction quality while penalizing unnecessary late exits. We provide guarantees on risk achieved by UAT and validate its performance on diverse tasks spanning vision-language understanding, text generation, and classification. Our framework demonstrates consistent improvements in speedup $(1.70-2.10\times)$ with a minimal performance drop $(<2)$\% as compared to full model performance.

---

Record id: `title:c65d4659ec08b51c`
