<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Less is More: Improving LLM Reasoning with Minimal Test-Time Intervention

- **Authors**: Zhen Yang, Mingyang Zhang, Feng Chen, Gonggui Ding, Liang Hou, Xin Tao, Ying-Cong Chen
- **Venue**: Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)
- **Published**: 2026-01-01
- **Source**: local
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

A training-free test-time method that detects high-entropy (uncertain) tokens during LLM decoding and applies classifier-free guidance, via a reused-KV-cache negative prompt, only at those tokens to correct reasoning errors with minimal overhead.

## Problem

LLM reasoning failures are not uniformly distributed across a generated response but are concentrated in a small number of high-entropy "critical" tokens where local uncertainty can propagate and destabilize the rest of the chain. Existing test-time-scaling methods (self-consistency, tree search, multiple reasoning trajectories) improve accuracy but trade away efficiency by adding substantial extra inference computation; it was open whether accuracy could be improved by intervening only at the few tokens that matter, without that broad computational cost.

## Contributions

- Show that reasoning failures in LLMs are concentrated in a small subset of high-entropy tokens rather than spread uniformly across a response.
- Introduce Selective CFG intervention, which applies classifier-free guidance only at tokens whose predictive entropy exceeds a threshold, instead of at every token.
- Introduce lightweight negative-prompt guidance that reuses the conditional branch's KV cache with a short injected negative prompt, avoiding the need to maintain a second unconditional KV cache.
- Demonstrate consistent accuracy gains across general, coding and STEM benchmarks and across model families (DeepSeek-R1, Qwen3, Ling-mini-2.0) with negligible inference overhead, and show the method also transfers to a vision-language model.

## Method

MTI intervenes on the logit distribution at individual decoding steps of the residual/output layer (not a fixed residual-stream layer): at each step it computes the Shannon entropy H_t of the model's softmax output over the vocabulary, and applies classifier-free guidance (CFG) only when H_t exceeds a threshold tau. The intervened logit is log P_hat(x_t|c,c_bar,x_<t) = (1-omega)*log P(x_t|c_bar,x_<t) + omega*log P(x_t|c,x_<t), with omega=1.5 by default. Rather than maintaining a separate unconditional KV cache (as in vanilla CFG), MTI reuses the conditional branch's KV cache and appends a short negative prompt (default: the two-word cue "OUTPUT ERROR") to construct the unconditional branch on the fly, adding only two auxiliary tokens per high-entropy position. It fires only at the minority of tokens whose entropy exceeds tau (as low as ~0.2% to as high as ~100% of tokens depending on tau, typically single-digit to ~30% in the reported sweeps), leaving all other tokens to decode normally. It is training-free and requires no backpropagation or calibration data beyond selecting tau and omega empirically; the paper reports that despite the extra CFG-style computation at flagged positions, total wall-clock latency is often lower than Direct Inference because MTI produces shorter, less erroneous reasoning chains (Table 3), and is far cheaper than vanilla CFG applied to every token (Table 6, App. E).

## Results

On DeepSeek-R1-7B, MTI reaches an average of 70.73% across six benchmarks (MMLU-Pro, GPQA-Diamond, MATH500, HumanEval, HumanEvalPlus, LiveCodeBench) versus 61.70% for Direct Inference (+9.28%), using CFG on 21.8% of tokens; on Qwen3-14B, MTI reaches 85.33% versus 82.33% DI (+3.00%) using CFG on 32.8% of tokens. On GPQA-Diamond with DeepSeek-R1-7B, greedy Direct Inference collapses into repetitive generation (29.29%); MTI corrects this to 51.52% (+22.23%). Under random sampling on AIME2024 (8 runs averaged), MTI improves DeepSeek-R1-7B from 54.17% to 62.92% (+8.75%) and Ling-mini-2.0 from 60.00% to 71.25% (+11.25%); vanilla CFG (VC) sometimes underperforms Direct Inference here (e.g. 73.34% vs 73.75% on Qwen3-8B). An ablation restricting CFG to only low-entropy tokens (<=1.5) degrades AIME2024 accuracy to 71.67%, versus 78.34% when restricted to high-entropy tokens (>1.5), confirming the entropy-localization hypothesis. Latency (Table 3): on Qwen3-14B/GPQA-Math500/etc., MTI (tau=1.0) takes 4551s versus 4547s for Direct Inference and 12411s for vanilla CFG; on Ling-mini-2.0, MTI (tau=0.1) takes 1495s versus 1288s DI and 3142s VC. Applied zero-shot to a vision-language model (Qwen3-8B-VL-Instruct) on spatial reasoning benchmarks, MTI improves Where2Place 61.39%→64.36% (+2.97), RefSpatial 42.45%→44.24% (+1.79) and VaBenchPoint 38.87%→40.86% (+1.99) while triggering CFG on only 3.7-4.5% of tokens. MTI also outperforms SOTA test-time-scaling baselines (TALE, NoThinking, Dynasor, DEER, CGRS) on Qwen3-8B and DeepSeek-R1-7B across AIME2024/MATH500/GPQA-Diamond (Table 5).

