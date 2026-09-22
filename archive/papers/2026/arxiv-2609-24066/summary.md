<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Efficient Reasoning Exploration via State-Conditioned Latent Steering with Progress Guidance

- **Authors**: Hengyuan Zhang, Chenming Shang, Zunhai Su, Xiao Liang, Hui Shen, Jing Xiong, Dawei Li, Shiping Yang, Kailai Yang, Wei Zhang, Ruobing Xie, Hayden Kwok-Hay So, Ngai Wong
- **Venue**: cs.CL
- **Published**: 2026-09-21
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2609.24066>
- **PDF**: <https://arxiv.org/pdf/2609.24066v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.70

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Best-of-$N$ is a widely used inference strategy for complex reasoning, whose effectiveness depends on whether sampled candidates can cover diverse and high-quality reasoning paths. However, post-trained reasoning models often suffer from \emph{exploration collapse}, where independent rollouts repeatedly follow similar reasoning paths and limit the gains from increasing the rollout budget. Existing methods alleviate this issue by promoting broader exploration, but do not explicitly guide exploration toward continuations that make meaningful progress, resulting in limited exploration efficiency. To address this, we propose \emph{\underline{S}tate-conditioned \underline{P}rogress-guided \underline{S}teering} (SPS), a training-free latent steering framework. Specifically, SPS constructs a state-conditioned Direction Bank containing multiple progress-guided steering vectors for different prefix-state regions. During online inference, SPS retrieves a suitable steering vector based on the current prefix state and applies it at high-uncertainty transitions to guide the next reasoning step toward meaningful progress. Extensive experiments across multiple model scales and benchmarks demonstrate that SPS consistently outperforms strong baselines. Further analyses validate the effectiveness of its key designs and offer valuable insights for future research. The code is available at https://github.com/rattlesnakey/SPS.

---

Record id: `arxiv:2609.24066`
