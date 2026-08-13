# early exit

<!-- auto:begin -->

Terminating generation before the model would stop on its own. The four sources differ mainly in what signal triggers the exit: confidence in a trial answer induced at a reasoning transition, consistency of periodically probed intermediate answers, a CUSUM change-point statistic on predictive entropy, and an activation probe predicting the answer-formation stage. They report conflicting relationships to accuracy — some find it improves over unrestricted generation, one finds it costs a point or two — and the archive has no head-to-head comparison, though the benchmarks overlap enough to permit one. All four agree that fixed-fraction truncation is the wrong baseline because the right exit point varies per problem.

- **Kind**: method
- **Also called**: dynamic early exit, early stopping
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 6

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC23](../datasets/amc23.md), [answer stabilization](../concepts/answer-stabilization.md), [chain of thought](chain-of-thought.md), [chain-of-thought compression](chain-of-thought-compression.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [commitment boundary](../concepts/commitment-boundary.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER](deer.md), [Dynasor](dynasor.md), [entropy trajectory](../concepts/entropy-trajectory.md), [Gemma-4-26B-A4B-it](../models/gemma-4-26b-a4b-it.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-oss-20b](../models/gpt-oss-20b.md), [GSM8K](../datasets/gsm8k.md), [HumanEval+](../datasets/humaneval.md), [KV cache compression](kv-cache-compression.md), [length penalty](length-penalty.md), [linear probing](linear-probing.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-70B](../models/llama-3-1-70b.md), [MATH500](../datasets/math500.md), [monitorability](../concepts/monitorability.md), [Monte Carlo tree search](monte-carlo-tree-search.md), [OlympiadBench](../datasets/olympiadbench.md), [Omni-MATH](../datasets/omni-math.md), [optimal stopping](../concepts/optimal-stopping.md), [overthinking](../concepts/overthinking.md), [process reward](../concepts/process-reward.md), [process reward model](process-reward-model.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [QwQ-32B](../models/qwq-32b.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [reinforcement learning](reinforcement-learning.md), [self-consistency](self-consistency.md), [test-time compute](../concepts/test-time-compute.md), [token-level entropy](../concepts/token-level-entropy.md), [vLLM](vllm.md), [ZebraLogic](../datasets/zebralogic.md)

## Appears in

- [Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning](../../archive/papers/2026/arxiv-2608-04771/summary.md) — Couples KV-cache compression and generation-length control under a single process-reward signal, compressing harder at high-reward reasoning steps and stopping early when confidence is high.
- [Efficiently Scaling LLM Reasoning with Certaindex](../../archive/papers/2025/local-0c24c3c0e4729108/summary.md) — Defines certaindex, an algorithm-agnostic measure of how much a reasoning algorithm's answer has stopped changing, and builds it into a serving system that reallocates or terminates compute per query — saving up to 50% of tokens in batch inference and tripling online throughput.
- [Unveiling the Entropy Dynamics of Chain-of-Thought Reasoning](../../archive/papers/2026/local-379c0b6966148b4a/summary.md) — Shows that CoT entropy follows a two-phase structure — a high-entropy exploration region that shifts abruptly into a low-entropy convergence region — and detects that shift online with the CUSUM change-point algorithm to drive early exit and trajectory-weighted voting.
- [Dynamic Early Exit in Reasoning Models](../../archive/papers/2025/local-a1d9fa1eb8899dfc/summary.md) — Detects the points where a reasoning model switches thought chains, interrupts to induce a trial answer, and stops generation when that answer's confidence is high enough — cutting chain-of-thought length substantially while raising accuracy, with no training.
- [Beyond the Commitment Boundary: Probing Epiphenomenal Chain-of-Thought in Large Reasoning Models](../../archive/papers/2026/local-d6e266929de37684/summary.md) — Measures each CoT step's causal contribution by truncating the trace and forcing an answer, finds reasoning crosses a sharp single-step 'commitment boundary' after which the answer probability stops moving, and trains activation probes to detect that boundary and exit early.
- [OS-Pruner: Pruning Chains-of-Thought of Reasoning Models via Optimal Stopping](../../archive/papers/2026/local-dbfa51b5159a1a77/summary.md) — Recasts when-to-stop-reasoning as optimal stopping rather than classification, and proves that a fixed threshold on the probability of being correct can be arbitrarily far from optimal even when that probability is known exactly, because the decision needs the value of continuing and not the value of stopping.

<!-- auto:end -->

## Notes

### Corrections log

- **(1)** Claimed the four stopping signals had never been compared. Wrong — the
  CUSUM paper compares against DEER and Dynasor. Only the activation-probe
  signal remains uncompared.
- **(2)** Claimed no follow-up existed to difficulty-conditioned allocation.
  Wrong as a claim about the literature.
- **(3)** *(this pass)* Said training-free difficulty proxies were "not yet in
  this archive." **Now wrong — two are, with opposite properties.** Corrected
  section below.

### The four stopping signals

| Signal | Reads from | Compared? |
| --- | --- | --- |
| Trial-answer confidence at a transition marker (DEER) | forced intermediate answer | vs CUSUM, Dynasor |
| Probed-answer consistency (Certaindex) | forced intermediate answers, ~every 64 tok | vs CUSUM, DEER |
| CUSUM change-point on predictive entropy | output distribution | ran the comparison |
| Activation probe for the commitment boundary | hidden states | **no** |

### The baseline is the unreliable quantity — and now we know why

Same model (DeepSeek-R1-Distill-Qwen-7B), same benchmarks, two papers:

| | DEER paper | CUSUM paper |
| --- | --- | --- |
| AIME24 **vanilla** | 41.7 @ 13,765 tok | **55.63** @ 13,313 tok |
| AIME24 DEER | 49.2 | 46.67 |

DEER's own score is stable across labs; the *baseline* moves 13.9 points at
matched token budgets. **9.15 of those points are now accounted for**: on
exactly this model and benchmark, accuracy standard deviation across GPU type,
GPU count and batch size is 9.15 pp under BF16 with greedy decoding, falling to
0 at FP32. Add 2-4 pp of sampling noise and the gap is largely explained without
either paper erring.

**Verified across the archive: 1 of 45 papers reports numerical precision or
hardware configuration — the paper about it.** Token savings of 5-15% are not
interpretable against a 9,189-token hardware-induced standard deviation on the
same model.

### Difficulty: two estimators, opposite failure profiles

Stopping and allocating are different problems. All four signals above condition
on **convergence**, which is right for stopping and too late for allocating.
The archive now holds three allocation-side entries:

| Approach | Signal | Where it fails |
| --- | --- | --- |
| PRM-guided adaptive configuration | step scores from a process reward model | **degrades at difficulty** — strong on MATH-500 L1-4, weak on L5 |
| **RADAR** | item response theory over an evaluation matrix; latent query difficulty vs configuration ability | needs a calibration matrix; unidimensional ability assumption |
| **Reasoning-strength probe** | linear read of question activations *before generation* | needs activation access; validated on Qwen family |

The third is the important one. The model **already computed the estimate** —
reasoning length is decodable from the prompt's activations at Spearman 0.84,
carried by a single direction whose magnitude scales with difficulty, and it acts
by shifting the logits of `</think>`. So the allocation question changes from
*how do we estimate difficulty* to *how do we read the estimate the model made*.
And unlike the PRM signal, it does not degrade with difficulty — its
demonstrated failure mode is model-family transfer, not hardness.

Also new: **training-side allocation.** DIET conditions the token penalty and
target length on on-the-fly difficulty, and reports that existing compression
methods *disrupt* the natural positive correlation between response length and
problem difficulty. **None of the early-exit papers in this archive reports
whether its savings preserve that relationship** — a method that shortens hard
problems as much as easy ones is doing something other than what its
token-savings number implies. That check is cheap and should be applied to all
four signals above.
