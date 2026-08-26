# gpt-oss-120b

<!-- auto:begin -->

gpt-oss-120b is an open-weight language model that archived papers evaluate on, not a concept, method or dataset; the wiki has no kind for a model, so it is filed under the least wrong of the three available. Risky Business runs it as one of seven open-weight reasoning models on HazMart (77 hand-written agentic shopkeeper scenarios, 11 harm categories, 5 runs each) scoring chain-of-thought faithfulness against safe action under Targeted Reasoning Replacement -- the comparison in which four of the seven models exceed 80% faithfulness, QwQ-32B is best on both axes at about 75%, and DeepSeek-R1-Distill-Llama-70B is the most faithful at 97.5% while acting safely in only 12.3% of cases; the model's own figures are not given in the archived record. Adaptive Thinking uses it as one of four backbones, with Qwen3-8B, Qwen3-235B-A22B and Intern-S1-mini, for Sonata, an adapter that predicts a query's self-consistency from last-layer hidden states at prefill and sets the thinking budget before any thinking tokens are generated. Neither paper says anything about the model's architecture, training or provenance: it appears only as something to run a method on.

- **Kind**: method
- **Also called**: GPT-OSS-120B
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [adaptive test-time compute](../concepts/adaptive-test-time-compute.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [best-of-n selection](best-of-n-selection.md), [Chain-of-thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [Chain-of-thought monitorability](../concepts/chain-of-thought-monitorability.md), [Compute-optimal inference](../concepts/compute-optimal-inference.md), [GPQA](../datasets/gpqa.md), [GPT-OSS-20B](gpt-oss-20b.md), [GSM8K](../datasets/gsm8k.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [Qwen3-8B](qwen3-8b.md), [QwQ-32B](qwq-32b.md), [Self-Consistency](self-consistency.md), [Test-Time Scaling](../concepts/test-time-scaling.md)

## Appears in

- [Risky Business: Measuring The Faithfulness-Safety Tension](../../archive/papers/2026/arxiv-2608-03745/summary.md) — Introduces HazMart (77 hand-written agentic shopkeeper scenarios) and Targeted Reasoning Replacement, a search-and-replace edit of a model's own reasoning trace, and shows that models which follow their traces more faithfully also follow tampered unsafe traces more often, with two anti-correlated residual-stream directions in QwQ-32B that can be steered independently.
- [Disagree to Explore, Agree to Commit: Routing-Guided Test-Time Scaling for Software Agents](../../archive/papers/2026/arxiv-2608-22191/summary.md) — Risa reads the MoE router's expert-selection trace as a behavioral fingerprint of what a software agent is doing, using it to push sibling actions away from recently repeated computation during exploration and toward peer agreement once a patch is being written, then to arbitrate among completed attempts without an external judge or test execution.
- [Adaptive Thinking: Large Language Models Know When to Think in Latent Space](../../archive/papers/2026/title-cc91145094e2b147/summary.md) — Sonata predicts a query's self-consistency from the last-layer hidden state at prefill and uses that prediction to set the thinking budget before the model starts reasoning.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
