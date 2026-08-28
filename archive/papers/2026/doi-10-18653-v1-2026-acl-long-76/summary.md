<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ZoomR: Memory Efficient Reasoning through Multi-Granularity Key Value Retrieval

- **Authors**: David H. Yang, Yuxuan Zhu, Mohammad Mohammadi Amiri, Keerthiram Murugesan, Tejaswini Pedapati, Subhajit Chaudhury, Pin-Yu Chen
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.76/>
- **PDF**: <https://aclanthology.org/2026.acl-long.76.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.76
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

ZoomR fine-tunes a reasoning model to summarize its own thoughts after each paragraph, then at inference dynamically retrieves only a small, consensus-selected subset of full-resolution reasoning segments (zooming in) while keeping the rest as compressed summary keys -- cutting KV-cache GPU memory more than 4x versus a full cache with accuracy close to the vanilla full-KV baseline, and finds that attention-head consensus on which segments matter is itself a diagnostic signal correlated with answer correctness.

## Problem

Long chain-of-thought reasoning generates tens of thousands of output tokens, and the key-value (KV) cache needed for autoregressive decoding grows linearly with output length, causing both quadratic-scaling compute cost per new token and prohibitive GPU memory use (e.g. >16GB for a 16K-token response at batch size 8); existing KV cache optimization mostly targets compressing a long *input* context during prefill, and existing dynamic token-selection methods for the *output* either discard critical intermediate reasoning steps (StreamingLLM's sliding window, H2O's token-level importance scoring) or restrict attention entirely to lossy summaries, creating an information bottleneck when a reasoning step actually needs fine-grained historical detail.

## Contributions

- ZoomR, a dynamic KV cache selection policy for long-output reasoning that combines coarse-grained compressed summaries with selective full-resolution 'zoom-in' on consensus-important segments, addressing the long-output-generation-specific memory bottleneck that prior KV cache methods (focused on long input/prefill) do not target
- a lightweight fine-tuning procedure that teaches a reasoning model to generate its own paragraph-level summaries during generation, requiring no architecture change
- an attention-head voting and consensus mechanism that identifies which historical reasoning segments genuinely need full-resolution access at each decoding step, achieving more than 4x memory savings versus a CPU-offloaded full KV cache with accuracy close to the vanilla full-KV baseline
- a novel finding that attention-head consensus/agreeability over which segments matter is itself diagnostic of reasoning correctness: correct answers show faster, more stable convergence to an agreed-upon important-segment set than incorrect ones

## Method

