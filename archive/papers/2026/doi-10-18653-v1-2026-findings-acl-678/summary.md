<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Self-Reflection Improves Safety of Large Reasoning Models

- **Authors**: Qiang Huang, Wei Zhai, Feng Huang, Dejing Dou
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.678/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.678.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.678
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Trains large reasoning models with a special [Self-Reflection] token that triggers mid-generation introspection and recovery once harmful content is detected, cutting harmful content rate from 13.8% to 4.1% (nearly 3x) versus mainstream safety tuning, while also reducing generation token overhead by 15%+ compared to backtracking-based safety defenses.

## Problem

Safety alignment for large reasoning models is typically preventive (SFT, RLHF, DPO), producing 'shallow safety alignment' where models learn to reject harmful requests only within the first few output tokens, leaving later-generated content vulnerable to manipulation or jailbreak; existing backtracking-based defenses (which discard and regenerate harmful segments) reduce this risk but introduce substantial computational overhead and can still be circumvented when harmful signals are diffuse or adversarial prompts are carefully crafted.

## Contributions

- Self-Reflection, a special-token mechanism that triggers mid-generation introspection and recovery upon detecting harmful content, distinct from prior backtracking approaches that discard/regenerate entire harmful segments
- an SFT+DPO training recipe that supervises reflection to trigger precisely at the onset of harmful content while explicitly suppressing unnecessary reflection on already-safe generations, integrated into standard post-training pipelines
- empirical results showing ~3x reduction in harmful content rate versus mainstream safety tuning, improved safety-helpfulness balance, ~15%+ lower generation-token overhead than backtracking defenses, and the strongest jailbreak robustness among compared methods including against an attack specifically designed to defeat it

## Method

Introduces a special [Self-Reflection] token (~50 tokens of explicit questioning/reflection semantics, e.g. 'Wait') that the model inserts mid-generation upon detecting early signals of harmful output, triggering a self-doubt-pause-reflection process that recovers to a safe response without discarding or restarting generation. Training has two stages: (1) SFT on reflection examples constructed by using a safety classifier (Llama Guard 3) to locate the harmful prefix within a harmful response, then training the model to immediately emit [Self-Reflection] at that point and continue to a safe response, with harmful-prefix likelihood explicitly not maximized to avoid increasing harmful-generation probability; (2) DPO on constructed preference pairs that both encourage Self-Reflection when it corrects an unsafe trajectory and suppress Self-Reflection when the initial response is already safe (to avoid over-reflection/redundant computation on benign inputs). Evaluated on four LRMs (DeepSeek-R1-Distill-LLaMA-8B, DeepSeek-R1-Distill-Qwen-7B, NVIDIA-Nemotron-Nano-9B-v2, Qwen3-8B) against Backtracking-based defenses (Reset, BSAFE) on three safety benchmarks (ToxicChat, Aegis-AI-Content-Safety, SafetyBench), two safety-helpfulness trade-off benchmarks (OR-Bench for over-refusal, PHTest), three utility benchmarks (MATH500, LiveCodeBench, GPQA Diamond), and four jailbreak attacks (Prefilling, GCG, AutoDAN, plus a novel Adaptive attack specifically designed to bypass Self-Reflection via delayed reflection triggers or post-reflection adversarial re-injection).

## Results

Self-Reflection combined with SFT+DPO reduces harmful content rate (HCR) from 13.8% (SFT baseline) to 4.1%, a ~3x improvement over mainstream safety tuning, while also lowering over-refusal rate (RR) on OR-Bench/PHTest and maintaining or slightly improving utility accuracy (MATH500/LiveCodeBench/GPQA Diamond) versus baselines -- i.e. the safety gain does not trade off against helpfulness. Generation-efficiency measurements show Self-Reflection's average token count stays close to the vanilla (untuned) model and is markedly lower than Backtracking methods: e.g. on Qwen3-8B, Self-Reflection averages 541 tokens vs. BSAFE's 628 (>15% reduction), because Self-Reflection performs a single reflective intervention rather than Backtracking's repeated discard-and-regenerate cycles. Under adversarial jailbreak attacks, Self-Reflection achieves the lowest average attack success rate (ASR) across all four attack types on both tested backbones (5.3% on LLaMA-8B, 6.6% on Qwen3-8B), roughly 13x and 7.5x lower than the SFT-only baseline and nearly 3x lower than the strongest Backtracking method (BSAFE), including against the specially-designed Adaptive attack targeting Self-Reflection itself (delayed triggers, post-reflection adversarial re-injection) -- indicating the mechanism's intrinsic self-correction (rather than external hard resets) is harder to circumvent than Backtracking even without adversarial training.

