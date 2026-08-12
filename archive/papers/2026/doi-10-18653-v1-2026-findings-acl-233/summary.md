<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# MAC-Reasoner: A Multi-Agent Collaborative Framework for Enhancing Logical Reasoning in Large Language Models

- **Authors**: Yehua Lin, Liping Zheng, Yin Chen
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.findings-acl.233>
- **DOI**: 10.18653/V1/2026.FINDINGS-ACL.233
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.50

## In one line

Keeps the LLM as the reasoner while a symbolic solver supplies a Logic-Augmented Context, so conflicts flagged by execution direct attention to violated constraints instead of replacing deduction.

## Problem

Logical reasoning demands strict deductive correctness. Purely model-based approaches hallucinate, while neuro-symbolic methods delegate deduction to external solvers and reduce the LLM to a translator — which forfeits the model's reasoning rather than improving it.

## Contributions

- The argument that neuro-symbolic delegation reduces the LLM to a translator and forfeits its reasoning
- MAC-Reasoner, a multi-agent framework constructing a Logic-Augmented Context from solver execution
- Use of solver output as a verification reference where logical conflicts direct attention to violated constraints
- Consistent improvements with three backbones on four challenging benchmarks
- Demonstration that the resulting traces serve as SFT data for more accurate and efficient logical reasoning

## Method

MAC-Reasoner is a multi-agent framework building a Logic-Augmented Context. A translator agent converts the problem into an executable symbolic program; symbolic information from solver execution is transformed into the Logic-Augmented Context, serving as a verification reference where logical conflicts trigger heightened attention to violated constraints. The solver informs the model's reasoning rather than substituting for it, which is the distinction from standard neuro-symbolic pipelines. Reasoning traces produced this way are also usable for supervised fine-tuning.

## Results

Evaluated with three backbone LLMs on four challenging benchmarks, MAC-Reasoner shows consistent and robust improvements over baselines. Traces from MAC-Reasoner can be used for SFT to yield more accurate and efficient logical reasoning. No numbers, benchmarks or backbones are named in the abstract.

## Limitations

No quantitative results, benchmark names or backbones in the abstract. Depends on the translator agent producing a faithful symbolic program, which is the standard failure point of neuro-symbolic pipelines and is not evaluated separately here. Requires problems expressible as executable symbolic programs. 'Heightened attention to violated constraints' is described without a stated mechanism.

## Why it matters here

- **reasoning-evaluation**: A thin fit for this topic, which it reached on benchmark vocabulary; it proposes a reasoning method, not an evaluation. What connects it here is the use of a solver as an oracle verifier over intermediate constraints, which is the same free-ground-truth trick that FinChain gets from executable templates and findings-acl.460 gets from the interpreter. Three entries in this drain obtain step-level verification without human annotation, and that is a pattern worth recording, since annotation cost is what limits process evaluation everywhere else in the archive. Its second claim — that the generated traces are usable as SFT data — makes the verifier a source of training signal, closing the loop the archive's process-supervision thread cares about.

## Entities

- **Concepts**: neuro-symbolic reasoning, [verification](../../../../wiki/concepts/verification.md), logical reasoning, [hallucination](../../../../wiki/concepts/hallucination.md), multi-agent collaboration, constraint violation, [self-training](../../../../wiki/concepts/self-training.md)
- **Methods**: MAC-Reasoner, symbolic program execution, multi-agent framework, [supervised fine-tuning](../../../../wiki/methods/supervised-fine-tuning.md)
- **Datasets**: _none recorded_

Tags: `neuro-symbolic`, `logical reasoning`, `multi-agent`, `verification`, `self-training`

## Abstract

,

---

Record id: `doi:10.18653/v1/2026.findings-acl.233`
