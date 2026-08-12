<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Unveiling the Entropy Dynamics of Chain-of-Thought Reasoning

- **Authors**: Ting Xu, Xu He, Yupu Lu, Jiankai Sun, Dong Li, Wai Lam, Jianye Hao
- **Venue**: ICML 2026 (Proceedings of the 43rd International Conference on Machine Learning, PMLR 306)
- **Published**: 2026-01-01
- **Source**: local
- **Topics**: reasoning-training, test-time-scaling
- **Relevance score**: reasoning-training 0.50, test-time-scaling 0.50

## In one line

Shows that CoT entropy follows a two-phase structure — a high-entropy exploration region that shifts abruptly into a low-entropy convergence region — and detects that shift online with the CUSUM change-point algorithm to drive early exit and trajectory-weighted voting.

## Problem

Existing work on CoT treats reasoning as discrete segments and studies local properties — individual steps, layers, state transitions — leaving the global temporal question open: how does reasoning progress from exploration to convergence, and does a solution emerge gradually or at a sudden transition? Practically, training-free early-exit methods rely on heuristic triggers (answer confidence above a threshold, two consecutive stable answers, EMA-variance of next-token entropy) that have no formal guarantees and are vulnerable to transient low-entropy fluctuations during exploration. Detecting when a trajectory has actually converged, in real time and with controllable error, was unaddressed.

## Contributions

