<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# V-FiLLM: Verified Financial LLM Reasoning Benchmark

- **Authors**: Alicia Larsen, Victoire Laurent, Aulia Kharis Rakhamsari, Lara Turgut, Nino Antulov-Fantulin
- **Venue**: cs.AI
- **Published**: 2026-08-11
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.11047>
- **PDF**: <https://arxiv.org/pdf/2608.11047v1>
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.50, reasoning-training 0.25, test-time-scaling 0.25

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

While existing benchmarks have made substantial progress in evaluating LLMs across STEM domains, financial reasoning over structured data remains comparatively less explored. We introduce V-FiLLM, a framework that generates financial reasoning benchmarks from executable computation trees grounded in real tables, yielding items whose answers are correct by construction. Trees are evaluated symbolically to obtain ground truth and rendered into natural-language questions, removing any model from the labeling loop, so items can be generated at arbitrary scale without annotation cost and without inheriting a generator's error rate. V-FiLLM exposes four independently controllable axes of difficulty including computation depth, expression breadth, financial concept complexity, and context size. By evaluating on open-source models, we find that accuracy falls up to 51% as reasoning depth increases, and up to 47% points under adversarial numerical perturbations, highlighting remaining challenges in robust financial reasoning over tables. We further show that lightweight LoRA fine-tuning on verified chain-of-thought traces improves accuracy from 81.1% to 85.6% on held-out problems and outperforms the base model by 5% points on FinQA (Chen et al., 2022a), s), suggesting that targeted, low-cost adaptation is a promising direction for compositional reasoning in financial QA.

---

Record id: `arxiv:2608.11047`