## Limitations

The effectiveness of Self-Reflection is highly dependent on the quality, diversity, and coverage of the constructed Reflection-Safety training pairs; if the training set fails to cover a variety of harm scenarios or complex adversarial patterns, self-correction ability may be limited on out-of-domain or novel jailbreaking attacks not represented in training. The paper notes a rigorous theoretical investigation of the method's generalization across diverse model architectures is still warranted, and flags exploring Self-Reflection as a general capability-enhancing technique beyond the safety domain as future work.

## Why it matters here

- **overthinking**: Tangential: this is a safety/jailbreak-robustness paper rather than a reasoning-efficiency paper, but it is directly relevant background for any overthinking-mitigation method that inserts special reflection/control tokens into a reasoning trace -- it shows a single, precisely-triggered mid-generation intervention token can outperform repeated discard-and-regenerate cycles both on the target metric (here safety, elsewhere often accuracy) and on token efficiency (>15% fewer tokens than the backtracking baselines), which is structurally the same tradeoff (one well-placed intervention vs. repeated redundant regeneration) that motivates efficient early-exit and self-correction methods in the overthinking literature.

## Entities

- **Concepts**: [Self-Reflection] token, shallow safety alignment, self-doubt-pause-reflection process, adaptive jailbreak attack (delayed trigger / post-reflection re-injection)
- **Methods**: Self-Reflection (SFT + DPO with reflection-triggering preference pairs), Reset (backtracking baseline), BSAFE (backtracking baseline), Llama Guard 3 (safety classifier for training-data construction)
- **Datasets**: ToxicChat, Aegis-AI-Content-Safety-Dataset, SafetyBench, OR-Bench, PHTest, [MATH500](../../../../wiki/datasets/math500.md), [LiveCodeBench](../../../../wiki/datasets/livecodebench.md), [GPQA Diamond](../../../../wiki/datasets/gpqa-diamond.md), HH-RLHF, OpenAssistant-2, HelpSteer2, Dolly 2.0, PKU-SafeRLHF

Tags: `safety-alignment`, `jailbreak-robustness`, `self-correction`, `reasoning-trace-intervention`

## Abstract

Large Reasoning Models(LRMs) have achieved significant breakthroughs over prior large language models (LLMs), but they also entail greater potential safety risks. Existing alignment methods often remain at a shallow level of protection, making them insufficient to address deeper risks and strategic attacks in complex reasoning processes. To bridge this gap, we move beyond the conventional paradigm that treats safety alignment merely as a preventive measure to reduce harmful outputs. Drawing inspiration from human-like introspection and self-correction, we propose Self-Reflection, a technique that introduces a special Self-Reflection token, enabling LRMs to perform Self-Reflection during generation and recover from harmful outputs. Our approach integrates seamlessly into standard post-training paradigms , further enhancing both helpfulness and safety. The experimental results demonstrate that models trained with Self-Reflection not only consistently outperform the baseline in terms of safety (reducing the HCR from 13.8% to 4.1%, nearly a threefold improvement over mainstream approaches), but also achieve substantial advantages in both helpfulness and the safety–helpfulness balance. More importantly, under evaluations involving various adversarial attacks, including a specially designed adaptive attack, the Self-Reflection mechanism significantly enhances model safety without targeted adversarial training.Notice: This paper contains harmful content.

---

Record id: `doi:10.18653/v1/2026.findings-acl.678`
