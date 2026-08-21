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

Introduces FineHarm, a 29K prompt-response dataset with token-level harmfulness annotations, and the Streaming Content Monitor, a moderator trained on both response- and token-level labels that reads an LLM's output stream and reaches 0.95+ macro F1 after seeing on average the first 18% of tokens.

## Problem

Deployed LLM products place a moderation model after the model as an external guardrail. Conventional moderators do full detection: they judge harmfulness from the complete output, so the user waits for the whole response to be generated before anything can be blocked, which adds service latency and means harmful text has already been produced. Partial detection — watching the stream and stopping generation as soon as harm is detected — addresses that, but prior work takes moderators trained on complete responses and applies them to prefixes. That creates a training-inference gap: the model was never supervised on incomplete text and its judgements on prefixes are correspondingly worse. What is missing is supervision at the right granularity, since a response-level label says nothing about where in the response harm begins.

## Contributions

- FineHarm, a 29K prompt-response dataset with fine-grained token-level harmfulness annotations supporting token-level training.
- The Streaming Content Monitor, trained under dual response- and token-level supervision to judge harmfulness natively on incomplete output rather than on complete responses.
- Evidence of 0.95+ macro F1 comparable to full detection while observing on average the first 18% of tokens, with over 80% of harmful responses caught within the first 30%.
- Use of SCM as a pseudo-harmfulness annotator for token-level DPO, reporting higher harmlessness than standard DPO at comparable helpfulness on PKU-SafeRLHF.

## Method

Two halves, data and model. The data half is FineHarm: 29K prompt-response pairs annotated at token level, so that training can supervise not just whether a response is harmful but from which point it becomes so. The annotation pipeline is heuristic and part-of-speech based. The model half is the Streaming Content Monitor, trained under dual supervision from both the response-level label and the token-level labels. Because it has seen where harm starts, SCM can be run over the generated stream token by token, emitting a harmfulness judgement as the response unfolds and triggering an early stop as soon as the judgement crosses threshold, rather than waiting for the response to complete. A secondary use follows from the same token-level output: SCM's per-token predictions serve as a pseudo-annotator of harmfulness, which is used to supply token-level preference signal for safety alignment.

## Results

SCM is built on Qwen2.5 at 0.5B, 1.5B and 7B, with ModernBERT (0.4B) for comparison. It reaches 0.95+ macro F1, described as comparable to full detection, while seeing on average only the first 18% of response tokens. The distribution behind that average: over 80% of harmful responses are caught within the first 30% of tokens and roughly 50% within the first 10%. Baselines are full-detection moderators — HateBERT, ToxDectRoBERTa, Google Perspective API, OpenAI Moderation API, and LlamaGuard-3-8B. On safety alignment, token-level DPO using SCM annotations reports a higher harmlessness score than standard DPO on PKU-SafeRLHF at comparable helpfulness. Two qualifications on the headline. The 18% figure is a mean over a skewed distribution, so the tail — the responses whose harm only becomes visible late — is where the latency saving is smallest and is not summarised by the mean. And the 0.95+ macro F1 is on FineHarm, the paper's own dataset, built by the same POS-based heuristic that supplied the training labels; ToxicChat and ToxiGen are the independent check.

## Limitations

Stated: the heuristic part-of-speech-based annotation may miss complex semantic factors, so the token-level labels are approximate; performance depends on how representative the training data is; and the safety-alignment application is preliminary and needs further optimisation. Beyond what is stated: FineHarm is both the training set and the principal evaluation set, and its labels come from the same heuristic pipeline, which flatters in-distribution numbers — the ToxicChat and ToxiGen results carry the generalization claim. Early stopping is irreversible in a way full detection is not: a response cut off at 18% on a false positive is destroyed rather than merely flagged, and the cost asymmetry between false positives and false negatives is different for streaming than for post-hoc moderation. A macro F1 aggregate does not show that tradeoff. The monitor also runs alongside generation, so its own compute cost partly offsets the latency it saves, and the comparison of end-to-end latency against a full-detection pipeline is the number a deployment would want.

## Why it matters here

- **overthinking**: A keyword false positive. The match was on 'early stopping', but the phrase here means terminating generation because the content is harmful, not because the reasoning is complete. The topic concerns how long a reasoning model should think — reasoning length, test-time compute, and stopping when the problem has been solved rather than continuing to spend tokens. This paper is content moderation: the stopping criterion is a safety classifier's judgement about the text, the quantity being saved is service latency and exposure to harmful output, and nothing in it involves reasoning traces, chain of thought, answer correctness, or the accuracy/length tradeoff. A reasoning model would be stopped by SCM regardless of whether its reasoning was finished, which is the opposite of what the topic asks about. The only shared structure is mechanical — both are decisions to halt decoding partway, made by a monitor reading the stream — and the paper's finding that a prefix carries enough signal for a confident judgement after 18% of tokens is a fact about harmfulness classification, not about whether an answer has been reached. There is no substantive connection to record. Worth noting for the keyword list that 'early stopping' is standard vocabulary in both moderation and optimisation and will keep producing matches of this kind.

## Entities

- **Concepts**: full detection versus partial detection in moderation, training-inference gap from supervising on complete responses only, token-level harmfulness annotation, streaming judgement and early termination of generation, moderation latency, pseudo-harmfulness annotation for alignment
- **Methods**: Streaming Content Monitor (SCM), FineHarm dataset construction with POS-based token-level annotation, dual response-level and token-level supervision, partial (streaming) detection versus full detection, token-level DPO using SCM as pseudo-annotator
- **Datasets**: FineHarm (constructed here; 29K prompt-response pairs with token-level annotations), ToxicChat (out-of-distribution evaluation), ToxiGen (out-of-distribution evaluation), PKU-SafeRLHF (safety alignment experiment)

Tags: `content-moderation`, `llm-safety`, `guardrails`, `streaming-detection`, `token-level-annotation`, `dpo`, `inference-latency`, `not-llm-reasoning`

## Abstract

Abstract Though safety alignment has been applied to most large language models (LLMs), LLM service providers generally deploy a subsequent moderation as the external safety guardrail in real-world products. Existing moderators mainly practice a conventional full detection, which determines the harmfulness based on the complete LLM output, causing high service latency. Recent works pay more attention to partial detection where moderators oversee the generation midway and early stop the output if harmfulness is detected, but they directly apply moderators trained with the full detection paradigm to incomplete outputs, introducing a training-inference gap that lowers the performance. In this paper, we explore how to form a data-and-model solution that natively supports partial detection. For the data, we construct FineHarm , a dataset consisting of 29K prompt-response pairs with fine-grained token-level annotations to provide reasonable supervision for token-level training. Then, we propose the Streaming Content Monitor (SCM) , which is trained with dual supervision of response- and token-level labels and can follow the output stream of LLM to make a timely judgment of harmfulness. Experiments show that SCM gains 0.95+ in macro F1 score that is comparable to full-detection, by only seeing the first 18% of tokens in responses on average. Moreover, the SCM can serve as a pseudo-harmfulness annotator for improving safety alignment and lead to a higher harmlessness score than DPO.

---

Record id: `title:09cd451102b203a7`
