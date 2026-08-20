<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Optimizing Test-Time Compute via Meta Reinforcement Fine-Tuning

- **Authors**: Yuxiao Qu, Matthew Y. R. Yang, Amrith Setlur, Lewis Tunstall, Edward Emanuel Beeching, Ruslan Salakhutdinov, Aviral Kumar
- **Venue**: ICML 2025
- **Published**: 2025-01-01
- **Source**: local
- **Topics**: test-time-scaling, reasoning-training
- **Relevance score**: test-time-scaling 0.50

## In one line

Formalizes 'spend test-time compute well' as a meta-reinforcement-learning problem — treating one long output stream as a sequence of episodes and scoring it by cumulative regret over tokens — and trains against a dense progress bonus that outcome-only reward cannot express.

## Problem

Models are trained to spend test-time compute by generating long chains, either by fine-tuning on search traces or by RL against a 0/1 outcome reward, but nobody has asked whether those approaches use the compute efficiently or whether they keep paying off as the budget grows. Two concrete failures motivate the paper: models may spend tokens far beyond the length a typical solution needs, including on easy questions, and it is unclear whether they can discover solutions to harder questions when run at budgets much larger than those seen in training. Outcome-reward RL is blind to both, because a 0/1 signal at the end says nothing about whether any individual segment of the stream earned its tokens.

## Contributions

- A meta-RL formalization of test-time compute: the long output stream is segmented into episodes run at test time, so the question becomes how an agent should trade exploration against exploitation within a single generation rather than across training.
- Cumulative regret over output tokens as the efficacy measure — the area between an oracle's success probability as a function of budget and the model's own — which makes 'efficient use of test-time compute' a quantity rather than an intuition.
- The empirical finding that state-of-the-art reasoning models do not minimize this regret, so their token spending is not efficient under the paper's criterion.
- A dense reward bonus that fixes it: the progress made by each subsequent block of the output stream, quantified as the change in the likelihood of eventual success, added to the usual 0/1 outcome reward.
- MRT, a class of fine-tuning methods built on that bonus, evaluated against outcome-reward RL on mathematical reasoning.

## Method

The output stream is divided into semantically meaningful segments, and each segment is treated as one episode of a meta-RL problem in which the model must both make progress on the answer and gather information that improves its later attempts. Under this view, a well-behaved reasoning trace looks like a regret-minimizing agent: early segments may explore, but every segment should raise the probability of eventual success by enough to justify its tokens. Efficacy is measured by cumulative regret against an oracle whose success probability rises monotonically with budget — geometrically, the area between the oracle's curve and the model's, which MRT is designed to minimize. The training signal follows directly: rather than only a 0/1 correctness reward at the end, each block receives a dense bonus equal to the change in likelihood of eventual success that it produced, so a block that advances the solution is rewarded and one that merely consumes tokens is not. This bonus is optimized jointly with the outcome reward, and the paper instantiates the idea as a family of fine-tuning methods rather than a single algorithm.

## Results

MRT yields a 2-3x relative gain in performance and roughly a 1.5x gain in token efficiency on mathematical reasoning compared with outcome-reward RL. The diagnostic result underlying the method is equally important: current state-of-the-art models do not minimize cumulative regret over their output stream, meaning their progress toward a correct answer is inconsistent across the stream rather than monotone — some segments raise the probability of success and others do not, and outcome-reward RL provides no pressure to distinguish them.

## Limitations

No limitations section is present in the material read. Points a reader should weigh: the progress bonus is defined as the change in likelihood of eventual success, which must itself be estimated, so the method inherits whatever bias that estimator carries and the paper's advantage over outcome-reward RL depends on that estimate being better than nothing — the archive's process-reward work suggests such estimates degrade exactly on hard problems. The segmentation of the output stream into blocks is a design choice that determines what 'progress' is measured over. Evaluation is on mathematical reasoning, so whether regret-minimizing token spending transfers to domains without a verifiable answer is untested. And the headline figures are relative gains against one baseline family; absolute accuracies and the benchmark composition matter for comparison against the wider literature.

## Why it matters here

