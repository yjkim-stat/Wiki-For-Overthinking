# vLLM

<!-- auto:begin -->

The inference engine most of these sources run on. It appears only as infrastructure, but with one substantive consequence worth recording: the early-exit and probing methods here require interrupting generation, inserting a prompt and resuming, which is why they are demonstrated on locally served open-weight models and are not applicable to closed API models.

- **Kind**: method
- **Also called**: vLLM
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC23](../datasets/amc23.md), [benchmark contamination](../concepts/benchmark-contamination.md), [DAPO](dapo.md), [DAPO-Qwen-32B](../models/dapo-qwen-32b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER](deer.md), [early exit](early-exit.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [greedy decoding](greedy-decoding.md), [GSM8K](../datasets/gsm8k.md), [HumanEval+](../datasets/humaneval.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [MATH500](../datasets/math500.md), [memorization](../concepts/memorization.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](../concepts/overthinking.md), [pass-k](pass-k.md), [PRIME](prime.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [QwQ-32B](../models/qwq-32b.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [reproducibility](../concepts/reproducibility.md), [RLVR](rlvr.md), [test-time compute](../concepts/test-time-compute.md), [token-level entropy](../concepts/token-level-entropy.md)

## Appears in

- [Dynamic Early Exit in Reasoning Models](../../archive/papers/2025/local-a1d9fa1eb8899dfc/summary.md) — Detects the points where a reasoning model switches thought chains, interrupts to induce a trial answer, and stops generation when that answer's confidence is high enough — cutting chain-of-thought length substantially while raising accuracy, with no training.
- [VAR-MATH: Probing True Mathematical Reasoning in LLMs via Symbolic Multi-Instance Benchmarks](../../archive/papers/2026/local-d62cc27b0209da49/summary.md) — Converts AMC23 and AIME24/25 into symbolic templates whose constants are replaced by sampled variables, requires a model to solve several instantiations of each problem, and finds RL-finetuned models lose most of their reported accuracy under that consistency requirement.
- [Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference](../../archive/papers/2025/local-de572e138fc98639/summary.md) — Shows that greedy decoding is not deterministic across hardware: changing GPU type, GPU count or evaluation batch size shifts a reasoning model's AIME'24 accuracy by up to 9 percentage points and its response length by 9,000 tokens under BF16, because floating-point addition is non-associative.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
