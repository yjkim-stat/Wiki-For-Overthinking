# Answer Convergence

<!-- auto:begin -->

Answer convergence is the observation, shared by all three sources here, that a reasoning model settles on the answer it will finally give well before it stops generating, so the remainder of the trace changes the outcome little. The sources agree on the phenomenon and disagree on where to look for it: one defines an Answer Convergence Ratio by repeatedly truncating the trace, forcing an answer, and finding the earliest chunk after which that answer no longer changes — reporting ratios near 0.0 on NaturalQuestions, about 0.8 on GSM8K and MATH-500 and about 0.9 on GPQA and AIME'24; a second locates it in the confidence of probed intermediate answers, and adds that trajectories which never converge are the expensive ones, averaging over 25K tokens against about 12K for correct ones on Qwen3-4B; a third looks at reasoning-level semantic redundancy instead of the answer at all, and reports that 41-52% of reasoning tokens are generated after the model has already reached its final answer. All three treat convergence as a stopping signal rather than a correctness signal, and the first states plainly that convergence does not guarantee correctness.

- **Kind**: concept
- **Also called**: answer convergence
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Budget Forcing](../methods/budget-forcing.md), [Chain-of-Draft](../methods/chain-of-draft.md), [Concise CoT (CCoT)](../methods/concise-cot-ccot.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER](../methods/deer.md), [Dynasor](../methods/dynasor.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md), [MathVision](../datasets/mathvision.md), [MathVista](../datasets/mathvista.md), [NoThinking](../methods/nothinking.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](overthinking.md), [PLAN-AND-BUDGET](../methods/plan-and-budget.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-4B](../models/qwen3-4b.md), [QwQ-32B](../models/qwq-32b.md), [Reasoning Completion Point (RCP)](reasoning-completion-point-rcp.md)

## Appears in

- [Early Stopping for Large Reasoning Models via Confidence Dynamics](../../archive/papers/2026/local-204ad034bca12641/summary.md) — CoDE-Stop stops reasoning when either a ramping confidence threshold is crossed or an early-step-weighted 'degeneration score' of accumulated confidence instability exceeds a threshold, targeting both trajectories that are already done and trajectories that are going nowhere, and its evaluation is the archive's first independent head-to-head of RCPD and Answer Convergence under one protocol.
- [Answer Convergence as a Signal for Early Stopping in Reasoning](../../archive/papers/2025/local-5596d5f3510679fc/summary.md) — Defines the Answer Convergence Ratio — the fraction of a chain of thought needed before the forced answer stops changing — measures it by incremental truncation across five tasks and five models, and proposes three inference-time stopping methods (answer consistency, a logit boost on the end-of-thinking token, and an LSTM probe over activations), of which only the learned probe holds accuracy on hard tasks.
- [Stop When Reasoning Converges: Semantic-Preserving Early Exit for Reasoning Models](../../archive/papers/2026/local-8ec022e440eb9021/summary.md) — Proposes PUMA, an inference-time early-exit framework that flags reasoning steps as candidate exits when a contrastively-trained embedding detector finds them semantically redundant with recent context, then confirms the exit is safe via answer-level confidence/consistency verification before stopping.

<!-- auto:end -->

## Notes

# Stopping on convergence: what the methods actually read, and what nobody measures

Assembled 2026-09-03. Every method below is read from a record this archive
holds. Where a claim comes from a paper's own table it says so; where it comes
from someone else re-running that method, it says that instead, because the two
disagree and the disagreement is the most useful thing here.

No `analysis-sources` marker, for the reason the overthinking note gives: that
counter is checked against *this note's* evidence, which is the three papers
that use the term "answer convergence". This section rests on about fifteen
readings filed under other entities — RCPD, ThinkBrake, NEAT, BLADE, REFRAIN,
TRACE, ParaTempo, CGRS, THOUGHTTERMINATOR, PUMA, CoDE-Stop, DeepPrune, the
token-complexity study and the multilingual latent-reasoning study — so any
number here would be wrong in both directions at once.

## One phenomenon, six places to look for it

All of these methods rest on the same bet: the model fixes its answer well
before it stops, so there is a moment after which further generation is
redundant. They differ in **what they read to detect that moment**, and the
signals form a ladder from the model's output surface down into its weights.

| Layer | What is read | Methods |
| --- | --- | --- |
| Output string | Does the forced answer stop changing | Answer Consistency (ACR), TRACE-ACS, DeepPrune (across traces) |
| Answer distribution | Confidence / entropy of a probed answer | DEER (one step), CGRS, CoDE-Stop, ParaTempo (time-averaged) |
| Termination token | How strongly `</think>` is preferred | RCPD (its rank), ThinkBrake (its log-margin), Think Token Adjustment (boost its logit) |
| Reasoning semantics | Is new content still appearing | RCP (KL to a terminal distribution), PUMA (embedding similarity), REFRAIN (cosine to prior steps) |
| Activations | Does internal state predict termination | BLADE, Learn-to-Stop, NEAT (exit neurons) |
| Nothing — a budget | A deadline fixed in advance | Budget Force, THOUGHTTERMINATOR |

The ladder is not a ranking. It is a trade of **cost against faithfulness to
what you actually want to know**: the output string is what you care about but
is expensive to probe and brittle across answer formats; the termination token
is free to read but is a proxy; activations are richer but need a trained
probe and white-box access.

## The size of the phenomenon is not in dispute

Four independent measurements, four instruments, one answer:

