# self-consistency

<!-- auto:begin -->

Sampling several reasoning paths and taking the most common answer, the archive's default aggregation baseline — and now with its failure mode proved rather than observed. Its success probability converges to zero, not to a plateau, whenever some incorrect answer is individually more likely than the correct one: with 46% against 45%, more samples make the wrong answer certain. That is why the archive's stronger methods either refine before voting, weight trajectories by an internal signal, or replace voting with pairwise comparison, which carries a guarantee that majority does not. On the cost side it is the target of most stopping work here: an optimal Bayesian rule proves that tracking the leading answer's count and its margin over the runner-up is asymptotically all that is needed, and several methods stop once the answer has stopped changing. One source goes further and argues later samples are not merely redundant but harmful, since errors accumulate with test-time compute.

- **Kind**: method
- **Also called**: SC, majority voting, self-consistency decoding
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 9

**Related**: [activation patching](activation-patching.md), [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [answer stabilization](../concepts/answer-stabilization.md), [beam search](beam-search.md), [best-of-n](best-of-n.md), [chain of thought](chain-of-thought.md), [compounding error](../concepts/compounding-error.md), [curriculum learning](../concepts/curriculum-learning.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER](deer.md), [Dynasor](dynasor.md), [early exit](early-exit.md), [effective depth](../concepts/effective-depth.md), [entropy collapse](../concepts/entropy-collapse.md), [entropy trajectory](../concepts/entropy-trajectory.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-4o](../models/gpt-4o.md), [greedy decoding](greedy-decoding.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [information bottleneck](../concepts/information-bottleneck.md), [latent chain of thought](latent-chain-of-thought.md), [linear probing](linear-probing.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-70B](../models/llama-3-1-70b.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [LLM-as-a-judge](llm-as-a-judge.md), [majority voting](majority-voting.md), [MATH](../datasets/math.md), [MATH-500](../datasets/math-500.md), [MATH500](../datasets/math500.md), [MMLU-PRO](../datasets/mmlu-pro.md), [monosemanticity](../concepts/monosemanticity.md), [Monte Carlo tree search](monte-carlo-tree-search.md), [OlympiadBench](../datasets/olympiadbench.md), [optimal stopping](../concepts/optimal-stopping.md), [overthinking](../concepts/overthinking.md), [pass-k](pass-k.md), [process supervision](../concepts/process-supervision.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen2.5](../models/qwen2-5.md), [Qwen2.5-0.5B](../models/qwen2-5-0-5b.md), [Qwen2.5-1.5B](../models/qwen2-5-1-5b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-14B](../models/qwen3-14b.md), [QwQ-32B](../models/qwq-32b.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [reward hacking](../concepts/reward-hacking.md), [self-certainty](self-certainty.md), [self-correction](../concepts/self-correction.md), [self-verification](../concepts/self-verification.md), [sparse autoencoder](sparse-autoencoder.md), [superposition](../concepts/superposition.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](test-time-scaling.md), [token-level entropy](../concepts/token-level-entropy.md), [verification](../concepts/verification.md)

## Appears in

- [Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning](../../archive/papers/2026/arxiv-2608-05643/summary.md) — Spends test-time compute on iteratively refining each sampled rollout rather than on drawing more of them, then majority-votes the refined answers, with no verifier.
- [FoE: Forest of Errors Makes the First Solution the Best in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1128/summary.md) — Finds that a reasoning model's first solution is usually its best and that later alternatives are actively harmful, characterizes the errors as a forest structure, and prunes accordingly.
- [Efficiently Scaling LLM Reasoning with Certaindex](../../archive/papers/2025/local-0c24c3c0e4729108/summary.md) — Defines certaindex, an algorithm-agnostic measure of how much a reasoning algorithm's answer has stopped changing, and builds it into a serving system that reallocates or terminates compute per query — saving up to 50% of tokens in batch inference and tripling online throughput.
- [Unveiling the Entropy Dynamics of Chain-of-Thought Reasoning](../../archive/papers/2026/local-379c0b6966148b4a/summary.md) — Shows that CoT entropy follows a two-phase structure — a high-entropy exploration region that shifts abruptly into a low-entropy convergence region — and detects that shift online with the CUSUM change-point algorithm to drive early exit and trajectory-weighted voting.
- [Optimal Bayesian Stopping for Efficient Inference of Consistent LLM Answers](../../archive/papers/2026/local-5c4c22504406a6aa/summary.md) — Stops self-consistency sampling by Bayesian posterior over which answer is the mode, and proves that tracking only the top two answer counts plus an aggregate is enough for asymptotic optimality.
- [Capabilities and Fundamental Limits of Latent Chain-of-Thought](../../archive/papers/2026/local-6b66615b7bf3ef86/summary.md) — Explains why latent chain-of-thought excels at exploration but fails at computation by identifying decisional certainty as the governing variable, formalizing it as the Symbolic Index, and proving that curriculum learning is not merely helpful but necessary for training latent reasoners.
- [Step-Level Sparse Autoencoder for Reasoning Process Interpretation](../../archive/papers/2026/local-d9699040f5220b4c/summary.md) — Trains a sparse autoencoder over whole reasoning steps rather than tokens, conditioning both encoder and decoder on the preceding trajectory so the sparse code carries only what the step adds, and shows that step correctness, logicality, length and first token are all linearly decodable from that code.
- [Provable Scaling Laws for the Test-Time Compute of Large Language Models](../../archive/papers/2025/local-e5ae26db2daac1d7/summary.md) — Gives two aggregation algorithms whose failure probability provably decays to zero as inference compute grows, assuming only that the model can sometimes be right and can compare two solutions better than chance.
- [EDIS: Diagnosing LLM Reasoning via Entropy Dynamics](../../archive/papers/2026/local-e64d3a8c4788daf7/summary.md) — Introduces EDIS, a trajectory-level score that measures how unstably token entropy evolves during generation, and uses it to select better reasoning rollouts at inference and to curate training samples in RL.

<!-- auto:end -->

## Notes

### It is the baseline everyone beats the same way

Two archived papers independently replace the equal vote with a weight derived
from entropy behaviour, and both report the margin **growing** with the number
of sampled trajectories rather than closing:

- *Unveiling the Entropy Dynamics* weights by the final CUSUM statistic — how
  decisively the trajectory converged — and reaches a 3.33% lead at N = 64 on
  AIME25.
- *EDIS* weights by trajectory instability through score-weighted Borda voting,
  reaching 60.6% against 46.2% for majority voting at m = 16.
- *Landscape of Thoughts* trains a random forest on answer-distance features and
  passes 65% on StrategyQA at 50 trajectories where unweighted voting saturates
  near 30%.

Three different signals, same conclusion: with enough samples, **aggregation is
the binding constraint, not sampling**. Self-consistency's failure mode has a
mechanism attached, from *Landscape of Thoughts* — incorrect trajectories
converge to their wrong answer *earlier* than correct ones converge to the right
one, so counting votes systematically rewards the failure mode.

### What this implies for reading new papers

A method that beats self-consistency at N = 4 is barely evidence. The
interesting quantity is the slope against N, and whether the baseline has
saturated in the range shown. Two of the three results above only become
convincing past N = 16, and the third's headline gap is measured on the single
dataset where the baseline saturates lowest.
