<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Revisiting the Test-Time Scaling of o1-like Models: Do they Truly Possess Test-Time Scaling Capabilities?

- **Authors**: Zhiyuan Zeng, Qinyuan Cheng, Zhangyue Yin, Yunhua Zhou, Xipeng Qiu
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2025.acl-long.232/>
- **PDF**: <https://aclanthology.org/2025.acl-long.232.pdf>
- **DOI**: 10.18653/v1/2025.acl-long.232
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Systematically shows that o1-like models (QwQ, R1, LIMO, and R1-Distill variants) do not actually possess consistent sequential test-time scaling: correct solutions are on average shorter than incorrect ones on the same questions, accuracy does not consistently improve (and sometimes inverse-scales) with solution length, and this traces to a failure of self-revision (models rarely fix wrong answers and sometimes break correct ones) -- leading to Shortest Majority Vote, a parallel-scaling method weighting majority-vote clusters by inverse-log solution length, which significantly outperforms both plain Majority Vote and a shortest-solution-only heuristic.

## Problem

Whether o1-like reasoning models genuinely possess test-time scaling capability -- performance that reliably improves as the chain-of-thought is allowed to grow longer -- remained unverified, despite widespread assumption that longer CoT inherently yields better reasoning.

## Contributions

- systematic evidence across five o1-like models and four benchmarks that longer chain-of-thought does not consistently improve, and sometimes inversely correlates with, accuracy -- correct solutions are on average shorter than incorrect ones on matched questions
- identification of insufficient self-revision capability (low wrong-to-correct conversion rate, comparable or higher correct-to-wrong conversion rate for weaker models) as the primary mechanistic cause of failed sequential scaling
- a direct comparison showing parallel scaling achieves better coverage and scalability than sequential self-revision at matched compute for o1-like models
- Shortest Majority Vote, a parallel-scaling method that weights majority-vote answer clusters by count divided by log-mean-solution-length, significantly outperforming conventional Majority Vote and a naive shortest-solution heuristic

## Method

Samples each of five o1-like models (QwQ, R1-671b, R1-Distill-32b/14b/1.5b, LIMO) five times per question across four benchmarks (MATH-500, AIME, Omni-MATH, GPQA-diamond), sorts the five same-question solutions by length into five rank groups, and compares length and accuracy across groups. Separately measures, for each question with both correct and incorrect sampled solutions, whether correct solutions are shorter or longer on average. To probe why, counts self-revision markers ('Wait', 'Alternatively') as a proxy for solution length growth, and force-prompts models to continue reasoning for up to 40 additional steps (using the higher-probability of 'Wait'/'Alternatively' as the continuation cue) on AIME, tracking accuracy, solution length, and the proportion of wrong-to-correct versus correct-to-wrong answer flips across revision steps, plus the proportion of revisions that simply retain the original (possibly wrong) answer. Compares sequential scaling (iterative self-revision) against parallel scaling (10 independently sampled solutions, majority vote) on coverage (pass@k) and accuracy for R1-Distill-32b and QwQ. Proposes Shortest Majority Vote: within each majority-vote answer cluster i (count c_i, mean solution length l_i), score s_i = c_i / log(l_i), and select the cluster with the highest score as the final answer -- log-discounting length so long solutions do not simply dominate purely on token count, motivated by the empirical log-linear relationship between performance and compute.

## Results

