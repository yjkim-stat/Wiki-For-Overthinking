<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Towards a Mechanistic Understanding of Large Reasoning Models: A Survey of Training, Inference, and Failures

- **Authors**: Yi Hu, Jiaqi Gu, Ruxin Wang, Zijun Yao, Hao Peng, Xiaobao Wu, Jianhui Chen, Muhan Zhang, Liangming Pan
- **Venue**: preprint
- **Published**: 2026-01-01
- **Source**: local+anthology
- **Link**: <https://aclanthology.org/2026.acl-long.889/>
- **PDF**: <https://aclanthology.org/2026.acl-long.889.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.889
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

A survey that organizes existing mechanistic-interpretability research on large reasoning models into three areas -- reasoning-oriented training dynamics, reasoning mechanisms, and unintended behaviors (hallucination, CoT unfaithfulness, overthinking, unsafety) -- and proposes directions for future mechanistic work.

## Problem

LRMs trained with RL show strong reasoning performance but remain largely black boxes: it is unclear how RL's role differs from SFT's, what internal structures underlie reasoning traces, and what mechanistically causes unintended behaviors such as hallucination, unfaithful chain-of-thought, overthinking, and unsafe outputs. The paper argues no prior survey focuses specifically on the mechanistic (rather than purely behavioral) understanding of LRMs.

## Contributions

- First survey to focus specifically on the mechanistic (rather than general behavioral) understanding of large reasoning models
- A three-part taxonomy organizing mechanistic LRM research into training dynamics, reasoning mechanisms, and unintended behaviors
- A dedicated synthesis of overthinking as one of four unintended-behavior categories, covering its length-performance curve, stage-wise failure patterns, and proposed internal mechanisms
- A roadmap of future directions: applied interpretability, improved interpretability methodology at LRM scale, and a unified theoretical framework for reasoning
- A maintained companion resource ('Awesome-LRM-Mechanisms' project) linked from the paper

## Method

This is a literature survey, not an empirical study: it synthesizes findings from other papers into a taxonomy (Fig. 1/2) with three top-level sections. Sec 2 (Understanding LRM Training) covers the respective roles of SFT and RL in post-training and the internal dynamics of RL training (entropy collapse, activation/weight changes, the 'aha moment'). Sec 3 (Understanding LRM Reasoning) covers general structural properties of reasoning traces (macro-level lifecycle, sentence-level operational units, topological/graph structure), specific behaviors (thought anchors, self-reflection, backtracking, complexity-adaptive reasoning), and internal mechanisms (sparse autoencoders, steering vectors, linear probes revealing interpretable/steerable directions for these behaviors). Sec 4 (Understanding LRM Failures) covers hallucination, CoT unfaithfulness, overthinking, and unsafety, each with behavioral patterns and proposed internal mechanisms drawn from cited work. Sec 5 and Appendix B propose future directions (applied interpretability, improved methodology, unified theory).

## Results

No first-party experiments or benchmark numbers; the paper's 'results' are synthesized claims from the surveyed literature. On overthinking specifically (Sec 4.3, the section most relevant to this topic): the length-performance relationship is repeatedly reported as inverted-U-shaped -- accuracy rises with reasoning length up to a point, then declines as chains grow excessively long (citing Marjanovic et al. 2025, Su et al. 2025a, Ghosal et al. 2025, Yang et al. 2025b, Gema et al. 2025). Incorrect answers tend to correspond to longer reasoning chains than correct ones. Models are reported to allocate disproportionately long chains to simple problems while reasoning insufficiently through complex ones -- a misalignment between reasoning effort and problem difficulty. Overthinking is decomposed into failures at three stages of a hypothesis-generation / expansion / verification loop: excessive unexplored candidate generation, redundant step-by-step expansion on trivial problems (up to 'tens or even hundreds of times longer outputs than non-reasoning models with marginal performance gain', citing Chen et al. 2024), and non-terminating verification where models fail to recognize a correct answer has been reached. Proposed mechanistic causes include steerable overthinking-associated directions in activation space (Huang et al. 2025b; Baek and Tegmark 2025) and conflict between a model's fast intuitive answer and its subsequent deliberate reasoning (Dang et al. 2025).

## Limitations

Stated by the authors: the field moves fast enough that the survey may not capture the most recent advances; the survey focuses only on language-only models and does not address multimodal reasoning models; and it is limited to traditional LLM (transformer, discrete-token, autoregressive) architectures, excluding diffusion-based LLMs, continuous-token transformers, and looped transformers. As a survey, it also draws all of its evidence second-hand from cited studies rather than running independent experiments, so its overthinking claims (e.g., the inverted-U curve) inherit whatever limitations those individual studies have.

## Why it matters here

- **overthinking**: Section 4.3 of the survey is dedicated entirely to overthinking: it synthesizes evidence for an inverted U-shaped accuracy-vs-reasoning-length curve, characterizes overthinking as control/termination failures across a hypothesis-generation/expansion/verification loop, and reviews proposed internal mechanisms (steerable activation-space directions, conflict between fast and deliberate answers). This is a direct, if secondary-source, treatment of the accuracy/efficiency tradeoff of reasoning length that the topic tracks.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), inverted U-shaped length-performance curve, hallucination in reasoning models, chain-of-thought unfaithfulness, [reward hacking](../../../../wiki/concepts/reward-hacking.md), entropy collapse in RL training, thought anchors, [aha moment](../../../../wiki/concepts/aha-moment.md), SFT explores / RL compresses, mechanistic interpretability of LRMs
- **Methods**: sparse autoencoders (SAEs), steering vectors, [linear probing](../../../../wiki/methods/linear-probe.md), activation/circuit analysis, SVD analysis of weight matrices, causal intervention on chain-of-thought
- **Datasets**: _none recorded_

Tags: `survey`, `mechanistic-interpretability`, `large-reasoning-models`, `overthinking`, `chain-of-thought`, `reinforcement-learning`, `hallucination`, `unfaithfulness`

## Abstract

Reinforcement learning (RL) has catalyzed the emergence of Large Reasoning Models (LRMs) that have pushed reasoning capabilities to new heights. While their performance has garnered significant excitement, exploring the internal mechanisms driving these behaviors has become an equally critical research frontier. This paper provides a comprehensive survey of the mechanistic understanding of LRMs, organizing recent findings into three core dimensions: 1) training dynamics, 2) reasoning mechanisms, and 3) unintended behaviors. By synthesizing these insights, we aim to bridge the gap between black-box performance and mechanistic transparency. Finally, we discuss under-explored challenges to outline a roadmap for future mechanistic studies, including the need for applied interpretability, improved methodologies, and a unified theoretical framework.

---

Record id: `local:34cecfd6f28ba72b`
