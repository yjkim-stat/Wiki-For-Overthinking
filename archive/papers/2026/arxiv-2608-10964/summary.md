<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# CARE: Confidence-Aware Reasoning for Reliable Medical VQA

- **Authors**: Yuetian Du, Yucheng Wang, Zhenyuan Chen, Luyuan Chen, Rongyu Zhang, Jinjian Zhang, Wei Zhou, Zhijie Xu, Ming Kong, Zhan Zhou, Jie Liu, Qiang Zhu
- **Venue**: cs.CV
- **Published**: 2026-08-11
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.10964>
- **PDF**: <https://arxiv.org/pdf/2608.10964v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.40, test-time-scaling 0.25

## In one line

Adds a correctness-conditioned confidence term to the GRPO reward for medical visual question answering -- rewarding answer-token confidence when the answer is right and penalising it when wrong -- on top of an SFT cold start built from answer-conditioned reasoning traces filtered by a verifier.

## Problem

Reinforcement fine-tuning gives medical multimodal models chain-of-thought traces and better accuracy, but leaves a systematic gap between expressed certainty and diagnostic correctness. Standard RFT rewards are binary format and accuracy terms, which say nothing about how confidently a wrong answer was given, and in a clinical setting the miscalibration is what undermines the model's usability rather than the error rate alone.

## Contributions

- A correctness-conditioned calibration term inside the GRPO reward: answer-span confidence is added when the answer is correct and subtracted, scaled by lambda, when it is not.
- An answer-conditioned trace synthesis pipeline with a verifier admitting only trajectories whose chain deduces the ground-truth conclusion, avoiding expert annotation.
- Simultaneous best accuracy, ECE and hallucination rate on three medical VQA benchmarks against six reasoning-focused medical multimodal baselines, none of which leads on all three.
- A stage ablation separating closed-ended from open-ended questions, showing RL alone is best on the former and SFT+RL on the latter.

## Method

Two phases. Reasoning traces are synthesised in reverse: a capable multimodal model is shown the image, the question and the ground-truth diagnosis, and asked to produce an intermediate trajectory under a strict template with named phases (visual analysis, differential diagnosis, conclusion). A verifier -- GPT-4o -- admits a trajectory only if its chain logically deduces the ground-truth conclusion, which the authors describe as an objective proxy for quality assurance. SFT on the surviving corpus gives the reference policy. Then GRPO with K=4 rollouts and a composite reward of three parts: a binary format reward for the think and answer delimiters, an output reward that is exact match for closed-ended questions and recall-based coverage for open-ended ones, and the calibration term. Confidence is the mean token probability over the answer span only, excluding reasoning tokens, formatting and special tokens. The calibration reward is that confidence times the output reward, minus lambda times the confidence when the output reward is zero -- so being confident is rewarded exactly in proportion to being right and penalised in proportion to being wrong. lambda is 0.5. The same Qwen2.5-VL-7B-Instruct architecture is both the trace synthesiser and the policy.

## Results

Three medical VQA benchmarks. CARE-7B reports the best accuracy, lowest expected calibration error and lowest hallucination rate on all three simultaneously: VQA-RAD 0.767 / 0.202 / 0.048, SLAKE 0.873 / 0.115 / 0.070, PathVQA 0.689 / 0.290 / 0.059. The strongest baselines each win only one axis -- Lingshu-7B has 0.831 accuracy on SLAKE with 0.322 ECE, Fleming-VL-8B has the best baseline ECE on SLAKE at 0.181 with lower accuracy, and MedVLThinker-7B leads PathVQA accuracy at 0.652 with the worst-but-one ECE at 0.569. The SLAKE ECE is a 36 percent relative improvement over the best baseline. The stage ablation is the most informative table and it complicates the headline: RL alone, with no SFT cold start, is the best configuration on closed-ended questions on all three benchmarks and by wide margins -- VQA-RAD closed 0.864 against SFT+RL's 0.658, PathVQA closed 0.955 against 0.863, SLAKE closed 0.861 against 0.779 -- with correspondingly better closed-ended ECE (0.096, 0.020, 0.119). SFT+RL wins the open-ended splits (SLAKE open 0.881, PathVQA open 0.421, VQA-RAD open 0.620), where SFT alone already supplies most of the gain (SLAKE open rises from 0.513 training-free to 0.803 with SFT alone). So the deployed pipeline is the better configuration for free-form answers and the worse one for constrained ones, and the paper's per-benchmark headline numbers aggregate over both. Hallucination is judged by Lingshu-32B under a fixed rubric with deterministic decoding, with a quadratic penalty that deliberately over-weights heavily hallucinated samples. Confidence histograms shift rightward after training, which the authors are careful to say is only meaningful read together with the falling ECE.

