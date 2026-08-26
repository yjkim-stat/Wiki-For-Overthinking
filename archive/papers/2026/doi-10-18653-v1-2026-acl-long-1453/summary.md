<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ReasoningGuard: Safeguarding Large Reasoning Models with Inference-time Safety Aha Moments

- **Authors**: Yuquan Wang, Mi Zhang, Yining Wang, Geng Hong, Mi Wen, Xiaoyu You, Min Yang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1453/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1453.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1453
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large Reasoning Models (LRMs) have demonstrated impressive performance in reasoning-intensive tasks, but they remain vulnerable to harmful content generation, particularly in the mid-to-late steps of their reasoning processes. Current defense methods, however, depend on costly fine-tuning and additional expert knowledge, which limits their scalability.In this work, we propose ReasoningGuard, an inference-time safeguard for LRMs.It injects timely safety aha moments during the reasoning process to guide the model towards harmless yet helpful reasoning.Our approach leverages the internal attention mechanisms of the LRM to accurately identify key points in the reasoning path, triggering safety-oriented reflections.To safeguard both the subsequent reasoning steps and the final answers, we implement a scaling sampling strategy during decoding to select the optimal reasoning path.With minimal additional inference cost, ReasoningGuard effectively mitigates four types of jailbreak attacks, including recent ones targeting the reasoning process of LRMs. Our approach outperforms nine existing safeguards, providing state-of-the-art defenses while avoiding common exaggerated safety issues.

---

Record id: `doi:10.18653/v1/2026.acl-long.1453`
