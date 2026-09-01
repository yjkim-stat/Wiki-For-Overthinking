<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Test-Time Scaling in Multimodal Foundation Models: A Comprehensive Survey of Generation and Reasoning

- **Authors**: Cong Wan, Ying He, Zhongzhan Huang, Hefeng Wu
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.383/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.383.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.383
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

The first systematic survey of test-time scaling (TTS) for multimodal foundation models proposes a unified three-way taxonomy -- sampling-based (Best-of-N, majority voting), feedback-based (reward models, iterative refinement), and search-based (beam search, tree search/MCTS, heuristic/adaptive search) -- spanning both multimodal generation (image/video) and multimodal reasoning, arguing multimodal TTS is fundamentally harder than text-only TTS because it must scale compute across perceptual evidence, spatial grounding, and temporal context simultaneously, not just unimodal reasoning depth.

## Problem

Test-time scaling (dynamically allocating extra inference-time compute via sampling, search, or verification rather than additional pretraining) has proven effective for LLM reasoning, and the research community is rapidly adapting similar strategies to multimodal foundation models (MFMs, spanning multimodal large language models and diffusion-based generation models), but no systematic survey or unified theoretical framework yet exists to delineate this rapidly-evolving landscape, and multimodal TTS is fundamentally more challenging than its text-only counterpart because MFMs must simultaneously scale compute across perceptual evidence, spatial grounding, and temporal context, with intermediate-step evaluation requiring strict cross-modal faithfulness to visual and spatial relations rather than mere textual consistency.

## Contributions

- the first comprehensive, systematic survey dedicated to test-time scaling in multimodal foundation models, covering both multimodal generation and multimodal reasoning
- a unified taxonomic framework categorizing existing multimodal TTS methodologies into three paradigms (sampling-based, feedback-based, search-based) with sub-taxonomies for each
- a comparative analysis of the three paradigms' applicability and trade-offs (parallelizability, latency, computational overhead) across generation and reasoning task types
- a review of representative applications, benchmarks, and open challenges, offering a strategic roadmap for future research on multimodal TTS

## Method

Formalizes TTS as selecting an inference procedure pi that queries a fixed-parameter model to maximize expected output utility subject to a test-time compute budget constraint, explicitly scoping the survey to compute-centric inference (as distinct from test-time memory augmentation or test-time weight adaptation). Surveys and taxonomizes existing multimodal TTS methods into three paradigms: (1) Sampling-based methods, which generate multiple candidate solutions in parallel and select/aggregate via Best-of-N (using a scoring function or an MLLM-as-judge, e.g. CLIP-score selection in diffusion trajectories, tournament-style VLM scoring, KL-divergence-based VLA action filtering) or Majority Voting (selecting the most frequent/consistent candidate, extended to character-level path clustering or multi-frame video consistency voting); (2) Feedback-based methods, relying on auxiliary evaluation signals -- Reward Models, split into Output Reward Models (ORMs, scoring final candidates, often paired with BoN) and Process Reward Models (PRMs, scoring intermediate steps to guide exploration strategies like beam/tree search) -- and Iterative Refinement, an explicit generate-evaluate-correct loop (e.g. reflection-guided diffusion-transformer refinement, multi-agent collaborative feedback, dynamic zooming for GUI grounding); (3) Search-based methods, enabling planning-based exploration via Beam Search (maintaining/pruning multiple candidate paths, sometimes with backtracking or world-model-guided valuation), Tree Search (recursively branching/backtracking, including Monte Carlo Tree Search variants using internal self-rewards, external retrieval, or collective multi-model learning), and Heuristic and Adaptive Search (evolutionary/gradient-free black-box search over latent spaces, adaptive termination based on confidence/consistency criteria, sparse-to-dense frame incorporation, coarse-to-fine reward-guided resampling). Comparatively analyzes the three paradigms' trade-offs: sampling-based methods are easy to parallelize but show diminishing returns as candidate count grows; feedback-based methods improve alignment/reliability more directly but introduce sequential latency dependent on the verifier/judge model; search-based methods incur the highest computational overhead (repeated branching, evaluation, rollback) but are most effective when accuracy is prioritized and process supervision is available, especially for long-chain multimodal reasoning. Reviews representative applications in two domains: Multimodal Generation (image generation, dominated by sampling-based BoN plus iterative prompt/conditioning-signal refinement, since visual generation is mainly judged by final output quality rather than explicitly verifiable intermediate states; video generation, favoring search-based methods for temporal consistency and motion smoothness) and Multimodal Reasoning (video reasoning, relying on search-based retrieval of query-relevant segments or iterative extraction/judging of key visual evidence to filter redundant information).

