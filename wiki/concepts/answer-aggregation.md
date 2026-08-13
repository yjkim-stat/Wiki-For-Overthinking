# answer aggregation

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [beam search](../methods/beam-search.md), [best-of-n](../methods/best-of-n.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [CMIMC](../datasets/cmimc.md), [compute allocation](compute-allocation.md), [DeepSeek-R1-0528-Qwen3-8B](../models/deepseek-r1-0528-qwen3-8b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [gpt-oss-20b](../models/gpt-oss-20b.md), [HMMT](../datasets/hmmt.md), [KV cache](kv-cache.md), [linear probe](../methods/linear-probe.md), [majority voting](../methods/majority-voting.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [MMMU](../datasets/mmmu.md), [Monte Carlo tree search](../methods/monte-carlo-tree-search.md), [pass@k](../methods/pass-k.md), [process reward model](../methods/process-reward-model.md), [process supervision](process-supervision.md), [prompt sensitivity](prompt-sensitivity.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [Qwen3.5-27B](../models/qwen3-5-27b.md), [self-consistency](../methods/self-consistency.md), [test-time compute](test-time-compute.md), [test-time scaling](../methods/test-time-scaling.md), [trajectory diversity](trajectory-diversity.md), [vLLM](../methods/vllm.md)

## Appears in

- [Thought-Level Beam Search for Reasoning](../../archive/papers/2026/arxiv-2608-08020/summary.md) — Reformulates test-time reasoning as compute allocation over partial trajectories under a hardware budget, and runs a zero-sum beam search over reasoning steps that prunes weak traces and immediately re-spends the freed capacity by branching from high-scoring prefixes.
- [Test-Time Augmentation for LLMs: When Input Diversity Beats Output Diversity at Matched Compute](../../archive/papers/2026/arxiv-2608-09351/summary.md) — Asks whether a fixed inference budget buys more accuracy spent on varying the input than on varying the reasoning path, and finds paraphrase aggregation beats self-consistency on five of six benchmarks at matched compute.
- [Claim-Level Reliability Assessment for Efficient Test-Time Reasoning](../../archive/papers/2026/arxiv-2608-11994/summary.md) — Reallocates half of a test-time sampling budget from generating more solutions to asking the same model to refute a handful of decision-critical claims extracted from each trace, then weights the consensus vote by how many claims survive.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