- **reasoning-training**: The cleanest statement in this archive of what a training signal for reasoning should optimize. Every other training paper here asks which tokens should receive gradient — entropy, divergence, covariance, advantage sign — and answers with a selection rule. This one changes the objective instead: the target is not accuracy at the end but the shape of the progress curve along the way, made precise as cumulative regret over output tokens. That reframing subsumes several separate concerns the archive tracks as distinct problems. Overthinking becomes regret incurred after the answer is settled. The failure of outcome-only supervision, which the archive's complexity-theoretic paper explains by circuit depth, gets a second explanation here: a 0/1 signal cannot tell a segment that earned its tokens from one that did not. And the dense progress bonus is a process reward derived without step labels, which places it alongside the archive's implicit-PRM result as a third route to label-free step feedback — this one obtained by changing what is rewarded rather than how the reward is parameterized.
- **test-time-scaling**: Answers a question this topic keeps circling without formalizing: what does it mean to spend inference compute well. The archive measures this indirectly — tokens saved at matched accuracy, the point where a pass@k curve flattens, the fraction of a trace generated after the answer stabilized. Cumulative regret over the output stream unifies those into one quantity with an oracle reference, and the finding that state-of-the-art models fail to minimize it is the general version of the specific wastes this archive documents. It also inverts the topic's usual direction of causation. Every other method here treats the model as fixed and engineers the inference procedure around it — stopping rules, trajectory selection, budget allocation. MRT trains the model so that its own token stream is efficient, which if it works makes the external machinery less necessary. The 1.5x token-efficiency gain is modest next to the 5-15% savings the archive's early-exit methods report, but it is obtained without any inference-time apparatus at all.

## Entities

- **Concepts**: meta-reinforcement learning, [test-time compute](../../../../wiki/concepts/test-time-compute.md), cumulative regret, dense reward, progress bonus, [exploration-exploitation trade-off](../../../../wiki/concepts/exploration-exploitation-trade-off.md), [token efficiency](../../../../wiki/concepts/token-efficiency.md), [overthinking](../../../../wiki/concepts/overthinking.md), [process-supervision](../../../../wiki/concepts/process-supervision.md), [outcome reward](../../../../wiki/concepts/outcome-reward.md)
- **Methods**: MRT (Meta Reinforcement Fine-Tuning), outcome-reward RL, [RLVR](../../../../wiki/methods/rlvr.md), supervised finetuning on search traces, [process reward model](../../../../wiki/methods/process-reward-model.md)
- **Datasets**: [MATH](../../../../wiki/datasets/math.md), [AIME24](../../../../wiki/datasets/aime-2024.md)

Tags: `meta-rl`, `test-time compute`, `regret`, `dense reward`, `token efficiency`, `rl fine-tuning`

## Abstract

Training models to effectively use test-time compute is crucial for improving the reasoning performance of LLMs. Current methods mostly do so via fine-tuning on search traces or running RL with 0/1 outcome reward, but do these approaches efficiently utilize test-time compute? Would these approaches continue to scale as the budget improves? In this paper, we try to answer these questions. We formalize the problem of optimizing test-time compute as a meta-reinforcement learning (RL) problem, which provides a principled perspective on spending test-time compute. This perspective enables us to view the long output stream from the LLM as consisting of several episodes run at test time and leads us to use a notion of cumulative regret over output tokens as a way to measure the efficacy of test-time compute. Akin to how RL algorithms can best tradeoff exploration and exploitation over training, minimizing cumulative regret would also provide the best balance between exploration and exploitation in the token stream. While we show that state-of-the-art models do not minimize regret, one can do so by maximizing a dense reward bonus in conjunction with the outcome 0/1 reward RL. This bonus is the "progress" made by each subsequent block in the output stream, quantified by the change in the likelihood of eventual success. Using these insights, we develop Meta Reinforcement Fine-Tuning, or MRT, a new class of fine-tuning methods for optimizing test-time compute. MRT leads to a 2-3x relative gain in performance and roughly a 1.5x gain in token efficiency for math reasoning compared to outcome-reward RL.

---

Record id: `local:c45962c819666804`
