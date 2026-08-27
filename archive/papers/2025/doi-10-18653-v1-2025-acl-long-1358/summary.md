<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Learning to Reason Over Time: Timeline Self-Reflection for Improved Temporal Reasoning in Language Models

- **Authors**: Adrián Bazaga, Rexhina Blloshmi, Bill Byrne, Adrià de Gispert
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2025.acl-long.1358/>
- **PDF**: <https://aclanthology.org/2025.acl-long.1358.pdf>
- **DOI**: 10.18653/v1/2025.acl-long.1358
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## In one line

TISER (Temporal Self-Reflective Prompting) extends chain-of-thought into a four-stage test-time-scaling pipeline -- reasoning, explicit timeline construction, iterative self-reflection, then answer generation -- for temporal reasoning, and fine-tuning smaller open models (Mistral-7B, Qwen2.5-7B) on TISER-formatted synthetic traces lets them match or beat GPT-4o on in-domain and out-of-distribution temporal reasoning benchmarks.

## Problem

LLMs struggle with temporal reasoning (event sequencing, durations, inter-temporal relationships) even at frontier scale, and while test-time scaling of reasoning has improved general reasoning performance, no prior work applies test-time scaling specifically to temporal reasoning, where errors often stem from failing to construct or verify a coherent event timeline.

## Contributions

- TISER, a four-stage test-time-scaling framework (reasoning, timeline construction, iterative reflection, answer generation) specifically targeting temporal reasoning, the first work to apply test-time scaling to this task
- a synthetic dataset-construction method that augments existing temporal reasoning benchmarks with TISER-formatted intermediate reasoning traces, filtered for gold-answer consistency, enabling supervised fine-tuning
- state-of-the-art results on multiple temporal reasoning benchmarks (in-domain and out-of-distribution) with fine-tuned 7B open models matching or exceeding GPT-4o, plus an ablation identifying self-reflection as the most impactful individual stage

## Method

TISER runs a four-stage loop per question: (I) generate an initial CoT reasoning trace; (II) extract temporal events from that trace and the context and organize them into an explicit ordered timeline; (III) reflect by comparing the reasoning trace against the timeline to detect inconsistencies/errors, producing a revised reasoning trace; repeating stages II-III until the reasoning and timeline are consistent; then (IV) generate the final answer from the refined reasoning and timeline. To fine-tune smaller models on this pipeline, a synthetic training dataset is constructed by using an off-the-shelf LLM (DeepSeek V2.5 or GPT-4o) to generate TISER-formatted traces (tagged <reasoning>/<timeline>/<reflection>/<answer>) for existing temporal-reasoning benchmark questions (TGQA, TempReason, TimeQA), keeping only samples where the LLM-generated answer matches the gold answer; models are then LoRA-fine-tuned on this filtered, tagged data. Evaluated on in-domain test splits of TGQA/TempReason(L2/L3)/TimeQA plus two out-of-distribution benchmarks -- Test-of-Time (ToT, a symbolic temporal reasoning benchmark) and MultiHopRAG (a broad-domain RAG QA task) -- across closed (GPT-4o) and open (Mistral-7B, Qwen2.5-7B) models, both off-the-shelf (prompting only) and fine-tuned.

## Results

