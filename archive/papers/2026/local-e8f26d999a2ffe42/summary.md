<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# DiffAdapt: Difficulty-Adaptive Reasoning for Token-Efficient LLM Inference

- **Authors**: Xiang Liu, Xuming Hu, Xiaowen Chu, Eunsol Choi
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: local
- **Topics**: overthinking

## In one line

Introduces DiffAdapt, a lightweight probe trained on a reasoning LLM's frozen hidden states that classifies each question as Easy/Normal/Hard and, before generation starts, selects a matching fixed prompt/temperature/max-token strategy, cutting token usage by up to 22.4% without retraining the LLM.

## Problem

Reasoning LLMs generate long chains of thought for every problem regardless of need, wasting compute on easy problems while sometimes still lacking adequate resources for hard ones; the paper first asks why this happens (by analyzing token-level uncertainty across difficulty) and then how to allocate reasoning strategy per-question without retraining the base model.

## Contributions

- Identifies a consistent U-shaped generation-entropy pattern across difficulty levels on three models: high entropy despite high accuracy on easy problems (a 22-25% entropy reduction from easy to medium difficulty), low entropy at medium difficulty, and high entropy with low accuracy on hard problems.
- Runs oracle experiments showing that choosing per-question among three fixed strategies (Easy/Normal/Hard) yields up to 50% token savings while improving accuracy by over 10% versus any single uniform strategy, and a 7.2% average accuracy gain over the best fixed baseline with token allocation ranging from 198 tokens (GSM8K) to 4,675 tokens (AIME25).
- Introduces DiffAdapt, a three-stage framework (proxy-model data generation with heuristic entropy/correctness labeling, MLP probe training on frozen last-layer hidden states, and inference-time strategy selection) that needs no LLM fine-tuning, only a small probe.
- Shows DiffAdapt reduces token usage by up to 22.4% while matching or improving accuracy across five models and eight benchmarks, outperforms the training-free DEER early-exit baseline (which can increase token usage by up to 53.3% relative to a fixed Normal strategy), is robust to per-model threshold transfer and reduced training data, and is orthogonal to Length-Control RL training (composable with Nemotron-1.5B and ThinkPrune-7B).

## Method

The paper first characterizes overthinking via generation entropy: for each token position t, entropy H_t = -sum_j p_t,j log p_t,j is averaged across a sampled response, and correctness rate is measured across 10 samples per problem on the DeepMath-103K dataset binned into 10 difficulty levels. This reveals a U-shaped entropy curve (high entropy despite high accuracy on easy problems, low entropy at medium difficulty, high entropy with low accuracy on hard problems), with a 22-25% entropy reduction from easy to medium difficulty. Based on this, DiffAdapt defines three fixed inference strategies (Easy/Normal/Hard), each a combination of a prompt template, a sampling temperature, and a maximum token budget as a fraction of a full budget (Easy: temperature 0.5, 0.4x max tokens, 'direct solving with verification' prompt; Normal: temperature 0.8, 1.0x max tokens, step-by-step prompt; Hard: temperature 0.4, 0.5x max tokens, 'fail fast' resource-aware prompt). The inference-time intervention is strategy selection, not activation editing: (1) a proxy model (typically the same LLM) samples responses to unlabeled questions and computes their generation entropy and correctness rate; these are converted into Easy/Normal/Hard labels via per-model entropy/correctness thresholds (alpha, beta, gamma); (2) a lightweight 2-layer MLP probe C_theta = {W1,W2,b1,b2} is trained (base LLM weights kept frozen) to predict this 3-way difficulty label from the hidden state h_L extracted from the model's last layer after prefilling the question (i.e. before any reasoning token is generated), via d = softmax(W2 * ReLU(W1 h_L + b1) + b2), trained by cross-entropy against the heuristic labels; (3) at inference, after prefilling a new question the probe reads h_L once, predicts a difficulty class, and the corresponding fixed prompt/temperature/max-token strategy is applied for the entire generation -- no further intervention occurs during decoding. The probe step does not touch the model's prefilling or decoding computation, so it composes with batching, KV cache and prefix cache. Cost is reported end-to-end: on Qwen3-4B with a vLLM backend (first 40 OlympiadBench problems, batch size 10, single A800 GPU, 32K max tokens), DiffAdapt completes in 10 minutes versus 64 minutes for the vLLM baseline and 57 minutes for the DEER early-exit baseline -- a 6x and 5x wall-clock speedup respectively -- with the probe itself being a small MLP forward pass added once per question at prefill time.

## Results

