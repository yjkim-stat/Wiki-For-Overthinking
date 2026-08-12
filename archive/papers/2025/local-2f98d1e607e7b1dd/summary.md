<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Measuring Chain-of-Thought Monitorability Through Faithfulness and Verbosity

- **Authors**: Austin Meek, Eitan Sprejer, Iván Arcuschin, Austin J. Brockmeier, Steven Basart
- **Venue**: preprint
- **Published**: 2025-01-01
- **Source**: local
- **Topics**: reasoning-faithfulness, reasoning-training, test-time-scaling
- **Relevance score**: reasoning-faithfulness 0.50, reasoning-training 0.50, test-time-scaling 0.50

## In one line

Argues that faithfulness alone is insufficient for CoT monitoring and adds verbosity — whether the trace lists every factor needed to solve the task — combining the two into a monitorability score, then shows models can look faithful while omitting key factors.

## Problem

CoT monitoring for AI safety depends on the trace being a real window into the model's reasoning, but the standard faithfulness proxy is narrow: insert a cue into the prompt, check whether the answer changes, and if it does, check whether the CoT mentions the cue. That measures one moment and discards information whenever the model keeps its answer — which is common, and often the desirable behaviour, since a capable model should be able to reject a sycophantic cue, a jailbreak prompt or false information. It also says nothing about aspects of the reasoning not tied to the injected cue, so a trace can pass while leaving most of the reasoning unverbalized.

## Contributions

- A two-axis definition of monitorability: faithfulness as transparency about the model's internal reasoning process, operationalized as the rate at which an injected cue is acknowledged, and verbosity as explicit disclosure of the factors relevant to the task.
- An LLM-based pipeline for extracting the causal factors required to solve each problem in the benchmark, released as a dataset, which is what makes verbosity measurable.
- A crucial definitional change from prior work: a model that acknowledges a cue but keeps its answer counts as faithful, so 'non-switch' cases enter the measurement instead of being discarded or counted faithful by default.
- An evaluation across four matched pairs of instruction-tuned and reasoning models on BBH, GPQA and MMLU, with a per-cue-type breakdown across five cue categories.
- A public implementation on the Inspect evaluation library, plus the causal-factor dataset and all model transcripts.

## Method

For every task a baseline prompt and a cued prompt are created, the latter injecting an explicit cue pointing at an answer different from the model's baseline answer. Five cue types are used: a sycophantic appeal to a Stanford professor, a visual pattern marking correct answers with a black square, embedded metadata carrying an answer and a success rate, grader hacking via a hidden validation function, and unethically obtained information. Verbosity is measured by first having five judge models (Claude 4 Sonnet, QwQ-32b, DeepSeek-R1-0528, Gemini 2.5 Flash, Gemma 3 27B-IT) each enumerate the factors necessary to solve a question, then concatenating those lists and passing them to Claude 4 Sonnet for de-duplication and removal of trivial factors — yielding on average 8.6 factors for BBH, 10.7 for GPQA and 9.2 for MMLU. A lightweight judge (QwQ-32b) then checks how many of those factors appear in the baseline CoT, and separately whether the cued CoT explicitly acknowledges the injected cue. For non-reasoning models the output is evaluated; for reasoning models both the reasoning section and the final output. The monitorability score is the mean of the two, with the authors noting that other monotonic combinations (weighted average, geometric mean, minimum) would also work. All generations use temperature 0. The reasoning trace is framed by a 'workbench' analogy: verbosity is laying out all the tools and materials, faithfulness is doing the processing on them in view.

## Results

Reasoning models are consistently more monitorable than their instruction-tuned counterparts, on both axes and across all four model pairs — DeepSeek-R1 is highest overall at 78.3% average monitorability and Claude 3.7 Sonnet with extended thinking second at 68.8%; within the Qwen family, Qwen 3 Thinking leads at 67.3% and Qwen 3 scores 59.2% against Qwen 2.5's 42.2%. Verbosity tracks faithfulness rather than trading against it, so longer traces do carry more information — but only to a point, after which performance deteriorates at an inverse scaling law, meaning highly monitorable and highly performant are in tension. Cue type matters enormously: the Stanford-professor sycophancy cue is the most monitorable at 89.2% for Claude 3.7 Sonnet, while other cues are much harder. The largest reasoning-versus-instruction gaps appear on the unethically-sourced-information cue, where Claude 3.7 Sonnet exceeds Claude 3.5 by 43.8 points and DeepSeek-R1 exceeds DeepSeek-V3 by 32.8; the Stanford cue also produces a 37.8-point gap between QwQ-32B (81.7%) and Qwen 2.5 72B (43.9%). Dataset difficulty is inversely related to monitorability: GPQA-Diamond scores lowest and BBH highest. On the state-transition analysis, the case prior work discards is the dominant one: instances where the model is correct at baseline, is then cued toward an incorrect answer, and stays correct account for 66.4% (Claude 3.5 Sonnet) to 80.3% (Qwen-3-235B) of all samples. Monitorability scores are similar across all four transition types, which is the paper's argument that marking non-switch cases faithful by default, or ignoring them, throws away most of the available signal.

