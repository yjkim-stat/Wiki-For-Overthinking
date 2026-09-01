<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# A Reward-Guided Dual-Phase Framework for Adaptive Inference-Time Reasoning

- **Authors**: Yingqian Cui, Zhenwei Dai, Pengfei He, Bing He, Hui Liu, Zhan Shi, Xianfeng Tang, Jingying Zeng, Suhang Wang, Yue Xing, Jiliang Tang, Benoit Dumoulin
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.511/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.511.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.511
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## In one line

DREAM decomposes tree-based test-time search into separate planning and execution phases, each with its own reward model and adaptive per-step budget allocation, improving the accuracy-tokens tradeoff over standard beam search and majority voting on math reasoning and code generation.

## Problem

Existing PRM-guided tree-based test-time-scaling methods treat each reasoning step's plan and execution as a single unit scored together, and allocate a fixed sampling budget to every step regardless of difficulty -- but planning and execution have measurably different behavior (planning is more uncertain/harder, execution errors are more fatal because they propagate to later steps), and step difficulty varies across problems and datasets, so uniform coupled treatment wastes computation.

## Contributions

- an empirical demonstration that planning and execution steps in multi-step reasoning have measurably different confidence and error-propagation behavior, motivating separate treatment
- DREAM, a dual-phase tree-search framework with dedicated plan and execution reward models searched independently at each step
- a dynamic, per-step budget allocation mechanism that early-stops on confident steps and reallocates budget to harder ones, with a demonstrated synergistic effect when combined with dual-phase search

## Method

Confirms via perplexity and reward-model measurements on GSM8K that planning steps have much higher perplexity (mean 5.46 vs 1.26) and lower reward (mean 0.804 vs 0.768, but the deeper finding is that execution errors propagate downstream) than execution steps, motivating DREAM (Dual-phase REward-guided Adaptive reasoning framework at test tiMe): at each reasoning step, N1 planning candidates are sampled and scored by a dedicated plan reward model (PRM_plan), the top n1 selected; conditioned on those, N2 execution candidates are sampled and scored by an execution reward model (PRM_exec), with the top n2 retained for the next step. A dynamic budget allocation extension (DREAM+) adds a two-threshold early-stopping/extra-sampling rule per phase: stop sampling early once enough high-reward candidates are found (saving budget on easy steps), or sample additional candidates when none clear a lower threshold (spending more budget on hard steps). Reward models are trained via rollout-based labeling (5 independent continuations per step; a step is + if at least one rollout reaches the correct final answer) on ~400K synthetic trajectories each for GSM8K and MATH, fine-tuning Qwen2.5-32B-Instruct.

## Results

On GSM8K and MATH across three reasoning models (Qwen2.5-MATH-1.5B-Instruct, DeepSeekMath-7B-Instruct, LLaMA-3/3.1-8B-Instruct), all tree-based search methods beat majority voting by up to 20 percentage points on MATH with LLaMA-3.1-8B-Instruct; DREAM outperforms standard beam search (which does not separate plan/execution) with the gap widening as token budget increases. DREAM+ (with dynamic budget allocation) adds roughly a further 2% accuracy at comparable token budgets on GSM8K with LLaMA-3-8B-Instruct over DREAM alone, with a documented synergistic effect between dual-phase search and adaptive allocation (the combination outperforms either alone, more so than either component in isolation). On out-of-distribution benchmarks (AMC23, ASDiv) not used for reward-model training, DREAM(+) still beats majority vote by up to 30% on AMC23, indicating the reward model generalizes rather than overfitting to its training backbone. A reward-model-size ablation shows a 32B reward model consistently outperforms a 7B version, though the 7B model still substantially beats majority voting. FLOP accounting confirms token-count trends hold under FLOPs too: reward-model scoring (FLOP-rew) stays under 1/10 of generation FLOPs (FLOP-gen) since it only needs a single forward pass per candidate, not autoregressive decoding.

## Limitations

The approach relies on relatively large, separately-trained reward models; increasing reward/reasoning model size improves guidance quality but adds computation and memory cost. In GSM8K, around 80% of reasoning steps trigger the early-stopping branch of adaptive budget allocation, but in MATH only around 5% do (because MATH problems are more uniformly hard), so the adaptive mechanism's benefit is dataset-dependent and marginal when every step in a trajectory is uniformly hard.

## Why it matters here

- **overthinking**: Directly relevant to efficient allocation of test-time compute: rather than spending a fixed search budget uniformly across every reasoning step, DREAM identifies where reasoning is actually uncertain (planning) versus where errors are costly (execution) and moves budget accordingly, with an early-stopping mechanism that explicitly avoids wasted computation on easy steps -- the same 'don't spend more than the step needs' principle that motivates length-aware and budget-aware overthinking mitigations, applied at the sub-step granularity of a search tree rather than to overall trace length.

## Entities

- **Concepts**: dual-phase search (plan/execution separation), adaptive/dynamic budget allocation, [Process Reward Model (PRM)](../../../../wiki/concepts/process-reward-model-prm.md), rollout-based reward labeling
- **Methods**: DREAM (dual-phase reward-guided search), dynamic budget allocation, standard beam search (baseline), REBASE (baseline), majority vote (baseline)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), MATH (MATH500), [AMC23](../../../../wiki/datasets/amc23.md), [ASDiv](../../../../wiki/datasets/asdiv.md)

Tags: `test-time-scaling`, `tree-search`, `process-reward-model`, `adaptive-computation`, `reasoning`

## Abstract

Large Language Models (LLMs) have made strong progress in reasoning. To enhance the reasoning performance, a common inference-time approach is tree-based search, which decomposes the reasoning process into multiple steps, expands multiple reasoning paths, and uses reward models to prune and select candidates. However, based on our exploration, the simple decomposition may lead to suboptimal searching efficiency: while planning is generally harder, it is the execution errors that are more likely to propagate to later steps. This indicates that planning and execution play different roles in reasoning and should be treated differently during tree-based search. Given this, to enhance the searching efficiency, we propose a dual-phase test-time scaling framework that separates reasoning into planning and execution, and performs search over each phase independently. To further refine the algorithm, we also introduce a dynamic budget allocation mechanism that adaptively redistributes sampling effort based on reward feedback, allowing early stopping on confident steps and reallocation of computation to more challenging steps. Experiments on both math reasoning and code generation benchmarks demonstrate that our approach consistently improves accuracy while reducing redundant computation.

---

Record id: `doi:10.18653/v1/2026.findings-acl.511`
