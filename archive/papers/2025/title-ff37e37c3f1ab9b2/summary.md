<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# QFFT, Question-Free Fine-Tuning for Adaptive Reasoning

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/119264>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.62

## In one line

QFFT fine-tunes a short-CoT instruct model on Long CoT responses with the question deleted from every training example, so the model keeps its default concise reasoning and switches to reflective Long CoT only when it hits uncertainty or an error, cutting average tokens by roughly 50% at accuracy comparable to ordinary SFT.

## Problem

Distilling Long CoT traces into a smaller model by supervised fine-tuning on (question, Long CoT response) pairs makes the student reason at length on every input, including simple ones. The paper's diagnosis is specific: the Q -> R mapping learned during SFT overrides the model's original Short CoT patterns - a phenomenon it calls Override. It demonstrates this by retaining questions on only a fraction alpha of training samples: at alpha = 0 the model still uses Short CoT on over 50% of inputs, but raising alpha from 0.1% to 1% drops the Short CoT proportion from 40.95% to 13.24%. So a vanishingly small number of question-answer pairs is enough to destroy the concise mode. Existing Long-to-Short methods compress the trace after the fact and, the paper argues, add training cost while reducing tokens only modestly.

## Contributions

- Question-Free Fine-Tuning: fine-tuning on Long CoT responses with the question removed, so the Q -> R mapping that overrides Short CoT is never learned.
- The Override diagnosis, with the alpha-sweep experiment showing that retaining questions on 1% of samples drops Short CoT usage from 40.95% to 13.24%.
- Reasoning Adaptability Cohen's Kappa (RAK), a chance-corrected metric for whether a model's choice of reasoning pattern tracks question difficulty as judged by a Short CoT reference model.
- Evidence that QFFT's Long CoT is triggered by uncertainty and error (53% verification, 26% backtracking) and rises with difficulty (7.41% -> 51.12% across MATH500 difficulty levels).
- Evidence that QFFT beats SFT under noisy distillation data, out of domain, and in a 100-example low-resource setting.

## Method

QFFT drops the question Q entirely and trains with a plain causal LM objective over the Long CoT response R alone: L = -(1/|R|) sum_t log P(R_t | R_<t). Because no concrete Q -> R mapping is ever learned, a non-empty prompt at inference does not trigger Long CoT, so the model answers from its pre-existing Short CoT behaviour; the reflective machinery learned from R (the 'wait' pattern, verification, backtracking) is nonetheless available and fires when the model detects uncertainty or an error mid-solution. The paper frames this two ways: as SFT with null questions, and as a form of continued pre-training on reasoning responses. It assumes reflective behaviour learned conditional on Long-CoT uncertainty transfers to uncertainty arising inside Short CoT reasoning. To measure adaptivity it defines Reasoning Adaptability Cohen's Kappa (RAK): the agreement, beyond chance, between which pattern the model chooses and whether a Short CoT reference model can solve the question.

## Results

Base models Qwen2.5-Instruct-7B and -32B; distillation corpora S1.1 (1k), LIMO (871), Bespoke-Stratos (17k), all DeepSeek-R1 traces; 16 samples per question, temperature 0.6, max 32,768 tokens. Averaged over GSM8K/MATH/AIME25 (Table 2): 7B on S1.1, QFFT 62.8 acc / 5.3K tokens / RAK 34.7 vs SFT 63.2 / 8.2K / 1.8 - accuracy -0.4, tokens -50.5%. 7B on LIMO: 61.9 / 5.5K / 33.7 vs 61.8 / 8.2K / 2.2 (+0.1 acc, -33.3% tokens). 7B on BS-17K: 63.4 / 4.1K / 34.7 vs 64.0 / 7.0K / 2.3 (-0.6 acc, -54.2% tokens). 32B on S1.1: 77.5 / 5.3K / 35.4 vs 78.2 / 7.5K / 1.5 (-0.6 acc, -44.4% tokens). 32B on LIMO: 76.7 / 5.4K / 33.2 vs 76.6 / 6.3K / 3.3 (+0.1 acc, -29.6% tokens). Against Long-to-Short baselines on 32B (Table 3), QFFT scores AES 2.3 while O1-Pruner (7B) reaches 0.8K tokens on GSM8K but AES -1.7, and SimPO-shortest 32B -1.6; SFT-Shortest 32B has AES -12.9. Adaptivity: on MATH500 the share of Long CoT responses rises from 7.41% at the easiest difficulty to 51.12% at the hardest; 53% of Long CoT triggers are verification behaviour and 26% backtracking. Out of domain (32B, S1.1): MMLU-Pro 73.6 vs 64.9 for SFT, GPQA 65.7 vs 60.6, LLM-AggreFact 76.8 vs 60.5. Noise robustness on MATH: with entirely mismatched question-answer training pairs (Level IV) SFT falls from 76.5 to 0.4 pass@1 while QFFT holds 78.6.

## Limitations

