<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Disagree to Explore, Agree to Commit: Routing-Guided Test-Time Scaling for Software Agents

- **Authors**: Kang Chen, Junjie Nian, Yixin Cao, Yugang Jiang
- **Venue**: cs.AI
- **Published**: 2026-08-23
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.22191>
- **PDF**: <https://arxiv.org/pdf/2608.22191v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

Risa reads the MoE router's expert-selection trace as a behavioral fingerprint of what a software agent is doing, using it to push sibling actions away from recently repeated computation during exploration and toward peer agreement once a patch is being written, then to arbitrate among completed attempts without an external judge or test execution.

## Problem

Test-time scaling for repository-level repair has two nested selection problems -- which of many sibling actions to execute at each tool step, and which of several completed patches to submit -- and neither has a canonical answer form to match against. Existing systems resolve them with execution feedback, trained verifiers, or judge models. Sibling actions from a shared prefix are also correlated, so a similarity signal means something different within an attempt than across independently sampled ones.

## Contributions

- Shows that MoE router traces encode an agent's behavioral role with high precision -- 0.940 three-way holdout accuracy over 78,535 actions, write-versus-rest precision 1.00 -- giving a runtime gate that needs no scaffold-specific command taxonomy.
- Establishes that routing similarity must be read relative to the comparison set: same-prefix siblings share evidence, while independently sampled attempts converging at the patch stage is a stronger signal.
- A steering rule that inverts sign by role -- maximize disagreement with the attempt's own recent computation while exploring, maximize peer agreement once several candidates propose a write.
- A terminal arbitration rule over decision tokens that matches text consensus on SWE-bench Verified without any answer-string matching or test execution.
- A stagnation measurement: mean routing similarity to recent history separates resolved rate 33.8% to 5.4% across quintiles.

## Method

Sparse-MoE routers already record, per token and layer, which experts were selected and with what weight. Risa aggregates this into a fingerprint over layer-expert cells for the action span only, located from the model's action-channel markers so the comparison describes the proposed tool call rather than the reasoning before it. Three role centroids (inspect/execute, run tests, write) are fit per model configuration from parsed tool-call labels on task-disjoint data and frozen; at runtime a candidate is assigned to its highest-cosine centroid, and the two non-write roles are collapsed into an exploratory class. The role gate then selects the comparison rule. Exploration (write rule inactive): score S_explore(c) = -(1/m_t) * sum over the m_t = min(3, |H_t|) most similar entries in a W = 64 window of executed history, of weighted-Jaccard similarity -- i.e. prefer the action least like what this attempt has already computed. Commitment (>= 2 write candidates): S_write(c) = z(H(c)) + 1.5 z(M(c)) + z(Sbar(c)) - z(P(c)), where M is the fraction of other write candidates within routing similarity tau = 0.65, Sbar is mean peer similarity, H is fingerprint entropy and P peak mass, the last two acting as dispersion guards against an uninformative routing concentration. After K = 4 complete attempts, accumulated diffs are re-encoded and decision-token agreement -- read off the least-probable tokens -- selects the submission. Weights are never updated; only the reference set changes per decision.

## Results

SWE-bench Verified, gpt-oss-20b and gpt-oss-120b at native low/medium/high reasoning effort, n = 16 siblings per step, K = 4 attempts, 496-498 tasks per condition. All selectors act on the same Risa-steered pools, so terminal arbitration is isolated from generation. Risa gains 2.3-5.7 points over Uniform across the six conditions, macro-average 44.9% -> 48.2%, with the largest gains at high reasoning effort; Risa-H (text-first, routing tie-break) reaches 48.3% and Text consensus 48.0%. Oracle over the four-attempt pool is 60.9%. Transfer to Qwen3.6-35B-A3B (498 tasks, role centroids refit only): Risa 45.2%, Risa-H 45.6%, Text 45.0%, Uniform 41.7%; Risa and Text both beat Uniform at p < 0.001, while Risa versus Text is 10 routing-only wins against 9 text-only wins, exact McNemar p = 1.000. Supporting measurements: the role classifier reaches 0.940 three-way holdout accuracy on 78,535 task-disjoint actions against a 0.746 majority baseline, with write-versus-rest recall 0.93 at precision 1.00, and agrees with the exact parsed role on 96.8% of actions. Routing repetition tracks stagnation: averaging each action's similarity to its three closest fingerprints in the previous 64, resolved rate falls from 33.8% in the most-different quintile to 5.4% in the most-similar (n = 1,021). Across 658 final-step generations the least-probable quarter of tokens carries 72% of total surprisal. On an empirically hard 80-instance set, steering raises submittable-patch yield from 79% to 94%; on a fixed 200-task 20b subset the full pipeline reaches 50.5% against 45.4% for unguided generation with uniform selection.

