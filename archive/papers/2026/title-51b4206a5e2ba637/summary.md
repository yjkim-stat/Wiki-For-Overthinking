<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Certain Head, Uncertain Tail: Expert-Sample for Test-Time Scaling in Fine-Grained MoE

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/62643>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Expert-Sample scales test-time compute for fine-grained MoE LLMs by randomizing only low-confidence expert routing choices, keeping high-confidence expert selections fixed, to get diverse samples without the usual diversity-stability tradeoff of temperature sampling.

## Problem

Token-level temperature sampling used to generate diverse candidates for test-time scaling (e.g. pass@k, Best-of-N) trades off diversity against stability; the paper asks whether MoE routing structure offers a better axis for controlling diversity at inference time.

## Contributions

- Observes that in fine-grained MoE routers, expert scores split into a high-confidence 'head' and an uncertain 'tail'.
- Proposes Expert-Sample, a training-free test-time scaling method that keeps head expert selections greedy while injecting controlled randomness only into tail expert routing.
- Shows this avoids the diversity-stability tradeoff that token-level temperature sampling incurs, while keeping normal-temperature decoding.
- Reports gains in pass@32 and Best-of-N verified accuracy on Qwen3-30B-A3B-Instruct.

## Method

In fine-grained Mixture-of-Experts models, router scores over experts show a confident head and an uncertain tail. Expert-Sample exploits this at inference time: it leaves the routing of high-confidence ('head') experts unchanged (greedy), and introduces controlled randomness only in the selection among low-confidence ('tail') experts. This produces diverse generations for test-time scaling (e.g. multiple sampled solutions for pass@k or Best-of-N) without perturbing token-level sampling temperature, which the paper argues avoids the usual tradeoff between output diversity and stability.

## Results

On Qwen3-30B-A3B-Instruct with GPQA-Diamond, pass@32 improved from 85.4% to 91.9%, and Best-of-N verified accuracy improved from 59.1% to 62.6%.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Directly relevant: it is a test-time compute scaling method for reasoning-capable MoE LLMs, improving the accuracy/efficiency return of sampling more candidates at inference (pass@k, Best-of-N verification) by changing where randomness is injected, rather than lengthening or shortening a single reasoning chain.

## Entities

- **Concepts**: test-time scaling via sampling diversity, MoE router confidence structure, diversity-stability tradeoff
- **Methods**: Expert-Sample, Best-of-N verification, pass@k sampling
- **Datasets**: [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md)

Tags: `test-time-scaling`, `mixture-of-experts`, `sampling`, `best-of-n`

---

Record id: `title:51b4206a5e2ba637`
