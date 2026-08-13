# gpt-oss-120b

<!-- auto:begin -->

A large open-weight reasoning model, used by both sources as the strong open baseline against which a task's difficulty is calibrated. One includes it among five models in an observability sweep, where the question is what a monitor can read rather than what the model scores. The other reports it alongside GPT-5 as showing promise while solve rates stay below 5% on its hard instances even under expensive scaling — the sense in which a benchmark is established as unsaturated. Its function here is to mark where the open frontier sits when a result needs that context.

- **Kind**: model
- **Also called**: GPT-OSS-120B
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [activation steering](../methods/activation-steering.md), [AIME](../datasets/aime.md), [backtracking](../concepts/backtracking.md), [benchmark contamination](../concepts/benchmark-contamination.md), [causal intervention](../concepts/causal-intervention.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [compositional generalization](../concepts/compositional-generalization.md), [construct validity](../concepts/construct-validity.md), [contrastive activation addition](../methods/contrastive-activation-addition.md), [DAPO](../methods/dapo.md), [DAPO-Math-17k](../datasets/dapo-math-17k.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [entropy collapse](../concepts/entropy-collapse.md), [exploration](../concepts/exploration.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-5](gpt-5.md), [gpt-oss-20b](gpt-oss-20b.md), [linear probe](../methods/linear-probe.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [long chain-of-thought distillation](../methods/long-chain-of-thought-distillation.md), [MMLU](../datasets/mmlu.md), [MMLU-Pro](../datasets/mmlu-pro.md), [monitorability](../concepts/monitorability.md), [Omni-MATH](../datasets/omni-math.md), [pass@k](../methods/pass-k.md), [policy entropy](../concepts/policy-entropy.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-4B](qwen3-4b.md), [Qwen3-8B](qwen3-8b.md), [Qwen3-8B-Base](qwen3-8b-base.md), [QwQ-32B](qwq-32b.md), [reasoning boundary](../concepts/reasoning-boundary.md), [RLVR](../methods/rlvr.md), [safety alignment](../concepts/safety-alignment.md), [self-correction](../concepts/self-correction.md), [self-repair](../concepts/self-repair.md), [steering vector](../methods/steering-vector.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time compute](../concepts/test-time-compute.md), [trajectory diversity](../concepts/trajectory-diversity.md), [verbosity](../concepts/verbosity.md)

## Appears in

- [How Much Does a Reasoning Summary Reveal? An Observability Ladder for Large Language Models](../../archive/papers/2026/arxiv-2608-02089/summary.md) — Holds one completed reasoning run fixed and varies only what a monitor is allowed to inspect — response, self-summary, full trace, internals — and finds the summary's value nearly vanishes once the monitor already has the prompt, so monitorability is a property of the display and the reader jointly rather than of the text.
- [BODHI: Do LLMs Branch Out and Discover Heterogeneous Inferences?](../../archive/papers/2026/arxiv-2608-02867/summary.md) — Builds prefix trees of semantically equivalent reasoning statements and measures how RLVR changes a model's preference between branches, finding the entropy collapse is not stylistic — the collapse is stronger for semantically distinct continuations than for syntactic variants of the same statement.
- [Risky Business: Measuring The Faithfulness-Safety Tension](../../archive/papers/2026/arxiv-2608-03745/summary.md) — Tampers with a model's own reasoning trace in two directions — toward an equivalent safe option and toward an unsafe one — and finds the models that follow their traces most faithfully are the ones that follow them into harm, with the two behaviours carried by two distinct, anti-correlated residual-stream directions that can be steered apart.
- [PBEBench: A Multi-Step Programming by Examples Reasoning Benchmark inspired by Historical Linguistics](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-432/summary.md) — An inductive-reasoning benchmark from historical linguistics that requires inducing cascades of string-rewrite programs, with automated contamination-resistant generation and controllable difficulty.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
