<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# CURV: Enhancing Chart Understanding Through Curriculum Visual Grounded Reasoning

- **Authors**: Xuehang Guo, Pingyue Zhang, Ruiyi Zhang, Zhenhailong Wang, Hanrui Lyu, Heng Ji, Tong Sun, Qingyun Wang, Manling Li
- **Venue**: cs.CV
- **Published**: 2026-08-03
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.02833>
- **PDF**: <https://arxiv.org/pdf/2608.02833v1>
- **Topics**: reasoning-training, test-time-scaling
- **Relevance score**: reasoning-evaluation 0.25, reasoning-training 0.40, test-time-scaling 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Chart question answering (CQA) requires multimodal large language models (MLLMs) to integrate visual comprehension with logical reasoning, yet current models struggle with accurate visual grounding and coherent reasoning chains. While extrinsic chain-of-thought prompting and visual cues significantly improve performance, current MLLMs lack intrinsic visual grounded reasoning capabilities, leading to inaccurate perception and reasoning disconnected from visual evidence. To address these limitations, we propose CURV, a curriculum learning framework that develops intrinsic visual reasoning capabilities by reformulating CQA as multi-step visual grounded reasoning, where each step coordinates logical reasoning with dynamic visual grounding through spatial attention concentration. To assist model learning, we further introduce CCQA, a three-level curriculum dataset with scalable synthetic generation across diverse chart types and reasoning patterns. Our curriculum systematically progresses from basic single-operation reasoning to complex multi-chart compositional tasks. Experiments demonstrate that CURV achieves up to $\uparrow20.50\%$ improvements over baselines and is generalizable to real-world benchmarks (up to $\uparrow12.30\%$) and out-of-domain multimodal reasoning tasks (up to $\uparrow10.20\%$), validating the effectiveness of internalizing visual reasoning with dynamic grounding for enhanced chart understanding capabilities. Code is available at: https://xhguo7.github.io/CURV/.

---

Record id: `arxiv:2608.02833`
