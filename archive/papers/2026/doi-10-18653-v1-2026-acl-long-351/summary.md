<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# S2O: Early Stopping for Sparse Attention via Online Permutation

- **Authors**: Yu Zhang, Songwei Liu, Chenqian Yan, Linsheng, Beichen Ning, Fangmin Chen, Xing Wang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.351/>
- **PDF**: <https://aclanthology.org/2026.acl-long.351.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.351
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

S2O is a FlashAttention-compatible sparse-attention method for long-context prefill that reorders queries and keys/values via lightweight index arrays (no physical tensor permutation) to concentrate attention mass into a compact region, then applies an online early-stopping rule that skips low-contribution key/value blocks once marginal attention-mass gain falls below a threshold, achieving up to 7.51x attention speedup and 3.81x end-to-end prefill speedup on Llama-3.1-8B at 128K context with lower approximation error than prior sparse-attention baselines.

## Problem

Attention scales quadratically with sequence length, making long-context prefill the dominant inference bottleneck; block-sparse attention reduces this cost but coarse fixed-size blocks impose an intrinsic sparsity ceiling because attention heatmaps in LLMs actually exhibit thin, stripe-like structures rather than uniform block-level importance, so even accurate block selection wastes substantial computation on low-importance positions within selected blocks.

## Contributions

- identification of a practical sparsity ceiling in coarse block-sparse attention caused by a mismatch between fine-grained stripe-like attention structures and block-wise computation, motivating a global (not merely local) permutation approach
- a FlashAttention-compatible, index-guided online permutation scheme that reorders the effective computation order of queries and historical keys/values without physically permuting tensors in memory, achieving global permutation benefits at negligible index-remapping overhead
- a monotone-gain early-stopping rule that adaptively terminates key/value block processing once marginal attention-mass gain becomes negligible, avoiding the rigid fixed-subset commitment of Top-K/Top-CDF sparse-attention methods
- state-of-the-art sparsity-error trade-off and substantial measured speedups (7.51x attention, 3.81x end-to-end) on Llama-3.1-8B at 128K context, with accuracy preserved across multiple long-context benchmarks and model families

## Method

Observes that attention heatmaps are dominated by fine-grained vertical, horizontal and slash-like stripes rather than block-uniform patterns, and that a global (not merely local) permutation of queries and keys/values can concentrate this dispersed attention mass into a compact, top-left-weighted region. Rather than physically reordering tensors in memory (which is costly), S2O introduces an online, index-guided permutation: within each fixed-length segment, queries are cheaply ranked and permuted via a shared guide vector (front-loading queries likely to induce salient horizontal stripes), and historical keys/values are ranked per segment by their similarity to a mean-pooled segment query representative, producing a logical causal-prefix ordering. A FlashAttention-style kernel then gathers Q/K/V tiles according to these logical indices (physical HBM layout unchanged) and computes attention in two passes: Pass-1 initializes stable online-softmax states via a small dense intra-segment causal window; Pass-2 traverses the ranked historical key/value prefix in the permuted order, updating online-softmax accumulators, and applies a monotone-gain early-stopping rule that terminates processing once the marginal normalization-mass gain from newly processed blocks falls below a threshold tau relative to the accumulated mass -- unlike Top-K/Top-CDF methods that pre-commit to a fixed block subset, this adaptively determines how much of the prefix is worth computing per query.

## Results

