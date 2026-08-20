<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# CURV: Enhancing Chart Understanding Through Curriculum Visual Grounded Reasoning

- **Authors**: Xuehang Guo, Pingyue Zhang, Ruiyi Zhang, Zhenhailong Wang, Hanrui Lyu, Heng Ji, Tong Sun, Qingyun Wang, Manling Li
- **Venue**: cs.CV
- **Published**: 2026-08-03
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.02833>
- **PDF**: <https://arxiv.org/pdf/2608.02833v1>
- **Topics**: reasoning-training, test-time-scaling
- **Relevance score**: reasoning-evaluation 0.25, reasoning-training 0.40, test-time-scaling 0.40

## In one line

Reformulates chart question answering as a chain in which every reasoning step carries a predicted image region, trains that pairing through a curriculum graded by nesting depth, and finds explicit intermediate grounding worth 8.78 points over letting the model attend implicitly.

## Problem

Multimodal models fail chart questions in a way that is not a reasoning failure or a perception failure alone. The paper's opening measurement separates them: giving a model human-annotated visual information raises accuracy by 18.33 points, prompting it to reason first raises it by 10.00, and doing both raises it by 43.33 — so the two supports are not additive and what is missing is their coupling. Extrinsic chain-of-thought prompting and supplied visual cues both help while neither is internalized, leaving reasoning that proceeds disconnected from the visual evidence it claims to rest on.

## Contributions

- A formulation in which the answer is reached through a sequence of (reasoning step, grounded visual region) pairs rather than a single mapping from image and question to answer
- A two-stage training scheme separating the two halves: first learning to predict the region that grounds a step, then feeding the resulting grounded image state back in as input for generating the next step
- Two distinct notions of task complexity kept apart — the number of reasoning steps a model takes, and the tier of reasoning depth defined as the maximum nesting of logical functions the task actually requires
- A synthetic curriculum dataset built by systematic template instantiation over seven chart types, with each reasoning step paired to ground-truth regions and binary masks
- An evaluation that reports both a model judge and a rule-based scorer at four strictness thresholds, on the stated ground that a judge alone carries known biases

## Method

Chart question answering is written as a mapping from image and question to a sequence of reasoning-step and visual-region pairs and thence to an answer. Stage I supervises the region prediction: at each step the model predicts the visual focus grounding its current reasoning step, conditioned on the image, question and all prior grounding pairs, against ground-truth regions. Stage II makes the grounding operative — the predicted focus is applied to the image to construct a grounded visual state that becomes additional input when generating the next step, with a combined objective over reasoning supervision, grounding loss and final answer. Three ways of realizing the grounded state are compared: applying a mask over the image, drawing a box, and cropping. The curriculum grades tasks by nesting depth across three levels, built from seven chart types and thirty domain categories with only thirty unique charts per type, so multiple question-reason-ground-answer quadruplets are derived from each base image rather than memorizing appearances. Five open models are finetuned — Qwen2.5-VL at 3B and 7B, InternVL3 at 1B, 2B and 8B — against two proprietary and several open baselines, and evaluated on held-out curriculum test sets, four real chart benchmarks and two out-of-domain multimodal ones.

## Results

On the curriculum test sets the finetuned 7B model reaches 69.86, 40.21 and 26.11 under the model judge across the three levels, against its own base model's 54.21, 28.68 and 16.18 — up to 15.65 points, and up to 12.22 above the proprietary baselines. The comparison is closer than the framing suggests: GPT-4.1-mini scores 70.86 at level 1 and 26.14 at level 3, so the finetuned open model leads clearly only at level 2 (40.21 against 37.61) and is effectively tied or behind elsewhere. Transfer holds on real charts (at least 1.20 points across four benchmarks) and out of domain, where the 3B model gains 10.20 on MathVista. The ablations are the useful part. Explicit grounding beats implicit by 8.78 points, which the authors read as visual grounding earning its place as an intermediate vision-reasoning bridge rather than as the final objective. Among grounding realizations, masking beats boxing, and cropping remains competitive (up to 7.93 on the judge metric) despite a sixteen-fold resolution reduction. Curriculum composition matters in a specific direction: training on levels 1 and 2 gives the most consistent gains across all levels, while training on level 3 alone is less effective, so foundational tasks generalize upward better than hard ones generalize downward. Applying the framework under reinforcement learning yields up to 12.58 points and combining it with supervised finetuning 17.04, but the paper reports the RL overhead as substantially higher and states the supervised route as the better efficiency trade.

## Limitations

