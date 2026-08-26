<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ERRV: Eliciting Efficient Reasoning through Reasoning Vectors for Policy Optimization in Large Language Models

- **Authors**: Zhuowen Han, Lei Yang, Renren Jin, Dan Shi, Chenxi Sun, Deyi Xiong
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1425/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1425.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1425
- **Topics**: overthinking
- **Relevance score**: overthinking 0.62

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Recently, large reasoning models have achieved impressive performance, but their lengthy reasoning processes incur substantial inference overhead. To mitigate this issue, we propose the concept of reasoning vectors, representations extracted from the model’s hidden states, which can guide the model towards generating more concise and accurate responses. Building upon this, we present ERRV, a training framework that elicits efficient reasoning through reasoning vectors, which enables the model to generate high-quality responses during reinforcement learning. By performing targeted policy optimization on both accuracy and length objectives, ERRV effectively activates the model’s latent capability for efficient reasoning. Our experiments demonstrate that after training with ERRV, the model achieves approximately 30% reduction in reasoning length while maintaining stable accuracy, without guidance from the reasoning vector during inference. This establishes a trade-off between efficiency and performance. Furthermore, we identify key properties of reasoning vectors: robustness, characterized by high similarity before and after training, and generalizability, demonstrating applicability across base models, distilled models, RL-trained models, parameter-merged models, and mixed-thought models. These properties collectively guarantee the reliability and broad applicability of our approach.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1425`
