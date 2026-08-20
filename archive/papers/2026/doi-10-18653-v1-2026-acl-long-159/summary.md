<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Make Mechanistic Interpretability Auditable: A Call to Develop Guidelines via Continuous Collaborative Reviewing

- **Authors**: Michael Lan, Narmeen Fatimah Oozeer, Chaithanya Bandi, Philip Quirke, Austin Meek, Fazl Barez, Amir Abdullah
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.159>
- **DOI**: 10.18653/V1/2026.ACL-LONG.159
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.50

## In one line

A position paper arguing mechanistic interpretability cannot be used in safety-critical settings until its findings are auditable, and proposing continuous collaborative reviewing plus source-based claim tracking.

## Problem

Mechanistic interpretability has produced insights but has no standardized system for auditing experiments, so its findings go unused in safety-critical applications such as medical AI and autonomous systems where stakeholders must certify validity. The paper grounds this concretely: two papers reached conflicting conclusions about the same behaviour, and a third found both were partially correct but incomparable because of methodological inconsistencies. Without standardized auditing such ambiguities block adoption where correctness guarantees are required.

## Contributions

- A diagnosis that mechanistic interpretability lacks auditability and that this blocks safety-critical adoption
- A documented case where two papers conflicted on one behaviour and a third found both partially correct but incomparable
- A proposal for continuous reviewing on a collaborative platform hosting critiques, negative results, reproductions and partial results
- A proposal to generalize platform practice into expert-verified guidelines and protocols
- A proposal for source-based auditing that tracks which arguments each claim depends on

## Method

Three proposals complementing peer review. First, continuous reviewing on a Collaborative Reviewing Platform where meta-science results that do not fit into papers — critiques, negative results, post-hoc extensions, reproductions, replications, partial results — are organized and discussed, with comments and revisions possible at any time. Second, generalizing good practices found there into expert-verified guidelines and protocols. Third, source-based auditing systems that track which arguments a claim depends on, so a claim's support can be inspected rather than assumed.

## Results

A position paper. It provides early concrete examples to catalyze discussion rather than empirical results.

## Limitations

No empirical evaluation; the proposals are untested. The diagnosis rests on one documented case of conflicting conclusions rather than a survey of how often the problem occurs. Continuous reviewing platforms depend on sustained community participation, which the paper cannot demonstrate. Expert-verified guidelines require an authority to verify them, and who does so is not settled.

## Why it matters here

- **reasoning-interpretability**: Names the exact failure this archive has already recorded independently: two interpretability papers reaching opposite conclusions about the same behaviour, incomparable because they shared no model or method. The archive holds its own instance in the MI-Peaks versus commitment-boundary collision, where the two agree on which discourse markers matter and disagree on what that means, with no shared model between them. So this paper's premise is confirmed by evidence collected here, which raises it above the usual position paper. Its source-based claim tracking is also close to what this archive's wiki does — evidence counts per concept, claims traceable to the summaries that support them — which makes it a useful external check on that design.

## Entities

- **Concepts**: mechanistic interpretability, [reproducibility](../../../../wiki/concepts/reproducibility.md), [auditability](../../../../wiki/concepts/auditability.md), [meta-evaluation](../../../../wiki/concepts/meta-evaluation.md), methodological inconsistency, negative results, AI governance
- **Methods**: continuous collaborative reviewing, source-based auditing, protocol standardization
- **Datasets**: _none recorded_

Tags: `position paper`, `interpretability`, `auditing`, `reproducibility`, `governance`

## Abstract

While mechanistic interpretability (MI) has produced important insights into neural network internals, the field has yet to establish a standardized system to audit experiments. As such, many of its findings remain underutilized in safety-critical applications such as medical AI and autonomous systems, as stakeholders cannot certify their validity. Recent work demonstrates this concretely: two papers found conflicting conclusions for the same behavior, and a third study revealed that both were partially correct but incomparable due to methodological inconsistencies. Without standardized auditing, such ambiguities hinder adoption in high-stakes contexts requiring strong correctness guarantees. We call for the MI community to work towards developing a novel reviewing system that complements peer review via: (1) Continuous reviewing supported by a \emph{Collaborative Reviewing Platform} where meta-science results and discussions (such as critiques, negative results, post-hoc extensions, reproductions, replications, and partial results) that fit outside of papers are organized and discussed, allowing for comments and revisions to be made at any time (2) Generalizing good practices found on this platform into expert-verified guidelines and protocols to improve auditing efficiency, and (3) Source-based auditing systems that track arguments which claims depend on. This position paper encourages constructive debate over the necessity, design and implementation of such a framework, providing early concrete examples to help catalyze these dialogues. Overall, we propose that auditing MI itself is essential for its application in AI safety, industry, and governance.

---

Record id: `doi:10.18653/v1/2026.acl-long.159`
