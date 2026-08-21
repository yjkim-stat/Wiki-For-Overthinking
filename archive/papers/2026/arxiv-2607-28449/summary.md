<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Lightning OPD 2.0: Mitigating Style Bias in Cross-Teacher On-Policy Distillation for Large Reasoning Models

- **Authors**: Yecheng Wu, Song Han, Han Cai
- **Venue**: cs.CL
- **Published**: 2026-07-30
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2607.28449>
- **PDF**: <https://arxiv.org/pdf/2607.28449v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Lightning OPD 2.0 subtracts a cross-fitted estimate of recurring teacher-reference log-probability disagreement from the token-level on-policy-distillation signal, so an OPD teacher can differ from the model that generated the SFT demonstrations.

## Problem

On-policy distillation converts teacher-student disagreement into dense token-level supervision, but prior work found it needs teacher consistency: the OPD teacher must be the same model that generated the SFT demonstrations. That condition often fails — SFT data may have mixed or undocumented provenance, regenerating demonstrations per candidate teacher is expensive, and the best demonstration generator need not be the best distillation teacher. In the resulting cross-teacher setting, a stronger OPD teacher can give little or no improvement over the SFT reference, because low teacher probability on a token may reflect a preference for different wording, formatting, derivation length or reasoning cadence rather than a wrong reasoning step, and the objective cannot tell the two apart.

## Contributions

- Formulates cross-teacher OPD, where the SFT data generator and the OPD teacher are chosen independently, and shows distillation gains largely vanish there (Qwen3-4B-SFT math: 48.3 SFT vs 48.6 Lightning OPD).
- Identifies a component of teacher-reference disagreement that is predictable across unrelated rollouts from token identity and coarse position/surprisal coordinates, and proposes it as an operational proxy for style-token bias.
- Lightning OPD 2.0: cross-fitted, response-balanced, smoothed lookup tables estimate that component and subtract it from the teacher score before the token-level update, with no live teacher and no change to the policy surrogate.
- A post-hoc diagnostic comparing the corrected cross-teacher signal to a teacher-consistent one, showing >1-nat deviations drop from 8.14% to 3.85% and 7.19% to 2.02% of scored tokens.
- Component ablations separating the token lookup, the context lookup and prompt-level cross-fitting.

## Method

Built on Lightning OPD's frozen offline replay: one response per prompt is sampled from the SFT reference pi_R and frozen, then both pi_R and the chosen OPD teacher pi_T score the realized tokens once before training. Define the teacher-reference disagreement d_it = log pi_T(y_it|h_it) - log pi_R(y_it|h_it), and posit d_it = b(z_it) + v_it where b is whatever recurs at coarse coordinates across unrelated rollouts. Two coordinate families are used: token identity, and a context coordinate built from binned normalized response position (B_pos bins) crossed with binned reference-policy surprisal xi_it = -log pi_R(y_it|h_it) (B_ref bins up to xi_max); the two tables are kept separate rather than crossed, to avoid sparse groups. Estimation is by cross-fitting: cached rollouts are split into K=5 deterministic folds with all rollouts from a prompt kept in one fold, and for a token in fold k the lookup tables are fitted only on the other K-1 folds. Each response gets unit total weight spread over its active tokens so long responses do not dominate; rare groups are smoothed toward the non-held-out global mean and unseen groups take that mean. The style estimate is the equal-weight average b_hat_it = 0.5*m_tok(y_it) + 0.5*m_ctx(p_it, r_it). The residualized advantage is A_res = (log pi_T(y_it|h_it) - b_hat_it) - log pi_theta(y_it|h_it), i.e. only the disagreement term is corrected and the reference-anchoring term is left alone; equivalently a fixed effective teacher score l_tilde = l_T - b_hat is computed once before training. Optimization otherwise reuses the Lightning OPD policy surrogate (PPO clipping 0.2). The paper is explicit that the split is operational, not a semantic labeling of which tokens are style.

## Results

Two cross-teacher settings, both with Qwen3-30B-A3B-Thinking-2507 as the OPD teacher; training on DAPO-Math-17k (math) and KlearReasoner-CodeSub-15K (code), 150 steps each, temperature 0.6, top-p 0.95, max generation 40,960 tokens, avg Pass@1 over 64 samples for math and 8 for code. Qwen3-4B-SFT (demonstrations from Qwen3-8B): math average 48.3 (SFT) -> 48.6 (Lightning OPD) -> 51.7 (2.0); code average 32.6 -> 34.3 -> 35.7. Klear-Reasoner-8B-SFT (long-CoT SFT data from DeepSeek-R1-0528): math 73.6 -> 73.6 -> 74.6; code 54.9 -> 57.1 -> 58.5. Best individual numbers: AIME 2024 82.4% and LiveCodeBench v5 63.0% from the Klear-Reasoner-8B start. The two adapted baselines are close on the stronger reference: IW-OPD 73.9 math / 57.4 code and TA-OPD 73.9 / 57.6 vs 74.6 / 58.5, so the margin there is 0.7-0.9 points; on Qwen3-4B the math margin is larger (51.7 vs 48.2 IW-OPD, 45.6 TA-OPD). Mechanism check: against a diagnostic teacher-consistent signal (Qwen3-8B, the actual demonstration generator, for Qwen3-4B-SFT; Klear-Reasoner-8B as a proxy for the other), the fraction of tokens whose signal deviates by more than 1 nat falls from 8.14% to 3.85% and from 7.19% to 2.02% respectively, with larger relative reductions at higher thresholds. Ablation on AIME24/HMMT25: removing cross-fitting (in-sample) gives 62.7/36.7 and 81.8/63.1 vs the full 63.5/36.7 and 82.4/63.8; token-only and context-only variants are each weaker in some setting. All results are single training runs; no variance or seed spread is reported.

