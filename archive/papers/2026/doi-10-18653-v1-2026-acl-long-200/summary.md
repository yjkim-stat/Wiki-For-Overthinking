<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Thermometer of Thoughts: Enhancing LLM’s Exploration via Attention Temperature Modulation

- **Authors**: Zhiyuan Yu, Shijian Xiao, Cam-Tu Nguyen, Zhangyue Yin, Lekai Xing, Wenzhong Li, Sanglu Lu
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.200/>
- **PDF**: <https://aclanthology.org/2026.acl-long.200.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.200
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## In one line

Introduces attention-temperature modulation (softening/sharpening the attention softmax at inference, distinct from decoding-temperature sampling) as a difficulty-adaptive exploration control -- higher attention temperature broadens exploration and helps hard problems, lower temperature curbs overthinking and helps easy ones -- and pairs it with a difficulty-induced weighted-voting aggregation scheme (Thermometer of Thoughts), improving Pass@10 by 6.78-14.20% and aggregation accuracy by 9.74% across seven reasoning benchmarks.

## Problem

Standard exploration-diversity techniques for LLM reasoning rely on output-level stochastic decoding (sampling from the fixed next-token distribution), which only explores within the model's existing reasoning patterns and cannot escape a local optimum in the solution space, limiting genuine diversity of reasoning pathways -- and it was unknown whether perturbing the model's internal attention mechanism, rather than its output distribution, could provide more fundamental exploration control.

## Contributions

- attention temperature modulation, a novel exploration-control mechanism that directly perturbs the attention mechanism's internal focus (rather than the output token distribution), shown to enhance LLM reasoning exploration without compromising reasoning capability within a safe range
- empirical characterization of attention temperature as difficulty-adaptive: higher temperature broadens exploration and benefits hard problems, while lower temperature curbs overthinking and benefits easy problems, validated via a four-level output-quality rubric and a difficulty-stratified token/accuracy analysis
- Thermometer of Thoughts (ToT), a two-stage inference strategy combining Attention Temperature Scaling with Difficulty-Induced weighted-voting Aggregation, improving Pass@10 by 6.78-14.20% and aggregation accuracy by 9.74% on average across 7 reasoning benchmarks and 4 models
- a Continuation Tendency Score (CTS) metric providing direct evidence that attention temperature reshapes the qualitative reflection/exploration structure of reasoning chains, distinct from and stronger than decoding temperature's effect

## Method

Introduces attention temperature tau, a scaling factor inserted into the attention softmax (1/sqrt(d_k) -> 1/(tau*sqrt(d_k))), implemented with a one-line change to each layer's attention scaling (no extra inference parameter needed in the API sense) -- distinct from decoding temperature, which only reshapes the output token distribution. Defines attention entropy (over top-K attention weights) and decoding entropy, and empirically shows these correlate more strongly on harder benchmarks (AIME2024, HMMT) than easier ones (GSM8K), motivating attention temperature as a lever for reasoning depth. Validates via a four-level output-quality rubric (DeepSeek-R1 as judge) that attention temperature in [0.9, 1.1] does not degrade output quality or reasoning capability, while temperatures below 0.5 or above 1.7 cause reasoning chains to become irrelevant. Proposes a two-stage inference strategy, Thermometer of Thoughts (ToT): (1) Attention Temperature Scaling (ATS) generates n reasoning traces per question at each of k distinct attention temperatures (spanning the safe range) to diversify reasoning traces beyond what decoding-temperature sampling alone can reach; (2) Difficulty-Induced Aggregation (D-induced) first estimates problem difficulty from the answer consensus (confidence score C_low) among the lowest-temperature generations -- if C_low exceeds a threshold theta, the problem is classified simple and majority voting is applied only to the low-temperature generations (computational efficiency); otherwise the problem is classified challenging and all generations across all temperatures are aggregated via temperature-weighted voting, where higher-temperature (more exploratory) generations receive exponentially higher weight via a scaling parameter beta.

## Results

