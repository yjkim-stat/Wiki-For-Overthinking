<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# A Few Bad Apples Spoil the Bunch: Preventing Global Entropy Collapse Driven by a Small Set of Tokens in LLM Reasoning

- **Authors**: Jaeeun Jang, Hansle Lee, Sangmin Kim
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.641/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.641.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.641
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Reinforcement Learning with Verifiable Rewards (RLVR) and Reinforcement Learning from Internal Feedback (RLIF) often fail to benefit from test-time compute due to entropy collapse and the resulting loss of reasoning diversity. We show that this collapse is driven not by uniform entropy decay, but by premature overconfidence at a small number of structurally critical decision points. Based on a token-level analysis of GRPO-style policy optimization, we propose SCOPE (Structural Collapse-aware Optimization via Partial Entropy control), which assigns each generated token a redistribution score and applies selective KL regularization to only the top ∼ 5% of tokens under this score. Across model scales and architectures on math reasoning benchmarks, SCOPE consistently improves performance under both RLVR and RLIF settings, demonstrating that targeted entropy control at a vanishingly small subset of tokens is sufficient to sustain reasoning diversity and effective test-time scaling.

---

Record id: `doi:10.18653/v1/2026.findings-acl.641`
