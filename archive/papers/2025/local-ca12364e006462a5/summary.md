<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Revisiting Overthinking in Long Chain-of-Thought from the Perspective of Self-Doubt

- **Authors**: Keqin Peng, Liang Ding, Yuanxin Ouyang, Meng Fang, Dacheng Tao
- **Venue**: preprint
- **Published**: 2025-01-01
- **Source**: local
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

The paper quantifies overthinking in long chain-of-thought reasoning through a new self-doubt lens (LLM-judged categories SD / OT-without-SD / NOT), finds self-doubt (redundant re-verification of an already-correct answer) is a major cause, and shows a simple input-validity-checking prompt reduces response length by 37.1% on average while improving accuracy by 3.6% across four RLLMs, and improves abstain behavior on missing-premise datasets.

## Problem

Long chain-of-thought reasoning boosts accuracy but causes reasoning models to keep verifying or re-deriving an already-correct answer, generating unnecessary tokens (overthinking) and increasing inference cost; prior work analyzed this only qualitatively via sample inspection, without a quantitative account of what specifically drives it or a training-free fix grounded in that cause.

## Contributions

- Proposes a quantitative, LLM-judge-based categorization of reasoning paths into three classes — Overthinking with Self-Doubt (SD), Overthinking without Self-Doubt (OT w/o SD), and Non-Overthinking (NOT) — and uses it to show self-doubt (excessive re-verification of an already-correct answer) is a major, previously under-quantified driver of overthinking, accounting for nearly 60% of cases on MATH-500 with DeepSeek-R1-Distill-Qwen-32B.
- Introduces a prompting method (no training) that first asks the model to assess the validity/completeness of the input question and then answer concisely or state what information is missing, framed as reducing the model's overreliance on / deference to user input (motivated by social comparison theory).
- Shows the method reduces average response length by 37.1% while improving average accuracy by 3.6% across 4 RLLMs (DeepSeek-R1-Distill-Qwen-14B/32B/70B, Qwen3-32B) on GSM8K, GSM8K-Zero and MATH-500.
- Shows the method substantially improves abstain rate (correctly identifying a missing premise) and reduces token consumption on four Missing-Premise (MiP) datasets (MiP-Formula, MiP-SVAMP, MiP-GSM8K, MiP-MATH), e.g. cutting MiP-Formula length from >5,000 to about 1,000 tokens.
- Demonstrates via a reasoning-step count (Figure 2) and a self-doubt-ratio metric (Table 4) that the method reduces both the number of reasoning steps and the self-doubt ratio, with a 23.8-point reduction in self-doubt ratio on MATH-500, though self-doubt ratio increased on GSM8K.

## Method

