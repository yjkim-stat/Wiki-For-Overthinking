<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# When Correct Solutions Repeat: Rarity-Aware Credit Redistribution for GRPO

- **Authors**: Zhe Cao, Miaowen Wen, Fangjiong Chen
- **Venue**: cs.AI
- **Published**: 2026-08-04
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.03467>
- **PDF**: <https://arxiv.org/pdf/2608.03467v2>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-evaluation 0.25, reasoning-training 0.62

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Reinforcement learning with verifiable rewards (RLVR) com- monly optimizes each correct completion as an independent learning signal. In GRPO, this completion-level uniformity creates structure-level skew: recurring correct solution forms accumulate positive coefficient mass in proportion to how often they are sampled, while rare forms receive limited credit. We formalize this behavior as multiplicity-induced structure-level credit concentration and introduce a partition- conditioned rule that redistributes positive advantages accord- ing to cluster rarity. Cue-GRPO instantiates this rule with- out auxiliary-model inference by using deterministic Strategy Cues to construct rollout-local partitions of verified-correct traces. Across Qwen2.5-Math-7B and Llama-3.1-8B-Instruct, Cue-GRPO improves AIME repeated-sampling performance, with the largest gains at high sampling budgets. Credit Re- distribution (CR) under Judge Partitions (JP) further indi- cates that the proposed redistribution mechanism can oper- ate with judge-derived partitions. Cue-GRPO adds only 6% wall-clock training overhead over GRPO. These results sup- port structure-level credit redistribution as a practical design axis for RLVR, with Strategy Cues providing a low-overhead implementation for competition mathematics. Code is avail- able at https://github.com/CzZ12/When-Correct-Solutions- Repeat-Rarity-Aware-Credit-Redistribution-for-GRPO.

---

Record id: `arxiv:2608.03467`
