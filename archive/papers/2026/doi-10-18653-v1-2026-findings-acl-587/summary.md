<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Distilling the Essence: Efficient Reasoning Distillation via Sequence Truncation

- **Authors**: Wei-Rui Chen, Vignesh Kothapalli, Ata Fatahibaarzi, Hejian Sang, Shao Tang, Qingquan Song, Zhipeng Wang, Muhammad Abdul-Mageed
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.587/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.587.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.587
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

Systematically ablates which section (prompt, CoT, answer) of a reasoning-distillation training sequence carries the useful supervisory signal and how much of the CoT is needed, finding CoT-inclusive supervision is essential while training on only the first 50% of tokens retains ~91% of full-sequence accuracy at roughly half the training time, memory, and FLOPs.

## Problem

Knowledge distillation from large reasoning models (LRMs) to smaller students typically trains on full prompt+CoT+answer sequences, which is computationally expensive over long CoT traces, and it is unclear which segment of the sequence (prompt, CoT, or answer) actually carries the useful supervisory signal, or whether the full trace length is needed at all -- especially given growing evidence that reasoning models 'overthink' with much of the trace's later content being redundant self-verification.

## Contributions

- a controlled section-wise supervision ablation showing CoT tokens are the dominant, near-sufficient carrier of distillation signal, with prompt/answer supervision adding only marginal benefit, explained by a linguistic-entailment analysis showing the CoT already encompasses the prompt and answer's content in the large majority of examples
- the Lead-Span Proportion (LSP) truncation protocol, showing training on only the first 50% of a reasoning trace's tokens retains ~91% of full-sequence downstream accuracy while roughly halving training time, GPU memory, and FLOPs
- a Left-vs-Right 50% ablation and a first-correct-derivation localization analysis showing the useful reasoning signal is concentrated in the early-to-mid portion of the trace (question understanding, ideation, self-reflection, first derivation), while later tokens are dominated by verification and restating an already-correct answer -- positioning sequence truncation as a training-time lens on overthinking, distinct from prior inference-time overthinking mitigation

## Method

Trains seven teacher-student pairs (Qwen3-32B/8B teachers, Qwen3-8B/4B/1.7B/0.6B-Base students) via supervised knowledge distillation (KL-divergence soft loss + cross-entropy hard loss, lambda=0.5) on five long-CoT datasets (OpenThoughts-114k, Bespoke-Stratos-17k, Synthetic-1, Llama-Nemotron, SkyT1-17k), masking the loss to different combinations of the sequence's three sections -- Prompt (P), Chain-of-Thought (CoT), Answer (A) -- to isolate which section's supervision matters (RQ1: six conditions -- A, P+A, CoT, CoT+A, P+CoT, P+CoT+A). Separately, a Lead-Span Proportion (LSP) truncation protocol removes the rightmost (1-p) fraction of tokens from each training example entirely (not just masked from loss, but excluded from the forward pass), varying p from 0.1 to 1.0, to test whether early tokens alone suffice (RQ2), plus a Left-50%-vs-Right-50% ablation to confirm any gain is from token position rather than merely fewer tokens. Evaluated on AIME24/AIME25 with 64-sample budgets via lighteval.

## Results

RQ1: any supervision setting that includes CoT tokens (CoT, CoT+A, P+CoT, P+CoT+A) substantially outperforms settings that exclude CoT (A-only, P+A), with only minor differences among the CoT-inclusive variants -- full P+CoT+A supervision does not reliably beat CoT-only supervision. A GPT-5.1-judged linguistic analysis of 100 sampled examples confirms why: in 99%/89% (OpenThoughts) and 97%/93% (Bespoke) of cases the CoT already semantically entails the prompt/answer respectively, and in 100%/99% of cases the final answer in the CoT matches the answer segment -- the CoT implicitly encompasses the prompt and answer's information. RQ2: accuracy-vs-LSP curves show near-monotonic improvement that saturates well before p=1.0; training on only the first 50% of tokens retains on average ~91% of full-sequence accuracy across 30 settings (3 teacher-student pairs x 5 datasets x 2 benchmarks), with retention as high as ~99% for the 8B-4B pair on AIME25, while cutting training time, GPU memory, and FLOPs by roughly 50% each (a clear inflection point in cost occurs exactly at LSP=0.5, beyond which quadratic attention cost escalates sharply -- e.g. an 8B-4B setting needs a full 80GB H100 at LSP=1.0 but fits a 40GB A100 at LSP=0.5). The Left-50%-vs-Right-50% ablation confirms this is not simply 'fewer tokens is fine': training on the left half consistently and substantially outperforms training on an equal-sized right half across all settings, and training loss on the left half is comparable to full-sequence loss while loss on the right half is markedly higher -- the early segment is inherently more learnable, not merely more token-efficient by count. A GPT-5.1-based analysis locating the 'first derivation of the correct answer' within each CoT trace finds it clusters near the sequence midpoint on average, and the segment preceding it contains question restatement, initial ideation, and 2-5 self-reflection cues (average ranging 1.9-5.1 across datasets) before the answer is first reached -- while the remainder of the trace, after that point, is dominated by verification, minor cleanup, and restating an already-correct answer, i.e. the empirical signature of overthinking. Benefits of the LSP truncation protocol only materialize once the student model has enough capacity (4B and 8B); the smallest students (0.6B, 1.7B) show little sensitivity to LSP, tracking close to their full-length baselines regardless.

