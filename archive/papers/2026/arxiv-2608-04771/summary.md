<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning

- **Authors**: Qiyuan Zhu, Dezhi Li, Pengyu Cheng, Tianle Chen, Jiacheng Wang, Ruijie Shen, Hao Gu, Sida Lin, Zirui Liu, Jiacheng Liu, Sirui Han
- **Venue**: cs.AI
- **Published**: 2026-08-05
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.04771>
- **PDF**: <https://arxiv.org/pdf/2608.04771v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.67

## In one line

ReCo uses a 30M process-reward estimator to set, per reasoning step, both the KV-cache retention ratio and generation-side controls (a reflection-token logit penalty and confidence-based early stopping), cutting generated tokens by 37-65% and end-to-end latency by 2.08-2.35x versus full-cache CoT.

## Problem

Long chain-of-thought inflates inference cost, and KV-cache compression is the usual remedy, but reasoning-oriented compressors apply one uniform policy across the whole trajectory and score themselves only by what they evict. The paper argues two things are missed: reasoning steps differ in how much context loss they tolerate, and a smaller cache makes the model generate more tokens, cancelling part of the saving. On MATH-500 with R-KV at a 25% compression rate, average generation rose from 3268.7 to 4538.1 tokens (+38.8%) on DeepSeek-R1-Distill-Qwen-7B and from 4409.8 to 7891.7 (+79.0%) on Llama-8B; 79.8% of MATH-500 problems (399/500) produced longer output than full cache at that rate, and over 50% did across the whole 15-40% range.

## Contributions

- Argues that on reasoning models KV-cache compression cannot be judged by eviction alone, since compressing the cache lengthens the reasoning it was meant to make cheaper, and quantifies that inflation (up to +79.0% average tokens; 79.8% of MATH-500 problems longer at a 25% rate).
- Shows that a process reward tracks per-step compression tolerance: deleting the same token budget from high-reward steps beats deleting it from randomly chosen steps by 4.0/3.5 points (GSM8K/MATH-500, Llama-8B) and 6.5/5.9 points (Qwen-7B).
- Proposes ReCo, coupling reward-adaptive KV retention, a reward-banded reflection-token logit penalty and confidence-probe early stopping under a single per-step reward, with no training of the reasoning model.
- Reports 37%-65% fewer generated tokens, 2.08x-2.35x latency speedup and 37.7% lower peak memory over Full CoT across three models and six benchmarks, at the smallest accuracy drop among compared compressed methods.

## Method

The trajectory is split into steps at newline tokens. After each step c_i a compact 30M estimator (Pilot, distilled from Skywork-o1-Open-PRM-7B) assigns a scalar reward v_i in [0,1]. That one reward drives three components. (1) KV compression: whenever the cache has grown by S tokens, the whole accumulated cache is compressed to m_i = lambda_i * L, with lambda_i = lambda - delta * (v_i - v_mean)/(v_max - v_min), so a step scoring above the trajectory's own mean prunes harder and a below-average step retains more; within the allowance, tokens are kept by the attention they attract from the w most recent tokens, with the last w always retained. Reward decides how much survives, attention decides what. (2) Reflection control: reflection tokens ("Wait", "Hmm", "Alternatively" and tokenizer variants) get a logit penalty beta_i in three reward bands - 0 below tau_l, beta/2 in the middle, full beta above tau_h - so a confident step is pushed to conclude rather than reopen branches. It acts on logits only, adding no tokens and no extra forward pass. (3) Early stopping: after the reward stays in the top band for two consecutive steps, a closing prompt ("Okay, I think I have finished thinking.") elicits a tentative answer, and generation commits if that answer's perplexity satisfies PPL(a) <= tau_p, otherwise the probe is discarded and reasoning resumes. No training of the reasoning model is required.

## Results

Averaged over three runs on a single NVIDIA H20 GPU. Accuracy (six-benchmark average) vs Full CoT: 60.2% vs 62.8% on DeepSeek-R1-Distill-Llama-8B, 60.0% vs 61.9% on Qwen-7B, 69.6% vs 72.3% on Qwen3-8B - the smallest drop among compressed methods, where SnapKV falls to 37.5% and R-KV to 48.1% on Llama-8B. Average tokens fall 37% / 65% / 46% below Full CoT on the three models (Llama-8B 7078 -> 4491; Qwen-7B 5920 -> 2067; Qwen3-8B 6788 -> 3652), while cache-only baselines increase token count (SnapKV 7078 -> 11266 on Llama-8B). Latency speedup 2.08x / 2.35x / 2.18x, against 1.09-1.33x for cache-only baselines. Peak GPU memory on AIME25 (Llama-8B) 17.92 GB vs 28.78 GB full cache, 20.70 GB R-KV, 26.90 GB SAT. The accuracy advantage is largest on the hardest sets: AIME25 33.3% on Llama-8B where every KV baseline is <= 20%. It is not uniform: on Qwen-7B AIME24 SAT reaches 53.3% against ReCo's 40.0% and Full CoT's 43.3%, and on Llama-8B MATH-500 ReCo is 80.6% against Full CoT's 83.8%. Ablation (Llama-8B): each component alone is worse - KV compression alone spends 12.8k tokens on AIME25 against ReCo's 8.6k; reflection control and early stopping alone cut tokens but lose accuracy on hard sets. Setting delta = 0 (uniform, reward-agnostic retention) is among the weakest configurations (65.0% AMC). ReCo's own overhead is 0.60% (Pilot scoring), 0.11% (compression), 1.24% (reflection penalty) and 1.98% (early stopping) of end-to-end time. One configuration (lambda = 0.25, delta = 0.10, tau_p = 1.10) is used for all models and datasets.

