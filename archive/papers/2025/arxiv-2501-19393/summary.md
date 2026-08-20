<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# s1: Simple test-time scaling

- **Authors**: Niklas Muennighoff, Zitong Yang, Weijia Shi, Xiang Lisa Li, Li Fei-Fei, Hannaneh Hajishirzi, Luke Zettlemoyer, Percy Liang, Emmanuel Candès, Tatsunori Hashimoto
- **Venue**: cs.CL
- **Published**: 2025-01-31
- **Source**: seed
- **Link**: <https://arxiv.org/abs/2501.19393>
- **PDF**: <https://arxiv.org/pdf/2501.19393v3>
- **Topics**: test-time-scaling
- **Relevance score**: reasoning-evaluation 0.25, reasoning-faithfulness 0.25, test-time-scaling 0.62

## In one line

Reaches test-time scaling with two simple ingredients: supervised finetuning on 1,000 curated reasoning traces, and 'budget forcing', which controls thinking length by cutting generation off or appending 'Wait' to extend it.

## Problem

Test-time scaling was demonstrated by a closed model whose methodology was not shared, prompting replication efforts. The question the paper sets itself is what the simplest sufficient recipe is.

## Contributions

- s1K, a 1,000-question dataset with reasoning traces, curated against three criteria — difficulty, diversity and quality — each validated by ablation.
- Budget forcing, a decoding-time control that terminates the thinking process to shorten it or appends 'Wait' when the model tries to stop, to lengthen it.
- The observation that appending 'Wait' often makes the model double-check and fix incorrect reasoning steps.
- s1-32B, the resulting model, released open-source with data and code.

## Method

Qwen2.5-32B-Instruct is supervised-finetuned on the 1,000-example s1K set, then equipped with budget forcing at inference: generation of the thinking block is either cut short to impose a smaller budget, or extended by suppressing the end-of-thinking token and appending the literal token 'Wait', prompting continued deliberation. The three curation criteria are validated by ablating each.

## Results

s1-32B exceeds o1-preview on competition math (MATH and AIME24) by up to 27%. Scaling s1-32B with budget forcing extrapolates beyond its own no-intervention performance, from 50% to 57% on AIME24. Summarized from the abstract alone, so the figures below are only those the abstract states; the paper's full evaluation is not represented here.

## Limitations

Not discussed in the abstract. Bounds a reader should note: the extrapolation result is a 7-point move on AIME24, a 30-problem set, so the absolute counts are small; and budget forcing works by appending a specific token, which makes it a property of a model that has learned to treat that token as a cue rather than a general control mechanism.

## Why it matters here

- **test-time-scaling**: The paper that made the topic's central knob explicit and trivially reproducible: chain length is a dial, and it can be turned in both directions with no training and no verifier. That framing is what most archived work here operates on — early exit turns the dial down with a statistical stopping rule, trajectory weighting turns it up and then selects, and the overthinking literature exists because the dial has a wrong end. The 50% to 57% extrapolation on AIME24 is also the topic's cleanest demonstration that a fixed model has performance above what it reaches when left alone. Its 'Wait' mechanism connects directly to the archive's faithfulness side, where injecting a doubt cue recovers about 15% of failed trajectories and where 'wait' is measured as the most frequent marker of verbalized uncertainty — the same token doing the same work, arrived at from two different directions.

## Entities

- **Concepts**: test-time scaling, budget forcing, thinking budget, data curation, difficulty diversity and quality, extrapolation beyond baseline performance
- **Methods**: [budget forcing](../../../../wiki/methods/budget-forcing.md), [supervised finetuning](../../../../wiki/methods/supervised-fine-tuning.md), s1
- **Datasets**: s1K, [MATH](../../../../wiki/datasets/math.md), [AIME24](../../../../wiki/datasets/aime-2024.md)

Tags: `s1`, `budget forcing`, `test-time scaling`, `sft`, `data curation`, `wait token`

## Abstract

Test-time scaling is a promising new approach to language modeling that uses extra test-time compute to improve performance. Recently, OpenAI's o1 model showed this capability but did not publicly share its methodology, leading to many replication efforts. We seek the simplest approach to achieve test-time scaling and strong reasoning performance. First, we curate a small dataset s1K of 1,000 questions paired with reasoning traces relying on three criteria we validate through ablations: difficulty, diversity, and quality. Second, we develop budget forcing to control test-time compute by forcefully terminating the model's thinking process or lengthening it by appending "Wait" multiple times to the model's generation when it tries to end. This can lead the model to double-check its answer, often fixing incorrect reasoning steps. After supervised finetuning the Qwen2.5-32B-Instruct language model on s1K and equipping it with budget forcing, our model s1-32B exceeds o1-preview on competition math questions by up to 27% (MATH and AIME24). Further, scaling s1-32B with budget forcing allows extrapolating beyond its performance without test-time intervention: from 50% to 57% on AIME24. Our model, data, and code are open-source at https://github.com/simplescaling/s1

---

Record id: `arxiv:2501.19393`
