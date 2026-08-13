<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Scaling Evaluation-Time Compute with Reasoning Models as Evaluators

- **Authors**: Seungone Kim, Ian Wu, Jinu Lee 0001, Xiang Yue, Seongyun Lee, Minkyeong Moon, Carolin Lawrence, Kiril Gashteovski, Julia Hockenmaier, Graham Neubig, Sean Welleck
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.findings-acl.2102>
- **DOI**: 10.18653/V1/2026.FINDINGS-ACL.2102
- **Topics**: reasoning-training, test-time-scaling
- **Relevance score**: reasoning-training 0.67

## In one line

Shows evaluator accuracy improves monotonically with reasoning tokens spent, and that buying compute at evaluation time can substitute for buying it at generation time.

## Problem

LM evaluators that generate CoT are widely used to assess responses, and scaling test-time compute is known to help solve hard problems. Whether the same scaling improves an LM's evaluation capability, as opposed to its problem-solving, had not been tested.

## Contributions

- The question of whether test-time compute scaling improves evaluation as well as problem-solving, and an affirmative answer
- Scaling of evaluation-time compute for both outcome evaluation and step-level process evaluation
- The finding that evaluator performance improves monotonically with reasoning tokens generated
- Demonstration that evaluation-time compute can be as effective as generation-time compute for improving problem-solving via reranking

## Method

Reasoning models — LMs that natively generate long CoT — are employed as evaluators. Evaluation-time compute is scaled for two targets: the overall candidate response (outcome evaluation) and the individual reasoning steps within it (process evaluation). The resulting more accurate evaluators are then used to rerank multiple generations, which converts an evaluation improvement into a problem-solving improvement and makes the two compute budgets directly comparable.

## Results

Evaluator performance improves monotonically with the number of reasoning tokens generated, mirroring trends seen in LM reasoning. Spending more compute at evaluation time is shown to be as effective as increasing compute during generation for improving problem-solving performance.

## Limitations

No numbers, models or benchmarks are named in the abstract. Monotonic improvement is reported without a stated saturation point, so the range over which it holds is unclear. The equivalence between evaluation-time and generation-time compute is an aggregate claim; whether it holds per task type or per difficulty level is not reported. Reranking gains are bounded by the candidate pool, so evaluation compute cannot exceed what generation produced.

## Why it matters here

- **reasoning-training**: Reframes a question this archive treats as settled — where inference compute should go. The verifier side has been assumed fixed while generation is scaled, and this shows the verifier scales too, at a comparable exchange rate. That makes the archive's best-of-N and process-reward results potentially compute-mismatched, since a weak verifier over many samples and a strong verifier over few are different points on one budget. It also gives a cheap path to better process supervision without training a reward model: spend more tokens judging. The absence of a saturation point is the gap, because the whole claim is about an exchange rate that must eventually break.

## Entities

- **Concepts**: [test-time compute](../../../../wiki/concepts/test-time-compute.md), test-time scaling, [meta-evaluation](../../../../wiki/concepts/meta-evaluation.md), process evaluation, [verification](../../../../wiki/concepts/verification.md), best-of-n, [judge reliability](../../../../wiki/concepts/judge-reliability.md), [compute allocation](../../../../wiki/concepts/compute-allocation.md)
- **Methods**: [LLM-as-a-judge](../../../../wiki/methods/llm-as-a-judge.md), reranking, [best-of-n](../../../../wiki/methods/best-of-n.md), [process evaluation](../../../../wiki/methods/process-evaluation.md), outcome evaluation
- **Datasets**: _none recorded_

Tags: `evaluation-time compute`, `llm-as-a-judge`, `test-time scaling`, `reranking`, `process evaluation`

## Abstract

As language model (LM) outputs get more and more natural, it is becoming more difficult than ever to evaluate their quality. Simultaneously, increasing LMs'"thinking"time through scaling test-time compute has proven an effective technique to solve challenging problems in domains such as math and code. This raises a natural question: can an LM's evaluation capability also be improved by spending more test-time compute? To answer this, we investigate employing reasoning models-LMs that natively generate long chain-of-thought reasoning-as evaluators. Specifically, we examine methods to leverage more test-time compute by (1) using reasoning models, and (2) prompting these models to evaluate not only the response as a whole (i.e., outcome evaluation) but also assess each step in the response separately (i.e., process evaluation). In experiments, we observe that the evaluator's performance improves monotonically when generating more reasoning tokens, similar to the trends observed in LM-based generation. Furthermore, we use these more accurate evaluators to rerank multiple generations, and demonstrate that spending more compute at evaluation time can be as effective as using more compute at generation time in improving an LM's problem-solving capability.

---

Record id: `doi:10.18653/v1/2026.findings-acl.2102`
