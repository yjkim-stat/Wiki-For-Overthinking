<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Monte Carlo Tree Search for Table-to-Multimodal Report Generation

- **Authors**: Teng Lin, Zhiyang Zhang, Yuyu Luo, Nan Tang
- **Venue**: cs.AI
- **Published**: 2026-08-04
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.04071>
- **PDF**: <https://arxiv.org/pdf/2608.04071v1>
- **Topics**: test-time-scaling
- **Relevance score**: test-time-scaling 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Automatically generating professional multimodal reports comprising both textual analysis and visual charts from structured tabular data is a critical challenge in data intelligence. Existing methods suffer from fixed linear pipelines and isolated subtask processing, which hinder joint optimization of factual accuracy, visual quality, and narrative coherence. To address these issues, this paper proposes MCTS-Report, a Monte Carlo Tree Search (MCTS)-driven framework that formulates multimodal table-to-report generation as a progressive construction process over a structured search space. The core idea is to decompose report generation into atomic actions, including chapter planning, visualization task identification, chart generation, insight organization, and narrative refinement, each executed by an LLM based on dynamic reasoning conditioned on the current report state. We use an LLM to generate step-by-step reasoning and actions during MCTS, storing the reasoning trajectory in each node for context-aware, coherent report construction. To guide the search, we design a multi-dimensional reward function that jointly evaluates numerical fact consistency (via SQL), chart quality, chart-text alignment, and structural completeness, while incorporating a diversity penalty to suppress repeated charts and a precondition check to prune invalid actions. We also construct MMRBench, a comprehensive benchmark comprising real-world tables from six domains, paired with expert-refined reference report structures and verifiable key insights. Experiments on MMRBench demonstrate that MCTS-Report significantly outperforms strong baselines across structural completeness, numerical accuracy, chart-text alignment, and insight novelty, achieving a 77.9 overall score.

---

Record id: `arxiv:2608.04071`
