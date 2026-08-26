<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Tandem: Riding Together with Large and Small Language Models for Efficient Reasoning

- **Authors**: Zichuan Fu, Xian Wu, Guojing Li, Yejing Wang, Yijun Chen, Zhao Zihao, Luo Yixuan, Hanyu Yan, Yefeng Zheng, Xiangyu Zhao
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.2098/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.2098.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.2098
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Recent advancements in large language models (LLMs) have catalyzed the rise of reasoningintensive inference paradigms, where models perform explicit step-by-step reasoning before generating final answers. While such approaches improve answer quality and interpretability, they incur substantial computational overhead due to the prolonged generation sequences. In this paper, we propose Tandem, a novel collaborative framework that synergizes large and small language models (LLMs and SLMs) to achieve high-quality reasoning with significantly reduced computational cost. Specifically, the LLM serves as a strategic coordinator, efficiently generating a compact set of critical reasoning insights. These insights are then used to guide a smaller, more efficient SLM in executing the full reasoning process and delivering the final response. To balance efficiency and reliability, Tandem introduces a cost-aware termination mechanism that adaptively determines when sufficient reasoning guidance has been accumulated, enabling early stopping of the LLM’s generation. Experiments on mathematical reasoning and code generation benchmarks demonstrate that Tandem reduces computational costs by approximately 40% compared to standalone LLM reasoning, while achieving superior or competitive performance. Furthermore, the sufficiency classifier trained on one domain transfers effectively to others without retraining. The code is available at: https://github.com/Applied-MachineLearning-Lab/ACL2026_Tandem.

---

Record id: `doi:10.18653/v1/2026.findings-acl.2098`
