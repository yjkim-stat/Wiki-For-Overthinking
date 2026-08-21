<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# HiDrop: Hierarchical Vision Token Reduction in MLLMs via Late Injection, Concave Pyramid Pruning, and Early Exit

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10011723>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

HiDrop prunes about 90% of the vision tokens in a multimodal LLM by injecting them only at the layer where visual-text fusion actually begins and then dropping them on a concave schedule with a per-layer early exit, matching baseline accuracy while training 1.72x faster.

## Problem

Vision tokens dominate the quadratic attention cost of multimodal LLMs. Progressive pruning already exists, but the paper argues existing methods misread what the shallow layers do - treating them as if they fused vision and text when they are in fact passive - and apply rigid, fixed pruning schedules across depth, leaving efficiency on the table. Dynamic pruning also carries implementation overheads (positional encoding, incompatibility with FlashAttention) that erase the theoretical savings.

## Contributions

- Late Injection: skipping shallow layers for visual tokens, on the finding that those layers do not perform cross-modal fusion
- Concave Pyramid Pruning with a per-layer Early Exit, replacing fixed pruning schedules with a learned concave retention curve
- A differentiable top-k operator and inter-layer similarity measure to optimize the schedule end to end
- Systems work - persistent positional encoding, FlashAttention-compatible selection, parallel decoupling of vision computation - to remove the hidden overhead of dynamic token reduction
- 91.7% vision-token compression at 96.5% of original average performance, with 1.72x faster training and 88.9% lower inference FLOPs

## Method

Late Injection: visual tokens skip the shallow layers entirely and are introduced at the depth where active cross-modal fusion starts, identified by an inter-layer similarity measure. Concave Pyramid Pruning: rather than a fixed per-layer drop rate, the retention curve across middle and deep layers is concave, and an Early Exit mechanism lets a layer stop carrying vision tokens once they stop contributing. Token selection uses a differentiable top-k operator so the schedule is learned rather than hand-set. Three engineering pieces keep the savings real: persistent positional encoding so dropped tokens do not shift positions, FlashAttention-compatible token selection, and parallel decoupling of the vision computation.

## Results

On LLaVA-1.5 across 11 benchmarks (MME-Perception, MMBench, MMBench-CN, GQA, VQAv2, ScienceQA-Image, VizWiz, TextVQA, POPE, SEED-Image, MMStar) with MobileLLaMA-2.7B, Vicuna-7B-v1.5 and Vicuna-13B-v1.5 backbones: HiDrop retains 96.5% of original average performance at 91.7% token compression, against PDrop 94.2% at 46.9% compression, TwigVLM 95.3% at 88.9%, and VoCo-LLaMA 90.4% at 88.9%. Training for LLaVA-1.5-7B drops from 159.3 to 94.4 GPU hours (1.72x). Inference FLOPs fall 88.9% (3.82T to 0.42T) and prefill latency 48.8% (63.6 to 32.6 ms).

## Limitations

The paper states no limitations section. Readers should note that the reported 96.5% is 3.5% below original performance, not a match, and that the comparison to PDrop conflates two axes - PDrop is run at half the compression rate, so the accuracy comparison is not like-for-like. The method is specific to LLaVA-style architectures where vision tokens are a separable prefix, and the injection depth and pruning schedule are tied to the backbone's fusion behaviour. Gains are on prefill; decode-time savings are not separately reported.

## Why it matters here

- **overthinking**: Not relevant - this is a false positive on the keyword 'early exit'. The tokens HiDrop discards are image patch embeddings in the model's input, not steps of a chain of thought, and its Early Exit terminates the propagation of visual tokens through layers, not the generation of a reasoning trace. Nothing in the paper concerns reasoning length, test-time compute scaling, or when a model should stop thinking: the model evaluated is LLaVA-1.5 on visual question answering, which produces short answers rather than extended reasoning, and every number reported is a prefill-side cost (FLOPs, GPU hours, prefill latency) rather than a decoding-length one. The only shared vocabulary with this topic is the word 'early exit' and the general shape of spending less compute where it does not help. Recommend the archive record it as out of scope; if the group wants a note from it, the transferable idea is that the layer at which information stops contributing can be measured rather than assumed, which is a depth analogue of the length question but not evidence about it.

## Entities

- **Concepts**: Vision Token Pruning, Multimodal Fusion Depth, [Layer-wise Early Exit](../../../../wiki/concepts/layer-wise-early-exit.md), Differentiable Top-K Selection, Prefill Cost Reduction
- **Methods**: HiDrop, Late Injection, Concave Pyramid Pruning, Early Exit (layer-wise vision token exit), differentiable top-k, inter-layer similarity measure, FlashAttention, LLaVA-1.5, PDrop (baseline), TwigVLM (baseline), VoCo-LLaMA (baseline)
- **Datasets**: MME-Perception, MMBench, MMBench-CN, [GQA](../../../../wiki/datasets/gqa.md), VQAv2, ScienceQA-Image, VizWiz, TextVQA, [POPE](../../../../wiki/datasets/pope.md), SEED-Image, [MMStar](../../../../wiki/datasets/mmstar.md)

Tags: `vision-token-pruning`, `mllm`, `early-exit`, `llava`, `inference-efficiency`, `false-positive-match`, `off-topic`

---

Record id: `title:b2302bb0271de496`
