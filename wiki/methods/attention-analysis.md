# attention analysis

<!-- auto:begin -->

Inspecting where and how strongly attention is directed in order to explain or intervene in a model's behaviour. The sources use it for three different jobs, which is what makes the term loose: to time an inference-time intervention by locating key points in a reasoning path, to diagnose a compositional performance drop alongside neuron patterns and membership inference, and to detect hallucination by measuring how well cross-step attention routing aligns with hidden-state semantic proximity. The third yields the least intuitive claim in the group — higher alignment predicts higher hallucination risk, read as a self-confirmation loop that suppresses self-auditing.

- **Kind**: method
- **Also called**: attention inspection, attention-based analysis
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 5

**Related**: [aha moment](../concepts/aha-moment.md), [AMC23](../datasets/amc23.md), [attention pattern](../concepts/attention-pattern.md), [chain of thought](chain-of-thought.md), [chain-of-thought compression](chain-of-thought-compression.md), [circuit complexity](../concepts/circuit-complexity.md), [compositional generalization](../concepts/compositional-generalization.md), [construct validity](../concepts/construct-validity.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [expressivity-learnability gap](../concepts/expressivity-learnability-gap.md), [generative rewriting](generative-rewriting.md), [gradient descent analysis](gradient-descent-analysis.md), [GSM8K](../datasets/gsm8k.md), [inference-time intervention](../concepts/inference-time-intervention.md), [jailbreak](../concepts/jailbreak.md), [length generalization](../concepts/length-generalization.md), [localization](../concepts/localization.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [membership inference](membership-inference.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [overthinking](../concepts/overthinking.md), [reasoning distillation](reasoning-distillation.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [reasoning skeleton](../concepts/reasoning-skeleton.md), [restructuring level](../concepts/restructuring-level.md), [self-training](../concepts/self-training.md), [state tracking](../concepts/state-tracking.md), [supervised finetuning](supervised-finetuning.md), [test-time compute](../concepts/test-time-compute.md), [token efficiency](../concepts/token-efficiency.md), [TokenSkip](tokenskip.md), [training dynamics](../concepts/training-dynamics.md), [verification](../concepts/verification.md)

## Appears in

- [ReasoningGuard: Safeguarding Large Reasoning Models with Inference-time Safety Aha Moments](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1453/summary.md) — An inference-time safeguard that reads a reasoning model's attention to find key points in its reasoning path and injects safety reflections there, then scales sampling to pick a safe path.
- [AgentCoMa: A Compositional Benchmark Mixing Commonsense and Mathematical Reasoning in Real-World Scenarios](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-380/summary.md) — A benchmark where each task needs one commonsense step and one math step, on which model accuracy drops nearly 30% relative to solving the steps in isolation while humans show no such gap.
- [RFS-Guard: Detecting Reasoning Hallucinations via Cross-Phase Routing Focus in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-885/summary.md) — Detects reasoning hallucinations by measuring how strongly cross-step attention routing aligns with hidden-state semantic proximity, finding that higher alignment means higher hallucination risk.
- [CRISP: Compressing Redundancy in Chain-of-Thought via Intrinsic Saliency Pruning](../../archive/papers/2026/local-39eae4c377c77302/summary.md) — Finds that the </think> token aggregates the reasoning chain in deep layers and that attention paid to it from that position ranks which steps matter, then uses that ranking to drive a four-operator compression search — cutting 58% of tokens with accuracy holding.
- [Transformers Provably Learn Chain-of-Thought Reasoning with Length Generalization](../../archive/papers/2025/local-fe69869b0e362891/summary.md) — Gives the first optimization guarantee that gradient descent trains constant-depth transformers to solve NC1-complete problems with chain of thought, and shows the algebraic structure of the task decides how far the learned reasoning extrapolates.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
