<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# How Do Answer Tokens Read Reasoning Traces? Self-Reading Patterns in Thinking LLMs for Quantitative Reasoning

- **Authors**: Haoyang Chen, Yi Liu, Jianzhi Shao, Tao Zhang, Chengfu Huo, Wei Hu
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1507/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1507.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1507
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Analyzing how answer tokens attend back to reasoning tokens ('self-reading') in thinking LLMs reveals a stable, structured 'benign self-reading' pattern strongly correlated with correctness -- a forward-drifting attention centroid plus persistent focus on key semantic anchors -- interpreted as internal certainty, versus diffuse/irregular attention in incorrect solutions; a training-free Self-Reading Quality (SRQ) score built from this pattern is used to select contrastive samples for activation-steering vectors that consistently improve accuracy (up to 2.6pp) across three models, three steering mechanisms, and multiple quantitative-reasoning benchmarks including out-of-domain transfer.

## Problem

Thinking LLMs generate a reasoning trace before answering, and prior activation-steering work has mainly targeted shaping the reasoning trace itself, but how answer tokens actually read and integrate that trace during answer generation -- navigating noise and extracting key evidence from traces that can span thousands of tokens -- remains unexplored, despite this integration step being where reasoning quality ultimately translates (or fails to translate) into a correct answer.

## Contributions

- identification of a stable, structured 'benign self-reading' pattern in the answer-to-reasoning attention of thinking LLMs -- a forward-shifting attention centroid plus persistent concentration on key semantic anchors -- strongly correlated with answer correctness, validated by human annotation and consistent across three model families
- an interpretation of this pattern through metacognitive control/monitoring theory, framing it as a behavioral signature of the model's internal certainty when committing to and evidencing a solution path
- Self-Reading Quality (SRQ), a training-free, quantitative score combining geometric (attention-trajectory) and semantic (anchor-concentration) sub-metrics that reliably distinguishes benign from disorganized self-reading
- an SRQ-driven contrastive sample-selection method for constructing activation-steering vectors, shown to consistently improve accuracy across three models, three steering mechanisms (CAA, Conceptor, PCA-CAA), and multiple benchmarks including out-of-domain transfer, outperforming or matching three existing reasoning-focused steering baselines

## Method

Analyzes the answer-to-reasoning attention submatrix in the middle-to-late layers of three frontier thinking LLMs (R1-Distill-Llama-8B, R1-Distill-Qwen-7B, Qwen3-4B-Thinking) on GSM8K, defining the attention centroid of an answer token as the row-normalized, weighted-average position it attends to over the reasoning trace. Identifies two features of a 'benign self-reading' pattern in correct solutions: (1) a forward-shifting attention centroid -- as answer decoding proceeds, the reading focus progressively moves toward later reasoning positions, tracked via a global Pearson correlation (SRQ_corr) and a diagonal-alignment score (SRQ_diag) between answer-token index and centroid position, plus a local sliding-window forward-consistency score (SRQ_local_cover); (2) persistent concentration on key semantic anchors (constraints, solution plans, conclusions) rather than uniform/diffuse attention, measured via semantic-dimension scores comparing attention flow toward LLM-API-labeled 'good' (correct/informative) vs. 'bad' (incorrect/misleading) reasoning tokens (SRQ_think, SRQ_ans) and boundary-emphasis scores on constraint/conclusion positions (SRQ_start/end). Interprets this jointly as a signature of internal certainty aligned with metacognitive control (steady forward progress along a committed solution path) and monitoring (repeatedly revisiting key evidence) theories from cognitive psychology. Validates the correctness-benign-self-reading link via human annotation (200 randomly sampled and a further 50-correct/50-incorrect balanced subset of GSM8K solutions, unanimous 3-annotator agreement required), finding benign self-reading common in correct solutions and rare in incorrect ones. Builds an integrated SRQ score (a weighted sum of rescaled geometric and semantic sub-metrics) per solution, ranks correct/incorrect solutions by it, and selects the top-80%-SRQ correct solutions and bottom-80%-SRQ incorrect solutions as contrastive sets to construct activation-steering vectors (mean answer-token-activation difference between the two sets, at a chosen layer) applied at inference via three different steering mechanisms (classic CAA, conceptor steering, PCA-CAA) to test the signal's generality.

## Results

