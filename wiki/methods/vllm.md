# vLLM

<!-- auto:begin -->

The inference engine most of these sources run on. It appears only as infrastructure, but with one substantive consequence worth recording: the early-exit and probing methods here require interrupting generation, inserting a prompt and resuming, which is why they are demonstrated on locally served open-weight models and are not applicable to closed API models.

- **Kind**: method
- **Also called**: vLLM
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [AMC23](../datasets/amc23.md), [answer aggregation](answer-aggregation.md), [beam search](beam-search.md), [benchmark contamination](../concepts/benchmark-contamination.md), [bootstrap resampling](bootstrap-resampling.md), [compute allocation](../concepts/compute-allocation.md), [DAPO](dapo.md), [DAPO-Qwen-32B](../models/dapo-qwen-32b.md), [DeepSeek-R1-0528-Qwen3-8B](../models/deepseek-r1-0528-qwen3-8b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER](deer.md), [Dynasor](dynasor.md), [early exit](early-exit.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [greedy decoding](greedy-decoding.md), [GSM8K](../datasets/gsm8k.md), [HMMT](../datasets/hmmt.md), [HumanEval+](../datasets/humaneval.md), [KV cache](../concepts/kv-cache.md), [linear probe](linear-probe.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [MATH500](../datasets/math500.md), [memorization](../concepts/memorization.md), [Monte Carlo tree search](monte-carlo-tree-search.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](../concepts/overthinking.md), [pass@k](../concepts/pass-k.md), [PRIME](prime.md), [process reward model](../concepts/process-reward-model.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-235B-A22B](../models/qwen3-235b-a22b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [QwQ-32B](../models/qwq-32b.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [reproducibility](../concepts/reproducibility.md), [RLVR](rlvr.md), [self-consistency](self-consistency.md), [test-time compute](../concepts/test-time-compute.md), [token-level entropy](../concepts/token-level-entropy.md), [trajectory diversity](../concepts/trajectory-diversity.md)

## Appears in

- [Thought-Level Beam Search for Reasoning](../../archive/papers/2026/arxiv-2608-08020/summary.md) — Reformulates test-time reasoning as compute allocation over partial trajectories under a hardware budget, and runs a zero-sum beam search over reasoning steps that prunes weak traces and immediately re-spends the freed capacity by branching from high-scoring prefixes.
- [Dynamic Early Exit in Reasoning Models](../../archive/papers/2025/local-a1d9fa1eb8899dfc/summary.md) — Detects the points where a reasoning model switches thought chains, interrupts to induce a trial answer, and stops generation when that answer's confidence is high enough — cutting chain-of-thought length substantially while raising accuracy, with no training.
- [VAR-MATH: Probing True Mathematical Reasoning in LLMs via Symbolic Multi-Instance Benchmarks](../../archive/papers/2026/local-d62cc27b0209da49/summary.md) — Converts AMC23 and AIME24/25 into symbolic templates whose constants are replaced by sampled variables, requires a model to solve several instantiations of each problem, and finds RL-finetuned models lose most of their reported accuracy under that consistency requirement.
- [Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference](../../archive/papers/2025/local-de572e138fc98639/summary.md) — Shows that greedy decoding is not deterministic across hardware: changing GPU type, GPU count or evaluation batch size shifts a reasoning model's AIME'24 accuracy by up to 9 percentage points and its response length by 9,000 tokens under BF16, because floating-point addition is non-associative.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
