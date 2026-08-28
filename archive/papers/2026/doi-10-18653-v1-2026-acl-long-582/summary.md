<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Mathematical Proof as a Litmus Test: Revealing Failure Modes of Advanced Large Reasoning Models

- **Authors**: Dadi Guo, Jiayu Liu, Zhiyuan Fan, Zhitao He, Haoran Li, Yuxin Li, Yumeng Wang, Yi R. Fung
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.582/>
- **PDF**: <https://aclanthology.org/2026.acl-long.582.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.582
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

RFMDataset uses 200 manually-curated mathematical proof problems and a 10-category fine-grained error taxonomy (judged by LLM-as-a-judge, validated against human labels) to reveal that even top reasoning models (GPT-o1/o3, Claude-3.7-Sonnet-Thinking, Qwen3-235B, DeepSeek-R1) achieve under 20-60% proof accuracy, dominated by logical violation, hidden assumption, vague argument, and incomplete proof failures that self-reflection prompting only modestly improves.

## Problem

High reported accuracy of large reasoning models on popular math benchmarks and reliance on purely numerical final-answer evaluation mask true reasoning shortcomings, since single flawed intermediate steps that don't change the final numerical answer go undetected, and small competition benchmarks (e.g. 30-problem AIME) leave too few incorrect instances for thorough failure analysis.

## Contributions

- RFMDataset, 200 diverse, difficulty-controlled mathematical proof problems specifically curated (novel, non-overused sources) to expose reasoning failures that final-answer-only benchmarks mask
- a 10-category fine-grained proof-failure taxonomy plus an LLM-as-a-judge evaluation pipeline validated against human annotation (87.61% MCC)
- an empirical finding that even top reasoning models achieve low overall proof accuracy (mostly under 20-60%) and that failure-mode distributions are strikingly similar across models and difficulty levels, concentrated in logical violation, hidden assumption, vague argument, and incomplete proof
- evidence that prompting models to self-reflect on specific named failure modes yields only modest, inconsistent improvement, implying the underlying limitations are not simply superficial oversights correctable via self-correction alone

## Method

Manually constructs RFMDataset: 200 diverse mathematical proof problems (52 middle-school, 88 high-school, 60 undergraduate; 9 subjects; 4 difficulty levels) selected from exams, media, textbooks and competitions for diversity, difficulty (excluding intuitively/deterministically solvable problems), and novelty (avoiding overused sources like IMO). Ten proprietary/open-source large reasoning models generate proofs, which are evaluated by an LLM-as-a-judge (Gemini-2.5-pro-preview-0506) using a 10-category fine-grained failure-mode taxonomy (Transformation Error, Over Generalization, Invalid Construction, Wrong Division, Circular Reasoning, Logic Violation, Hidden Assumption, Boundary Neglect, Vague Argument, Incomplete Proof, plus 'Others'), reporting pass@1 accuracy and per-failure-mode distribution; judge reliability is validated against 240 human-labeled samples (MCC 87.61% overall, up to 91.09% for GPT-o4-mini). A follow-up experiment prompts three models (Doubao-1.5-thinking-pro, GPT-o4-mini, DeepSeek-R1-0528) to self-reflect on specific targeted failure modes (logical violation; vague argument/incomplete proof; both combined) to test whether self-correction resolves the identified failures.

## Results

