<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# When Is Thinking Enough? Early Exit via Sufficiency Assessment for Efficient Reasoning

- **Authors**: Yang Xiang, Yixin Ji, Ruotao Xu, Dan Qiao, Zheming Yang, Juntao Li, Min Zhang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1080/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1080.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1080
- **Topics**: overthinking
- **Relevance score**: overthinking 0.75

## In one line

DTSR (Dynamic Thought Sufficiency in Reasoning) is a training-free early-exit framework where the model itself, at each reflection signal ('Wait', 'Alternatively', etc.), evaluates from a third-person perspective whether its own chain-of-thought so far is sufficient to answer, exiting once a self-assessed sufficiency score crosses a threshold, cutting reasoning length 28.9-34.9% with near-zero accuracy loss across Qwen3-8B/14B/32B and five benchmarks, outperforming NoThinking, NOWAIT, and DEER while also cutting inference latency 25-40% (unlike DEER, which reduces length but increases latency).

## Problem

Large reasoning models suffer from overthinking -- consuming excessive tokens re-verifying answers or exploring alternatives even on simple problems after the correct solution is already reached -- and existing early-exit methods rely on handcrafted or empirical indicators (fixed token budgets, consistency of probed intermediate answers, confidence of intermediate answers) that are unreliable (reasoning models are shown to be overconfident, especially on incorrect answers, and this overconfidence grows with reasoning length) and impractical for tasks with long-form or open-ended answers where intermediate answers cannot be easily extracted.

## Contributions

- an empirical analysis identifying that a reasoning trace's optimal early-exit point is typically followed by explicit self-reflection cues, motivating reflection-signal-triggered (rather than every-token or fixed-interval) sufficiency checking
- DTSR, a training-free framework where the model performs metacognitive third-person self-assessment of its own chain-of-thought's sufficiency at reflection signals, exiting once a threshold sufficiency score is reached -- generalizable to long-form/open-ended tasks unlike prior intermediate-answer-probing methods (DynasorCoT, DEER)
- extensive experiments across three model scales and six benchmarks (including out-of-domain code generation) showing DTSR reduces reasoning length 28.9-50%+ with near-lossless accuracy, outperforming NoThinking, NOWAIT, and DEER, while also reducing end-to-end inference latency 25-40% (unlike DEER, which reduces tokens but increases latency due to synchronous batch evaluation)
- a discussion and ablation (DTSR vs. DTSR-1) demonstrating that a third-person self-evaluation framing is more reliable than direct first-person self-judgment for assessing reasoning sufficiency, offering insight into LRM self-evaluation paradigms and overconfidence

## Method

Inspired by human metacognition, DTSR operates in two stages. (1) Reflection Signal Monitoring: rather than assessing sufficiency after every token (computationally impractical), the model's generation is monitored for reflection-signal tokens (empirically identified via an analysis of Qwen3-32B reasoning trajectories showing that a trace's true optimal early-exit point -- the earliest position at which the model can already produce a correct answer -- is typically followed by explicit self-reflection/verification cues like 'Wait', 'Alternatively', and phrases beginning with 'But'). (2) Thought Sufficiency Check: upon detecting a reflection signal (and only if at least a minimum token interval k has elapsed since the last check, to avoid redundant checks when signals cluster), the model is prompted -- from a third-person perspective, treating its own reasoning trace as an external object to evaluate rather than directly judging itself -- to produce a scalar sufficiency score in [0,100] for whether the current chain-of-thought already suffices to derive the final answer; if the score meets or exceeds a threshold tau, the model appends </think> and proceeds to the final answer, otherwise it resumes reasoning from the reflection point and continues until the next signal. Evaluated on Qwen3-8B/14B/32B across six benchmarks (GSM8K, MATH-500, AMC 2023, OlympiadBench, GPQA Diamond, LiveCodeBench) against Vanilla (no intervention), NoThinking (skip reasoning via prompting), NOWAIT (masking reflective tokens like 'wait'/'hmm'), and DEER (entropy-based confidence on intermediate answers), plus training-based comparisons in an appendix table.

## Results

