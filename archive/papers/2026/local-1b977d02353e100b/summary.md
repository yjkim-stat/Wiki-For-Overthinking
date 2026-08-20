<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Landscape of Thoughts: Visualizing the Reasoning Process of Large Language Models

- **Authors**: Zhanke Zhou, Zhaocheng Zhu, Xuan Li, Mikhail Galkin, Xiao Feng, Sanmi Koyejo, Jian Tang, Bo Han
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: local
- **Topics**: test-time-scaling

## In one line

Turns each intermediate step of a reasoning trajectory into a numerical feature vector of distances to the answer choices, projects those into 2D to visualize how trajectories move through answer space, and reuses the same features to build a lightweight verifier for weighted voting.

## Problem

Reasoning behaviour of LLMs is inspected in practice by reading trajectories by hand, which does not scale — roughly 30 seconds per trajectory means 50 minutes for 100 — and does not aggregate, so dataset-level conclusions drawn from 10,000 trajectories end up subjective. Earlier probing work is tied to particular decoders and tasks. What was missing is a general, reusable way to look at reasoning trajectories in a user's own setting, from a single example up to a whole dataset.

## Contributions

- A representation that makes textual reasoning states numerical without training anything: each state is characterized by its perplexity-based distance to every answer choice, computed by the same LLM that produced the thoughts.
- A visualization built by t-SNE projection of those features, in which answer choices appear as landmarks and the density of states shows how a trajectory converges, applicable to any open-weight model and any multiple-choice reasoning dataset.
- Three trajectory-level metrics defined on the same features — consistency (does an intermediate state already point at the final answer), uncertainty (entropy of the distance vector) and perplexity at the level of a thought rather than a token.
- A set of empirical observations relating convergence behaviour to accuracy across model scales, tasks and decoding methods.
- A demonstration that the features support prediction as well as inspection: a random-forest verifier trained on state features and consistency, with no language model of its own, used to weight votes across sampled trajectories.

## Method

For a multiple-choice question with choices c_1..c_k, a trajectory of thoughts t_1..t_n induces states s_i = [x, t_1, ..., t_i]. Each state is represented by a k-dimensional feature f_i whose j-th entry is the length-normalized distance from the state to choice c_j, computed as a perplexity: the accumulated autoregressive probability of the choice tokens given the state, raised to the power of minus one over the choice's token length, so choices of different lengths are comparable. The feature vector is normalized to unit L1 norm, and each choice also gets a landmark feature vector that encodes zero distance to itself and equal distances to the others. Stacking the state features for many trajectories together with the k landmark vectors gives a feature matrix, which t-SNE projects to 2D; because the two projected dimensions correspond to directions in answer space, a state's position reflects its relative distance to each candidate answer. Choices are reordered so the correct answer occupies the same dimension across questions, which lets many questions share one landscape instead of requiring many trajectories per question. Consistency of a state is an indicator that the closest choice at that state equals the closest choice at the final state; uncertainty is the entropy of the normalized distance vector. The verifier is a random forest mapping the sequence of state features and consistency values to a correctness prediction — deliberately low-capacity given the small feature dimension — trained on thoughts sampled from the training split of each dataset and applied at test time to weight each trajectory's vote in a majority vote. The method is post-hoc throughout: it never intervenes in or alters the trajectory. It requires a model that both generates thoughts and exposes likelihoods, which excludes closed models such as GPT-4 and Gemini.

## Results

Across Llama-3.2-1B, 3B and Llama-3.1-8B, 70B with CoT on 50 AQuA problems (accuracies 15.8%, 42.0%, 53.2%, 84.4%), larger models converge to the correct answer faster, with higher consistency and lower uncertainty and perplexity. Within any single method, incorrect trajectories converge to a wrong answer earlier — often by 20-40% of states — while correct trajectories settle only in the final 80-100%, implying early states can lead anywhere and the correct answer is typically determined late. Intermediate states in correct trajectories are markedly more consistent with the final answer than in incorrect ones, and consistency is generally low overall, which the paper reads as evidence that the reasoning process is unstable even under decoding methods designed to proceed directly. Across tasks (AQuA, MMLU, StrategyQA, CommonsenseQA with Llama-3.1-70B, accuracies 84.4%, 80.2%, 75.8%, 64.8%), structurally similar tasks give similar landscapes, while CommonsenseQA shows concentrated search regions consistent with direct knowledge retrieval rather than step-by-step reasoning. Across decoding methods on AQuA (CoT 84.4%, least-to-most 82.2%, MCTS 75.8%, tree-of-thought 81.6%), methods whose correct trajectories converge faster achieve higher accuracy. The reasoning model QwQ-32B shows more complex landscapes with self-evaluation and self-correction appearing early, and greater diversity among correct trajectories. Verifier results: with 10 trajectories the gain over unweighted voting is modest but consistent across models and decoding methods, with the largest gains on the 1B and 3B models. The scaling result is the strongest: on StrategyQA, sweeping from 1 to 50 trajectories, the verifier passes 65% accuracy while unweighted voting saturates near 30%. Transfer is partial — a verifier trained on AQuA improves StrategyQA by 4.5% and one trained on the 70B model improves the 3B model by 5.5% — but not all pairs benefit.

