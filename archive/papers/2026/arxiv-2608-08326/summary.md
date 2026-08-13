<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# StructReward: Efficient Structured Process Rewards for Self-Correcting Multimodal Reasoning

- **Authors**: Yifan Li, Ruxin Sun, Tongzhou Zhao
- **Venue**: cs.AI
- **Published**: 2026-08-08
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.08326>
- **PDF**: <https://arxiv.org/pdf/2608.08326v2>
- **Topics**: reasoning-training, test-time-scaling
- **Relevance score**: reasoning-training 0.67, test-time-scaling 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Reinforcement learning with verifiable rewards (RLVR) has emerged as an effective approach for improving multimodal reasoning. However, most existing methods evaluate an entire response using a binary reward based only on final-answer correctness, thereby discarding the supervision available in intermediate reasoning steps. Process reward models offer finer-grained feedback, but they typically rely on separately trained verifiers, costly chain-of-thought annotations, or online judging by large language models (LLMs). In this work, we introduce StructReward, a compute-efficient framework that provides dense reinforcement signals through structured step-level reward alignment. StructReward represents each generated solution as a sequence of reasoning steps and aligns them with process-labeled reference steps using lightweight numerical, symbolic, and lexical matching rules. The aligned labels are aggregated into a dense process reward and combined with final-answer consistency and output-validity rewards through a gated Group Relative Policy Optimization (GRPO) objective. We further recycle policy rollouts into complementary supervision for response comparison and reflective self-correction, rather than discarding them after policy updates. Separately, we use a strong LLM to rewrite sampled correct trajectories into reflection-oriented training instances, further strengthening the policy's ability to evaluate and refine its reasoning. Since reward computation is performed online without an additional learned verifier or external LLM judge, StructReward substantially reduces the computational overhead of multimodal reinforcement learning. Experimental results show that structured process supervision and rollout recycling provide an efficient path toward self-improving multimodal reasoning.

---

Record id: `arxiv:2608.08326`
