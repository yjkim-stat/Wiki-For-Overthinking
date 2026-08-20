<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# PROSLEX: A Novel Dataset for Expert-Annotated Legal Statute Prediction for Indian Judiciary

- **Authors**: Subinay Adhikary, Upal Bhattacharya, Vivek Kumar Singh, Anurag Sharma, Shubham Kumar Nigam, Suvasis Das, Shouvik Kumar Guha, Koustav Rudra, Kripabandhu Ghosh
- **Venue**: cs.AI
- **Published**: 2026-08-09
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.08830>
- **PDF**: <https://arxiv.org/pdf/2608.08830v1>
- **Topics**: test-time-scaling
- **Relevance score**: reasoning-training 0.25, test-time-scaling 0.40

## In one line

Builds an expert-annotated Indian Supreme Court dataset in which each applicable statute is paired with the specific text span a legal expert says establishes it, and uses it to show that predicting the right statute and giving the right reason are separable abilities.

## Problem

Legal statute prediction has been treated as multi-label classification, so a system is scored only on whether it names the right provision. Existing Indian-judiciary resources carry no expert-written justification, which means nothing distinguishes a model that identified the statutory elements from one that pattern-matched the surface facts, and nothing supports evaluating an explanation.

## Contributions

- PROSLEX: 1,623 Indian Supreme Court documents with 7,450 expert-annotated explanation spans tied to seven IPC statutes, with per-statute train/validation/test splits and a documented per-document annotation cost.
- A calibrated adjudication protocol: a 50-pair blind study by a senior expert establishes that ROUGE-L below 0.75 needs adjudication in 90 percent of instances, and that threshold then governs the whole corpus, with 37 percent of cases adjudicated.
- A benchmark showing fine-tuned domain encoders still beat four frontier LLMs on statute prediction (0.82 against 0.71), while chain-of-thought LLMs lead when an explanation is also required.
- A measured collapse of tree-of-thoughts across four models, and an error analysis of correct predictions with legally invalid supporting spans.

## Method

From 33,546 Supreme Court of India judgements (1950-2016, 444 Acts, 3,428 Sections), seven IPC statutes were chosen by legal significance, sufficient document count and distinctiveness of provision -- the last criterion deliberately excluding neighbouring homicide sections that would confound the label. Two postgraduate legal experts per statute independently selected cases where the section was upheld rather than merely charged, extracted the case facts, and annotated the text spans constituting the explanation for each statute. Inter-annotator agreement was measured as ROUGE-L overlap between the two experts' explanation-statute pairs; a calibration study had a senior expert with 15 years' experience blind-review 50 sampled pairs and indicate whether adjudication was needed, which established that pairs below 0.75 needed it in 90 percent of instances. That threshold was then applied: below it the senior expert selected or merged, at or above it the more detailed annotation was kept. About 37 percent of cases went to adjudication. Evaluation covers fine-tuned encoders (InLegalBERT, LegalBERT, BERT-base, Longformer, RoBERTa) and four LLMs under zero-shot, few-shot with K-nearest-neighbour exemplar selection in InLegalBERT embedding space, chain-of-thought, and tree-of-thoughts with breadth-first search (depth 7, 3 children, 10 nodes per level, confidence threshold 0.4). Explanations are scored lexically (ROUGE, BLEU), semantically (BLEURT, BERTScore) and by legal experts on a 0-4 alignment scale.

## Results

1,623 annotated documents with 7,450 explanations, split 70/10/20 stratified, at a cost of 94 INR per document and about 152,562 INR total, which the authors state was the entire project budget and the binding constraint on size. Expert agreement: mean ROUGE-L 0.79 (SD 0.12), median 0.80, quartiles 0.72 and 0.87. On statute prediction alone the fine-tuned domain encoder wins: InLegalBERT 0.82 macro-F1 against DeepSeek's best LLM result of 0.71 few-shot and 0.64 zero-shot. The striking result is tree-of-thoughts, which collapses to 0.17, 0.13, 0.18 and 0.21 macro-F1 for DeepSeek, Llama-3.1-70B, Claude and GPT-4 -- three to four times worse than the same models few-shot, and worse than every other configuration in the paper including zero-shot. The authors attribute this to branches interpreting the same statutory language differently, producing inconsistent predictions that the search cannot reconcile. Chain-of-thought with explanation recovers most of it and lets GPT-4 reach 0.75, above every other LLM setting though still below the encoder. Every configuration fails on IPC 506 (criminal intimidation): 0.45 for the best encoder, 0.02 to 0.06 for the worst encoders, and 0.33 to 0.54 for the LLMs. On explanations GPT-4 leads on all six automatic metrics (ROUGE-L 0.31, BLEU 0.28, BLEURT 0.63, BERTScore 0.67) and on expert rating (3.91 of 4), with DeepSeek second on expert rating (3.83) but nearly last on every automatic metric (ROUGE-L 0.15, BERTScore 0.46) -- so the two families of measure disagree about the ordering. Expert ratings are bimodal: for GPT-4, 47 of the sampled explanations score 4 and none score 0 or 1, while Llama-3.1-70B has 38 at 4 and 10 at 0 including outright generation failures; scores of 1 and 2 are rare across all models. The error analysis shows GPT-4 predicting IPC 147 correctly while grounding it in a span describing a fight rather than the span describing the appellant leading a group in assault, which is what the statute requires.

