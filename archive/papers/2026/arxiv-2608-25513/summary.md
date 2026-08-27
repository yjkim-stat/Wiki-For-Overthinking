<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Adaptive Regularization for Random Features: A Neighboring Early-Stopping Rule with Oracle-Rate Guarantees

- **Authors**: Caixing Wang, Zhibo Chen, Yue Wang
- **Venue**: stat.ML
- **Published**: 2026-08-26
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.25513>
- **PDF**: <https://arxiv.org/pdf/2608.25513v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Random feature methods provide a scalable approximation to kernel ridge regression (KRR), but the regularization parameter that yields the oracle learning rate depends on unknown smoothness and capacity parameters. In this work, we propose a neighboring early-stopping rule for adaptive regularization in KRR with random features (KRR-RF). The method uses a grid that is uniform in inverse regularization and compares only adjacent estimators, reducing the number of discrepancy comparisons relative to standard all-pairs Lepskii-type procedures. Both the neighboring discrepancy and its empirical complexity term can be computed directly in the random feature space, without constructing the exact kernel Gram matrix. We establish a high-probability comparison bound for neighboring KRR-RF estimators and show that, under standard source and capacity conditions together with suitable grid and random feature budget conditions, the selected estimator attains the oracle polynomial learning rate up to logarithmic factors. The result allows the regularization parameter to be selected without prior knowledge of the source and capacity exponents and covers both well-specified and partially misspecified regimes. Our analysis is based on an empirical random feature effective dimension that connects the observable stopping threshold with the population complexity of the random feature model. Simulation and real-data experiments illustrate the prediction performance and computational behavior of the proposed method in comparison with standard tuning procedures.

---

Record id: `arxiv:2608.25513`