## Limitations

The study is restricted to mathematical reasoning tasks with rigorous verifiable ground truth (AIME24/25); generalization to other reasoning domains (commonsense reasoning, code generation) is left to future work. Findings are drawn from a single model family (Qwen3, both teachers and students) to isolate truncation effects from architectural heterogeneity; cross-family distillation (e.g. Qwen to Gemma) is not tested. The LSP ablation is not token-budget-matched across settings (LSP=0.5 has half the training tokens of LSP=1.0, not an equal-token comparison with more examples at shorter length), which the authors flag as an important direction for future work.

## Why it matters here

- **overthinking**: Directly relevant and explicitly frames its contribution in terms of overthinking: it is the training-time counterpart to inference-time overthinking mitigation, showing empirically that a distillation dataset's later CoT tokens (past the first correct derivation) carry a training-time signature of overthinking -- verification, minor cleanup, restating an already-correct answer -- that is largely dispensable for transferring reasoning capability. Its finding that truncating training sequences to the first half retains ~91% of accuracy at half the compute cost is a concrete, quantified instance of the general claim in this archive's findings that reasoning-trace length and reasoning quality are not the same thing, applied specifically to what a student model needs to learn from rather than to what a model should generate at inference time.

## Entities

- **Concepts**: Lead-Span Proportion (LSP) truncation, section-wise supervision (prompt/CoT/answer masking), training-time overthinking (post-first-derivation redundancy), first-derivation-of-correct-answer localization
- **Methods**: knowledge distillation (soft KL + hard cross-entropy loss), Lead-Span Proportion (LSP) truncation, section-wise loss masking
- **Datasets**: [OpenThoughts-114k](../../../../wiki/datasets/openthoughts-114k.md), [Bespoke-Stratos-17k](../../../../wiki/datasets/bespoke-stratos-17k.md), Synthetic-1, [Llama-Nemotron-Post-Training-Dataset](../../../../wiki/datasets/llama-nemotron-post-training-dataset.md), SkyT1-17k, [AIME24](../../../../wiki/datasets/aime-2024.md), [AIME25](../../../../wiki/datasets/aime-2025.md)

Tags: `knowledge-distillation`, `sequence-truncation`, `overthinking`, `training-efficiency`, `compute-optimal`

## Abstract

Distilling the capabilities from a large reasoning model (LRM) to a smaller student model often involves training on substantial amounts of reasoning data. However, knowledge distillation (KD) over lengthy sequences with prompt (P), chain-of-thought (CoT), and answer (A) sections makes the process computationally expensive. In this work, we investigate how the allocation of supervision across different sections (P, CoT, A) affects student performance. Our analysis shows that selective KD over only the CoT tokens can be effective when the prompt and answer information is encompassed by it. Building on this insight, we establish a truncation protocol to quantify computation-quality tradeoffs as a function of sequence length. We observe that beyond a specific length, longer training sequences provide marginal returns for downstream performance but require substantially higher memory and FLOPs. To this end, training on only the first 50% of tokens of every training sequence can retain, on average, ≈91% of full-sequence performance on math benchmarks while reducing training time, memory usage, and FLOPs by about 50% each. Codes are available at https://github.com/weiruichen01/distilling-the-essence.

---

Record id: `doi:10.18653/v1/2026.findings-acl.587`