Applying TISER prompting alone (no fine-tuning) improves GPT-4o's macro-average EM/F1 from 78.5/87.2 to 81.8/89.8, and substantially improves off-the-shelf open models on some benchmarks (e.g. Qwen2.5-7B TempReason L2/L3 EM rises from 51.0/40.1 to 55.2/51.6) but not uniformly -- e.g. Mistral-7B's TempReason(L2) EM is higher with standard prompting (22.0%) than TISER (20.8%), attributed to the model not being trained to follow the self-reflection framework. Fine-tuning on TISER-formatted data (generated via GPT-4o) with TISER-style inference yields the largest gains: Qwen2.5-7B's macro-average EM/F1 rises from 25.2/27.8 (off-the-shelf standard prompting) to 91.1/94.4, exceeding GPT-4o's macro average (78.5-81.8 EM) and beating the prior state-of-the-art TG-LLM (57.4 macro EM) by a wide margin; Mistral-7B similarly reaches 84.5-88.7 macro EM after fine-tuning, up from 15.1-25.2 off-the-shelf. Joint fine-tuning across all three source datasets (TGQA+TempReason+TimeQA combined) outperforms fine-tuning on any single subset for every individual test set (macro average 91.1% vs. 72.5-77.6% for single-subset fine-tuning), indicating cross-task transfer. Ablation (removing reasoning, timeline construction, or reflection individually) shows reflection is the single most important stage: reasoning+timeline-without-reflection reaches only 70.5% macro average versus 91.1% for the full pipeline, and reasoning-alone or timeline-alone reach 70.0%/68.0% respectively -- all substantially above the no-reasoning standard-prompt baseline (54.3%) but well below the full combination. On out-of-distribution benchmarks, fine-tuned Qwen2.5-7B with TISER reaches 68.5% EM on Test-of-Time (symbolic temporal reasoning, versus 22.5% off-the-shelf-TISER and 18.0% off-the-shelf-standard) and improves specifically on temporal-category queries in MultiHopRAG (33.5% vs. 27.3% for standard fine-tuning) while preserving performance on non-temporal (inference, comparison) query types.

## Limitations

The multi-stage inference pipeline increases the number of tokens generated at test time, adding computational overhead versus standard prompting or plain CoT. The approach depends on training datasets with detailed intermediate reasoning traces (timeline, reflection), which may not be readily available in every domain, requiring synthetic data generation via another LLM as done here. TISER currently focuses exclusively on text-only temporal reasoning; other forms of abstract or multi-modal temporal reasoning are left to future work.

## Why it matters here

- **overthinking**: Relevant as a positive test-time-scaling case study with an explicit efficiency-vs-accuracy trade-off acknowledged by the authors: TISER extends the reasoning trace length via structured self-reflection to fix a specific failure mode (temporal inconsistency), and the paper's own Limitations section names the added token/compute overhead as a direct cost of this longer, multi-stage reasoning process -- a concrete instance of the general tension the overthinking topic studies, here resolved in favor of the longer trace because the accuracy gains (e.g. macro EM 25.2% to 91.1% after fine-tuning) are judged to outweigh the extra inference cost for this task.

## Entities

- **Concepts**: Temporal Self-Reflective Prompting (TISER), explicit timeline construction, iterative self-reflection loop, test-time scaling for temporal reasoning
- **Methods**: Temporal Self-Reflective Prompting (TISER), [LoRA fine-tuning](../../../../wiki/methods/lora-fine-tuning.md), synthetic reasoning-trace generation with answer-consistency filtering
- **Datasets**: TGQA, TempReason (L2, L3), TimeQA (easy, hard), Test-of-Time (ToT, out-of-distribution), MultiHopRAG (out-of-distribution)

Tags: `overthinking`, `test-time-scaling`, `temporal-reasoning`, `self-reflection`, `fine-tuning`

## Abstract

Large Language Models (LLMs) have emerged as powerful tools for generating coherent text, understanding context, and performing reasoning tasks. However, they struggle with temporal reasoning, which requires processing time-related information such as event sequencing, durations, and inter-temporal relationships. These capabilities are critical for applications including question answering, scheduling, and historical analysis. In this paper, we introduce TISER, a novel framework that enhances the temporal reasoning abilities of LLMs through a multi-stage process that combines timeline construction with iterative self-reflection. Our approach leverages test-time scaling to extend the length of reasoning traces, enabling models to capture complex temporal dependencies more effectively. This strategy not only boosts reasoning accuracy but also improves the traceability of the inference process. Experimental results demonstrate state-of-the-art performance across multiple benchmarks, including out-of-distribution test sets, and reveal that TISER enables smaller open-source models to surpass larger closed-weight models on challenging temporal reasoning tasks.

---

Record id: `doi:10.18653/v1/2025.acl-long.1358`
