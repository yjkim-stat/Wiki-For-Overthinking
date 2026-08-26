<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Answering Complex Geographic Questions by Adaptive Reasoning with Visual Context and External Commonsense Knowledge

- **Authors**: Fan Li, Jianxing Yu, Jielong Tang, Wenqing Chen, Hanjiang Lai, Yanghui Rao, Jian Yin
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2025.acl-long.1239/>
- **PDF**: <https://aclanthology.org/2025.acl-long.1239.pdf>
- **DOI**: 10.18653/v1/2025.acl-long.1239
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

This paper focuses on a new task of answering geographic reasoning questions based on the given image (called GeoVQA). Unlike traditional VQA tasks, GeoVQA asks for details about the image-related culture, landscape, etc. This requires not only the identification of the objects in the image, their properties and relations, but also the understanding of the geographic knowledge of the objects, such as location, transportation, landmark, cuisine, etc. This background knowledge does not explicitly appear in the image, nor is there an extra-textual description. Without this missing but necessary knowledge, it is difficult for existing matching-based methods to infer the correct answer. To tackle these challenges, we propose a new geographic reasoning framework for our task. We first analyze the image and describe its fine-grained content by text and keywords using a multi-modal retrieval augmented technique, so as to deduce an answer in a unified textual modality. Next, we retrieve the crucial geographic commonsense knowledge. To reduce the retrieval complexity, we design a dynamic method that can adaptively collect the relevant clues for each reasoning step. The step in the incorrect direction will be pruned according to some judgment criteria. The remaining steps can help us form a reasoning chain to derive a correct answer. Moreover, we create a large-scale dataset GVQA with 41,329 samples to conduct the evaluation. The results demonstrate the effectiveness of our approach.

---

Record id: `doi:10.18653/v1/2025.acl-long.1239`
