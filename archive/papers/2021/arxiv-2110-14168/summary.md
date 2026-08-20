<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Training Verifiers to Solve Math Word Problems

- **Authors**: Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, John Schulman
- **Venue**: cs.LG
- **Published**: 2021-10-27
- **Source**: seed
- **Link**: <https://arxiv.org/abs/2110.14168>
- **PDF**: <https://arxiv.org/pdf/2110.14168v2>
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.62

## In one line

Introduces GSM8K, 8.5K grade-school math word problems, and shows that training a verifier to rank many sampled solutions beats finetuning the generator directly.

## Problem

Language models matched human performance on many tasks yet failed at robust multi-step mathematical reasoning, and the abstract notes that even the largest transformers of the time scored poorly on a problem distribution that is conceptually simple. There was no diagnostic dataset isolating that failure.

## Contributions

- GSM8K: 8.5K high-quality, linguistically diverse grade school math word problems, built to diagnose multi-step reasoning failure.
- The finding that model size alone does not solve this distribution.
- Training verifiers to judge the correctness of completions, and using them at test time to rank many sampled candidates.
- Evidence that verification scales better with additional data than a finetuning baseline.

## Method

Many candidate solutions are sampled at test time and a separately trained verifier judges the correctness of each; the highest-ranked candidate is returned. This is contrasted against finetuning the generator to produce the answer directly. The abstract does not give the verifier's architecture, training data construction, or sample count.

## Results

The abstract states that verification significantly improves performance on GSM8K and that it scales more effectively with increased data than the finetuning baseline, but gives no accuracy figures, model sizes or sample counts. Summarized from the abstract alone, so the figures below are only those the abstract states; the paper's full evaluation is not represented here.

## Limitations

Not discussed in the abstract. What a reader of this archive should note is downstream rather than internal: GSM8K has since become a saturated benchmark, and later archived work uses it as the easy rung of a suite and raises contamination concerns about publicly available math benchmarks in general.

## Why it matters here

- **reasoning-evaluation**: The origin of the benchmark that nearly every archived paper reports on, which makes it the reference point for what those numbers mean. Two things matter for this topic. First, its framing: the dataset was built as a diagnostic for a specific failure, not as a leaderboard, and it was designed around problems whose conceptual simplicity makes a low score informative. Second, its fate: a benchmark introduced because large models could not solve it is now the easy end of every suite in this archive, so it is a concrete case study in benchmark saturation and in why a claim resting on GSM8K gains needs a harder companion set. This is also the first paper filed under this topic.

## Entities

- **Concepts**: multi-step mathematical reasoning, [verification](../../../../wiki/concepts/verification.md), generative vs discriminative scaling, sampling and reranking, [benchmark design](../../../../wiki/concepts/benchmark-design.md)
- **Methods**: verifier training, test-time reranking, [supervised finetuning](../../../../wiki/methods/supervised-fine-tuning.md)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md)

Tags: `gsm8k`, `verifier`, `math word problems`, `benchmark`, `reranking`

## Abstract

State-of-the-art language models can match human performance on many tasks, but they still struggle to robustly perform multi-step mathematical reasoning. To diagnose the failures of current models and support research, we introduce GSM8K, a dataset of 8.5K high quality linguistically diverse grade school math word problems. We find that even the largest transformer models fail to achieve high test performance, despite the conceptual simplicity of this problem distribution. To increase performance, we propose training verifiers to judge the correctness of model completions. At test time, we generate many candidate solutions and select the one ranked highest by the verifier. We demonstrate that verification significantly improves performance on GSM8K, and we provide strong empirical evidence that verification scales more effectively with increased data than a finetuning baseline.

---

Record id: `arxiv:2110.14168`
