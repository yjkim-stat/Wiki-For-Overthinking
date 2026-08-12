# DeepSeek-R1-Distill-Llama-8B

<!-- auto:begin -->

The 8B Llama-based member of the R1 distillation series. It carries two of this archive's clearer single-model results: recycling its high-mutual-information representations through the same layer yields a 20% relative accuracy improvement on AIME24, and its causal-attribution score density is among the highest measured, meaning its CoT steps depend on each other more strongly than in the Qwen3-based models compared alongside it. Its mutual-information trajectory also shows the sharpest contrast against its non-reasoning base.

- **Kind**: model
- **Also called**: DS-Llama-8B
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [AIME24](../datasets/aime24.md), [budget forcing](../methods/budget-forcing.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [DeepSeek-R1-Distill-Qwen-14B](deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [epistemic verbalization](../concepts/epistemic-verbalization.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [greedy decoding](../methods/greedy-decoding.md), [GSM8K](../datasets/gsm8k.md), [information bottleneck](../concepts/information-bottleneck.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B](llama-3-1-8b.md), [Llama-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MMLU-PRO](../datasets/mmlu-pro.md), [pass-k](../methods/pass-k.md), [Qwen2.5-14B](qwen2-5-14b.md), [Qwen2.5-32B](qwen2-5-32b.md), [Qwen2.5-7B](qwen2-5-7b.md), [Qwen2.5-Math-7B](qwen2-5-math-7b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-8B](qwen3-8b.md), [QwQ-32B](qwq-32b.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [reproducibility](../concepts/reproducibility.md), [self-correction](../concepts/self-correction.md), [test-time scaling](../methods/test-time-scaling.md), [verification](../concepts/verification.md), [vLLM](../methods/vllm.md), [ZebraLogic](../datasets/zebralogic.md)

## Appears in

- [Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks in LLM Reasoning](../../archive/papers/2025/local-2c3407071e27c9d6/summary.md) — Tracks mutual information between each reasoning step's representation and the correct answer, finds it spikes at sparse 'MI peaks' that decode to reflective tokens like 'Wait' and 'Hmm', and shows suppressing exactly those tokens degrades reasoning while suppressing equally many others does not.
- [Local Causal Attribution of Chain-of-Thought Reasoning](../../archive/papers/2026/local-6db01f05462cef8e/summary.md) — Fits a structural causal model over the units of a single chain-of-thought trace using leave-one-out interventions and linear regression, producing a pairwise influence matrix between every pair of steps at a cost linear in the number of units.
- [Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference](../../archive/papers/2025/local-de572e138fc98639/summary.md) — Shows that greedy decoding is not deterministic across hardware: changing GPU type, GPU count or evaluation batch size shifts a reasoning model's AIME'24 accuracy by up to 9 percentage points and its response length by 9,000 tokens under BF16, because floating-point addition is non-associative.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