## Limitations

Stated: the paper finds that even meaningless negative prompts (e.g. "apple") or positive prompts improve over Direct Inference, though less than semantically explicit negative prompts like "OUTPUT ERROR", and states that the interpretability of this effect "remains unexplored" as a direction for future research. The failure-case analysis (App. A.9) shows that when the entropy threshold is set too high, the intervention skips critical high-entropy tokens and the model reproduces the original erroneous reasoning step. Unstated: the entropy threshold tau is swept per model/benchmark (optimal values range from 0.5 to 1.5 across models in Table 1), and although the paper reports a broad "green zone" where MTI beats both baselines, achieving the peak reported gains still required this per-model calibration; the authors themselves note that "cross-validation on a held-out dataset can be used" to select tau, which is a form of task-specific tuning despite the method being framed as needing no calibration data. Inference cost is reported explicitly (Table 3, wall-clock latency), so this is not a gap in this paper.

## Why it matters here

- **overthinking**: MTI is an inference-time control method that selectively applies classifier-free guidance only at high-entropy decoding steps to correct error-prone reasoning trajectories, and the paper reports this incidentally shortens output by avoiding erroneous or redundant reasoning chains (Table 3) — a training-free, low-overhead alternative to full test-time compute scaling that bears directly on the survey's question of where and when to intervene mid-generation.

## Entities

- **Concepts**: token entropy, classifier-free guidance, KV cache reuse, negative prompting, selective intervention
- **Methods**: Minimal Test-Time Intervention (MTI), Selective CFG intervention, Lightweight negative-prompt guidance, Classifier-Free Guidance (CFG), Contrastive Decoding (CD)
- **Datasets**: [MMLU-Pro](../../../../wiki/datasets/mmlu-pro.md), [HumanEval](../../../../wiki/datasets/humaneval.md), HumanEvalPlus, [LiveCodeBench](../../../../wiki/datasets/livecodebench.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), [MATH500](../../../../wiki/datasets/math500.md), [AIME2024](../../../../wiki/datasets/aime-2024.md), Where2Place, RefSpatial, VaBenchPoint

Tags: `test-time-intervention`, `classifier-free-guidance`, `token-entropy`, `kv-cache-reuse`, `negative-prompting`, `decoding`, `training-free`

## Abstract

Recent progress in large language models (LLMs) has focused on test-time scaling to improve reasoning via increased inference computation, but often at the cost of efficiency. We revisit test-time behavior and uncover a simple yet underexplored phenomenon: reasoning uncertainty is highly localized—only a small subset of high-entropy tokens dominantly affects output correctness. Motivated by this, we propose Minimal Test-Time Intervention (MTI), a training-free framework that enhances reasoning accuracy and stability with minimal overhead. MTI includes: (i) Selective CFG intervention, applying classifier-free guidance only at uncertain positions; and (ii) Lightweight negative-prompt guidance, reusing the main model's KV cache to approximate unconditional decoding efficiently. MTI yields consistent gains across general, coding, and STEM tasks—e.g., +9.28% average improvement on six benchmarks for DeepSeek-R1-7B and +11.25% on AIME2024 using Ling-mini-2.0—while remaining highly efficient. The code can be found here.

---

Record id: `local:0f0156fba32ad42d`
