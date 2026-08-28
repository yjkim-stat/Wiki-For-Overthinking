<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Merlin’s Whisper: Enabling Efficient Reasoning in Large Language Models via Black-box Persuasive Prompting

- **Authors**: Heming Xia, Cunxiao Du, Rui Li, Chak Tou Leong, Yongqi Li, Wenjie Li
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.917/>
- **PDF**: <https://aclanthology.org/2026.acl-long.917.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.917
- **Topics**: overthinking
- **Relevance score**: overthinking 0.62

## In one line

WHISPER treats a large reasoning model purely as a black-box communicator and mitigates overthinking with no training or model access at all, using an iterative refinement loop over persuasive prompts (psychological, evidence-based, role-play, threat, instruction) that finds a single deployable prompt suffix cutting response length up to 3x on simple questions with preserved accuracy.

## Problem

Large reasoning models generate excessively long reasoning traces even for trivial questions (overthinking), inflating latency and KV-cache memory; existing mitigations either require additional training (SFT on shortened CoTs, RL with length penalties, incurring compute cost and generalization risk) or need white-box access to model internals (early exiting, reflection-token suppression, activation steering), while prior prompting-only approaches rely on human-curated instructions like 'Be concise' that either degrade performance substantially or yield limited length reduction.

## Contributions

- the first work to mitigate LRM overthinking via persuasive prompting rather than training or model-internal intervention, requiring no additional training and working as a plug-and-play black-box solution
- WHISPER, an iterative refinement framework generating and ranking persuasive prompt candidates across five perspectives (psychological, evidence-based, role-play, threat, instruction) to find a deployable length-minimizing prompt suffix
- empirical validation across open- and closed-source LRMs (including two commercial thinking APIs) showing up to 3x length reduction on simple questions and ~37-50% average reduction with preserved accuracy, outperforming a reflective prompt optimizer (GEPA) and a white-box inference-intervention baseline (DEER) on compression
- generalizability analysis showing top prompts transfer across model scales within a family, partially across model families, and across data domains beyond the math domain used for prompt development

## Method

Casts efficient reasoning as a black-box persuasive-prompting optimization: find a prompt suffix that minimizes a target model's average response length on a held-out set without hurting accuracy. WHISPER generates candidate persuasive prompts from five perspectives -- psychological (emotional appeal, threat), evidence-based persuasion (citing fabricated authoritative studies), role-playing, and detailed instructions/budget constraints -- using GPT-4o as a prompt generator, seeded with human-curated exemplars and formal perspective definitions. In each iteration, 10 candidates per perspective are generated, evaluated on a development set (average response length and accuracy vs. a tolerance threshold), and the top-5 by length (among those within the accuracy tolerance) are kept as exemplars for the next iteration; after 3 refinement rounds the single best-performing prompt is selected for deployment. Evaluated on open-source LRMs (DeepSeek-R1-Distill-Llama-8B/Qwen-14B, Qwen3-14B and other scales) and closed-source APIs (Claude-3.7-Sonnet-Thinking, Gemini-2.5-Pro-Thinking) across GSM8K, MATH-500, AMC 2023, and AIME 2024, compared against NoThinking, 'Be concise', Chain-of-Draft, the reflective prompt-optimizer GEPA, and the white-box method DEER (used for reference only, not as a fair baseline).

## Results

