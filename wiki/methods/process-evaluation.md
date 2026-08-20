# process evaluation

<!-- auto:begin -->

Scoring the reasoning that led to an answer rather than only the answer, which six sources treat as necessary and which they show is limited by the cost of reference reasoning. Two obtain that reference for free from execution — parameterized symbolic templates with executable Python, which also regenerate contamination-free instances — while three pay for it with expert annotation and one of those can afford it for only 46% of its items. One scores the intermediate artefact and the reasoning from it in separate layers. One shows the evaluator itself improves monotonically with reasoning tokens spent. The recurring finding across them is that answers are frequently right while the reasoning is not, so answer-only scoring overstates competence.

- **Kind**: method
- **Also called**: process scoring, reasoning process evaluation, step-level evaluation
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 7

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [benchmark contamination](../concepts/benchmark-contamination.md), [best-of-n](best-of-n.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [compute allocation](../concepts/compute-allocation.md), [construct validity](../concepts/construct-validity.md), [DAPO](dapo.md), [DAPO-Qwen-32B](../models/dapo-qwen-32b.md), [DeepSeek-R1-0528-Qwen3-8B](../models/deepseek-r1-0528-qwen3-8b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [error detection](../concepts/error-detection.md), [FinQA](../datasets/finqa.md), [GPT-4o](../models/gpt-4o.md), [GRPO](grpo.md), [hallucination](../concepts/hallucination.md), [judge reliability](../concepts/judge-reliability.md), [LiveCodeBench](../datasets/livecodebench.md), [LLM-as-a-judge](llm-as-a-judge.md), [MATH500](../datasets/math500.md), [meta-evaluation](../concepts/meta-evaluation.md), [Minerva](../datasets/minerva.md), [multimodal reasoning](../concepts/multimodal-reasoning.md), [pass@k](../concepts/pass-k.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [reasoning boundary](../concepts/reasoning-boundary.md), [reranking](reranking.md), [RLVR](rlvr.md), [self-correction](../concepts/self-correction.md), [supervised fine-tuning](supervised-fine-tuning.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](../concepts/test-time-scaling.md), [traceability](../concepts/traceability.md), [training dynamics](../concepts/training-dynamics.md), [verification](../concepts/verification.md)

## Appears in

- [VisAidMath: Benchmarking Visual-Aided Mathematical Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1719/summary.md) — Benchmarks whether multimodal models can construct visual aids for geometry problems, and finds high answer accuracy conceals near-total failure at producing or reasoning from those aids.
- [Mathematical Proof as a Litmus Test: Revealing Failure Modes of Advanced Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-582/summary.md) — Uses 200 mathematical proof problems as a diagnostic, finding some reasoning models solve under 20% and cataloguing 10 fine-grained error types that numerical benchmarks hide.
- [FinChain: A Symbolic Benchmark for Verifiable Chain-of-Thought Financial Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-662/summary.md) — A financial reasoning benchmark built from parameterized symbolic templates with executable Python, giving machine-verifiable step-level ground truth and contamination-free regeneration.
- [ErrorRadar: Benchmarking Complex Mathematical Reasoning of Multimodal Large Language Models Via Error Detection](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1217/summary.md) — Benchmarks multimodal models on detecting and categorizing errors in K-12 math solutions collected from real student interactions, with the best model about 10% behind human experts.
- [Scaling Evaluation-Time Compute with Reasoning Models as Evaluators](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2102/summary.md) — Shows evaluator accuracy improves monotonically with reasoning tokens spent, and that buying compute at evaluation time can substitute for buying it at generation time.
- [SciVQR: A Multidisciplinary Multimodal Benchmark for Advanced Scientific Reasoning Evaluation](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-28/summary.md) — A multimodal scientific reasoning benchmark over 54 subfields with domain-specific visuals and expert solutions for 46% of items, scoring the reasoning process as well as the answer.
- [Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs](../../archive/papers/2025/local-fb100130d8c7c2bd/summary.md) — Shows that base models win pass@K on mathematics by producing wrong chains that land on right answers, and that scoring the chain too — CoT-Pass@K — reverses the verdict in RLVR's favour at every K.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
