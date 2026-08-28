<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Skill-Aware Data Selection and Fine-Tuning for Data-Efficient Reasoning Distillation

- **Authors**: Lechen Zhang, Yunxiang Zhang, Wei Hu, Lu Wang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-short.49/>
- **PDF**: <https://aclanthology.org/2026.acl-short.49.pdf>
- **DOI**: 10.18653/v1/2026.acl-short.49
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

A skill-centric distillation framework maps math problems onto a hierarchical skill tree, samples the 1,000 SFT training examples inversely proportional to the student model's per-skill accuracy (so it trains more on skills it is weak at), and prepends the required skill chain to each example, beating random-sampling SFT baselines by 1.6/1.4 points average accuracy on Qwen3-4B/8B across five math benchmarks with the same 1K-example budget.

## Problem

Distilling large reasoning models' capabilities into weaker LLMs via supervised fine-tuning typically requires large-scale data and treats all training examples equally, ignoring that a single problem draws on multiple underlying atomic skills and that models differ in which specific skills they are weak at, so training data selection is not adapted to the model's actual current strengths and weaknesses.

## Contributions

- a skill-tree-based attribution pipeline mapping math problems to multiple relevant skills via recursive top-down LLM prompting
- skill-based data sampling that weights training examples inversely by the student model's own per-skill accuracy, adapting the training distribution to the specific model's weaknesses rather than treating all examples equally
- skill-aware training that prepends the explicit skill chain required to solve each problem, teaching the model to traverse skill structure explicitly
- a demonstration that combining both techniques with only 1,000 training examples beats random-sampling SFT baselines and generalizes across skill taxonomies, model families, and against other strong data-selection baselines (LIMO, s1, Light-R1, Select2Reason)

## Method

A three-step pipeline: (1) Skill tree attribution -- each of 100K OpenMathReasoning QA pairs is mapped top-down onto a pre-defined hierarchical skill tree (from Instruct-SkillMix) by prompting Qwen2.5-32B-Instruct to recursively select the relevant skill at each level, O(log N) per example; (2) Skill-based sampling -- the student model's accuracy is measured per leaf skill on the corpus, and training examples are sampled with probability inversely proportional to (clipped) per-skill accuracy, so weaker skills are oversampled and well-mastered skills undersampled, constructing a 1,000-example training subset; (3) Skill-aware training -- each selected example is augmented by prepending its explicit ordered skill chain (e.g. 'Skills: Mathematics -> Probability -> Bayes' theorem') before the solution, so the model learns to traverse required skills explicitly before solving.

## Results

With only 1,000 training examples (from a 100K corpus), the full method (skill-based selection + skill-aware SFT) improves Avg@8 accuracy over random-sampling standard SFT by +1.6 points on Qwen3-4B (68.4% vs. 66.8% average across AMC23/AIME2024/AIME2025/MATH-L5/OlympiadBench) and +1.4 points on Qwen3-8B (69.5% vs. 68.1%). Skill-based data selection alone (with standard SFT) outperforms random sampling by +0.5 (Qwen3-4B, largest gain +2.4 on AIME2024) and +0.4 (Qwen3-8B, largest gain +3.2 on AMC23) average points; skill-aware training alone (with random selection) adds further consistent gains, with the largest boost on AIME2024 (up to +5.0) and strongest overall gains of +0.8 (Qwen3-4B) and +1.3 (Qwen3-8B) versus standard SFT. Notably, fine-tuning on the full 100K corpus underperforms the untrained base model, underscoring that data selection quality matters more than quantity for reasoning distillation. Per-skill accuracy analysis on MATH-500 shows skill-based sampling flattens the accuracy curve toward balanced mastery across skills (raising weak-skill accuracy while preserving already-strong skills), and skill-aware augmentation further improves this consistency. Ablations show a sampling-aggressiveness exponent of T=1.0 (inverse accuracy weighting) balances performance best (T too low or too high underperforms), and that using the full hierarchical skill chain in training outperforms using only root-level or only leaf-level skill labels, showing the complete hierarchy is beneficial, not just the most specific skill.

## Limitations

The approach relies on an existing, manually-constructed skill tree that may not perfectly align with the actual skill decomposition used internally by the student model. The accuracy-based sampling assumes per-skill evaluation accuracy reliably reflects model competence, but skill-wise accuracy can be noisy, especially for skills with limited evaluation data in the corpus. Only two model scales (4B and 8B) were evaluated; results are consistent across three model families in generalization experiments but further validation at larger scale is left to future work.

## Why it matters here

- **overthinking**: Not directly about overthinking: this paper targets data-efficient accuracy distillation (which training examples teach a weaker model the most, given its current skill gaps), not reasoning-trace length or the inference-time accuracy/efficiency tradeoff. It is tangential background on how the reasoning models this archive studies are trained, not a measurement or mitigation of overthinking itself.

## Entities

- **Concepts**: skill-centric distillation, hierarchical skill tree, skill-based (weakness-targeted) sampling, skill-aware training (explicit skill-chain prompting)
- **Methods**: skill-tree attribution, weakness-inverse-proportional sampling, skill-chain-augmented supervised fine-tuning
- **Datasets**: OpenMathReasoning (100K corpus), [AMC23](../../../../wiki/datasets/amc23.md), [AIME2024](../../../../wiki/datasets/aime-2024.md), [AIME2025](../../../../wiki/datasets/aime-2025.md), MATH (Level 5), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md), [MATH-500](../../../../wiki/datasets/math500.md)

Tags: `distillation`, `data-efficiency`, `supervised-fine-tuning`, `skill-taxonomy`, `math-reasoning`

## Abstract

Large reasoning models such as DeepSeek-R1 and their distilled variants achieve strong performance on complex reasoning tasks. Yet, distilling these models often demands large-scale data for supervised fine-tuning (SFT), motivating the pursuit of data-efficient training methods. To address this, we propose a skill-centric distillation framework that efficiently transfers reasoning ability to weaker models with two components: (1) Skill-based data selection, which prioritizes examples targeting the student model’s weaker skills, and (2) Skill-aware fine-tuning, which encourages explicit skill decomposition during problem solving. With only 1,000 training examples selected from a 100K teacher-generated corpus, our method surpasses random SFT baselines by +1.6% on Qwen3-4B and +1.4% on Qwen3-8B across five mathematical reasoning benchmarks. Further analysis confirms that these gains concentrate on skills emphasized during training, highlighting the effectiveness of skill-centric training for efficient reasoning distillation.

---

Record id: `doi:10.18653/v1/2026.acl-short.49`
