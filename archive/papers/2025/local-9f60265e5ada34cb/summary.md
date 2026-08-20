<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# The Danger of Overthinking: Examining the Reasoning-Action Dilemma in Agentic Tasks

- **Authors**: Alejandro Cuadron, Dacheng Li, Wenjie Ma, Xingyao Wang, Yichuan Wang, Siyuan Zhuang, Shu Liu, Luis Gaspar Schroeder, Tian Xia, Huanzhi Mao, Nicholas Thumiger, Aditya Desai, Ion Stoica, Ana Klimovic, Graham Neubig, Joseph E. Gonzalez
- **Venue**: International Conference on Machine Learning (ICML) 2025
- **Published**: 2025-01-01
- **Source**: local
- **Topics**: overthinking
- **Relevance score**: overthinking 0.67

## In one line

Defines and measures 'overthinking' in Large Reasoning Models on real software-engineering agent tasks, showing that favoring internal reasoning over environment interaction correlates with lower SWE-bench issue-resolution rates and can be mitigated at lower cost.

## Problem

In agentic settings a model must repeatedly choose between acting on the environment (execute, observe feedback) and reasoning internally about hypothetical outcomes before acting — a tension the authors call the Reasoning-Action Dilemma. Prior evaluation of Large Reasoning Models has mostly used static, non-interactive benchmarks (AIME, MMLU, GPQA), so it was unclear whether their extended chain-of-thought reasoning helps or hurts when a model must gather and act on real, evolving environmental feedback rather than a fixed problem statement.

## Contributions

- Defines and names 'overthinking' — an LRM's tendency to favor internal reasoning simulation over environment interaction in agentic tasks — and formalizes the underlying 'Reasoning-Action Dilemma'.
- Builds and validates an LLM-as-a-judge framework (Claude 3.5 Sonnet) that scores agent trajectories 0-10 for overthinking based on three concrete patterns — Analysis Paralysis, Rogue Actions, Premature Disengagement — correlating rho=0.80 with human expert scores on a 20-trace sample.
- Analyzes 3,908 trajectories (4,018 total including pilot) across 19 models on SWE-bench Verified, showing overthinking negatively correlates with issue-resolution rate and that reasoning models overthink about 3x more than non-reasoning models.
- Shows a practical, cheap mitigation: sampling multiple low-reasoning-effort solutions and selecting the one with the lowest overthinking score improves resolution rate (up to 30.3% at k=3, surpassing the high-reasoning baseline) while cutting inference cost by up to 43%.
- Shows native function-calling support reduces overthinking and improves performance more than the tested reinforcement-learning-based training alone (o1 resolution 29.1% to 47.7% with function calling enabled).
- Open-sources the evaluation framework and the full trajectory dataset with overthinking scores and judge rationale.

## Method

The authors build an LLM-as-a-judge scoring framework (evaluator: Claude 3.5 Sonnet, temperature 0) that reads a full agent trajectory and assigns an 'overthinking score' from 0 (always interacting with the environment) to 10 (complete detachment from environmental feedback), grounded in three defined failure patterns: Analysis Paralysis (excessive planning with little execution), Rogue Actions (issuing multiple dependent actions without waiting for feedback between them), and Premature Disengagement (ending the task based on internal simulation rather than confirmed outcomes). The judge prompt and worked examples are given in Appendix A, and the scorer is validated against 4 human expert annotators on 20 sampled traces (Spearman rho = 0.80, Figure 5). They deploy 19 models (reasoning and non-reasoning, proprietary and open-weight, 1.5B–671B parameters, with/without native function calling) as CodeAct agents inside the OpenHands framework, tasked with resolving real GitHub issues from SWE-bench Verified, and analyze 3,908 generated trajectories (4,018 including earlier pilot analysis). They then regress overthinking score against issue-resolution rate, compare scores across model type, model size, reasoning-effort setting and context-window size, and test two mitigations: (1) sampling k solutions at low reasoning effort and selecting the one with the lowest overthinking score ('Lowest Overthinking@k'), and (2) enabling native function calling versus prompt-based tool use.

## Results

