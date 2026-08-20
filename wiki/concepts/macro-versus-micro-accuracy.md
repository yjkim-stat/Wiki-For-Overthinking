# macro versus micro accuracy

<!-- auto:begin -->

Whether a summary score weights each example equally (micro) or each class or category equally (macro), and in both sources here the choice changes the ranking rather than merely the number. On the industrial-safety benchmark, a fine-tuned 9B model takes the highest micro accuracy at 89.0 percent, slightly above the strongest frontier model's 88.7, while that frontier model's sibling takes the best macro at 89.5 against the fine-tuned model's 88.7 -- so the fine-tuned system is the best overall and the least uniform across categories, and reporting one number would have concealed which. In the robot-plan verification work the divergence is sharper: weighted metrics favour the seven-judge ensemble while macro-F1, which weights each decision class equally regardless of its support, peaks at three judges, and the paper takes that as the argument for the smaller ensemble. Neither source treats the distinction as a subject; between them they establish the practical rule, that where class support is unequal the two orderings are different claims and a paper reporting only the support-weighted one has not shown that its system is good at the rare class.

- **Kind**: concept
- **Also called**: macro-F1 versus micro-F1
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [benchmark contamination](benchmark-contamination.md), [benchmark design](benchmark-design.md), [calibration](calibration.md), [chain-of-thought distillation](../methods/chain-of-thought-distillation.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [class imbalance](class-imbalance.md), [Claude Sonnet 4.5](../models/claude-sonnet-4-5.md), [decontamination](../methods/decontamination.md), [Gemini-3.1-Pro](../models/gemini-3-1-pro.md), [Gemini-3.5-Flash](../models/gemini-3-5-flash.md), [GPT-5.5](../models/gpt-5-5.md), [GPT-5.6-Sol](../models/gpt-5-6-sol.md), [GPT-5.6 Terra](../models/gpt-5-6-terra.md), [GPT o3](../models/gpt-o3.md), [jury aggregation](../methods/jury-aggregation.md), [Kimi-K2.6](../models/kimi-k2-6.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [multi-hop reasoning](multi-hop-reasoning.md), [multiple-choice evaluation](../methods/multiple-choice-evaluation.md), [position bias](position-bias.md), [prompt injection](prompt-injection.md), [Qwen3.5-9B](../models/qwen3-5-9b.md), [Qwen3.6-27B](../models/qwen3-6-27b.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [self-consistency](../methods/self-consistency.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md)

## Appears in

- [SafeSceneReason: A Multimodal Reasoning Benchmark Connecting Industrial Hazards with Accident Knowledge](../../archive/papers/2026/arxiv-2608-09230/summary.md) — Builds an industrial-safety reasoning benchmark from two pipelines -- program execution over safety scene graphs, and evidence graphs extracted from real accident-investigation reports -- and shows that general multimodal capability does not transfer to it while a 9B model fine-tuned on its chain-of-thought split matches frontier systems.
- [Agentic Harnesses: LLM-Driven Verification Layers for Robot Autonomy](../../archive/papers/2026/arxiv-2608-09857/summary.md) — Puts an ensemble of LLM judges between a robot-autonomy planner and its execution layer as gating middleware that accepts, rejects or escalates each plan to human review, and reports that ensemble size barely moves accuracy while the errors concentrate at the escalate boundary rather than between accept and reject.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
