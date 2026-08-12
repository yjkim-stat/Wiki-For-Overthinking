<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# RFS-Guard: Detecting Reasoning Hallucinations via Cross-Phase Routing Focus in Large Reasoning Models

- **Authors**: Zihang Liu 0001, Zhouhua Fang, Hui Liu, Zhiwei Liu, Yong Li 0004, Haishuai Wang
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.885>
- **DOI**: 10.18653/V1/2026.ACL-LONG.885
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.80

## In one line

Detects reasoning hallucinations by measuring how strongly cross-step attention routing aligns with hidden-state semantic proximity, finding that higher alignment means higher hallucination risk.

## Problem

Reasoning models produce hallucinations such as subtle arithmetic slips or constraint violations. Prior detectors rely on external verification or local token-level signals, and overlook whether the cross-phase information flow from reasoning to answering is structurally robust.

## Contributions

- The Routing Focus Score: alignment between cross-step attention routing and hidden-state semantic proximity as a step-level indicator
- RFS-Guard, a hallucination detector needing no external verification and no repeated sampling
- The empirical association of higher reasoning-to-answer RFS with higher hallucination risk
- A routing-collapse account in which self-confirmation loops suppress self-auditing
- Detection and localization of hallucinations across multiple domains and models

## Method

The Routing Focus Score is a step-level indicator measuring how strongly cross-step attention routing aligns with semantic proximity derived from hidden-state cosine similarity. RFS-Guard is a lightweight detection framework built on RFS. It needs no external tool and no repeated sampling, so detection costs one forward pass.

## Results

Higher reasoning-to-answer RFS is consistently associated with higher hallucination risk, which the authors interpret as a routing-collapse failure mode where the model prefers self-confirmation loops and suppresses its ability to audit its own generation. Across multiple domains and models, RFS-Guard detects and localizes hallucinations without external tools or repeated sampling.

## Limitations

No numbers in the abstract; domains and models are unnamed. The direction of the association is counter-intuitive — more alignment between attention routing and semantic proximity predicts more hallucination — and the routing-collapse account is an interpretation, not a demonstrated mechanism. Association is correlational, so RFS may track a correlate of difficulty rather than hallucination. Requires attention and hidden-state access.

## Why it matters here

- **reasoning-training**: The mechanism it proposes — that a model attending to what it already believes is more likely to be wrong — is a concrete, testable account of why self-verification underperforms, and this archive holds two independent findings that it does (near-zero self-revision content margin, and proof self-reflection failing to fix named errors). If self-confirmation is visible as attention-routing collapse, it is detectable in one forward pass, which is cheaper than any sampling-based check and could serve as a training signal rather than only a monitor. The counter-intuitive sign of the effect is the reason to verify this one before relying on it.

## Entities

- **Concepts**: reasoning hallucination, [attention pattern](../../../../wiki/concepts/attention-pattern.md), information flow, self-confirmation, [verification](../../../../wiki/concepts/verification.md), [localization](../../../../wiki/concepts/localization.md), routing collapse
- **Methods**: Routing Focus Score, RFS-Guard, [attention analysis](../../../../wiki/methods/attention-analysis.md), cosine similarity over hidden states
- **Datasets**: _none recorded_

Tags: `hallucination detection`, `attention routing`, `self-confirmation`, `interpretability`, `verification`

## Abstract

Large reasoning models (LRMs) achieve strong performance on complex tasks by generating intermediate reasoning before the final answer, yet they remain prone to reasoning hallucinations such as subtle arithmetic or constraint-violation errors. Prior hallucination detectors often rely on external verification or local token-level signals, which are limited for LRMs and largely overlook whether the cross-phase information flow from reasoning to answering is structurally robust. We propose Routing Focus Score (RFS), a step-level indicator that measures how strongly cross-step attention routing aligns with semantic proximity derived from hidden-state cosine similarity. We further design RFS-Guard, a lightweight hallucination detection framework based on RFS. Empirically, we observe that higher reasoning–answer RFS is consistently associated with higher hallucination risk, suggesting a routing-collapse failure mode where models might prefer self-confirmation loops and suppress the ability to audit their own generations. Experimental results across multiple domains and models demonstrate the superiority of RFS-Guard for detecting and localizing hallucinations in LRMs without requiring external tools or repeated sampling.

---

Record id: `doi:10.18653/v1/2026.acl-long.885`
