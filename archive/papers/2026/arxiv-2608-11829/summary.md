<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling

- **Authors**: Xinmu Ge, Zizhuo Zhang, Yu Huang, Jianing Zhu, Lin Yuan, Wanli Gu, Weichang Wu, Weiran Huang, Xiaolu Zhang, Bo Han, Jun Zhou, Jiangchao Yao
- **Venue**: cs.LG
- **Published**: 2026-08-12
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.11829>
- **PDF**: <https://arxiv.org/pdf/2608.11829v1>
- **Topics**: test-time-scaling
- **Relevance score**: reasoning-training 0.25, test-time-scaling 0.50

## In one line

Evaluates on-policy distillation across sampling budgets from 1 to 1024 and finds it consistently improves accuracy at small budgets while losing to the untrained base model at large ones, so what it transfers is sampling efficiency rather than capability -- and off-policy distillation, tested the same way, does expand the boundary.

## Problem

On-policy distillation is understood as letting a student acquire knowledge from a stronger teacher and thereby exceed what it could do before. That claim is normally supported at a single sampling budget, where a gain is consistent with either of two very different things: the student learned to solve problems it could not solve, or the student learned to reach solutions it could already reach more often. Nothing in a pass@1 number distinguishes them.

## Contributions

- A pass@K and avg@K analysis from K=1 to 1024 across three student-teacher pairs and four benchmarks, showing on-policy distillation's advantage at small budgets reverses at large ones while avg@K stays higher everywhere.
- A problem-level retained/learned/forgotten accounting showing the forgotten set exceeds the learned set at large K in every setting, with the retained set carrying the gain.
- Training-step tracking showing capability-boundary degradation emerges by around 80 steps, before convergence, and is unstable while small-K improvement is stable.
- Replication of the pattern across four published on-policy variants, with off-policy distillation evaluated identically as a contrast that does raise both metrics at every budget.
- A perplexity analysis showing the distilled model's trajectories move toward the teacher's preference while remaining more likely under the base distribution than either the base's own or the teacher's trajectories.

## Method

Two metrics read together across budgets K from 1 to 1024. Pass@K at small K measures how reliably a correct path is found under limited sampling; at large K it probes what the model can reach at all, and is the usual proxy for a capability boundary. Avg@K measures the average correctness of the sampled distribution, that is sampling efficiency. Three student-teacher pairs are trained on the same mathematics corpus and each compared against its own pre-distillation base and its teacher on four competition benchmarks, at fixed temperature, top-p and seed with a 32k context. Three further analyses. A problem-level solvability accounting classifies each problem at each K as retained (solvable before and after), learned (solvable only after) or forgotten (solvable before, not after), and reports the net change. Pass@K is tracked over training steps to see when any degradation appears. And four published variants of the objective -- reward-extrapolated, implicit-reward-from-RL-shift, entropy-routed forward KL, and pure forward KL -- are put through the same test, alongside off-policy distillation as a contrast. Perplexity of trajectories from the base, distilled and teacher models is computed under both the base and teacher distributions.

## Results

The crossing is consistent and large. In one setting on one benchmark, pass@K runs 32.3 base / 45.4 distilled at K=1 and reverses to 100.0 / 95.0 at K=1024; on another benchmark of that setting, 4.2 / 12.0 at K=1 becomes 70.0 / 53.3 at K=1024. The same shape appears in all three settings: the largest gain is at K=1, it shrinks monotonically, and it reverses somewhere between 16 and 128 depending on the pair. Avg@K, by contrast, is higher for the distilled model at every budget in every setting, which is what identifies the gain as sampling efficiency. The solvability accounting gives the mechanism directly: under large-K criteria the forgotten set is larger than the learned set in all three settings, so more previously solvable problems become unsolvable than the reverse -- while the retained set grows with K and dominates both, meaning the improvement is concentrated on problems the student could already solve. The training-dynamics view shows the two effects are not simultaneous in character: small-K pass@K improves stably, while large-K pass@K fluctuates and has already clearly declined by around 80 steps, before convergence. The checkpoint table makes this concrete on one setting, where pass@1 rises 72.2 to 76.0 across 260 steps while pass@1024 falls 100.0 to 97.5, and on another benchmark 76.7 to 70.0 at pass@1024 with pass@1 rising 23.4 to 28.5. All four published variants reproduce the pattern -- higher avg@K everywhere and higher small-K pass@K, with large-K pass@K at or below the base model -- with one exception, a pure forward-KL variant on one benchmark. Off-policy distillation, evaluated identically, is higher on both pass@K and avg@K at every budget, so the difference is not an artefact of the measurement. Perplexity supports the reading: the distilled model's trajectories are more likely under the teacher than the base model's are, but they are also more likely under the base distribution than either the base model's own or the teacher's trajectories -- so probability mass moved toward paths the base already supported rather than toward the teacher's unfamiliar ones. A case study shows the base and distilled models following the identical factorisation route on a retained problem, at 221 against 893 correct out of 1024.

