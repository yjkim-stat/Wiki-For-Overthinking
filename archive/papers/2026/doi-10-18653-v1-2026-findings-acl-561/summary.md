<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Follow the Path: Reasoning over Knowledge Graph Paths to Improve Large Language Model Factuality

- **Authors**: Mike Zhang, Johannes Bjerva, Russa Biswas
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.561/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.561.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.561
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

We introduce fs1, a simple yet effective method that improves the factuality of reasoning traces by sourcing them from large reasoning models and grounding them by conditioning on knowledge graph (KG) paths. We fine-tune eight instruction-tuned Large Language Models (LLMs) on 3.9K factually grounded reasoning traces and rigorously evaluate them on six complex open-domain question-answering (QA) benchmarks encompassing 23.9K questions. Our results demonstrate that our fs1-tuned model consistently outperforms instruction-tuned counterparts with parallel sampling by 6-14 absolute points (pass@). Our detailed analysis shows that fs1 considerably improves model performance over more complex questions (requiring 3 or more hops on KG paths) and numerical answer types compared to the baselines. Furthermore, in single-pass inference, we notice that smaller LLMs show the most improvements. While prior works demonstrate the effectiveness of reasoning traces primarily in the STEM domains, our work shows strong evidence that anchoring reasoning to factual KG paths is a critical step in transforming LLMs for reliable knowledge-intensive tasks.

---

Record id: `doi:10.18653/v1/2026.findings-acl.561`
