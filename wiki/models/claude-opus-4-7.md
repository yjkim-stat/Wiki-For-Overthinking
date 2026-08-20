# Claude Opus 4.7

<!-- auto:begin -->

A Claude model appearing twice in this archive, and in one of those appearances it is one of only two models exhibiting a behaviour the other four do not. In the steering-pressure study it is one of two frontier models that openly resist instructions to suppress values reasoning -- and the two do so in statistically distinguishable ways, one challenging the instruction while complying and the other refusing the framing outright -- while also leading the field on refusing a compromised framing with a values-consistent alternative at 91 percent, against 12 percent for the lowest model in the same evaluation. It appears again among the general-purpose models evaluated as autoformalisers, where frontier models preserve invalidity better than specialised fine-tuned systems. Neither source describes the model itself; its interest here is as evidence that non-compliance modes are developer-specific rather than general.

- **Kind**: model
- **Also called**: Claude Opus 4.7
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [abstention](../concepts/abstention.md), [activation steering](../methods/activation-steering.md), [benchmark design](../concepts/benchmark-design.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [Cohen's kappa](../methods/cohen-s-kappa.md), [construct validity](../concepts/construct-validity.md), [DeepSeek](deepseek.md), [detection versus control](../concepts/detection-versus-control.md), [difference-in-means direction](../methods/difference-in-means-direction.md), [formal verification](../methods/formal-verification.md), [GPT-5](gpt-5.md), [IFEval](../datasets/ifeval.md), [jury aggregation](../methods/jury-aggregation.md), [linear probe](../methods/linear-probe.md), [Llama-3.2-1B-Instruct](llama-3-2-1b-instruct.md), [Llama-3.3-70B-Instruct](llama-3-3-70b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH](../datasets/math.md), [monitorability](../concepts/monitorability.md), [nested cross-validation](../methods/nested-cross-validation.md), [OlympiadBench](../datasets/olympiadbench.md), [outcome reward](../concepts/outcome-reward.md), [permutation test](../methods/permutation-test.md), [position bias](../concepts/position-bias.md), [Qwen](qwen.md), [reward hacking](../concepts/reward-hacking.md), [selectivity control](../methods/selectivity-control.md), [steering vector](../methods/steering-vector.md), [sycophancy](../concepts/sycophancy.md), [verification](../concepts/verification.md)

## Appears in

- [Divergent Response Modes in Frontier Language Models Under Steering Pressure](../../archive/papers/2026/arxiv-2608-06578/summary.md) — Measures not how far six frontier models move under steering pressure but what kind of response they give when they decline, finds several response modes belonging to a single model, and then traces the largest within-model split to a linearly decodable and causally steerable direction in an open-weight model's residual stream.
- [FaithformBench: Benchmarking Faithfulness of Mathematical Chain-of-Thought Autoformalisation](../../archive/papers/2026/arxiv-2608-10916/summary.md) — Tests whether systems that translate natural-language reasoning steps into Lean preserve invalidity as well as validity, by automatically perturbing steps to make them wrong, and finds pervasive silent correction -- with the systems best at preserving valid inputs the most likely to repair invalid ones.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
