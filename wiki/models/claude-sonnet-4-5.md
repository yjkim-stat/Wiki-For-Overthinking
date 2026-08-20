# Claude Sonnet 4.5

<!-- auto:begin -->

A mid-sized Claude model used in this archive in two applied settings, neither of which studies it. It is one of the judge models in a robot-autonomy verification ensemble that gates plans before execution, where the reported finding is about ensemble size rather than about any member -- accuracy stays within 0.76 to 0.78 from one judge to seven. It also appears in the reasoning-trace extraction work as one of the Claude-family models whose encrypted reasoning blocks were found replayable into other models of the family, and, in the injection-scheme map, as one of the 4.5-generation models that accepts a thought placed in the current assistant turn. Nothing in either source characterises the model itself.

- **Kind**: model
- **Also called**: Claude Sonnet 4.5
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [class imbalance](../concepts/class-imbalance.md), [Claude Haiku 4.5](claude-haiku-4-5.md), [Claude Sonnet 4.6](claude-sonnet-4-6.md), [Gemini-3.1-Pro](gemini-3-1-pro.md), [Gemini-3.5-Flash](gemini-3-5-flash.md), [GPT-5](gpt-5.md), [gpt-5.6-luna](gpt-5-6-luna.md), [GPT-5.6-Sol](gpt-5-6-sol.md), [GPT-5.6 Terra](gpt-5-6-terra.md), [GPT-5-mini](gpt-5-mini.md), [GPT o3](gpt-o3.md), [Humanity's Last Exam](../datasets/humanity-s-last-exam.md), [jury aggregation](../concepts/jury-aggregation.md), [knowledge distillation](../methods/knowledge-distillation.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [macro versus micro accuracy](../concepts/macro-versus-micro-accuracy.md), [monitorability](../concepts/monitorability.md), [o4-mini](o4-mini.md), [persistent semantic entity](../concepts/persistent-semantic-entity.md), [prompt injection](../methods/prompt-injection.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [self-consistency](../methods/self-consistency.md)

## Appears in

- [Agentic Harnesses: LLM-Driven Verification Layers for Robot Autonomy](../../archive/papers/2026/arxiv-2608-09857/summary.md) — Puts an ensemble of LLM judges between a robot-autonomy planner and its execution layer as gating middleware that accepts, rejects or escalates each plan to human review, and reports that ensemble size barely moves accuracy while the errors concentrate at the escalate boundary rather than between accept and reject.
- [Stealing Reasoning Traces from Proprietary LLM APIs](../../archive/papers/2026/arxiv-2608-09867/summary.md) — Shows that the encrypted reasoning blocks major providers return to clients are interchangeable across sessions, users and models within a provider, and measures four consequences of that interchangeability -- distillation, third-party secret extraction, hazardous-content exposure and monitor-invisible prompt injection -- before responsible disclosure closed it.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