Overthinking score negatively predicts issue resolution for both reasoning models (β1=-7.894, R²=0.892, p=0.000) and non-reasoning models (β1=-15.938, R²=0.839, p=0.010) (Table 1). Reasoning models average an overthinking score of 3.505±1.774 versus 2.228±0.751 for non-reasoning models (Table 2) — roughly 3x higher. Within matched model families, overthinking rises as model size shrinks (DS-R1 family 6.700±1.656 vs Qwen2.5 family 5.001±1.732 averaged over 7B/14B/32B, Table 3; Figure 6), and the reasoning-vs-non-reasoning gap narrows at smaller scale. o1 run at low reasoning effort scores 35% higher on overthinking than o1 at high effort (2.774±3.081 vs 2.426±2.880, Table 4). No significant correlation was found between context window size and overthinking score when architecture/size are held fixed (e.g. Qwen2.5-32B vs QwQ-32B, both 32K context: 2.31±0.42 vs 2.28±0.39, p>0.05). Practically: o1 at high reasoning effort reaches 29.1% issue resolution at $1,400 total cost; low effort reaches 21.0% at $400 (3.5x cheaper). Generating two low-effort solutions ($800) and picking the one with the lowest overthinking score reaches 27.3% resolution (43% lower cost than the high-effort baseline, Figure 3); with three samples ($1,200) it reaches 30.3%, surpassing the high-effort baseline while still costing $200 less. Adding native function calling to o1 raises resolution from 29.1% to 47.7% while cutting average overthinking score from 2.43 to 1.05; the same FC-vs-non-FC comparison on the BCFL multi-turn benchmark shows a smaller gain (36% to 41%), suggesting function calling alone does not fully explain the larger effect seen on SWE-bench. DeepSeek-R1-671B shows overthinking scores comparable to non-reasoning DeepSeek-V3-671B, which the authors attribute to R1's training not including extensive reinforcement learning specifically for software-engineering tasks.

## Limitations

The paper has no dedicated limitations section, but several are stated in-text: o1's reasoning tokens are hidden by OpenAI, so its overthinking score is derived only from observable actions rather than the actual internal reasoning chain, unlike other models. The overthinking scorer is an LLM judge (Claude 3.5 Sonnet) validated against only 20 human-scored traces from 4 experts, a small validation set. The context-window analysis compares only two models at one matched context size (32K), and the authors explicitly note 'further investigation is needed to confirm the underlying cause' for the model-size finding (Section 5.3). Only a single-agent CodeAct scaffold was tested; multi-agent scaffolds, which the authors note can behave structurally differently, were excluded by design. All empirical results are limited to software-engineering agentic tasks on SWE-bench Verified; the authors list generalization to other domains and environments with different interaction costs as open questions for future work (Section 6.3).

## Why it matters here

- **overthinking**: The paper's central subject is overthinking itself: it coins the term for LRMs favoring internal reasoning chains over environmental feedback in agentic tasks, builds a validated scorer for it, and directly measures the accuracy/efficiency tradeoff — higher overthinking scores predict lower SWE-bench resolution rates, and reducing overthinking (via lowest-overthinking-score selection or native function calling) improves both accuracy and cost.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), Reasoning-Action Dilemma, Analysis Paralysis, Rogue Actions, Premature Disengagement, [test-time compute scaling](../../../../wiki/concepts/test-time-compute-scaling.md), reasoning effort
- **Methods**: CodeAct agent scaffolding, OpenHands framework, LLM-as-a-judge (Claude 3.5 Sonnet), native function calling, Pass@k, Lowest Overthinking@k
- **Datasets**: [SWE-bench Verified](../../../../wiki/datasets/swe-bench-verified.md)

Tags: `overthinking`, `reasoning-action-dilemma`, `agentic-tasks`, `swe-bench`, `llm-as-judge`, `large-reasoning-models`, `function-calling`, `software-engineering-agents`

## Abstract

Large Reasoning Models (LRMs) represent a breakthrough in AI problem-solving capabilities, but their effectiveness in interactive environments can be limited. This paper introduces and analyzes overthinking in LRMs—a phenomenon where models favor extended internal reasoning chains over environmental interaction. Through experiments on software engineering tasks using SWE Bench Verified, we observe three recurring patterns: Analysis Paralysis, Rogue Actions, and Premature Disengagement. We propose a framework to study these behaviors, which correlates with human expert assessments, and analyze 4018 trajectories. We observe that higher overthinking scores correlate with decreased performance, with reasoning models exhibiting stronger tendencies toward overthinking compared to non-reasoning models. Our analysis reveals that simple efforts to mitigate overthinking in agentic environments—such as selecting the solution with the lower overthinking score—can improve model performance by almost 30% while reducing computational costs by 43%. These results suggest that mitigating overthinking has strong practical implications. We suggest that by leveraging native function-calling capabilities and selective reinforcement learning overthinking tendencies could be mitigated. We also open-source our evaluation framework and dataset to facilitate research in this direction at https://github.com/AlexCuadron/Overthinking.

---

Record id: `local:9f60265e5ada34cb`
