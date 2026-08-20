# ProofWriter

<!-- auto:begin -->

A rule-based deductive logic set, used in this archive by two papers with very different purposes and one shared caution about how its numbers are produced. The 1.58-bit quantization paper uses it as the scientific-logic arm of its evaluation and turns it into evidence about calibration rather than about logic: adding 256 ProofWriter training examples to the calibration mix moves the average from 39.50 to 82.21, against 84.92 for the full-precision model, so what the quantized model can still do depends on what it was calibrated on. ReLIT reports 98.60 on it as a theorem-finding set, far above the 82.40 of the best reasoning LLM in the same table -- but the archive's reading of that paper records that ReLIT was trained on 5,000 ProofWriter examples while every LLM number in the table is few-shot from GLoRE, so the comparison is not like for like. ReLIT's adaptive halting also uses the fewest recursion steps on it, 3.6 against 5.2 on RuleTaker and 7.8 on NaN-NLI, which that paper reads as the task being the least demanding of the four.

- **Kind**: dataset
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [answer stabilization](../concepts/answer-stabilization.md), [chain of thought](../methods/chain-of-thought.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Coconut](../methods/coconut.md), [DeepSeek-R1](../models/deepseek-r1.md), [GPT-4](../models/gpt-4.md), [GSM8K](gsm8k.md), [HumanEval+](humaneval.md), [implicit chain of thought](../concepts/implicit-chain-of-thought.md), [latent reasoning](../concepts/latent-reasoning.md), [MATH500](math500.md), [MBPP+](mbpp.md), [Omni-MATH](omni-math.md), [OpenCodeInstruct](opencodeinstruct.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-235B-A22B](../models/qwen3-235b-a22b.md), [Qwen3-30B-A3B](../models/qwen3-30b-a3b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B](../models/qwen3-4b.md), [QwQ-32B](../models/qwq-32b.md), [recurrent depth](../methods/recurrent-depth.md), [RoBERTa](../models/roberta.md)

## Appears in

- [Attend to Your Own Thoughts: Breaking the Barrier for Post-Training Quantization of Reasoning LLMs through the Lens of 1.58-Bit Quantization](../../archive/papers/2026/arxiv-2608-01078/summary.md) — Finds that ternary post-training quantization of a reasoning model collapses because the calibration set is web text, and repairs it by calibrating on chain-of-thought traces the target model generates for itself.
- [Think Deep, Speak Once: Relit, A Recursive Latent Implicit Transformer Framework](../../archive/papers/2026/arxiv-2608-08113/summary.md) — Bolts a small trainable recurrent block between a frozen 1.1B language model's body and its output head, so reasoning happens as repeated refinement of two latent vectors rather than as generated tokens.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