## Results

As a survey rather than an empirical study, its main contributions are organizational: it compiles and taxonomizes dozens of representative works (2024 Q4 through 2025 Q4, showing a rapid growth trend in publication volume) across the three-paradigm taxonomy, cross-tabulated by domain (generation vs. reasoning), guidance-signal type (explicit scoring function vs. MLLM-based semantic judgment), feedback scope/form (global vs. step-level; scalar vs. text vs. visual), and search-strategy properties (pruning, backtracking, dynamic budget adjustment). Its comparative analysis concludes that method choice should track task characteristics: sampling-based and iterative-refinement methods suit multimodal generation (final-output-judged, less verifiable intermediate structure), while search-based methods suit multimodal reasoning tasks with more structured, partially-verifiable intermediate steps (mathematical, spatial reasoning) that benefit from pruning erroneous branches and backtracking; feedback-based methods sit between these extremes, offering more targeted guidance than pure sampling while remaining cheaper than full search. It also references relevant benchmarks for evaluating multimodal TTS capabilities (detailed in an appendix) and identifies open challenges and future research directions as its final contribution.

## Limitations

As a review paper, its own scope is explicitly bounded to compute-centric test-time scaling (fixed model parameters, allocating additional inference-time operations such as sampling, search, verification, or refinement), deliberately excluding test-time memory augmentation (retrieval stores, episodic memory, persistent caches, expressive hidden states) and test-time training/adaptation (gradient-based or lightweight parameter updates at inference) except where a method's dominant mechanism is compute scaling with memory as an auxiliary component. The survey's coverage is necessarily a snapshot of a rapidly evolving field (explicitly noting publication volume nearly doubling within the surveyed year), so its taxonomy and comprehensiveness are bounded by the literature available at time of writing.

## Why it matters here

- **overthinking**: Only indirectly relevant: this is a broad taxonomy survey of test-time-compute allocation methods across multimodal generation and reasoning tasks, not a study of reasoning-trace length, overthinking, or the accuracy/efficiency tradeoff within a single reasoning chain. Its comparative-tradeoffs analysis (when sampling vs. feedback vs. search-based scaling is most cost-effective, and why multimodal TTS is inherently harder than text-only TTS since it must scale perceptual, spatial, and temporal compute simultaneously) provides useful organizing context for the multimodal overthinking papers elsewhere in this archive (e.g. GPRO's perception-vs-reasoning failure decomposition) but does not itself address overthinking directly.

## Entities

- **Concepts**: test-time scaling (TTS) taxonomy, sampling-based methods (Best-of-N, majority voting), feedback-based methods (reward models, iterative refinement), search-based methods (beam search, tree search, heuristic/adaptive search), compute-centric vs. memory vs. weight-adaptation test-time methods, Output Reward Model vs. Process Reward Model
- **Methods**: [Best-of-N](../../../../wiki/methods/best-of-n.md), [Majority Voting](../../../../wiki/methods/majority-voting.md), Output/Process Reward Models, Iterative Refinement, [Beam Search](../../../../wiki/methods/beam-search.md), Tree Search / Monte Carlo Tree Search, Heuristic and Adaptive Search
- **Datasets**: _none recorded_

Tags: `survey`, `test-time-scaling`, `multimodal`, `taxonomy`, `reward-models`, `search-methods`

## Abstract

Test-time Scaling (TTS) has emerged as a pivotal research direction for enhancing model performance by dynamically allocating computational resources during inference. Recent advancements have adapted this paradigm to Multimodal Foundation Models (MFMs), unlocking their potential in multimodal reasoning and generation. Despite rapid progress, the field lacks a systematic survey and unified theoretical framework to delineate the developmental landscape of multimodal TTS. To bridge this gap, we present the first comprehensive review of TTS research for MFMs, proposing a unified taxonomic framework that categorizes existing methodologies into three distinct strategies: sampling-based, feedback-based, and search-based approaches. We further summarize representative applications and benchmarks commonly utilized to evaluate multimodal TTS capabilities in generation and reasoning tasks. Finally, this survey discusses open challenges and outlines future research directions, providing a systematic roadmap for subsequent studies in this rapidly evolving field.

---

Record id: `doi:10.18653/v1/2026.findings-acl.383`
