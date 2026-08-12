# Monte Carlo tree search

<!-- auto:begin -->

Search over reasoning states guided by simulated rollouts, one of the structured alternatives to linear chain-of-thought. In this archive it appears as a comparison rather than a contribution: one source runs it against chain-of-thought, least-to-most and tree-of-thought on the same problems and finds it lower in accuracy (75.8% against 84.4% for CoT on AQuA), and another treats it as one of four algorithm archetypes its scheduling metric must cover, using the reward model's mean output as the certainty signal.

- **Kind**: method
- **Also called**: MCTS, Monte Carlo Tree Search
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 5

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [AIME24](../datasets/aime24.md), [AMC23](../datasets/amc23.md), [answer stabilization](../concepts/answer-stabilization.md), [beam search](beam-search.md), [best-of-n](best-of-n.md), [chain of thought](chain-of-thought.md), [CommonsenseQA](../datasets/commonsenseqa.md), [credit assignment](../concepts/credit-assignment.md), [DeepSeek-R1](../models/deepseek-r1.md), [DPO](dpo.md), [Dynasor](dynasor.md), [early exit](early-exit.md), [GPT-OSS](../models/gpt-oss.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama](../models/llama.md), [Llama-3.1-70B](../models/llama-3-1-70b.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [majority voting](majority-voting.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [overthinking](../concepts/overthinking.md), [process reward model](process-reward-model.md), [process supervision](../concepts/process-supervision.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen](../models/qwen.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [QwQ-32B](../models/qwq-32b.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [reinforcement learning with verifiable rewards](../concepts/reinforcement-learning-with-verifiable-rewards.md), [self-consistency](self-consistency.md), [self-correction](../concepts/self-correction.md), [self-reflection](self-reflection.md), [supervised fine-tuning](supervised-fine-tuning.md), [t-SNE](t-sne.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](test-time-scaling.md), [verification](../concepts/verification.md)

## Appears in

- [Efficiently Scaling LLM Reasoning with Certaindex](../../archive/papers/2025/local-0c24c3c0e4729108/summary.md) — Defines certaindex, an algorithm-agnostic measure of how much a reasoning algorithm's answer has stopped changing, and builds it into a serving system that reallocates or terminates compute per query — saving up to 50% of tokens in batch inference and tripling online throughput.
- [Landscape of Thoughts: Visualizing the Reasoning Process of Large Language Models](../../archive/papers/2026/local-1b977d02353e100b/summary.md) — Turns each intermediate step of a reasoning trajectory into a numerical feature vector of distances to the answer choices, projects those into 2D to visualize how trajectories move through answer space, and reuses the same features to build a lightweight verifier for weighted voting.
- [What If We Allocate Test-Time Compute Adaptively?](../../archive/papers/2026/local-80ef8b5ce7217f7c/summary.md) — Replaces uniform test-time compute allocation with a training-free agent that picks reasoning tools, a search strategy and an exploration parameter per problem, using a process reward model both to prune within a trajectory and to select across iterations.
- [Free Process Rewards without Process Labels](../../archive/papers/2024/local-b1536fcbe72cb268/summary.md) — Proves that parameterizing an outcome reward as the log-likelihood ratio between a policy and a reference model makes the per-step Q value fall out of the same model for free, so a process reward model can be obtained by training an outcome reward model on response-level labels alone.
- [Position: Stop Anthropomorphizing Intermediate Tokens as Reasoning/Thinking Traces!](../../archive/papers/2026/local-e62f069bc5144f28/summary.md) — A position paper arguing that reading a reasoning model's intermediate tokens as 'reasoning' or 'thinking' is unsupported by the available evidence and actively harmful, and collating experiments in which trace semantics and solution accuracy come apart.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
