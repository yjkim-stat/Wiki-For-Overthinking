<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Reproducing and Stress-Testing Two Approaches to LLM Reasoning Reliability: Test-Time Probability Aggregation and Logic-Representation Editing

- **Authors**: Minhan Cho, Jimin Kweon
- **Venue**: cs.AI
- **Published**: 2026-08-09
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.08514>
- **PDF**: <https://arxiv.org/pdf/2608.08514v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.50, test-time-scaling 0.25

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

We independently reproduce two recent methods for making large language model (LLM) reasoning more reliable, and stress-test them across domains and models (RPC across four new task domains with Qwen3-8B, LCF across four 7-8B models). The first, RPC, aggregates token probabilities and self-consistency at inference; the second, LCF, trains projectors that split hidden states into "content" and "logic" and edits the logic part toward a valid region. Validating such reliability claims matters because the original evaluations are run by each method's own authors and were never independently reproduced or stress-tested across models and domains, and LCF shipped no public code. We re-run RPC's published-path aggregation and re-implement LCF's projector, contrastive, and intervention pipeline, then extend both to text-to-SQL, legal extraction, fallacy identification, and precedent grading, and probe LCF's representation directly. RPC reproduces the original grid exactly on the authors' released reasoning paths; on four new domains its edge over self-consistency is never significant (ties or small mixed differences, paired p >= 0.28), and on BIRD, the one domain where we vary the budget, the edge grows with K as predicted but its largest gap (+2.5 accuracy at K=32, p=0.16) reverses to -0.25 when we enlarge the sample to n=200. LCF's logic-validity direction is real but weak (0.82 separability at the single best sub-layer versus 0.95 for a semantic-attribute control); its one positive effect (Qwen3 $Δ$Prob) is not significant (p=0.56), while it significantly reduces $Δ$Prob on two of the other three models.

---

Record id: `arxiv:2608.08514`
