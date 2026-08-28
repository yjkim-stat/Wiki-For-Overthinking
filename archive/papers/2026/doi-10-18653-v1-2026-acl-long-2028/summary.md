<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Programming over Thinking: Efficient and Robust Multi-Constraint Planning

- **Authors**: Derrick Goh Xin Deik, Quanyu Long, Zhengyuan Liu, Nancy F. Chen, Wenya Wang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.2028/>
- **PDF**: <https://aclanthology.org/2026.acl-long.2028.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.2028
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

SCOPE replaces long natural-language reasoning chains for multi-constraint planning with a two-stage, multi-agent pipeline that infers a query's combination/constraint structure once and compiles it into reusable, deterministic solver functions (Combination/Filter/Deliver), reaching 93.1% success on TravelPlanner with GPT-4o (a 61.6-point gain over CoT) while cutting inference cost 1.4x and time 4.67x versus the best baseline.

## Problem

Multi-constraint planning requires exhaustively reasoning over a large candidate space where a single missed combination or accumulated small error invalidates the result; pure natural-language reasoning (CoT, ToT) is inherently probabilistic and grows exponentially costlier and less reliable as constraints compound, while existing solver- or code-based approaches either write problem-specific code from scratch for every query or depend on fixed solvers, failing to capture generalizable planning logic reusable across queries.

## Contributions

- a reusable abstraction that separates query-specific reasoning from execution logic, generating solver functions parameterized to handle different queries in the same domain with minimal adaptation rather than regenerating problem-specific code per query
- an autonomous multi-agent pipeline (Query-Specific Problem Reasoning + Generic Solver Generation) that induces this abstraction from a single example query-answer pair, with no manual prompt engineering or fixed solver dependency
- state-of-the-art multi-constraint planning results across 5 proprietary LLMs and 3 benchmarks, with especially large gains on weaker foundation models, at substantially lower inference cost and latency than text-based (CoT/ToT/multi-agent) and prior solver-based baselines
- empirical evidence and ablations that the approach improves robustness (stable high success rate as combinatorial complexity grows, unlike text-reasoning baselines which degrade rapidly) and that each pipeline stage (formalization, optimization, solver refinement) is necessary

## Method

SCOPE (Scalable COde Planning Engine) disentangles query-specific reasoning from generic code execution across two stages. In Query-Specific Problem Reasoning, a Planning Agent converts one example query into a structured JSON representation with 'combinations' (parameters defining the full candidate-plan generation space, for exhaustive rather than heuristic enumeration) and 'constraints' (parameters isolating validation/filtering logic), a Solution Agent converts the example's answer into a matching structured-output format, and one or more Optimization Agents iteratively refine these representations to remove redundancy, resolve ambiguity and ensure combinations fully cover the candidate space. In Generic Solver Generation, three agents (Combination/Filter/Deliver Function Generator) synthesize three reusable Python functions operating on parameter values rather than hardcoded instance content: Combination Function exhaustively enumerates candidate plans, Filter Function returns only plans satisfying all constraints, and Deliver Function converts the final structured plan into a natural-language answer; a solver-refinement loop iteratively regenerates any function whose output does not match the example's structured solution or ground-truth answer. At inference, only a lightweight Input Agent extracts combination/constraint parameter values for a new query (using the same in-context exemplar), which are then fed through the pre-generated, unmodified solver functions -- no further LLM reasoning or code regeneration occurs per query.

## Results

