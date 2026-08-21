<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# DiffAdapt: Difficulty-Adaptive Reasoning for Token-Efficient LLM Inference

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10011403>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

DiffAdapt trains a small probe on a reasoning model's hidden state to classify each question as Easy/Normal/Hard and picks a matching prompt, temperature and token limit, cutting token use without retraining the model.

## Problem

Reasoning LLMs generate long thinking traces whose utility is unclear, spending the same or more compute on easy questions as on hard ones. Existing efficiency methods fine-tune the base model, which is expensive and fixes one length policy for all inputs; the open question is how to allocate inference compute per question cheaply and without touching the model's weights.

## Contributions

- Documents a consistent U-shaped entropy pattern over problem difficulty across three reasoning models, with a 22-25% entropy reduction from the easy to the medium region, and reads the easy-side high entropy as overthinking.
- Introduces DiffAdapt, a probe over the LLM's final hidden state that selects among three fixed inference strategies (prompt, temperature, max tokens) per question, with no fine-tuning of the base model.
- Reports up to 22.4% token reduction at comparable or improved accuracy across five models and eight benchmarks, and an oracle upper bound of about 50% token savings with over 10 points of accuracy gain.

## Method

First an analysis: the entropy of token probabilities in reasoning traces follows a U-shape across difficulty — high on easy problems despite high accuracy, low at medium difficulty, high again on hard problems where it reflects genuine uncertainty. The 22-25% entropy drop from the easy to the medium region is read as overthinking on easy instances. DiffAdapt builds on this by defining three inference strategies (Easy/Normal/Hard), each a fixed triple of prompt, sampling temperature and maximum token length. A small probe classifies the LLM's final hidden state of the question prefill to predict difficulty, and the matching strategy is applied. The base LLM is never fine-tuned, only the probe is trained, so the method is deployment-ready and compatible with batching and KV/prefix caching.

## Results

Evaluated on five models — Qwen3-4B, DeepSeek-R1-Qwen-7B, DeepSeek-R1-Llama-8B, and two length-control-RL models, Nemotron-1.5B and ThinkPrune-7B — over eight benchmarks: GSM8K, MATH500, AIME 2024, AIME 2025, OlympiadBench, Minerva, GPQA and MMLU-Pro. Token reduction against the Normal fixed strategy is up to 22.4% (Qwen3-4B), with 9.7% on DeepSeek-R1-Qwen-7B and 10.1% on ThinkPrune-7B, at comparable or improved accuracy. Measured token allocation tracks difficulty, from 198 tokens on GSM8K to 4,675 on AIME25. An oracle that picks the best strategy per question reaches roughly 50% token savings with over 10 points of accuracy gain. End-to-end inference time is reported as 6x faster than a vLLM baseline and 5x faster than DEER.

## Limitations

The paper notes that on length-control-RL models DiffAdapt is slightly worse than the Easy strategy under low token limits, and only reaches its best results under high token budgets. It acknowledges that aggressive budget reduction hurts accuracy on hard or error-prone cases and recommends falling back to the Normal strategy when probe confidence is low; that thresholds derived from proxy-model sampling may need re-calibration when moving across domains; and that the question-prefill hidden state may not fully capture difficulty. The reader should also note the gap between the realised 9.7-22.4% savings and the oracle's ~50% with +10 accuracy: most of the available headroom is lost to probe error, so the result measures the difficulty probe more than the strategy design. The headline 22.4% is the best of five models, not the typical one.

## Why it matters here

- **overthinking**: Squarely on topic and one of the more directly usable results for the group. It names overthinking explicitly and supplies an operational signal for it: token-probability entropy is U-shaped in difficulty, high on easy problems the model already answers correctly, so entropy on the easy side measures wasted compute rather than uncertainty. It also settles a practical point — per-question compute allocation can be obtained from a probe over the frozen model's prefill hidden state, needing no length-control RL and composing with it. The oracle gap (about 50% savings and +10 accuracy available, 9.7-22.4% realised) is the number worth carrying: it says the ceiling on adaptive length control is far above current difficulty prediction, and localises the bottleneck in difficulty estimation rather than in the stopping mechanism.

## Entities

- **Concepts**: Overthinking on easy instances, Difficulty-adaptive test-time compute, Token-probability entropy as a difficulty signal, U-shaped entropy over difficulty, [Hidden-state probing](../../../../wiki/concepts/hidden-state-probing.md), Inference strategy selection, Oracle upper bound on adaptive routing
- **Methods**: DiffAdapt, hidden-state difficulty probe, Easy/Normal/Hard inference strategies, token-entropy analysis, [DEER](../../../../wiki/methods/deer.md), [ThinkPrune](../../../../wiki/methods/thinkprune.md), [vLLM](../../../../wiki/methods/vllm.md)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH500](../../../../wiki/datasets/math500.md), [AIME 2024](../../../../wiki/datasets/aime-2024.md), [AIME 2025](../../../../wiki/datasets/aime-2025.md), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md), [Minerva](../../../../wiki/datasets/minerva.md), [GPQA](../../../../wiki/datasets/gpqa.md), [MMLU-Pro](../../../../wiki/datasets/mmlu-pro.md)

Tags: `overthinking`, `adaptive-compute`, `difficulty-prediction`, `token-efficiency`, `entropy`, `test-time-compute`, `iclr-2026`

---

Record id: `title:18b94d8204ec3367`