## Limitations

The paper has no limitations section and its evaluation has a structural problem the text does not address: the calibration reward optimises mean answer-token probability, and ECE is computed from confidence scores binned the same way, so the training objective and the headline calibration metric are functions of the same quantity. A lower ECE under those conditions is partly a check that optimisation succeeded rather than independent evidence of calibration; nothing here tests the confidence against a held-out proper scoring rule, against sampled agreement, or against clinician judgement. Second, the ablation shows the full pipeline is not the best configuration for closed-ended questions on any benchmark, which is not reconciled with the main table. Third, the reasoning traces are generated with the answer in hand and admitted only when they reach that answer, so the corpus is selected for post-hoc rationalisations that happen to land correctly; the hallucination reduction the authors attribute to 'answer-grounded reasoning paths' is equally consistent with traces that were filtered for agreeing with the label. Fourth, the hallucination metric is a single VLM judge with a hand-chosen quadratic penalty and a global normalisation constant, reported without agreement against human labels or a second judge. Fifth, single runs, no seeds, no intervals, and the verifier is a proprietary model.

## Why it matters here

- **reasoning-training**: The interesting content is in what the reward asks for and what the evaluation can then show. Making the reward proportional to confidence when correct and to minus confidence when wrong is a clean way to put calibration into a group-relative objective, and it is the same move the archive's selective-prediction entries describe from the abstention side -- score the pair, not the accuracy. But the metric it is scored against, expected calibration error, is computed from the same answer-token probability the reward optimises, so this paper is an instance of the circularity the archive keeps flagging: a training signal and its evaluation must be different measurements, or the result only says the optimiser worked. Two secondary observations transfer. The stage ablation shows RL without a cold start beating SFT+RL on every closed-ended split by 8 to 20 points while losing every open-ended one, so the value of a reasoning cold start depends on whether the answer space is constrained -- and a single aggregate accuracy would have hidden it. And the trace corpus is generated backwards from the label and admitted only when it reaches that label, which makes the resulting 'reasoning' a filtered rationalisation; the archive now holds two papers this month training on backwards-constructed traces and reporting downstream gains, which is worth watching separately from any faithfulness claim.

## Entities

- **Concepts**: [confidence calibration](../../../../wiki/concepts/confidence-calibration.md), [expected calibration error](../../../../wiki/concepts/expected-calibration-error.md), [selective prediction](../../../../wiki/concepts/selective-prediction.md), [hallucination](../../../../wiki/concepts/hallucination.md), reward shaping, [rationalization](../../../../wiki/concepts/post-hoc-rationalization.md), LLM-as-a-judge, [verifiable reward](../../../../wiki/concepts/verifiable-reward.md)
- **Methods**: CARE, Confidence-Aware Reward, [GRPO](../../../../wiki/methods/grpo.md), [supervised fine-tuning](../../../../wiki/methods/supervised-fine-tuning.md), reinforcement fine-tuning, [chain-of-thought prompting](../../../../wiki/methods/chain-of-thought-prompting.md), [rejection sampling](../../../../wiki/methods/rejection-sampling.md)
- **Datasets**: [VQA-RAD](../../../../wiki/datasets/vqa-rad.md), SLAKE, [PathVQA](../../../../wiki/datasets/pathvqa.md)

Tags: `calibration`, `medical-vqa`, `grpo`, `reward-design`, `hallucination`

## Abstract

Reinforcement Fine-Tuning (RFT) has enabled medical Multimodal Large Language Models (MLLMs) to produce Chain-of-Thought (CoT) reasoning for visual question answering, yet these models suffer from $\textit{confidence miscalibration}$---a systematic gap between expressed certainty and actual diagnostic accuracy that undermines clinical trust. We propose $\textbf{CARE}$, a $\textbf{C}$onfidence-$\textbf{A}$ware medical $\textbf{RE}$asoning framework that jointly optimizes accuracy and calibration through a dual-stage pipeline. First, a scalable Medical-CoT synthesis provides structured cold-start data for Supervised Fine-Tuning. Second, Group Relative Policy Optimization (GRPO) with a novel $\textbf{Confidence-Aware Reward (CAR)}$ mechanism ties the model's confidence to diagnostic correctness within the reward signal. Across three Medical VQA benchmarks, $\textbf{CARE}$ achieves the highest diagnostic accuracy while obtaining the lowest Expected Calibration Error and Hallucination Rate, establishing a foundation for trustworthy clinical decision support. Our code is available at https://github.com/anotherbricki/CARE.

---

Record id: `arxiv:2608.10964`