DiffAdapt achieves up to 22.4% token savings (Qwen3-4B) and around 10% (DeepSeek-R1-Qwen-7B: 9.7%, ThinkPrune-7B: 10.1%) relative to a fixed Normal strategy, while DEER increases token usage relative to Normal (-27.5% on Qwen3-4B, -53.3% on DeepSeek-R1-Qwen-7B, i.e. more tokens used). End-to-end latency on Qwen3-4B (vLLM backend, A800 GPU) drops from 64 minutes (baseline) and 57 minutes (+DEER) to 10 minutes (+DiffAdapt), a 6x and ~5.7x speedup. Ablations on Qwen3-4B show DiffAdapt averages 70.9% versus 71.2% with thresholds transferred wholesale from DeepSeek-R1 (negligible difference, confirming robustness), versus 67.7% with a linear probe head instead of the 2-layer MLP (~3.2-point drop), and 68.5% with only 30% of training data (minimal degradation). A blind pairwise LLM-as-judge study (Qwen3-30B-A3B judge, N=50 GSM8K queries) preferred DiffAdapt's reasoning over the Normal-strategy baseline in 76% of cases, with catastrophic early-truncation failures occurring in only 2% of cases.

## Limitations

The heuristic difficulty-labeling thresholds (alpha, beta, gamma) are set per model from the observed entropy-correctness distribution rather than derived analytically, and require an optional sanity check on a validation split. The proxy-model data generation stage still requires 10 sampling iterations per training problem to estimate entropy and correctness, adding an upfront one-time cost not counted in the reported per-query inference latency. Evaluation is restricted to mathematical/scientific reasoning benchmarks (GSM8K, MATH500, AIME, OlympiadBench, Minerva, GPQA, MMLU-Pro); the paper does not evaluate on non-reasoning or open-ended generation tasks. The three inference strategies (Easy/Normal/Hard) are fixed and hand-designed (prompt template, temperature, token-budget fraction) rather than learned jointly with the probe.

## Why it matters here

- **overthinking**: Directly characterizes overthinking as a U-shaped entropy anomaly on easy problems and proposes an inference-time, training-free-for-the-LLM intervention (a small probe reading the frozen model's hidden state to pick a reasoning strategy) that cuts token usage by up to 22.4% and end-to-end latency by up to 6x without hurting accuracy.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), U-shaped entropy pattern, difficulty-adaptive inference, [token-efficient reasoning](../../../../wiki/concepts/token-efficient-reasoning.md)
- **Methods**: DiffAdapt (difficulty probe + strategy selection), generation entropy analysis, DEER (early-exit baseline), heuristic difficulty labeling
- **Datasets**: [DeepMath-103K](../../../../wiki/datasets/deepmath-103k.md), [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH500](../../../../wiki/datasets/math500.md), [AIME 2024](../../../../wiki/datasets/aime-2024.md), [AIME 2025](../../../../wiki/datasets/aime-2025.md), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md), [Minerva](../../../../wiki/datasets/minerva.md), [GPQA](../../../../wiki/datasets/gpqa.md), [MMLU-Pro](../../../../wiki/datasets/mmlu-pro.md)

Tags: `difficulty-adaptive-inference`, `token-efficiency`, `overthinking`, `entropy-analysis`, `probe-based-routing`, `test-time-compute`, `early-exit-comparison`

## Abstract

Recent reasoning Large Language Models (LLMs) demonstrate remarkable problem-solving abilities but often generate long thinking traces whose utility is unclear. Our work aims to improve their efficiency, enabling them to reach high performance without overthinking. First, we analyze the entropy of token probabilities in reasoning traces. Across three models, we observe a consistent U-shaped entropy pattern: high entropy on easy problems despite high accuracy, low entropy on problems with medium difficulty, and high entropy on hard problems reflecting uncertainty. Specifically, we notice 22-25% entropy reduction from easy to medium difficulty regions, suggesting an overthinking phenomenon on easy instances. Building on these insights, we introduce DiffAdapt, a lightweight framework that selects Easy/Normal/Hard inference strategies per question based on their difficulty and reasoning trace entropy. Each inference strategy consists of a fixed prompt, temperature and maximum token length. In contrast to existing efficiency optimization methods, our approach does not fine-tune base LLM but a small probe that classifies LLM's final hidden state, allowing inexpensive adaptation. We comprehensively evaluate our method on five models and eight benchmarks. Our method achieves comparable or improved accuracy while reducing token usage by up to 22.4%, establishing a practical path toward compute-efficient reasoning.

---

Record id: `local:e8f26d999a2ffe42`