## Limitations

Stated: the method assumes accessible sparse-MoE routing and repeated trajectories, so it suits white-box MoE agents; dense or closed models would need a different internal readout, and other domains would need role definitions for their action spaces; combining routing with semantic or execution evidence is left to future work. Noticed by the reader: (a) the headline claim is parity, not superiority -- 48.2%/48.3% against Text's 48.0% on the gpt-oss macro-average, and on the full Qwen benchmark Risa versus Text is exact McNemar p = 1.000, so the defensible result is that routing matches answer-string consensus without needing answer strings; (b) Oracle is 60.9% against 48.3% best, so most of the complementary coverage in a four-attempt pool is still unselected; (c) the compute budget is large and unreported as a cost -- 16 sampled siblings at every tool step across 4 full attempts -- and no accuracy-per-token or wall-clock comparison against a cheaper baseline is given; (d) several constants carry the method (tau = 0.65, W = 64, m_t <= 3, the 3/2 weight on peer support) and are fixed on a separate pilot rather than swept; (e) role centroids are fit from parsed tool-call labels, so the 'no external judge' claim holds at runtime but not at setup; (f) the largest gains occur at high reasoning effort, which the paper reports but does not explain.

## Why it matters here

- **overthinking**: Scales test-time compute by sampling siblings and repeating attempts rather than by lengthening one trajectory, so like other parallel-scaling work it sits beside the archive's subject rather than inside it. Two results do bear on it directly. First, an internal-state stagnation measure with a real effect size: averaging an action's routing similarity to its three closest entries in the previous 64 executed actions splits resolved rate from 33.8% in the most-different quintile to 5.4% in the most-similar (n = 1,021). This is the wasted-loop case measured from activations rather than from text, and unlike lexical repetition counts it is invariant to surface rewording -- relevant to the archive's internal-state proxies, and cheaper than them since the router trace is already produced during inference. Second, the steering rule is an explicit operationalisation of when to stop exploring: maximize novelty against one's own history until several candidates propose the same commitment, then switch sign and maximize agreement. That is a stopping criterion defined on internal computation rather than on answer invariance, which is the family the archive's open synthesis question is about. The paper also reports that arbitration gains are largest at high reasoning effort without explaining why -- consistent with, but not evidence for, more effort producing more redundant computation to arbitrate over.

## Entities

- **Concepts**: [Test-Time Scaling](../../../../wiki/concepts/test-time-scaling.md), MoE Routing Traces, Behavioral Role Fingerprinting, Stagnation Detection, Repetition Score, Decision Tokens, Token Surprisal, Best-of-N Selection, Self-Consistency, Exploration-Commitment Tradeoff
- **Methods**: Risa (Routing-Informed Steering and Arbitration), Weighted Jaccard routing similarity, Role centroid classification, Decision-token agreement arbitration, Text consensus (Jaccard over diff line pairs), [Uniform sampling baseline](../../../../wiki/methods/uniform-sampling-baseline.md)
- **Datasets**: SWE-bench Verified (496-498 eligible tasks per condition; 500-task full benchmark for Qwen)

Tags: `test-time scaling`, `moe routing`, `software agents`, `swe-bench`, `stagnation`, `best-of-n`, `internal states`, `agent steering`

## Abstract

Software-engineering agents solve repository-level tasks through long, stochastic tool-use trajectories, and repeated attempts often find fixes missed by one run. Test-time scaling is difficult because patches lack canonical answer forms, while sibling actions from a shared prefix are correlated. We study whether native MoE router traces can guide steering and selection without an external judge or selection-time test execution. Our analysis shows that routing provides a robust behavioral role signal; token-granular readouts and decision-matched comparison sets turn it into effective control. We therefore introduce Risa (Routing-Informed Steering and Arbitration): within trajectories, routing encourages diverse exploration and controlled convergence during patch commitment; across separately sampled trajectories, agreement at informative patch positions selects a final candidate. We evaluate on SWE-bench Verified using open-weight sparse MoE agents across scales and reasoning-effort settings. Risa's routing arbitration raises the macro-average resolved rate from 44.9% under uniform sampling to 48.2% on the gpt-oss family, matching text consensus without answer-string matching, and it transfers to Qwen3.6, where it improves on uniform choice and matches text consensus on the full 500-task benchmark.

---

Record id: `arxiv:2608.22191`
