<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Programming over Thinking: Efficient and Robust Multi-Constraint Planning

- **Authors**: Derrick Goh Xin Deik, Quanyu Long, Zhengyuan Liu, Nancy F. Chen, Wenya Wang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.2028/>
- **PDF**: <https://aclanthology.org/2026.acl-long.2028.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.2028
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Multi-constraint planning involves identifying, evaluating, and refining candidate plans while satisfying multiple, potentially conflicting constraints. Existing large language model (LLM) approaches face fundamental limitations in this domain. Pure reasoning paradigms, which rely on long natural language chains, are prone to inconsistency, error accumulation, and prohibitive cost as constraints compound. Conversely, LLMs combined with coding- or solver-based strategies lack flexibility: they often generate problem-specific code from scratch or depend on fixed solvers, failing to capture generalizable logic across diverse problems.To alleviate these issues, we introduce the Scalable Code Planning Engine (SCOPE), a systematic framework that disentangles query-specific problem reasoning from generic code execution. SCOPE first transforms input queries into optimized structured representations, capturing the interdependent constraints, and then autonomously generates reusable solver functions (Combination, Filter, and Deliver) that provide consistent and reliable execution across diverse problems. SCOPE achieves state-of-the-art performance while lowering cost and latency. For example, with GPT-4o, it reaches 93.1% success on TravelPlanner, a 61.6% gain over the best baseline (CoT) while cutting inference cost by 1.4 times and time by approximately 4.67 times. Code is available at https://github.com/DerrickGXD/SCOPE.

---

Record id: `doi:10.18653/v1/2026.acl-long.2028`