Overall proof accuracy is low across the board: Qwen3-235B-A22B, Deepseek-R1-0120, Claude-3.7-Sonnet-Thinking and GPT-o1 all score below 20% overall; Gemini-2.5-Pro-Preview-0506/0605 and Gemini-3-Pro-Preview are the only models exceeding 50% (56.50-59.50%), while most other models fall short even at the lowest difficulty level -- all models except the two Gemini variants achieve under 60% accuracy even on the easiest problems. Accuracy varies substantially by knowledge domain: models consistently do worse on geometry, number sequence, combinatorics and probability, and better on algebra and number theory. Failure-mode distributions are strikingly similar across different models regardless of their overall accuracy or the problem's difficulty level, concentrated in four categories: logical violation, hidden assumption, vague argument, and incomplete proof -- Gemini models show notably lower proportions of logical-violation and vague-argument errors than others, correlating with their higher overall accuracy. Logical violation and vague argument directly indicate failures in the correctness/rigor of single reasoning steps; hidden assumption (treated as a form of hallucination, using unstated conditions) and incomplete proof (insufficient demonstration, failing to recognize when a proof is actually complete) indicate hallucination and incompleteness in the reasoning process. Explicitly prompting models to self-reflect on specific failure modes produces only modest, inconsistent gains: e.g. DeepSeek-R1-0528's overall accuracy moves from 37.00% (baseline) up to a best of 42.00% across reflection variants (varying by MS/HS/UG subset and which failure mode is targeted, with some reflection variants performing worse than baseline on some subsets), and GPT-o4-mini's best achievable score across all reflection strategies (27.00%) is only modestly above its baseline (21.00%) -- self-reflection is insufficient to fundamentally resolve the underlying reasoning limitations, though prompts targeted at specific failure modes can help in at least one MS/HS/UG subset.

## Limitations

Pass@1 (single-sample) accuracy is used rather than pass@k due to the cost of generating and judging multiple full proofs per problem for fine-grained failure analysis, which the paper acknowledges limits statistical robustness relative to multi-sample evaluation. The LLM-as-a-judge approach cannot independently verify a proof's deeper mathematical insight/cleverness (only the absence of identifiable step-level failures is used as a soundness proxy), so a proof's true intrinsic value beyond step-level correctness is not directly assessed. The self-reflection experiments are limited to three models and three prompt variants; the paper's proposed remedies (domain-specific training data, formally verifiable agentic environments like Lean) are discussed as future directions rather than evaluated.

## Why it matters here

- **overthinking**: Not directly about overthinking: this paper diagnoses correctness and rigor failures in reasoning models' mathematical proofs, not reasoning-trace length or the accuracy/efficiency tradeoff. It is tangential background evidence that current reasoning models have persistent step-level reasoning-quality limitations regardless of how much they 'think,' and that self-reflection prompting -- a mechanism some overthinking-mitigation methods rely on or try to curb -- does not reliably fix reasoning-quality problems even when explicitly targeted at named failure modes.

## Entities

- **Concepts**: mathematical proof as diagnostic (litmus test), fine-grained proof failure taxonomy, logical violation, hidden assumption (hallucination), incomplete proof, self-reflection insufficiency
- **Methods**: LLM-as-a-judge (Gemini-2.5-pro-preview-0506), fine-grained failure-mode taxonomy classification, targeted self-reflection prompting
- **Datasets**: RFMDataset (new, 200 proof problems)

Tags: `mathematical-reasoning`, `proof-generation`, `failure-mode-analysis`, `evaluation-methodology`, `self-reflection`

## Abstract

Large reasoning models ( e.g., R1, o3) have demonstrated remarkable mathematical problem-solving abilities. However, the high reported accuracy of these advanced models on popular datasets and reliance on purely numerical evaluation often mask their true reasoning shortcomings. To address this, we propose leveraging the inherent rigor and methodological complexity of mathematical proofs as a diagnostic tool to expose these hidden failures. Specifically, we introduce the RFMDataset (Reveal Failure Modes), a collection of 200 diverse mathematical proof problems to thoroughly evaluate the performance of advanced models. Our in-depth analysis of their failures uncovers 10 fine-grained error types, which shows fundamental limitations in current large reasoning models: 1) Large reasoning models still have limited capability in generating entirely correct mathematical proofs, with some models solving less than 20% of problems and even making mistakes on fundamental ones; 2) models exhibit a diverse spectrum of reasoning failures, prominently demonstrating the lack of guarantees for the correctness and rigor intermediate reasoning steps; and 3) models show hallucination and incompleteness during the reasoning process. Our findings also reveal that directly prompting models to self-reflect on specific failure modes is insufficient to resolve the current logical dilemmas, necessitating domain knowledge and formal verification.

---

Record id: `doi:10.18653/v1/2026.acl-long.582`