On Llama-3.1-8B at 128K context, S2O reduces single-operator mean-squared error (MSE, versus full dense attention) by 3.82x at matched sparsity, and reduces prefill compute density by 3.31x at matched MSE, compared to the strongest baseline (PBS, a local permutation-based method); it also outperforms FlexPrefill and XAttn (pattern/probing-based block-selection methods) at all tested sparsity levels. End-to-end measurements show 7.51x attention-operator speedup and 3.81x end-to-end prefill speedup over dense FlashAttention2 at 128K context, with sparse-preprocessing overhead (index computation) accounting for only a small fraction of total time and remaining below 10% relative to attention speedup gains across context lengths from 32K to 128K. On long-context benchmarks (InfiniteBench, RULER, LongBench v2) across Llama-3.1-8B and Qwen3-8B, S2O attains accuracy comparable to full dense attention across most tasks (average 0.379/0.386 vs. full-attention's 0.383/0.386 on InfiniteBench) while reducing prefill compute density by 2-3x compared to the default configuration, and maintains accuracy across a wide range of context lengths on RULER while achieving higher sparsity than baselines. Ablations show the early-stop threshold tau is the dominant factor governing the speed-accuracy trade-off (segment length S has only minor effect on approximation error), and component ablation confirms query-side intra-segment permutation (Q_perm) meaningfully improves the speed-quality trade-off over both a local-window-only variant (large approximation error from omitting the historical-prefix ranking) and a no-Q-permutation variant (identity query order within segments), by front-loading queries likely to induce salient horizontal stripes and enabling earlier, more effective attention-mass accumulation and early stopping.

## Limitations

The method introduces additional hyperparameters (segment length, early-stop threshold, scheduling rules) that may require re-tuning across different models, context lengths and hardware platforms, and the best configuration is not guaranteed to transfer reliably. Evaluation focuses primarily on the prefill stage of decoder-only LLMs; extending the approach to other architectures (encoder-decoder, multimodal models) and to training-time usage requires further study. Experiments are conducted on a specific GPU and software stack (Triton implementation, BF16 on NVIDIA GPUs), so performance and memory behavior may vary across other accelerators and deployment environments.

## Why it matters here

- **overthinking**: Not relevant to reasoning length or the accuracy/efficiency tradeoff of LLM reasoning: 'early stopping' here refers to terminating sparse-attention key/value block processing during long-context prefill, an unrelated inference-efficiency mechanism at the attention-operator level rather than the reasoning-trace level. It matched the topic's collection keywords only via the shared term 'early stopping.'

## Entities

- **Concepts**: online (index-guided) permutation, monotone-gain early stopping for sparse attention, coordinate-scheduled sparse attention, stripe-like attention heatmap structure
- **Methods**: S2O (online permutation + monotone-gain early stopping), FlashAttention / FlashAttention2 (baseline, dense reference), FlexPrefill (baseline), XAttn (baseline), PBS (baseline)
- **Datasets**: InfiniteBench, RULER, [LongBench v2](../../../../wiki/datasets/longbench-v2.md)

Tags: `sparse-attention`, `long-context-inference`, `early-stopping`, `efficient-transformers`, `prefill-optimization`

## Abstract

Attention scales quadratically with sequence length, fundamentally limiting long-context inference.Existing block-granularity sparsification can reduce latency, but coarse blocks impose an intrinsic sparsity ceiling, making further improvements difficult even with carefully engineered designs.We present S2O, which performs early stopping for sparse attention via online permutation.Inspired by virtual-to-physical address mapping in memory systems, S2O revisits and factorizes FlashAttention execution, enabling inference to load non-contiguous tokens rather than a contiguous span in the original order.Motivated by fine-grained structures in attention heatmaps, we transform explicit permutation into an online, index-guided, discrete loading policy; with extremely lightweight preprocessing and index-remapping overhead, it concentrates importance on a small set of high-priority blocks.Building on this importance-guided online permutation for loading, S2O further introduces an early-stopping rule: computation proceeds from high to low importance; once the current block score falls below a threshold, S2O terminates early and skips the remaining low-contribution blocks, thereby increasing effective sparsity and reducing computation under a controlled error budget.As a result, S2O substantially raises the practical sparsity ceiling.On Llama-3.1-8B under a 128K context, S2O reduces single-operator MSE by 3.82× at matched sparsity, and reduces prefill compute density by 3.31× at matched MSE; meanwhile, it preserves end-to-end accuracy and achieves 7.51× attention and 3.81× end-to-end speedups.

---

Record id: `doi:10.18653/v1/2026.acl-long.351`
