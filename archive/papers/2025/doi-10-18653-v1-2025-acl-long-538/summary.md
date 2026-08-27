<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ARise: Towards Knowledge-Augmented Reasoning via Risk-Adaptive Search

- **Authors**: Yize Zhang, Tianshu Wang, Sirui Chen, Kun Wang, Xingyu Zeng, Hongyu Lin, Xianpei Han, Le Sun, Chaochao Lu
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2025.acl-long.538/>
- **PDF**: <https://aclanthology.org/2025.acl-long.538.pdf>
- **DOI**: 10.18653/v1/2025.acl-long.538
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## In one line

ARISE combines Monte Carlo Tree Search with a Bayesian Risk-Value function -- estimating each reasoning-state node's risk from the policy model's own likelihood of regenerating the original question given that state -- to guide retrieval-augmented multi-hop reasoning, outperforming SOTA knowledge-augmented-reasoning baselines by up to 23.10% and RAG-equipped DeepSeek-R1-distilled LRMs by up to 25.37%, while making explicit that its search-based gains come at substantially higher inference-time cost.

## Problem

Knowledge-augmented reasoning (KAR) methods for open-ended, knowledge-intensive multi-hop QA suffer from two unaddressed problems: error propagation, where a mistake in an early reasoning step cascades uncorrected through the rest of a linear chain, and a verification bottleneck, where balancing exploration versus exploitation across multiple candidate reasoning branches is hampered by unreliable self-verification or the need for specifically-trained verifiers.

## Contributions

- ARISE, a framework combining decomposition-then-retrieval reasoning-state generation with Monte Carlo Tree Search to mitigate error propagation in knowledge-augmented reasoning
- a Bayesian Risk-Value function that scores reasoning-state nodes via the policy model's own likelihood of regenerating the original question, avoiding both error-prone LLM self-verification and the need for a separately-trained verifier
- empirical results showing ARISE outperforms SOTA knowledge-augmented-reasoning methods by up to 23.10% and RAG-equipped DeepSeek-R1-distilled LRMs by up to 25.37%, with gains growing with task difficulty and with policy-model scale, alongside an explicit characterization of the resulting computational-overhead trade-off

## Method

ARISE has three components. (1) Reasoning State Generation: at each step, the policy model decomposes the problem into a sub-question, retrieves supporting documents (via BM25), and reasons over them to produce an intermediate result, which is appended to the growing reasoning state. (2) Monte Carlo Tree Search treats each step as a tree node and runs the standard select (UCT)/expand/simulate/backpropagate loop, allowing exploration of multiple reasoning branches and backtracking rather than following one linear chain. (3) Risk Assessment defines a node's value via a Bayesian Risk-Value function: rather than training a separate verifier or relying on error-prone LLM self-verification, it estimates how well a candidate intermediate result r explains the original question q by computing the policy model's own average log-likelihood of generating the tokens of q conditioned on the reasoning state so far including r (i.e. treating 'would this reasoning state make the model regenerate the original question' as a proxy for reasoning quality), then maps this risk through a sigmoid to a bounded node value in (0,1) used to seed and update UCT search. Evaluated on 200-question subsets of HotpotQA, 2WikiMultihopQA and MusiQue with Qwen2.5-14B/7B-Instruct and Llama3.1-8B-Instruct as policy models, against prompt-based (Query2Doc, Self-Ask, Verify-and-Edit, Auto-RAG) and search-based (Self-Consistency/CoT-SC, RATT) RAG baselines, and separately against DeepSeek-R1-distilled learning-based LRMs equipped with RAG.

## Results

ARISE outperforms all baselines across all three benchmarks on Qwen2.5-14B-Instruct, with average absolute EM improvements of 19.83% over vanilla RAG, 13.29% over prompt-based baselines, and 15.5% over search-based baselines; it maintains an average 13.67% EM improvement over vanilla RAG on Qwen2.5-7B-Instruct. Relative gains grow with task difficulty: on the 14B model, ARISE's relative EM improvement over vanilla RAG is 23.53% on HotpotQA (easiest), 52.70% on 2WikiMultihopQA, and 179.31% on MusiQue (hardest), versus much smaller average improvements (5.74%/11.94%/66.09% respectively) for the strongest competing baselines. ARISE underperforms slightly on Llama3.1-8B relative to some continuous-reasoning methods (CoT, ToT), a pattern also seen for the similarly-structured Auto-RAG baseline, suggesting Llama is less suited to the iterative decomposition-and-retrieval paradigm this class of methods uses -- though ARISE still retains a notable F1 advantage on Llama over other KAR methods. Compared to RAG-equipped DeepSeek-R1-distilled LRMs, ARISE (search-based) shows an average 4.03% relative improvement, and the paper concludes learning-based LRMs have not yet matched search-based reasoning's effectiveness for this task class. Scaling the policy model from 0.5B to 32B parameters (Qwen2.5 series) shows ARISE's Pass@N upper bound and Pass@1 (optimal-path) both improve with scale while the Pass@1-to-Pass@N gap shrinks from 25.00% to 7.25%, meaning ARISE increasingly approaches its own theoretical ceiling as models get larger, whereas vanilla RAG shows diminishing returns beyond 7B. Ablating the Risk-Value function against vanilla MCTS (uniform node values) and an LLM-as-verifier variant shows Risk-Value gives a 10.71% average relative improvement over vanilla MCTS (up to 17.39% on MusiQue) and clearly outperforms LLM-as-verifier, which the paper attributes to pretrained LLMs being poorly calibrated as standalone verifiers for guiding search. A search-space (depth x width) sweep shows performance improves with more exploration but with sharply diminishing returns and rapidly escalating reasoning time (e.g. depth 3->4 and width 4->6 raises reasoning time from 52 to 266 minutes for marginal score gain), motivating a depth=4/width=5 configuration as a practical trade-off. Direct overhead comparison on MusiQue/Qwen2.5-14B shows ARISE takes 160 minutes versus 10 (vanilla) to 155 (RATT, the next most expensive baseline) for the best accuracy achieved by any method tested.

