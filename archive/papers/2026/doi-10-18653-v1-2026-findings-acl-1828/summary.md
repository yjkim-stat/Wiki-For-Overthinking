<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Activation Steering for Chain-of-Thought Compression

- **Authors**: Seyedarmin Azizi, Erfan Baghaei Potraghloo, Souvik Kundu, Massoud Pedram
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1828/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1828.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1828
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large language models (LLMs) demonstrate strong performance on multi-step reasoning tasks by producing intermediate explanations, commonly referred to as chains of thought (CoTs). However, the generated rationales are typically verbose, consuming many additional tokens, and thus degrading throughput and increasing inference energy consumption. Interestingly, we find that verbose and concise CoTs correspond to distinct regions in the model’s intermediate activation space, suggesting that verbosity is a steerable latent attribute. Building on this observation, we develop an inference-time method to automatically steer the model response towards concise reasoning traces without updating model parameters. Our method, dubbed ASC (Activation-Steered Compression), generates concise CoTs by directly adjusting internal representations via activation steering. A key component of ASC is Contrastive Energy-Based Steering (CES), a principled procedure to learn a single steering vector from a small set of verbose–concise CoT pairs by optimizing a length-normalized contrastive energy objective. To further ensure reliable steering and preserve general utility, CES enforces a differentiable KL trust region during steering vector optimization, explicitly constraining the distribution shift within a specified budget. With only 100 pairs of verbose–concise examples, ASC reduces the generated token length by as much as 69.4% across five reasoning benchmarks (MATH500, GSM8K, LiveCodeBench, GSM8K-Hard, and AQuA-RAT) while maintaining accuracy across models with 1.5B, 7B, 8B, and 32B parameters. On MATH500, ASC achieves an end-to-end inference speed-up of 2.7× on an 8B model.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1828`
