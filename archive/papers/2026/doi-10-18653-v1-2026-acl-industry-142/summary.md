<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Prompt-Level Distillation: A Non-Parametric Alternative to Model Fine-Tuning for Efficient Reasoning

- **Authors**: Sanket Badhe, Deep Shah
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-industry.142/>
- **PDF**: <https://aclanthology.org/2026.acl-industry.142.pdf>
- **DOI**: 10.18653/v1/2026.acl-industry.142
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Prompt-Level Distillation (PLD) transfers a teacher model's reasoning heuristics into a compact student model's system prompt -- via supervised instruction extraction, DBSCAN clustering into a conflict-free instruction set, and a closed-loop conflict-resolution refinement against training failures -- letting Gemma-3 4B and Mistral Small 3.1 match frontier-model (Gemini 3 Flash) accuracy on logic-heavy classification tasks at zero-shot inference speed and no parameter updates.

## Problem

Chain-of-Thought prompting gives accurate reasoning but at prohibitive per-query latency and cost from generating long verbose traces; the standard alternative, fine-tuning a smaller student model via Knowledge Distillation, sacrifices interpretability, requires costly retraining whenever the teacher model improves or domain logic shifts, needs thousands of curated examples, and often fails to transfer genuine reasoning ability (only imitating surface style) rather than the underlying logic.

## Contributions

- Prompt-Level Distillation (PLD), a non-parametric framework that transfers a teacher model's reasoning capability into a student model's system prompt rather than into its weights, avoiding retraining/maintenance debt and parameter updates entirely
- a modular four-phase pipeline (supervised instruction extraction, DBSCAN-based clustering synthesis, closed-loop conflict resolution against training failures, zero-shot inference) that produces a portable, human-verifiable library of reasoning heuristics
- empirical demonstration that PLD lets compact models (Gemma-3 4B, Mistral Small 3.1 24B) match or exceed a frontier teacher model's own zero-shot accuracy on logic-intensive classification tasks (Contract-NLI, StereoSet, LogiQA), while running at zero-shot inference speed and cost across two distinct model architectures/families

## Method

PLD operates in four phases. (1) Supervised Instruction Extraction: for each labeled training example, a teacher model (Gemini 3 Flash, thinking mode) is prompted to simultaneously reason toward the ground-truth label and abstract that specific reasoning process into a generalized natural-language instruction (removing entity-specific details while preserving the causal logic). (2) Clustering Logic Synthesis: the resulting per-example micro-instructions are embedded (Gemini Embedding) and grouped via DBSCAN (density-based clustering, chosen over K-means because it isolates non-generalizable noise points rather than forcing every instruction into a cluster), and each dense cluster is consolidated by an LLM (Gemini 3 Pro) into one unified instruction. (3) Closed-Loop Conflict Resolution: the student model is run with the current consolidated instruction set on the training data, failure cases (where the model followed the instructions but reached the wrong label) are isolated, and a Conflict Resolution Model (same as the teacher) analyzes these failures plus successful examples to generate an updated, refined instruction set -- repeated until the validation error rate converges. (4) Inference: the fully refined instruction set is injected as the student's system prompt for zero-shot deployment, requiring no parameter updates and no retrieval of external documents at inference time. Evaluated on Contract-NLI (document-level legal entailment, 3-class), StereoSet (stereotypical-bias domain classification, comparatively simple), and LogiQA (complex deductive/conditional/disjunctive logical reasoning from expert exams), with Gemma-3 4B and Mistral Small 3.1 24B as students and Gemini 2 Flash and Gemini 3 Flash also evaluated, against zero-shot, few-shot (k=5), LoRA fine-tuning, and TextGrad (an automatic-prompt-optimization baseline).

## Results