## Limitations

The paper is candid that verifier transfer across datasets and models works in some pairs and not others, and leaves improving it to future work. Scope limits are structural: the method needs multiple-choice questions, since the features are distances to enumerated candidate answers, with extension to open-ended tasks discussed only in an appendix; and it needs a model that exposes token likelihoods, so closed models are excluded. A reader should note that the qualitative observations rest on 50 problems per dataset, which is thin for claims about dataset-level reasoning behaviour, and that t-SNE layouts are sensitive to their own hyperparameters — the paper reports robustness to alternative dimensionality reduction in an appendix, but the visual impressions that motivate the observations are still mediated by a stochastic embedding. The verifier's headline scaling result is shown on one dataset (StrategyQA), which is also the dataset where the unweighted baseline saturates lowest, so the size of the gap should not be read as typical. Finally, the metrics are defined relative to the trajectory's own final state, so consistency measures early agreement with wherever the model ended up, not with the truth.

## Why it matters here

- **test-time-scaling**: Two contributions land squarely here. The verifier is a cheap alternative to the usual test-time-scaling machinery: it scores trajectories from features already computed by the generating model, with a random forest rather than a trained reward model, and its advantage grows with the number of sampled trajectories rather than saturating — the StrategyQA sweep from 1 to 50 trajectories is exactly the accuracy-versus-budget curve this topic tracks, and the baseline flattening near 30% while the verifier passes 65% is a clear case of aggregation, not sampling, being the binding constraint. Separately, the diagnostic result that incorrect trajectories converge early while correct ones converge late gives a mechanism for why verifier-weighted selection beats majority voting: a wrong answer accumulates confident votes sooner, so counting votes rewards the failure mode. The cross-method landscapes also let CoT, least-to-most, MCTS and tree-of-thought be compared on how they move through answer space rather than only on final accuracy.

## Entities

- **Concepts**: [reasoning trajectory](../../../../wiki/concepts/reasoning-trajectory.md), intermediate state, answer-space distance features, trajectory convergence, consistency, uncertainty, thought-level perplexity, verifier-weighted voting, [self-correction](../../../../wiki/concepts/self-correction.md), post-hoc analysis
- **Methods**: landscape of thoughts (LoT), [t-SNE](../../../../wiki/methods/t-sne.md), [chain-of-thought](../../../../wiki/methods/chain-of-thought.md), least-to-most prompting, tree-of-thought, [Monte Carlo tree search](../../../../wiki/methods/monte-carlo-tree-search.md), random forest, weighted majority voting
- **Datasets**: AQuA, [MMLU](../../../../wiki/datasets/mmlu.md), [StrategyQA](../../../../wiki/datasets/strategyqa.md), [CommonsenseQA](../../../../wiki/datasets/commonsenseqa.md)

Tags: `visualization`, `reasoning analysis`, `verifier`, `test-time scaling`, `uncertainty`, `perplexity`, `t-sne`, `multiple choice`

## Abstract

Numerous applications of large language models (LLMs) rely on their ability to perform step-by-step reasoning. However, the reasoning behavior of LLMs remains poorly understood, posing challenges to research, development, and safety. To address this gap, we introduce landscape of thoughts (LoT), the first landscape visualization tool to inspect the reasoning trajectories with certain reasoning methods on any multi-choice dataset. We represent the textual states in a trajectory as numerical features that quantify the states' distances to the answer choices. These features are then visualized in two-dimensional plots using t-SNE. Qualitative and quantitative analysis with the landscape of thoughts effectively distinguishes between strong and weak models, correct and incorrect answers, as well as different reasoning tasks. It also uncovers undesirable reasoning patterns, such as low consistency and high uncertainty. Additionally, users can adapt LoT to a model that predicts the property they observe. We showcase this advantage by adapting LoT to a lightweight verifier that evaluates the correctness of trajectories. Empirically, this verifier boosts the reasoning accuracy and the test-time scaling effect.

---

Record id: `local:1b977d02353e100b`
