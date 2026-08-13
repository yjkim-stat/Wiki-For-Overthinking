<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Test-Time Scaling for CAD Generation via Verifier-Free Consensus Selection

- **Authors**: Aaron Haag, Altay Kaçan, Bertram Fuchs, Oliver Lohse
- **Venue**: cs.CE
- **Published**: 2026-08-10
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.09706>
- **PDF**: <https://arxiv.org/pdf/2608.09706v1>
- **Topics**: test-time-scaling
- **Relevance score**: test-time-scaling 0.57

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large language models can write parametric CAD programs from a natural-language description (text-to-CAD generation), but a single sample is often wrong. Increasing test-time compute by sampling multiple candidates only helps if a good candidate can be identified, yet no ground-truth model is available at generation time. Existing systems often require a separate verifier, such as a vision-language judge, to select among candidates. We investigate whether the candidate pool itself provides enough signal for effective selection and a verifier-free alternative. We introduce 3D CAD consensus selection, hereafter consensus selection: sample $N$ parametric CAD programs, compile them to 3D models, and return the candidate that agrees most with the rest of the pool. The method is training-free and compatible with existing CAD agents. We investigate geometric and topological notions of agreement, each of which improves its corresponding evaluation metric. On the exact candidate pools of a state-of-the-art CAD generation method, geometric consensus improves all three geometric metrics over the method's verifier, while topological consensus matches it on topology. Across every tested LLM and prompt variant, geometric consensus also improves geometric accuracy over random selection from the same pool, reducing Chamfer distance by $1-10\%$.

---

Record id: `arxiv:2608.09706`
