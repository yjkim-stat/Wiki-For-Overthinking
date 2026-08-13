# gpt-oss-20b

<!-- auto:begin -->

A 20B open-weight OpenAI reasoning model, used in the archive where open weights are required. One source measures how well it follows instructions inside its reasoning trace and reports an instruction-following score of 0.11, raised to 0.27 by targeted finetuning on synthetic data — so more than doubled and still leaving most traces non-compliant. The other uses it to probe whether chain-of-thought is epiphenomenal, truncating traces and forcing an answer to locate a commitment boundary. Both need access the model's openness provides: trace-level manipulation and per-step intervention.

- **Kind**: model
- **Also called**: GPT OSS 20B, GPT-OSS-20B, gpt-oss-20b
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [alignment](../concepts/alignment.md), [answer stabilization](../concepts/answer-stabilization.md), [chain-of-thought compression](../methods/chain-of-thought-compression.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [commitment boundary](../concepts/commitment-boundary.md), [controllability](../concepts/controllability.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [early exit](../methods/early-exit.md), [Gemma-4-26B-A4B-it](gemma-4-26b-a4b-it.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-OSS](gpt-oss.md), [gpt-oss-120b](gpt-oss-120b.md), [GSM8K](../datasets/gsm8k.md), [instruction following](../concepts/instruction-following.md), [length penalty](../methods/length-penalty.md), [linear probe](../methods/linear-probe.md), [linear probing](../methods/linear-probing.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH500](../datasets/math500.md), [MMLU-Pro](../datasets/mmlu-pro.md), [monitorability](../concepts/monitorability.md), [multi-turn reasoning](../methods/multi-turn-reasoning.md), [Omni-MATH](../datasets/omni-math.md), [optimal stopping](../concepts/optimal-stopping.md), [overthinking](../concepts/overthinking.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-4B](qwen3-4b.md), [Qwen3-8B](qwen3-8b.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [reinforcement learning](../methods/reinforcement-learning.md), [reward hacking](../concepts/reward-hacking.md), [self-correction](../concepts/self-correction.md), [synthetic data generation](../methods/synthetic-data-generation.md), [verbosity](../concepts/verbosity.md), [ZebraLogic](../datasets/zebralogic.md)

## Appears in

- [How Much Does a Reasoning Summary Reveal? An Observability Ladder for Large Language Models](../../archive/papers/2026/arxiv-2608-02089/summary.md) — Holds one completed reasoning run fixed and varies only what a monitor is allowed to inspect — response, self-summary, full trace, internals — and finds the summary's value nearly vanishes once the monitor already has the prompt, so monitorability is a property of the display and the reader jointly rather than of the text.
- [ReasonIF: Large Reasoning Models Fail to Follow Instructions During Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1456/summary.md) — Benchmarks whether reasoning models follow instructions inside their reasoning traces, finding under 25% compliance at best and worse as difficulty rises.
- [Beyond the Commitment Boundary: Probing Epiphenomenal Chain-of-Thought in Large Reasoning Models](../../archive/papers/2026/local-d6e266929de37684/summary.md) — Measures each CoT step's causal contribution by truncating the trace and forcing an answer, finds reasoning crosses a sharp single-step 'commitment boundary' after which the answer probability stops moving, and trains activation probes to detect that boundary and exit early.
- [OS-Pruner: Pruning Chains-of-Thought of Reasoning Models via Optimal Stopping](../../archive/papers/2026/local-dbfa51b5159a1a77/summary.md) — Recasts when-to-stop-reasoning as optimal stopping rather than classification, and proves that a fixed threshold on the probability of being correct can be arbitrarily far from optimal even when that probability is known exactly, because the decision needs the value of continuing and not the value of stopping.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
