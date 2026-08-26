<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Scaling Evaluation-Time Compute with Reasoning Models as Evaluators

- **Authors**: Seungone Kim, Ian Wu, Jinu Lee, Xiang Yue, Seongyun Lee, Minkyeong Moon, Carolin Lawrence, Kiril Gashteovski, Julia Hockenmaier, Graham Neubig, Sean Welleck
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.2102/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.2102.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.2102
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Language model (LM) evaluators that generate chain-of-thought (CoT) reasoning are widely used for the assessment of LM responses. Simultaneously, increasing LMs’ “thinking” time through scaling test-time compute has proven to be an effective technique for solving challenging problems in domains such as math and code. This raises a natural question: can an LM’s evaluation capability also be improved by scaling test-time compute? To answer this, we investigate employing reasoning models - LMs that natively generate long CoT reasoning - as evaluators. We explore scaling evaluation-time compute by using reasoning models to evaluate both the overall candidate response (i.e., outcome evaluation) and the individual reasoning steps within it (i.e., process evaluation). We observe that evaluator performance improves monotonically with the number of reasoning tokens generated, mirroring trends seen in LM reasoning. Furthermore, we use these more accurate evaluators to rerank multiple generations, and demonstrate that spending more compute at evaluation time can be as effective as increasing compute during generation for improving an LM’s problem-solving performance.

---

Record id: `doi:10.18653/v1/2026.findings-acl.2102`
