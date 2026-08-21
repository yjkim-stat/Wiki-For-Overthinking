# reasoning effort

<!-- auto:begin -->

The archive uses the term in two ways it never reconciles. As a provider-exposed setting it is a knob on how much a model is allowed to think: The Danger of Overthinking compares reasoning-effort settings across 19 models on SWE-bench Verified and finds that sampling three low-effort solutions and keeping the one with the lowest overthinking score reaches 30.3% issue resolution, above the high-effort baseline, while cutting inference cost by up to 43%. As a measured quantity it is an oversight or selection signal: TRACE truncates a chain of thought at rising fractions of its length, forces an answer at each cut, and scores the area under the reward-versus-length curve, on the premise that exploiting a reward loophole costs less reasoning than solving the task; Think Deep, Not Just Long instead measures the fraction of tokens still being revised in the network's late layers, which correlates with accuracy at mean r = 0.683 across 8 models and 4 benchmarks against -0.594 for token length. Neither measure is comparable across a model's own effort settings - the deep-thinking ratio is explicitly reported as higher at lower reasoning levels and lower accuracy - so a setting, an emitted-token count and a depth-of-computation measure all travel under the same name.

- **Kind**: concept
- **Also called**: Reasoning Effort, Reasoning effort
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [Chain-of-thought monitorability](chain-of-thought-monitorability.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](../methods/grpo.md), [HMMT 2025](../datasets/hmmt-2025.md), [Llama-3-8B](../methods/llama-3-8b.md), [Overthinking](overthinking.md), [pass@K](pass-k.md), [RLOO](../methods/rloo.md), [Self-Certainty](self-certainty.md), [Self-Consistency](../methods/self-consistency.md), [SWE-bench Verified](../datasets/swe-bench-verified.md), [Test-Time Compute Scaling](test-time-compute-scaling.md)

## Appears in

- [The Danger of Overthinking: Examining the Reasoning-Action Dilemma in Agentic Tasks](../../archive/papers/2025/local-9f60265e5ada34cb/summary.md) — Defines and measures 'overthinking' in Large Reasoning Models on real software-engineering agent tasks, showing that favoring internal reasoning over environment interaction correlates with lower SWE-bench issue-resolution rates and can be mitigated at lower cost.
- [Is it Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort](../../archive/papers/2026/title-49c61dced5ecc63a/summary.md) — TRACE detects implicit reward hacking by truncating a model's chain of thought at increasing fractions, forcing an answer at each cut, and scoring the area under the resulting reward-versus-CoT-length curve — a hacking model reaches high reward with little of its reasoning consumed.
- [Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens](../../archive/papers/2026/title-bcd9cf99a0e84a2d/summary.md) — Measures a reasoning model's inference-time effort not by how many tokens it emits but by what fraction of them are still being revised in the network's late layers, and uses that fraction to pick which of many sampled generations to keep.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