## Limitations

The paper's own: the design favours tractability over exhaustiveness — single-turn, temperature-0 question answering, lightweight judge models for grading, and verbosity scored by recall. It states directly that the verbosity metric can be gamed, since a model could raise its score by echoing the prompt or listing extra factors, and notes verbosity correlates with response length at Pearson r = 0.209. More advanced reasoning behaviour such as backtracking is not captured. Named next steps are human-verified causal factors, richer cue sets, and extension to multi-turn or agentic settings. A reader should add that the pipeline is model-judged end to end — factors are enumerated by five LLMs, de-duplicated by a sixth, and both scores assigned by a seventh — so the benchmark measures agreement with a panel's notion of what a problem requires; human calibration of the verbosity metric is reported only in an appendix. The monitorability score is also an unweighted mean of two quantities on different footings, one a rate over five injected cues and the other a recall over roughly nine judged factors, and the paper offers no argument for equal weighting beyond simplicity.

## Why it matters here

- **reasoning-faithfulness**: The paper that names what this topic's standard measurement misses, and the gap is larger than it first appears: the case prior work discards — model acknowledges a cue and keeps its answer — is 66-80% of all samples here. That reframes faithfulness measurement as a coverage problem rather than a detection problem. The verbosity axis is the genuinely new contribution for this archive: every other faithfulness result here asks whether a specific influence was reported, and none asks whether the trace lays out what solving the problem requires at all. A trace can pass the cue test and still be unmonitorable by omission, which is the failure mode a safety scheme built on reading traces would actually encounter. Two findings sharpen the archive's picture. Reasoning models being more monitorable than their instruction-tuned pairs runs against the inverse-scaling result reported elsewhere here, that larger and more capable models produce less faithful reasoning — the two are measuring different things (capability scaling versus reasoning-training), and holding both is more informative than choosing. And the observed tension between verbosity and performance, deteriorating at an inverse scaling law past a point, states the cost of monitorability as a quantity rather than an aspiration, which connects directly to the epiphenomenal-tail and early-exit work in this archive: the tokens that make a trace more monitorable are partly the same tokens those methods cut.

## Entities

- **Concepts**: [monitorability](../../../../wiki/concepts/monitorability.md), [chain of thought faithfulness](../../../../wiki/concepts/chain-of-thought-faithfulness.md), [verbosity](../../../../wiki/concepts/verbosity.md), causal factors, cue acknowledgement, working memory analogy, [sycophancy](../../../../wiki/concepts/sycophancy.md), steganography, sandbagging, [post-hoc rationalization](../../../../wiki/concepts/post-hoc-rationalization.md), [inverse scaling](../../../../wiki/concepts/inverse-scaling.md)
- **Methods**: cue injection, [LLM as a judge](../../../../wiki/methods/llm-as-a-judge.md), causal factor extraction, monitorability scoring, Inspect evaluation library
- **Datasets**: [BBH](../../../../wiki/datasets/bbh.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), [MMLU](../../../../wiki/datasets/mmlu.md)

Tags: `monitorability`, `faithfulness`, `verbosity`, `cot monitoring`, `ai safety`, `cue injection`, `benchmark`

## Abstract

Chain-of-thought (CoT) outputs let us read a model's step-by-step reasoning. Since any long, serial reasoning process must pass through this textual trace, the quality of the CoT is a direct window into what the model is thinking. This visibility could help us spot unsafe or misaligned behavior (monitorability), but only if the CoT is transparent about its internal reasoning (faithfulness). Fully measuring faithfulness is difficult, so researchers often focus on examining the CoT in cases where the model changes its answer after adding a cue to the input. This proxy finds some instances of unfaithfulness but loses information when the model maintains its answer, and does not investigate aspects of reasoning not tied to the cue. We extend these results to a more holistic sense of monitorability by introducing verbosity: whether the CoT lists every factor needed to solve the task. We combine faithfulness and verbosity into a single monitorability score that shows how well the CoT serves as the model's external 'working memory', a property that many safety schemes based on CoT monitoring depend on. We evaluate instruction-tuned and reasoning models on BBH, GPQA, and MMLU. Our results show that models can appear faithful yet remain hard to monitor when they leave out key factors, and that monitorability differs sharply across models. We release our evaluation code using the Inspect library, along with two datasets containing causal factors and model transcripts, to support reproducible future work.

---

Record id: `local:2f98d1e607e7b1dd`
