<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# THOUGHTTERMINATOR: Benchmarking, Calibrating, and Mitigating Overthinking in Reasoning Models

- **Authors**: Xiao Pu, Michael Saxon, Wenyue Hua, William Yang Wang
- **Venue**: preprint
- **Published**: 2025-01-01
- **Source**: local
- **Topics**: overthinking

## In one line

The paper defines model-relative measures of overthinking (local/global overthinking scores) built from observed token-spend distributions, introduces the DUMB500 easy-question dataset to probe overthinking on trivial inputs, and proposes THOUGHTTERMINATOR, a training-free decoding-time technique that interrupts a reasoning model with token-budget reminders and forces an answer at a difficulty-calibrated deadline.

## Problem

Reasoning models trained with inference-time scaling often keep generating tokens after they could already produce a correct answer ("overthinking"), wasting compute; prior mitigations either require retraining/fine-tuning (costly, may hurt performance) or require white-box access to the base model's internals, and there was no resource to measure this tendency on easy questions where it is expected to be worst.

## Contributions

- Formalizes 'observational overthinking' via two metrics computed from sampled model outputs without needing a ground-truth minimal answer length: local envelope overthinking O_env (spread between max and min token spend per question) and global overthinking O_g (gap between a model's average spend and the best-observed minimum spend across a pool of models).
- Shows empirically on MATH500, GPQA and ZebraLogic that question difficulty (estimated as multi-model inaccuracy rate) correlates with token spend, but that reasoning models are poorly calibrated to it, especially on easy questions.
- Introduces DUMB500, a 500-question dataset of deliberately trivial math, chat, code and task questions, to extend overthinking evaluation to the easy end of the difficulty spectrum where existing hard benchmarks (MATH500/GPQA/ZebraLogic) offer few examples.
- Introduces THOUGHTTERMINATOR, a training-free, black-box decoding method that periodically inserts interrupt messages reporting tokens used/remaining (scheduled from a predicted per-question token budget) and forces a final answer via constrained decoding once the budget is exhausted.

## Method

The paper first defines question difficulty D(q,a) as a model's empirical inaccuracy rate over repeated samples of a question, and a multi-model difficulty as the expectation of this over a pool of models. It measures each answer's token spend and shows difficulty correlates with token spend (Figure 1). It then defines observational overthinking without needing a true minimal answer length: local envelope overthinking O_env(M) is the mean per-question gap between a model's max and min sampled token spend, and global overthinking O_g(M) is the mean per-question gap between a model's average spend and the minimum spend achieved by any model in a reference pool. THOUGHTTERMINATOR operates in three stages: (1) scheduling — given a question, estimate a token 'deadline' either via a difficulty predictor (a Llama-3-8B-Instruct fine-tuned to classify questions into 10 difficulty bins, each mapped to an average minimal-successful-answer token length from a training set) or a zero-shot gpt-4o difficulty estimate; (2) running — during generation, an interrupt message is inserted every n = min(250, deadline/2) tokens telling the model how many tokens it has used and how many remain, and at each interrupt a regex checks whether a final answer in the expected format has already been produced, terminating early if so; (3) terminating — if no answer has appeared by the deadline, a termination message is shown and a final answer is forced via constrained decoding using the same answer-format regex.

## Results

Table 2 (Base vs. Thought Terminator, 5 reasoning models across MATH500/GPQA/ZebraLogic/DUMB500 pooled): QwQ-32B-Preview: local O_env 2923→518 (-82%), global O_g 3698→693 (-81%), accuracy 0.80→0.79 (-1%). QwQ-32B: local O_env 13662→215 (-98%), global O_g 11248→1021 (-91%), accuracy 0.94→0.80 (-15%). DeepSeek-R1-Distill-Qwen-1.5B: local O_env 5730→696 (-88%), global O_g 4262→882 (-79%), accuracy 0.50→0.80 (+59%). DeepSeek-R1-Distill-Qwen-7B: local O_env 3881→678 (-83%), global O_g 4001→948 (-76%), accuracy 0.73→0.81 (+11%). DeepSeek-R1-Distill-Llama-8B: local O_env 4232→725 (-83%), global O_g 5755→1148 (-80%), accuracy 0.92→0.80 (-13%). All figures and percentage changes are read directly from Table 2 on page 8; the percentages in parentheses are the paper's own relative-change annotations, not independently recomputed. Text on page 8 additionally states 4/5 models on MATH500, 2/3 models on GPQA, and all models on ZebraLogic and DUMB500-MATH show significant overthinking reduction at effectively equivalent or better Pass@10 under THOUGHTTERMINATOR versus standard decoding (from Figure 6, not tabulated with exact numbers). Table 1 (page 3) gives base local/global overthinking scores without THOUGHTTERMINATOR, including for non-reasoning models (e.g. Llama-3.1-8B-Instruct: local O_env 1971, global O_g 1755) versus reasoning models (e.g. QwQ-32B: local 13662, global 11248), showing reasoning models have markedly higher raw overthinking scores than non-reasoning ones.

## Limitations

The paper's own difficulty and minimum-spend measures are model-pool-relative (defined over the specific set of models evaluated) rather than absolute. The trained difficulty estimator is a fine-tuned Llama-3-8B-Instruct classifier, so its budget predictions inherit whatever biases that training set has. THOUGHTTERMINATOR's gains are not uniform across models: QwQ-32B loses 15 accuracy points (0.94 to 0.80) and QwQ-32B-Preview loses 1 point despite large overthinking-score reductions, so the technique trades some accuracy for efficiency on the strongest base models even though it net-improves smaller/weaker ones. Evaluation of THOUGHTTERMINATOR is limited to DeepSeek-R1-distill and QwQ model families.

## Why it matters here

- **overthinking**: Directly on-topic for the stopping-criteria cluster: THOUGHTTERMINATOR is a training-free, black-box, decoding-time stopping method comparable in spirit to RCP/RCPD, ThinkBrake, NEAT, DEER, BLADE and REFRAIN, but its mechanism (periodic in-context token-budget reminders plus a forced constrained-decoding answer at a predicted deadline) differs from those that rely on internal confidence signals, probes, or white-box access. It also contributes two new measurement tools — local envelope (O_env) and global (O_g) overthinking scores — and a new easy-question benchmark (DUMB500) that the existing cluster's hard-benchmark evaluations (MATH500-, GPQA-, ZebraLogic-style) do not cover, and it reports a case (QwQ-32B) where large overthinking-score reduction comes with a real accuracy cost (-15 points), which complicates the cluster's general claim that stopping methods are largely accuracy-neutral.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), difficulty-calibrated token spend, observational overthinking, local envelope overthinking score, global overthinking score, difficulty estimation, test-time deadline scheduling, constrained decoding for answer termination
- **Methods**: THOUGHTTERMINATOR, DUMB500, difficulty-calibrated token budget scheduling, constrained decoding termination, trained difficulty estimator (fine-tuned Llama-3-8B-Instruct), zero-shot gpt-4o difficulty estimation
- **Datasets**: [MATH500](../../../../wiki/datasets/math500.md), [GPQA](../../../../wiki/datasets/gpqa.md), [ZebraLogic](../../../../wiki/datasets/zebralogic.md), DUMB500

Tags: `overthinking`, `test-time-compute`, `decoding-strategy`, `training-free`, `difficulty-calibration`, `benchmark`, `reasoning-models`

## Abstract

Reasoning models have demonstrated impressive performance on difficult tasks that traditional language models struggle at. However, many are plagued with the problem of overthinking—generating large amounts of unnecessary tokens which don't improve accuracy on a question. We introduce approximate measures of problem-level difficulty and demonstrate that a clear relationship between problem difficulty and optimal token spend exists, and evaluate how well calibrated a variety of reasoning models are in terms of efficiently allocating the optimal token count. We find that in general, reasoning models are poorly calibrated, particularly on easy problems. To evaluate calibration on easy questions we introduce DUMB500, a dataset of extremely easy math, reasoning, code, and task problems, and jointly evaluate reasoning model on these simple examples and extremely difficult examples from existing frontier benchmarks on the same task domain. Finally, we introduce THOUGHTTERMINATOR, a training-free black box decoding technique that significantly improves reasoning model calibration.

---

Record id: `local:eff598a06b1089db`