The paper has no limitations section. What a reader should weigh: the training data is synthetic and template-generated from thirty charts per type, so the curriculum's coverage of reasoning patterns is by construction what the templates encode, and generalization to real charts is demonstrated at margins of 1.20 to a few points rather than at the scale of the in-domain gains. The headline comparison against proprietary models holds at one of three curriculum levels. Grounding supervision requires per-step ground-truth regions and binary masks, which exist here because the data is synthesized and which no real corpus supplies — the method as trained is therefore not directly applicable to existing chart datasets. Absolute accuracy at the hardest level stays low for everything tested (at most 42.54 by the paper's own note), so the multi-chart result is a comparison among weak systems. The macro evaluation uses a model judge from the same family as one of the baselines it scores, and no seeds or variance are reported.

## Why it matters here

- **reasoning-training**: The 8.78-point gap between explicit and implicit grounding is the transferable result, and it is a training claim rather than an architectural one: the same model attending to the same image performs better when the intermediate region is supervised as an output than when it is left to attention. That is the multimodal instance of a pattern this archive records repeatedly — supervision on the intermediate object changes whether the model uses it, as with running-state supervision making a written scratchpad state causally readable where answer-only training leaves it inert. The curriculum result points the same way as the archive's latent-CoT work: composition order matters, and here foundational levels generalize upward while the hardest level alone does not generalize down. The opening measurement is also worth keeping as a diagnostic template — separating vision errors, reasoning errors and answer errors under four supervision modes shows the two supports are non-additive (18.33 and 10.00 separately, 43.33 together), which no single accuracy number would reveal.
- **test-time-scaling**: Its bearing here is mostly negative and worth stating as such. The method's benefit comes from training the grounding in, not from spending more inference: the explicit-versus-implicit contrast holds the inference budget fixed and changes only whether the intermediate region was a supervised output. And the reinforcement-learning variant, which buys the largest gain at 17.04 points combined with supervised finetuning, is set aside by the authors on cost grounds in favour of the cheaper route. For an archive tracking what extra inference-time computation buys, this is a case where the answer was to move the work into training instead.

## Entities

- **Concepts**: visual grounding, curriculum learning, [multimodal reasoning](../../../../wiki/concepts/multimodal-reasoning.md), [chain of thought](../../../../wiki/concepts/chain-of-thought.md), [reasoning depth](../../../../wiki/concepts/reasoning-depth.md), [compositional generalization](../../../../wiki/concepts/compositional-generalization.md), [process supervision](../../../../wiki/concepts/process-supervision.md), LLM-as-a-judge, synthetic data generation
- **Methods**: CURV, [chain-of-thought prompting](../../../../wiki/methods/chain-of-thought-prompting.md), [supervised fine-tuning](../../../../wiki/methods/supervised-fine-tuning.md), [reinforcement learning](../../../../wiki/methods/reinforcement-learning.md), intersection over union, [LLM-as-a-judge](../../../../wiki/methods/llm-as-a-judge.md)
- **Datasets**: CCQA, ChartQA, ChartQA-Pro, CharXiv, ChartMuseum, [MathVista](../../../../wiki/datasets/mathvista.md), [MMMU-Pro](../../../../wiki/datasets/mmmu-pro.md)

Tags: `chart understanding`, `visual grounding`, `curriculum learning`, `multimodal`, `process supervision`

## Abstract

Chart question answering (CQA) requires multimodal large language models (MLLMs) to integrate visual comprehension with logical reasoning, yet current models struggle with accurate visual grounding and coherent reasoning chains. While extrinsic chain-of-thought prompting and visual cues significantly improve performance, current MLLMs lack intrinsic visual grounded reasoning capabilities, leading to inaccurate perception and reasoning disconnected from visual evidence. To address these limitations, we propose CURV, a curriculum learning framework that develops intrinsic visual reasoning capabilities by reformulating CQA as multi-step visual grounded reasoning, where each step coordinates logical reasoning with dynamic visual grounding through spatial attention concentration. To assist model learning, we further introduce CCQA, a three-level curriculum dataset with scalable synthetic generation across diverse chart types and reasoning patterns. Our curriculum systematically progresses from basic single-operation reasoning to complex multi-chart compositional tasks. Experiments demonstrate that CURV achieves up to $\uparrow20.50\%$ improvements over baselines and is generalizable to real-world benchmarks (up to $\uparrow12.30\%$) and out-of-domain multimodal reasoning tasks (up to $\uparrow10.20\%$), validating the effectiveness of internalizing visual reasoning with dynamic grounding for enhanced chart understanding capabilities. Code is available at: https://xhguo7.github.io/CURV/.

---

Record id: `arxiv:2608.02833`