## Limitations

The paper has no limitations section. Reader-visible limits: seven statutes and 1,623 documents, explicitly capped by a fixed annotation budget, so coverage is a small fraction of the 512 criminal-law sections; a statute was excluded when it was hard to distinguish from a neighbour, which removes exactly the cases where statute prediction is legally contested. Only cases where the section was upheld were annotated, so the dataset contains no negative evidence about provisions that were charged and rejected. Agreement is reported as ROUGE-L between two annotators, a lexical overlap of free-text spans rather than a chance-corrected agreement statistic, and the 0.75 threshold rests on a 50-pair calibration by a single senior expert. Expert explanation ratings are reported without inter-rater agreement and appear to cover roughly 50 items per model. The tree-of-thoughts collapse is diagnosed in prose rather than measured -- no ablation isolates search depth, branching or the pruning threshold from the failure -- so a configuration artefact cannot be ruled out. The LLMs are proprietary snapshots evaluated at one temperature with no repeats.

## Why it matters here

- **test-time-scaling**: The cleanest negative result on structured search this archive holds: tree-of-thoughts with breadth-first search over a 2,187-path space loses three to four times its few-shot macro-F1 for all four models tested, landing below zero-shot. The authors' diagnosis is that branches interpret the same statutory language inconsistently and the search has no way to adjudicate between them -- which says the precondition for search paying off is a scorer that can compare branches on the axis that matters, and that where the difficulty is interpretive rather than combinatorial, more branches means more disagreement rather than more coverage. The paper also separates two things test-time-scaling work usually reports together: GPT-4 predicts the statute correctly while grounding it in the wrong span, so an accuracy gain from more inference compute is not evidence that the reasoning improved. That is the same dissociation the archive's chain-of-thought faithfulness entries keep finding, arriving here from a domain where a human expert can say exactly which span was required.

## Entities

- **Concepts**: legal statute prediction, explanation faithfulness, [annotation agreement](../../../../wiki/concepts/annotation-agreement.md), human evaluation, in-context learning, search over reasoning
- **Methods**: [chain-of-thought prompting](../../../../wiki/methods/chain-of-thought-prompting.md), [tree-of-thoughts](../../../../wiki/methods/tree-of-thoughts.md), [in-context learning](../../../../wiki/methods/in-context-learning.md), [few-shot prompting](../../../../wiki/methods/few-shot-prompting.md), [zero-shot prompting](../../../../wiki/methods/zero-shot-prompting.md), K-nearest-neighbour exemplar selection, multi-label classification
- **Datasets**: PROSLEX, Indian Supreme Court judgements corpus

Tags: `legal-nlp`, `explanation`, `tree-of-thoughts`, `expert-annotation`, `statute-prediction`

## Abstract

Legal Statute Prediction (LSP) involves automatically identifying relevant legal statutes given factual descriptions in legal documents, typically framed as a multi-label classification task within natural language processing and information retrieval research. While recent advances have begun incorporating Large Language Models (LLMs) for statute prediction, current approaches primarily focus on accuracy metrics without addressing the critical need for legal reasoning, a fundamental requirement in judicial contexts where decisions must be explainable and justifiable. To address this research gap, we present PROSLEX (PRediction Of Statutes and LEgal eXplanation), a comprehensive dataset comprising 1,623 expert-annotated legal documents from the Indian context. Each document is paired with statute predictions and detailed explanations, totaling 7,450 explanations, capturing the underlying legal reasoning. Using this dataset, we systematically evaluate various prompting strategies, including zero-shot, few-shot, chain-of-thought, and tree-of-thoughts approaches, to generate both statute predictions and their corresponding legal rationales. Our evaluation framework measures not only predictive performance but also the coherence and legal validity of generated explanations, positioning PROSLEX as a benchmark for developing explainable AI systems that can support legal practitioners while advancing research in interpretable legal NLP. To ensure reproducibility, we have made our PROSLEX dataset and model code available on GitHub: https://github.com/subinay494/Legal_Statute_Prediction_Explanation.

---

Record id: `arxiv:2608.08830`
