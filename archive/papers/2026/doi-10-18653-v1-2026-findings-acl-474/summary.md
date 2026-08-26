<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Prompting Test-Time Scaling Is A Strong LLM Reasoning Data Augmentation

- **Authors**: Sondos Mahmoud Bsharat, Zhiqiang Shen
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.474/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.474.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.474
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large language models (LLMs) exhibit strong reasoning when guided by chain-of-thought exemplars, yet collecting large, high-quality reasoning datasets remains laborious and resource-intensive. We introduce Prompting Test-Time Scaling (P-TTS), a prompt-space data augmentation framework for enhancing LLM reasoning via fine-tuning. In P-TTS, scaling refers to systematic expansion of the prompt space during offline teacher-data generation, not to increased inference-time compute for the deployed student. Rather than collecting thousands of examples, P-TTS starts from a small pool of 90 manually selected reasoning instances and applies principled instruction templates and paraphrased prompt variants to elicit diverse reasoning trajectories from a teacher model, producing a compact synthetic training set. We fine-tune Qwen-2.5 models of multiple sizes on the resulting data. On reasoning benchmarks including AIME25, MATH500, and GPQA-Diamond, P-TTS consistently improves accuracy over competitive small-data baselines such as S1 and S1.1 (1K-shot), with the largest gains on AIME25 while remaining strong on MATH500 and GPQA-Diamond. P-TTS also improves generalization on out-of-domain reasoning evaluations. Ablations show that exemplar diversity and prompt-space scaling are critical drivers of improvement, suggesting that prompt scaling explores the latent space of reasoning patterns, amplifying LLM problem-solving with minimal annotation overhead. P-TTS offers a practical, low-cost way to elicit strong LLM reasoning in resource-constrained or rapidly evolving domains. Our code and data are available at https://github.com/VILA-Lab/PTTS.

---

Record id: `doi:10.18653/v1/2026.findings-acl.474`