## Limitations

The paper has no limitations section. Reader-visible limits: three student-teacher pairs, all in mathematics, all with 1.5B-to-1.7B students, so nothing establishes whether the trade-off holds at larger scale or outside verifiable mathematics -- and the archive should note the students are small enough that a capability boundary at K=1024 may be dominated by base coverage. Evaluation uses a single seed at fixed decoding parameters, and the benchmarks are 30 to 40 problems each at the AIME sizes, so a pass@1024 difference of 2.5 points is one problem; several of the reported reversals are of that magnitude, though the direction is consistent across twelve setting-benchmark pairs. The forgotten-versus-learned accounting inherits that granularity. The off-policy contrast uses different checkpoints trained on different data by other parties rather than a matched off-policy run against the same teacher and corpus, so the paradigm comparison is suggestive rather than controlled. And the framing as illusory distillation is a claim about consistency: the paper shows the boundary is not consistently expanded, not that it is never expanded, and its own forward-KL exception is an instance.

## Why it matters here

- **test-time-scaling**: This is the archive's cleanest use of the sampling budget as a diagnostic instrument rather than as a method. Reading pass@K and avg@K together across three orders of magnitude in K separates two things a single-budget number cannot: avg@K rises everywhere while pass@K crosses, which pins the gain to how often correct paths are sampled rather than to which paths exist. The solvability accounting turns that into a per-problem statement -- more problems are forgotten than learned at large K, and the retained set carries the improvement -- and the training curves show the two effects are separable in time, with boundary degradation appearing by step 80 while small-K gains keep accruing. Two consequences for how the archive reads other work. First, any post-training result reported at pass@1 is compatible with a narrowed reachable set, and the check costs only a larger K; four published improvements to this objective all reproduce the pattern, so it is a property of the paradigm rather than of one implementation. Second, the off-policy contrast is the control that stops this from being a measurement artefact -- evaluated identically, off-policy distillation is above the base at every budget on both metrics. This directly extends the archive's existing finding that verifiable-reward training narrows the set of distinct solution paths while improving reliability: the same trade appears here under a completely different objective, which suggests it belongs to on-policy training on self-generated trajectories rather than to reward-based learning specifically.

## Entities

- **Concepts**: on-policy distillation, off-policy distillation, [pass@k](../../../../wiki/concepts/pass-k.md), capability boundary, [sampling efficiency](../../../../wiki/concepts/sampling-efficiency.md), [test-time scaling](../../../../wiki/concepts/test-time-scaling.md), [catastrophic forgetting](../../../../wiki/concepts/catastrophic-forgetting.md), forward KL divergence, reverse KL divergence, [perplexity](../../../../wiki/concepts/perplexity.md)
- **Methods**: [on-policy distillation](../../../../wiki/methods/on-policy-distillation.md), off-policy distillation, [GKD](../../../../wiki/methods/gkd.md), MiniLLM, ExOPD, Direct-OPD, [EOPD](../../../../wiki/methods/eopd.md), [GRPO](../../../../wiki/methods/grpo.md), [knowledge distillation](../../../../wiki/methods/knowledge-distillation.md)
- **Datasets**: [DAPO-Math-17k](../../../../wiki/datasets/dapo-math-17k.md), [AMC23](../../../../wiki/datasets/amc23.md), [AIME 2024](../../../../wiki/datasets/aime-2024.md), [AIME 2025](../../../../wiki/datasets/aime-2025.md), [AIME 2026](../../../../wiki/datasets/aime-2026.md)

Tags: `on-policy-distillation`, `pass-at-k`, `capability-boundary`, `sampling-efficiency`, `negative-result`

## Abstract

On-policy distillation (OPD) has emerged as a promising post-training technique for enhancing LLM reasoning. It is commonly believed to enable the student model to distill knowledge from a stronger teacher model, thereby expanding capabilities beyond the pre-OPD base model. In this study, we examine this view through the lens of test-time scaling by varying the sampling budget K and evaluating performance with pass@K and avg@K. Specifically, across several OPD variants, we observe that OPD-trained models maintain superior avg@K performance across sampling budgets, while the advantage in pass@K gradually shifts to the pre-OPD base models as K increases. These results suggest that OPD primarily improves sampling efficiency rather than consistently expanding the student's reasoning capability boundary. The pass@K dynamics throughout OPD training further reveal a progressive shift toward stronger small-K performance at the expense of the large-K capability boundary. Furthermore, a problem-level solvability analysis using pass@1024 as the criterion reveals an asymmetry: OPD causes more previously solvable problems to become unsolvable than previously unsolvable problems to become solvable. Together, these findings suggest that, from the perspective of capability expansion, OPD behaves more like an "illusory distillation": its apparent gains arise primarily from improved sampling efficiency rather than from acquiring genuinely new reasoning capabilities from the teacher.

---

Record id: `arxiv:2608.11829`
