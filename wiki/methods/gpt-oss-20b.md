# GPT-OSS-20B

<!-- auto:begin -->

GPT-OSS-20B is a language model that archived papers evaluate on, not a concept, method or dataset; the wiki has no kind for a model, so it is filed under the least wrong of the three available. ParaTempo uses it, with Qwen3.5-35B-A3B, as a backbone for training-free parallel reasoning: on GPT-OSS-20B mean latency falls 32.2% (129.7s to 88.0s) and tokens 18.1%, but accuracy falls from self-consistency's 71.8% to 68.0%, and on HMMT26 the model is the paper's worst cell at 5.3 points below SC@16 -- a larger efficiency gain and a larger accuracy cost than on the Qwen backbone. FROST prunes attention-marked sentence-level reasoning outliers from chains of thought produced by GPT-OSS-20B and Phi-4-Reasoning, reporting a 69.68% average token reduction and 26.70% average accuracy gain over the base model across GSM8K, MATH500, AIME24 and Minerva. Both treat it as an off-the-shelf reasoning model whose chain of thought is long enough to be worth cutting; neither reports its architecture or training.

- **Kind**: method
- **Also called**: GPT-OSS, gpt-oss-20b
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2026](../datasets/aime-2026.md), [best-of-n selection](best-of-n-selection.md), [DRP](drp.md), [Efficient Reasoning](../concepts/efficient-reasoning.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-oss-120b](gpt-oss-120b.md), [GSM8K](../datasets/gsm8k.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [Phi-4-Reasoning](phi-4-reasoning.md), [Self-Consistency](self-consistency.md), [SelfBudgeter](selfbudgeter.md), [Test-Time Scaling](../concepts/test-time-scaling.md), [Thinkless](thinkless.md), [Token Budget](../concepts/token-budget.md), [vLLM](vllm.md)

## Appears in

- [ParaTempo: Efficient Parallel Reasoning via Temporal Confidence](../../archive/papers/2026/arxiv-2608-16425/summary.md) — A training-free controller for parallel reasoning that probes each branch every 500 tokens for a tentative answer distribution, averages recent probes into a 'temporal confidence' score, and uses that one signal to prune, retire, fork and globally stop branches.
- [Disagree to Explore, Agree to Commit: Routing-Guided Test-Time Scaling for Software Agents](../../archive/papers/2026/arxiv-2608-22191/summary.md) — Risa reads the MoE router's expert-selection trace as a behavioral fingerprint of what a software agent is doing, using it to push sibling actions away from recently repeated computation during exploration and toward peer agreement once a patch is being written, then to arbitrate among completed attempts without an external judge or test execution.
- [FROST: Filtering Reasoning Outliers with Attention for Efficient Reasoning](../../archive/papers/2026/title-e2cdfd631cb4eda0/summary.md) — FROST uses attention weights to identify and prune sentence-level 'reasoning outliers' from a reasoning model's chain of thought, reporting an average 69.68% token reduction and 26.70% accuracy gain over the base model on four maths benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
