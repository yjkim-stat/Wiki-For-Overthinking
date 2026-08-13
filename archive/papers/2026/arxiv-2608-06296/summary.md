<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# On-Policy Self-Distillation without Any Supervision

- **Authors**: Yijiang Li, Bingyang Wang, Yijun Liang, Yunjie Tian, Di Fu, Nuno Vasconcelos
- **Venue**: cs.LG
- **Published**: 2026-08-06
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.06296>
- **PDF**: <https://arxiv.org/pdf/2608.06296v2>
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.40, reasoning-training 0.25, test-time-scaling 0.25

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

On-policy (Self-)Distillation (OPD / OPSD) has shown strong potential for post-training large language models (LLMs). However, existing methods still rely heavily on external supervision, including ground-truth signals, environmental feedback, or guidance from larger models, and therefore fall short of genuine "self"-distillation. In this study, we show that on-policy self-distillation can be achieved using only a model's own generations via internal consistency. We propose unsupervised on-policy self-distillation (U-OPSD). U-OPSD first samples multiple rollouts and constructs a pseudo solution by majority vote under a self-consistency threshold. It then conditions the model's distribution on the pseudo-solution and distills itself on the disagreeing completions, allowing the model to correct itself precisely where it is confidently wrong. Across diverse benchmarks, base models, and training settings, U-OPSD consistently improves over the base models and matches or surpasses supervised methods with ground truth (GT) such as OPSD and GRPO. On five mathematical reasoning benchmarks, i.e., AIME24, AIME25, HMMT25, MATH500, and AMC23, U-OPSD improves over the base model by 8.5% and 10.7% on Qwen3 non-thinking mode at 4B and 8B scales, and outperforms OPSD by 3.2% and 2.3% on average, respectively. In thinking mode, U-OPSD stays on par with OPSD, ahead by 0.9% at 4B and level at 8B and surpassing GRPO by 0.7% and 1.1%, respectively. Code is available at [https://github.com/williamium3000/u-opsd](https://github.com/williamium3000/u-opsd).

---

Record id: `arxiv:2608.06296`
