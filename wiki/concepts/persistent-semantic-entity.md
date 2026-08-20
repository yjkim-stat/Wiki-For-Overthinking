# persistent semantic entity

<!-- auto:begin -->

Implicit agent state that survives past the session it was created in, defined by its originating paper as a triple of name binding (behaviour registered under a string identifier), event triggering (activation through implicit runtime events rather than explicit invocation) and propagation (one trigger cascading across tool, agent and session boundaries). What distinguishes it from memory leaks or caching artifacts is that it operates at the semantic level, through names and events rather than explicit data flow, so conventional debugging does not see it -- standard logging captures 25 percent of the relevant state against 75 percent for logging that also records registry operations and event triggers. Its mechanism ablation is unusually clean: name binding alone produces 95 and 45 percent contamination on two models while every configuration without it is exactly zero, though the authors note that removing it also removes the injection vector, so it is established as necessary without being isolated as the unique lever. The second source is the same phenomenon in production infrastructure rather than in a constructed setting: encrypted reasoning blocks returned to clients are not bound to a session, user or model, so a block carrying an internalised instruction can be replayed into a different session and be treated as the model's own prior reasoning.

- **Kind**: concept
- **Also called**: PSE
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [chain of thought faithfulness](chain-of-thought-faithfulness.md), [Claude Haiku 4.5](../models/claude-haiku-4-5.md), [Claude-Sonnet-4](../models/claude-sonnet-4.md), [Claude Sonnet 4.5](../models/claude-sonnet-4-5.md), [Claude Sonnet 4.6](../models/claude-sonnet-4-6.md), [DeepSeek-V3.2](../models/deepseek-v3-2.md), [factorial ablation](../methods/factorial-ablation.md), [Gemini-2.0-flash](../models/gemini-2-0-flash.md), [Gemini-3.1-Pro](../models/gemini-3-1-pro.md), [Gemini-3.5-Flash](../models/gemini-3-5-flash.md), [GPT-4o](../models/gpt-4o.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [GPT-5](../models/gpt-5.md), [gpt-5.6-luna](../models/gpt-5-6-luna.md), [GPT-5.6-Sol](../models/gpt-5-6-sol.md), [GPT-5.6 Terra](../models/gpt-5-6-terra.md), [GPT-5-mini](../models/gpt-5-mini.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [Humanity's Last Exam](../datasets/humanity-s-last-exam.md), [knowledge distillation](../methods/knowledge-distillation.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.3-70B](../models/llama-3-3-70b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [monitorability](monitorability.md), [multi-agent pipeline](multi-agent-pipeline.md), [o4-mini](../models/o4-mini.md), [prompt injection](prompt-injection.md), [Qwen2.5-Coder-7B](../models/qwen2-5-coder-7b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-VL-235B](../models/qwen3-vl-235b.md), [ReAct](../methods/react.md), [self-verification](self-verification.md), [Wilson confidence interval](../methods/wilson-confidence-interval.md)

## Appears in

- [Persistent Semantic Entities in Tool-Augmented LLM Systems](../../archive/papers/2026/arxiv-2608-07952/summary.md) — Formalises implicit agent state that survives session boundaries as Persistent Semantic Entities defined by name binding, event triggering and propagation, and measures across 24 models that whether injected contamination decays depends on what kind of contamination it is rather than on model scale or deployment.
- [Stealing Reasoning Traces from Proprietary LLM APIs](../../archive/papers/2026/arxiv-2608-09867/summary.md) — Shows that the encrypted reasoning blocks major providers return to clients are interchangeable across sessions, users and models within a provider, and measures four consequences of that interchangeability -- distillation, third-party secret extraction, hazardous-content exposure and monitor-invisible prompt injection -- before responsible disclosure closed it.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
