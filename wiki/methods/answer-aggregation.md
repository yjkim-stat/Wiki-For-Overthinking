# answer aggregation

<!-- auto:begin -->

The rule that turns several sampled answers into one, and the part of test-time scaling that all three sources change rather than the sample count. Majority voting is the default they depart from: one weights each trace by how many of its decision-critical claims survive an attempted refutation, one weights by a score-guided beam's running estimate, and one leaves the rule alone and varies the input instead. The reason to treat it as a lever is measured -- when self-consistency is wrong although a correct candidate is already among the samples, changing only the aggregation recovers roughly 37% of those cases. It is also where the archive's finding that extra samples strengthen whatever the rule already does gets its remedy.

- **Kind**: method
- **Also called**: answer aggregation, vote aggregation
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [beam search](beam-search.md), [best-of-n](best-of-n.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [CMIMC](../datasets/cmimc.md), [compute allocation](../concepts/compute-allocation.md), [consensus](../concepts/consensus.md), [DeepSeek-R1-0528-Qwen3-8B](../models/deepseek-r1-0528-qwen3-8b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [gpt-oss-20b](../models/gpt-oss-20b.md), [HMMT](../datasets/hmmt.md), [KV cache](../concepts/kv-cache.md), [linear probe](linear-probe.md), [majority voting](majority-voting.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [MMMU](../datasets/mmmu.md), [Monte Carlo tree search](monte-carlo-tree-search.md), [pass@k](../concepts/pass-k.md), [prefix caching](prefix-caching.md), [process reward model](process-reward-model.md), [process supervision](../concepts/process-supervision.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [Qwen3.5-27B](../models/qwen3-5-27b.md), [self-consistency](self-consistency.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](../concepts/test-time-scaling.md), [trajectory diversity](../concepts/trajectory-diversity.md), [verifier-free verification](verifier-free-verification.md), [vLLM](vllm.md)

## Appears in

- [Thought-Level Beam Search for Reasoning](../../archive/papers/2026/arxiv-2608-08020/summary.md) — Reformulates test-time reasoning as compute allocation over partial trajectories under a hardware budget, and runs a zero-sum beam search over reasoning steps that prunes weak traces and immediately re-spends the freed capacity by branching from high-scoring prefixes.
- [Test-Time Augmentation for LLMs: When Input Diversity Beats Output Diversity at Matched Compute](../../archive/papers/2026/arxiv-2608-09351/summary.md) — Asks whether a fixed inference budget buys more accuracy spent on varying the input than on varying the reasoning path, and finds paraphrase aggregation beats self-consistency on five of six benchmarks at matched compute.
- [Claim-Level Reliability Assessment for Efficient Test-Time Reasoning](../../archive/papers/2026/arxiv-2608-11994/summary.md) — Reallocates half of a test-time sampling budget from generating more solutions to asking the same model to refute a handful of decision-critical claims extracted from each trace, then weights the consensus vote by how many claims survive.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
