<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Zero Gap Is Not Restoration: Stratified Per-Question Probability Evaluation and Step-wise Mitigation of Benchmark Contamination

- **Authors**: Ruijie Hou, Yueyang Jiao, Zhao Wang, Yingming Li
- **Venue**: cs.CL
- **Published**: 2026-08-07
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.07341>
- **PDF**: <https://arxiv.org/pdf/2608.07341v1>
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.50

## In one line

Shows that the standard metric for judging contamination-mitigation strategies can be scored by cancellation rather than by restoration, replaces it with a per-question stratified metric under which the published ranking reverses, and proposes a mitigation that decides its intervention during decoding instead of from a prior estimate.

## Problem

Test data leaks into pretraining corpora and inflates benchmark scores. One response is contamination-mitigation evaluation: build no new dataset, but intervene during decoding to suppress memorization and restore the contaminated model's genuine capability. Whether a mitigation strategy actually restores anything must be checked against a reliable metric, and the metric used throughout that literature -- the gap of aggregate performance -- assigns each question a discrete correct/incorrect mark, averages over the dataset, and takes the difference from the clean model's average. Both halves of that are broken, and because the metric shapes how strategies are designed, the damage is not confined to the scoreboard.

## Contributions

- A demonstration that a zero aggregate gap certifies nothing: over-suppression on some questions cancels under-suppression on others
- SA-PPG, a metric that reads zero if and only if every question's solve probability matches the clean model's, and that is stratified so a trivial strategy cannot score well by chasing the clean model's most frequent value
- A rank reversal on published strategies: the method that looks near-perfect under the old metric is barely better than no intervention under the new one
- RailCap, a mitigation that replaces the pre-hoc contamination estimate with step-wise supervision during generation

## Method

The metric is rebuilt in three steps. First the readout: a single sampled response marked 0/1 is a Bernoulli draw, and what stabilizes as samples grow is the solve probability, so each question's performance is estimated from 50 samples. Second the aggregation order: taking absolute values per question and then averaging gives A-PPG, which is zero exactly when every question is restored, whereas averaging first and differencing gives the old metric and equals the absolute difference of the two error components. Written out, A-PPG is the sum of under-suppression (residual contamination) and over-suppression (collateral damage) while the old metric is their difference -- so the old metric reaches zero whenever the two are equal, which cancellation alone achieves. Third, equal weighting: when the clean model is weak, most questions sit near zero solve probability, and a strategy that simply drives the contaminated model to fail everything scores a zero gap on that majority while large gaps on the capable minority are diluted. SA-PPG therefore bins questions by the clean model's own solve probability into 50 equal-width groups, averages within each group and then across groups, so a strategy must restore at every capability level. RailCap, the proposed mitigation, is built on two observations about the contaminated model's own generation: on leaked questions its sampled responses collapse onto its greedy trajectory while on unleaked ones they disperse, and at the decoding steps where clean and contaminated models diverge, the clean model's choice is the contaminated model's runner-up about half the time. So it greedy-decodes once per question, indexes every n-gram window of that trajectory to its successor token, and during sampling caps that successor's logit to the current second-largest whenever the last n tokens fall back onto the trajectory. Suppression accumulates step by step and how much any question receives is decided online rather than allocated in advance by a one-shot estimate. Contamination is simulated on Llama-2-7B, Gemma-4-E2B and Pythia-12B: fine-tune the base on training data to get the clean model, then continue from it with test-split questions mixed in to get the contaminated one, over GSM8K and a paraphrased version whose wording is rewritten but whose numbers and answers are unchanged.

## Results

The rank reversal is the headline and it is complete. On Llama-2 with GSM8K, LNE-blocking reads 0.0235 under the old metric against 0.3192 for no intervention at all, and is the best strategy in that column; under SA-PPG it reads 0.2932 against 0.3261 for no intervention, which is barely a difference, and it falls behind two other strategies. RailCap, which is not best under the old metric at 0.0728, is best under SA-PPG at 0.1914. Same responses, same models, same strategies -- only the metric changes, and the verdict inverts. The decomposition shows where the old metric hides the error: LNE-blocking's over-suppression component is 2.0 times RailCap's, yet its aggregate reading is 3.8 times better, because the extra collateral damage cancels against the residual contamination and pushes the number toward zero. The readout correction is worth separating from the aggregation correction, and the paper measures both. Drawing two independent sampling batches from the same clean model, the mean per-question gap between batches is 0.190 under the single-sample discrete readout and 0.041 under the 50-sample solve probability -- so a 0/1 readout does not even reproduce between two evaluations of one model. And a synthetic All-Zero strategy that makes the contaminated model fail every question scores 0.2190 under equal-weight A-PPG, better than no intervention (0.3793) and better than two published strategies, while stratification ranks it worst of all at 0.4903. RailCap attains the lowest SA-PPG in all six model-by-domain settings. The baselines are consistent and modest: TED is nearly indistinguishable from no intervention everywhere, and LNE-blocking is worse than no intervention on all three models in the paraphrase domain, which the paper reads as a one-shot pre-hoc estimate degrading when the questions seen at inference differ from the contaminated ones.

