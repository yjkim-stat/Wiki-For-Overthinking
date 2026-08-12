<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Perception Before Reasoning: Dynamic Latent Reasoning for Video Understanding and Question Answering

- **Authors**: Haotian Xia, Zilin Xiao, Junbo Zou, Vicente Ordonez, Hanjie Chen
- **Venue**: cs.CV
- **Published**: 2026-08-04
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.04124>
- **PDF**: <https://arxiv.org/pdf/2608.04124v1>
- **Topics**: reasoning-faithfulness
- **Relevance score**: reasoning-faithfulness 0.50, reasoning-training 0.25, test-time-scaling 0.25

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Video question answering requires models to ground language queries in visual evidence and, when necessary, reason over that evidence across time. Existing methods typically rely on long textual chain-of-thought rationales, even though many questions can be answered as soon as the relevant object, action, or frame is localized. We propose Dynamic Latent Reasoning (DyLaR), which first grounds a question in a short block of perception latents (continuous hidden states that encode query-relevant visual evidence), and then adaptively decides whether to append reasoning latents (continuous thoughts that reason over this evidence in latent space) before answering. DyLaR learns this behavior by grounding perception latents in verified visual evidence and distilling verified rationales into reasoning latents, followed by reinforcement learning that further refines when to reason. Across nine video benchmarks and four multimodal language model backbones, DyLaR improves average accuracy over same-backbone baselines while generating fewer than 20 tokens per query. On Qwen3-VL-4B, for example, DyLaR improves average accuracy over Qwen3-VL-4B-Thinking from 54.0 to 58.2 while reducing response length from 1,220.7 to 18.5 tokens per query. Ablations further show that grounded perception latents, rationale-supervised reasoning latents, and adaptive routing each improve accuracy.

---

Record id: `arxiv:2608.04124`
