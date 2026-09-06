<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# On Reasoning Strength Planning in Large Reasoning Models

- **Authors**: Leheng Sheng, An Zhang, Zijian Wu, Weixiang Zhao, Changshuo Shen, Yi Zhang, Xiang Wang, Tat-Seng Chua
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: local
- **Topics**: overthinking

## In one line

Finds that large reasoning models pre-plan how many reasoning tokens a question will need, encoded as a single pre-allocated direction vector in their activations whose magnitude can be read out to predict reasoning length or added/subtracted to causally control it.

## Problem

LRMs are known to allocate more reasoning tokens to harder questions, but why and how this difficulty-aware length allocation happens internally was unexplored; the paper asks whether the reasoning strength is planned before generation begins and, if so, how that plan is encoded in the model's activations.

## Contributions

- Shows via linear probing on question-only activations (before the first reasoning token) that the eventual reasoning token count is predictable in advance, with Spearman correlation over 0.8 across model sizes and families.
- Extracts a single pre-allocated direction vector via difference-in-means across MATH difficulty levels, showing near-identical direction (cosine similarity ~0.99) across difficulty pairs and layers, with magnitude tracking the extra reasoning tokens required.
- Demonstrates the vector causally controls reasoning length via activation steering: subtracting it shortens reasoning and can reduce performance, adding it lengthens reasoning and can improve performance up to a point (e.g. average accuracy across MATH500/AIME2024/OlympiadBench rising from 51.84% to 52.42% for R1-Distill-Qwen-1.5B, and from 73.75% to 75.43% for R1-Distill-Qwen-32B, under moderate positive steering).
- Shows the vector operates by shifting the logit of the end-of-reasoning token </think> far more than it shifts logits of random tokens or the eos token, and demonstrates two applications: detecting overthinking before generation (the predictor yields higher predicted lengths for overthink-attack-forced AlpacaEval questions than for vanilla ones) and cutting reasoning tokens on easy questions (MMLU, MATH500 Level-1) via negative steering without hurting accuracy.

## Method

Linear probing: a Lasso-regularized linear regression is fit on the residual-stream activation h^(l) at the position of the start-of-reasoning <think> token (before any reasoning token is generated) at each layer l, to predict the eventual reasoning token count; this establishes that the strength is decided in advance from question activations alone (Spearman R up to 0.84, improving with layer depth). Difference-in-means is then used to extract a 'pre-allocation vector' r^(l) at each layer, computed as the difference between mean <think>-position activations of hard-difficulty and easy-difficulty MATH questions; these vectors are nearly identical in direction across difficulty pairs (cosine similarity ~0.99) and their L2 norm scales with the extra reasoning tokens the harder difficulty requires. The intervention is activation steering at inference time: at the <think>-token position, the model's activation h^(l) at a chosen layer l is modified once, before generation, as h^(l)' = h^(l) + lambda * r^(l), where r^(l) is the layer-averaged pre-allocation vector and lambda is a scalar steering strength (tested from -0.2 to +0.2). This single additive shift at the point reasoning begins causally changes how many reasoning tokens are subsequently generated -- negative lambda shortens reasoning, positive lambda lengthens it -- without changing the length of the final answer after </think>. The mechanism is traced further to logits: steering with r^(l) shifts the logit of the end-of-reasoning token </think> (raising it under negative steering, lowering it under positive steering) much more than it shifts logits of random tokens or the <|endoftext|> token, indicating the vector acts by making early or late termination of reasoning more or less likely.

## Results

Linear probes predict reasoning token count from pre-generation activations with Spearman R up to 0.84 (R1-Distill-Qwen-1.5B on MATH), improving in later layers. Pre-allocation vectors across four difficulty-pair contrasts show cosine similarity around 0.99 to 1.0 in later layers. Activation steering with lambda from -0.2 to +0.2: moderate positive steering raises average accuracy across MATH500/AIME2024/OlympiadBench for all five tested models (e.g. 1.5B: 51.84%->52.42%; 7B: 66.91%->68.82%; 14B: 72.37%->74.72%; 32B: 73.75%->75.43%; QwQ-32B: 64.19%->64.65%), but pushing steering strength further does not give additional gains and can degrade performance. Negative steering on MMLU and MATH500-Level-1 substantially cuts reasoning token counts while leaving accuracy essentially unchanged. On AlpacaEval, questions forced into overthinking via an overthink attack receive markedly higher predicted reasoning-token counts than vanilla questions, across all five models tested.

## Limitations

The paper uses only a linear probe and does not test whether more complex architectures (e.g. MLPs) predict reasoning length better. Experiments focus mainly on the Qwen-family model series (DeepSeek-R1-Distill-Qwen at four sizes and QwQ-32B); it is untested whether the findings hold for reasoning models built on other backbones. Difficulty-based experiments for extracting the pre-allocation vector are run only on the MATH dataset's five difficulty levels. The paper reports no measurement of the inference-time compute or latency cost of computing or applying the steering vector itself (extracting activations, adding the vector, or running the linear probe) -- only its effect on the resulting reasoning token count and accuracy.

## Why it matters here

- **overthinking**: Directly studies the mechanism behind difficulty-aware reasoning-length allocation, proposes an inference-time activation-steering intervention to shorten or lengthen reasoning strength, and uses the same predictor to detect overthinking before generation and to cut reasoning tokens on easy questions without accuracy loss.

## Entities

- **Concepts**: reasoning strength planning, pre-allocated direction vector, activation steering, difficulty-aware reasoning length allocation
- **Methods**: linear probing (Lasso regression), difference-in-means direction extraction, [activation steering](../../../../wiki/methods/activation-steering.md)
- **Datasets**: [MATH](../../../../wiki/datasets/math.md), [MATH500](../../../../wiki/datasets/math500.md), [AIME2024](../../../../wiki/datasets/aime-2024.md), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md), [MMLU](../../../../wiki/datasets/mmlu.md), AlpacaEval

Tags: `activation-steering`, `reasoning-length-control`, `interpretability`, `overthinking-detection`, `test-time-compute`, `linear-probing`, `difficulty-awareness`

## Abstract

Recent studies empirically reveal that large reasoning models (LRMs) can automatically allocate more reasoning strengths (i.e., the number of reasoning tokens) for harder problems, exhibiting difficulty-awareness for better task performance. While this automatic reasoning strength allocation phenomenon has been widely observed, its underlying mechanism remains largely unexplored. To this end, we provide explanations for this phenomenon from the perspective of model activations. We find evidence that LRMs pre-plan the reasoning strengths in their activations even before generation, with this reasoning strength causally controlled by the magnitude of a pre-allocated directional vector. Specifically, we show that the number of reasoning tokens is predictable solely based on the question activations using linear probes, indicating that LRMs estimate the required reasoning strength in advance. We then uncover that LRMs encode this reasoning strength through a pre-allocated directional vector embedded in the activations of the model, where the vector's magnitude modulates the reasoning strength. Subtracting this vector can lead to reduced reasoning token number and performance, while adding this vector can lead to increased reasoning token number and even improved performance. We further reveal that this direction vector consistently yields positive reasoning length prediction, and it modifies the logits of end-of-reasoning token </think> to affect the reasoning length. Finally, we demonstrate two potential applications of our findings: overthinking behavior detection and enabling efficient reasoning on simple problems. Our work provides new insights into the internal mechanisms of reasoning in LRMs and offers practical tools for controlling their reasoning behaviors. Our code is available at https://github.com/AlphaLab-USTC/LRM-plans-CoT.

---

Record id: `local:77b3413236375923`