PLD's fully refined ('Post-Conflict') prompt outperforms zero-shot, few-shot, fine-tuning, and TextGrad across all three benchmarks and all four models tested. On StereoSet, Gemma-3 4B's macro-F1 rises from 0.57 (zero-shot) to 0.90 (+0.33 absolute). On Contract-NLI, Gemma-3 4B rises from 0.67 to 0.83 macro-F1, and Mistral Small 3.1 from 0.71 to 0.78. On LogiQA, Gemma-3 4B's accuracy rises from 0.67 to 0.70 and Gemini 2 Flash from 0.64 to 0.67. Crucially, PLD closes most of the performance gap between compact student models and the more powerful teacher (Gemini 3 Flash) -- e.g. on Contract-NLI, Gemini 3 Flash zero-shot reaches 0.77 macro-F1 while PLD-distilled Gemma-3 4B reaches 0.83, i.e. the compact model matches or exceeds the frontier teacher's own zero-shot baseline on this task -- while Gemma-3 4B is reported as roughly 25x cheaper and 80x faster than Gemini-3 Flash (per the paper's cost/latency appendices). The closed-loop conflict-resolution phase (Phase 3) contributes a further +2.5% macro-F1 on the structurally complex Contract-NLI dataset beyond the clustered-but-unrefined instruction set, converging after 2 iterations there, but yields negligible additional gain on the simpler StereoSet task (converging after 1 iteration) -- indicating iterative conflict refinement matters most for tasks with intricate, overlapping edge cases rather than simple classification. Applying the PLD-style extraction-and-consolidation process to the teacher model itself (Gemini 3 Flash) also improves its own Contract-NLI macro-F1 (from a 0.77 zero-shot baseline to 0.86), showing the technique benefits even a frontier model by explicitly externalizing latent reasoning it does not otherwise apply.

## Limitations

The evaluation focuses on reasoning-intensive classification tasks with complex, static decision boundaries (e.g. regulatory compliance); PLD may be limited on tasks requiring dynamic, runtime computation (e.g. complex arithmetic or symbolic proofs) where reasoning cannot be fully externalized into a concise static instruction summary but instead genuinely requires generating intermediate tokens at inference time. The framework does not explicitly model the scaling limits of the system prompt itself -- as task complexity grows, the consolidated instruction set may grow large enough to exceed the effective context window or induce prompt-processing latency, potentially requiring further compression techniques not explored in this work. Because the teacher model can hallucinate or amplify biases present in the training data during instruction extraction (a particular risk on the StereoSet bias-measurement dataset), practitioners must verify that the consolidated instruction set does not itself encode discriminatory logic, since the student model follows these instructions faithfully.

## Why it matters here

- **overthinking**: Directly relevant as an alternative-lever mitigation: rather than shortening a reasoning trace at inference time or training a model to think less, PLD eliminates runtime chain-of-thought generation entirely for a class of tasks by pre-compiling the teacher's reasoning logic into a static, reusable prompt -- explicitly framed by the authors as decoupling reasoning depth from computational cost and as an alternative to the latency/cost overhead CoT imposes. Its explicit limitation (tasks needing genuine dynamic/runtime computation cannot be fully externalized this way) delineates where inference-time reasoning-length reduction approaches remain necessary versus where prompt-level externalization can substitute for them outright.

## Entities

- **Concepts**: Prompt-Level Distillation (PLD), non-parametric reasoning transfer, closed-loop conflict resolution, semantic clustering of extracted instructions (DBSCAN)
- **Methods**: Prompt-Level Distillation (supervised extraction + DBSCAN clustering + closed-loop conflict resolution), TextGrad (automatic prompt optimization baseline), LoRA fine-tuning (baseline), Knowledge Distillation (comparison paradigm)
- **Datasets**: Contract-NLI, StereoSet, [LogiQA](../../../../wiki/datasets/logiqa.md)

Tags: `overthinking`, `distillation`, `prompt-engineering`, `efficient-reasoning`, `chain-of-thought`

## Abstract

Advanced reasoning typically requires Chain-of-Thought prompting, which is accurate but incurs prohibitive latency and substantial test-time inference costs. The standard alternative, fine-tuning smaller models, often sacrifices interpretability while introducing significant resource and operational overhead. To address these limitations, we introduce Prompt-Level Distillation (PLD). We extract explicit reasoning patterns from a Teacher model and organize them into a structured list of expressive instructions for the Student model’s System Prompt. Evaluated using Gemma-3 4B, PLD improved Macro F1 scores on StereoSet (57% to 90.0%) and Contract-NLI (67% to 83%), while increasing LogiQA accuracy to 70%. Similar results on Mistral Small 3.1 demonstrate cross-architecture generalizability, enabling these compact models to match frontier performance with negligible latency overhead. These expressive instructions render the decision-making process transparent, allowing for full human verification of logic, making this approach ideal for regulated industries such as law, finance, and content moderation, as well as high-volume use cases and edge devices.

---

Record id: `doi:10.18653/v1/2026.acl-industry.142`
