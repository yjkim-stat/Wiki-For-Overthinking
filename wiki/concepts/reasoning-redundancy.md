# reasoning redundancy

<!-- auto:begin -->

The part of a chain of thought that does no work, and the quantity every efficiency method in this archive is trying to identify. Fifteen sources locate it differently — after the answer is derived, where double-checking continues; in tokens with negative marginal log-probability contribution to the correct answer; in segments the model's own likelihood landscape marks as extraneous; in the low-entropy convergence region after a sharp two-phase transition; in review nodes of a dependency graph that have too few descendants or sit too late; in steps receiving little attention from the reasoning-termination token; in later alternative solutions, argued to be actively harmful rather than merely wasteful; and in structure inherited from a teacher whose capacity did not match the student's. **This note previously recorded that no source compared these criteria on the same trace. One now does**, and the answer reframes the disagreement rather than settling it: at step granularity three importance criteria overlap 70-80% on which steps to *preserve* while diverging on which to *delete*, so the criteria converge on a shared reasoning backbone and differ only over interchangeable filler; at token granularity the agreement collapses, and only symbol-aware scoring avoids deleting operators and numbers. That study also refutes the premise several archived methods rest on, reporting that pruning which deliberately targets reflective statements performs no better than pruning that ignores them, because redundancy in long traces is diffuse — the skeleton is repeated and rephrased throughout rather than concentrated in a nameable class of step. Two caveats keep the question open: the comparison covers three generic scoring functions in a distillation setting, so the reasoning-specific criteria above are still untested against each other, and the 70-80% figure is a light-compression number that falls by half at aggressive ratios. Reported reductions run from roughly 40% to 87%, sometimes with accuracy gains.