Across 5 proprietary LLMs (GPT-4o, GPT-o3, GPT-5, Gemini-1.5-Pro, Gemini-2.5-Pro) and 3 benchmarks (TravelPlanner, and Natural Plan's Trip Planning and Meeting Planning), SCOPE consistently improves success rate over Direct prompting, CoT, ToT, EvoAgent, HyperTree Planning, Thought-of-Search and CPMPy baselines, with the largest gains on weaker foundational models: GPT-4o's success rate rises from 12.5% (best baseline, ToS) to 87.1% on Trip Planning, and from a CoT baseline of 31.5% to 93.1% on TravelPlanner (a 61.6-point absolute gain), while cutting inference cost 1.4x and time 4.67x versus the best baseline. On Meeting Planning, SCOPE reaches 100% success rate with several models (GPT-4o, GPT-5, Gemini-2.5-Pro) versus a range of 34.7-59.8% for baselines. Gains shrink but remain positive on the strongest foundational models (GPT-5, Gemini-2.5-Pro), where SCOPE still matches or exceeds baseline performance, indicating the framework's advantage comes from deterministic executable logic rather than the base model's raw reasoning scale -- confirmed directly by SCOPE on smaller/weaker models (GPT-4o, Gemini-1.5-Pro) matching or outperforming stronger baseline models (GPT-o3, GPT-5) at much lower cost. Success rate stays high (often above 90%) across increasing problem complexity levels for SCOPE, while text-based baselines (especially on weaker foundation models) collapse rapidly as complexity/combinatorial constraints grow -- SCOPE's advantage widens with harder problems rather than narrowing. Cost/time analysis shows SCOPE avoids the exponentially growing API cost that multi-step, multi-agent text-reasoning baselines (ToT, EvoAgent, HTP) incur, since it performs plan enumeration in deterministic code rather than repeated LLM text generation, while remaining comparable in per-query cost to single-step methods and far cheaper in total cost-to-correct-solution than iterative reasoning baselines. An ablation removing Problem Formalization, Problem Optimization, or Solver Refinement each causes large performance drops (e.g. removing Problem Optimization drops Trip Planning success from 87.1% to 0.0%), confirming all three pipeline components are necessary. A single example query-answer pair suffices for solver construction in the reported experiments due to full constraint coverage, though supplementary analysis (referenced in the appendix) shows using multiple examples with incomplete individual constraint coverage improves robustness via union coverage.

## Limitations

The framework relies on LLMs' coding and structured-generation skills, so the reported experiments primarily evaluate closed-source models (GPT-4o/o3/5, Gemini-1.5/2.5-Pro) rather than open-source models. Solver functions remain tied to a specific problem domain: while reusable across queries within that domain, they cannot be directly applied to a new domain without redefining the problem structure, and SCOPE does not explicitly handle domain drift (a new query whose structure cannot be fully expressed within the existing solver's specification) -- extending the framework with automatic drift detection and adaptive solver regeneration is left as future work. Error analysis identifies the lightweight per-query Input Agent as the primary source of remaining failures: smaller/weaker models can misassign structured-representation parameter values, overgeneralize invalid constraint interpretations from the one-shot exemplar, or introduce subtle numerical errors on tasks requiring large structured outputs (e.g. Meeting Planning).

## Why it matters here

- **overthinking**: Central to the topic in spirit if not in vocabulary ('Programming over Thinking' is literally the paper's framing): it identifies the same core failure mode the overthinking literature targets for reasoning traces -- long natural-language reasoning chains are probabilistic, accumulate error, and become prohibitively costly as problem complexity grows -- and proposes a structurally different fix than length-penalty or early-stopping methods: replace repeated, per-query natural-language reasoning with a one-time reasoning step that compiles into reusable, deterministic code. Its ablation showing the pipeline's structuring stages (not raw model scale) drive the gains, and its result that smaller models with SCOPE beat larger models doing plain CoT, is a strong data point for the broader claim that much of what a long reasoning trace does for planning-style tasks can be done more reliably and far more cheaply outside natural-language token generation entirely.

## Entities

- **Concepts**: reasoning-execution disentanglement, reusable solver functions (Combination/Filter/Deliver), structured combination/constraint representation, code-as-proxy-for-reasoning
- **Methods**: SCOPE (Scalable COde Planning Engine), Chain-of-Thought (CoT, baseline), Tree-of-Thought (ToT, baseline), EvoAgent (baseline), HyperTree Planning (HTP, baseline), Thought of Search (ToS, baseline), CPMPy constraint programming (baseline)
- **Datasets**: TravelPlanner, Natural Plan (Trip Planning, Meeting Planning)

Tags: `multi-constraint-planning`, `code-generation`, `agentic-reasoning`, `efficient-reasoning`, `reasoning-execution-separation`

## Abstract

Multi-constraint planning involves identifying, evaluating, and refining candidate plans while satisfying multiple, potentially conflicting constraints. Existing large language model (LLM) approaches face fundamental limitations in this domain. Pure reasoning paradigms, which rely on long natural language chains, are prone to inconsistency, error accumulation, and prohibitive cost as constraints compound. Conversely, LLMs combined with coding- or solver-based strategies lack flexibility: they often generate problem-specific code from scratch or depend on fixed solvers, failing to capture generalizable logic across diverse problems.To alleviate these issues, we introduce the Scalable Code Planning Engine (SCOPE), a systematic framework that disentangles query-specific problem reasoning from generic code execution. SCOPE first transforms input queries into optimized structured representations, capturing the interdependent constraints, and then autonomously generates reusable solver functions (Combination, Filter, and Deliver) that provide consistent and reliable execution across diverse problems. SCOPE achieves state-of-the-art performance while lowering cost and latency. For example, with GPT-4o, it reaches 93.1% success on TravelPlanner, a 61.6% gain over the best baseline (CoT) while cutting inference cost by 1.4 times and time by approximately 4.67 times. Code is available at https://github.com/DerrickGXD/SCOPE.

---

Record id: `doi:10.18653/v1/2026.acl-long.2028`