- **41–52%** of reasoning tokens are generated after the model has already
  reached its final answer (PUMA, across five models).
- The **Answer Convergence Ratio** sits near 0.8 on GSM8K and MATH-500 and near
  0.9 on GPQA and AIME'24 — and near **0.0** on NaturalQuestions, where the
  explicit trace does nothing at all.
- Oracle stopping — cutting at the best boundary in hindsight — recovers
  **61%** of AIME failures while cutting 44% of tokens (ThinkBrake).
- Trajectories that never converge are where the compute goes: **~12K tokens
  for correct rollouts against >25K for incorrect ones** (CoDE-Stop, Qwen3-4B).

That last one is the observation the rest of the cluster does not make.
Every other method asks *is the answer ready*; only CoDE-Stop's degeneration
score asks *is this trajectory going anywhere at all*, which is the question
the token budget is actually being spent on.

## Self-reported results do not survive re-running

This is the finding that most changes how the cluster should be read. When one
paper re-ran the others on shared, pre-generated trajectories:

| Method | Its own paper | Re-run by CoDE-Stop |
| --- | --- | --- |
| RCPD | up to 44% of tokens saved | **0–9%** (CR 96.9 / 91.3 / 100.0 / 96.2 over four models) |
| Answer Convergence | up to 40%, accuracy roughly held | CR 20.3% at **51.1** accuracy against vanilla's 78.4 |

On Qwen3-14B — the one model RCPD's own paper and this evaluation share —
RCPD's reported 60% compression becomes 91.3%.

**This is evidence about a protocol, not a refutation.** The model sets and
benchmark mixes differ, and the re-run reports `Cost > Tok` for RCPD in every
row, which implies it generates intermediate answers where published RCPD only
reads a rank out of the next-token distribution it already has. If that is an
implementation mismatch it would change both the accounting and the trigger.
The right reading is narrower and still uncomfortable: **no method in this
cluster has been independently reproduced at its claimed operating point.**

## What nobody measures: whether the detector detects the thing

Several of these methods define a target offline and then deploy a cheap proxy
for it. Almost none checks that the proxy agrees with the target.

- RCP defines `k_RCP` by a KL residual and a length plateau, then deploys four
  hand-set thresholds on the rank of `</think>` (`R_t ≤ 5`; the ladder
  `[10, 50, 100, 1000]`; `≤ 20` over 3 steps; `≤ 50` over 6). **No precision,
  recall or step-level error against its own gold labels is reported.** A rule
  that ignored `k_RCP` but stopped somewhere reasonable would produce the same
  results table.
- PUMA and CoDE-Stop likewise validate only end-to-end, on accuracy and tokens.
- The exceptions are the learned probes. BLADE labels a boundary by forcing an
  answer 16 times and keeping only unanimous outcomes, and Learn-to-Stop trains
  on labels derived from the model's own converged prediction — both are
  evaluated as predictors, not just as pipelines.

The archive's own reading of RCP flagged this gap before the re-run above
existed; the re-run is what that gap looks like from outside.

## Two accounting rules the cluster keeps rediscovering

**Probing is not free.** CoDE-Stop reports `Cost` — total tokens including
intermediate-answer overhead — and under it Think or Not costs *more* than
vanilla (11,668 against 8,344 on Qwen3-4B) while generating fewer reasoning
tokens. NEAT separately measured CGRS increasing wall-clock 41–63% despite
shortening output. ParaTempo excludes its probe forward passes from its token
counts entirely. PUMA is the one that closes this properly: 1.40× and 1.28×
measured wall-clock speedups with detector overhead of 0.4–1.1%.

**Shallow signals have a difficulty ceiling, and it is low.** Answer
Consistency improves NaturalQuestions (35.0 → 38.4) and GSM8K (89.4 → 91.0)
and then destroys the hard end on the same model: MATH-500 91.0 → 55.0, GPQA
33.3 → 14.1, AIME'24 73.3 → **13.3**. Only its supervised activation probe
holds. This is the same boundary at which the multilingual study finds latent
answer formation vanishing (LRS 0.38 on MGSM, 0.03 on Multilingual AIME) and
the same ordering BLADE reports. Three instruments, one conclusion: **output
consistency is a signal that works exactly where you do not need it.**

## The bound that may make the whole competition small

The token-complexity study fits a per-question floor — the minimum reasoning
length that model needs for that question — and finds that **31 different
compression prompts trace a single accuracy-versus-length curve per (model,
benchmark)**, not one curve per prompt family. Against that floor, achieved
compression is a fraction of what is available: for GPT-4o on MMLU-Pro Math,
BeConcise reaches 415 tokens against DefaultCoT's 586 (1.41×) where the derived
bound allows 121 (4.83×); on GSM8K the bound permits 10.9–11.2× against roughly
1.4× achieved. A budget-guessing baseline sits *below* the curve traced by
simple static prompts.

If that curve is real, the differences argued over above are positions on one
line rather than different lines, and the interesting question stops being
*which signal* and becomes *why is everyone so far from the floor*.

## What would settle the open questions

1. **Detector fidelity.** Report precision/recall of each online rule against
   its own offline target. Cheap, and nobody has done it.
2. **One protocol, published hyperparameters, wall-clock included.** The
   CoDE-Stop table is the first attempt; it needs the original authors'
   implementations, not reimplementations.
3. **Distance to the token-complexity floor** as the reported metric, instead
   of percentage saved against a vanilla baseline that varies per paper.
