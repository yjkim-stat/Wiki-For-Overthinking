<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Language Models Can Control Their Own Attention

- **Authors**: Namgyu Ho, Huzama Ahmad, Woosung Koh, Se-Young Yun, Tal Schuster, Cicero Nogueira dos Santos
- **Venue**: preprint
- **Published**: 2026-01-01
- **Source**: local

## In one line

Zero-shot prompting protocol that has a language model tag its own chain-of-thought with <global>/<focus>/<local> spans, which an inference engine parses like tool calls to skip most of the long-context KV-cache read during decoding.

## Problem

Global attention layers read the entire KV cache at every decode step even though attention weight concentrates on a small subset of tokens, and that read dominates decode latency in long-context serving; prior sparse-attention methods still need an extrinsic O(N)-per-step scan to guess which tokens matter, so the paper asks whether the model itself already knows which context it needs and can simply say so.

## Contributions

- Declarative Attention, a zero-shot protocol eliciting a model to declare its own attention scope (<global>/<focus>/<local>) as part of its chain-of-thought
- A vLLM integration that reads these declarations at decode time and rewrites the KV-cache block table so the attention kernel skips unneeded blocks with no kernel modification
- Evaluation across 15 long-context tasks and six models showing DA reduces attended tokens 52.0%/31.1% on the two largest evaluated models at 1.27pp/2.75pp accuracy cost, with the accuracy gap narrowing and absolute token savings growing as model size and context length increase

## Method

Declarative Attention (DA) restructures the model's chain-of-thought into three named modes emitted as tags: <global> (attends to all context segments, used to navigate and pick a region), <focus magic_chunks="K"> (attends only to the named ~2048-token context segment(s), plus a fixed scaffold of system instruction/question/instruction/prior response), and <local> (attends to none of the context segments, only the response generated so far). The long context is pre-split into addressable ~2048-token "magic chunk" segments delivered as a simulated tool-use transcript; the model decides which mode to use and which chunks to name entirely at inference time, purely through prompting -- no parameters are trained and no external scorer computes the signal. A DA state machine integrated into vLLM watches the model's own emitted tags at each decode step and rewrites the request's KV-cache block table (rounded to block boundaries, typically 16-32 tokens) so the attention kernel physically reads only the kept blocks; FlashAttention and the rest of the serving stack run unmodified. The mask applies only to global-attention layers -- the efficient layers of hybrid architectures (sliding-window attention on Gemma-4-31B, Gated DeltaNet recurrent state on Qwen-3.6-27B) have a fixed per-step cost DA does not touch. Cost: DA reduces average attended KV tokens per response by 52.0% (Gemma-4-31B: 13.43M->6.45M) and 31.1% (Qwen-3.6-27B: 22.54M->15.52M) versus vanilla full attention, at accuracy drops of 1.27pp and 2.75pp respectively; DA also runs about 15-35% more decode steps than vanilla because its multi-mode reasoning is longer, so the net benefit is a roofline-estimated decode wall-clock time of 0.71x (Gemma-4-31B) and 0.77x (Qwen-3.6-27B) of vanilla on a B200 accelerator, assuming 40% compute utilization and 70% memory-bandwidth utilization in a large-batch, memory-bound serving regime -- no measured (as opposed to roofline-estimated) wall-clock numbers are reported.

## Results

Across 15 long-context sources (RULER, LongBench v1/v2, LooGLE, ZeroSCROLLS) with an LLM-judge scorer, DA cuts total average attended tokens by 52.0% on Gemma-4-31B (13.43M->6.45M per response) and 31.1% on Qwen-3.6-27B (22.54M->15.52M), for accuracy drops of 1.27pp (87.01%->85.74%) and 2.75pp (85.31%->82.56%). A DA-no-mask ablation isolates that the attention mask, not the chunked prompt format, is the source of the savings and accounts for the bulk of the accuracy cost (DA-nm matches vanilla accuracy within 0.69pp on Qwen). The accuracy gap to vanilla narrows monotonically as backbone size grows within both model families (e.g. relative accuracy 29% at Gemma-4-E4B to 99% at Gemma-4-31B), tracked to the model's <focus>-tag parse success rate rising from 58% (E4B) to 99% (31B). Absolute token savings grow with context length, from about -1M tokens at short context to about -21M tokens at 64-256K context on Gemma-4-31B. Roofline analysis projects decode wall-clock reduction to 0.71x (Gemma-4-31B) and 0.77x (Qwen-3.6-27B) of vanilla.

## Limitations

All results use non-thinking mode: the paper states models failed to follow the DA protocol within thinking tags in preliminary experiments, so reasoning-length/thinking-budget behavior is explicitly out of scope for this evaluation. The efficiency benefit is capped by the model's non-global-attention layers, which DA cannot reduce -- on Gemma-4-31B the sliding-window-attention floor is 42% of DA's remaining decode time even though the global-attention read it targets falls by more than half. Reported wall-clock savings (0.71x/0.77x) are roofline-estimated ceilings at stated hardware-utilization assumptions (40% MFU, 70% MBU) in a large-batch, memory-bound deployment regime, not measured end-to-end latency; the paper explicitly excludes prefill and phase-disaggregated serving. Smallest models (Gemma-4-E4B) retain only 29% of vanilla accuracy under the protocol, with a 58% focus-tag parse success rate, so DA's benefit depends on a minimum backbone capability the smallest models studied do not meet. DA also runs about 15-35% more decode steps than vanilla because the elicited multi-mode reasoning is longer, partially offsetting the per-step KV-read savings before the mask is applied.

## Entities

- **Concepts**: intrinsic (self-declared) vs extrinsic (externally scored) sparse attention, system-2 sparse attention, KV-cache block-table masking, roofline wall-time cost model
- **Methods**: Declarative Attention (DA), DA-no-mask ablation (DA-nm), block-aligned KV-cache block-table masking in vLLM, magic-chunk context segmentation
- **Datasets**: RULER (niah single/multikey), LongBench v1 (qmsum), LongBench v2 (multidoc_qa, code_repo, singledoc_qa, dialogue_history), LooGLE (summarization, longdep_qa, shortdep_cloze), ZeroSCROLLS (quality, space_digest)

Tags: `sparse attention`, `kv cache`, `long context`, `self-control`, `inference-time efficiency`, `decode latency`

## Abstract

Language models spend most of their attention on a small fraction of context, yet they read the entire KV cache to find the few tokens that matter. If the user asks about a previous detail in a 1M-token conversation, global attention layers must scan the full context to generate each token of the reply. A prominent approach mitigates this cost by pre-selecting relevant tokens via lightweight proxy scores, but this extrinsic scoring still incurs O(N) per step. We take an intrinsic approach motivated by the simple question: wouldn't the model already know which parts of the context are relevant? To this end, we introduce Declarative Attention (DA), a protocol that elicits the model to declare where it needs to attend within its chain-of-thought, partitioning generation into three modes: <global> (full context), <focus> (a specific region), and <local> (recent output only). The inference engine parses these declarations like tool calls and skips most of the KV cache read. Under zero-shot evaluation across 15 long-context tasks with off-the-shelf models (Gemma-4-31B, Qwen-3.6-27B), DA on off-the-shelf models significantly reduces total attended tokens during decoding (52.0%, 31.1%) with modest accuracy drops (1.27pp, 2.75pp) that shrink with model scale. DA unlocks a new axis of sparse attention, with further potential under training-based methods that future work can explore.

---

Record id: `local:3e017f43dbbd5883`
