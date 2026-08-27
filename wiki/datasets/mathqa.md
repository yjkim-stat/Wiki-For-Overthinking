# MathQA

<!-- auto:begin -->

A maths question-answering set that two archived papers use at the easy end of their suites; neither describes its contents, so the archive knows it only by the cost it takes to answer. ShorterBetter places it out-of-domain (with MMLU, BBH, LiveCodeBench, MBPP and HumanEval) and gets the archive's characteristic easy-set result: ShorterBetter-7B reaches 85.4% on MathQA in 980 average tokens against 83.3% in 3,442 for its Distill-7B baseline - a 71.5% token cut with accuracy slightly up, where the same pair on AIME still spends 5,288 against 11,382 tokens. In CaTS it is the worked example for confidence-based early stopping of Best-of-N, where accuracy rises from 73.7 to 83.6 at a 16-sample budget, so here the saving comes from stopping sampling rather than from shortening a chain of thought. The two uses are different enough that MathQA carries no single role in the archive beyond being the cheap benchmark against which the expensive ones are read.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [adaptive test-time compute](../concepts/adaptive-test-time-compute.md), [AIME](aime.md), [AMC](amc.md), [BBH](bbh.md), [best-of-N](../methods/best-of-n.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [Confidence-based early stopping](../methods/confidence-based-early-stopping.md), [Confidence Calibration](../concepts/confidence-calibration.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../methods/deepseek-r1-distill-qwen-7b.md), [early stopping](../concepts/early-stopping.md), [GSM8K](gsm8k.md), [HumanEval](humaneval.md), [LiveCodeBench](livecodebench.md), [Llama3.1-8B-Instruct](../models/llama3-1-8b-instruct.md), [LoRA fine-tuning](../methods/lora-fine-tuning.md), [MATH](math.md), [MBPP](mbpp.md), [MMLU](mmlu.md), [O1-Pruner](../methods/o1-pruner.md), [Omni-MATH](omni-math.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen2.5-Instruct](../methods/qwen2-5-instruct.md), [Redundant Self-Verification](../concepts/redundant-self-verification.md), [RLVR](../methods/rlvr.md), [SciQ](sciq.md), [Self-Consistency](../methods/self-consistency.md), [Still](still.md), [TriviaQA](triviaqa.md)

## Appears in

- [GrACE: A Generative Approach to Better Confidence Elicitation and Efficient Test-Time Scaling in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1069/summary.md) — GrACE teaches an LLM to output a discriminative, calibrated confidence score during generation itself -- via the similarity between the last hidden state and a learned embedding for a special <CNF> token, trained against k-fold-binned accuracy targets -- eliminating the separate evaluation stage post-generation methods require, and uses this on-the-fly confidence to weight self-consistency voting and drive early-stopping, improving test-time-scaling accuracy by up to 3.3% while cutting required samples by more than half in many cases.
- [CaTS: Calibrated Test-Time Scaling for Efficient LLM Reasoning](../../archive/papers/2026/title-03232c54fde9b57f/summary.md) — Proposes CaTS, a calibrated test-time scaling framework that uses a self-distilled confidence signal to adaptively allocate sampling budget per query, including early stopping once the model is confident.
- [ShorterBetter: Guiding Reasoning Models to Find Optimal Inference Length for Efficient Reasoning](../../archive/papers/2025/title-d40396527f776f1d/summary.md) — ShorterBetter takes the length of the shortest correct response in a sampled group as a per-problem target and rewards the model for matching it, cutting output length by 50%-80% on DeepSeek-Distill-Qwen-1.5B/7B.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