## Limitations

No limitations section. The load-bearing one a reader must supply: SA-PPG is defined relative to a clean model, and outside a simulation that reference does not exist -- the whole evaluation depends on having trained a matched uncontaminated twin, so this is a metric for comparing mitigation strategies in the lab and not for auditing a deployed model. Contamination is likewise simulated by deliberately mixing test items into a fine-tuning corpus, which produces verbatim-style exposure; the archive's companion entry on audit power measures that verbatim, paraphrase and surface-shuffle exposure produce sharply different behavioural signals, so results established on the strongest mechanism should not be read as covering the others -- the paraphrase domain here mitigates that but keeps numbers and answers identical, so it varies wording only. Everything is GSM8K or a rewrite of it, so the capability distribution that stratification is defined over is one benchmark's. RailCap needs a greedy decode per question and logit access at every step, ruling out closed models, and its n-gram threshold is a single setting whose sensitivity is unreported. Finally, the clean models are themselves LoRA fine-tunes at one hyperparameter setting, and the claim that base checkpoints are uncontaminated is verifiable only for Pythia.

## Why it matters here

- **reasoning-evaluation**: This archive already holds the result that a brief round of GRPO erases the signals contamination detectors rely on, and treats it as a reason to distrust benchmark numbers. This attacks the layer above: even where mitigation is attempted, the metric everyone used to judge it can be satisfied by damaging the model as much as the contamination inflated it. The All-Zero control is the cleanest statement of that -- a strategy that makes the model fail everything outscores two published methods. It also gives the archive a measurement it lacked, that a single-sample 0/1 readout does not reproduce between two evaluations of the same model (mean per-question gap 0.190 against 0.041 for a 50-sample probability), which bears on far more of this literature than contamination work.

## Entities

- **Concepts**: [benchmark contamination](../../../../wiki/concepts/benchmark-contamination.md), contamination mitigation, solve probability, aggregate metric, over-suppression, stratified aggregation, [memorization](../../../../wiki/concepts/memorization.md), greedy trajectory, [construct validity](../../../../wiki/concepts/construct-validity.md)
- **Methods**: SA-PPG, RailCap, LNE-blocking, shortcut neuron patching, TED, [greedy decoding](../../../../wiki/methods/greedy-decoding.md), [LoRA](../../../../wiki/methods/lora.md), n-gram matching
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), OpenOrca

Tags: `contamination`, `evaluation-metric`, `memorization`, `decoding`, `measurement-validity`

## Abstract

Test data from public benchmarks inevitably leaks into pretraining corpora, inflating evaluation scores once memorized. \textbf{Contamination mitigation evaluation} intervenes in the decoding process to suppress memorization and restore a contaminated model's genuine capability, but its prevailing metric, the \textbf{G-AP} (\textbf{G}ap of \textbf{A}ggregate \textbf{P}erformance), is flawed. Discrete correct/incorrect readouts cannot characterize per-question performance, averaging before differencing lets over- and under-suppression cancel out, and uniform per-question weighting invites strategies to push solve probabilities onto the clean model's high-frequency values. We propose \textbf{SA-PPG} (\textbf{S}tratified \textbf{A}ggregate of \textbf{P}er-question \textbf{P}robability \textbf{G}aps): estimate each question's solve probability by sampling, difference it against the clean model per question, and aggregate within groups defined by the clean model's solve probability. Existing mitigation strategies first estimate where contamination lies and then operate on the estimate, so they are only as correct as the estimate. \textbf{RailCap} instead judges contamination during generation: whenever a sample falls back onto the greedy trajectory, the next trajectory token is capped to the runner-up, accumulating suppression until the response distribution becomes sufficiently dispersed. Across multiple contaminated models and benchmarks, SA-PPG reveals that prior strategies' restoration is substantially overestimated, while RailCap attains the lowest SA-PPG.

---

Record id: `arxiv:2608.07341`
