<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Reinforcement Learning Teachers of Test Time Scaling

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/115573>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Trains a reinforcement-learned teacher model that is given the solution and rewarded for producing explanations that help a student model understand it, outperforming distillation pipelines built from much larger models.

## Problem

Training reasoning LMs with RL for correctness alone requires the model to already have some chance of solving the task at initialization, which limits exploration; the paper targets the related but different goal of producing good teachers for distillation and RL cold-starting rather than better solvers.

## Contributions

- Introduces Reinforcement-Learned Teachers (RLTs), models trained with RL to produce explanations for a given question-and-solution pair, optimized for distilling a student model rather than for solving problems from scratch.
- Trains RLTs with dense rewards obtained by feeding each explanation to a student model and scoring the student's resulting understanding of the solution.
- Shows that raw outputs of a 7B RLT give higher final performance on competition and graduate-level tasks than existing distillation and cold-starting pipelines that use reasoning traces from much larger LMs.
- Shows RLTs remain effective when training larger students and when applied zero-shot to out-of-distribution tasks.

## Method

An RLT is prompted with both the question and its solution, and is trained via reinforcement learning to produce a detailed explanation ('connect-the-dots') rather than to solve the problem unaided. The reward is dense and comes from feeding the RLT's explanation to a student model and measuring how well the student then understands the solution, sidestepping the exploration problem of training a reasoning model with pure correctness reward from scratch. The resulting explanations are used directly for distillation into student models or for cold-starting further RL.

## Results

A 7B RLT's raw outputs give higher final performance on competition and graduate-level tasks than existing distillation and cold-starting pipelines built from reasoning traces of orders-of-magnitude larger LMs; effectiveness is maintained when training larger students and when applied zero-shot out-of-distribution. No specific numeric scores are given in the abstract.

## Limitations

The abstract does not report specific benchmark names, accuracy numbers, or the size of the larger LMs compared against; it also does not address reasoning length or inference-time compute allocation.

## Why it matters here

- **overthinking**: The paper's title places it under the 'test-time scaling' umbrella, but its actual contribution is a training-time method for producing distillation teachers via dense reward from student comprehension. It does not study reasoning length, when a model should stop or continue thinking, or the accuracy/compute tradeoff of longer reasoning chains, so the connection to this topic is nominal rather than substantive.

## Entities

- **Concepts**: distillation, cold-starting RL, dense reward from student understanding
- **Methods**: Reinforcement-Learned Teachers (RLT), reinforcement learning with dense reward, [distillation](../../../../wiki/methods/knowledge-distillation.md), cold-start for RL
- **Datasets**: competition-level tasks, graduate-level tasks

Tags: `distillation`, `reinforcement-learning`, `teacher-student`, `cold-start`

## Abstract

Abstract Training reasoning language models (LMs) with reinforcement learning (RL) for one-hot correctness inherently relies on the LM being able to explore and solve its task with some chance at initialization. Furthermore, a key use case of reasoning LMs is to act as teachers for distilling new students and cold-starting future RL iterations rather than being deployed themselves. From these considerations, we introduce a new framework that avoids RL's exploration challenge by training a new class of Reinforcement-Learned Teachers (RLTs) focused on yielding the most effective downstream distillation. RLTs are prompted with both the question and solution to each problem, and tasked to simply "connect-the-dots" with detailed explanations tailored for their students. We train RLTs with dense rewards obtained by feeding each explanation to the student and testing its understanding of the problem's solution. In practice, the raw outputs of a 7B RLT provide higher final performance on competition and graduate-level tasks than existing distillation and cold-starting pipelines that collect and postprocess the reasoning traces of orders of magnitude larger LMs. Furthermore, RLTs maintain their effectiveness when training larger students and when applied zero-shot to out-of-distribution tasks, unlocking new levels of efficiency and re-usability for the RL reasoning framework.

---

Record id: `title:21d46f88974ff7dd`