## Limitations

The paper states no limitations section. Points a reader should notice: accuracy is not preserved but degraded by 1.9-2.7 points on the six-benchmark average against Full CoT, and by more on individual sets (AIME24 46.7% -> 43.3% on Llama-8B; MATH-500 83.8% -> 80.6%), so the speedup is bought with a real if small accuracy cost. Five of the six benchmarks are mathematics; the only non-math set, GPQA, shows no gain on Llama-8B (33.8% for both ReCo and Full CoT). Evaluation covers three 7-8B distilled or open models on one H20 GPU; nothing larger, and no non-reasoning or agentic workload, is tested. The method depends on an external process-reward estimator distilled from a math-focused PRM, so its behaviour on domains where process reward is poorly calibrated is untested. Length-only baselines (SAT, Dynasor) are 'tuned to a comparable level of acceleration', a comparison choice that fixes the operating point rather than tracing each method's accuracy-latency curve. The claimed relation between reward and compression tolerance rests on a single motivating experiment on two models and two datasets (GSM8K, MATH-500) using one deletion protocol.

## Why it matters here

- **overthinking**: Directly on topic, and it adds a mechanism the topic's usual framing misses: memory-side compression and reasoning length are coupled, not separable. The measured length inflation - R-KV at a 25% cache rate raising MATH-500 output from 3268.7 to 4538.1 tokens on Qwen-7B and 4409.8 to 7891.7 on Llama-8B, with 79.8% of problems longer - means an efficiency intervention can cause overthinking as a side effect, so any accounting of reasoning cost that stops at the cache is incomplete. It also supplies a concrete stop-at-the-right-point rule that separates two signals the archive should not conflate: process reward certifies the trajectory is sound, answer perplexity certifies the model is confident in the answer, and the paper stops only when both hold, arguing perplexity alone would license confident-but-wrong halts. The ablation that sets delta = 0 (uniform retention) and finds it among the weakest settings is evidence that per-step allocation, not just a smaller average budget, is what buys the accuracy.

## Entities

- **Concepts**: [Overthinking](../../../../wiki/concepts/overthinking.md), Compression tolerance of a reasoning state, Length inflation under cache compression, [Process reward model](../../../../wiki/concepts/process-reward-model.md), [KV-cache compression](../../../../wiki/concepts/kv-cache-compression.md), Reflection tokens, Confidence-based early stopping, Step-wise inference-time budget allocation
- **Methods**: ReCo (Reward-Coordinated Compression), Reward-adaptive KV-cache retention ratio, Attention-guided token selection within a reward-set budget, Reward-banded reflection-token logit penalty, Confidence-probe early stopping on answer perplexity, Pilot (30M process-reward estimator distilled from Skywork-o1-Open-PRM-7B), SnapKV, [R-KV](../../../../wiki/methods/r-kv.md), RPC, SAT, Dynasor
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH-500](../../../../wiki/datasets/math-500.md), AMC2023, AIME24, AIME25, [GPQA](../../../../wiki/datasets/gpqa.md), [DeepSeek-R1-Distill-Llama-8B](../../../../wiki/datasets/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-7B](../../../../wiki/datasets/deepseek-r1-distill-qwen-7b.md), [Qwen3-8B](../../../../wiki/datasets/qwen3-8b.md)

Tags: `overthinking`, `efficient-reasoning`, `kv-cache`, `early-stopping`, `process-reward`, `chain-of-thought`, `inference-latency`

## Abstract

Large Reasoning Models (LRMs) excel on complex tasks through long chain-of-thought (CoT) reasoning, but their lengthy intermediate steps cause severe overthinking that inflates inference cost. KV-cache compression is a common solution, yet existing reasoning-oriented methods apply a uniform policy across the trajectory and judge compression only by what it removes from the cache. Two observations point the other way. First, a reasoning state's tolerance to context loss varies along the trajectory, and process reward tracks it: deleting tokens at high-reward steps preserves accuracy far better than deleting the same budget at random. Second, compression is not free on the generation side, since a smaller cache leads the model to generate more tokens, partly canceling the saving. Together these motivate coordinating both sides under a single process reward. We propose ReCo (Reward-Coordinated Compression), a step-wise framework in which a lightweight process-reward estimator scores each completed step and drives three components: (1) reward-adaptive KV-cache compression that shrinks the retained cache harder at high-reward steps and less at low-reward ones, (2) a reward-banded penalty on reflection tokens that curbs redundant generation, and (3) confidence-based early stopping that triggers when the reasoning is reliable. Across three reasoning models and six benchmarks, ReCo reduces generated tokens by 37%-65% and end-to-end latency by 2.08x-2.35x over Full CoT, all while largely preserving accuracy.

---

Record id: `arxiv:2608.04771`
