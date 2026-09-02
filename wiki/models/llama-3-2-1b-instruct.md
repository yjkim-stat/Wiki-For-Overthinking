# Llama-3.2-1B-Instruct

<!-- auto:begin -->

Llama-3.2-1B-Instruct is a small instruction-tuned open-weight model used in this archive as one of the smaller/weaker backbones in Marco-o1 v2's distillation-bottleneck study: MCTS-generated CoT training data plus CoT-aware post-training sharply improves it on some benchmarks (e.g. Blocksworld 0.2%->5.6%, instruction-following-other 33.1%->47.1%) while leaving it at 0.0% on AIME throughout. It also appears among the models THOUGHTTERMINATOR evaluates for overthinking (local/global overthinking scores, the DUMB500 easy-question probe), with no model-specific result for it broken out in that source.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME](../datasets/aime.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [difficulty estimation](../concepts/difficulty-estimation.md), [GPQA](../datasets/gpqa.md), [GPT-4o](gpt-4o.md), [GSM8K](../datasets/gsm8k.md), [LLaMA-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [LLaMA 3.2 3B Instruct](llama-3-2-3b-instruct.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-1.5B-Instruct](qwen2-5-1-5b-instruct.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [QwQ-32B](qwq-32b.md), [QwQ-32B-Preview](qwq-32b-preview.md), [ZebraLogic](../datasets/zebralogic.md)

## Appears in

- [Marco-o1 v2: Towards Widening The Distillation Bottleneck for Reasoning Models](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-1145/summary.md) — Marco-o1 v2 identifies 'formalistic long-time thinking' -- distilled small models mechanically replicating a large reasoning model's surface reasoning patterns (content repetition, over-reflection) without internalizing the underlying logic, often producing no final answer at all -- and fixes it by generating CoT training data from scratch via MCTS plus three CoT-aware post-training techniques (thought-length balance, fine-grained/masking-based DPO, joint SFT+DPO loss).
- [THOUGHTTERMINATOR: Benchmarking, Calibrating, and Mitigating Overthinking in Reasoning Models](../../archive/papers/2025/local-eff598a06b1089db/summary.md) — The paper defines model-relative measures of overthinking (local/global overthinking scores) built from observed token-spend distributions, introduces the DUMB500 easy-question dataset to probe overthinking on trivial inputs, and proposes THOUGHTTERMINATOR, a training-free decoding-time technique that interrupts a reasoning model with token-budget reminders and forces an answer at a difficulty-calibrated deadline.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