There is no limitations section; the paper goes from a related-work discussion to the conclusion. Points the reader should notice from its own tables: (1) The headline '>50% token reduction' is the best case, not the average - the reduction is 71-76% on GSM8K but only 20-30% on AIME25, and averages 29.6% to 54.2% depending on model and corpus. The paper says this itself: savings shrink as difficulty rises because Long CoT is genuinely needed. (2) Accuracy is not uniformly preserved. AIME25 is where it costs: 32B/S1.1 48.6 -> 46.8, 32B/LIMO 45.8 -> 45.0, 7B/S1.1 18.2 -> 17.2, 7B/BS-17K 19.8 -> 18.3. The comparable-accuracy claim rests on averaging those losses against gains on GSM8K and MATH. (3) O1-Pruner and SimPO-shortest cut tokens further than QFFT; QFFT wins on the AES tradeoff metric, whose parameters (alpha = 0.1, beta = 0.1, gamma = 1.0) are chosen to penalise accuracy loss ten times more than they reward token savings, so the ranking is sensitive to that choice. (4) The RAK metric depends on Assumption 1, that the reference Short CoT model's ability approximates the distilled model's Short CoT ability - question difficulty is defined by what Qwen2.5-Instruct can solve, not intrinsically. (5) The Long/Short classification in the analysis uses GPT-4o on two sentences either side of the first 'wait'. (6) In-domain evaluation is mathematics only; the out-of-domain evidence is MMLU-Pro, GPQA and LLM-AggreFact.

## Why it matters here

- **overthinking**: Directly on topic, and it moves the causal story rather than adding another length-penalty method. Its central claim is that overthinking in distilled reasoners is not an inherent property of Long CoT data but an artefact of the training format: the (question, Long CoT) pairing overwrites the Short CoT behaviour the base model already had, and the alpha-sweep shows 1% of paired examples is enough to do it (Short CoT usage 40.95% -> 13.24%). The fix is a deletion, not an added objective - no length reward, no difficulty classifier, no budget at inference - which makes it a cheap baseline any length-control method should now be compared against. It also supplies a reusable measurement: RAK asks whether a model spends its tokens on the questions that need them, chance-corrected against a Short CoT reference, which is a sharper instrument than average token count and separates 'shorter' from 'adaptively shorter' (SFT models score 0.2-4.6, QFFT 26.6-45.7). The difficulty-conditioned Long CoT rate (7.41% at the easiest MATH500 level to 51.12% at the hardest) and the trigger breakdown (53% verification, 26% backtracking) are direct evidence on when models decide to keep going. Two cautions for the topic's notes: the '>50% token reduction' headline is an average dominated by GSM8K (-71 to -76%) while AIME25 sees only -20 to -30%, exactly where length matters most; and accuracy is not free at the hard end, with AIME25 dropping in four of five configurations (32B/S1.1 48.6 -> 46.8). The paper's own framing - Short CoT risks oversimplification, Long CoT risks overthinking, adaptive reasoning balances both - is the two-sided version of this topic and is worth quoting.

## Entities

- **Concepts**: [Overthinking](../../../../wiki/concepts/overthinking.md), [Adaptive Reasoning](../../../../wiki/concepts/adaptive-reasoning.md), Long CoT, Short CoT, Override (SFT overwriting default reasoning patterns), Long-to-Short compression, Reasoning Adaptability, Accuracy-Efficiency Score, Reflective behaviour triggers (verification, backtracking, subgoal setting, backward chaining), [Test-time scaling](../../../../wiki/concepts/test-time-scaling.md), Reasoning distillation
- **Methods**: QFFT (Question-Free Fine-Tuning), Supervised Fine-Tuning on Long CoT, Difficulty-Adaptive Distillation (DAD), [SFT-Shortest](../../../../wiki/methods/sft-shortest.md), [DPO-Shortest](../../../../wiki/methods/dpo-shortest.md), SimPO-Shortest, [O1-Pruner](../../../../wiki/methods/o1-pruner.md), RAK (Reasoning Adaptability Cohen's Kappa), AES (Accuracy-Efficiency Score), LLaMA Factory
- **Datasets**: S1.1 (1k), LIMO (871), Bespoke-Stratos (17k), [GSM8K](../../../../wiki/datasets/gsm8k.md), MATH500, [AMC23](../../../../wiki/datasets/amc23.md), [Minerva](../../../../wiki/datasets/minerva.md), [AIME 2024](../../../../wiki/datasets/aime-2024.md), [AIME 2025](../../../../wiki/datasets/aime-2025.md), [GPQA](../../../../wiki/datasets/gpqa.md), [MMLU-Pro](../../../../wiki/datasets/mmlu-pro.md), LLM-AggreFact

Tags: `overthinking`, `adaptive-reasoning`, `long-cot`, `short-cot`, `reasoning-distillation`, `long-to-short`, `token-efficiency`, `fine-tuning`, `math-reasoning`, `neurips2025`

## Abstract

Abstract Recent advancements in Long Chain-of-Thought (CoT) reasoning models have improved performance on complex tasks, but they suffer from overthinking, which generates redundant reasoning steps, especially for simple questions. This paper revisits the reasoning patterns of Long and Short CoT models, observing that the Short CoT patterns offer concise reasoning efficiently, while the Long CoT patterns excel in challenging scenarios where the Short CoT patterns struggle. To enable models to leverage both patterns, we propose Question-Free Fine-Tuning (QFFT), a fine-tuning approach that removes the input question during training and learns exclusively from Long CoT responses. This approach enables the model to adaptively employ both reasoning patterns: it prioritizes the Short CoT patterns and activates the Long CoT patterns only when necessary. Experiments on various mathematical datasets demonstrate that QFFT reduces average response length by more than 50\%, while achieving performance comparable to Supervised Fine-Tuning (SFT). Additionally, QFFT exhibits superior performance compared to SFT in noisy, out-of-domain, and low-resource scenarios.

---

Record id: `title:ff37e37c3f1ab9b2`
