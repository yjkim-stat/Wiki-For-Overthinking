<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# EvtGraph: Event-Adaptive Compression for Sparse Temporal Graph Learning in Multimodal Time Series

- **Authors**: Ziqian Wang, Tingxiong Xiao, Yuxiao Cheng, Jinli Suo
- **Venue**: cs.LG
- **Published**: 2026-08-05
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.04368>
- **PDF**: <https://arxiv.org/pdf/2608.04368v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

EvtGraph compresses multimodal time series into a small budgeted set of learned event tokens and runs a temporally constrained sparse graph network over them, reporting 0.9060 Macro AUROC on MIMIC-IV + CXR against 0.8405 for the best baseline.

## Problem

Multimodal temporal data (clinical vitals, images, text; sensor streams) are irregularly sampled and uneven in information density, while standard architectures discretize time uniformly and so spend equal capacity on redundant and informative intervals. Lifting such sequences into graphs makes this worse: node count grows linearly with sequence length per modality and dense connectivity is quadratic. Existing remedies keep a predefined temporal grid (multi-scale/pyramid models), reduce cost over a fixed tokenization (sparse attention, correlation graphs), or prune post hoc (ToMe, DynamicViT), so sparsity remains an efficiency heuristic rather than a property of the representation.

## Contributions

- Frames multimodal temporal representation learning as capacity allocation under an explicit node budget rather than as post-hoc pruning of a fixed tokenization.
- Proposes EvtGraph, combining event-adaptive compression (EAMC), a differentiable node budget controller (NBC) with straight-through top-B selection and residual reassignment of discarded tokens, and a temporally admissible top-kappa sparse graph (T2SG) with O(kappa*B) edges.
- Reports 0.9060 Macro AUROC on MIMIC-IV + CXR, the lowest cross-domain error on TimeMMD (MSE 1.054), and 0.9494 on UCI HAR, at 149K-286K parameters.
- Shows accuracy peaking at a small budget (B* = 8), over 94% of assignment weight on the top-3 timesteps per segment, and same-budget uniform/random selection underperforming the learned selection.

## Method

Multimodal inputs are aligned onto a shared temporal axis (dense signals resampled, sparse ones snapped to nearest timestamps, missing values masked rather than imputed) and encoded to features H, then passed through H -> Z -> Z' -> G, trained end to end. EAMC (event-adaptive compression) splits the sequence into S fixed contiguous blocks of length ceil(T/S) rather than learning boundaries, scores each timestep within a block, and forms one event token as a temperature-softmax weighted sum of the block's features; the temperature is annealed and a residual pooling term with weight gamma prevents degeneration. NBC (node budget controller) scores each token and keeps the top-B, using a differentiable relaxation with a temporal bias term and a straight-through estimator so the forward pass is hard selection; discarded tokens are folded into their nearest retained neighbour in time under LayerNorm. T2SG builds a directed graph over the retained tokens with edges only from earlier to later within a lag window epsilon, keeping each node's top-kappa neighbours, giving at most B nodes and O(kappa*B) edges; 2-3 shallow graph layers are used to avoid over-smoothing at small B.

## Results

MIMIC-IV + CXR, AUROC over 3 seeds: EvtGraph 0.9060 Macro with 286K parameters, against the strongest baseline LSTM at 0.8405 and GRU at 0.8392; per-outcome 0.9043 AKI, 0.9037 circulatory failure, 0.9147 death, 0.8961 sepsis. Graph-pooling baselines are near chance on this task (DiffPool 0.4919, MinCutPool 0.5807 Macro). TimeMMD with 149K parameters: in-domain MSE 0.203 / MAE 0.337 (best baseline GRU 0.217 / 0.368), cross-domain MSE 1.054 / MAE 0.812 (best baseline DynamicViT 1.285 / 0.902). UCI HAR accuracy 0.9494 against TCN 0.9430. Accuracy peaks at a small node budget B* = 8 and then saturates as cost rises (Figure 2b); edge count scales near-linearly with node count (Figure 4b). Over 94% of the assignment weight falls within the top-3 timesteps per segment. Ablation on MIMIC-IV + CXR (Macro): full 0.906, w/o NBC 0.898, w/o temporal constraint 0.895, w/o event adaptivity 0.879, w/o RevIN 0.835, w/o masking 0.867; controlled same-budget baselines Uniform Compression 0.894 and Random Selection 0.892, so adaptivity contributes about 1.2-1.4 Macro AUROC points over compressing the same amount uniformly or at random. The efficiency claims (latency, memory, Pareto frontier) are presented only as figures; no latency, FLOP or memory table appears. Training was on a single NVIDIA A100 40GB, 30 epochs, Muon optimizer, with node budget B = 8 and edge budget kappa = 2.

