<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# AdaReasoner: Adaptive Reasoning Enables More Flexible Thinking

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/117660>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

AdaReasoner is an RL-trained, model-agnostic plugin that picks a per-task reasoning configuration - prompt instruction format, decoding temperature and number of reasoning steps - instead of using one fixed prompting setup for every task.

## Problem

Prompting approaches fix their configuration in advance: one instruction template, one temperature, one reasoning depth, chosen to work acceptably across tasks. Different kinds of thinking want different settings - joke generation and mathematical reasoning are the paper's two poles - so a fixed configuration is rarely optimal for any single task, and searching the configuration space per task by hand does not scale.

## Contributions

- AdaReasoner, an LLM-agnostic plugin that selects reasoning configuration per task rather than fixing it globally
- A factorized action space over instruction format, temperature and reasoning-step count, with a targeted exploration strategy for RL training
- A pretrained reward model allowing the policy to be adapted to a new task from a few-shot guide
- Theoretical results on fast convergence and a sublinear policy gap
- Consistent accuracy gains over CoT, Auto-CoT, in-context CoT and Best-of-N across six LLMs, with OOD robustness preserved

## Method

A small policy model chooses a configuration for each task from a factorized action space of three hyperparameters: the reasoning instruction format, the generation temperature, and the number of reasoning steps. Factorizing the space keeps it from growing multiplicatively. The policy is trained by reinforcement learning with a targeted exploration strategy and a pretrained reward model that scores the base LLM's output under a chosen configuration, requiring only a few-shot guide per task. The base LLM is untouched, so the same plugin drives any model. The paper gives convergence guarantees and a sublinear bound on the policy gap.

## Results

Averaged accuracy across the evaluated tasks: with GPT-4o, AdaReasoner 80.42% against in-context CoT 74.42%, Auto-CoT 72.32% and CoT 68.71%; with Llama-3.3-70B-Instruct, 80.74% against Best-of-N 73.92% and CoT 71.56%; with DeepSeek-R1, 86.28% against Auto-CoT 80.47% and CoT 78.91%. Six LLMs in total (GPT-4o, Llama-3.3-70B-Instruct, Qwen-2.5-72B-Instruct, Claude-3.5-Sonnet, DeepSeek-R1, o3-mini). In-distribution tasks are MMLU (Math), Metaphor, TruthfulQA and LogiQA; OOD robustness is checked on BRIGHTER, StepGame and CRoW; knowledge-intensive gains on GPQA, MMLU-Chem and MedExQA.

## Limitations

The authors state that AdaReasoner needs per-task few-shot fine-tuning and adds computational overhead for the RL optimization, and that the manually defined discrete action space may limit expressiveness. A reader should add that no inference cost is reported anywhere: token counts, response lengths and latency are not measured, so the accuracy gains over CoT come with no accounting of what they cost. Since one of the three tuned knobs is the number of reasoning steps, a configuration that wins by simply reasoning for longer would be indistinguishable from one that reasons better, and the paper provides no evidence to separate them.

## Why it matters here

- **overthinking**: Adjacent rather than central, but it belongs in the topic because the number of reasoning steps is one of the three variables it learns per task - so it is an instance of deciding how much to think, arrived at from the prompting side rather than from training the model to stop. What it adds to the topic is the framing that reasoning depth is one axis among several: temperature and instruction format are tuned jointly with it, which suggests that the right amount of thinking is not separable from how the thinking is elicited. What it cannot supply is the tradeoff itself. The paper reports accuracy only and measures no token count, length or latency, so it does not establish whether AdaReasoner's gains come from thinking more appropriately or simply from thinking more - and on this topic those are the two answers that need telling apart. Use it as evidence that per-task depth selection helps accuracy, not as evidence about efficiency.

## Entities

- **Concepts**: [Adaptive Reasoning](../../../../wiki/concepts/adaptive-reasoning.md), Reasoning Configuration Search, Factorized Action Space, Reward-Model-Guided Prompting, Test-Time Configuration Adaptation
- **Methods**: AdaReasoner, factorized action space, reinforcement learning policy optimization, pretrained reward model, [Chain-of-Thought (baseline)](../../../../wiki/methods/chain-of-thought-baseline.md), Auto-CoT (baseline), in-context CoT (baseline), [Best-of-N (baseline)](../../../../wiki/methods/best-of-n-baseline.md)
- **Datasets**: MMLU (Math), Metaphor, [TruthfulQA](../../../../wiki/datasets/truthfulqa.md), [LogiQA](../../../../wiki/datasets/logiqa.md), BRIGHTER, StepGame, CRoW, [GPQA](../../../../wiki/datasets/gpqa.md), MMLU-Chem, MedExQA

Tags: `adaptive-reasoning`, `prompt-configuration`, `reinforcement-learning`, `reasoning-steps`, `temperature`, `llm-agnostic-plugin`

## Abstract

Abstract LLMs often need effective configurations, like temperature and reasoning steps, to handle tasks requiring sophisticated reasoning and problem-solving, ranging from joke generation to mathematical reasoning. Existing prompting approaches usually adopt general-purpose, fixed configurations that work “well enough” across tasks but seldom achieve task-specific optimality. To address this gap, we introduce AdaReasoner, an LLM-agnostic plugin designed for any LLM to automate adaptive reasoning configurations for tasks requiring different types of thinking. AdaReasoner is trained using a reinforcement learning (RL) framework, combining a factorized action space with a targeted exploration strategy, along with a pretrained reward model to optimize the policy model for reasoning configurations with only a few-shot guide. AdaReasoner is backed by theoretical guarantees and experiments of fast convergence and a sublinear policy gap. Across six different LLMs and a variety of reasoning tasks, it consistently outperforms standard baselines, preserves out-of-distribution robustness, and yield gains on knowledge-intensive tasks through tailored prompts.

---

Record id: `title:b12c09d1a21e70d0`
