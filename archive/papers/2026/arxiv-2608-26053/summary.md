<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# $R^3$: Training Robots to Reason in Natural Language via Reinforcement Learning

- **Authors**: Lehong Wu, Yuxiao Qu, Zheyuan Hu, Ivan Zhang, Limin Wei, Zackory Erickson, Aviral Kumar
- **Venue**: cs.RO
- **Published**: 2026-08-26
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.26053>
- **PDF**: <https://arxiv.org/pdf/2608.26053v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## In one line

R3 is a two-stage post-training recipe (SFT mid-training on expert reasoning traces, then rubric-based single-step RL on offline instruction-only data) that trains a vision-language model to produce free-form natural-language reasoning steering a frozen low-level robot policy, and shows this test-time reasoning causally improves generalization beyond what training-time reasoning supervision alone provides.

## Problem

Whether training a VLM to produce free-form natural-language reasoning at test time -- rather than only as an auxiliary training-time signal -- can improve long-horizon robotic manipulation is unclear; prior robotic reasoning work uses structured (not free-form) reasoning traces mostly as training supervision, and a recent finding (Chen et al.) showed reasoning at test time provides little additional benefit once a model has been trained with reasoning supervision.

## Contributions

- R3, a two-stage post-training recipe (SFT mid-training on limited expert reasoning traces, then rubric-based single-step RL on broader reasoning-free offline data) that turns an off-the-shelf VLM into a robotic reasoner steering a frozen low-level policy
- evidence that explicit inference-time reasoning causally improves generalization beyond what the same reasoning data provides as training-time-only supervision, contrasting with a prior finding in a related embodied setting
- an empirical comparison showing free-form language reasoning outperforms an Embodied-Chain-of-Thought-style structured reasoning adaptation in this long-horizon manipulation setting

## Method

A hierarchical architecture: a high-level VLM (Qwen3.5-4B) generates a free-form reasoning trace and a short-horizon instruction given the scene, goal and interaction history; a frozen low-level policy executes the instruction. R3 trains the VLM in two stages: Stage I mid-trains it with next-token prediction on a small set of expert-generated reasoning traces (from Gemini 3 Flash, with both successful and unsuccessful trajectories) to initialize useful reasoning style (decomposition, constraint tracking, self-correction); Stage II applies single-step RL (Dr.GRPO) on a broader offline dataset containing only expert instructions (no reasoning traces), rewarding the model via a VLM-as-judge (rubric-based on Language Table) or exact-match reward (grocery packing) when its generated instruction semantically matches the expert's -- avoiding expensive multi-turn robot rollouts and long-horizon credit assignment. Evaluated on 14 long-horizon block-arrangement tasks in Language Table (split into mid-training, RL, and held-out OOD tasks) and a bimanual grocery-packing suite, against instruction-only imitation learning (IL) baselines and an adaptation of Embodied Chain-of-Thought (ECoT, structured vision-grounded reasoning) to the same setting.

## Results

R3 (full: mid-training + RL) outperforms instruction-only IL across nearly all mid-training, RL, and 5 out-of-distribution held-out tasks in Language Table, with the largest gains on OOD tasks (e.g. +14.2pp on diag_line, +9.9pp on iL, +18.6pp on iV, +8.7pp on rect, +4.8pp on clear_half) -- IL yields only minor gains or degrades below the base model on OOD tasks, while R3 generalizes. RL alone (no mid-training) already improves over the base model on almost all tasks except diag_line, and mid-training further improves RL post-training and gives more structured OOD gains on tasks related to mid-training tasks. On the grocery-packing suite, R3 (RL only, no reasoning traces needed) outperforms instruction-only imitation without reasoning. Ablating the inference-time reasoning budget on a fixed R3 checkpoint (truncating reasoning to 0/50/100 tokens vs. full) shows performance increases with more reasoning budget on most tasks, and the model spends more tokens reasoning on harder, lower-success tasks (Figure 5) -- causal evidence that test-time reasoning itself, not just training-time supervision, drives the gains, in contrast to a prior finding for a related embodied setting. A VQA diagnostic suite shows R3 improves both static perception and action-oriented understanding, but this improvement alone (present even for a training-time-only reasoning variant) does not fully explain manipulation gains -- R3 still generalizes better than instruction-only imitation baselines trained with the same reasoning data via pre-training or co-training rather than test-time generation. Comparing free-form reasoning against ECoT-style structured reasoning (vision-grounded bounding boxes/object states) shows ECoT-style components slightly degrade overall performance versus R3's free-form reasoning in this setting.