- A systematic empirical analysis of predictive-entropy dynamics across a full CoT trajectory, identifying a consistent two-phase regime shift from an Uncertainty Region to a Confidence Region across three models and difficulty levels.
- Two properties of the Confidence Region that make it exploitable: High Reliability (accuracy jumps from under 20% to a plateau above 60% on entry) and High Redundancy (models keep generating, often over 30% of total trajectory length, after the answer is settled).
- The first formulation of CoT monitoring as a sequential change-point detection problem, adopting CUSUM with its classical minimax-optimality and false-alarm guarantees, and an identifiability condition (strictly positive KL divergence between the two regimes' entropy distributions) validated empirically.
- Two training-free inference algorithms built on the detector: CUSUM early exit, and CUSUM-weighted test-time voting that scores each trajectory by its final CUSUM statistic instead of giving every trajectory an equal vote.

## Method

At each reasoning step i the model is interrupted with an answer-inducing prompt ('</think> The answer is \boxed') to extract an intermediate answer A_i, and the predictive entropy H_i of that answer is computed by averaging token entropies over A_i. The sequence of H_i is modelled as switching between two stochastic regimes at an unknown change-point nu: H_i ~ f0 before it (Uncertainty Region) and f1 after (Confidence Region). Detection is posed as minimizing worst-case average detection delay subject to a lower bound gamma on the expected time to false alarm. CUSUM solves this: the per-step log-likelihood ratio Z_i = log(f1(H_i)/f0(H_i)) measures instantaneous evidence for convergence, and the statistic S_i = max(0, S_{i-1} + Z_i) accumulates it, with the stopping rule tau_h = inf{i : S_i >= h}. A drift-separation lemma shows E_0[Z_i] < 0 and E_1[Z_i] > 0 under the identifiability assumption, so S_i drifts down during exploration and up after convergence. Setting h = log(gamma) gives the false-alarm bound e^h <= E_inf[tau_h] <= C·e^h, leaving one interpretable hyperparameter for the reliability-efficiency trade-off. The distributions f0 and f1 are fitted once per model by histogram density estimation on entropies from 100 randomly selected trajectories of Bespoke-Stratos-17k, so no fine-tuning is involved. Early exit runs the detector online and stops generation the first time S_i >= h. Test-time scaling instead runs N trajectories to completion and weights each one's answer by its final CUSUM score S_final = max_k sum_{i=k}^{L} Z_i, which measures how decisively the trajectory committed, then returns the highest-weighted answer.

## Results

Change-point location: the normalized change-point falls at 30-34% of the trajectory on easy problems and 52-56% on hard ones; stronger models converge earlier (Qwen3-14B 30%/52% vs DeepSeek-R1-Distill-Qwen-7B 33.9%/56.4%); earlier convergence correlates with correctness, most strongly for the distilled model (Pearson r = -0.45) and weakest for the natively trained 14B (r = -0.26). Early exit, averaged across three models and AIME24/AIME25/GPQA-Diamond, reaches 63.06% accuracy with an 11.1% token reduction, against DEER at 59.78% and Dynasor at 58.70% (+3.28 and +4.36 points). Per model the averages are: DeepSeek-R1-Distill-Qwen-7B 44.44% at 10281 tokens (-15.5%) vs DEER 39.97% and Dynasor 36.37%; Qwen3-4B-Thinking-2507 73.3% at 16119 tokens (-5.6%) vs 72.28% and 70.9%; Qwen3-14B 71.45% at 10838 tokens (-11.1%) vs 67.1% and 68.83%. The gap is largest on GPQA with DeepSeek-7B: 40.40% vs 35.73% (DEER) and 19.32% (Dynasor). CUSUM also dominates on the Pareto frontier of AIME25 as each method's hyperparameter is swept. End-to-end latency on AIME25 with Qwen3-4B-Thinking-2507 is 419s versus 504s vanilla, 460s DEER and 492s Dynasor, so probing overhead does not eat the token savings. For test-time scaling on AIME25, CUSUM-weighted voting beats self-consistency at every N from 2 to 64 across all three models, and the gap widens with N — reaching a 3.33% lead at N = 64 for Qwen3-4B-Thinking-2507. The distribution of S_final separates correct from incorrect trajectories, though both show a mode near S_final = 0.

## Limitations

The paper has no limitations section; what follows is drawn from its own tables and setup. Most importantly, early exit does not beat unrestricted generation on accuracy — vanilla scores 45.02%, 74.32% and 73.69% on the three models against CUSUM's 44.44%, 73.3% and 71.45%. The claim is a better efficiency-accuracy Pareto frontier against other early-exit methods, not a free improvement, and the abstract's framing of 'without compromising accuracy' is a small-loss-for-tokens trade rather than a null one. The detector needs per-model calibration data: f0 and f1 are estimated from 100 Bespoke-Stratos-17k trajectories, so a new model requires that step. CUSUM's classical guarantees assume i.i.d. observations within each regime, which entropy sequences violate; the paper argues consistency still holds by citing a sub-quadratic partial-sum variance condition and asserting it is satisfied, but does not test the dependence directly. Evaluation rests on AIME24 and AIME25, which are 30 problems each — mitigated by 16 random runs per dataset, but still a narrow base — plus GPQA-Diamond, and all models are 4B-14B, so behaviour at frontier scale is untested. Finally, extracting an intermediate answer at every step requires interrupting generation, which is feasible for open-weight models only.

## Why it matters here

- **test-time-scaling**: Both halves of this topic in one paper, driven by one signal. On the spending-less side it gives early exit a statistical footing that heuristic stopping rules lack: a single threshold h with an explicit false-alarm bound and asymptotically minimax detection delay, replacing hand-tuned confidence triggers. On the spending-more side it answers what to do with N sampled trajectories — weight by how decisively each converged rather than counting votes equally — and shows the advantage over self-consistency growing with N, which is exactly the shape of the compute-versus-accuracy curve this topic tracks. The High Redundancy finding quantifies the waste the topic exists to measure: over 30% of a trajectory is generated after the answer is settled. The honest reading of Table 2 is also useful here, since it shows the frontier is a trade, not a dominance.

## Entities

- **Concepts**: predictive entropy, [entropy trajectory](../../../../wiki/concepts/entropy-trajectory.md), uncertainty region, confidence region, two-phase reasoning structure, sequential change-point detection, worst-case average detection delay, false alarm control, [reasoning redundancy](../../../../wiki/concepts/reasoning-redundancy.md), [overthinking](../../../../wiki/concepts/overthinking.md), [answer stabilization](../../../../wiki/concepts/answer-stabilization.md)
- **Methods**: CUSUM, CUSUM-weighted voting, [early exit](../../../../wiki/methods/early-exit.md), [self-consistency](../../../../wiki/methods/self-consistency.md), [DEER](../../../../wiki/methods/deer.md), [Dynasor](../../../../wiki/methods/dynasor.md), histogram density estimation
- **Datasets**: [AIME24](../../../../wiki/datasets/aime24.md), [AIME25](../../../../wiki/datasets/aime25.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), Bespoke-Stratos-17k

Tags: `entropy`, `change-point detection`, `cusum`, `early exit`, `test-time scaling`, `self-consistency`, `chain of thought`, `inference efficiency`

## Abstract

This paper investigates the entropy dynamics of Chain-of-Thought (CoT) and uncovers a consistent two-phase structure: an Uncertainty Region of exploration transitioning sharply to a Confidence Region of convergence. We demonstrate that the Confidence Region possesses two critical properties: 1) High Reliability—answers in the confidence region become highly accurate and stable, and 2) High Redundancy—models generate unnecessary tokens long after reaching the correct answer. These properties unlock more efficient and reliable inference strategies: 1) Early Exit leverages reliability and redundancy to terminate computation safely when returns diminish, and 2) Test-Time Scaling uses the Confidence Region signal to prioritize converged trajectories. To operationalize these strategies, we formulate Confidence Region detection as a sequential change-point detection problem, being the first to apply classical change-point methods to CoT reasoning. Using the Cumulative Sum (CUSUM) algorithm, a statistically optimal change-point detector, we develop a training-free framework for real-time inference control. Experiments show our approach establishes a superior Pareto-frontier for early exit. CUSUM achieves 63.06% accuracy with 11.1% token reduction, outperforming DEER and Dynasor by 3.28% and 4.36% in accuracy respectively. For test-time scaling, CUSUM-weighted voting consistently outperforms self-consistency.

---

Record id: `local:379c0b6966148b4a`