Across all three model sizes and five math/science benchmarks, DTSR achieves near-identical accuracy to Vanilla reasoning (e.g. Qwen3-8B: 81.0 vs. 81.9 overall Acc) while reducing average sequence length by 28.9-34.9% (Qwen3-8B: 4,428 vs. 6,510 tokens, -32.0%; Qwen3-14B: 3,748 vs. 5,761, -34.9%; Qwen3-32B: 4,010 vs. 5,638, -28.9%), and on Qwen3-14B specifically, DTSR even improves accuracy over Vanilla on GPQA and OlympiadBench (84.8 vs. 84.4 overall Acc). Compared to prior training-free efficient-reasoning baselines, NoThinking shortens sequences most aggressively but severely limits reasoning capability by bypassing the reasoning process entirely; NOWAIT (masking reflective tokens) causes significant performance degradation on complex tasks because restricting the model's inherent self-reflection removes genuinely useful reasoning, not just redundant reasoning; DEER (confidence-based on intermediate answers) is limited by LRM overconfidence, especially on incorrect answers, and considers only partial (intermediate-answer) information rather than the global reasoning trace. On LiveCodeBench (a programming task, evaluated separately as an out-of-domain generalization check), DTSR reduces generation length by over 50% (52% for Qwen3-8B, 53% for Qwen3-14B) with only minimal accuracy degradation, and the paper attributes programming tasks' larger overthinking margin to models already being capable of generating correct code mid-trace but continuing to spend tokens on repeated verification. As the maximum token budget is expanded from 2k to 16k on MATH-500, DTSR consistently generates shorter sequences than Vanilla at every budget, with the length gap growing as the budget increases -- indicating DTSR's savings scale with, rather than saturate under, larger token budgets. Ablations: the token interval k has little effect on accuracy but exhibits a U-shaped effect on latency (k<=64: latency increases from frequent checks; k>64: latency increases from missed optimal exit points), with k=64 identified as the best trade-off; lowering the sufficiency threshold tau below 100 causes accuracy to drop noticeably (premature termination on underdeveloped reasoning) even though it shortens sequences somewhat, identifying tau=100 as optimal. End-to-end inference latency is reduced 25-40% by DTSR versus Vanilla, and notably DTSR beats DEER on latency even though DEER also reduces token count, because DEER's synchronous batch-evaluation scheme (all samples must finish generating before a collective evaluation) causes idle computation and increased latency under continuous batching, whereas DTSR's design allows samples to interleave between generation and evaluation phases. A first-person self-evaluation variant (DTSR-1, asking the model to directly judge its own reasoning's adequacy mid-process rather than from a third-person, external-object framing) performs worse than DTSR on both accuracy and length on MATH-500, supporting the authors' framing that separating reasoning generation from adequacy judgment (via a third-person perspective) is what enables reliable self-assessment, rather than the model being unable to self-assess sufficiency at all.

## Limitations

Due to computational resource constraints, experiments are conducted only on LLMs up to 32B parameters; behavior at larger scales is untested. The work focuses exclusively on textual reasoning tasks including mathematics and code; it has not been extended to multimodal reasoning or agentic scenarios, which the authors leave for future exploration.

## Why it matters here

- **overthinking**: Directly central to the topic, explicitly named and targeted: DTSR is presented as a mechanism for 'effectively mitigating overthinking while maintaining strong reasoning performance,' and its core empirical claim -- that reasoning models exhibit overconfidence which grows with reasoning length, making raw confidence scores (as used by DEER) an unreliable exit criterion -- is a mechanistic caution directly relevant to any confidence-based overthinking mitigation method in this archive (e.g. CAT, MUR, GrACE). Its comparison against NOWAIT (naive reflective-token suppression, which the paper shows removes genuinely useful reasoning alongside redundant reasoning) and its third-person-vs-first-person self-evaluation ablation together offer a nuanced picture of exactly which self-assessment designs work for overthinking mitigation and which merely suppress the reasoning trace's substance.

## Entities

- **Concepts**: reflection signal (Wait/Alternatively/But-triggered exit cue), thought sufficiency check, third-person self-evaluation (vs. first-person), optimal early-exit point, LRM overconfidence
- **Methods**: Dynamic Thought Sufficiency in Reasoning (DTSR), reflection signal monitoring, third-person thought sufficiency check, NoThinking / NOWAIT / DEER (baselines)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH-500](../../../../wiki/datasets/math500.md), [AMC 2023](../../../../wiki/datasets/amc23.md), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md), [GPQA Diamond](../../../../wiki/datasets/gpqa-diamond.md), [LiveCodeBench](../../../../wiki/datasets/livecodebench.md)

Tags: `overthinking`, `early-exit`, `metacognition`, `training-free`, `self-evaluation`

## Abstract

Large reasoning models (LRMs) have achieved remarkable performance in complex reasoning tasks, driven by their powerful inference-time scaling capability.However, LRMs often suffer from overthinking, which results in substantial computational redundancy and significantly reduces efficiency.Early-exit methods aim to mitigate this issue by terminating reasoning once sufficient evidence has been generated, yet existing approaches mostly rely on handcrafted or empirical indicators that are unreliable and impractical.In this work, we introduce Dynamic Thought Sufficiency in Reasoning (DTSR), a novel framework for efficient reasoning that enables the model to dynamically assess the sufficiency of its chain-of-thought (CoT) and determine the optimal point for early exit.Inspired by human metacognition, DTSR operates in two stages: (1) Reflection Signal Monitoring, which identifies reflection signals as potential cues for early exit, and (2) Thought Sufficiency Check, which evaluates whether the current CoT is sufficient to derive the final answer.Experimental results on the Qwen3 models show that DTSR reduces reasoning length by 28.9%–34.9% with minimal performance loss, effectively mitigating overthinking.We further discuss overconfidence in LRMs and self-evaluation paradigms, providing valuable insights for early-exit reasoning.

---

Record id: `doi:10.18653/v1/2026.acl-long.1080`