Human annotation confirms the link between benign self-reading and correctness: on 200 randomly-sampled GSM8K solutions from R1-Distill-Llama-8B, 159/171 correct solutions exhibit benign self-reading versus only 3/26 incorrect solutions; on a balanced 50-correct/50-incorrect subset, the pattern holds (48/50 correct with benign self-reading vs. 4/48 incorrect). Aggregated attention heatmaps over 100 correctly-solved samples per model show a consistent, stable soft-diagonal ridge across all three models, confirming benign self-reading is not anecdotal but an intrinsic, structured behavior of correct reasoning in thinking LLMs. SRQ-driven steering consistently improves accuracy across all three models, three steering mechanisms, and three benchmarks (GSM8K, MATH500, SVAMP): on GSM8K, gains range from +1.1 to +2.6 points depending on model/mechanism (e.g. R1-Distill-Llama-8B+PCA-CAA: 87.5%->89.9%, +2.4); on the harder, longer-solution MATH500, gains of +0.6 to +2.3 points are observed (R1-Distill-Llama-8B+Conceptor: 86.0%->87.9%, +2.3); on SVAMP (used to test cross-dataset transfer of vectors constructed from GSM8K), gains of +1.0 to +2.5 points are observed across all models/mechanisms, confirming the method targets a general internal reading strategy rather than overfitting to one dataset's steering vectors. Comparison against three other reasoning-focused steering baselines (RepE, SAE-free, SEAL) on GSM8K shows SRQ-based steering matches or exceeds all three under both PCA-CAA and CAA mechanisms (e.g. PCA-CAA: SRQ reaches 89.9%/88.4% on the two models versus RepE's 89.5%/87.8% and SAE-free's 89.6%/88.1%). Generalization to SciQ (scientific QA) and the substantially harder AIME24-25 competition-math benchmark (using steering vectors transferred from MATH500) also shows consistent gains, reaching up to +6.6 points over the base model on AIME24-25 for R1-Distill-Llama-8B (41.7%->48.3%), equivalent to four additional correctly-solved competition problems -- confirming the filtered signal reflects a general property of internal certainty rather than a GSM8K-specific artifact. An ablation removing either SRQ sub-dimension (geometric-only vs. semantic-only vs. full) shows both contribute, with the geometric (forward-drift) component having a stronger individual effect on steering effectiveness than the semantic (anchor-concentration) component. A 'Same Pool' control analysis (applying SRQ filtering within the same fixed candidate pool used by a standard steering baseline, rather than drawing from a larger pool) shows SRQ-filtered steering remains competitive with or slightly outperforms the baseline while using fewer samples, confirming the improvement comes from selecting higher-quality contrastive pairs via SRQ rather than merely having access to more raw data. A qualitative case study of an incorrect-but-long solution (many reflective 'wait' tokens, reaching a wrong final answer) shows a diffuse attention heatmap with no clear diagonal band and a centroid trajectory that oscillates rather than drifting forward -- illustrating a failure of both control (no committed solution branch) and monitoring (no consistent semantic-anchor lock-on) even when the trace superficially resembles thorough deliberation.

## Limitations

The paper does not discuss limitations explicitly in the excerpted sections; the analysis and steering method are demonstrated on three specific model families/sizes (7-8B distilled or 4B thinking models) and a set of quantitative reasoning benchmarks -- generalization to substantially larger models, closed-source models, or non-quantitative reasoning domains is not directly reported. SRQ construction requires LLM-API-based (GPT-5, Gemini-3-pro-preview) span-level labeling of 'good' vs. 'bad' reasoning tokens for the semantic dimension, an external supervision dependency for the sample-selection stage even though the resulting steering intervention itself is training-free at inference time.

## Why it matters here

- **overthinking**: Directly relevant as a mechanistic account of what distinguishes productive from unproductive reasoning, complementary to length- or entropy-based diagnostics elsewhere in this archive: it locates the signal not in the reasoning trace itself but in how the *answer* stage reads it back, and its case study of a long, reflection-token-heavy but wrong solution -- diffuse attention with no forward drift or anchor lock-on -- is a concrete, attention-level characterization of the kind of unproductive elaboration (reasoning that looks thorough but never commits to or evidences a solution path) that overthinking-mitigation methods in this archive try to detect and remove.

## Entities

- **Concepts**: self-reading (answer-to-reasoning attention), benign self-reading pattern, attention centroid (forward drift), semantic anchor concentration, Self-Reading Quality (SRQ), internal certainty (control and monitoring)
- **Methods**: Self-Reading Quality (SRQ) scoring, Contrastive Activation Addition (CAA), Conceptor steering, PCA-CAA, RepE (baseline), SAE-free (baseline), SEAL (baseline)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH500](../../../../wiki/datasets/math500.md), [SVAMP](../../../../wiki/datasets/svamp.md), [SciQ](../../../../wiki/datasets/sciq.md), AIME24-25

Tags: `mechanistic-interpretability`, `attention-analysis`, `activation-steering`, `reasoning-trace-analysis`, `internal-certainty`

## Abstract

Thinking LLMs produce reasoning traces before answering. Prior activation steering work mainly targets on shaping these traces. It remains less understood how answer tokens actually read and integrate the reasoning to produce reliable outcomes. Focusing on quantitative reasoning, we analyze the answer-to-reasoning attention and observe a benign self-reading pattern aligned with correctness, characterized by a forward drift of the reading focus along the reasoning trace and a persistent concentration on key semantic anchors, whereas incorrect solutions exhibit diffuse and irregular attention pattern. We interpret this as internal certainty during answer decoding, where the model commits to a viable solution branch and integrates key evidence. Following this, we propose a training-free steering method driven by Self-Reading Quality (SRQ) scores combining geometric metrics for process control with semantic metrics for content monitoring. SRQ selects data to build steering vectors that guide inference toward benign self-reading and away from uncertain and disorganized reading. Experiments show that our method yields consistent accuracy gains.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1507`
