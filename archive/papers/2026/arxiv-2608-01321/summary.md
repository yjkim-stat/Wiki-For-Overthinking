<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# BiCAA: Bidirectional Credit Assignment for Search-Augmented Agent

- **Authors**: Yibin Huang, Bin Xu, Hailong Cao, Conghui Zhu
- **Venue**: cs.CL
- **Published**: 2026-08-02
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.01321>
- **PDF**: <https://arxiv.org/pdf/2608.01321v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.40

## In one line

Gives each retrieval step of a search agent a dense reward built from two ground-truth-conditioned signals — how much the step raised the model's likelihood of the correct answer, and how necessary the step looks in hindsight — and fuses them asymmetrically so that a step which helps locally but is redundant globally is discounted.

## Problem

GRPO rewards a search agent only on its final answer, so a trajectory of ten retrievals receives one scalar and nothing distinguishes the retrieval that found the key document from the one that repeated a query. The paper's claim is that the resulting sparsity produces training instability and redundant search. Existing process rewards pick one of two views and each is insufficient on its own: forward signals such as information gain measure a step's immediate contribution but cannot tell a locally useful step from a necessary one, while hindsight attribution identifies which steps mattered for the final answer but gives no feedback on how a step changed the agent's information state when it was taken.

## Contributions

- Two criteria for judging a search step stated separately: forward solvability gain, the marginal rise in the token-averaged log-likelihood of the gold answer caused by that retrieval, and hindsight success criticality, the step's action log-likelihood when the gold answer is placed in the prompt, normalized against the trajectory average
- An asymmetric fusion rule that multiplies a positive gain by the criticality weight and a negative gain by its reciprocal, so pivotal helpful steps are amplified while redundant harmful ones are penalized harder
- A unified advantage that normalizes process and outcome rewards separately before combining them, with geometric discounting on the process term only
- A four-quadrant step-level analysis showing the two signals disagree often enough to matter, and that agreement predicts retrieval quality

## Method

For each intermediate step, forward solvability gain is the difference between successive token-level average log-likelihoods of the ground-truth answer given the trajectory prefix. Hindsight success criticality is the geometric mean of token-wise action log-likelihoods with the ground-truth answer conditioned into the prompt, divided by the trajectory-wide mean and clipped to a fixed interval, so a value above 1 marks a step the policy favours once the answer is known. The two are fused as omega*g when g is non-negative and g/omega when it is negative. Process and outcome rewards are z-normalized within each group of G rollouts, and the turn-level advantage adds the undiscounted normalized outcome reward to a geometrically discounted sum of the next L process rewards scaled by alpha; the result is trained with a clipped surrogate and a KL penalty, with gradients computed only on decision tokens and tool responses masked. Backbones are Qwen2.5-7B-Instruct and Qwen3-8B on 8 GPUs, global batch 32, group size 16, learning rate 1e-6, alpha 0.25, KL coefficient 0.001, with E5-base-v2 over a local Wikipedia corpus returning the top 3 passages and interaction capped at 10 turns. Evaluation is word-level F1 over four in-domain sets (NQ, TriviaQA, HotpotQA, 2WikiMultiHopQA) and three out-of-domain ones (MuSiQue, Bamboogle, PopQA).

## Results

On Qwen2.5-7B-Instruct the average across seven benchmarks is 52.1 against 48.3 for the strongest RL baseline HCAPO, 47.2 for GiGPO, 45.7 for IGPO, 38.5 for Search-R1 and 36.4 for CoT+RAG. The gain concentrates on multi-hop sets: 57.7 on HotpotQA and 51.9 on 2Wiki, which is 20.6 and 27.5 above CoT+RAG. It is not uniform — on Bamboogle BiCAA reaches 59.0 while HCAPO reaches 69.0 and GiGPO 68.9, so the method loses that benchmark by about ten F1 while winning the average. On Qwen3-8B the average rises from 50.9 for GRPO to 53.3. The ablations separate the three reward terms: removing forward solvability gain costs 3.6 points of average (52.1 to 48.5) and the damage is concentrated in multi-hop reasoning (HotpotQA 57.7 to 51.8, 2Wiki 51.9 to 46.2, MuSiQue 28.6 to 24.2) while single-hop NQ barely moves (45.5 to 44.6); removing hindsight criticality costs 2.8 (to 49.3); and removing the terminal outcome reward is the largest loss at 6.3 (to 45.8) and is the only one that degrades every benchmark, so dense process supervision alone does not anchor the policy. The step-level classification supports the fusion rule: where both signals are positive, 78.4% of retrievals are judged useful and 12.1% repeated, whereas positive gain with low criticality drops usefulness to 47.2% and raises repetition to 36.8%, and where both are negative only 24.3% are useful and 46.3% are off-target. Behaviourally, the variant without criticality shows search frequency climbing monotonically through training with redundancy surging, while the full method peaks mid-training and declines. The alpha sweep is sharp: 0.00 gives 45.4, 0.25 gives 52.1, and 1.00 falls to 44.8, below several baselines. The two extra signals cost 10 to 13 percent of per-step training latency.