The authors first quantify overthinking via self-doubt: they generate reasoning paths for GSM8K, GSM8K-Zero and MATH-500 using DeepSeek-R1-Distill-Qwen-32B, then use Qwen2.5-72B-Instruct as an automated judge (given the question, model answer and reference answer) to classify each path into one of three categories: Overthinking with Self-Doubt (unnecessarily long + repeats verification of an already-correct answer), Overthinking without Self-Doubt (unnecessarily long but no redundant verification), or Non-Overthinking. Long CoTs are split at the delimiter \n\n into two segments and the second segment is used to judge self-doubt, since self-doubt tends to appear later in the response. Motivated by social comparison theory (the idea that heavy reliance on others' evaluations induces self-doubt when those evaluations are unfavorable or inconsistent), the authors attribute LLM self-doubt to excessive deference to the user/input question. Their mitigation is a prompting change only (no fine-tuning): the baseline prompt is just the question; their prompt appends an instruction telling the model to first check, before reasoning deeply, whether all necessary information is available, to explicitly state if any key data is missing or ambiguous, and otherwise to answer with the minimum number of tokens required (exact templates in Table 2). This is tested across DeepSeek-R1-Distill-Qwen-14B/32B/70B and Qwen3-32B, temperature 0.

## Results

Table 1 (well-defined math tasks, baseline vs. their prompting method, 4 models): DeepSeek-R1-Distill-Qwen-14B average across GSM8K/GSM8K-Zero/MATH-500: length 1585→913, accuracy 88.6→90.3. DS-Distill-32B: length 1407→1066, accuracy 86.5→92.8. DS-Distill-70B: length 1335→933, accuracy 87.1→92.1. Qwen3-32B: length 2502→1385, accuracy 94.7→94.5. The paper's own headline (page 3, bold text under Table 1): average reasoning length reduced by -37.1% while accuracy improves by +3.6%, and on GSM8K-Zero with DeepSeek-R1-Distill-Qwen-32B and DeepSeek-R1-Distill-Llama-70B accuracy improves by +16.7% and +14.7% respectively. Table 3 (four Missing-Premise datasets, same 4 models, metric = response length and abstain rate): method reduces token consumption by more than 80% on MiP-Formula (e.g. DS-Distill-14B: 5740→735 tokens, abstain rate 54.0%→96.0%; text states MiP-Formula drops from 'more than 5,000 tokens to about 1,000'), and improves abstain rate by nearly 40 points on MiP-Formula and MiP-GSM8K per the paper's text. Table 4 (self-doubt ratio, DeepSeek-R1-Distill-Qwen-32B, 3 datasets): GSM8K 5.9→17.2 (an increase, delta -11.3 as tabulated), GSM8K-Zero 13.5→10.1 (delta +3.5, a reduction), MATH-500 62→38.2 (delta +23.8, the paper's headline self-doubt reduction). Figure 1 (pie charts, DeepSeek-R1-Distill-Qwen-32B baseline): overthinking (SD+OT w/o SD) proportions were GSM8K 80.8% (SD 8.8%, OT w/o SD 72.0%), GSM8K-Zero 92.3% (SD 35.5%, OT w/o SD 56.8%), MATH-500 82.7% (SD 59.5%, OT w/o SD 23.2%) — self-doubt alone was ~59.5% of all MATH-500 cases.

## Limitations

The paper's own stated limitations: (1) Domain and task scope — the prompting strategy is evaluated only on three mathematical reasoning benchmarks (GSM8K, GSM8K-Zero, MATH-500) and four missing-premise datasets; it is unclear whether the same reduction in overthinking/self-doubt holds for other reasoning domains such as commonsense QA, multi-step planning, or multimodal tasks. (2) Reliance on automated evaluation — the quantitative analysis of overthinking and self-doubt depends on an LLM-based judge (Qwen2.5-72B-Instruct) and a simple paragraph-segmentation heuristic (splitting on \n\n and using the second segment) to categorize reasoning paths, which may introduce biases or misclassifications if the evaluator misunderstands nuanced reasoning patterns or misses subtle verification steps. Additionally, on GSM8K the self-doubt ratio increased under their method (Table 4), which the authors attribute to early verification of question correctness combined with short reasoning paths, an effect not fully explained.

## Why it matters here

- **overthinking**: Directly targets the cluster's central accuracy/efficiency tradeoff question, but from a causal-mechanism angle rather than a stopping-rule angle: instead of proposing when to halt generation (as RCP/RCPD, ThinkBrake, NEAT, DEER, BLADE, REFRAIN and Minimal Sufficient CoT do), it argues overthinking is substantially explained by self-doubt (repeated re-verification of a correct answer, attributed to the model's deference to user input) and shows a prompt-only intervention that heads off that self-doubt before generation starts, cutting length 37.1% and improving accuracy 3.6% on average. It also extends the cluster's evaluation surface to missing-premise (MiP) datasets, where the relevant metric is abstain rate rather than accuracy, showing the same intervention improves the model's willingness to say a premise is missing rather than reasoning at length toward a forced answer.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), self-doubt, long chain-of-thought, social comparison theory applied to LLM self-verification, missing-premise (MiP) questions, input-validity prompting
- **Methods**: self-doubt-based overthinking classification (SD / OT w/o SD / NOT), LLM-as-a-judge (Qwen2.5-72B-Instruct), input-validity-checking prompt, reasoning-step counting via \n\n segmentation, self-doubt ratio metric
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), GSM8K-Zero, [MATH-500](../../../../wiki/datasets/math500.md), MiP-Formula, MiP-SVAMP, MiP-GSM8K, MiP-MATH

Tags: `overthinking`, `self-doubt`, `chain-of-thought`, `prompting`, `missing-premise`, `mathematical-reasoning`, `training-free`

## Abstract

Reasoning Large Language Models (RLLMs) have demonstrated impressive performance on complex tasks, largely due to the adoption of Long Chain-of-Thought (Long CoT) reasoning. However, they often exhibit overthinking — performing unnecessary reasoning steps even after arriving at the correct answer. Prior work has largely focused on qualitative analyses of overthinking through sample-based observations of long CoTs. In contrast, we present a quantitative analysis of overthinking from the perspective of self-doubt, characterized by excessive token usage devoted to re-verifying already-correct answer. We find that self-doubt significantly contributes to overthinking. In response, we introduce a simple and effective prompting method to reduce the model's overreliance on input questions, thereby avoiding self-doubt. Specifically, we first prompt the model to question the validity of the input question, and then respond concisely based on the outcome of that evaluation. Experiments on three mathematical reasoning tasks and four datasets with missing premises demonstrate that our method substantially reduces answer length and yields significant improvements across nearly all datasets upon 4 widely-used RLLMs. Further analysis demonstrates that our method effectively minimizes the number of reasoning steps and reduces self-doubt.

---

Record id: `local:ca12364e006462a5`
