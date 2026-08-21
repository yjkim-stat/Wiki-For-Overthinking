<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# BEEM: Boosting Performance of Early Exit DNNs using Multi-Exit Classifiers as Experts

- **Authors**: _unknown_
- **Venue**: ICLR 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2025/poster/30371>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

BEEM is an exit criterion for early-exit DNNs that accumulates confidence across intermediate classifiers, adding a classifier's score only when it agrees with its neighbour, and exits when the running total passes a threshold set from intermediate-exit error rates.

## Problem

Early-exit networks attach classifiers to intermediate layers so that easy inputs can leave the network before the final layer. How much latency this saves, and how much accuracy it costs, is decided almost entirely by the exit rule. The common rule reads a single intermediate classifier's confidence, which is noisy: an early classifier can be confidently wrong, so the rule either exits too soon and loses accuracy or sets a conservative threshold and loses the speedup.

## Contributions

- An exit criterion that aggregates confidence across multiple exit classifiers instead of reading a single one, gated on agreement between neighbouring exits.
- A rule for setting the exit threshold from the measured error rates of the intermediate exits, targeting the accuracy of full-network inference rather than a chosen speed budget.
- Reported 1.5x-2.1x speedup over prior early-exit methods on GLUE tasks and COCO captioning, across ALBERT, BERT, and Swin/GPT-2 backbones.
- Public source code.

## Method

Each exit classifier is treated as an expert. As a sample passes through the network, BEEM maintains an aggregated confidence score. A classifier's confidence is added to the running total only if its predicted class agrees with the preceding exit's prediction; disagreement between neighbouring experts resets or withholds the contribution, so the score accumulates only along a run of consistent predictions. This is what captures the ensemble effect over exits rather than trusting one layer in isolation. The sample exits at the first point where the aggregated score exceeds a threshold. The threshold is not a free hyperparameter tuned for speed: it is derived from the measured error rates of the intermediate exits, chosen with the aim of matching or beating the accuracy of running the full network. A variant, BEEM-A, weights each expert's contribution by its accuracy.

## Results

Reported speedups of 1.5x to 2.1x over the compared early-exit methods (baselines include DeeBERT, ElasticBERT, FastBERT, PABEE, LeeBERT, ZTW, PCEE-BERT, PALBERT, JEI-DNN, DeeCap, MuE), with backbones ALBERT, BERT, and Swin Transformer plus a GPT-2 decoder for captioning. On GLUE dev sets the accuracy-weighted variant BEEM-A reports gains over the full network of roughly +0.4% on SST-2 and +0.7% on RTE at 1.89x-2.09x speedup. On COCO image captioning BEEM-A reports 82.4 BLEU-1 against 82.5 for the full-network baseline at 1.67x speedup. The pattern in the paper's own numbers is that the claim of beating the final layer holds on the easier language classification tasks, while on the harder captioning task the method is at best level with full inference and slightly below it on BLEU-1 — the speedup there is bought with a small accuracy loss, not for free.

## Limitations

The paper states that although it beats the final layer on the NLP tasks, performance 'takes a hit' on difficult tasks such as image captioning, and attributes this to the exit threshold being optimised on validation data in a way that may not transfer to test data. Beyond what is stated: the threshold is calibrated per dataset from intermediate error rates, so it requires a labelled validation split and re-calibration for each new task and backbone. The consistency rule depends on the exits being ordered and comparable, so it does not obviously carry to architectures where intermediate heads disagree in vocabulary or granularity. All evaluation is on classification and captioning with backbones of a few hundred million parameters; there is no experiment on generative reasoning, chain-of-thought, or any large reasoning model.

## Why it matters here

- **overthinking**: This is a keyword false positive for the topic as defined. The match was on 'early exit', but here that term has its ordinary computer-vision and encoder-NLP meaning — leaving a fixed feed-forward network at an intermediate layer during a single classification or captioning forward pass. There is no large reasoning model, no chain of thought, no test-time compute scaling, and no notion of reasoning length anywhere in the paper; the unit of saved compute is transformer layers, not thinking tokens, and the decision is made once per input rather than continuously during a generated trace. The only connection is a structural analogy: BEEM is a halting rule that spends more compute on inputs that look hard and stops on ones that look easy, which is the same shape as the question of when a reasoning model should stop. Its specific idea — that a single intermediate confidence reading is unreliable and that agreement across several successive checkpoints is a better stop signal — is the sort of thing a confidence-based early-answer method for reasoning traces could borrow. That is a transferable design pattern, not evidence about overthinking, and nothing in the paper's experiments speaks to the accuracy/length tradeoff in reasoning models. File as background on adaptive-compute halting criteria; it should not be cited as a result about reasoning length.

## Entities

- **Concepts**: early exit / adaptive-depth inference, exit classifiers as an ensemble of experts, confidence-based halting criterion, input-adaptive compute allocation, accuracy versus inference-latency tradeoff
- **Methods**: BEEM, BEEM-A, early exit DNN, confidence aggregation over exits, neighbouring-expert consistency check, error-rate-derived exit threshold
- **Datasets**: GLUE (SST-2, MNLI, RTE, QNLI, QQP, MRPC, CoLA), COCO (image captioning)

Tags: `early-exit`, `adaptive-inference`, `inference-latency`, `confidence-threshold`, `ensemble`, `glue`, `image-captioning`, `not-llm-reasoning`

---

Record id: `title:033e4d34acb0410b`