- **Kind**: concept
- **Also called**: inert reasoning, invalid thinking, redundant reasoning
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 15

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [AIME](../datasets/aime.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [answer stabilization](answer-stabilization.md), [attention analysis](../methods/attention-analysis.md), [chain of thought](../methods/chain-of-thought.md), [chain-of-thought compression](../methods/chain-of-thought-compression.md), [chain of thought distillation](../methods/chain-of-thought-distillation.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [commitment boundary](commitment-boundary.md), [compounding error](compounding-error.md), [credit assignment](credit-assignment.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER](../methods/deer.md), [DPO](../methods/dpo.md), [Dynasor](../methods/dynasor.md), [early exit](../methods/early-exit.md), [entropy trajectory](entropy-trajectory.md), [foresight](foresight.md), [Gemini-2.5-Flash](../models/gemini-2-5-flash.md), [Gemma-4-26B-A4B-it](../models/gemma-4-26b-a4b-it.md), [generative rewriting](../methods/generative-rewriting.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-oss-20b](../models/gpt-oss-20b.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [HumanEval+](../datasets/humaneval.md), [KV cache compression](../methods/kv-cache-compression.md), [length control](../methods/length-control.md), [length penalty](../methods/length-penalty.md), [linear probe](../methods/linear-probe.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [LoRA](../methods/lora.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MMLU-Pro](../datasets/mmlu-pro.md), [monitorability](monitorability.md), [OlympiadBench](../datasets/olympiadbench.md), [Omni-MATH](../datasets/omni-math.md), [optimal stopping](optimal-stopping.md), [overthinking](overthinking.md), [Pareto frontier](pareto-frontier.md), [predictive entropy](predictive-entropy.md), [preference optimization](../methods/preference-optimization.md), [process reward](process-reward.md), [process reward model](../methods/process-reward-model.md), [prompt difficulty](prompt-difficulty.md), [Qwen2.5](../models/qwen2-5.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [QwQ-32B](../models/qwq-32b.md), [reasoning distillation](../methods/reasoning-distillation.md), [reasoning skeleton](reasoning-skeleton.md), [reinforcement learning](../methods/reinforcement-learning.md), [reinforcement learning post-training](../methods/reinforcement-learning-post-training.md), [restructuring level](restructuring-level.md), [reward shaping](reward-shaping.md), [self-consistency](../methods/self-consistency.md), [self-correction](self-correction.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time compute](test-time-compute.md), [test-time scaling](../methods/test-time-scaling.md), [token efficiency](token-efficiency.md), [token-level entropy](token-level-entropy.md), [token selection](token-selection.md), [TokenSkip](../methods/tokenskip.md), [vLLM](../methods/vllm.md), [ZebraLogic](../datasets/zebralogic.md)

## Appears in

- [Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning](../../archive/papers/2026/arxiv-2608-04771/summary.md) — Couples KV-cache compression and generation-length control under a single process-reward signal, compressing harder at high-reward reasoning steps and stopping early when confidence is high.
- [FoE: Forest of Errors Makes the First Solution the Best in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1128/summary.md) — Finds that a reasoning model's first solution is usually its best and that later alternatives are actively harmful, characterizes the errors as a forest structure, and prunes accordingly.
- [Think Better, Not Longer: Token-Level Marginal Utility for Efficient Reasoning in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1386/summary.md) — Defines a token's marginal utility as its log-probability gain for the ground-truth answer, then trains against negative-utility tokens to shorten chains of thought.
- [Optimizing Length Compression in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-146/summary.md) — Identifies double-checking after the correct answer is already derived as 'invalid thinking', and trains a GRPO variant with a compress reward that targets exactly that portion.
- [Think How to Think: Mitigating Overthinking with Autonomous Difficulty Cognition in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1766/summary.md) — Two-stage fine-tuning that first injects difficulty cues into output prefixes for prospective strategy selection, then injects redundancy cues mid-reasoning for retrospective correction.
- [Your Reasoning Model Knows What Counts: Self-Guided Chain-of-Thought Pruning for Efficient Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-25/summary.md) — Prunes chain-of-thought segments the model's own likelihood landscape marks as extraneous, then trains on the resulting pruning preference pairs.
- [Neural Chain-of-Thought Search: Searching the Optimal Reasoning Path to Enhance Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1149/summary.md) — Reformulates reasoning as a search over thinking strategies, showing sparse reasoning paths exist that are simultaneously more accurate and shorter than standard outputs.
- [DRP: Distilled Reasoning Pruning with Mathematical Skill-aware Step Decomposition for Efficient Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-196/summary.md) — Has a teacher decompose and prune a student's reasoning by mathematical skill, then distills the pruned paths back, on the argument that CoT structure must match student capacity.
- [Unveiling the Entropy Dynamics of Chain-of-Thought Reasoning](../../archive/papers/2026/local-379c0b6966148b4a/summary.md) — Shows that CoT entropy follows a two-phase structure — a high-entropy exploration region that shifts abruptly into a low-entropy convergence region — and detects that shift online with the CUSUM change-point algorithm to drive early exit and trajectory-weighted voting.
- [CRISP: Compressing Redundancy in Chain-of-Thought via Intrinsic Saliency Pruning](../../archive/papers/2026/local-39eae4c377c77302/summary.md) — Finds that the </think> token aggregates the reasoning chain in deep layers and that attention paid to it from that position ranks which steps matter, then uses that ranking to drive a four-operator compression search — cutting 58% of tokens with accuracy holding.
- [When Compression Helps and When It Hurts: Condition-Aware Analysis of Chain-of-Thought Distillation](../../archive/papers/2026/local-4acfffb647c2e41f/summary.md) — Runs the head-to-head this literature had been missing, comparing three importance criteria on the same traces at matched compression ratios, and finds step-level criteria agree on what to keep while disagreeing on what to cut — because redundancy is diffuse rather than located in any identifiable class of step.
- [Dynamic Early Exit in Reasoning Models](../../archive/papers/2025/local-a1d9fa1eb8899dfc/summary.md) — Detects the points where a reasoning model switches thought chains, interrupts to induce a trial answer, and stops generation when that answer's confidence is high enough — cutting chain-of-thought length substantially while raising accuracy, with no training.
- [Graph-Based Chain-of-Thought Pruning for Reducing Redundant Reflections in Reasoning LLMs](../../archive/papers/2026/local-d3ff7e5088463145/summary.md) — Turns a linear chain of thought into a dependency DAG, labels each node as advancing the frontier or reviewing it, and prunes review nodes on two graph criteria — too few descendants, or too late in the trace — cutting 42% of tokens while accuracy holds or rises.
- [Beyond the Commitment Boundary: Probing Epiphenomenal Chain-of-Thought in Large Reasoning Models](../../archive/papers/2026/local-d6e266929de37684/summary.md) — Measures each CoT step's causal contribution by truncating the trace and forcing an answer, finds reasoning crosses a sharp single-step 'commitment boundary' after which the answer probability stops moving, and trains activation probes to detect that boundary and exit early.
- [OS-Pruner: Pruning Chains-of-Thought of Reasoning Models via Optimal Stopping](../../archive/papers/2026/local-dbfa51b5159a1a77/summary.md) — Recasts when-to-stop-reasoning as optimal stopping rather than classification, and proves that a fixed threshold on the probability of being correct can be arbitrarily far from optimal even when that probability is known exactly, because the decision needs the value of continuing and not the value of stopping.

<!-- auto:end -->

## Notes

### The comparison that was missing has now been run — on three of the criteria

This note used to end by observing that the archive's criteria for locating
redundancy had never been compared against each other on the same trace, so
whether they marked the same tokens was unknown. That was the archive's
sharpest open question in this cluster and it is now partly answered. The
answer has three parts and only the first is what anyone expected.

**They agree on what to keep and disagree on what to cut.** Three importance
criteria — a learned saliency score, entropy, and negative log-likelihood — run
through the same prune pipeline on the same traces at matched ratios overlap
70-80% on the *preserved* step set while diverging on the deleted one. Read
directly: the criteria are all recovering one reasoning skeleton, and they
differ only over which interchangeable elaboration to drop. That explains
something the archive had recorded without explaining, namely why a dozen
independently designed criteria all report large reductions with accuracy
intact. The number decays, though — the same pairs fall to 0.36-0.38 Jaccard at
a 0.5 prune ratio, which is exactly the regime where the choice would matter.

**Granularity, not the criterion, is the real variable.** At token level the
agreement collapses: entropy and NLL each delete 30% of symbol and math tokens
where the learned score deletes 15%, shifting its cuts onto stopwords. A
controlled ablation closes it — simply forbidding the probability-based scores
to touch math tokens erases most of their disadvantage. So the operative
property is symbol preservation, not score quality.

**Redundancy is diffuse, which refutes a premise several archived methods rest
on.** Reflective steps are 30.2% of a long trace, and pruning that deliberately
targets them is reported to do no better than pruning that ignores them,
because the skeleton is repeated and rephrased throughout rather than padded at
nameable points. Three entries in this archive are built on the opposite
assumption — a graph pruner that removes reflection branches and late
re-verification, a reward-coordinated method that penalizes reflection tokens,
and an early-exit rule that treats reflection transitions as candidate stopping
points. None of them is refuted outright, because none was tested against a
reflection-agnostic control; that is precisely the baseline they do not run.

### What the answer does not cover

The comparison is of three generic scoring functions in a **distillation**
setting — compressing teacher traces to supervise a student. The archive's own
criteria are mostly neither: marginal utility against the gold answer, process
reward, the model's likelihood landscape over semantic units, a commitment
boundary located by truncation, a CUSUM change-point in predictive entropy,
attention from the reasoning-termination token, graph descendant count and
relative depth, skill-aware decomposition. None of those is in the comparison.
So the honest state is that the *shape* of the answer is known — convergence on
a skeleton, divergence on filler, diffuse rather than localized redundancy —
while whether it holds for the criteria this archive actually collects is not.

One archived result cuts against reading the convergence too strongly. Removing
the same number of tokens by graph role rather than by position costs five
accuracy points where naive length truncation costs twenty-five. If all criteria
were recovering the same skeleton and the rest were interchangeable, position
should not matter that much. The two findings are compatible — truncation
removes a contiguous suffix rather than a scattered subset — but the gap is
large enough to be worth resolving.

### The cheapest experiment left

Run the archive's own criteria head to head: score the same traces with three
or four of them, report pairwise overlap on preserved and deleted sets at
matched ratios, and include a reflection-agnostic control. The comparison study
supplies the protocol; nothing about it requires new methodology, and it would
convert a dozen incomparable efficiency papers into one ranked set.

A second, smaller one follows from the stopping side. It is now proved that a
fixed threshold on the probability that a prefix is already correct can be
arbitrarily far from optimal, because the decision needs the value of
continuing rather than the value of stopping. Every threshold-based method in
this archive is on the wrong side of that result, and none has been measured
against a continuation-value policy on the same traces.

### The tension this note has not stated

Two results in the archive point opposite ways about the same class of token,
and nothing here has said so.

`finding:752ed6cea6e824bd` establishes that a small set of reflective
transition tokens does disproportionate work, on three quantities measured
independently: mutual information with the answer spikes at steps that decode
to *So*, *Hmm*, *Wait* and *Therefore* and are 0.51-4.8% of a trajectory;
suppressing seventeen of them costs 17 to 30 accuracy points where suppressing
the same number of randomly chosen tokens costs almost nothing; and in RaML's
optimization view a single `Hold on` moves the objective by 279.50 against a
mean of 0.96.

The comparison study says pruning that targets reflective statements does no
better than pruning that ignores them.

These are not contradictory, and the note should not pretend they resolve.
*Some particular reflective tokens are load-bearing* and *reflective sentences
are a good marker of what to remove* are different claims, and every source
above measures only one of them. What is missing is the experiment that
separates them: rank reflective steps by a causal criterion — MI, or the
answer's own log-probability — and prune only the bottom of that ranking, with
a reflection-agnostic control at matched token count. If the load-bearing
tokens are a thin subset of a large reflective class, both results hold at once
and the practical rule follows immediately. Nobody has run it.

Note also that the two literatures do not use the same unit. The suppression
experiments act on *tokens*, the pruning methods on *steps* or *sentences*, and
this note has already recorded that granularity, not the criterion, is the real
variable at this scale. That alone could account for the whole disagreement,
which is another reason not to file it as settled.

<!-- analysis-sources: 15 -->
