<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Concise Math Reasoning via Difficulty-Aware Distillation

- **Authors**: Yifan Wu, Jingze Shi, Bingheng Wu, Jiayi Zhang, Xiaotian Lin, Yizhang Zhu, Zhaoyang Yu, Bang Liu, Chenglin Wu, Nan Tang, Yuyu Luo
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.2155/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.2155.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.2155
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Human experts tackle difficult math problems by identifying and executing a few pivotal steps rather than listing every intermediate thought. In contrast, standard Chain-of-Thought (CoT) distillation trains small models on lengthy reasoning traces, encouraging a uniform overthinking style across easy and hard items alike. The result is rigid, slow solutions that sacrifice adaptivity. This approach stands in sharp contrast to human intuition. Humans naturally adapt their problem-solving strategy, dedicating significant effort to difficult problems while finding quick, simple solutions for easier ones. We argue that the root cause lies in the training data: it contains excess information and reasoning steps organized in ways misaligned with human practice. We address this with Difficulty-Aware Distillation(DAD), a procedure for producing training data that mirrors concise human reasoning. A large teacher model first assesses a problem’s difficulty and then rewrites the solution to retain only the essential steps. Using this process, we constructed LiteCoT, a 100,000-example corpus of short, clear rationales, and used it to train our Liter models. With 100k LiteCoT, we outperform models trained on 800k long CoT and cut both training and inference costs. The advantage is consistent across standard math benchmarks, showing that concise, human-aligned data delivers equal or better accuracy with much less compute. For example, on the challenging AIME24 exam, our approach reaches 74.2% Pass@1 using only about 5K inference tokens, surpassing other methods that consume many more tokens.

---

Record id: `doi:10.18653/v1/2026.findings-acl.2155`