WHISPER achieves a 3x reduction in response length on simple GSM8K questions with the Qwen3 series and a ~37% average token reduction across all four benchmarks on Qwen3-14B (up to 22% on DeepSeek-R1-Distill), while maintaining comparable accuracy to the original model (e.g. Qwen3-14B: 89.6% vs. original 87.9% overall accuracy at 63.0% of original token count; DeepSeek-R1-Distill-Llama-8B: 79.0% vs. original 78.5% at 80.3% token ratio). It consistently outperforms GEPA (a reflective prompt-optimization framework) and beats the white-box DEER baseline by up to 18 percentage points of compression ratio, despite DEER having model-internal access WHISPER does not. On closed APIs, WHISPER cuts average token usage 46% on Claude-3.7-Sonnet-Thinking and 50% on Gemini-2.5-Pro-Thinking on MATH-500 while preserving accuracy (96.3%->96.4% and 97.1%->97.5% respectively -- i.e. accuracy is not degraded, in some cases nominally improves). Evidence-based persuasion perspective (citing a fabricated MIT study, etc.) achieves the best compression on Qwen3-14B (63-65% compression ratio for top candidates), while role-playing performs best on DeepSeek-R1-Distill-Qwen-14B. Top-performing prompts generalize across model scales within a family (Qwen3 4B/8B/14B/32B) and partially across families (some candidates like Evidence-II and RolePlay-III overlap between Qwen3 and DeepSeek-R1-Distill-Qwen). Domain generalization to GPQA-Diamond and CommonsenseQA (out-of-domain from the math-only prompt-development set) still yields 37-56% token reduction on GPQA-Diamond and ~2x reduction on CommonsenseQA, without re-tuning the prompt. Successive refinement iterations improve compression (18%->22% on DeepSeek-R1-Distill-Qwen-14B, 32%->37% on Qwen3-14B) without further accuracy loss; no further gains are observed beyond three iterations.

## Limitations

Due to computational constraints, experiments were not conducted on larger LRMs such as Qwen3-235B-A22B, though the authors expect the method to retain effectiveness there. Evaluated open-source LRMs are primarily from the Qwen3 and DeepSeek-R1-Distill families; broader model-family coverage (e.g. gpt-oss) is left to future work. The persuasive prompts include fabricated evidence (e.g. citing a nonexistent 2022 MIT study) as one of the effective perspectives, which the paper's ethics statement distinguishes from jailbreak-style adversarial attacks (it targets concise reasoning rather than eliciting harmful outputs) but which is nonetheless a form of designed falsehood embedded in deployed prompts.

## Why it matters here

- **overthinking**: Directly and centrally relevant: it explicitly targets overthinking and demonstrates that a large fraction of a reasoning model's excess length is not load-bearing capability but a persuadable behavioral default -- appropriately framed prompts (no training, no model access) recover most of the token savings that training-time and white-box inference-time methods elsewhere in this archive achieve through much more invasive means, which is itself informative about how shallow/social the overthinking behavior can be.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), black-box persuasive prompting, iterative prompt refinement, [compression ratio](../../../../wiki/concepts/compression-ratio.md)
- **Methods**: WHISPER (iterative persuasive-prompt refinement), [NoThinking (baseline)](../../../../wiki/methods/nothinking-baseline.md), 'Be concise' prompting (baseline), Chain-of-Draft (baseline), GEPA (reflective prompt optimization, baseline), DEER (white-box inference intervention, reference)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH-500](../../../../wiki/datasets/math500.md), [AMC 2023](../../../../wiki/datasets/amc23.md), [AIME 2024](../../../../wiki/datasets/aime-2024.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), [CommonsenseQA](../../../../wiki/datasets/commonsenseqa.md), PRM800K (PDSet source)

Tags: `overthinking`, `prompting`, `black-box`, `test-time-efficiency`, `persuasion`

## Abstract

Large reasoning models (LRMs) have demonstrated remarkable proficiency in tackling complex tasks through step-by-step thinking. However, this lengthy reasoning process incurs substantial computational and latency overheads, hindering the practical deployment of LRMs. This work presents a new approach to mitigating overthinking in LRMs via black-box persuasive prompting. By treating LRMs as black-box communicators, we investigate how to persuade them to generate concise responses without compromising accuracy. We introduce Whisper, an iterative refinement framework that generates high-quality persuasive prompts from diverse perspectives. Experiments across multiple benchmarks demonstrate that Whisper consistently reduces token usage while preserving performance. Notably, Whisper achieves a 3× reduction in average response length on simple GSM8K questions for the Qwen3 series and delivers an average ∼40% token reduction overall. For closed-source APIs, Whisper reduces token usage on MATH-500 by 46% for Claude-3.7 and 50% for Gemini-2.5. Further analysis reveals the broad applicability of Whisper across data domains, model scales, and families, underscoring the potential of black-box persuasive prompting as a practical strategy for enhancing LRM efficiency.

---

Record id: `doi:10.18653/v1/2026.acl-long.917`
