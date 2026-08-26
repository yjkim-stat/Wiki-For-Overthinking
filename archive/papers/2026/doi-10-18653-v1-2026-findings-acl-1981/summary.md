<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Beyond ’Aha!’: Toward Systematic Meta-Abilities Alignment in Large Reasoning Models

- **Authors**: Zhiyuan Hu, Yibo Wang, Hanze Dong, Yuhui Xu, Amrita Saha, Caiming Xiong, Bryan Hooi, Junnan Li
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1981/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1981.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1981
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large reasoning models (LRMs) already possess a latent capacity for long chain-of-thought reasoning. Prior work has shown that outcome-based reinforcement learning (RL) can incidentally elicit advanced reasoning behaviors such as self-correction, backtracking, and verification–phenomena often referred to as the model’s ”aha moment”. However, the timing and consistency of these emergent behaviors remain unpredictable and uncontrollable, limiting the scalability and reliability of LRMs’ reasoning capabilities. To address these limitations, we move beyond reliance on prompts and unpredictable ”aha moments”. Instead, we explicitly align models with three meta-abilities: deduction, induction, and abduction, using automatically generated, self-verifiable tasks. Our three-stage pipeline (individual alignment, parameter-space merging, domain-specific reinforcement learning) boosts performance by over 10% relative to instruction-tuned baselines. Furthermore, domain-specific RL from the aligned checkpoint yields an additional gain in performance ceiling for both 7B and 32B models across math, coding, and science benchmarks, showing that explicit meta-ability alignment offers a scalable and dependable foundation for reasoning. Code and data can be found in Software and Data part in submission page.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1981`
