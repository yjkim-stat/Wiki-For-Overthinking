# process supervision

<!-- auto:begin -->

Supervising the steps rather than only the outcome, and a line the archive has watched become cheaper. The original obstacle was labels: step-level annotation is expensive, and the archive's sources have now routed around it four ways. It falls out of an outcome reward for free — parameterizing that reward as a policy-to-reference log-likelihood ratio makes the per-step Q value the partial sum, so a process reward model comes from response-level labels alone. It can be borrowed from a privileged teacher, with the token-level teacher-student divergence as the dense signal, then aggregated to turns or concentrated on pivots. It can be read from the model's own trajectory, via entropy instability or state-transition probabilities. And it can be executed, where symbolic templates or an interpreter supply step-level ground truth at no annotation cost. What remains contested is how much it adds: one archived theoretical account argues that if pretraining already separates correct from incorrect chains, an outcome-only gradient inherits that separation, which would explain why process supervision sometimes buys little.

- **Kind**: concept
- **Also called**: process reward, process-supervision, step supervision, step-level supervision
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 14

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [activation patching](../methods/activation-patching.md), [adaptive compute allocation](adaptive-compute-allocation.md), [advantage estimation](advantage-estimation.md), [AIME 2024](../datasets/aime-2024.md), [AMC23](../datasets/amc23.md), [answer aggregation](../methods/answer-aggregation.md), [attention pattern](attention-pattern.md), [backtracking](backtracking.md), [Bamboogle](../datasets/bamboogle.md), [belief state](belief-state.md), [best-of-n](../methods/best-of-n.md), [chain of thought](../methods/chain-of-thought.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [circuit complexity](circuit-complexity.md), [CMIMC](../datasets/cmimc.md), [Coconut](../methods/coconut.md), [component ablation](../methods/component-ablation.md), [compositional generalization](compositional-generalization.md), [consensus](consensus.md), [credit assignment](credit-assignment.md), [curriculum learning](curriculum-learning.md), [DPO](../methods/dpo.md), [effective depth](effective-depth.md), [entropy collapse](entropy-collapse.md), [entropy trajectory](entropy-trajectory.md), [error compounding](error-compounding.md), [exploration-exploitation trade-off](exploration-exploitation-trade-off.md), [expressivity](expressivity.md), [Gemini-1.5-Pro](../models/gemini-1-5-pro.md), [Gemma-3-4B](../models/gemma-3-4b.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [GPT-4o](../models/gpt-4o.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [gpt-oss-20b](../models/gpt-oss-20b.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [HMMT](../datasets/hmmt.md), [HotpotQA](../datasets/hotpotqa.md), [Kimi-K2.5](../models/kimi-k2-5.md), [KL regularization](../methods/kl-regularization.md), [knowledge distillation](../methods/knowledge-distillation.md), [KV cache](kv-cache.md), [latent reasoning](latent-reasoning.md), [length generalization](length-generalization.md), [linear probe](../methods/linear-probe.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [Llama-3-8B](../models/llama-3-8b.md), [LLaVA-OneVision-7B](../models/llava-onevision-7b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [long-horizon reasoning](long-horizon-reasoning.md), [LoRA](../methods/lora.md), [majority voting](../methods/majority-voting.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MathVista](../datasets/mathvista.md), [meta-reasoning](../methods/meta-reasoning.md), [Mistral-7B-v0.3](../models/mistral-7b-v0-3.md), [MMMU-Pro](../datasets/mmmu-pro.md), [monitorability](monitorability.md), [Monte Carlo tree search](../methods/monte-carlo-tree-search.md), [multimodal reasoning](multimodal-reasoning.md), [MuSiQue](../datasets/musique.md), [Natural Questions](../datasets/natural-questions.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [outcome reward](outcome-reward.md), [overthinking](overthinking.md), [pass@k](pass-k.md), [privileged information](privileged-information.md), [process reward](process-reward.md), [process reward model](process-reward-model.md), [Qwen2.5-3B](../models/qwen2-5-3b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen2.5-coder-7B](../models/qwen2-5-coder-7b.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen2.5-VL](../models/qwen2-5-vl.md), [Qwen2.5-VL-3B](../models/qwen2-5-vl-3b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [Qwen2.5-VL-7B-Instruct](../models/qwen2-5-vl-7b-instruct.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B-Instruct-2507](../models/qwen3-4b-instruct-2507.md), [Qwen3.5-27B](../models/qwen3-5-27b.md), [Qwen3-VL-8B](../models/qwen3-vl-8b.md), [ReAct](../methods/react.md), [reasoning depth](reasoning-depth.md), [reinforcement learning](../methods/reinforcement-learning.md), [residual stream](residual-stream.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [reward hacking](reward-hacking.md), [reward shaping](reward-shaping.md), [RLVR](../methods/rlvr.md), [selectivity control](../methods/selectivity-control.md), [self-certainty](../methods/self-certainty.md), [self-consistency](../methods/self-consistency.md), [self-correction](self-correction.md), [state tracking](state-tracking.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [synthetic data generation](../methods/synthetic-data-generation.md), [teacher-student gap](teacher-student-gap.md), [test-time compute](test-time-compute.md), [test-time scaling](test-time-scaling.md), [token efficiency](token-efficiency.md), [token-level distillation](../methods/token-level-distillation.md), [token-level entropy](token-level-entropy.md), [token selection](token-selection.md), [TriviaQA](../datasets/triviaqa.md), [truthfulness](truthfulness.md), [verifiable reward](verifiable-reward.md), [verification](verification.md), [visual grounding](visual-grounding.md)

## Appears in

- [CURV: Enhancing Chart Understanding Through Curriculum Visual Grounded Reasoning](../../archive/papers/2026/arxiv-2608-02833/summary.md) — Reformulates chart question answering as a chain in which every reasoning step carries a predicted image region, trains that pairing through a curriculum graded by nesting depth, and finds explicit intermediate grounding worth 8.78 points over letting the model attend implicitly.
- [Perception Before Reasoning: Dynamic Latent Reasoning for Video Understanding and Question Answering](../../archive/papers/2026/arxiv-2608-04124/summary.md) — Splits a video model's latent computation into perception latents that always ground the question in visual evidence and reasoning latents allocated only when the question needs inference, and shows that reasoning latents without rationale supervision are worse than no reasoning latents at all.
- [AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning](../../archive/papers/2026/arxiv-2608-05987/summary.md) — Turns token-level teacher-student log-probability gaps into turn-level credit for agentic RL by recursively updating a Bayesian belief in log-odds space, identifying pivotal turns without a critic.
- [DASH: Divergence-Adaptive Supervision Horizons for On-Policy Self-Distillation of Reasoning Models](../../archive/papers/2026/arxiv-2608-06243/summary.md) — Weights on-policy self-distillation supervision by how each local teacher-student divergence compares to the sequence mean, gating backward multi-step aggregation on that comparison.
- [RP-OPSD: Reasoning-Pivot-Guided On-Policy Self-Distillation for Multilingual Reasoning Transfer](../../archive/papers/2026/arxiv-2608-06347/summary.md) — Concentrates privileged self-distillation on reasoning pivots identified by the teacher's distributional shift when an English reference solution is added or removed, for multilingual reasoning transfer.
- [VTO: Visual Tool Orchestration for Video Anomaly Detection](../../archive/papers/2026/arxiv-2608-08219/summary.md) — Trains a multimodal agent to orchestrate twelve video-analysis tools for anomaly detection with GRPO under a dual reward that combines exact-match rule checks with an LLM judge scoring logicality, relevance and completeness, and releases the benchmark it is evaluated on.
- [LoongReflect: Boosting Long-Horizon Reflection in Search Agents via Global Perspective Distillation](../../archive/papers/2026/arxiv-2608-11967/summary.md) — Gives a search agent an explicitly reversible trajectory tree with reflect and backtrack as first-class actions, and trains the reflection policy with a dense local signal distilled from a teacher that can see the whole trajectory alongside the sparse terminal reward the local decision is ultimately judged by.
- [Claim-Level Reliability Assessment for Efficient Test-Time Reasoning](../../archive/papers/2026/arxiv-2608-11994/summary.md) — Reallocates half of a test-time sampling budget from generating more solutions to asking the same model to refute a handful of decision-critical claims extracted from each trace, then weights the consensus vote by how many claims survive.
- [MR-ALIGN: Meta-Reasoning Informed Factuality Alignment for Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-204/summary.md) — Improves factuality by reweighting reasoning segments according to state-transition probabilities along the thinking process, targeting a gap where correct facts appear in reasoning but not in the answer.
- [Do Models Read What They Write? Causal Registers in Scratchpad Reasoning](../../archive/papers/2026/local-54a1c25fa51cd59a/summary.md) — Edits the internal representation of a written scratchpad state while holding the printed text fixed, and asks whether the next step follows the transition rule applied to the edited value — turning 'does the model use its scratchpad?' into a causal test with a single correct answer.
- [Free Process Rewards without Process Labels](../../archive/papers/2024/local-b1536fcbe72cb268/summary.md) — Proves that parameterizing an outcome reward as the log-likelihood ratio between a policy and a reference model makes the per-step Q value fall out of the same model for free, so a process reward model can be obtained by training an outcome reward model on response-level labels alone.
- [Optimizing Test-Time Compute via Meta Reinforcement Fine-Tuning](../../archive/papers/2025/local-c45962c819666804/summary.md) — Formalizes 'spend test-time compute well' as a meta-reinforcement-learning problem — treating one long output stream as a sequence of episodes and scoring it by cumulative regret over tokens — and trains against a dense progress bonus that outcome-only reward cannot express.
- [EDIS: Diagnosing LLM Reasoning via Entropy Dynamics](../../archive/papers/2026/local-e64d3a8c4788daf7/summary.md) — Introduces EDIS, a trajectory-level score that measures how unstably token entropy evolves during generation, and uses it to select better reasoning rollouts at inference and to curate training samples in RL.
- [Towards Revealing the Mystery behind Chain of Thought: A Theoretical Perspective](../../archive/papers/2023/local-f3c308f76ff7a114/summary.md) — Proves via circuit complexity that bounded-depth Transformers cannot directly solve basic arithmetic, linear equations or general dynamic programming unless their size grows super-polynomially, while constant-size autoregressive Transformers can solve all of them by generating chain-of-thought derivations.

<!-- auto:end -->

## Notes

### Correction (2026-08-08)

An earlier version of this note said label-free step-level feedback was an open
direction that "nobody in this archive has done." **That was wrong when written
and is now clearly wrong.** It had been done, in 2024, and the archive simply
did not hold the paper.

**Free Process Rewards without Process Labels** proves that if the outcome
reward is parameterized as `r(y) = β·log(π_θ(y)/π_ref(y))`, then the running sum
of per-token log-ratios is *an exact expectation of the outcome reward at each
step* — the Q value. So the process reward for step *t* is just that step's own
log-ratio term, and training an ORM on response-level labels trains a PRM for
free. Reported to beat an MCTS-annotated baseline at 1/38 the FLOPs.

The corrected statement: **three routes to label-free step feedback now exist in
this archive**, and they are genuinely different mechanisms.

| Route | Signal | Status |
| --- | --- | --- |
| Reward parameterization | log-ratio partial sums = Q values | **done**, with proof and bounds |
| Entropy dynamics | local instability within a segmented trajectory | proposed as future work, not done |
| Internal representations | step correctness linearly decodable at 78-86% | probe exists, needs labels to train |

### The finding worth interrogating

That paper reports that **adding real step labels on top of the implicit PRM
brings no further improvement** (49.2 vs 49.3). If true, the field's expensive
annotation effort buys something already obtainable for free.

The authors themselves flag the obvious confound — the step labels came from
MCTS annotation, which is noisy, so the null may reflect label quality rather
than label irrelevance. That is exactly the check this group is positioned to
run: the archive's step-level probing work produces step-correctness labels from
a different source entirely (internal representations, not rollouts), so testing
whether *those* add anything on top of an implicit PRM would separate the two
explanations.

### The cleanest result in the archive

*Towards Revealing the Mystery behind Chain of Thought* runs the comparison
everyone wants: identical problems, identical architecture, with the
direct-answer datasets built by **deleting derivations from the CoT datasets**,
so the only difference is what the loss covers. Step-supervised 3-layer
Transformers reach near-perfect accuracy; answer-only supervision mostly stays
below 60% and fails outright on linear equations at every depth.

The mechanism it gives is complexity-theoretic — answer-only supervision asks a
bounded-depth model for something outside its class. The archive now has a
second, independent mechanism from the state-editing work: running-state
supervision makes a written state *causally readable* by later steps, where
pretrained and answer-only models leave it inert. **Process supervision does two
separable things — it changes what the model can compute, and it changes whether
the trace becomes part of the computation.**

Two under-used results from the same theory paper:

- **Demonstration quality matters less than expected.** Accuracy stays above 95%
  with 30% of training samples missing an intermediate step and carrying a
  single-token corruption.
- **Length extrapolation.** Trained on 1-15 operators, still works at 16-18.
  Step supervision taught a procedure, not a distribution.

### Design rule now available

From the state-editing work: process supervision should favour intermediates
whose consequences can be *checked* — program states, theorem-prover goals,
tool-call arguments, database updates — rather than rewarding plausible
reasoning text. That is a concrete selection criterion, and it is the piece the
entropy-based and probe-based routes above still lack.