The longest-solution group is on average roughly twice as long as the shortest-solution group across all models/benchmarks, but accuracy across the five length-ranked groups shows no consistent improvement, and for AIME and Omni-MATH specifically an inverse-scaling pattern appears (accuracy decreases as solution length increases). Across all model sizes and datasets, average correct-solution length is consistently shorter than average incorrect-solution length on the same questions; this length gap is larger for weaker models (QwQ, R1-Distill-1.5b) than for the strongest model (R1-671b). Solution length correlates strongly (near-linearly) with the frequency of self-correction markers ('Wait'), confirming length growth is driven by self-revision. Forced continued-reasoning experiments (up to 40 extra steps on AIME) show solution length grows almost linearly with steps (nearly tripling by step 40), while accuracy of QwQ and R1-Distill-1.5b decreases monotonically with more revision steps; R1-Distill-32b/14b and LIMO show initial improvement that plateaus/oscillates after ~10 steps. The successful-revision rate (wrong-to-correct) stays below 10% for all five models throughout revision, while the failed-revision rate (correct-to-wrong) is comparable or, for QwQ and R1-Distill-1.5b, higher than the successful-revision rate -- directly explaining why forcing more revision hurts these two models. When the model's original answer is wrong, it simply retains that wrong answer in 32-72% of revisions (R1-Distill-32b 72%, R1-14b 70%, R1-1.5b 58%, LIMO 54%, QwQ 32%), showing self-revision mostly fails to correct errors rather than actively worsening them, except for the two weakest sequential-scalers. Comparing scaling strategies: parallel scaling (10 samples, majority vote) achieves substantially higher coverage (pass@k) than sequential scaling (40-step self-revision) at matched token budget for both R1-Distill-32b and QwQ, and sequential revision's computational cost is higher for the same token count since it attends over a longer context. Shortest Majority Vote significantly outperforms both plain Majority Vote and a naive 'always pick shortest solution' heuristic across R1-Distill-32b/14b/1.5b, QwQ and LIMO on both AIME and GPQA, at both 2 and 16 sampled solutions (e.g. AIME, 16 solutions: R1-Distill-1.5b 40.00% MV -> 42.20% Shortest MV; QwQ 51.33% MV -> 62.25% Shortest MV; LIMO 68.88% MV -> 70.00% Shortest MV); a log-length weighting outperforms sqrt/linear/square alternatives, which are shown to be unstable and sometimes degrade performance versus plain Majority Vote.

## Limitations

Evaluation on the full R1-671b model was limited to the initial length/accuracy analysis (Figures 1-2) due to its considerable inference cost; all subsequent revision/scaling experiments used the smaller distilled R1 variants instead. The experimental framework is limited to static model checkpoints; the authors explicitly flag that test-time scaling behavior under dynamic (e.g. RL-training-time-evolving) checkpoints is unstudied and left to future work. Shortest Majority Vote may have limited applicability to models with genuinely strong sequential-scaling capability (were one to exist), since it assumes shorter solutions are a useful signal -- though the authors note solution length remains valuable as a guidance signal for candidate selection even in that case, and suggest a 'Longest Majority Vote' variant as a fallback.

## Why it matters here

- **overthinking**: Directly central to the topic and one of its strongest empirical anchors: it provides systematic, multi-model, multi-benchmark evidence that longer reasoning traces in o1-like models do not reliably improve accuracy and can inverse-scale, with a clear mechanistic account (self-revision failing to fix errors, and for the weakest models actively breaking correct answers more often than it fixes wrong ones) -- directly explaining a major form of overthinking as a self-revision-capability deficit rather than a pure length problem. Its practical fix, Shortest Majority Vote, is a concrete, immediately-applicable inference-time method that uses solution length itself as a signal to counteract this failure mode.

## Entities

- **Concepts**: inverse scaling with chain-of-thought length, self-revision failure (successful- vs. failed-revision rate), [sequential vs. parallel test-time scaling](../../../../wiki/concepts/sequential-vs-parallel-test-time-scaling.md), Shortest Majority Vote (length-discounted majority voting)
- **Methods**: forced continued-reasoning ('Wait'/'Alternatively' prompted revision), sequential scaling (self-revision), parallel scaling (majority vote), Shortest Majority Vote
- **Datasets**: [MATH-500](../../../../wiki/datasets/math500.md), AIME (AIMO validation set, 90 questions), Omni-MATH (500-question sample), GPQA-diamond (198 questions)

Tags: `overthinking`, `test-time-scaling`, `self-revision`, `inverse-scaling`, `majority-voting`

## Abstract

The advent of test-time scaling in large language models (LLMs), exemplified by OpenAI’s o1 series, has advanced reasoning capabilities by scaling computational resource allocation during inference. While successors like QwQ, Deepseek-R1 (R1) and LIMO replicate these advancements, whether these models truly possess test-time scaling capabilities remains underexplored. This study found that longer CoTs of these o1-like models do not consistently enhance accuracy; in fact, correct solutions are often shorter than incorrect ones for the same questions. Further investigation shows this phenomenon is closely related to models’ self-revision capabilities - longer CoTs contain more self-revisions, which often lead to performance degradation. We then compare sequential and parallel scaling strategies on QwQ, R1 and LIMO, finding that parallel scaling achieves better coverage and scalability. Based on these insights, we propose “Shortest Majority Vote”, a method that combines parallel scaling strategies with CoT length characteristics, significantly improving models’ test-time scalability compared to conventional majority voting approaches.

---

Record id: `doi:10.18653/v1/2025.acl-long.232`
