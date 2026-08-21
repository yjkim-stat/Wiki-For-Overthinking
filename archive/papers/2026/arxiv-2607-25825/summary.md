<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# CHILL-Harness: Counterfactual Harness Learning for Efficient Reasoning in Long-Horizon Agents

- **Authors**: Jiarun Fu, Lizhong Ding, Sida Chen, Honglei Xin, Chunhui Zhang, Pengqi Li, Qiuning Wei, Ye Yuan, Guoren Wang
- **Venue**: arXiv
- **Published**: 2026-07-28
- **Source**: semanticscholar
- **Link**: <https://www.semanticscholar.org/paper/00a392559287f448c41d331f0e43694389177348>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Agent harnesses have become the operational infrastructure of modern large language model agents, coordinating context, tools, verification, and execution control to translate latent model capability into reliable long-horizon behavior. However, reliable long-horizon behavior requires harness control to adapt to task demands, execution environments, and evolving execution states, whereas current harnesses predominantly rely on hand-crafted or globally fixed policies; this mismatch manifests as unnecessary computational overhead and, in adverse cases, reduced task success. To address this limitation, we formulate the task of enabling adaptive orchestration in harness systems as a causal learning problem and propose Counterfactual Harness Intervention Learning for Long-Horizon Agents (CHILL-Harness). CHILL-Harness intervenes at the orchestration layer to enable advantage-guided workflow adaptation, thereby improving reasoning and execution efficiency while preserving task performance. Specifically, we develop causal intervention effect learning as the effect-estimation component of CHILL-Harness to estimate intervention-relative workflow advantage from confidence-weighted execution evidence and identify advantageous workflow adaptations. We further introduce advantage-realizing causal orchestration as its realization component to adaptively allocate counterfactual reasoning and realize only workflow adjustments supported by sufficient expected advantage. Finally, we incorporate a success-preserving objective and advantage-margin authorization constraints into CHILL-Harness to promote reliable adaptation. Extensive experiments on heterogeneous long-horizon tasks spanning information seeking, software engineering, and terminal interaction show that CHILL-Harness consistently preserves or improves task success while substantially reducing token consumption and execution time.

---

Record id: `arxiv:2607.25825`
