<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Inference Compute-Optimal Video Vision Language Models

- **Authors**: Peiqi Wang, ShengYun Peng, Xuewen Zhang, Hanchao Yu, Yibo Yang, Lifu Huang, Fujun Liu, Qifan Wang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2025.acl-long.117/>
- **PDF**: <https://aclanthology.org/2025.acl-long.117.pdf>
- **DOI**: 10.18653/v1/2025.acl-long.117
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Derives, via large-scale training sweeps and a parametric power-law model of task error, the inference-compute-optimal allocation across LM size, frame count, and tokens-per-frame for video vision-language models, finding jointly scaling all three factors matters, that optimal allocation is highly task-specific, and that as finetuning data grows the optimal frontier shifts toward more frames/tokens and a smaller LM.

## Problem

Video vision-language models are deployed at massive inference scale (routinely processing millions of videos), so inference compute -- not training compute -- dominates total cost, yet no prior work identifies the inference-compute-optimal way to jointly allocate a fixed per-example inference budget across language model size, video frame count, and visual tokens per frame, together with the interacting effect of finetuning data size.

## Contributions

- a formal framework and cost model for inference-compute-optimal allocation across LM size, frame count, and visual tokens per frame in video VLMs, distinct from training-compute-optimal scaling laws
- an additive power-law-with-interaction parametric model of task error (add-interact) fit from large-scale training sweeps (~100k A100 hours) that outperforms simpler additive/multiplicative forms
- empirical evidence that the inference-compute-optimal allocation is highly task-specific, and that it shifts toward larger visual representations (more frames, more tokens per frame) and a smaller LM as available finetuning data grows

## Method

Defines the inference compute cost of a LLaVA-like video VLM as a function of LM size (x_N), frame count (x_T), and tokens-per-frame (x_V), including both the vision encoder's and the LM's FLOPs. Conducts two types of training sweeps on video-instruction data (~2.2M examples): a 'star sweep' varying one factor at a time from an inference-compute-intensive center across three finetuning data sizes (0.25M/0.5M/1M), and an 'isoFLOP sweep' jointly varying all three factors while holding total inference FLOPs fixed at four budgets (2/5/15/30 TFLOPs) at a fixed finetuning size (n=2M). Fits several parametric functional forms for task error as a function of (x, n), finding an additive power-law-with-interaction-term model ('add-interact') fits best via 5-fold cross-validation, then solves a constrained discrete optimization (brute-force search, since practical LM sizes/token counts are discrete) to find the inference-compute-optimal scaling factors x*(c;n) for a given compute budget c and data size n. Evaluates across eight diverse video tasks (captioning, open-ended QA, multiple-choice QA, long-video understanding, fine-grained perception).

## Results

Jointly scaling all three factors (x_N, x_T, x_V) is necessary for optimal performance: at a fixed 30-TFLOP budget, a 7.5B-parameter LM outperforms a 1B LM, and increasing compute from 15 to 30 TFLOPs yields only marginal gains for the 1B model but a large gain for the 7.5B model -- LM size is a bottleneck that frame/token scaling alone cannot overcome. Performance improves with both scaling factors and finetuning data size but with diminishing returns; the add-interact parametric model achieves R^2=0.99 in-distribution but extrapolates unevenly across tasks (LongVideoBench and Next-QA show >5% average relative error, corresponding to >3-point deviation on a 0-100 scale, while most other tasks extrapolate well). The utility of each scaling factor is highly task-dependent: increasing frame count x_T yields larger gains than increasing finetuning data n for long-video-understanding tasks (e.g. LongVideoBench), whereas for fine-grained perception (PerceptionTest) the optimal frontier favors more visual tokens per frame x_V over more frames x_T. As finetuning data size n grows from 1M to 10M, the compute-optimal frontier's elasticity analysis shows a consistent (though task-varying) trend: optimal LM size x_N* shifts downward (negative elasticity) while optimal frame count x_T* and tokens-per-frame x_V* shift upward (positive elasticity) -- i.e., with more finetuning data available, it becomes optimal to spend a fixed inference budget on richer visual representations rather than a larger LM. The compute-optimal frontier itself is non-monotonic (not monotonically non-decreasing) due to the discrete, coarse-grained domain of available LM sizes and token-count values. Scaling frame count x_T generally yields larger performance gains than scaling tokens-per-frame x_V for a fixed compute increase, suggesting improving the vision model's ability to process more frames is more impactful than increasing per-frame token resolution.

## Limitations

Inference compute is estimated via theoretical FLOPs, which the paper explicitly notes is insufficient for real-world deployment because it omits hardware-utilization gaps between theoretical peak and actual throughput, the compute/memory-bandwidth split between prefilling and decoding stages (only prefilling-stage compute is modeled), and modern inference-efficiency techniques like quantization and speculative decoding. Vision-model size itself is not varied (SoViT-400m/14 vision encoder held fixed throughout, since suitable model families at multiple sizes were unavailable), even though prior work suggests jointly scaling language and vision model size matters. Only three LM sizes (1B, 3B, 8B, from the Llama-3.2 family) were tested due to a gap in available pretrained sizes between 8B and 70B, potentially limiting how well the LM-size relationship is captured. Video instruction dataset, LM family, and downsampling method (bilinear interpolation) are all held fixed rather than varied, and the parametric model's extrapolation reliability varies substantially by task (poor for LongVideoBench and Next-QA).

## Why it matters here

- **overthinking**: Adjacent rather than central: this is compute-optimal allocation for video VLM *input representation* (how many frames, how many visual tokens) rather than for LLM *reasoning-trace length*, but it is methodologically close to the topic's core question -- given a fixed inference budget, how should it be spent to maximize task performance -- and its finding that the optimal allocation is highly task-specific and shifts with available data is a structural parallel to overthinking's claim that a fixed 'think more' policy is suboptimal because the right amount of test-time compute depends on the problem.

## Entities

- **Concepts**: inference-compute-optimal frontier (vs. training-compute-optimal), joint scaling of LM size / frame count / tokens-per-frame, add-interact parametric error model, elasticity of optimal scaling factors to data size
- **Methods**: star sweep / isoFLOP sweep training, add-interact parametric power-law modeling, bootstrap aggregation (bagging), constrained discrete optimization (brute-force search)
- **Datasets**: LLaVA-Video-178K (finetuning source), Video Detailed Caption (VDC), ActivityNet-QA (AQA), VCGBench (VCG), LongVideoBench (LVB), PerceptionTest (PT), MVBench (MV), Video-MME (VMME), Next-QA (NQA)

Tags: `compute-optimal`, `test-time-compute`, `video-vision-language-models`, `scaling-laws`, `inference-efficiency`

## Abstract

This work investigates the optimal allocation of inference compute across three key scaling factors in video vision language models: language model size, frame count, and the number of visual tokens per frame. While prior works typically focuses on optimizing model efficiency or improving performance without considering resource constraints, we instead identify optimal model configuration under fixed inference compute budgets. We conduct large-scale training sweeps and careful parametric modeling of task performance to identify the inference compute-optimal frontier. Our experiments reveal how task performance depends on scaling factors and finetuning data size, as well as how changes in data size shift the compute-optimal frontier. These findings translate to practical tips for selecting these scaling factors.

---

Record id: `doi:10.18653/v1/2025.acl-long.117`