## Limitations

Evaluated only in two simulated testbeds (Language Table block arrangement, bimanual grocery packing) with a single VLM backbone (Qwen3.5-4B) and a fixed low-level policy; generalization to real robots and other model scales/architectures is not demonstrated. The RL stage uses a single-step formulation to sidestep long-horizon credit assignment rather than full multi-turn RL with real environment rollouts, so gains are bounded by how well single-step reward (semantic match to an expert's next instruction) approximates eventual task success. The reward function requires either a VLM-as-judge (validated only against 100 human-labeled prompt-response pairs) or exact-match parsing (grocery packing), both of which could introduce judge-specific biases not explored beyond the reported inter-annotator agreement check.

## Why it matters here

- **overthinking**: Adjacent domain, directly relevant methodologically: this is test-time-scaling/reasoning-budget research outside the LLM-text setting (embodied robotic manipulation), and it explicitly engages the overthinking/underthinking literature -- citing 'underthinking' as a related failure mode (thought-switching) the base model exhibits before mid-training, and directly testing (via reasoning-budget truncation) whether more inference-time reasoning tokens causally improve outcomes, finding they do and that harder tasks elicit longer reasoning. Its contrarian finding versus a prior embodied-CoT result (that test-time reasoning matters causally, not just as training signal) is relevant to the broader debate this topic tracks about when reasoning length is doing real work versus wasted computation.

## Entities

- **Concepts**: free-form natural-language robotic reasoning (vs. structured CoT), mid-training for behavioral priors, rubric-based single-step RL from offline instruction data, reasoning as test-time compute for embodied control
- **Methods**: mid-training (SFT on expert reasoning traces), rubric-based single-step RL (Dr.GRPO), VLM-as-judge reward, Embodied Chain-of-Thought (ECoT, comparison baseline)
- **Datasets**: Language Table (14 designed long-horizon block-arrangement tasks), bimanual grocery packing (simulated)

Tags: `robotics`, `test-time-compute`, `reasoning`, `reinforcement-learning`, `vision-language-model`

## Abstract

Reasoning in language allows foundation models to spend more test-time compute on hard problems, such as those requiring decomposition, constraint tracking, and prediction of future consequences. Whether this mechanism can improve robotic manipulation remains unclear, where long-horizon tasks require tracking partial progress, reasoning about object relations, recovering from mistakes, and steering noisy low-level policies. In this paper, we study whether VLMs can be trained to reason directly in natural language to guide low-level manipulation policies. We introduce $R^3$, a simple post-training recipe that turns off-the-shelf VLMs into robotic reasoners: it first mid-trains a VLM on expert-generated reasoning traces to initialize the desired reasoning style, then improves the reasoner with single-step rubric-based RL from offline action data. Unlike prior robotic reasoning methods that mostly use structured traces as auxiliary supervision, $R^3$ trains free-form language reasoning to produce test-time guidance for action. We instantiate $R^3$ on Language Table and simulated bimanual grocery packing, two controlled testbeds for studying robotic reasoning and long-horizon manipulation. $R^3$ improves exploration and generalization across unseen tasks and significantly outperforms instruction-only imitation learning baselines on both benchmarks. Our analyses suggest that free-form language reasoning can function as a test-time compute mechanism for steering low-level policies. Our project page is available at https://robotic-reasoner.github.io/.

---

Record id: `arxiv:2608.26053`
