<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Compute-Optimal Quantization-Aware Training

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10009552>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

An empirical scaling study of how to split a fixed pretraining compute budget between a full-precision phase and a quantization-aware training phase, yielding a loss scaling law that predicts the optimal QAT fraction.

## Problem

Quantization-aware training is usually run as a second phase after full-precision pretraining, and that split is known to beat QAT alone, but how much of the total training compute should go to the QAT phase was unclear. Getting it wrong wastes budget or leaves accuracy on the table, and the answer was not known to vary systematically with compute, model size or bit width.

## Contributions

- Shows that the loss-optimal ratio of QAT to full-precision training increases with total compute, contradicting previous findings.
- Shows the optimal QAT fraction is predictable across model sizes (86.0M-2.2B) and quantization widths from the tokens-per-parameter-byte statistic.
- Derives a loss scaling law predicting optimal QAT ratios and final performance across QAT/FP allocations and bit widths, and uses it to predict the optimal bit width under a memory constraint.
- Proposes fusing learning-rate cooldown with QAT, removing redundant full-precision updates for compute savings.

## Method

Sweep training runs over compute budgets, QAT bit widths and model sizes from 86.0M to 2.2B parameters, varying the fraction of total compute spent in the QAT phase versus the full-precision phase, and fit the resulting losses. The paper finds the loss-optimal QAT-to-FP ratio increases with total compute — the opposite of what previous work found — and that the optimal fraction is predictable across model sizes and bit widths from the tokens-per-parameter-byte statistic. From the sweep it derives a loss scaling law predicting both the optimal QAT ratio and the final loss for a given allocation and bit width, then uses that law to predict which bit width is optimal under a given memory constraint and how quantized accuracy compares to full precision, verifying both experimentally. Separately it proposes fusing the learning-rate cooldown with QAT so the decay happens jointly with quantization-aware training, removing full-precision updates that would otherwise be discarded.

## Results

Model sizes 86.0M to 2.2B parameters. The paper reports that the loss-optimal QAT/FP ratio rises with total compute, that the optimal fraction is predicted across model sizes and bit widths by tokens-per-parameter-byte, and that scaling-law predictions about optimal bit width under a memory constraint and about QAT-versus-full-precision accuracy were confirmed experimentally. The cooldown-and-QAT fusion is described as achieving compute savings; the abstract gives no percentage, and no per-benchmark numbers were available in the material consulted (conference abstract and arXiv abstract only; the full paper's tables were not read).

## Limitations

No limitations were available in the material consulted. The reader should note the scope: this is a pretraining-compute allocation study for weight quantization, with loss as the objective, so the scaling law is fitted within one training setup and its transfer to other architectures, data mixes or post-training regimes is not established here, and the largest model is 2.2B parameters. Results and numbers here come from the abstract rather than the experiments section, so the specific accuracy figures behind each claim are not recorded.

## Why it matters here

- **overthinking**: Not relevant — this is a keyword false positive. The topic matched on 'compute-optimal', but here that phrase means the loss-optimal split of a fixed *pretraining* compute budget between full-precision and quantization-aware phases. The paper is about weight quantization and training-time FLOP allocation; it says nothing about reasoning traces, chain-of-thought length, test-time compute scaling, or when a model should stop generating. The only shared idea is the generic one of spending a budget where it buys the most loss reduction, which is not the accuracy/efficiency tradeoff of reasoning length that this topic tracks. Recommend it be treated as out of scope for the overthinking topic.

## Entities

- **Concepts**: [Compute-optimal allocation](../../../../wiki/concepts/compute-optimal-allocation.md), Scaling law fitting, Quantization-aware training, Tokens per parameter byte, Learning-rate cooldown
- **Methods**: Quantization-aware training (QAT), loss scaling law fitting, tokens-per-parameter-byte statistic, cooldown and QAT fusion
- **Datasets**: _none recorded_

Tags: `quantization`, `qat`, `scaling-laws`, `pretraining-compute`, `off-topic`, `iclr-2026`

---

Record id: `title:19ebd4d7f589cbd8`
