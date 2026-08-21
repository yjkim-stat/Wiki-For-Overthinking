# Accuracy-token Pareto frontier

<!-- auto:begin -->

Used by both sources as the yardstick for whether emitting a reasoning trace is worth what it costs in output tokens, with the frontier serving as the comparison surface rather than as something either paper computes in closed form. AdaThinkV makes the tradeoff per question: it estimates from matched forced-thinking and forced-no-thinking rollouts whether reasoning's accuracy gain outweighs its extra tokens, and trains a video multimodal LLM to decide accordingly. 'Reason Wide, Not Deep' moves the same point differently -- distilling a short natural-language skill from agent trajectories into a non-reasoning model's system prompt and measuring how much of the think/no-think accuracy gap it recovers at a fraction of the output tokens. Note: the archive tracks this under several near-duplicate entries that were never merged -- 'Accuracy-Efficiency Pareto Frontier', 'Accuracy-Efficiency Tradeoff', 'Accuracy-Length Tradeoff' and 'accuracy-efficiency tradeoff of reasoning length' -- and they are substantially the same idea.

- **Kind**: concept
- **Also called**: accuracy-token frontier, token-accuracy Pareto frontier
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Accuracy-Efficiency Pareto Frontier](accuracy-efficiency-pareto-frontier.md), [Accuracy-Efficiency Tradeoff](accuracy-efficiency-tradeoff.md), [Accuracy-Length Tradeoff](accuracy-length-tradeoff.md)

## Appears in

- [AdaThinkV: Adaptive Thinking for Token-Efficient Video Reasoning](../../archive/papers/2026/arxiv-2608-01980/summary.md) — AdaThinkV trains a video multimodal LLM to decide per question whether to emit an explicit reasoning trace, by estimating from matched forced-mode rollouts whether reasoning's accuracy gain outweighs its extra tokens, and by expanding rollout groups that produce no learning signal.
- [Reason Wide, Not Deep: Amortizing the Reasoning Premium into Distilled Skills](../../archive/papers/2026/arxiv-2608-07885/summary.md) — Distills a short natural-language 'skill' from an existing corpus of agent trajectories with a coding agent, injects it into a non-reasoning model's system prompt, and measures how much of the think/no-think gap it recovers at a fraction of the output tokens.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
