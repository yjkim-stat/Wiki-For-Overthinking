<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?

- **Authors**: Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Yang Yue, Shiji Song, Gao Huang
- **Venue**: preprint
- **Published**: 2025-01-01
- **Source**: local
- **Topics**: reasoning-training, reasoning-evaluation, test-time-scaling

## In one line

Measures RLVR-trained models against their base models with pass@k at large k and finds the base wins, concluding RLVR sharpens sampling toward paths the base already had rather than adding new ones.

## Problem

RLVR is assumed to work like classical RL — exploration discovering strategies the agent did not have. That assumption is tested by average-case metrics such as greedy decoding or pass@1, which cannot distinguish a model that acquired a new capability from one that became more likely to sample an old one.

## Contributions

- The use of pass@k at large k as a reasoning-boundary metric rather than an average-case one
- The finding that base models overtake their RLVR-trained counterparts as k grows, across model families, algorithms and math, code and visual benchmarks
- Evidence that the boundary narrows monotonically as RLVR training proceeds
- Coverage and perplexity analysis placing RLVR reasoning paths inside the base model's sampling distribution
- The sampling efficiency gap, showing six popular RLVR algorithms perform similarly and remain far from the base-model bound
- The contrast with distillation, which does introduce patterns absent from the student's base model

## Method

Pass@k at large k is used as the boundary metric: a problem counts as solved if any of k samples is correct, so the average over a dataset estimates what a model can reach given enough attempts rather than what it does on the first. An unbiased low-variance estimator is used. Coverage and perplexity analysis then asks whether the RLVR model's paths lie inside the base model's output distribution. A sampling efficiency gap is defined as the RLVR model's pass@1 against the base model's pass@k at k=256, treating the base as the upper bound, and six algorithms are compared on it. Guessing is addressed by manually checking CoT correctness on a subset and by leaning on code tasks where a compiler and unit tests verify. Few-shot prompts are deliberately avoided for base models to keep the comparison unconfounded.

## Results

Across LLaMA-3.1-8B and Qwen2.5-7B/14B/32B-Base on AIME24, MATH500, Minerva and Olympiad, RLVR models lead at small k and base models catch up and surpass them as k grows into the tens or hundreds. The reasoning boundary narrows further as RLVR training progresses: on Omni-MATH-Train, pass@1 rises across GRPO steps 150, 300 and 450 while coverage at pass@256 falls. Perplexity analysis places RLVR-generated paths inside the base model's distribution. Six algorithms — PPO, GRPO, Reinforce++, RLOO, ReMax, DAPO — show only minor variation in the sampling efficiency gap and all remain far from the base-model bound. Distillation behaves differently and does expand the boundary beyond the base model. Sampling used temperature 0.6, top-p 0.95 and up to 16,384 tokens.

## Limitations

The paper is explicit that at astronomically large k even uniform sampling would eventually stumble on a correct path, and defends its range by noting the base model already wins at k=128 or 1024. Its own guessing control is manual checking on a subset plus reliance on code tasks, which is weaker than verifying every math CoT — and this is exactly the gap the companion study exploits. Zero-RL is used for math but instruction-tuned starting points for code and visual tasks, so the comparison is not uniform across domains. Pass@k is presented as a boundary probe rather than a practical metric, so a narrowed boundary and a better deployed model are not in conflict.

## Why it matters here

- **reasoning-evaluation**: Argues that the field's default metrics measure the wrong thing — pass@1 and greedy decoding report average-case behaviour and cannot see a boundary. The paper's own caveat is the more durable contribution for this topic: pass@k on mathematics is contaminated by guessing, because a wrong chain can land on a right short answer, and the authors mitigate it only by manual inspection of a subset. That admission is the opening the companion study widens with CoT-Pass@K.
- **reasoning-training**: The sharpest challenge in the archive to what RLVR is for. If every path an RLVR model produces already lies in the base model's distribution, then the training signal is a resampling device and the capability ceiling was set in pretraining — which would mean the archive's entire token-selection and credit-assignment literature is optimizing allocation within a fixed set rather than enlarging it. That six algorithms differ only marginally on the sampling efficiency gap supports the same reading: the algorithms are converging on the same reachable set. Read against the companion paper (arXiv 2506.14245), which this archive also holds, the disagreement turns out to be about the metric rather than the phenomenon.
- **test-time-scaling**: Reframes the pass@k curve as a statement about a model's reachable set rather than a scaling law: the crossing point where a base model overtakes its RLVR counterpart is where extra sampling stops buying efficiency and starts revealing coverage. For anything in this topic that spends compute on repeated sampling, it implies the returns depend on which model is sampled, and that the RLVR-trained one may be the worse choice at large budgets.