## Limitations

Experiments are confined to multi-hop QA tasks; applicability to mathematical problem-solving, code generation, or complex decision-making is unexplored and left to future work. Prompts were not systematically designed for generalization/robustness across diverse scenarios. The Risk-Value function, while avoiding a separately-trained verifier, is itself a proxy (regeneration likelihood of the original question) rather than a directly-learned, generalizable reward, and the paper explicitly frames a generalizable reward design as important future work, contrasting with static post-trained reward models that struggle on open-ended, knowledge-intensive tasks where new knowledge is dynamically involved. The MCTS search space (depth and width) is predefined and fixed rather than adaptively determined based on per-question reasoning complexity or knowledge density, which the authors identify as an open challenge for achieving an effective broad-vs-deep search trade-off and reducing redundancy in the reasoning process.

## Why it matters here

- **overthinking**: Relevant as a test-time-scaling method whose own reported results directly quantify the accuracy-cost trade-off central to overthinking: its search-space sweep shows performance gains diminish sharply while reasoning time grows nearly 5x for a small further depth/width increase, and its head-to-head overhead table shows ARISE takes 16x longer than vanilla RAG for its accuracy gain -- explicit, measured evidence of the point at which added test-time search stops paying for itself. Its finding that gains grow with task difficulty (larger relative improvement on harder benchmarks) also supports the overthinking-adjacent principle that more test-time compute should be allocated where the problem actually needs it, rather than uniformly.

## Entities

- **Concepts**: error propagation (in linear KAR chains), verification bottleneck (explore-exploit trade-off in multi-branch reasoning), Bayesian Risk-Value function (regeneration-likelihood-based node scoring), risk-adaptive Monte Carlo Tree Search
- **Methods**: [Monte Carlo Tree Search (MCTS)](../../../../wiki/methods/monte-carlo-tree-search-mcts.md), Bayesian Risk-Value function, retrieval-augmented generation (BM25), Query2Doc / Self-Ask / Verify-and-Edit / Auto-RAG (prompt-based baselines), Self-Consistency / RATT (search-based baselines)
- **Datasets**: [HotpotQA](../../../../wiki/datasets/hotpotqa.md), 2WikiMultihopQA, [MusiQue](../../../../wiki/datasets/musique.md)

Tags: `test-time-scaling`, `monte-carlo-tree-search`, `retrieval-augmented-generation`, `multi-hop-reasoning`, `risk-adaptive-search`

## Abstract

Large language models (LLMs) have demonstrated impressive capabilities and are receiving increasing attention to enhance their reasoning through scaling test-time compute. However, their application in open-ended, knowledge-intensive, complex reasoning scenarios is still limited. Reasoning-oriented methods struggle to generalize to open-ended scenarios due to implicit assumptions of complete world knowledge. Meanwhile, knowledge-augmented reasoning (KAR) methods fails to address two core challenges: 1) error propagation, where errors in early steps cascade through the chain, and 2) verification bottleneck, where the explore–exploit trade-off arises in multi-branch decision processes. To overcome these limitations, we introduce ARise, a novel framework that integrates risk assessment of intermediate reasoning states with dynamic retrieval-augmented generation (RAG) within a Monte Carlo tree search paradigm. This approach enables effective construction and optimization of reasoning plans across multiple maintained hypothesis branches. Experimental results show that ARise significantly outperforms the state-of-the-art KAR methods by up to 23.10%, and the latest RAG-equipped large reasoning models by up to 25.37%. Our project page is at https://opencausalab.github.io/ARise.

---

Record id: `doi:10.18653/v1/2025.acl-long.538`
