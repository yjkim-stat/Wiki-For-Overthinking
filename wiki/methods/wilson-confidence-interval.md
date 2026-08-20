# Wilson confidence interval

<!-- auto:begin -->

A confidence interval for a binomial proportion that stays inside [0,1] and behaves sensibly at small counts and extreme rates, where the normal approximation does not. Both sources use it for the same purpose, which is to stop a small-sample proportion from being read as a ranking. The agent-contamination work reports every rate with a Wilson interval and leans on them to state what its data cannot support -- a persistence rate of 10/10 at turn 10 carries the interval [0.72, 1.00] and a 0/10 rate carries [0, 0.28], which is why the paper claims neither unbounded persistence nor cross-family generality. The ARC work uses them the same way and is explicit that ten tasks per concept family gives a profile rather than a reliable ranking, since the intervals for 9/10 and 2/10 overlap broadly (59.6-98.2 percent against 5.7-51.0). Neither source studies the estimator; between them they establish the practice the archive should expect, which is that a proportion measured on tens of items is reported with its interval or not reported as a comparison.

- **Kind**: method
- **Also called**: Wilson score interval
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [bootstrap confidence intervals](bootstrap-confidence-intervals.md), [Coconut](coconut.md), [compositional generalization](../concepts/compositional-generalization.md), [DeepSeek-V3.2](../models/deepseek-v3-2.md), [factorial ablation](factorial-ablation.md), [Gemini-2.0-flash](../models/gemini-2-0-flash.md), [GPT-4o](../models/gpt-4o.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [implicit chain of thought](../concepts/implicit-chain-of-thought.md), [in-context learning](../concepts/in-context-learning.md), [latent reasoning](../concepts/latent-reasoning.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.3-70B](../models/llama-3-3-70b.md), [LLM-as-a-judge](llm-as-a-judge.md), [monitorability](../concepts/monitorability.md), [multi-agent pipeline](../concepts/multi-agent-pipeline.md), [pass@k](../concepts/pass-k.md), [persistent semantic entity](../concepts/persistent-semantic-entity.md), [prompt injection](../concepts/prompt-injection.md), [Qwen2.5-coder-7B](../models/qwen2-5-coder-7b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-VL-235B](../models/qwen3-vl-235b.md), [ReAct](react.md), [recurrent depth](../concepts/recurrent-depth.md), [self-verification](../concepts/self-verification.md), [test-time scaling](../concepts/test-time-scaling.md)

## Appears in

- [Persistent Semantic Entities in Tool-Augmented LLM Systems](../../archive/papers/2026/arxiv-2608-07952/summary.md) — Formalises implicit agent state that survives session boundaries as Persistent Semantic Entities defined by name binding, event triggering and propagation, and measures across 24 models that whether injected contamination decays depends on what kind of contamination it is rather than on model scale or deployment.
- [BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](../../archive/papers/2026/arxiv-2608-09888/summary.md) — Combines in-context learning through evolving recurrent memory with iterative reasoning in a continuous latent workspace that is never decoded into language, reaching 29.5% pass@2 on public ARC-AGI-1 at $0.0007 per task from 150M parameters, and then probes with controlled tasks what the resulting demonstration-bound operators can and cannot do.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