Across four reasoning models (Hunyuan-1.8B-Instruct, Qwen3-0.6B, Qwen3-1.7B, DeepSeek-R1-Distilled-Qwen-1.5B) and seven benchmarks (MATH500, AIME2024, AIME2025, HMMT, GSM8K, GPQA, HumanEval), attention temperature sampling (ATS) achieves Pass@10 improvements of 6.78% (Qwen3-1.7B) and 14.20% (Qwen3-0.6B) over conventional random next-token sampling, and consistently exceeds decoding-temperature sampling (DTS) by more than 1.3 points -- the improvement holds on general reasoning (GPQA) and coding (HumanEval) tasks as well as math, confirming attention temperature produces genuinely more diverse/effective exploration than output-distribution perturbation alone. Difficulty-Induced Aggregation (D-induced) achieves an average relative improvement of 9.74% over plain majority voting across all model/dataset settings, with the largest gains concentrated on the hardest competition benchmarks (AIME2024/2025, HMMT: average +16.2%) versus more modest gains on easier tasks (GSM8K +2.6%, GPQA +4.2%) -- confirming that difficulty-adaptive aggregation matters most where naive uniform voting is weakest. A difficulty-stratified analysis on MATH500 with Qwen3-1.7B (Figure 5) shows the interior mechanism directly: at low difficulty levels (1-2), reducing attention temperature yields shorter (up to 41.7% fewer tokens) responses without hurting accuracy, curbing overthinking, while at high difficulty levels (4-5), raising attention temperature increases both token count (up to +31.9%) and accuracy, broadening the exploration basis for hard problems. A reasoning-pattern analysis via a novel Continuation Tendency Score (CTS, measuring how often adjacent reasoning segments continue linearly vs. transition into reflection/alternative-exploration) shows CTS shifts downward (more reflection/exploration) as attention temperature increases on AIME2024, with no corresponding trend for decoding temperature -- direct evidence that attention temperature, unlike decoding temperature, shapes the qualitative structure of reasoning, not just surface-level token diversity. Layer-wise and head-wise (non-uniform) attention-temperature perturbations both degrade performance versus a uniform setting (Pass@10 drops of 2.37% and 2.91% respectively), indicating a consistent temperature across the whole model is important for stable reasoning patterns.

## Limitations

Because the method requires modifying LLM source code (attention-layer scaling), it cannot be evaluated on API-only proprietary models such as GPT-5. Due to computational resource constraints, the paper did not investigate whether attention-temperature scaling continues to help at larger model scales (e.g. Qwen3-32B) beyond the up-to-1.8B/1.7B models tested. Time constraints prevented conducting additional reasoning-trajectory sampling that could further mitigate randomness-related variance in the reported results.

## Why it matters here

- **overthinking**: Central to the topic: explicitly identifies overthinking on simpler problems as a target and shows lowering attention temperature curbs it (fewer tokens, no accuracy loss), while the same mechanism at higher temperature helps genuinely hard problems by broadening exploration -- a single tunable inference-time control spanning both ends of the accuracy/efficiency tradeoff, rather than the usual asymmetric approach of penalizing length only. Its distinction between attention temperature (reshaping internal focus/reasoning structure, evidenced via the Continuation Tendency Score) and decoding temperature (only reshaping output token diversity) is a mechanistic insight relevant to any paper in this archive that manipulates sampling temperature as a length- or exploration-control lever.

## Entities

- **Concepts**: attention temperature (attention-softmax scaling), attention entropy vs. decoding entropy, difficulty-induced aggregation, Continuation Tendency Score (CTS)
- **Methods**: Attention Temperature Scaling (ATS), Difficulty-Induced Aggregation (D-induced), Thermometer of Thoughts (ToT), decoding temperature sampling (DTS, baseline), random sampling (RS, baseline)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH500](../../../../wiki/datasets/math500.md), [AIME2024](../../../../wiki/datasets/aime-2024.md), [AIME2025](../../../../wiki/datasets/aime-2025.md), [HMMT](../../../../wiki/datasets/hmmt.md), [GPQA](../../../../wiki/datasets/gpqa.md), [HumanEval](../../../../wiki/datasets/humaneval.md)

Tags: `overthinking`, `test-time-scaling`, `attention-mechanism`, `difficulty-adaptive-reasoning`, `exploration`

## Abstract

Improving the exploration of reasoning is essential for advancing Large Language Models’ (LLMs) problem-solving performance. Current methods primarily rely on output-level stochasticity, which decode within fixed reasoning patterns of LLM and suffer from insufficient exploration. In this paper, we introduce adjusting attention temperature to directly modulate the model’s internal focus during reasoning, which enables a dynamic shift between exploratory and focused processing. We reveal that moderate adjustments preserve LLM’s reasoning capability while producing problem hardness-dependent benefits: higher temperatures facilitate solving complex tasks by encouraging wider exploration, whereas lower temperatures mitigate overthinking on simpler problems. Leveraging this insight, we propose a two-stage inference strategy: first, attention temperature scaling modulates the LLM’s reasoning patterns to diversify the reasoning traces; then, a difficulty-aware aggregation scheme is introduced to effectively identify the most reliable solution from the generated candidates. Extensive evaluations show that our method improves Pass@10 by 6.78–14.20% and aggregation accuracy by 9.74% across 7 reasoning benchmarks.

---

Record id: `doi:10.18653/v1/2026.acl-long.200`
