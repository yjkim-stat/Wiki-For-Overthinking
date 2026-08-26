<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Select2Reason: Efficient Instruction-Tuning Data Selection for Long-CoT Reasoning

- **Authors**: Cehao Yang, Xueyuan Lin, Xiaojun Wu, Chengjin Xu, Xuhui Jiang, Honghao Liu, Hui Xiong, Jian Guo
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.331/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.331.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.331
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

A practical approach to activate long chain-of-thoughts reasoning ability in large language models is to perform supervised fine-tuning on instruction datasets synthesized by strong large reasoning models, offering a cost-effective alternative to reinforcement learning. However, large-scale instruction sets incur significant training overhead, while effective strategies for automatic data selection still remain unexplored. We propose Select2Reason, a novel and efficient instruction-tuning data selection framework for long-CoT reasoning. From the perspective of emergence of rethinking behaviors like self-correction and backtracking, we investigate metrics that may determine the quality of long-CoT instructions. Select2Reason leverages a difficulty-aware reward model to estimate the learning value of questions and jointly incorporates a reasoning trace length-based heuristic through a weighted scheme for ranking to prioritize high-utility examples. Empirical results on OpenR1-Math-220k demonstrate that fine-tuning LLM on only 10% of the data selected by our method achieves performance competitive with or superior to full-data tuning and open-source baseline across nine competition-level mathematical benchmarks and four broader reasoning tasks. Further experiments highlight the scalability in varying data size, efficiency during inference, and adaptability to other instruction pools of Select2Reason with minimal cost.

---

Record id: `doi:10.18653/v1/2026.findings-acl.331`
