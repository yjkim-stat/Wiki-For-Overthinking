# jury aggregation

<!-- auto:begin -->

Combining verdicts from several judge models rather than sampling one judge repeatedly, on the argument that different models cancel each other's biases where repeated samples of one model do not. The translation-quality work supports it directly: a jury of different reasoning models beats a jury of repeated samples from a single model and exceeds every individual member at segment level, and its inter-judge agreement is then reused as a data filter, keeping segments where the jury's scores span zero and discarding wider spreads, with the resulting annotations distilled into a 12B student that beats every open reasoning-model judge tested. The robot-plan verification work is the counterweight and is more equivocal: scaling the ensemble from one judge to seven moves aggregate accuracy only from 0.76 to 0.78, and the disaggregated picture shows what more judges actually buy -- reject-class F1 rises monotonically from 0.81 to 0.86 while accept recall falls, so the ensemble converges on refusing. Read together the sources suggest a jury's value lies in diversity of model rather than in count, and that adding members can move the operating point toward conservatism rather than improving discrimination.

- **Kind**: method
- **Also called**: judge ensemble, multi-model jury
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [Aya-expanse-8B](../models/aya-expanse-8b.md), [best-of-n](best-of-n.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [class imbalance](../concepts/class-imbalance.md), [Claude Haiku 4.5](../models/claude-haiku-4-5.md), [Claude Sonnet 4.5](../models/claude-sonnet-4-5.md), [Claude Sonnet 4.6](../models/claude-sonnet-4-6.md), [consensus](../concepts/consensus.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [GEMBA-MQM](gemba-mqm.md), [Gemini-2.0-flash](../models/gemini-2-0-flash.md), [Gemini-2.5-pro](../models/gemini-2-5-pro.md), [GPT-4](../models/gpt-4.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [GPT-4o](../models/gpt-4o.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [GPT-5.6 Terra](../models/gpt-5-6-terra.md), [GPT o3](../models/gpt-o3.md), [knowledge distillation](knowledge-distillation.md), [Llama-3-70B-Instruct](../models/llama-3-70b-instruct.md), [Llama-3-8B-Instruct](../models/llama-3-8b-instruct.md), [LLM-as-a-judge](llm-as-a-judge.md), [LoRA](lora.md), [macro versus micro accuracy](../concepts/macro-versus-micro-accuracy.md), [multi-agent pipeline](../concepts/multi-agent-pipeline.md), [o4-mini](../models/o4-mini.md), [persona conditioning](persona-conditioning.md), [prompt injection](../concepts/prompt-injection.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [retrieval-augmented generation](retrieval-augmented-generation.md), [self-consistency](self-consistency.md), [supervised fine-tuning](supervised-fine-tuning.md), [test-time scaling](../concepts/test-time-scaling.md), [WMT22](../datasets/wmt22.md)

## Appears in

- [TQLite: Multi-LLM Jury Guided Distillation for Real-time MQM Translation Quality Evaluation](../../archive/papers/2026/arxiv-2608-02975/summary.md) — Benchmarks 20-plus models as MQM translation-quality judges, finds reasoning models best and a jury of different ones better than any member, then distils that jury's agreement-filtered annotations into a 12B student that beats every open reasoning-model judge tested.
- [Agentic Harnesses: LLM-Driven Verification Layers for Robot Autonomy](../../archive/papers/2026/arxiv-2608-09857/summary.md) — Puts an ensemble of LLM judges between a robot-autonomy planner and its execution layer as gating middleware that accepts, rejects or escalates each plan to human review, and reports that ensemble size barely moves accuracy while the errors concentrate at the escalate boundary rather than between accept and reject.
- [Social Chain of Thought: A Multi-Agent Architecture Grounded in Medical Differential Diagnosis Methodology](../../archive/papers/2026/arxiv-2608-11420/summary.md) — Structures multi-agent medical differential diagnosis as rounds of persona-conditioned specialist deliberation, and shows the recall advantage is not reproduced by best-of-n sampling from the same model, concentrates entirely in the cases where monolithic inference fails, and reverses on the easiest quartile.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