## Limitations

The paper has no limitations section. What a reader should weigh: both signals condition on the ground-truth answer, so neither exists at inference and neither transfers to a setting where answers are unavailable — this is a training-time reward shaping result, not a step-level verifier. The alpha sweep that selects 0.25 is run on the same benchmarks the headline table reports, and the curve is steep enough (44.8 at alpha=1.00) that the setting is doing real work, so the reported average carries a hyperparameter chosen on the evaluation. The Bamboogle deficit against two baselines is visible in the main table and is not discussed. The step-level quadrant analysis, which is the main evidence that the two signals are complementary rather than redundant, rests on GPT-5.5 labelling 100 sampled trajectories with no human validation of those labels and no inter-rater check. No variance or seed count is reported for any number in the paper. The retrieval configuration is fixed throughout — one dense retriever, top-3 passages, a local Wikipedia corpus, 10 turns — so the redundancy findings are tied to a setting where more search has a bounded payoff.

## Why it matters here

- **reasoning-training**: It is a concrete instance of the pattern this archive keeps meeting in RLVR: a sparse terminal reward is insufficient, dense process reward alone is worse, and the working configuration is a weighted blend whose weight matters more than either component. The ablation makes that precise here — removing the outcome reward costs more than removing either process signal, and the process weight collapses performance below baseline when pushed to 1.00. The forward/hindsight decomposition is also worth carrying: a step that raises answer likelihood and a step that was necessary are separately measurable, they disagree on a substantial fraction of retrievals, and that disagreement is what identifies redundant search.

## Entities

- **Concepts**: [credit assignment](../../../../wiki/concepts/credit-assignment.md), process reward, outcome reward, hindsight credit assignment, [advantage estimation](../../../../wiki/concepts/advantage-estimation.md), reward sparsity, multi-hop reasoning, search-augmented reasoning, redundant search
- **Methods**: BiCAA, forward solvability gain, hindsight success criticality, [GRPO](../../../../wiki/methods/grpo.md), [PPO](../../../../wiki/methods/ppo.md), Search-R1, IGPO, GiGPO, HCAPO, [retrieval-augmented generation](../../../../wiki/methods/retrieval-augmented-generation.md)
- **Datasets**: Natural Questions, TriviaQA, HotpotQA, 2WikiMultiHopQA, MuSiQue, Bamboogle, PopQA

Tags: `credit assignment`, `agentic search`, `process reward`, `reinforcement learning`, `multi-hop qa`

## Abstract

Multi-step search is a fundamental capability for search agents, enabling them to iteratively acquire, refine, and integrate external evidence for complex reasoning QA. However, vanilla GRPO allocates rewards exclusively based on the model's final outputs, yielding outcome-only supervision with no supervisory signals for intermediate reasoning steps. Such sparse supervision easily causes training instability and redundant search behaviors on multi-step search tasks. To mitigate this limitation, we adopt process reward to deliver stepwise supervision signals. For this process reward, we propose two complementary criteria to judge each search step: whether the step yields new evidence to facilitate problem solving, and whether it forms an efficient, pivotal intermediate decision within the overall reasoning trajectory. Building on this insight, we propose BiCAA: a bidirectional credit assignment framework that delivers dense, distinguishing process rewards for search-augmented agents. BiCAA builds bidirectional process rewards by fusing two complementary signals: forward solvability gain and hindsight success criticality. The former quantifies step-wise improvements in answer plausibility, while the latter evaluates each step's necessity for final success via hindsight outcome-based criticality scoring. We modulate and aggregate the two signals and then fuse them with the outcome reward. Experiments on search-augmented QA benchmarks show that BiCAA stabilizes policy optimization, reduces redundant search behavior, and achieves competitive performance.

---

Record id: `arxiv:2608.01321`