Fine-tunes a base reasoning model with LoRA (using a Bespoke-17K dataset augmented with Llama3-70B-generated paragraph-level summaries, delimited by explicit <|begin_of_summary|>/<|end_of_summary|> tokens) so the model learns to generate a concise summary after each reasoning paragraph during its own generation. At each decoding step, ZoomR represents each summary segment by a per-head, per-layer mean summary key (the average of that segment's token key vectors), computes an approximate per-head attention score between the current query and each mean summary key, and has each attention head 'vote' for its top-k most important summaries; votes are aggregated across all heads and layers into a consensus set of the c most-voted summaries, whose original full-text segments are restored to full resolution ('zoomed in') for the current attention computation, while the remaining candidate summaries stay compressed and everything else is dropped from the active context except an attention-sink prefix and a sliding window of the most recent tokens. The full KV cache is kept on CPU and only the selected subset (recomputed at semantic boundaries like end-of-sentence, not every token, to amortize cost) is transferred to GPU each step, with a pipelined layer-by-layer transfer to overlap data movement with computation.

## Results

Across GPQA Diamond, AIME2025, and MATH500 on both Llama-3.1-8B and Qwen2.5-7B (R1-Distill reasoning variants), ZoomR consistently outperforms StreamingLLM, H2O, and SumR (a summary-only variant with no full-detail retrieval) at matched GPU memory budgets: on Llama, ZoomR reaches 51.0% average accuracy (43.4/26.7/83.0 on the three benchmarks) versus StreamingLLM's 40.9%, H2O's 43.3%, and SumR's 43.9%, closing most of the gap to the vanilla full-KV-cache baseline's 54.8%; on Qwen, ZoomR reaches 51.3% versus baselines' 43.0-45.1%, versus vanilla's 57.2%. ZoomR shows an 8-percentage-point average accuracy improvement over SumR specifically, confirming that selecting only compressed summaries (no zoom-in) loses information that measurably hurts reasoning quality, and that retrieving full-resolution detail for consensus-important segments is what recovers it. ZoomR reduces GPU memory usage by more than 20x versus a full KV cache kept entirely on GPU, and more than 4x versus a full KV cache offloaded to CPU, at a 16K-token generation length and batch size 16; the theoretical memory-savings ratio grows sub-linearly favorable with sequence length (a worked example shows savings improving from 5.48x at 16K tokens to ~7.11x at 32K), since the number of consensus segments needed does not grow proportionally with output length. This memory efficiency trades off against throughput (tokens/sec drops versus full KV cache, e.g. Llama: 39.07 full-KV vs. 11.14 ZoomR), a cost attributed to CPU-GPU transfer latency limited by PCIe bandwidth. A novel diagnostic finding: an 'agreeability' metric (AG, the fraction of attention-head votes concentrated on the consensus set) is 5.7 percentage points higher for correct answers than incorrect ones during the first 38 recompute steps, and incorrect answers show substantially higher variability in AG over time (std 14.82% vs. 7.87% for correct answers) with a crossover at step 38 after which incorrect answers show higher (but less stable) agreeability -- suggesting correct reasoning converges quickly to a coherent, attention-head-agreed-upon solution path, while incorrect reasoning exhibits more exploratory, unstable attention patterns. Ablations on MATH500 (Llama) show consensus count c=1 (zooming into only one summary) drops accuracy 3% versus c=2, but c>=2 gives only ~1% further improvement while selected-KV count grows over 40%; similarly top-k=1 (each head voting for only one summary) drops accuracy ~3% versus k=2, but accuracy plateaus for k>=2 -- both hyperparameters have a clear minimum-viable setting beyond which returns diminish sharply relative to memory cost.

## Limitations

ZoomR's memory savings come at a throughput cost: decoding is measurably slower than a full on-GPU KV cache due to CPU-GPU data-transfer latency bound by PCIe bandwidth, making it a memory-for-speed tradeoff rather than a strict improvement on both axes. The approach requires an initial LoRA fine-tuning stage to teach the model to generate summaries in the expected format (though the paper notes sufficiently large models like Llama3-70B or GPT-4 may already do this if prompted, potentially avoiding fine-tuning). Summarization is inherently lossy compression, so segments not selected into the consensus set remain represented only by their compressed summary, and the paper's own motivating example (Figure 1) shows this can in principle miss fine-grained details a later reasoning step needs if the head-voting mechanism does not select the right segment as important.

## Why it matters here

- **overthinking**: Directly relevant to the cost side of overthinking: rather than shortening a reasoning trace, ZoomR accepts long traces as given and makes their memory cost sub-linear by keeping most of the trace compressed and retrieving full detail only where attention-head consensus says it is needed -- a complementary lever to length-penalty or early-stopping approaches elsewhere in this archive, applicable specifically to the long-output/decoding-time memory bottleneck rather than accuracy or token count. Its agreeability finding (correct reasoning converges to stable head-consensus faster than incorrect reasoning explores unstably) is also a candidate diagnostic signal for overthinking or unproductive exploration, distinct from confidence- or entropy-based signals used elsewhere.

## Entities

- **Concepts**: multi-granularity KV cache, reasoning summarization (thought compression), consensus-based segment retrieval, mean summary key, agreeability (attention-head consensus metric), attention sink
- **Methods**: ZoomR (multi-granularity dynamic KV selection), StreamingLLM (baseline), H2O (baseline), SumR (summary-only ablation baseline), [LoRA fine-tuning](../../../../wiki/methods/lora-fine-tuning.md)
- **Datasets**: Bespoke-17K (augmented with summaries, fine-tuning data), [GPQA Diamond](../../../../wiki/datasets/gpqa-diamond.md), [AIME2025](../../../../wiki/datasets/aime-2025.md), [MATH500](../../../../wiki/datasets/math500.md)

Tags: `KV-cache`, `memory-efficiency`, `long-output-generation`, `summarization`, `reasoning-efficiency`

## Abstract

Large language models (LLMs) have shown great performance on complex reasoning tasks but often require generating long intermediate thoughts before reaching a final answer. During generation, LLMs rely on a key-value (KV) cache for autoregressive decoding. However, the memory footprint of the KV cache grows with output length. Prior work on KV cache optimization mostly focus on compressing the long input context, while retaining the full KV cache for decoding. For tasks requiring long output generation, this leads to increased computational and memory costs. In this paper, we introduce ZoomR, a novel approach that enables LLMs to adaptively compress verbose reasoning thoughts into summaries and uses a dynamic KV cache selection policy that leverages these summaries while also strategically “zooming in” on fine-grained details. By using summary keys as a coarse-grained index during decoding, ZoomR uses the query to retrieve details for only the most important thoughts. This hierarchical strategy significantly reduces memory usage by avoiding full-cache attention at each step. Experiments across math and reasoning tasks show that our approach achieves competitive performance compared to baselines, while reducing inference memory requirements by more than 4 ×. These results demonstrate that a multi-granularity KV selection enables more memory efficient decoding, especially for long output generation.

---

Record id: `doi:10.18653/v1/2026.acl-long.76`