## Limitations

Stated: evaluation is confined to mathematical reasoning and code generation and to Qwen-family models with compatible tokenization, which the method needs so teacher and reference scores align to the same tokens. Beyond that: the decomposition into 'style' and 'reasoning evidence' is admitted to be operational, and the mechanism analysis only shows the corrected signal moves closer to a teacher-consistent reference, not that what was removed is style. On the Klear-Reasoner-8B-SFT setting the math gain over the SFT reference is 1.0 point and the gain over IW-OPD/TA-OPD is 0.7 points, on single runs of 64-sample Pass@1 with no confidence intervals, so the ordering among the three corrected methods is weakly supported; the clear separation is against unmodified Lightning OPD on Qwen3-4B. Only one response is sampled per prompt, and the ablation shows in-sample estimation is nearly as good as cross-fitting (one column ties, one is 0.1 higher), so the cross-fitting machinery earns less than the framing suggests. Bin counts B_pos, B_ref, xi_max and the smoothing strength are not given in the text read. IW-OPD and TA-OPD were reimplemented onto the frozen replay rather than run as published. No cost, latency or generation-length measurements are reported.

## Why it matters here

- **overthinking**: Tangential. This is a post-training/distillation paper: it matched the topic only through the phrase 'large reasoning model' in the title, and the tracked question — how long a model should think — is never studied. Nothing in the experiments measures reasoning length, token budget or test-time compute; all five reported metrics are Pass@1 accuracy, and the only budget mentioned is a fixed 40,960-token generation cap applied uniformly. The single thread of contact is incidental: the paper lists 'derivation length' and 'reasoning cadence' among the stylistic differences between a teacher and an SFT reference, and treats the resulting per-token disagreement as bias to be removed. If one wanted to use it, the transferable observation is that a distillation teacher penalizes a student for verbosity habits in a way that is predictable across unrelated rollouts and separable from problem-specific signal — which is a mechanism by which a teacher's preferred reasoning length could be transferred, or blocked from transferring, during post-training. The paper neither makes nor tests that claim, and it should not be counted as evidence about the accuracy/efficiency tradeoff.

## Entities

- **Concepts**: On-Policy Distillation, Teacher Consistency, Style-Token Bias, Cross-Fitting, Token-Level Credit Assignment, Reference-Policy Surprisal, Offline Frozen Replay, Residualization
- **Methods**: Lightning OPD 2.0, cross-fitted style residualization, Lightning OPD, [on-policy distillation (OPD)](../../../../wiki/methods/on-policy-distillation-opd.md), IW-OPD, TA-OPD, PPO-style clipped policy surrogate, Qwen3-30B-A3B-Thinking-2507 (teacher), Qwen3-4B-SFT, Klear-Reasoner-8B-SFT (students), slime training framework
- **Datasets**: [DAPO-Math-17k](../../../../wiki/datasets/dapo-math-17k.md), KlearReasoner-CodeSub-15K, [AIME 2024](../../../../wiki/datasets/aime-2024.md), [AIME 2025](../../../../wiki/datasets/aime-2025.md), HMMT February 2025, LiveCodeBench v5, [LiveCodeBench v6](../../../../wiki/datasets/livecodebench-v6.md)

Tags: `on-policy-distillation`, `post-training`, `style-bias`, `cross-fitting`, `math-reasoning`, `code-generation`, `qwen3`

## Abstract

On-policy distillation (OPD) provides dense token-level supervision from a teacher, but its effectiveness can depend on teacher consistency, meaning that the model providing OPD supervision should also have generated the demonstrations used to train the supervised fine-tuning (SFT) reference. However, this condition is frequently violated in practice when SFT data have mixed or unknown provenance or when different models are preferred for SFT data generation and subsequent distillation. In such cross-teacher settings, even a stronger OPD teacher can yield little improvement over the SFT reference. We find that raw teacher--reference disagreement contains potentially useful context-specific teacher evidence as well as a recurring component associated with differences in wording, formatting, and reasoning cadence. We introduce Lightning OPD 2.0 with cross-fitted style residualization, which uses rollout-level cross-fitting to estimate this recurring component as an operational proxy for style-token bias and subtracts it before constructing the token-level OPD update. Across mathematical reasoning and code generation benchmarks, Lightning OPD 2.0 consistently outperforms Lightning OPD in cross-teacher settings. Starting from Klear-Reasoner-8B-SFT, Lightning OPD 2.0 reaches 82.4% on AIME 2024 and 63.0% on LiveCodeBench v5. Together, these results establish Lightning OPD 2.0 as a practical approach to cross-teacher OPD, relaxing teacher consistency as a prerequisite and allowing the SFT data generator and distillation teacher to be selected independently. Code will be released soon.

---

Record id: `arxiv:2607.28449`
