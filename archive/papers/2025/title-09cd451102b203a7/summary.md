<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# From Judgment to Interference: Early Stopping LLM Harmful Outputs via Streaming Content Monitoring

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/116186>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Streaming Content Monitor (SCM) is a safety moderator trained with token-level supervision to judge harmfulness of an LLM's output mid-stream and stop generation early, matching full-detection accuracy after seeing only ~18% of the response on average.

## Problem

Safety moderators are normally trained and applied to complete LLM outputs (full detection), causing high latency; recent partial-detection approaches apply the same full-detection-trained moderators to incomplete outputs, creating a training-inference gap that lowers performance.

## Contributions

- FineHarm, a 29K-pair dataset with token-level harmfulness annotations
- Streaming Content Monitor (SCM), a moderator natively trained for partial-output detection
- use of SCM as a pseudo-harmfulness annotator that outperforms DPO for safety alignment

## Method

Constructs FineHarm, a 29K-pair dataset with fine-grained token-level harmfulness annotations, and trains the Streaming Content Monitor (SCM) with dual supervision (response-level and token-level labels) so it natively supports partial detection and can judge harmfulness as the output streams.

## Results

SCM reaches 0.95+ macro F1, comparable to full-detection moderators, while seeing only the first 18% of response tokens on average; used as a pseudo-harmfulness annotator, it also yields a higher harmlessness score than DPO for safety alignment.

## Limitations

Not stated in the abstract beyond the domain (LLM output moderation); no discussion of false-early-stop cases or failure modes when harmful content appears very late in a response.

## Why it matters here

- **overthinking**: Only loosely related: matched on the shared term 'early stopping,' but this is about stopping generation early to block unsafe content, not about reasoning length or the accuracy/efficiency tradeoff the topic tracks; it is a different application of the general idea that a decision can be made from a prefix of a generation rather than the whole thing.

## Entities

- **Concepts**: partial (streaming) content detection, token-level harmfulness supervision, early stopping for safety moderation
- **Methods**: dual response/token-level supervised training, streaming/partial content moderation
- **Datasets**: FineHarm (new, 29K prompt-response pairs)

Tags: `safety-moderation`, `early-stopping`, `streaming-inference`, `guardrail`

## Abstract

Abstract Though safety alignment has been applied to most large language models (LLMs), LLM service providers generally deploy a subsequent moderation as the external safety guardrail in real-world products. Existing moderators mainly practice a conventional full detection, which determines the harmfulness based on the complete LLM output, causing high service latency. Recent works pay more attention to partial detection where moderators oversee the generation midway and early stop the output if harmfulness is detected, but they directly apply moderators trained with the full detection paradigm to incomplete outputs, introducing a training-inference gap that lowers the performance. In this paper, we explore how to form a data-and-model solution that natively supports partial detection. For the data, we construct FineHarm , a dataset consisting of 29K prompt-response pairs with fine-grained token-level annotations to provide reasonable supervision for token-level training. Then, we propose the Streaming Content Monitor (SCM) , which is trained with dual supervision of response- and token-level labels and can follow the output stream of LLM to make a timely judgment of harmfulness. Experiments show that SCM gains 0.95+ in macro F1 score that is comparable to full-detection, by only seeing the first 18% of tokens in responses on average. Moreover, the SCM can serve as a pseudo-harmfulness annotator for improving safety alignment and lead to a higher harmlessness score than DPO.

---

Record id: `title:09cd451102b203a7`