## Entities

- **Concepts**: [pass-k](../../../../wiki/concepts/pass-k.md), [reasoning boundary](../../../../wiki/concepts/reasoning-boundary.md), [exploration-exploitation trade-off](../../../../wiki/concepts/exploration-exploitation-trade-off.md), sampling efficiency, [entropy collapse](../../../../wiki/concepts/entropy-collapse.md), reasoning distillation, coverage, base model as upper bound
- **Methods**: pass@k, [RLVR](../../../../wiki/methods/rlvr.md), [GRPO](../../../../wiki/methods/grpo.md), [PPO](../../../../wiki/methods/ppo.md), [Reinforce++](../../../../wiki/methods/reinforce.md), [RLOO](../../../../wiki/methods/rloo.md), ReMax, [DAPO](../../../../wiki/methods/dapo.md), perplexity analysis, [reasoning distillation](../../../../wiki/methods/reasoning-distillation.md)
- **Datasets**: [AIME24](../../../../wiki/datasets/aime-2024.md), [AMC23](../../../../wiki/datasets/amc23.md), [MATH500](../../../../wiki/datasets/math500.md), [Minerva](../../../../wiki/datasets/minerva.md), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md), [GSM8K](../../../../wiki/datasets/gsm8k.md), Omni-MATH-Rule, [LiveCodeBench](../../../../wiki/datasets/livecodebench.md), [HumanEval+](../../../../wiki/datasets/humaneval.md), [MathVista](../../../../wiki/datasets/mathvista.md), [MathVision](../../../../wiki/datasets/mathvision.md)

Tags: `rlvr`, `pass@k`, `reasoning boundary`, `base model`, `distillation`

## Abstract

Reinforcement Learning with Verifiable Rewards (RLVR) has recently demonstrated notable success in enhancing the reasoning performance of large language models (LLMs), particularly in mathematics and programming tasks. It is widely believed that, similar to how traditional RL helps agents to explore and learn new strategies, RLVR enables LLMs to continuously self-improve, thus acquiring novel reasoning abilities that exceed the capacity of the corresponding base models. In this study, we take a critical look at the current state of RLVR by systematically probing the reasoning capability boundaries of RLVR-trained LLMs across various model families, RL algorithms, and math/coding/visual reasoning benchmarks, using pass@k at large k values as the evaluation metric. While RLVR improves sampling efficiency towards correct paths, we surprisingly find that current training rarely elicit fundamentally new reasoning patterns. We observe that while RLVR-trained models outperform their base models at smaller values of k (e.g., k=1), base models achieve higher pass@k score when k is large. Moreover, we observe that the reasoning capability boundary of LLMs often narrows as RLVR training progresses. Further coverage and perplexity analysis shows that the reasoning paths generated by RLVR models are already included in the base models' sampling distribution, suggesting that their reasoning abilities originate from and are bounded by the base model. From this perspective, treating the base model as an upper bound, our quantitative analysis shows that six popular RLVR algorithms perform similarly and remain far from optimal in fully leveraging the potential of the base model. In contrast, we find that distillation can introduce new reasoning patterns from the teacher and genuinely expand the model's reasoning capabilities. Taken together, our findings suggest that current RLVR methods have not fully realized the potential of RL to elicit genuinely novel reasoning abilities in LLMs. This underscores the need for improved RL paradigms, such as effective exploration mechanism, more deliberate and large-scale data curation, fine-grained process signal, and multi-turn agent interaction, to unlock this potential.

---

Record id: `local:b050d2841cbb4959`
