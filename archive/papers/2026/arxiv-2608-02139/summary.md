<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Self-Improving Large Language Models via Progressive Experience Evolution

- **Authors**: Shijie Ren, Xiting Wang, Meng Li, Yujie Guo, Yunhang Yao, Ziheng Peng, Xunlong Wang, Yuetan Chen, Haoyang Zhou, Yunlong Liang, Fandong Meng
- **Venue**: cs.CL
- **Published**: 2026-08-03
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.02139>
- **PDF**: <https://arxiv.org/pdf/2608.02139v2>
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.40, reasoning-faithfulness 0.25

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large language models (LLMs) capable of self-improvement require not only effective policy optimization, but also a principled mechanism for transforming transient interaction experience into persistent model capabilities. Existing self-improvement paradigms remain fragmented: test-time methods can explicitly extract experience but cannot internalize it into model parameters, whereas training-time optimization methods can update model parameters but lack an explicit mechanism for accumulating transferable experience. Bridging these two paradigms requires a critical intermediate stage that remains underexplored, namely \emph{experience distillation}. To address this gap, we propose \textbf{SPEE} (\textbf{S}elf-\textbf{P}rogressive \textbf{E}xperience \textbf{E}volution), a unified post-training framework that sequentially performs explicit experience evolution followed by implicit policy optimization. During explicit experience evolution, SPEE reflects on trajectories collected from multiple interactions to extract, verify, and progressively evolve transferable experience, which is subsequently internalized into the policy through privilege-guided On-Policy Self-Distillation (OPSD). During implicit policy optimization, reward-driven reinforcement learning leverages these internalized priors to explore novel solution strategies. In the experience evolution stage, a continuously evolving global experience pool consolidates knowledge from both successful and failed trajectories, filters out low-utility experience, and mitigates post-hoc rationalization induced by individual trajectories. Experiments on five mathematical reasoning benchmarks demonstrate that SPEE consistently outperforms both test-time and training-time self-evolution baselines across three model scales. The source code is available at https://github.com/rrrsj/SPEE.

---

Record id: `arxiv:2608.02139`