## Limitations

Stated: the fixed coarse temporal partition may not capture events with highly variable or long-range structure; gains may diminish on near-stationary signals; performance depends on the node budget B, which requires task-specific tuning. A reader should add: the headline efficiency claim is never quantified in the text or a table - latency, memory and the Pareto frontier appear only inside figures, so 'significantly improving efficiency' cannot be checked against a number. The MIMIC-IV + CXR gap over baselines is large (about 6.5 Macro AUROC points over LSTM) while the same-budget controlled ablations move Macro by only ~1.2 points, which suggests much of the gain comes from the architecture as a whole rather than from the event-adaptive selection the paper argues for. The ablation is not uniformly favourable: removing NBC improves the death outcome (0.919 vs 0.915). All results are over 3 seeds with no significance testing, and the two blocks of baselines differ in parameter count by more than an order of magnitude (25K to 18.9M) without a matched-capacity control.

## Why it matters here

- **overthinking**: Tangential. It matched on the phrase 'adaptive compression', but this is a temporal graph neural network for multimodal time series - clinical vitals, chest X-rays, sensor streams - and involves no language model, no chain of thought and no reasoning length. The 'budget' here is a count of retained event tokens in an encoder (B* = 8 nodes), fixed before inference and tuned per task, not test-time compute spent deliberating on a problem. The only structural echo of the topic is the shared shape of the argument - allocate a fixed budget where information density is high rather than uniformly, and check it against same-budget uniform and random controls - which is the same experimental discipline the reasoning-length literature uses when it ablates a uniform policy. That is an analogy, not a contribution to the accuracy/efficiency tradeoff of reasoning length, and nothing here transfers as evidence about when a model should stop thinking.

## Entities

- **Concepts**: Budget-constrained representation learning, Event-centric temporal tokenization, Information density versus uniform computation allocation, Temporally admissible sparse graph, Adaptive computation / token pruning, Information bottleneck
- **Methods**: EvtGraph, EAMC (event-adaptive compression), NBC (node budget controller), T2SG (temporally constrained sparse graph), Straight-through estimator for top-B selection, RevIN, Neural CDE, Latent ODE, mTAN, ToMe, DynamicViT, DiffPool, MinCutPool, TimesNet, iTransformer, PatchTST
- **Datasets**: MIMIC-IV + CXR, Time-MMD (TimeMMD), UCI HAR

Tags: `temporal-graph`, `multimodal-time-series`, `adaptive-compression`, `clinical-prediction`, `token-budget`, `graph-neural-network`

## Abstract

Multimodal temporal data are inherently irregular and uneven in information density, yet most models rely on uniform discretization, leading to inefficient representations. We propose \textbf{EvtGraph}, a unified framework that aligns computation with temporal salience under explicit budget constraints. EvtGraph reparameterizes sequences into event-level tokens via event-adaptive compression (EAMC), selects a compact subset with a node budget (NBC), and performs temporally constrained sparse graph reasoning (T2SG). This transforms dense sequences into structured computation over salient events, reducing complexity while preserving critical transitions. We show that this design provides a practical mechanism for allocating representational capacity under a fixed budget, yielding a consistent performance--efficiency trade-off, where a small budget is often sufficient in practice. Experiments on multimodal clinical (MIMIC-IV + CXR) and cross-domain benchmarks demonstrate that EvtGraph outperforms both Transformer-based and recurrent baselines while significantly improving efficiency. These results suggest that budget-constrained event-centric representation provides a general paradigm for learning from high-redundancy temporal data.

---

Record id: `arxiv:2608.04368`
